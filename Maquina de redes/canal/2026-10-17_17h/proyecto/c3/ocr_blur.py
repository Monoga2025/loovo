"""Detecta texto sensible en PANTALLA (OCR RapidOCR a 3 fps en los tramos usados) y guarda plan/blur.json:
lista de [t_pantalla, x0, y0, x1, y1, texto]. Las franjas fijas (pestañas, barra de tareas, chrome del navegador)
las añade compose.py por regla. Rápido: un solo decodificador por tramo, y si el cuadro casi no cambió se reusan las cajas."""
import json, re, subprocess, sys, numpy as np
from rapidocr_onnxruntime import RapidOCR
SRC = "../../crudo/PANTALLA 17-52-13.mp4"; LAG = 0.138
E = json.load(open("../c2/plan/edl.json"))
PAT = re.compile(r"users|c:\\|c:/|desktop-|api_?key|password|secret|token=|sk-|\.env\b|imou|cuentas|localhost|@gmail|bearer|passw", re.I)
ocr = RapidOCR()
segs = []   # tramos de pantalla usados (con hueco/cola incluidos)
for i, p in enumerate(E["pieces"]):
    b = (E["pieces"][i + 1]["a"] if i + 1 < len(E["pieces"]) and E["pieces"][i + 1]["a"] - p["b"] < 1 else p["b"] + 1.0)
    segs.append((p["a"] - LAG - 0.2, b - LAG + 0.2))
out, n_ocr, n_tot = [], 0, 0
for a, b in segs:
    dec = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(a), "-i", SRC, "-t", str(b - a), "-vf", "fps=3", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], capture_output=True).stdout
    fr_sz = 1920 * 1080 * 3; prev, prev_hits = None, []
    for k in range(len(dec) // fr_sz):
        img = np.frombuffer(dec[k * fr_sz:(k + 1) * fr_sz], np.uint8).reshape(1080, 1920, 3); t = round(a + k / 3, 3); n_tot += 1
        small = img[::8, ::8].astype(np.int16)
        if prev is not None and np.abs(small - prev).mean() < 0.6: hits = prev_hits
        else:
            res, _ = ocr(img); n_ocr += 1; hits = []
            for box, txt, conf in (res or []):
                if PAT.search(txt):
                    xs, ys = [q[0] for q in box], [q[1] for q in box]; hits.append([int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys)), txt])
            prev, prev_hits = small, hits
        out += [[t] + h for h in hits]
    print(f"tramo {a:.1f}-{b:.1f} listo · OCR {n_ocr}/{n_tot}", flush=True)
json.dump(out, open("plan/blur.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("cajas sensibles", len(out))
for o in sorted({o[5] for o in out}): print(" ·", o[:100])
