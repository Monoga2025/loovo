# FILE: make_variants.py
# Uso: python make_variants.py motion build/seg/mask.mp4
# Plan B del texto-detrás-del-hablante cuando Chrome no aguanta el video con
# alfa (máquinas con poca RAM: el render se atasca con "capture stalled" /
# "Runtime.callFunctionOn timed out"). Crea tres proyectos hermanos sin alfa:
#   motion_all  = todo menos la silueta            (fondo + detrás + frente)
#   motion_nob  = todo menos silueta y detrás      (fondo + frente)
#   motion_mask = solo la máscara con el MISMO zoom (sin capas)
# Luego: composite_behind.py combina  final = R_all fuera de la persona, R_nob dentro.
# Requiere los marcadores <!-- LAYER:behind|person|front --> de templates/hyperframes/index.html.
import os, re, shutil, sys

proj, mask = sys.argv[1].rstrip("/\\"), sys.argv[2]
src = open(os.path.join(proj, "index.html"), encoding="utf-8").read()


def strip(html, layer):
    return re.sub(rf"\s*<!-- LAYER:{layer} -->.*?<!-- /LAYER:{layer} -->", "", html, flags=re.S)


variants = {"all": strip(src, "person")}
variants["nob"] = strip(variants["all"], "behind")
m = strip(variants["nob"], "front").replace('src="assets/base_graded.mp4"', 'src="assets/mask.mp4"')
m = re.sub(r"\n[^\n]*#pip[^\n]*", "", m)  # sin PiP en la máscara
variants["mask"] = m.replace("background: #070707", "background: #000000")

for name, html in variants.items():
    dst = f"{proj}_{name}"
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(proj, dst, ignore=shutil.ignore_patterns("snapshots", "renders", "*.webm", "node_modules"))
    open(os.path.join(dst, "index.html"), "w", encoding="utf-8").write(html)
    if name == "mask":
        shutil.copy(mask, os.path.join(dst, "assets", "mask.mp4"))
    layers = [k for k, pat in (("detrás", 'id="behind"'), ("silueta", 'id="person"'),
                                ("frente", 'id="graphics"'), ("máscara", "assets/mask.mp4")) if pat in html]
    print(f"{dst}: {', '.join(layers)}")
print("Renderiza cada uno (-w 2) y luego composite_behind.py")
