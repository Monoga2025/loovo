# FILE: measure_color.py
# Uso: python measure_color.py img1.png [img2.png ...]
# Mide color de forma objetiva (Claude no debe juzgar el color "a ojo"):
# Lab de la pared (zona superior derecha), de la cara (centro alto) y de las
# esquinas (viñeta), más L* medio y percentiles 5/95 (negros/altas luces).
# Referencias de la paleta de motion: crema #F2EEE8 = Lab(94, 0.3, 3.4); negro L* ~3.
# Ajusta las zonas si el encuadre es distinto (coordenadas en 1080x1920).
import subprocess, sys
import numpy as np


def load(p):
    s = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0", p],
                       capture_output=True, text=True).stdout.strip().split(",")
    w, h = int(s[0]), int(s[1])
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(h, w, 3).astype(float)


def lab(rgb):
    c = rgb / 255
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ M.T / np.array([0.95047, 1, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


for p in sys.argv[1:]:
    f = load(p)
    sy, sx = f.shape[0] / 1920, f.shape[1] / 1080
    zone = lambda y0, y1, x0, x1: lab(f[int(y0 * sy):int(y1 * sy), int(x0 * sx):int(x1 * sx)].reshape(-1, 3).mean(0))
    L = lab(f.reshape(-1, 3))[:, 0]
    wall, face, corner = zone(150, 450, 700, 1000), zone(650, 850, 380, 700), zone(0, 200, 0, 200)
    print(f"{p}: pared Lab {np.round(wall, 1)} | cara Lab {np.round(face, 1)} | esquina L* {corner[0]:.1f} | "
          f"L* medio {L.mean():.1f} p5 {np.percentile(L, 5):.1f} p95 {np.percentile(L, 95):.1f}")
