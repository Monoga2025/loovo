"""Centro de la cara (mediana de 7 cuadros, Haar) por tramo de persona -> plan/faces.json"""
import json, subprocess, numpy as np, cv2
E = json.load(open("plan/edl.json", encoding="utf-8"))
cc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
res = {}
for s in E["segs"]:
    if not s["cam"]: continue
    pts = []
    for k in range(7):
        t = s["t0"] + (k + 0.5) * s["dur"] / 7
        raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", s["src"], "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True).stdout
        g = np.frombuffer(raw, np.uint8).reshape(1920, 1080)
        f = cc.detectMultiScale(cv2.resize(g, (540, 960)), 1.1, 5, minSize=(60, 60))
        if len(f):
            x, y, w, h = max(f, key=lambda r: r[2] * r[3]); pts.append(((x + w / 2) * 2, (y + h / 2) * 2, w * 2))
    if pts:
        p = np.median(np.array(pts), 0); res[s["id"]] = [round(float(p[0])), round(float(p[1])), round(float(p[2])), len(pts)]
    print(s["id"], res.get(s["id"]))
json.dump(res, open("plan/faces.json", "w"), indent=1)
