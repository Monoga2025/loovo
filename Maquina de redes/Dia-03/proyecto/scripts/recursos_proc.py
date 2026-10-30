# FILE: recursos_proc.py
# Uso: python recursos_proc.py <carpeta_recursos> <marca.json>
# Convierte la biblioteca cruda en recursos listos para HyperFrames, con la identidad de marca:
#   fotos/<n>_corte.png   objeto recortado con rembg (u2net, local) para los aislados
#   fotos/<n>_duo.png     duotono de marca (oscuro -> color 1 -> color 2) para fondos y objetos
#   iconos/<n>.svg        Phosphor (MIT) sin color fijo (currentColor): se colorean con CSS mask
#   texturas/*.png        grano, semitono, ruido de color: generadas por código
#   formas/*.svg          flecha, subrayado a mano, esquinas, destello, rayo: dibujadas por código
# Todo queda anotado en manifest.json (fuente y licencia).
import json, os, sys, urllib.request
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter

root, marca = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
man_path = root / "manifest.json"
man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {}
for d in ("fotos", "iconos", "texturas", "formas"):
    (root / d).mkdir(exist_ok=True)
C = marca["colores"]


def hexrgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], np.float32)


def duotone(img, stops):
    a = np.asarray(img.convert("RGBA"), np.float32)
    lum = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]) / 255
    lum = np.clip((lum - 0.04) / 0.92, 0, 1)
    pos = np.linspace(0, 1, len(stops))
    out = np.zeros(a.shape[:2] + (3,), np.float32)
    for ch in range(3):
        out[..., ch] = np.interp(lum, pos, [hexrgb(s)[ch] for s in stops])
    return Image.fromarray(np.dstack([out, a[..., 3]]).astype(np.uint8), "RGBA")


# ---- fotos
CORTAR = set(marca.get("recortar", []))
DESCARTAR = set(marca.get("descartar", []))
session = None
for name, m in list(man.items()):
    if m.get("tipo") != "foto" or name in DESCARTAR:
        continue
    src = root / "_raw" / m["archivo"]
    if not src.exists():
        continue
    img = Image.open(src).convert("RGB")
    img.thumbnail((1600, 1600))
    if name in CORTAR:
        if session is None:
            os.environ.setdefault("U2NET_HOME", os.path.expanduser("~/.rembg/models/u2net"))
            from rembg import new_session, remove
            session = new_session("u2net")
        from rembg import remove
        cut = remove(img, session=session)
        bbox = cut.getbbox()
        cut = cut.crop(bbox) if bbox else cut
        cut.save(root / "fotos" / f"{name}_corte.png")
        base = cut
        m["corte"] = f"fotos/{name}_corte.png"
    else:
        base = img.convert("RGBA")
    duotone(base, [C["oscuro"], C["primario"], C["acento"]]).save(root / "fotos" / f"{name}_duo.png")
    m["duo"] = f"fotos/{name}_duo.png"
    print("foto", name)

# ---- iconos Phosphor (MIT) en currentColor
for ic in marca.get("iconos", []):
    out = root / "iconos" / f"{ic}.svg"
    if not out.exists():
        try:
            b = urllib.request.urlopen(urllib.request.Request(f"https://api.iconify.design/ph/{ic}.svg?height=256",
                                                              headers={"User-Agent": "loovo-motion/1.0"}), timeout=20).read()
            if b.startswith(b"<svg"):
                out.write_bytes(b)
        except Exception as e:
            print("icono", ic, "error", e)
            continue
    man[f"ico_{ic}"] = {"tipo": "icono", "archivo": f"iconos/{ic}.svg", "licencia": "MIT (Phosphor Icons)", "pagina": "https://phosphoricons.com"}

# ---- texturas por código
rng = np.random.default_rng(42)
g = (rng.normal(128, 38, (1920, 1080))).clip(0, 255).astype(np.uint8)
Image.fromarray(g, "L").save(root / "texturas" / "grano.png")
y, x = np.mgrid[0:1920, 0:1080]
cell = 24
cx, cy = (x % cell) - cell / 2, (y % cell) - cell / 2
rad = (1 - y / 1920) * cell * 0.45
dots = ((cx ** 2 + cy ** 2) < rad ** 2).astype(np.uint8) * 255
Image.fromarray(np.dstack([np.full_like(dots, 255)] * 3 + [dots]), "RGBA").save(root / "texturas" / "semitono.png")
blob = np.zeros((1200, 1200, 4), np.float32)
yy, xx = np.mgrid[0:1200, 0:1200]
for col, (px, py), r in ((C["primario"], (450, 500), 380), (C["acento"], (760, 700), 300)):
    w = np.exp(-(((xx - px) ** 2 + (yy - py) ** 2) / (2 * r ** 2)))
    blob[..., :3] += hexrgb(col) * w[..., None]
    blob[..., 3] = np.maximum(blob[..., 3], w * 255)
# Ventana radial: sin ella el alfa no llega a 0 en el borde y se ve un rectángulo duro sobre fondo oscuro
rr = np.sqrt((xx - 600) ** 2 + (yy - 600) ** 2) / 600
win = np.clip(1 - rr, 0, 1) ** 1.5
blob *= win[..., None]
Image.fromarray(blob.clip(0, 255).astype(np.uint8), "RGBA").filter(ImageFilter.GaussianBlur(30)).save(root / "texturas" / "aura.png")
for t in ("grano", "semitono", "aura"):
    man[f"tex_{t}"] = {"tipo": "textura", "archivo": f"texturas/{t}.png", "licencia": "propia (generada por código)"}

# ---- formas SVG por código (stroke = currentColor)
FORMAS = {
    "flecha_curva": '<path d="M20 180 C 80 40, 200 40, 260 120" fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round"/><path d="M228 86 L 262 122 L 214 134" fill="none" stroke="currentColor" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>',
    "subrayado": '<path d="M10 40 C 90 20, 180 50, 290 26" fill="none" stroke="currentColor" stroke-width="16" stroke-linecap="round"/>',
    "esquinas": '<path d="M10 70 V10 H70 M230 10 H290 V70 M290 230 V290 H230 M70 290 H10 V230" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="square"/>',
    "destello": '<path d="M150 10 C 160 110, 190 140, 290 150 C 190 160, 160 190, 150 290 C 140 190, 110 160, 10 150 C 110 140, 140 110, 150 10 Z" fill="currentColor"/>',
    "rayo": '<path d="M170 10 L 60 170 H 140 L 110 290 L 240 110 H 160 Z" fill="currentColor"/>',
    "circulo_mano": '<path d="M150 20 C 60 18, 14 80, 22 150 C 30 230, 120 282, 200 262 C 268 244, 292 170, 270 110 C 252 62, 200 30, 130 40" fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="round"/>',
}
for n, body in FORMAS.items():
    (root / "formas" / f"{n}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">{body}</svg>', encoding="utf-8")
    man[f"forma_{n}"] = {"tipo": "forma", "archivo": f"formas/{n}.svg", "licencia": "propia (dibujada por código)"}

man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(man), "recursos en el manifiesto")
