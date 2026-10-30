"""Seguimiento del puntero en PANTALLA (1920x1080) con plantillas (flecha y lupa de Windows).
Recorre el crudo de 32,0 s a 111,0 s cuadro a cuadro y guarda plan/cursor.json: [t_pantalla, x, y, score].
(x, y) = punta de la flecha o centro de la lupa. score < 0,6 = no encontrado."""
import json, subprocess, os, numpy as np, cv2
SRC = "../../crudo/PANTALLA 17-52-13.mp4"; T0, T1, W, H = 32.0, 111.0, 1920, 1080
os.makedirs("plan", exist_ok=True)
a = cv2.imread("qa/scr_91.4.png", 0); b = cv2.imread("qa/scr_35.0.png", 0)
TPL = [(a[1021:1046, 387:405], (2, 2)), (b[537:565, 946:974], (12, 10))]   # (plantilla, offset del punto activo)
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(T0), "-i", SRC, "-t", str(T1 - T0), "-f", "rawvideo", "-pix_fmt", "gray", "-"], stdout=subprocess.PIPE)
out, n, prev = [], 0, None
while True:
    buf = dec.stdout.read(W * H)
    if len(buf) < W * H: break
    g = np.frombuffer(buf, np.uint8).reshape(H, W)
    best = (-1, 0, 0)
    for tpl, (ox, oy) in TPL:
        if prev is not None:   # búsqueda local primero (rápida y estable)
            x0, y0 = max(0, prev[0] - 260), max(0, prev[1] - 260); x1, y1 = min(W, prev[0] + 260), min(H, prev[1] + 260)
            r = cv2.matchTemplate(g[y0:y1, x0:x1], tpl, cv2.TM_CCOEFF_NORMED); _, s, _, p = cv2.minMaxLoc(r)
            if s > best[0]: best = (s, x0 + p[0] + ox, y0 + p[1] + oy)
        if best[0] < 0.75:
            r = cv2.matchTemplate(g, tpl, cv2.TM_CCOEFF_NORMED); _, s, _, p = cv2.minMaxLoc(r)
            if s > best[0]: best = (s, p[0] + ox, p[1] + oy)
    t = round(T0 + n / 30, 4)
    out.append([t, int(best[1]), int(best[2]), round(float(best[0]), 3)])
    if best[0] >= 0.6: prev = (best[1], best[2])
    n += 1
json.dump(out, open("plan/cursor.json", "w"))
ok = sum(1 for o in out if o[3] >= 0.6); print("cuadros", n, "encontrado", ok)
