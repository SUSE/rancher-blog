#!/usr/bin/env python3
"""Fail when a live post published since the new blog launched has no featured image.

Older migrated posts are exempt: their cards use the branded fallback in layouts/partials/thumb.html.
"""
import re
import sys
from pathlib import Path

SINCE = "2026-11-11"  # launch of the Hugo blog
missing = []
for md in sorted(Path("content/blog").glob("*/index.md")):
    fm = re.match(r"^---\n(.*?)\n---\n", md.read_text(), re.S)
    if not fm:
        continue
    fm = fm.group(1)
    if re.search(r"^draft:\s*true", fm, re.M):
        continue
    date = re.search(r"^date:\s*\"?(\d{4}-\d{2}-\d{2})", fm, re.M)
    if not date or date.group(1) < SINCE:
        continue
    image = re.search(r"^image:\s*\"?([^\"\n]+)\"?\s*$", fm, re.M)
    if not image or not (md.parent / image.group(1).strip()).is_file():
        missing.append(md.parent)

for d in missing:
    print(f"::error file={d}/index.md::No featured image. Add one and set `image:` in the front matter, "
          f"or run: python3 tools/make_hero.py {d}")
sys.exit(1 if missing else 0)
