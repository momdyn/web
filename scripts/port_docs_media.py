#!/usr/bin/env python3
"""One-time port of the docs images from the old Sphinx project into docs-src/.

Usage:
    python3 scripts/port_docs_media.py /path/to/old-momdyn/docs

For every image a page in docs-src/ references (`.. image:: path` with an optional `:width:`), this finds the
original in the old docs folder and writes optimized siblings next to the page's expected path:
  * PNG / JPG -> <stem>.webp, resized to twice the widest width it is displayed at (retina), capped at 1200px
  * GIF       -> <stem>.mp4 and <stem>.webm (muted loop videos) plus <stem>.webp (poster frame)
The .rst files keep their original image paths. The build picks the optimized file with the same stem.
The originals are NOT copied: they stay in the old repos (the screenshots will be reshot later).
"""
import pathlib
import re
import subprocess
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "docs-src"
CAP = 1200


def refs():
    """(absolute image path under docs-src, widest displayed width or None)"""
    found = {}
    for rst in SRC.rglob("*.rst"):
        lines = rst.read_text().split("\n")
        for i, line in enumerate(lines):
            m = re.match(r"\s*\.\. image:: (\S+)", line)
            if not m:
                continue
            width = None
            for nxt in lines[i + 1:i + 6]:
                w = re.match(r"\s+:width:\s*(\d+)", nxt)
                if w:
                    width = int(w.group(1))
                if nxt.strip() and not nxt.strip().startswith(":"):
                    break
            target = (rst.parent / m.group(1)).resolve()
            prev = found.get(target)
            found[target] = max(filter(None, [prev, width]), default=None) if (prev or width) else None
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    old = pathlib.Path(sys.argv[1]).resolve()
    done = missing = 0
    before = after = 0
    for target, width in sorted(refs().items()):
        rel = target.relative_to(SRC.resolve())
        orig = old / rel
        if not orig.exists():
            print(f"MISSING original: {rel}"); missing += 1; continue
        out = SRC / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        before += orig.stat().st_size
        if orig.suffix.lower() == ".gif":
            w = min(CAP, (width or 400) * 2)
            vf = f"scale='min({w},iw)':-2,format=yuv420p"
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(orig), "-an", "-vf", vf, "-c:v", "libx264",
                            "-crf", "30", "-preset", "slow", "-movflags", "+faststart", str(out.with_suffix(".mp4"))], check=True)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(orig), "-an", "-vf", vf, "-c:v", "libvpx-vp9",
                            "-crf", "40", "-b:v", "0", str(out.with_suffix(".webm"))], check=True)
            im = Image.open(orig); im.seek(0); im = im.convert("RGB")
            im.thumbnail((w, w * 4)); im.save(out.with_suffix(".webp"), quality=80, method=6)
            after += sum(out.with_suffix(s).stat().st_size for s in (".mp4", ".webm", ".webp"))
        else:
            im = Image.open(orig)
            im = im.convert("RGBA") if im.mode in ("RGBA", "LA", "P") else im.convert("RGB")
            w = min(CAP, (width * 2) if width else im.width)
            if im.width > w:
                im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
            im.save(out.with_suffix(".webp"), quality=82, method=6)
            after += out.with_suffix(".webp").stat().st_size
        done += 1
    print(f"Ported {done} images ({missing} missing): {before/1e6:.1f} MB originals -> {after/1e6:.1f} MB optimized")


if __name__ == "__main__":
    main()
