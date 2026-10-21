"""Ping IndexNow for posts whose scheduled date passed in the last 90 minutes (i.e. just went live)."""
import datetime, glob, json, re, urllib.request

KEY = "71a06e32b46b84d1c60a501f224cf305"
HOST = "latetothetakeover.github.io"
now = datetime.datetime.now(datetime.timezone.utc)
urls = []
for path in glob.glob("_posts/*.md"):
    fm = open(path, encoding="utf-8").read().split("---", 2)[1]
    d = re.search(r"^date:\s*(.+)$", fm, re.M)
    p = re.search(r"^permalink:\s*(\S+)", fm, re.M)
    if not (d and p):
        continue
    dt = datetime.datetime.strptime(d.group(1).strip(), "%Y-%m-%d %H:%M:%S %z")
    if now - datetime.timedelta(minutes=90) < dt <= now:
        urls.append(f"https://{HOST}{p.group(1)}")
if urls:
    urls += [f"https://{HOST}/", f"https://{HOST}/sitemap.xml"]
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": f"https://{HOST}/{KEY}.txt", "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        print(urls, urllib.request.urlopen(req, timeout=30).status)
    except Exception as e:
        print("IndexNow ping failed (non-fatal):", e)
else:
    print("No newly live posts to ping.")
