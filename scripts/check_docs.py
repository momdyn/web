#!/usr/bin/env python3
"""Crawl the built site (index.html, privacy.html, terms.html, docs/**) and report problems.

Usage:  python3 scripts/check_docs.py        (exit code 1 if anything is wrong)

Checks: every internal link and image/video file exists, every #fragment matches an id on the target page, meta descriptions
(present, unique, 120-155 characters, no ellipsis, same text in og:description), titles, one h1, JSON-LD parses, alt text on
images, banned strings (Android, Google Play, old contact address, Facebook, ...), canonical URLs, sitemap coverage.
"""
import collections
import html
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
SITE = "https://momdyn.dc-engineer.com"
BANNED = ["android", "google play", "play.google", "mobilemultibodydynamics@gmail.com", "buymeacoffee", "facebook.com", "momdyn.com/",
          "channel/UC7ij1ezmh8a3Q7N3gF4zUkQ", "momdyn.github.io/html"]
GENERIC_ALT = {"classic menu", "header", "", "image"}

pages = {}
for f in [ROOT / "index.html", ROOT / "privacy.html", ROOT / "terms.html"] + sorted((ROOT / "docs").rglob("*.html")):
    if "pagefind" in f.parts:
        continue
    url = "/" + f.relative_to(ROOT).as_posix()
    url = re.sub(r"index\.html$", "", url)
    pages[url] = f.read_text()
ids = {u: set(re.findall(r'\bid="([^"]+)"', t)) for u, t in pages.items()}
errors, fixes = [], []


def target_for(base, href):
    href, _, frag = href.partition("#")
    if not href:
        return base, frag
    path = urllib.parse.urlparse(urllib.parse.urljoin(base, href)).path
    return path, frag


def exists(path):
    p = ROOT / path.lstrip("/")
    return p.is_file() or (p / "index.html").is_file()


descs = collections.defaultdict(list)
KNOWN_PLACEHOLDERS = {"media/hero.mp4", "media/hero.webm"}  # landing page videos still to be supplied by the owner
n_links = n_frags = 0
for url, text in pages.items():
    docs = url.startswith("/docs")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for m in re.finditer(r'\b(?:href|src|poster)="([^"]+)"', text):
        h = html.unescape(m.group(1))
        if re.match(r"^(https?:|mailto:|tel:|data:|javascript:)", h):
            continue
        path, frag = target_for(url, h)
        n_links += 1
        n_frags += bool(frag)
        if path.lstrip("/") in KNOWN_PLACEHOLDERS:
            continue
        if not exists(path) and path not in pages:
            errors.append(f"{url}: broken link/file {h}")
            continue
        if frag:
            tgt = path if path in pages else path.rstrip("/") + "/"
            if tgt not in ids and (path + "/") in ids:
                tgt = path + "/"
            if tgt in ids and frag not in ids[tgt]:
                errors.append(f"{url}: broken anchor {h}")
    low = text.lower()
    for b in BANNED:
        if b.lower() in low and not (url == "/privacy.html" and b == "momdyn.github.io/html"):
            errors.append(f"{url}: contains banned text {b!r}")
    for im in re.finditer(r"<img [^>]*>", text):
        alt = re.search(r'alt="([^"]*)"', im.group(0))
        if alt is None or alt.group(1).strip().lower() in GENERIC_ALT:
            errors.append(f"{url}: image without a meaningful alt: {im.group(0)[:90]}")
    if docs:
        d = re.search(r'<meta name="description" content="([^"]*)"', text)
        og = re.search(r'<meta property="og:description" content="([^"]*)"', text)
        t = re.search(r"<title>(.*?)</title>", text, re.S)
        if not d:
            errors.append(f"{url}: no meta description")
        else:
            desc = html.unescape(d.group(1))
            descs[desc].append(url)
            if not 120 <= len(desc) <= 155:
                errors.append(f"{url}: description is {len(desc)} characters")
            if desc.endswith(("...", "…")) or "…" in desc:
                errors.append(f"{url}: description has an ellipsis")
            if not og or og.group(1) != d.group(1):
                errors.append(f"{url}: og:description differs from the meta description")
        if not t or len(html.unescape(t.group(1))) > 75:
            errors.append(f"{url}: title missing or over 75 characters")
        if text.count("<h1") != 1:
            errors.append(f"{url}: expected one h1, found {text.count('<h1')}")
        can = re.search(r'<link rel="canonical" href="([^"]+)"', text)
        if not can or can.group(1) != SITE + url:
            errors.append(f"{url}: canonical is {can.group(1) if can else None}")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
            try:
                json.loads(block)
            except ValueError as e:
                errors.append(f"{url}: invalid JSON-LD: {e}")
        if "BreadcrumbList" not in text:
            errors.append(f"{url}: no BreadcrumbList")
for desc, urls in descs.items():
    if len(urls) > 1:
        errors.append(f"duplicate description on {urls}")
sm = (ROOT / "sitemap.xml").read_text()
for url in pages:
    if url.startswith("/docs") and SITE + url not in sm:
        errors.append(f"{url}: missing from sitemap.xml")
if "Sitemap:" not in (ROOT / "robots.txt").read_text():
    errors.append("robots.txt does not reference the sitemap")

print(f"Checked {len(pages)} pages, {n_links} internal links/files, {n_frags} with a #fragment.")
for e in errors:
    print("ERROR:", e)
print("OK: no problems" if not errors else f"{len(errors)} problem(s)")
sys.exit(1 if errors else 0)
