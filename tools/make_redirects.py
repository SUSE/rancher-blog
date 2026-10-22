"""Build the CloudFront KeyValueStore import file from the redirect map.

Usage: python3 tools/make_redirects.py redirect-map.csv [old-rancher-urls.csv] > cloudfront/redirects-kvs.json
Only archived and dropped posts go in: migrated posts are served by Hugo, and posts moving
to suse.com never reach rancher.com (suse.com keeps them until they are imported there).
"""
import csv, json, sys
from urllib.parse import urlparse

data = []
for row in csv.DictReader(open(sys.argv[1], encoding="utf-8")):
    if row["disposition"] not in ("archive_redirect", "drop") or not row["new_url"].startswith("https://"):
        continue
    slug = urlparse(row["old_url"]).path.rstrip("/").rsplit("/", 1)[-1]
    data.append({"key": slug, "value": row["new_url"]})
# pre-2021 rancher.com URLs (/blog/YYYY/<old-slug>), matched to new posts by slug or title
if len(sys.argv) > 2:
    for row in csv.DictReader(open(sys.argv[2], encoding="utf-8")):
        if row["target"]:
            data.append({"key": row["old_path"].strip("/").lower(), "value": row["target"]})
json.dump({"data": sorted(data, key=lambda d: d["key"])}, sys.stdout, indent=1)
print()
