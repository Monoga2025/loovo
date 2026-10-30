"""Ajusta bordes aproximados (tiempo del celular) al primer/último sonido real del mic del PC y lista pausas internas > 0,45 s."""
import sys, json, numpy as np, soundfile as sf
x, sr = sf.read("audio/B_pc15.wav"); B = 15.0; h = int(0.01 * sr)
n = len(x) // h; env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
TH = -50
def idx(t): return int(round((t - B) * 100))
SEG = json.load(open(sys.argv[1], encoding="utf-8"))
for sid, a, b, *_ in SEG:
    i0, i1 = idx(a - 0.3), idx(a + 0.4)
    on = i0 + int(np.argmax(env[i0:i1] > TH)) if (env[i0:i1] > TH).any() else idx(a)
    j0, j1 = idx(b - 0.4), idx(b + 0.3)
    loud = np.where(env[j0:j1] > TH)[0]
    off = j0 + int(loud[-1]) if len(loud) else idx(b)
    ta, tb = on / 100 + B, off / 100 + B
    v = env[on:off] > TH; pauses = []; k = 0
    while k < len(v):
        if not v[k]:
            s = k
            while k < len(v) and not v[k]: k += 1
            if (k - s) >= 45: pauses.append((round((on + s) / 100 + B, 2), round((on + k) / 100 + B, 2)))
        k += 1
    print(f"{sid:4s} ~{a:7.2f}-{b:7.2f}  -> voz {ta:7.2f}-{tb:7.2f}  dur {tb - ta:5.2f}  pausas {pauses}")
