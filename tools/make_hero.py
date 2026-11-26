#!/usr/bin/env python3
"""Featured images for posts that have none.

  python3 tools/make_hero.py content/blog/<slug>   writes images/featured.png in the bundle and sets `image:`
  python3 tools/make_hero.py --base                rebuilds assets/blog/hero-base.png (also used by the
                                                   card fallback in layouts/partials/thumb.html)

Needs Pillow (pip install pillow).
"""
import math
import random
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "assets/blog/hero-base.png"
FONTS = ROOT / "assets/blog/fonts"
LOGO = ROOT / "tools/hero/rancher-logo-white.png"
W, H = 1280, 672  # 40:21, the card ratio
MIDNIGHT, BLUE, TINT = (25, 32, 114), (36, 83, 255), (189, 203, 255)


def hexagon(cx, cy, r):
    return [(cx + r * math.cos(math.radians(60 * i + 30)), cy + r * math.sin(math.radians(60 * i + 30))) for i in range(6)]


def make_base():
    # diagonal midnight -> blue gradient
    grad = Image.new("RGB", (W, H))
    px = grad.load()
    for x in range(W):
        for y in range(H):
            t = min(1, max(0, (x / W) * 0.75 + (1 - y / H) * 0.25))
            px[x, y] = tuple(round(MIDNIGHT[i] + (BLUE[i] - MIDNIGHT[i]) * t) for i in range(3))
    img = grad.convert("RGBA")

    # hexagon mesh fading in towards the right edge, a few cells filled like cluster nodes
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    rnd = random.Random(7)
    r = 46
    dx, dy = r * math.sqrt(3), r * 1.5
    for row in range(-1, int(H / dy) + 2):
        for col in range(-1, int(W / dx) + 2):
            cx = col * dx + (dx / 2 if row % 2 else 0)
            cy = row * dy
            fade = max(0.0, (cx - W * 0.35) / (W * 0.65))
            if fade <= 0:
                continue
            d.polygon(hexagon(cx, cy, r - 3), outline=(255, 255, 255, int(70 * fade)), width=2)
            if rnd.random() < 0.10 * fade:
                d.polygon(hexagon(cx, cy, r - 3), fill=(255, 255, 255, int(40 * fade)))
    img = Image.alpha_composite(img, layer)

    logo = Image.open(LOGO).convert("RGBA")
    img.alpha_composite(logo, (72, H - 72 - logo.height))
    BASE.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(BASE, optimize=True)
    print(f"wrote {BASE.relative_to(ROOT)}")


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("no YAML front matter")
    return m


def field(fm, key):
    m = re.search(rf'^{key}:\s*(.+)$', fm, re.M)
    return m.group(1).strip() if m else ""


def wrap(draw, text, font, width):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def make_post(bundle):
    bundle = Path(bundle)
    md = bundle / "index.md"
    text = md.read_text()
    fm = front_matter(text).group(1)
    title = field(fm, "title").strip("\"'")
    products = re.findall(r'"([^"]+)"', field(fm, "products")) or ["Rancher"]
    eyebrow = " · ".join(products).upper()

    img = Image.open(BASE).convert("RGB")
    d = ImageDraw.Draw(img)
    eb_font = ImageFont.truetype(str(FONTS / "Poppins-SemiBold.ttf"), 24)
    left, maxw = 72, 1000
    for size in (64, 56, 48):  # shrink long titles until they fit in 3 lines
        t_font = ImageFont.truetype(str(FONTS / "Poppins-SemiBold.ttf"), size)
        lines = wrap(d, title, t_font, maxw)
        if len(lines) <= 3:
            break
    lh = round(size * 1.25)
    y = 96
    d.text((left, y), eyebrow, font=eb_font, fill=TINT)
    y += 56
    for line in lines[:3]:
        d.text((left, y), line, font=t_font, fill="white")
        y += lh
    out = bundle / "images/featured.png"
    out.parent.mkdir(exist_ok=True)
    img.save(out, optimize=True)

    if not field(fm, "image"):
        new_fm = re.sub(r"^(title:.*)$", r'\1\nimage: "images/featured.png"', fm, count=1, flags=re.M)
        md.write_text(text.replace(fm, new_fm, 1))
    print(f"wrote {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    make_base() if sys.argv[1] == "--base" else make_post(sys.argv[1])
