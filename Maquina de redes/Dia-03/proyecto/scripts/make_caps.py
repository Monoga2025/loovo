# FILE: make_caps.py
# Uso: python make_caps.py build/words_out.json motion/compositions/graphics.html \
#          --keys "ni,idea,Loovo,meta,hoy" --skip "8.28-10.21,12.6-14.84" [--max 4]
# Genera el bloque CAPS (subtítulos cinéticos) entre /*CAPS*/ y /*END CAPS*/:
# frases de hasta --max palabras que se cortan en puntuación o pausas > 0,35 s,
# sin puntuación final, con las palabras clave marcadas (rojo, grandes).
# --skip: tramos con escena a pantalla completa (ahí el texto de la escena ya
# hace de subtítulo). Revisa a mano el resultado: elegir claves es decisión de gusto.
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("words")
ap.add_argument("html")
ap.add_argument("--keys", default="")
ap.add_argument("--skip", default="")
ap.add_argument("--max", type=int, default=4)
a = ap.parse_args()

words = json.load(open(a.words, encoding="utf-8"))
keys = {k.strip().lower() for k in a.keys.split(",") if k.strip()}
skips = [tuple(map(float, r.split("-"))) for r in a.skip.split(",") if r.strip()]
in_skip = lambda t: any(s <= t < e for s, e in skips)

caps, cur = [], []


def flush(end):
    global cur
    if cur:
        caps.append({"a": round(cur[0][1], 2), "b": round(end, 2), "w": cur})
    cur = []


for i, w in enumerate(words):
    if in_skip(w["s"]):
        flush(w["s"])
        continue
    txt = w["w"].strip()
    clean = re.sub(r"[.,;:!?…]+$", "", txt)
    kw = 1 if clean.lower().strip("¿¡") in keys else 0
    cur.append([clean, round(w["s"], 2)] + ([1] if kw else []))
    nxt = words[i + 1] if i + 1 < len(words) else None
    gap = (nxt["s"] - w["e"]) if nxt else 9
    if len(cur) >= a.max or txt.endswith((".", ",", "?", "!", "…")) or gap > 0.35 or not nxt or in_skip(nxt["s"]):
        flush(min(nxt["s"], w["e"] + 0.6) if nxt else w["e"] + 0.4)

js = "const CAPS = [\n" + ",\n".join("        " + json.dumps(c, ensure_ascii=False) for c in caps) + ",\n      ];"
html = open(a.html, encoding="utf-8").read()
html = re.sub(r"/\*CAPS\*/.*?/\*END CAPS\*/", "/*CAPS*/\n      " + js + "\n      /*END CAPS*/", html, flags=re.S)
open(a.html, "w", encoding="utf-8").write(html)
print(f"{len(caps)} frases, {sum(len(c['w']) for c in caps)} palabras -> {a.html}")
