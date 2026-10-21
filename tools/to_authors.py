"""Turn `author: "Name"` into the `authors` taxonomy, except for generic accounts that should not get a page."""
import glob, json, re, sys
GENERIC = {"Rancher Admin", "SUSE", ""}
# WordPress accounts whose display name is an email: real name where it is unambiguous, otherwise no byline
ALIASES = {"andrea.mazzotti@suse.com": "Andrea Mazzotti", "nuno.carmo@suse.com": "Nuno Do Carmo",
           "rey.lejano@suse.com": "Rey Lejano", "jhuang@suse.com": ""}
changed = 0
for md in glob.glob(sys.argv[1] + "/content/blog/*/index.md"):
    t = open(md).read()
    m = re.search(r'(?m)^author: (".*")$', t)
    if not m:
        continue
    name = json.loads(m.group(1))
    name = ALIASES.get(name, name)
    assert "@" not in name, (md, name)
    if name in GENERIC:
        if name != json.loads(m.group(1)):
            t = t[:m.start()] + "author: " + json.dumps(name, ensure_ascii=False) + t[m.end():]; open(md, "w").write(t)
        continue
    t = t[:m.start()] + "authors: [" + json.dumps(name, ensure_ascii=False) + "]" + t[m.end():]
    open(md, "w").write(t); changed += 1
print("converted", changed)
