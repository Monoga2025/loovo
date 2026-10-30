"""Base de persona en la línea final (adaptado de make_base.py de monoga-adria):
corte por piezas del EDL + encuadre a la cara (track suavizado) + zoom de respiración easeInOutSine + saltos de zoom
en cada corte interno + zoom-through power4.in + zoom-out radial (4 cuadros) antes de cada motion graphic
+ quitar derrame verde (degreen.py) + LUT Adrià 75 % horneada. Uso: make_base2.py out.mp4"""
import sys, json, subprocess, numpy as np, cv2
sys.path.insert(0, "scripts")
from degreen import degreen
OUT = sys.argv[1]
SRC = "../crudo/VID20261017190855.mp4"
E = json.load(open("plan/edl.json")); P = E["pieces"]
W, H, FPS = 1080, 1920, 30
LUT = "assets/adria_look_75.cube"
S0, FACE_OUT_Y = 1.10, 660
AOFF = 0.133396   # el audio del crudo empieza 0,1334 s después del video: la EDL está en tiempo del wav
sine = lambda u: 0.5 - 0.5 * np.cos(np.pi * u)
p4in = lambda u: u ** 4
# (t0, t1, z0, z1, curva) en tiempo de salida
Z = [(0.00, 3.27, 1.16, 1.05, sine),
     (9.50, 11.745, 1.00, 1.05, sine), (11.745, 12.005, 1.09, 1.09, sine), (12.005, 13.40, 1.02, 1.06, sine), (13.40, 13.95, 1.06, 1.48, p4in),
     (25.33, 26.62, 1.10, 1.03, sine),
     (35.72, 37.72, 1.00, 1.06, sine),
     (46.92, 47.975, 1.02, 1.06, sine), (47.975, 49.485, 1.10, 1.05, sine), (49.485, 51.39, 1.00, 1.05, sine),
     (51.39, 52.705, 1.09, 1.04, sine), (52.705, 53.015, 1.00, 1.00, sine), (53.015, 54.855, 1.08, 1.03, sine),
     (54.855, 57.91, 1.00, 1.07, sine), (57.91, E["total"] + 1, 1.10, 1.02, sine)]
RADIAL_END = [3.27, 26.62, 37.72]       # último cuadro de persona antes del gráfico (zoom-out radial)
RAD = [0.98, 0.94, 0.88, 0.78]
def zoom(t):
    for a, b, z0, z1, f in Z:
        if a - 1e-6 <= t < b: return z0 + (z1 - z0) * f(min(max((t - a) / (b - a), 0), 1))
    return 1.0
def src_time(t):
    prev = None
    for p in P:
        if p["o"] - 1e-6 <= t < p["o"] + p["b"] - p["a"]: return p["a"] + t - p["o"]
        if p["o"] <= t: prev = p
    return prev["b"] + (t - (prev["o"] + prev["b"] - prev["a"]))   # hueco: sigue el crudo (sin congelar)
# cara: interpolada y suavizada (sigma 0,7 s) sobre el tiempo del crudo
T = json.load(open("plan/face_track.json"))
tt = np.array([r[0] for r in T]); ok = np.array([r[1] is not None for r in T])
cx = np.interp(tt, tt[ok], [r[1] for r in T if r[1] is not None]); cy = np.interp(tt, tt[ok], [r[2] for r in T if r[2] is not None])
k = np.exp(-0.5 * (np.arange(-6, 7) / 1.4) ** 2); k /= k.sum()
cx = np.convolve(np.pad(cx, 6, mode="edge"), k, "valid"); cy = np.convolve(np.pad(cy, 6, mode="edge"), k, "valid")
face = lambda ts: (float(np.interp(ts, tt, cx)), float(np.interp(ts, tt, cy)))
def M_for(s, f):
    fx, fy = f
    x = min(max(fx, W / 2 / s), W - W / 2 / s)
    y = min(max(fy + (H / 2 - FACE_OUT_Y) / s, H / 2 / s), H - H / 2 / s)
    return np.array([[s, 0, W / 2 - s * x], [0, s, H / 2 - s * y]])
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", "155.0", "-i", SRC, "-vf", "fps=30", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
cache = {"j": -1, "fr": None}
def frame_at(ts):   # lectura secuencial con búsqueda hacia delante (las piezas van en orden creciente)
    j = int(round((ts - 155.0) * FPS))
    if j < cache["j"]: raise RuntimeError("retroceso en el crudo")
    while cache["j"] < j:
        b = dec.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        cache["fr"] = np.frombuffer(b, np.uint8).reshape(H, W, 3); cache["j"] += 1
    return cache["fr"]
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-vf", f"lut3d=file={LUT}:interp=tetrahedral,eq=brightness=0.02:gamma=1.06,format=yuv420p",
                        "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-g", "30", OUT], stdin=subprocess.PIPE)
NF = int(round(E["total"] * FPS)); log = []
for n in range(NF):
    t = n / FPS; ts = src_time(t) + AOFF; fr = degreen(frame_at(ts)); f = face(ts)
    z = zoom(t); sc = S0 * z
    nr = next(((int(round(e * FPS)) - 1 - n) for e in RADIAL_END if 0 <= int(round(e * FPS)) - 1 - n < 4), None)
    if nr is not None:
        rel = RAD[3 - nr]; spread = (1 - rel) * 0.9; acc = np.zeros((H, W, 3), np.float32)
        for q in range(12):
            acc += cv2.warpAffine(fr, M_for(sc * rel * (1 + spread * q / 11), f), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        o = (acc / 12).astype(np.uint8)
    else:
        o = cv2.warpAffine(fr, M_for(sc, f), (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    enc.stdin.write(o.tobytes()); log.append([n, round(ts, 3), round(z, 4)])
dec.stdout.close(); dec.kill(); enc.stdin.close(); enc.wait()
json.dump(log, open(OUT.replace(".mp4", "_log.json"), "w"))
print("cuadros", NF)
