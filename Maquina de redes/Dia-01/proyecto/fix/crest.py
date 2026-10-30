import json
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

x, sr = sf.read("build/cut_audio.wav")
if x.ndim > 1: x = x.mean(axis=1)
w = json.load(open("build/words_out.json"))
def word_at(t):
    for q in w:
        if q["s"] - 0.03 <= t <= q["e"] + 0.03: return q["w"]
    return "(pausa)"
lo = sosfilt(butter(4, 400, "low", fs=sr, output="sos"), x)
hi = sosfilt(butter(4, 3000, "high", fs=sr, output="sos"), x)
blk = int(0.010 * sr)
n = len(x) // blk
rows = []
for i in range(n):
    seg = x[i*blk:(i+1)*blk]
    a = max(0, i - 15); b = min(n, i + 16)
    ctx = np.concatenate([x[j*blk:(j+1)*blk] for j in range(a, b) if abs(j - i) > 2]) if b - a > 5 else seg
    rms_ctx = np.sqrt(np.mean(ctx**2)) + 1e-9
    pk = np.max(np.abs(seg))
    crest = 20*np.log10(pk / rms_ctx)
    e_lo = np.sqrt(np.mean(lo[i*blk:(i+1)*blk]**2)) + 1e-9
    e_hi = np.sqrt(np.mean(hi[i*blk:(i+1)*blk]**2)) + 1e-9
    rows.append((i*0.010, crest, 20*np.log10(pk), 20*np.log10(e_lo/e_hi), 20*np.log10(rms_ctx)))
rows.sort(key=lambda r: -r[1])
print("t(s)  crest_dB  pico_dBFS  bajos-vs-agudos_dB  ctx_dBFS  palabra")
for r in rows[:30]:
    print(f"{r[0]:6.2f} {r[1]:6.1f} {r[2]:7.1f} {r[3]:7.1f} {r[4]:7.1f}  {word_at(r[0])}")
