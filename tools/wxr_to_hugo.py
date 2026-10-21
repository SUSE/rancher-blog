"""Convert the Rancher WordPress WXR export into Hugo page bundles.

Usage: wxr_to_hugo.py <export.xml> <inventory.csv> <out_site_dir>
Writes content/blog/<slug>/index.md for every published post and
image-map.csv (bundle path -> uploads-relative source path) for the copy step.
"""
import csv, html, json, os, re, sys
import xml.etree.ElementTree as ET
from collections import Counter
from markdownify import markdownify

NS = {"wp": "http://wordpress.org/export/1.2/", "content": "http://purl.org/rss/1.0/modules/content/",
      "dc": "http://purl.org/dc/elements/1.1/", "excerpt": "http://wordpress.org/export/1.2/excerpt/"}
UPLOAD_RE = re.compile(r"https?://(?:www\.)?suse\.com/c/wp-content/uploads/(\d{4}/\d{2}/[^\"'\s)?#]+)")
SIZE_RE = re.compile(r"-\d+x\d+(?=\.\w+$)")

src, inv_path, out = sys.argv[1:4]
inv = {r["post_id"]: r for r in csv.DictReader(open(inv_path))}
root = ET.parse(src).getroot()
authors = {a.findtext("wp:author_login", "", NS): a.findtext("wp:author_display_name", "", NS) for a in root.iter("{%s}author" % NS["wp"])}
attach = {i.findtext("wp:post_id", "", NS): i.findtext("wp:attachment_url", "", NS)
          for i in root.iter("item") if i.findtext("wp:post_type", "", NS) == "attachment"}


def wpautop(body):
    """WordPress renders every line break as a break; make each one a paragraph outside <pre> and tables."""
    body = body.replace("\r\n", "\n")
    if len(re.findall(r"(?i)<p[\s>]", body)) >= 1:  # older imports already use <p>, their newlines are soft wraps
        return body
    parts = re.split(r"(?is)(<pre\b.*?</pre>|<table\b.*?</table>)", body)
    block = r"(?:p|h[1-6]|ul|ol|li|div|figure|figcaption|blockquote|table|pre|iframe|hr|tr|td|th|tbody|thead)\b"
    def brk(m):
        before, after = m.string[:m.start()].rstrip(), m.string[m.end():].lstrip()
        if re.search(r"</?" + block + r"[^>]*>$", before) or re.match(r"</?" + block, after):
            return "\n"
        opened = lambda t: len(re.findall(rf"(?i)<{t}[\s>]", before)) - len(re.findall(rf"(?i)</{t}>", before))
        if any(opened(t) > 0 for t in ("a", "strong", "em", "b", "i", "code")):
            return " "  # soft wrap inside inline markup
        if opened("blockquote") > 0:
            return "<br>\n"
        return "<br><br>\n"  # markdownify turns this into a blank line, i.e. a new paragraph
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(r"\n+", brk, parts[i])
    return "".join(parts)


def caption(m):
    inner = m.group(1)
    img = re.search(r"(?is)<img[^>]*>", inner)
    text = re.sub(r"(?is)<a[^>]*>\s*<img[^>]*>\s*</a>|<img[^>]*>", "", inner).strip()
    return f"<figure>{img.group(0) if img else ''}<figcaption>{text}</figcaption></figure>"


def gist_table(m):
    """GitHub gist embeds pasted as tables, one <pre> per line: collapse to one code block."""
    lines = re.findall(r"(?is)<td[^>]*blob-code[^>]*>\s*(.*?)\s*</td>", m.group(0))
    code = "\n".join(re.sub(r"(?is)</?pre[^>]*>", "", l) for l in lines)
    return f"<pre>{code}</pre>"


def esc(s):
    return json.dumps(s, ensure_ascii=False)


images, stats, slugs = [], Counter(), Counter()
os.makedirs(f"{out}/content/blog", exist_ok=True)
for it in root.iter("item"):
    if it.findtext("wp:post_type", "", NS) != "rancher_blog" or it.findtext("wp:status", "", NS) != "publish":
        continue
    pid = it.findtext("wp:post_id", "", NS)
    meta = inv[pid]
    slug = re.sub(r"%[0-9a-f]{2}", "", it.findtext("wp:post_name", "", NS))  # one slug carries an encoded hair space
    slugs[slug] += 1
    assert slugs[slug] == 1, f"duplicate slug {slug}"
    body = it.findtext("content:encoded", "", NS) or ""
    body = re.sub(r"(?is)\[caption[^\]]*\](.*?)\[/caption\]", caption, body)
    body = re.sub(r"(?is)<table[^>]*>(?:(?!</table>).)*blob-code.*?</table>", gist_table, body)
    body = re.sub(r'(?i)\b(href|src)="\s*([^"]*?)\s*"',
                  lambda m: f'{m.group(1)}="{m.group(2).replace(" ", "%20").replace("(", "%28").replace(")", "%29")}"', body)
    # single-cell tables (Confluence code macros) wrap a code block: unwrap them
    body = re.sub(r"(?is)<table[^>]*>\s*(?:<tbody>)?\s*<tr>\s*<td[^>]*>(.*?)</td>\s*</tr>\s*(?:</tbody>)?\s*</table>", r"\1", body)
    body = wpautop(body)

    bundle_imgs = {}
    def localize(m):
        rel = html.unescape(m.group(1))
        name = os.path.basename(rel)
        bundle_imgs[name] = rel
        return f"images/{name}"
    body = UPLOAD_RE.sub(localize, body)
    # keep raw HTML for embeds Markdown cannot express
    md = markdownify(body, heading_style="ATX", bullets="-", code_language="", strip=["span", "div", "style", "script"],
                     keep_inline_images_in=["a", "td", "th", "figure", "h1", "h2", "h3", "h4", "h5", "h6"])
    md = re.sub(r"[ \t]+\n(?=[ \t]*\n)", "\n", md)
    md = re.sub(r"\n[ \t]+\n", "\n\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    stats["iframes"] += len(re.findall(r"<iframe", body))

    thumb = None
    for pm in it.findall("wp:postmeta", NS):
        if pm.findtext("wp:meta_key", "", NS) == "_thumbnail_id":
            u = attach.get(pm.findtext("wp:meta_value", "", NS), "")
            m = UPLOAD_RE.search(u)
            if m:
                thumb = os.path.basename(m.group(1)); bundle_imgs[thumb] = m.group(1)
    excerpt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", it.findtext("excerpt:encoded", "", NS) or ""))).strip()

    archived = meta["disposition"] == "archive_redirect"
    tags = [t for t in meta["topics"].split("|") if t]
    fm = [
        "---",
        f"title: {esc(html.unescape(it.findtext('title', '')))}",
        f"date: {it.findtext('wp:post_date', '', NS).replace(' ', 'T')}",
        f"slug: {esc(slug)}",
        f"author: {esc(authors.get(it.findtext('dc:creator', '', NS), it.findtext('dc:creator', '', NS)))}",
        f"description: {esc(excerpt[:300])}" if excerpt else None,
        f"image: {esc('images/' + thumb)}" if thumb else None,
        f"products: [{esc(meta['primary_product'])}]",
        f"tags: [{', '.join(esc(t) for t in tags)}]",
        f"content_type: {esc(meta['content_type'])}",
        f"draft: {'true' if archived else 'false'}",
        "migration:",
        f"  wp_id: {pid}",
        f"  original_url: {esc(it.findtext('link', ''))}",
        f"  disposition: {meta['disposition']}",
        f"  commercial: {meta['commercial_flag'] == 'yes'}".lower(),
        f"  outdated_reason: {esc(meta['outdated_reason'])}",
        f"  redirect_target: {esc(meta['redirect_target'])}",
        "---",
    ]
    d = f"{out}/content/blog/{slug}"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/index.md", "w") as f:
        f.write("\n".join(x for x in fm if x is not None) + "\n\n" + md)
    for name, rel in bundle_imgs.items():
        images.append((f"content/blog/{slug}/images/{name}", rel, SIZE_RE.sub("", rel)))
    stats["posts"] += 1
    stats["archived_as_draft"] += archived
    stats["leftover_shortcodes"] += len(re.findall(r"\[/?caption", md))

with open(f"{out}/image-map.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["dest", "source", "source_unsized"]); w.writerows(images)
stats["image_refs"] = len(images)
print(dict(stats))
assert stats["posts"] == 689 and stats["leftover_shortcodes"] == 0
