"""Centro de la cara (Haar, mediana de 9 cuadros) en la ventana VISIBLE de cada tramo de persona -> plan/faces.json"""
import json, subprocess, numpy as np, cv2
SRC = "../../VID20261011112118.mp4"
WIN = {"H3": (28.9, 31.6), "C2": (40.5, 43.4), "D3": (70.8, 72.1), "P1": (107.9, 111.1), "P2": (118.1, 119.9),
       "R2": (138.3, 140.5), "R4b": (167.1, 169.8)}
cc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml"); res = {}
for sid, (a, b) in WIN.items():
    pts = []
    for k in range(9):
        t = a + (k + 0.5) * (b - a) / 9
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", SRC, "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
        g = np.frombuffer(raw, np.uint8).reshape(1920, 1080)
        f = cc.detectMultiScale(cv2.resize(g, (540, 960)), 1.1, 5, minSize=(60, 60))
        if len(f):
            x, y, w, h = max(f, key=lambda r: r[2] * r[3]); pts.append(((x + w / 2) * 2, (y + h / 2) * 2, w * 2))
    if pts:
        p = np.median(np.array(pts), 0); res[sid] = [round(float(p[0])), round(float(p[1])), round(float(p[2])), len(pts)]
    print(sid, res.get(sid))
json.dump(res, open("plan/faces.json", "w"), indent=1)
