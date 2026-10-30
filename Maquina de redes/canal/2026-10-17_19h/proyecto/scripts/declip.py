"""Reconstruye picos recortados (|x| >= 0,97) con spline cúbico desde 8 muestras a cada lado. Salida float (picos > 1).
Uso: declip.py in.wav out.wav"""
import sys, numpy as np, soundfile as sf
from scipy.interpolate import CubicSpline
x, sr = sf.read(sys.argv[1]); x = x if x.ndim == 1 else x.mean(1); y = x.astype(np.float64).copy()
T, K = 0.97, 8
c = np.abs(x) >= T
d = np.diff(np.r_[0, c.astype(int), 0]); S = np.where(d == 1)[0]; E = np.where(d == -1)[0]
n = 0
for s, e in zip(S, E):
    if e - s > 120 or s < K or e + K > len(x): continue
    idx = np.r_[np.arange(s - K, s), np.arange(e, e + K)]
    good = idx[np.abs(x[idx]) < T]
    if len(good) < 6: continue
    cs = CubicSpline(good, x[good]); seg = cs(np.arange(s, e))
    sg = np.sign(x[s:e]); seg = np.where(np.abs(seg) < np.abs(x[s:e]), x[s:e], seg)   # nunca por debajo del recorte
    y[s:e] = np.clip(seg, -2.5, 2.5) * (sg == np.sign(seg)) + x[s:e] * (sg != np.sign(seg)); n += 1
sf.write(sys.argv[2], y.astype(np.float32), sr, subtype="FLOAT")
print("tramos reparados", n, "de", len(S), "pico nuevo", round(float(np.abs(y).max()), 3))
