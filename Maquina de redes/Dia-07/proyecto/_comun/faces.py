"""Centro de la cara (Haar, mediana de 7 cuadros) en un rango del crudo. Uso: faces.py a-b [a-b ...]"""
import sys, subprocess, numpy as np, cv2
SRC = "C:/Users/you/Desktop/VID_20261013_110529.mp4"
cc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
for r in sys.argv[1:]:
    a, b = map(float, r.split("-")); pts = []
    for k in range(7):
        t = a + (k + 0.5) * (b - a) / 7
        raw = subprocess.run(["ffmpeg", "-v", "error", "-threads", "1", "-ss", f"{t:.3f}", "-i", SRC, "-frames:v", "1", "-vf", "scale=540:960", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
        if len(raw) != 960 * 540: continue
        g = np.frombuffer(raw, np.uint8).reshape(960, 540)
        f = cc.detectMultiScale(g, 1.1, 5, minSize=(50, 50))
        if len(f): x, y, w, h = max(f, key=lambda q: q[2] * q[3]); pts.append(((x + w / 2) * 2, (y + h / 2) * 2, w * 2))
    p = np.median(np.array(pts), 0) if pts else None
    print(r, None if p is None else [int(v) for v in p], len(pts))
