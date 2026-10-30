"""Base de la persona: tiempos del EDL (video = WAV + aoff), corrección del verde + exposición (grade_verde.fix),
LUT Adrià 75 (ffmpeg lut3d), encuadre con la cara en y~780 y zoom de respiración easeInOutSine; salto de zoom en
cada corte interno. Los huecos siguen el crudo del tramo anterior. -> motion/assets/base.mp4 (1080x1920, 30 fps)"""
import json, math, subprocess, sys, numpy as np, cv2
sys.path.insert(0, "scripts"); from grade_verde import fix
E = json.load(open("plan/edl.json", encoding="utf-8")); FT = json.load(open("plan/face_track.json"))
W, H, FPS = 1080, 1920, 30; TOT = E["total"]; NF = int(round(TOT * FPS)); AO = E["aoff"]
SRC = "../crudo/VID20261017194137.mp4"
# cara suavizada (mediana 1,4 s) en tiempo de video del crudo
ft = np.array([[r[0], r[1] or np.nan, r[2] or np.nan] for r in FT], float)
for c in (1, 2):
    s = ft[:, c]; m = np.isnan(s); s[m] = np.interp(np.flatnonzero(m), np.flatnonzero(~m), s[~m]); 
    ft[:, c] = np.array([np.median(s[max(0, i - 3):i + 4]) for i in range(len(s))])
def face(ts):
    return np.interp(ts, ft[:, 0], ft[:, 1]), np.interp(ts, ft[:, 0], ft[:, 2])
P = E["pieces"]
def piece_at(t):
    for i, p in enumerate(P):
        end = p["o"] + p["b"] - p["a"] + p["gap"]
        if t < end or i == len(P) - 1: return i, p
# programas de zoom: por toma (seg); salto en los cortes
segs = []
for i, p in enumerate(P):
    if not segs or segs[-1][0] != p["seg"]: segs.append([p["seg"], p["o"], 0])
    segs[-1][2] = p["o"] + p["b"] - p["a"] + p["gap"]
def zoom(t, i):
    sid = P[i]["seg"]; s = next(x for x in segs if x[0] == sid); u = (t - s[1]) / max(s[2] - s[1], .1)
    k = segs.index(s)
    if k == 0:                                     # gancho: arranca cerca y baja (movimiento desde el cuadro 0)
        z = 1.26 - 0.12 * (1 - (1 - min(u, 1)) ** 3)
    else:
        lo, hi = (1.10, 1.18) if k % 2 else (1.18, 1.10)
        z = lo + (hi - lo) * (0.5 - 0.5 * math.cos(math.pi * min(u, 1)))
    sub = sum(1 for q in P[:i + 1] if q["seg"] == sid) - 1          # corte interno -> salto de zoom
    return z + (0.07 if sub % 2 else 0.0)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-vf", "lut3d=file=build/adria_look_75.cube:interp=tetrahedral", "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                        "-g", "15", "-pix_fmt", "yuv420p", "motion/assets/base.mp4"], stdin=subprocess.PIPE)
# decodifica por pieza (tramo + hueco) a 30 fps
cache = {}
def frames_for(i):
    p = P[i]; t0 = p["a"] + AO; d = p["b"] - p["a"] + p["gap"] + 0.2
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t0:.3f}", "-i", SRC, "-t", f"{d:.3f}", "-vf", "fps=30", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
cur = None; last = None
cx_s = cy_s = None
for n in range(NF):
    t = n / FPS; i, p = piece_at(t)
    if cur != i: fr = frames_for(i); cur = i
    k = int(round((t - p["o"]) * FPS)); src = fr[min(k, len(fr) - 1)] if len(fr) else last
    ts = p["a"] + AO + (t - p["o"]); cx, cy = face(ts)
    cx_s = cx if cx_s is None or k == 0 else cx_s + (cx - cx_s) * 0.25
    cy_s = cy if cy_s is None or k == 0 else cy_s + (cy - cy_s) * 0.25
    z = zoom(t, i)
    tx, ty = 540 - (cx_s - 540) * 0.0, 780          # cara a y~780; x se queda centrada en la cara con margen
    ox = min(max(540 - cx_s * z, W - W * z), 0); oy = min(max(ty - cy_s * z, H - H * z), 0)
    M = np.float32([[z, 0, ox], [0, z, oy]])
    g = fix(src); out = cv2.warpAffine(g, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    enc.stdin.write(out.tobytes()); last = src
    if n % 300 == 0: print("cuadro", n, "/", NF, flush=True)
enc.stdin.close(); enc.wait(); print("ok", NF)
