import json
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

x, sr = sf.read(__import__("sys").argv[1])
if x.ndim > 1: x = x.mean(axis=1)
w = json.load(open("build/words_out.json"))
def word_at(t):
    for q in w:
        if q["s"] - 0.03 <= t <= q["e"] + 0.03: return q["w"]
    return "(pausa)"
lo = sosfilt(butter(4, [60, 500], "bandpass", fs=sr, output="sos"), x)
def rms(a, t0, t1):
    i0, i1 = max(0, int(t0*sr)), min(len(a), int(t1*sr))
    seg = a[i0:i1]
    return 20*np.log10(np.sqrt(np.mean(seg**2)) + 1e-9) if len(seg) else -120
blk = int(0.005*sr)
env = np.array([np.max(np.abs(lo[i:i+blk])) for i in range(0, len(lo)-blk, blk)])
res = []
for i in range(12, len(env)-30):
    if env[i] < env[i-1] or env[i] < env[i+1]: continue
    t = i*0.005
    pk = rms(lo, t-0.003, t+0.007)
    before = rms(lo, t-0.080, t-0.020)
    after = rms(lo, t+0.050, t+0.110)
    attack = pk - before
    decay = pk - after
    if attack > 10 and decay > 10:
        res.append((t, attack, decay, pk, word_at(t)))
res.sort()
print("t(s)  ataque_dB  caida_60ms_dB  nivel_dB  palabra")
for r in res: print(f"{r[0]:6.2f} {r[1]:6.1f} {r[2]:7.1f} {r[3]:7.1f}  {r[4]}")
json.dump([(float(r[0]), float(r[1]), float(r[2]), r[4]) for r in res], open("fix/taps_check.json", "w"))
