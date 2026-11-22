#!/usr/bin/env python3
"""Turn a Blender render with a dark, partly opaque backdrop into a transparent icon that keeps its soft ground shadow.

Usage:  python3 scripts/icon_alpha.py render.webp out.webp [strength=0.6] [size=640]

The render's backdrop is black with a constant alpha (the unshadowed ground) that rises where the icon shadows it.
This script
  1. measures the unshadowed ground alpha (the baseline) and the local ground alpha under and around the object,
  2. recovers how much of each edge pixel is the object (coverage),
  3. makes the lit ground fully transparent, and turns the extra darkening into a black shadow of alpha = shadow * strength,
  4. crops to the content (square, small margin) and resizes.
Needs: pip install pillow numpy scipy
"""
import sys

import numpy as np
from PIL import Image
from scipy import ndimage as ndi

src, dst = sys.argv[1], sys.argv[2]
STRENGTH = float(sys.argv[3]) if len(sys.argv) > 3 else 0.6
SIZE = int(sys.argv[4]) if len(sys.argv) > 4 else 640

a = np.array(Image.open(src).convert("RGBA")).astype(float)
col, al = a[..., :3] / 255, a[..., 3] / 255
bg = (a[..., :3].sum(-1) == 0) & (al < 0.999)                       # pure black, not fully opaque: backdrop or shadow
idx = ndi.distance_transform_edt(~bg, return_distances=False, return_indices=True)
ab = al[idx[0], idx[1]]                                            # backdrop alpha nearest to each pixel (extends under the object)
b0 = np.percentile(al[bg], 2)                                      # unshadowed ground
cov = np.clip((al - ab) / np.maximum(1 - ab, 1e-6), 0, 1)          # object coverage (1 inside, fractional on edges)
cov[al > 0.999] = 1
premult = col * al[..., None]                                      # object colour * coverage (the shadow adds black)
shadow = np.clip((ab - b0) / (1 - b0), 0, 1)                       # 0 lit ground ... 1 fully dark
alpha = cov + (1 - cov) * shadow * STRENGTH
rgb = np.where(alpha[..., None] > 1e-6, premult / np.maximum(alpha[..., None], 1e-6), 0)
out = np.dstack([np.clip(rgb, 0, 1) * 255, np.clip(alpha, 0, 1) * 255]).astype("uint8")
img = Image.fromarray(out, "RGBA")

x0, y0, x1, y1 = img.getchannel("A").point(lambda v: 255 if v > 4 else 0).getbbox()
side = max(x1 - x0, y1 - y0)
pad = round(side * 0.04)
cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
half = side // 2 + pad
box = (cx - half, cy - half, cx + half, cy + half)
img = img.crop(box).resize((SIZE, SIZE), Image.LANCZOS)
img.save(dst, quality=92, method=6) if dst.endswith(".webp") else img.save(dst)
print(f"wrote {dst}: {SIZE}x{SIZE}, ground baseline alpha {b0:.3f}, shadow strength {STRENGTH}")
