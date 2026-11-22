#!/usr/bin/env python3
"""Generate the docs reference pages (docs-src/<group>/<component>.rst) from the Mechanism module.

The reference pages are the docstrings of the `create_*` methods of the `Mechanism` class, the same text
the iOS app shows as in-app component help. The module is read STATICALLY (with `ast`): it is never
imported or executed, so this needs no sympy and no access to the module's dependencies.

Usage:
    python3 scripts/gen_reference.py /path/to/mechanism/mechanism/mechanism.py

The component list and grouping mirror the app (Data.swift: classic_items, joints_items, ...).
Output pages are committed, so building the site does not need the module. Do not edit them by hand;
change the docstring in the Mechanism module and run this script again.
"""
import ast
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from reference_meta import M, NOUN, UNITS_NOTE, generic_desc, generic_unit  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs-src"

# group -> [(page title, create_* method)]   (same order as the app's menus)
GROUPS = {
    "classic": [
        ("Parameter", "create_param"), ("Generalized Coordinate", "create_coord"),
        ("Generalized Speed", "create_speed"), ("Frame", "create_frame"),
        ("Vector", "create_vector"), ("Point", "create_point"),
    ],
    "joints": [
        ("Rigid Translation", "create_rigid_translation"), ("Rigid Rotation", "create_rigid_rotation"),
        ("Prismatic", "create_prismatic_joint"), ("Revolute", "create_revolute_joint"),
        ("Universal", "create_universal_joint"), ("Spherical", "create_spherical_joint"),
        ("Planar", "create_planar_joint"), ("Free Motion", "create_free_motion_joint"),
        ("Cylindrical", "create_cylindrical_joint"),
    ],
    "bodies": [
        ("Particle", "create_particle"), ("Rigid Body Box", "create_body_box"),
        ("Rigid Body Cylinder", "create_body_cylinder"), ("Rigid Body Cone", "create_body_cone"),
        ("General Rigid Body", "create_general_rigid_body"),
    ],
    "loads": [
        ("External Force", "create_external_force"), ("Actuated Force", "create_actuated_force"),
        ("External Moment", "create_external_moment"), ("Actuated Moment", "create_actuated_moment"),
        ("Translational Spring", "create_translational_spring_damper"),
        ("Rotational Spring", "create_rotational_spring_damper"),
    ],
    "sensors": [
        ("Position Sensor", "create_position_sensor"), ("Velocity Sensor", "create_velocity_sensor"),
        ("Accelerometer", "create_accelerometer"), ("DCM Sensor", "create_dcm_sensor"),
        ("Rate Gyro", "create_rate_gyro"),
    ],
}


def slug(title):
    return re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")


def parse_docstring(doc):
    """Split a docstring into params {name: (type, text)}. Fields look like ':param str name: text', or
    ':param name: text' followed by ':type name: str or numeric'."""
    fields, cur = [], None
    for line in doc.split("\n"):
        m = re.match(r"^:(param|type|return|returns)\b([^:]*):\s*(.*)$", line)
        if m:
            cur = {"kind": m.group(1), "head": m.group(2).strip(), "text": m.group(3).strip()}
            fields.append(cur)
        elif cur is not None and line.strip():
            cur["text"] += " " + line.strip()
    params, types = {}, {}
    for f in fields:
        if f["kind"] == "param":
            parts = f["head"].split()
            params[parts[-1]] = [" ".join(parts[:-1]), f["text"]]
        elif f["kind"] == "type":
            types[f["head"].strip()] = f["text"]
    for name, p in params.items():
        if not p[0] and name in types:
            p[0] = types[name]
    return params


def inline(text):
    """The notes are written with `code` and [text](page.html) markers; convert them to reStructuredText."""
    out, pos = [], 0
    for m in re.finditer(r"`([^`]+)`|\[([^\]]+)\]\(([^)]+)\)", text):
        out.append(text[pos:m.start()].replace("_", "\\_").replace("*", "\\*"))
        out.append(f"``{m.group(1)}``" if m.group(1) else f"`{m.group(2)} <{m.group(3)}>`__")
        pos = m.end()
    out.append(text[pos:].replace("_", "\\_").replace("*", "\\*"))
    res = "".join(out)
    return re.sub(r"^TODO:", "**TODO:**", res)


def signature(fn):
    names = [a.arg for a in fn.args.args][1:]
    defs = [None] * (len(names) - len(fn.args.defaults)) + list(fn.args.defaults)
    return [(n, ast.unparse(d) if d is not None else "") for n, d in zip(names, defs)]


def param_rows(method, sig, doc_params, meta):
    rows, todo = [], []
    for name, default in sig:
        typ, text = doc_params.get(name, ["", ""])
        if not typ:
            typ = "str" if default.startswith(("'", '"')) or default == "None" else ("bool" if default in ("True", "False") else "numeric")
        if not text:
            text = generic_desc(name) or "TODO"
        if text == "TODO":
            todo.append(f"{method}.{name}: description")
        unit = meta["units"].get(name) or generic_unit(name)
        if unit is None:
            numeric = "numeric" in typ and "str" not in typ
            unit = "TODO" if numeric else "—"
            if unit == "TODO":
                todo.append(f"{method}.{name}: units")
        rows.append(f"   {name} | {typ} | {default or 'required'} | {unit} | {text}")
    return rows, todo


def title_tag(group, title):
    noun = NOUN[group]
    if group == "joints" and noun.lower() not in title.lower():
        title = f"{title} {noun}"
    if title == "Rate Gyro":
        title = "Rate Gyro Sensor"
    return f"{title} \u2013 Multibody Dynamics Reference | MOMDYN"


def render(group, title, method, sig, doc_params):
    meta = M[method]
    rows, todo = param_rows(method, sig, doc_params, meta)
    if len(meta["desc"]) < 120 or len(meta["desc"]) > 155:
        print(f"WARNING: {method} description is {len(meta['desc'])} characters")
    out = [f".. GENERATED by scripts/gen_reference.py from Mechanism.{method}() and scripts/reference_meta.py. Do not edit by hand.", "",
           ".. seo::", f"   :title: {title_tag(group, title)}", f"   :description: {meta['desc']}", "   :type: techarticle", "",
           title, "=" * len(title), "", meta["definition"], ""]
    if meta["figure"]:
        out += [f".. image:: ../{meta['figure']}", "   :width: 400", f"   :alt: {meta['figure_alt']}", ""]
    else:
        out += [f".. diagram:: {meta['figure_alt']}", ""]
    out += ["Parameters", "----------", "", UNITS_NOTE, "", ".. params::", ""] + rows + [""]
    if meta["equations"]:
        out += ["Equations", "---------", ""]
        for caption, tex in meta["equations"]:
            out += [inline(caption), "", ".. math::", "", f"   {tex}", ""]
    out += ["Sign conventions & notes", "------------------------", ""]
    out += [f"* {inline(n)}" for n in meta["notes"]] + [""]
    out += ["Related", "-------", ""]
    for target, label in meta["related"]:
        same = target.split("/")[0] == group
        href = f"{target.split('/')[1]}.html" if same else f"../{target}.html"
        out.append(f"* `{label} <{href}>`__")
    return "\n".join(out).rstrip() + "\n", todo


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    if src.is_dir():
        src = src / "mechanism" / "mechanism.py"
    tree = ast.parse(src.read_text())
    fns = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "Mechanism":
            for f in node.body:
                if isinstance(f, ast.FunctionDef) and f.name.startswith("create_"):
                    fns[f.name] = f
    n, todos = 0, []
    for group, items in GROUPS.items():
        (OUT / group).mkdir(parents=True, exist_ok=True)
        index = (OUT / f"{group}.rst").read_text() if (OUT / f"{group}.rst").exists() else ""
        for title, method in items:
            fn = fns.get(method)
            if fn is None or method not in M:
                print(f"WARNING: {method} missing in the module or in reference_meta.py, page skipped"); continue
            text, todo = render(group, title, method, signature(fn), parse_docstring(ast.get_docstring(fn) or ""))
            (OUT / group / f"{slug(title)}.rst").write_text(text)
            todos += todo
            n += 1
            if f"{group}/{slug(title)}" not in index:
                print(f"WARNING: docs-src/{group}.rst does not list {group}/{slug(title)} in its toctree")
    (OUT / "_todo_report.txt").write_text("\n".join(todos) + "\n")
    print(f"Generated {n} reference pages from {src}; {len(todos)} table cells marked TODO (see docs-src/_todo_report.txt)")


if __name__ == "__main__":
    main()
