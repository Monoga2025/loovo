"""Corte 3: adapta el motion del corte 2 (1080x1920) a la mitad superior (1080x960) sin tocar c2.
Toma la banda útil y = 250..1480 del lienzo original y la escala x0,78; las escenas se ensanchan a 1385 px
para que el fondo (pastel/carbón + puntos) llene los 1080 px. Escribe motion/index.html."""
import json, re, shutil, os
C2 = "../c2"; S, OX, OY = 0.78, 152, 250
if not os.path.isdir("motion/assets"): shutil.copytree(f"{C2}/motion/assets", "motion/assets")
for f in ("hyperframes.json", "package.json"): shutil.copy(f"{C2}/motion/{f}", f"motion/{f}")
json.dump({"id": "corte3top", "name": "corte3top", "createdAt": "2026-10-17T20:00:00.000Z"}, open("motion/meta.json", "w"))
W = json.load(open(f"{C2}/plan/words_on.json", encoding="utf-8")); E = json.load(open(f"{C2}/plan/edl.json"))
ws = [[("Code" + w["w"][4:]) if w["w"].lower().startswith("code") else w["w"], w["on"], w["e"]] for w in W]
p = open(f"{C2}/index.tpl.html", encoding="utf-8").read().replace("__WORDS__", json.dumps(ws, ensure_ascii=False)).replace("__DUR__", str(E["total"]))
R = lambda a, b: (p.count(a) == 1 or (_ for _ in ()).throw(SystemExit("no único: " + a))) and p.replace(a, b)
p = R('content="width=1080, height=1920"', 'content="width=1080, height=960"')
p = R("html, body { width: 1080px; height: 1920px;", "html, body { width: 1080px; height: 960px;")
p = R('data-width="1080" data-height="1920"', 'data-width="1080" data-height="960"')
p = R("<title>Corte 2 full motion</title>", "<title>Corte 3 split top</title>")
p = R("#grain { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;", "#grain { position: absolute; left: 0; top: 0; width: 1080px; height: 960px;")
p = R("#flash { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px;", "#flash { position: absolute; left: 0; top: 0; width: 1080px; height: 960px;")
xf = f"transform-origin: 0 0; transform: scale({S}) translateY(-{OY}px);"
p = R("</style>", f"""
/* --- corte 3: media pantalla --- */
.scene {{ width: {1080 + 2 * OX + 1}px; {xf} }}
.scene > :not(.dots) {{ margin-left: {OX}px; }}
.dots {{ left: -320px; top: -200px; width: 2000px; height: 2400px; }}
#caps {{ width: {1080 + 2 * OX + 1}px; {xf} }}
.cap {{ left: {70 + OX}px; }}
</style>""")
# inserts de pantalla: hijos de la raíz, misma transformación aplicada a su posición
def mv(m):
    L, T = float(m.group(2)), float(m.group(3))
    return f'tl.set("{m.group(1)}", {{ left: {round((L + OX) * S, 1)}, top: {round((T - OY) * S, 1)} }}'
p, n = re.subn(r'tl\.set\("(#v_\w+)", \{ left: ([\d.]+), top: ([\d.]+) \}', mv, p)
assert n == 4, n
p = R("// ---------- helpers ----------", f'gsap.set(".clip", {{ scale: {S}, transformOrigin: "0% 0%" }});\n// ---------- helpers ----------')
open("motion/index.html", "w", encoding="utf-8").write(p); print("ok", E["total"])
