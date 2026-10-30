"""Base de persona (solo la ventana en que se ve: B1..B3b) -> motion/assets/base.mp4 (empieza en W0 de la línea).
Piezas contiguas (bordes en mitad de los huecos), encuadre a la cara, zoom easeInOutSine (warpAffine Lanczos subpíxel),
saltos de zoom en los cortes, zoom-through power4.in al final + desenfoque radial 4 cuadros. LUT Adrià 75 % horneado."""
import json, subprocess, numpy as np, cv2
E = {s["id"]: s for s in json.load(open("plan/edl.json", encoding="utf-8"))["segs"]}
W, H, FPS = 1080, 1920, 30; LUT = "assets_src/adria_look_75.cube"; S0 = 1.12; FACE_OUT_Y = 700
W0, W1 = 3.40, 13.50
sine = lambda u: 0.5 - 0.5 * np.cos(np.pi * u); p4 = lambda u: u ** 4
# pieza: (seg, t_ini, t_fin, cara, programa de zoom [(t_rel, z, curva)])
P = [("B1", W0, 5.17, (760, 790), [(0, 1.14, None), (1.77, 1.06, sine)]),
     ("B2", 5.17, 10.50, (800, 800), [(0, 1.00, None), (5.33, 1.075, sine)]),
     ("B3a", 10.50, 11.44, (840, 815), [(0, 1.11, None), (0.94, 1.13, sine)]),
     ("B3b", 11.44, W1, (870, 825), [(0, 1.02, None), (1.55, 1.07, sine), (2.06, 1.42, p4)])]
RAD = [0.98, 0.94, 0.88, 0.78]
def zoom(k, tr):
    if tr <= k[0][0]: return k[0][1]
    for (a, za, _), (b, zb, f) in zip(k, k[1:]):
        if tr <= b: return za + (zb - za) * f(min(max((tr - a) / (b - a), 0), 1))
    return k[-1][1]
def M_for(s, face):
    fx, fy = face
    cx = min(max(fx, W / 2 / s), W - W / 2 / s)
    cy = min(max(fy + (H / 2 - FACE_OUT_Y) / s, H / 2 / s), H - H / 2 / s)
    return np.array([[s, 0, W / 2 - s * cx], [0, s, H / 2 - s * cy]])
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-vf", f"lut3d=file={LUT}:interp=tetrahedral,format=yuv420p", "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-g", "30",
                        "motion/assets/base.mp4"], stdin=subprocess.PIPE)
n0, n1 = int(round(W0 * FPS)), int(round(W1 * FPS)); log = []
for sid, a, b, face, prog in P:
    s = E[sid]; src0 = s["t0"] - (s["start"] - a)
    fa, fb = max(int(round(a * FPS)), n0), min(int(round(b * FPS)), n1); nf = fb - fa
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{src0:.4f}", "-i", s["src"], "-t", f"{nf / FPS + 0.2:.4f}", "-vf", "fps=30,scale=1080:1920",
                          "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
    last = None
    for j in range(nf):
        buf = p.stdout.read(W * H * 3)
        if len(buf) == W * H * 3: last = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        tr = (fa + j) / FPS - a; z = zoom(prog, tr); sc = S0 * z
        k = (fb - 1 - j) if sid == "B3b" else 99
        if k < len(RAD):
            rel = RAD[len(RAD) - 1 - k]; spread = (1 - rel) * 0.9; acc = np.zeros((H, W, 3), np.float32)
            for q in range(12):
                acc += cv2.warpAffine(last, M_for(sc * rel * (1 + spread * q / 11), face), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
            o = (acc / 12).astype(np.uint8)
        else:
            o = cv2.warpAffine(last, M_for(sc, face), (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
        enc.stdin.write(o.tobytes()); log.append(dict(n=fa + j, seg=sid, src=round(src0 + j / FPS, 4), z=round(float(z), 4)))
    p.stdout.close(); p.wait()
enc.stdin.close(); enc.wait(); json.dump(log, open("motion/assets/base_log.json", "w"), indent=0); print("cuadros", len(log), n1 - n0)
