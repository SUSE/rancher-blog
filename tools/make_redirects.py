"""Build the CloudFront KeyValueStore import file from the redirect map.

Usage: python3 tools/make_redirects.py redirect-map.csv > cloudfront/redirects-kvs.json
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
json.dump({"data": sorted(data, key=lambda d: d["key"])}, sys.stdout, indent=1)
print()
