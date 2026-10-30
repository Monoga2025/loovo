"""Mide el ducking: nivel (RMS con ponderación K aprox. = ebur128 momentáneo) de voz y música en cada tramo hablado,
ya con la ganancia final. Imprime diferencia por tramo."""
import json, numpy as np, soundfile as sf
from scipy import signal
E = json.load(open("plan/edl.json", encoding="utf-8")); P = json.load(open("audio/mix_params.json")); g = 10 ** (P["final_gain_db"] / 20)
v, sr = sf.read("audio/stem_voz.wav"); m, _ = sf.read("audio/stem_mus.wav")
# ponderación K (aprox.): shelf +4 dB > 1,5 kHz y HPF 38 Hz
b1, a1 = signal.butter(2, 38, "high", fs=sr); 
def kw(x):
    y = signal.lfilter(b1, a1, x, axis=0)
    hs = signal.butter(1, 1500, "high", fs=sr, output="sos"); return y + (10 ** (4 / 20) - 1) * signal.sosfilt(hs, y, axis=0)
v, m = kw(v * g), kw(m * g)
def db(x): return 10 * np.log10(np.mean(x ** 2) + 1e-12)
d = []
for s in E["segs"]:
    if s["r0"] is None: continue
    a, b = int(s["start"] * sr), int(s["end"] * sr)
    # solo ventanas de 400 ms con voz activa
    w = int(0.4 * sr); vals = []
    for i in range(a, b - w, w // 2):
        lv, lm = db(v[i:i + w]), db(m[i:i + w])
        if lv > -30: vals.append(lv - lm)
    if vals: d.append(min(vals)); print(f"{s['id']:4s} voz-música: mediana {np.median(vals):5.1f} dB, mínimo {min(vals):5.1f} dB")
print("MÍNIMO GLOBAL", round(min(d), 1), "dB")
