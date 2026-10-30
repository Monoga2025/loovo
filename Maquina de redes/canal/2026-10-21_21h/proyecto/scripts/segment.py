# FILE: segment.py
# Uso: python3 segment.py entrada.mp4 mascara.mp4 [--test t1,t2,...]
# Máscara de la persona (blanco = persona) fotograma a fotograma con rembg/u2net,
# local. Suavizado temporal (mediana de 3 fotogramas) para evitar parpadeo en
# los bordes, y un leve feather. Salida: video gris 1080x1920 del mismo fps.
import os, subprocess, sys, time
import numpy as np
from PIL import Image, ImageFilter

os.environ.setdefault("U2NET_HOME", os.path.expanduser("~/.rembg/models/u2net"))
from rembg import new_session  # noqa: E402

src, out = sys.argv[1], sys.argv[2]
test = sys.argv[4].split(",") if len(sys.argv) > 3 and sys.argv[3] == "--test" else None
W, H, SW, SH = 1080, 1920, 540, 960
session = new_session("u2net")


def predict(rgb):
    small = Image.fromarray(rgb).resize((SW, SH), Image.BILINEAR)
    m = session.predict(small)[0].convert("L").resize((W, H), Image.BILINEAR)
    return np.asarray(m.filter(ImageFilter.GaussianBlur(1.5)), np.float32)


def frames(path, ss=None, n=None):
    cmd = ["ffmpeg", "-v", "error"] + (["-ss", ss] if ss else []) + ["-i", path]
    cmd += (["-frames:v", str(n)] if n else []) + ["-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3:
            break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)


if test:
    for t in test:
        t0 = time.time()
        rgb = next(frames(src, t, 1))
        m = predict(rgb)
        Image.fromarray(m.astype(np.uint8)).save(f"{out}_{t}.png")
        print(f"t={t}s: {time.time() - t0:.2f}s/fotograma")
    sys.exit()

enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray",
                        "-s", f"{W}x{H}", "-r", "30", "-i", "-", "-c:v", "libx264", "-crf", "12",
                        "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
prev, cur, n, t0 = None, None, 0, time.time()
for rgb in frames(src):
    nxt = predict(rgb)
    if cur is not None:
        win = [x for x in (prev, cur, nxt) if x is not None]
        enc.stdin.write(np.median(np.stack(win), 0).astype(np.uint8).tobytes())
        n += 1
        if n % 100 == 0:
            print(f"{n} fotogramas ({(time.time() - t0) / n:.2f}s/f)", flush=True)
    prev, cur = cur, nxt
win = [x for x in (prev, cur) if x is not None]
enc.stdin.write(np.median(np.stack(win), 0).astype(np.uint8).tobytes())
enc.stdin.close()
enc.wait()
print(f"{n + 1} fotogramas -> {out}")
