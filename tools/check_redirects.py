"""Check every old blog URL in the redirect map lands where the map says, with a 200.

Usage:
  python3 tools/check_redirects.py redirect-map.csv                 # after cutover: follow each old_url
  python3 tools/check_redirects.py redirect-map.csv --origin URL    # before cutover: fetch each migrated post
                                                                     # on the Pages origin, e.g.
                                                                     # https://opensource.suse.com/rancher-blog
Writes redirect-check.csv next to the map and prints a summary. Exit code 1 if anything fails.
"""
import argparse, csv, os, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

MIGRATED = ("migrate", "migrate_refresh")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


opener = urllib.request.build_opener(NoRedirect)


def fetch(url):
    """Return (status, location) without following redirects."""
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "rancher-blog-redirect-check"})
    try:
        with opener.open(req, timeout=20) as r:
            return r.status, None
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location")
    except Exception as e:  # DNS, TLS, timeout
        return 0, str(e)


def follow(url, hops=6):
    chain = []
    for _ in range(hops):
        status, location = fetch(url)
        chain.append(f"{status} {url}")
        if status in (301, 302, 307, 308) and location:
            url = urljoin(url, location)
            continue
        return status, url, chain
    return 0, url, chain + ["too many redirects"]


def norm(u):
    return u.rstrip("/").replace("://rancher.com", "://www.rancher.com")


def check(row, origin):
    expected = row["new_url"]
    if expected.startswith("PENDING"):
        return {**row, "result": "pending", "final_status": "", "final_url": "", "chain": ""}
    if origin:
        if row["disposition"] not in MIGRATED:
            return {**row, "result": "skipped", "final_status": "", "final_url": "", "chain": ""}
        start = expected.replace("https://www.rancher.com", origin.rstrip("/"))
        status, final, chain = follow(start)
        ok = status == 200
    else:
        status, final, chain = follow(row["old_url"])
        ok = status == 200 and norm(final) == norm(expected)
    return {**row, "result": "ok" if ok else "FAIL", "final_status": status, "final_url": final, "chain": " > ".join(chain)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("map")
    ap.add_argument("--origin", help="check migrated posts on this origin instead of following old URLs")
    ap.add_argument("--workers", type=int, default=8)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.map, encoding="utf-8")))
    with ThreadPoolExecutor(a.workers) as pool:
        out = list(pool.map(lambda r: check(r, a.origin), rows))
    path = os.path.join(os.path.dirname(os.path.abspath(a.map)), "redirect-check.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    counts = {}
    for r in out:
        counts[r["result"]] = counts.get(r["result"], 0) + 1
    print(counts, "->", path)
    for r in out:
        if r["result"] == "FAIL":
            print("FAIL", r["old_url"], "|", r["chain"])
    sys.exit(1 if counts.get("FAIL") else 0)


if __name__ == "__main__":
    main()
