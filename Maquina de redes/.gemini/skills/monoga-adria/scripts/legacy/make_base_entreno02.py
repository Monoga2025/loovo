"""Base de la persona: corte (0,42-2,60 + 2,80-6,14 s de cand1), encuadre fijo + zoom de respiracion
easeInOutSine con warpAffine Lanczos (subpixel, sin temblor) y color G horneado.
Uso: make_base.py cand1.mp4 out.mp4"""
import sys, subprocess, numpy as np, cv2, json
SRC, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, DUR = 1080, 1920, 30, 6.30
GRADE = ("curves=master='0/0.015 0.25/0.25 0.5/0.535 0.8/0.85 1/0.965',"
         "colorbalance=rm=0.06:gm=-0.035:bm=-0.005:rh=0.015:gh=0.0:bh=-0.02,eq=saturation=1.03:contrast=1.02")
S0 = 1.12                    # encuadre base (quita techo y mesa)
ANCH_SRC = (690.0, 640.0)    # cara en el original
ANCH_OUT = (643.0, 549.0)    # donde queda la cara en la salida
Z0, Z1, ZA, ZB = 1.00, 1.07, 2.60, 5.52   # respiracion continua en el tramo de persona
def zoom(t):
    u = min(max((t - ZA) / (ZB - ZA), 0), 1)
    return Z0 + (Z1 - Z0) * (0.5 - 0.5 * np.cos(np.pi * u))   # easeInOutSine = cubic-bezier(.37,0,.63,1)
def src_t(t):
    return t + 0.42 if t < 2.18 else min(t + 0.62, 6.14 - 1 / FPS)
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", SRC, "-vf", "fps=30", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                     capture_output=True, check=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
N = int(round(DUR * FPS))
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS),
                        "-i", "-", "-vf", GRADE + ",format=yuv420p", "-c:v", "libx264", "-crf", "12", "-preset", "slow",
                        "-g", "15", OUT], stdin=subprocess.PIPE)
log = []
for n in range(N):
    t = n / FPS
    i = min(int(round(src_t(t) * FPS)), len(fr) - 1)
    s = S0 * zoom(t)
    M = np.array([[s, 0, ANCH_OUT[0] - s * ANCH_SRC[0]], [0, s, ANCH_OUT[1] - s * ANCH_SRC[1]]])
    o = cv2.warpAffine(fr[i], M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REFLECT)
    enc.stdin.write(o.tobytes())
    log.append({"n": n, "t": round(t, 4), "src_frame": i, "zoom": round(float(zoom(t)), 5), "scale_total": round(float(s), 5)})
enc.stdin.close(); enc.wait()
json.dump(log, open(OUT.replace(".mp4", "_zoom.json"), "w"), indent=0)
print("frames", N, "src frames", len(fr))
