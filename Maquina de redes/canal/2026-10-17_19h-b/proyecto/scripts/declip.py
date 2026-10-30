"""Reconstruye picos recortados (techo plano) con un ajuste cúbico a los vecinos de cada tramo.
Uso: declip.py in.wav out.wav [umbral]. Salida a la mitad de ganancia (los picos rehechos pasan de 1,0)."""
import sys, numpy as np, soundfile as sf
x, sr = sf.read(sys.argv[1]); x = x if x.ndim == 1 else x.mean(1)
thr = float(sys.argv[3]) if len(sys.argv) > 3 else 0.975
c = np.abs(x) >= thr
d = np.diff(np.r_[0, c.astype(np.int8), 0]); st = np.where(d == 1)[0]; en = np.where(d == -1)[0]
y = x.copy(); K = 6; n_fix = 0
for a, b in zip(st, en):
    if a - K < 0 or b + K > len(x) or b - a > 200: continue
    idx = np.r_[a - K:a, b:b + K]
    if np.any(c[idx]): idx = idx[~c[idx]]
    if len(idx) < 6: continue
    p = np.polyfit(idx - a, x[idx], 3)
    t = np.arange(a, b); f = np.polyval(p, t - a)
    s = np.sign(x[a:b].mean())
    m = np.maximum(np.abs(f), np.abs(x[a:b]))                    # nunca por debajo del recorte
    cap = 1.6; pk = m.max()
    if pk > cap: m = thr + (m - thr) * (cap - thr) / (pk - thr)  # escala la cúpula (sin techo nuevo)
    f = s * np.maximum(m, np.abs(x[a:b]))
    y[a:b] = f; n_fix += 1
sf.write(sys.argv[2], (y * 0.5).astype(np.float32), sr, subtype="FLOAT")
print("tramos", len(st), "rehechos", n_fix, "pico nuevo", round(float(np.abs(y).max()), 3))
