"""Busca en Wikimedia Commons y guarda miniaturas + metadatos. Uso: commons.py "consulta" prefijo [n]"""
import sys, json, time, urllib.request, urllib.parse, os
UA = {"User-Agent": "LoovoEditor/1.0 (video edit; contact via repo owner)"}
q, pre = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 12
u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(dict(action="query", generator="search",
    gsrsearch=q + " filetype:bitmap", gsrnamespace=6, gsrlimit=n, prop="imageinfo", iiprop="url|size|extmetadata",
    iiextmetadatafilter="LicenseShortName|Artist|LicenseUrl", iiurlwidth=360, format="json"))
d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA)))
os.makedirs("_dl/thumbs", exist_ok=True); meta = {}
for i, p in enumerate(d["query"]["pages"].values()):
    ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
    lic = m.get("LicenseShortName", {}).get("value", "?")
    if not any(k in lic for k in ("CC0", "Public domain", "CC BY")): continue
    fn = f"_dl/thumbs/{pre}{i:02d}.jpg"
    try:
        urllib.request.urlretrieve if False else open(fn, "wb").write(urllib.request.urlopen(urllib.request.Request(ii["thumburl"], headers=UA)).read())
    except Exception as e: print("fail", e); continue
    meta[fn] = dict(title=p["title"], url=ii["url"], page=ii["descriptionurl"], w=ii["width"], h=ii["height"], lic=lic,
                    lic_url=m.get("LicenseUrl", {}).get("value", ""), artist=m.get("Artist", {}).get("value", ""))
    print(fn, ii["width"], ii["height"], lic, p["title"][:60].encode("ascii","replace").decode())
    time.sleep(0.6)
old = json.load(open("_dl/meta.json")) if os.path.exists("_dl/meta.json") else {}
old.update(meta); json.dump(old, open("_dl/meta.json", "w"), indent=1)
