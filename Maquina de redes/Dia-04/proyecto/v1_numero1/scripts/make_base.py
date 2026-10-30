"""Base de persona para toda la línea final: corte por EDL + encuadre a la cara + zoom de respiración
(easeInOutSine, warpAffine Lanczos subpíxel) + zoom-through (power4.in) + zoom-out con desenfoque radial
(entrada al motion graphic) + LUT Adrià 75 % horneado. Uso: make_base.py [out.mp4]"""
import sys, json, subprocess, numpy as np, cv2
OUT = sys.argv[1] if len(sys.argv) > 1 else "motion/assets/base.mp4"
E = json.load(open("plan/edl.json", encoding="utf-8")); FACES = json.load(open("plan/faces.json"))
W, H, FPS = 1080, 1920, 30
LUT = "assets_src/adria_look_75.cube"  # copia de .claude/skills/monoga-adria/assets
S0 = 1.10                     # encuadre base
FACE_OUT_Y = 660              # dónde queremos la cara en la salida (se recorta al margen disponible)
sine = lambda u: 0.5 - 0.5 * np.cos(np.pi * u)
p4in = lambda u: u ** 4
# programas de zoom por tramo: [(t_rel, z, curva_hacia_este_punto)]
Z = {   # solo importan las ventanas visibles (persona); lo demás queda bajo el motion
 "H3":  [(0, 1.16, None), (2.88, 1.16, sine), ("end", 1.03, sine)],
 "C2":  [(0, 1.00, None), (0.42, 1.00, sine), ("end", 1.07, sine)],
 "D3":  [(0, 1.02, None), ("end", 1.11, sine)],
 "P1":  [(0, 1.00, None), (3.2, 1.13, sine)],            # sigue en el silencio (mano en la cara) con empuje lento
 "P2":  [(0, 1.03, None), ("end", 1.12, sine)],          # salto de zoom 1,13 -> 1,03 tapa el corte
 "R2":  [(0, 1.00, None), ("end", 1.07, sine)],
 "R4b": [(0, 1.10, None), (6.9, 1.10, sine), (9.7, 1.00, sine)],
}
RADIAL = {"D3": [0.98, 0.94, 0.88, 0.78], "P2": [0.98, 0.94, 0.88, 0.78], "R2": [0.98, 0.94, 0.88, 0.78]}
def zoom(sid, tr, dur):
    k = Z.get(sid, [(0, 1.0, None)])
    k = [(dur if a == "end" else a, z, f) for a, z, f in k]
    if tr <= k[0][0]: return k[0][1]
    for (a, za, _), (b, zb, f) in zip(k, k[1:]):
        if tr <= b: return za + (zb - za) * f(min(max((tr - a) / (b - a), 0), 1))
    return k[-1][1]
def M_for(s, face):
    fx, fy = face
    cx = min(max(fx, W / 2 / s), W - W / 2 / s)
    cy = min(max(fy + (H / 2 - FACE_OUT_Y) / s, H / 2 / s), H - H / 2 / s) if s >= 1 else fy
    return np.array([[s, 0, W / 2 - s * cx], [0, s, H / 2 - s * cy]])
class Reader:
    def __init__(self, seg):
        d = seg["dur"] + 3.0
        self.p = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", f"{seg['t0']:.4f}", "-i", seg["src"], "-t", f"{d:.4f}",
                                   "-vf", "fps=30", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
        self.j, self.last = -1, None
    def get(self, j):
        while self.j < j:
            b = self.p.stdout.read(W * H * 3)
            if len(b) < W * H * 3: break
            self.last = np.frombuffer(b, np.uint8).reshape(H, W, 3); self.j += 1
        return self.last
    def close(self): self.p.stdout.close(); self.p.wait()
NF = int(round(E["total"] * FPS))
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-vf", f"lut3d=file={LUT}:interp=tetrahedral,format=yuv420p", "-c:v", "libx264", "-crf", "14", "-preset", "medium",
                        "-g", "30", OUT], stdin=subprocess.PIPE)
segs = [s for s in E["segs"]]; log = []; prev = None; readers = {}
for n in range(NF):
    t = n / FPS
    s = next((x for x in segs if x["start"] - 1e-6 <= t < x["end"] - 1e-6), None)
    if s is None or not s["cam"]:   # hueco o placa: sigue el crudo del tramo anterior (sin congelar)
        s = max((x for x in segs if x["cam"] and x["start"] <= t), key=lambda x: x["start"])
    sid = s["id"]
    if sid not in readers:
        for r in readers.values(): r.close()
        readers = {sid: Reader(s)}
    tr = t - s["start"]; j = int(round(tr * FPS))
    fr = readers[sid].get(j)
    face = FACES.get(sid, [540, 800])[:2]
    z = zoom(sid, tr, s["dur"]); sc = S0 * z
    tr = min(tr, s["dur"] + 0.6) if False else tr
    nlast = int(round(s["dur"] * FPS)) - 1 - j      # 0 = último cuadro del tramo
    rad = RADIAL.get(sid)
    if rad and 0 <= nlast < len(rad):
        rel = rad[len(rad) - 1 - nlast]; spread = (1 - rel) * 0.9
        acc = np.zeros((H, W, 3), np.float32); K = 12
        for k in range(K):
            sk = sc * rel * (1 + spread * k / (K - 1))
            acc += cv2.warpAffine(fr, M_for(sk, face), (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        o = (acc / K).astype(np.uint8); z = z * rel
    else:
        o = cv2.warpAffine(fr, M_for(sc, face), (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    enc.stdin.write(o.tobytes()); prev = o
    log.append({"n": n, "seg": sid, "src_t": round(s["t0"] + j / FPS, 4), "zoom": round(float(z), 5)})
for r in readers.values(): r.close()
enc.stdin.close(); enc.wait()
json.dump(log, open(OUT.replace(".mp4", "_zoom.json"), "w"), indent=0)
print("frames", NF)
