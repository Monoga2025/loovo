"""Corte 3 split 9:16: arriba motion del corte 2 (build/motion_top.mp4, 1080x960), abajo PANTALLA con zoom que sigue al cursor.
Mismos tiempos y mismo audio que el corte 2 (../c2/audio/final.wav). Separador dorado fino. Invert flash solo arriba.
Uso: python compose.py salida.mp4 [--preview N]   (N = solo los primeros N s, para pruebas)"""
import sys, json, subprocess, numpy as np, cv2
OUT = sys.argv[1]; PREV = float(sys.argv[sys.argv.index("--preview") + 1]) if "--preview" in sys.argv else None
W, H, HH, FPS = 1080, 1920, 960, 30
SRC = "../../crudo/PANTALLA 17-52-13.mp4"; LAG = 0.138; D0, D1 = 32.0, 111.6   # pantalla va 138 ms antes que la cámara (GCC-PHAT)
E = json.load(open("../c2/plan/edl.json")); DUR = E["total"]; N = int(round((PREV or DUR) * FPS))
GOLD, GOLD_HI = (122, 176, 200), (174, 214, 230)   # BGR de #C8B07A y #E6D6AE

# ---------- tiempo de salida -> tiempo de cámara (fuente) ----------
P = E["pieces"]
def src(t):
    for i, p in enumerate(P):
        end = p["o"] + p["b"] - p["a"]; nxt = P[i + 1]["o"] if i + 1 < len(P) else 1e9
        if p["o"] - 1e-6 <= t < nxt: return p["a"] + (t - p["o"]), i   # en el hueco tras la pieza la pantalla sigue corriendo
    return P[-1]["b"] + t - (P[-1]["o"] + P[-1]["b"] - P[-1]["a"]), len(P) - 1
TS = [src(n / FPS) for n in range(N)]
seg_id = [P[i]["seg"] for _, i in TS]

# ---------- cursor ----------
C = json.load(open("plan/cursor.json")); CT = np.array([c[0] for c in C])
def cur(ts):
    k = int(np.argmin(abs(CT - ts))); c = C[k]
    ok = c[3] >= 0.72 and not (abs(c[1] - 281) < 6 and abs(c[2] - 1000) < 6)   # el glifo '❯' del prompt engaña a la plantilla
    return (c[1], c[2]) if ok else None

# ---------- foco manual donde el cursor está oculto (tramo G, alineado a lo que dice) ----------
MAN = [  # (desde, hasta) en s de cámara, centro, caja a resaltar (x0,y0,x1,y1) o None
    (94.60, 97.30, (500, 960), (272, 994, 720, 1024)),      # "desde acá puede ingresar a los subagentes" -> línea del subagente
    (97.30, 101.60, (900, 360), None),                       # "respuesta en formato de texto al agente orquestador" -> el prompt
    (101.60, 106.20, (520, 640), (272, 616, 590, 642)),      # "revisar los archivos" -> "Read 2 files, ran 4 shell commands"
    (106.20, 108.85, (1780, 1000), (1676, 994, 1900, 1024)),  # "ahorra un montón de tokens" -> contador de tokens
    (108.85, 112.0, (960, 560), None)]                       # "más rápido" -> abre plano
def man(s):
    for a, b, c, box in MAN:
        if a <= s < b: return c, box
    return None, None

# ---------- zoom por la voz ----------
EV = [  # (s de cámara, zoom, tipo)  deícticos = más fuerte
    (35.02, 2.25, "d"), (35.76, 2.25, "d"), (39.10, 2.0, "d"), (44.10, 1.85, "e"), (77.02, 2.15, "d"),
    (91.50, 2.25, "d"), (94.92, 2.2, "d"), (100.28, 1.6, "e"), (104.50, 1.95, "e"), (107.22, 2.3, "e")]
ZB = 1.32
def zenv(s):
    z, ring = ZB, 0.0
    for t0, zz, k in EV:
        a, h, r = t0 - 0.35, t0 + 1.0, 0.55    # entra 0,35 s antes, sostiene 1 s, sale en 0,55 s
        if a <= s < t0: f = (s - a) / 0.35
        elif t0 <= s < h: f = 1.0
        elif h <= s < h + r: f = 1 - (s - h) / r
        else: continue
        f = f * f * (3 - 2 * f); z = max(z, ZB + (zz - ZB) * f)
        if k == "d": ring = max(ring, f)
    return z, ring
if True:
    s_last = TS[-1][0]
    Z = np.array([zenv(s)[0] for s, _ in TS]); RING = np.array([zenv(s)[1] for s, _ in TS])
    Z[np.array([s for s, _ in TS]) > 109.6] = np.linspace(ZB, 1.08, int((np.array([s for s, _ in TS]) > 109.6).sum()) or 1)[: int((np.array([s for s, _ in TS]) > 109.6).sum())]

# objetivo de centro por cuadro
cx, cy, BOX, HASC = [], [], [], []
last = (960, 540)
for s, _ in TS:
    m, box = man(s)
    c = cur(s - LAG)
    if m is not None: tgt = m
    elif c is not None: tgt = c; last = c
    else: tgt = last
    cx.append(tgt[0]); cy.append(tgt[1]); BOX.append(box); HASC.append(c is not None and m is None)
cx, cy = np.array(cx, float), np.array(cy, float)

def smooth(x, tau, resets):
    a = 1 - np.exp(-1 / (FPS * tau)); y = x.copy()
    for lo, hi in resets:
        seg = x[lo:hi].copy()
        for _ in range(2):   # ida y vuelta: sin retraso, sin saltos
            for k in range(1, len(seg)): seg[k] = seg[k - 1] + a * (seg[k] - seg[k - 1])
            seg = seg[::-1]
        y[lo:hi] = seg
    return y
# reinicio del suavizado solo donde la pantalla salta de verdad (> 1 s de fuente)
cuts = [0] + [n for n in range(1, N) if TS[n][0] - TS[n - 1][0] > 1.0] + [N]
RS = list(zip(cuts[:-1], cuts[1:]))
rx, ry = smooth(cx, 0.12, RS), smooth(cy, 0.12, RS)          # objetivo casi crudo
cx, cy = smooth(cx, 0.30, RS), smooth(cy, 0.30, RS)          # paneo suave
Z = smooth(Z, 0.08, [(0, N)])
fz = np.clip((Z - ZB) / 0.5, 0, 1); fz = fz * fz * (3 - 2 * fz)   # con zoom fuerte el encuadre se clava en lo que nombra
cx, cy = cx * (1 - fz) + rx * fz, cy * (1 - fz) + ry * fz

# ---------- desenfoque de lo sensible ----------
import os
if not os.path.exists("plan/blur.json") and not PREV: raise SystemExit("falta plan/blur.json (corre ocr_blur.py)")
BL = [b for b in json.load(open("plan/blur.json", encoding="utf-8")) if "nada de secretos" not in b[5]] if os.path.exists("plan/blur.json") else []   # esa línea solo dice "nada de secretos"
BT = np.array([b[0] for b in BL]) if BL else np.array([])
def blur_boxes(ts):
    bx = [(0, 0, 1920, 40), (0, 1032, 1920, 1080)]                      # pestañas/título y barra de tareas
    if ts < 46: bx += [(0, 0, 1920, 182), (0, 962, 1920, 1034)]         # chrome del navegador, título del post de Reddit
    if len(BT):
        for k in np.nonzero(abs(BT - ts) <= 0.45)[0]:
            _, x0, y0, x1, y1, _t = BL[k]; bx.append((x0 - 8, y0 - 6, x1 + 8, y1 + 6))
    return bx
def apply_blur(img, boxes):
    for x0, y0, x1, y1 in boxes:
        x0, y0, x1, y1 = max(0, int(x0)), max(0, int(y0)), min(1920, int(x1)), min(1080, int(y1))
        if x1 - x0 < 4 or y1 - y0 < 4: continue
        roi = img[y0:y1, x0:x1]
        small = cv2.resize(roi, (max(1, (x1 - x0) // 16), max(1, (y1 - y0) // 16)), interpolation=cv2.INTER_AREA)
        img[y0:y1, x0:x1] = cv2.GaussianBlur(cv2.resize(small, (x1 - x0, y1 - y0), interpolation=cv2.INTER_LINEAR), (0, 0), 6)

# ---------- invert flash (Adrià) solo en la mitad de arriba ----------
CUTS = [int(round(17.20 * FPS)), int(round(36.95 * FPS))]
PP = lambda pts: np.array([[x * W, y * HH] for x, y in pts], np.int32)
FX = {-3: (PP([(.55, 1), (1, .78), (1, 1)]), 0.0, 1.35), -2: (PP([(.40, 1), (1, .66), (1, 1)]), 0.0, 1.35),
      -1: (PP([(0, .55), (1, .20), (1, 1), (0, 1)]), 0.45, 1.5), 0: (PP([(0, 0), (1, 0), (1, .75), (0, .12)]), 0.0, 1.3),
      1: (PP([(.70, 0), (1, 0), (1, .30)]), 0.0, 1.25), 2: (PP([(.74, 0), (1, 0), (1, .26)]), 0.0, 1.25),
      3: (PP([(0, 0), (1, 0), (1, .60), (0, .30)]), 0.0, 1.3)}
def fx(fr, poly, flash, gain):
    m = np.zeros((HH, W), np.uint8); cv2.fillPoly(m, [poly], 255)
    m = cv2.GaussianBlur(m, (0, 0), 1.5).astype(np.float32)[..., None] / 255
    inv = np.clip((255 - fr.astype(np.float32)) * gain + 25, 0, 255)
    o = fr * (1 - m) + inv * m
    if flash: o = o * (1 - flash) + 255 * flash
    return np.clip(o, 0, 255).astype(np.uint8)

# ---------- render ----------
top = subprocess.Popen(["ffmpeg", "-v", "error", "-i", "build/motion_top.mp4", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
scr = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(D0), "-i", SRC, "-t", str(D1 - D0), "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
aud = ["-i", "../c2/audio/final.wav", "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-shortest"]
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + aud +
                       ["-c:v", "libx264", "-crf", "17", "-preset", "slow", "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709",
                        "-color_trc", "bt709", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
fi, frame, log = -1, None, []
for n in range(N):
    b = top.stdout.read(W * HH * 3)
    t_img = np.frombuffer(b, np.uint8).reshape(HH, W, 3).copy() if len(b) == W * HH * 3 else t_img
    k = [n - c for c in CUTS if n - c in FX]
    if k: t_img = fx(t_img, *FX[k[0]])
    s, _ = TS[n]; want = int(round((s - LAG - D0) * FPS))
    while fi < want:
        raw = scr.stdout.read(1920 * 1080 * 3)
        if len(raw) < 1920 * 1080 * 3: break
        frame = np.frombuffer(raw, np.uint8).reshape(1080, 1920, 3).copy(); fi += 1
        apply_blur(frame, blur_boxes(D0 + fi / FPS))
    z = float(Z[n]); ch = 1080 / z; cw = ch * W / HH
    x0 = float(np.clip(cx[n] - cw / 2, 0, 1920 - cw)); y0 = float(np.clip(cy[n] - ch / 2, 0, 1080 - ch))
    M = np.array([[W / cw, 0, -x0 * W / cw], [0, HH / ch, -y0 * HH / ch]], np.float32)   # recorte subpíxel: zoom sin saltos
    bot = cv2.warpAffine(frame, M, (W, HH), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    sc = W / cw
    c = cur(s - LAG) if HASC[n] else None
    if c is not None and RING[n] > 0.02:   # aro dorado en el puntero cuando dice "acá/aquí/esto"
        px, py = int((c[0] - x0) * sc), int((c[1] - y0) * sc); r = int(30 + 14 * (1 - RING[n]))
        ov = bot.copy(); cv2.circle(ov, (px, py), r, GOLD, 5, cv2.LINE_AA)
        bot = cv2.addWeighted(ov, float(RING[n]), bot, 1 - float(RING[n]), 0)
    if BOX[n] is not None:                 # caja dorada fina sobre lo que nombra cuando no hay puntero
        bx = BOX[n]; s0 = TS[n][0]; a = next(a for a, bb, *_ in MAN if a <= s0 < bb); f = min(1.0, (s0 - a) / 0.3)
        p0 = (int((bx[0] - x0) * sc), int((bx[1] - y0) * sc)); p1 = (int((bx[2] - x0) * sc), int((bx[3] - y0) * sc))
        ov = bot.copy(); cv2.rectangle(ov, p0, p1, GOLD, 4, cv2.LINE_AA); bot = cv2.addWeighted(ov, f, bot, 1 - f, 0)
    out = np.empty((H, W, 3), np.uint8); out[:HH] = t_img; out[HH:] = bot
    out[HH - 2:HH + 2] = GOLD                                     # separador dorado de 4 px, sin bordes redondos
    enc.stdin.write(out.tobytes())
    log.append([round(n / FPS, 3), round(s, 3), round(float(cx[n])), round(float(cy[n])), round(z, 3), bool(HASC[n])])
enc.stdin.close(); enc.wait(); top.kill(); scr.kill()
json.dump(log, open("plan/zoom_log.json", "w")); print("cuadros", N, "->", OUT)
