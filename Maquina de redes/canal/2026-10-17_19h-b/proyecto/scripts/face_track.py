"""Cara (Haar) cada 0,5 s en todo el crudo -> plan/face_track.json [[t, cx, cy, w] | [t, null...]]"""
import json, subprocess, numpy as np, cv2
SRC = "../crudo/VID20261017190855.mp4"
det = cv2.FaceDetectorYN.create("build/yunet.onnx", "", (540, 960), 0.7)
p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", SRC, "-vf", "fps=2,scale=540:960", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
out = []; k = 0
while True:
    b = p.stdout.read(540 * 960 * 3)
    if len(b) < 540 * 960 * 3: break
    g = np.frombuffer(b, np.uint8).reshape(960, 540, 3)
    _, f = det.detect(g); f = [] if f is None else f[:, :4]
    t = k / 2; k += 1
    if len(f):
        x, y, w, h = max(f, key=lambda r: r[2] * r[3]); out.append([t, float((x + w / 2) * 2), float((y + h / 2) * 2), float(w * 2)])
    else: out.append([t, None, None, None])
json.dump(out, open("plan/face_track.json", "w"))
ok = [o for o in out if o[1] is not None]
print(len(out), "muestras,", len(ok), "con cara; cx mediana", np.median([o[1] for o in ok]), "cy", np.median([o[2] for o in ok]), "w", np.median([o[3] for o in ok]))
