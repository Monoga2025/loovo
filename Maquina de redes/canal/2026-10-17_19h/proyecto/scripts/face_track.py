"""Cara a 5 fps (YuNet, 540x960) + nitidez y apertura de boca aprox. -> plan/face_track.json
fila: [t, cx, cy, w, nitidez, ojos_y]  (coordenadas en 1080x1920)"""
import json, subprocess, numpy as np, cv2
d = cv2.FaceDetectorYN.create("build/yunet.onnx", "", (540, 960), 0.6)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", "../crudo/VID20261017194137.mp4", "-vf", "fps=5,scale=540:960", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
out, k = [], 0
while True:
    b = p.stdout.read(540 * 960 * 3)
    if len(b) < 540 * 960 * 3: break
    im = np.frombuffer(b, np.uint8).reshape(960, 540, 3)
    _, f = d.detect(im)
    r = [round(k / 5, 2), None, None, None, 0, None]
    if f is not None and len(f):
        x, y, w, h = [int(v) for v in max(f, key=lambda r: r[2] * r[3])[:4]]
        g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)[max(y, 0):y + h, max(x, 0):x + w]
        fr = max(f, key=lambda r: r[2] * r[3])
        r = [round(k / 5, 2), int((x + w / 2) * 2), int((y + h / 2) * 2), int(w * 2), round(float(cv2.Laplacian(g, cv2.CV_64F).var()), 1), int((fr[5] + fr[7]) )]
    out.append(r); k += 1
json.dump(out, open("plan/face_track.json", "w"))
print("cuadros", k, "con cara", sum(1 for r in out if r[1]))
