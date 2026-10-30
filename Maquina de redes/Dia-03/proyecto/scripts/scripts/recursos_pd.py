# FILE: recursos_pd.py
# Uso: python recursos_pd.py <carpeta_recursos> [--solo nombre1,nombre2]
# Descarga fotos de objetos con licencia libre verificada (dominio público o CC0) desde
# Wikimedia Commons y la NASA, las guarda en <carpeta>/_raw/ y anota fuente y licencia en
# <carpeta>/manifest.json. Solo acepta una imagen si la licencia que devuelve la API dice
# "Public domain", "CC0" o "PD". El recorte (rembg) y el tinte de marca los hace recursos_proc.py.
import json, sys, time, urllib.parse, urllib.request
from pathlib import Path

UA = {"User-Agent": "loovo-motion/1.0 (series Dia X de 42; local video editing)"}
OK = ("public domain", "cc0", "pd-", "pdm")

# nombre -> (fuente, consulta)
PEDIDOS = {
    "reloj_alarma": ("commons", "alarm clock isolated white background"),
    "celular": ("commons", "smartphone isolated on white"),
    "portatil": ("commons", "laptop computer isolated white background"),
    "taza_cafe": ("commons", "coffee cup isolated white background"),
    "reloj_arena": ("commons", "hourglass isolated"),
    "ajedrez_rey": ("commons", "chess king piece white background"),
    "bombillo": ("commons", "light bulb isolated white background"),
    "teclado": ("commons", "computer keyboard isolated white background"),
    "trofeo": ("commons", "trophy cup isolated white background"),
    "cerebro": ("commons", "brain anatomical model white background"),
    "robot": ("commons", "toy robot isolated white background"),
    "billete_1957": ("commons", "1957 one United States dollar star note"),
    "monedas": ("commons", "stack of coins isolated white background"),
    "calendario": ("commons", "desk calendar isolated white background"),
    "mano_celular": ("commons", "hand holding smartphone isolated white"),
    "busto_marmol": ("commons", "marble bust sculpture white background"),
    "luna": ("nasa", "full moon"),
    "tierra_noche": ("nasa", "earth at night city lights"),
    "cohete": ("nasa", "rocket launch"),
    "astronauta": ("nasa", "astronaut spacewalk"),
    "satelite": ("nasa", "satellite in orbit"),
    "servidores": ("nasa", "supercomputer"),
}


def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
        return json.load(r)


def commons(q):
    s = get_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "query", "list": "search", "srsearch": q + " filetype:bitmap", "srnamespace": 6, "srlimit": 15, "format": "json"}))
    for hit in s["query"]["search"]:
        d = get_json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(
            {"action": "query", "prop": "imageinfo", "iiprop": "url|extmetadata|size", "titles": hit["title"], "format": "json", "iiurlwidth": 1600}))
        info = list(d["query"]["pages"].values())[0].get("imageinfo", [{}])[0]
        lic = (info.get("extmetadata", {}).get("LicenseShortName", {}).get("value") or "").strip()
        if info.get("width", 0) >= 700 and any(k in lic.lower() for k in OK):
            return {"url": info.get("thumburl") or info["url"], "pagina": info.get("descriptionurl"), "licencia": lic, "titulo": hit["title"]}
    return None


def openverse(q):
    # Openverse: solo CC0 y marca de dominio público; prioriza rawpixel (objetos aislados)
    s = get_json("https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
        {"q": q, "license": "cc0,pdm", "page_size": 20, "mature": "false"}))
    res = sorted(s.get("results", []), key=lambda r: (r.get("source") != "rawpixel", -(r.get("width") or 0)))
    for r in res:
        if (r.get("width") or 0) >= 700 and r.get("license") in ("cc0", "pdm"):
            return {"url": r["url"], "pagina": r.get("foreign_landing_url"), "licencia": r["license"].upper() + " (Openverse, " + r.get("source", "") + ")",
                    "titulo": r.get("title") or ""}
    return None


def nasa(q):
    s = get_json("https://images-api.nasa.gov/search?" + urllib.parse.urlencode({"q": q, "media_type": "image"}))
    for it in s["collection"]["items"][:12]:
        nasa_id = it["data"][0]["nasa_id"]
        files = get_json(it["href"])
        cand = [f for f in files if f.lower().endswith((".jpg", ".png")) and "~medium" in f] or \
               [f for f in files if f.lower().endswith((".jpg", ".png")) and "~orig" not in f]
        if cand:
            return {"url": cand[0].replace("http://", "https://"), "pagina": f"https://images.nasa.gov/details/{nasa_id}",
                    "licencia": "NASA, dominio público (no implica respaldo de la NASA)", "titulo": it["data"][0].get("title", "")}
    return None


def main():
    root = Path(sys.argv[1])
    raw = root / "_raw"
    raw.mkdir(parents=True, exist_ok=True)
    man_path = root / "manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {}
    solo = set(sys.argv[3].split(",")) if len(sys.argv) > 3 and sys.argv[2] == "--solo" else None
    for name, (src, q) in PEDIDOS.items():
        if solo and name not in solo:
            continue
        if name in man and (raw / man[name]["archivo"]).exists():
            continue
        try:
            r = nasa(q) if src == "nasa" else (openverse(q) or commons(q))
            time.sleep(1.5)
        except Exception as e:
            print(f"{name}: error {e}")
            continue
        if not r:
            print(f"{name}: sin resultado con licencia libre")
            continue
        ext = ".png" if r["url"].lower().split("?")[0].endswith(".png") else ".jpg"
        fn = name + ext
        with urllib.request.urlopen(urllib.request.Request(r["url"], headers=UA), timeout=90) as resp:
            (raw / fn).write_bytes(resp.read())
        man[name] = {"archivo": fn, "tipo": "foto", **r}
        print(f"{name}: {r['licencia']} | {r['titulo'][:60]}")
        time.sleep(0.5)
    man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")


main()
