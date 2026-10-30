"""Post: 'invert flash' a la salida del motion graphic (Adrià 5:35, 7 cuadros a 25 fps -> 8 a 30 fps) + mezcla final.
Lee build/motion.mp4 (render HyperFrames) y audio/final.wav; escribe el MP4 final (H.264 CRF 18, AAC 48 kHz 320k).
Uso: post_fx.py salida.mp4"""
import sys, json, subprocess, numpy as np, cv2
OUT = sys.argv[1]; W, H, FPS = 1080, 1920, 30
E = {s["id"]: s for s in json.load(open("plan/edl.json", encoding="utf-8"))["segs"]}
CUT = int(round((E["PR3"]["start"] + 3 / FPS) * FPS))       # primer cuadro de la persona (el MG se oculta aquí)
P = lambda pts: np.array([[x * W, y * H] for x, y in pts], np.int32)
# (cuadro relativo al corte, polígono invertido, flash blanco, sobreexposición)
FX = {-3: (P([(.55, 1), (1, .78), (1, 1)]), 0.0, 1.35), -2: (P([(.40, 1), (1, .66), (1, 1)]), 0.0, 1.35),     # entra el borde diagonal ~20°
      -1: (P([(0, .55), (1, .20), (1, 1), (0, 1)]), 0.45, 1.5),                                                # pico: casi todo negativo + destello
       0: (P([(0, 0), (1, 0), (1, .75), (0, .12)]), 0.0, 1.3),                                                 # ya es la persona; arriba aún negativa
       1: (P([(.70, 0), (1, 0), (1, .30)]), 0.0, 1.25), 2: (P([(.74, 0), (1, 0), (1, .26)]), 0.0, 1.25),         # triángulo sobreexpuesto
       3: (P([(0, 0), (1, 0), (1, .60), (0, .30)]), 0.0, 1.3)}                                                 # rebote de un cuadro
def fx(fr, poly, flash, gain):
    m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [poly], 255)
    m = cv2.GaussianBlur(m, (0, 0), 1.5).astype(np.float32)[..., None] / 255
    inv = np.clip((255 - fr.astype(np.float32)) * gain + 25, 0, 255)
    o = fr * (1 - m) + inv * m
    if flash: o = o * (1 - flash) + 255 * flash
    return np.clip(o, 0, 255).astype(np.uint8)
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", "build/motion.mp4", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                        "-i", "audio/final.wav", "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "18", "-preset", "slow",
                        "-pix_fmt", "yuv420p", "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                        "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "-shortest", "-movflags", "+faststart", OUT], stdin=subprocess.PIPE)
n = 0
while True:
    b = dec.stdout.read(W * H * 3)
    if len(b) < W * H * 3: break
    fr = np.frombuffer(b, np.uint8).reshape(H, W, 3)
    k = n - CUT
    if k in FX: fr = fx(fr, *FX[k])
    enc.stdin.write(fr.tobytes()); n += 1
enc.stdin.close(); enc.wait(); print("cuadros", n, "corte MG->persona en", CUT, f"({CUT / FPS:.3f} s)")
