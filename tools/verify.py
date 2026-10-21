"""Compare rendered text of every post against the WordPress source (non-whitespace chars, comments removed)."""
import xml.etree.ElementTree as ET, re, html, os, sys
NS = {"wp": "http://wordpress.org/export/1.2/", "content": "http://purl.org/rss/1.0/modules/content/"}
txt = lambda h: re.sub(r"\s", "", html.unescape(re.sub(r"<[^>]+>", "", re.sub(r"(?s)<!--.*?-->", "", h))))
bad, n = [], 0
for it in ET.parse(sys.argv[1]).getroot().iter("item"):
    if it.findtext("wp:post_type", "", NS) != "rancher_blog" or it.findtext("wp:status", "", NS) != "publish":
        continue
    s = re.sub(r"%[0-9a-f]{2}", "", it.findtext("wp:post_name", "", NS)); p = f"{sys.argv[2]}/blog/{s}/index.html"
    if not os.path.exists(p): bad.append((s, "MISSING")); continue
    a = re.sub(r"(?s)<h1>.*?</p>", "", re.search(r"(?s)<article>(.*)</article>", open(p).read()).group(1), count=1)
    o, nn = txt(it.findtext("content:encoded", "", NS)), txt(a); n += 1
    r = len(nn) / max(len(o), 1)
    if r < 0.98 or r > 1.02: bad.append((s, round(r, 3), len(o)))
print("rendered", n, "outliers", len(bad))
for b in bad: print(b)
