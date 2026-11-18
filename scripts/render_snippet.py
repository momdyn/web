#!/usr/bin/env python3
"""Re-highlight media/export-snippet.py into index.html.

Usage (from the repo root):  python3 scripts/render_snippet.py
Needs:  pip install pygments

It replaces everything between <!-- SNIPPET:START --> and <!-- SNIPPET:END -->
with the highlighted code. No JavaScript runs on the site for this.
"""
import html
import pathlib
import re

from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

root = pathlib.Path(__file__).resolve().parent.parent
code = (root / "media" / "export-snippet.py").read_text().rstrip("\n")

# Token type -> short CSS class (defined in styles.css as .tok-*)
CLASSES = {
    Token.Comment: "tok-c1",
    Token.Keyword: "tok-k",
    Token.Operator.Word: "tok-ow",
    Token.Name.Builtin: "tok-nb",
    Token.Name.Function: "tok-nf",
    Token.Literal.Number: "tok-mf",
    Token.Literal.String: "tok-s",
}


def css_class(tok):
    while tok is not Token:
        if tok in CLASSES:
            return CLASSES[tok]
        tok = tok.parent
    return None


out = []
for tok, text in lex(code, PythonLexer()):
    cls = css_class(tok)
    escaped = html.escape(text, quote=False)
    out.append(f'<span class="{cls}">{escaped}</span>' if cls else escaped)

page = root / "index.html"
src = page.read_text()
new = re.sub(
    r"(<!-- SNIPPET:START -->).*?(<!-- SNIPPET:END -->)",
    lambda m: m.group(1) + "".join(out) + "\n" + m.group(2),
    src,
    flags=re.S,
)
page.write_text(new)
print(f"Rendered {len(code.splitlines())} lines into index.html")
