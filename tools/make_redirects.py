"""Build the CloudFront KeyValueStore import file from the redirect map.

Usage: python3 tools/make_redirects.py redirect-map.csv [old-rancher-urls.csv] > cloudfront/redirects-kvs.json
Archived and dropped posts go in, plus posts moving to suse.com: until the SUSE blog has them
(new_url still PENDING) they go to the SUSE blog home. Migrated posts are served by Hugo.
"""
import csv, json, sys
from urllib.parse import urlparse

SUSE_BLOG = "https://www.suse.com/blog/"  # interim home for posts not yet imported into the SUSE blog

data = []
for row in csv.DictReader(open(sys.argv[1], encoding="utf-8")):
    if row["disposition"] not in ("archive_redirect", "drop", "move_to_suse"):
        continue
    slug = urlparse(row["old_url"]).path.rstrip("/").rsplit("/", 1)[-1]
    target = row["new_url"] if row["new_url"].startswith("https://") else SUSE_BLOG
    data.append({"key": slug, "value": target})
# pre-2021 rancher.com URLs (/blog/YYYY/<old-slug>), matched to new posts by slug or title
if len(sys.argv) > 2:
    for row in csv.DictReader(open(sys.argv[2], encoding="utf-8")):
        if row["target"]:
            target = SUSE_BLOG if "suse.com/c/rancher_blog/" in row["target"] else row["target"]
            data.append({"key": row["old_path"].strip("/").lower(), "value": target})
json.dump({"data": sorted(data, key=lambda d: d["key"])}, sys.stdout, indent=1)
print()
