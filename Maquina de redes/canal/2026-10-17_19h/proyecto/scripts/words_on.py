"""Palabras del corte: corrige texto (no tiempos) y afina el inicio con la envolvente de audio/voz.wav -> plan/words_on.json"""
import json, numpy as np, soundfile as sf
W = json.load(open("transcript/words_cut.json", encoding="utf-8"))
FIX = {"¿Sabes": "¿Ustedes", "Ingeniero": "ingeniero", "Mecatrónico": "mecatrónico", "corrijes": "corriges", "lobo": "Loovo", "a@64.45": "de"}
for w in W:
    k = f"{w['w']}@{w['s']:.2f}"
    if k in FIX: w["w"] = FIX[k]
    elif w["w"] in FIX: w["w"] = FIX[w["w"]]
x, sr = sf.read("audio/voz.wav"); x = x if x.ndim == 1 else x.mean(1); h = sr // 100; n = len(x) // h
env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
prev = 0
for i, w in enumerate(W):
    if i == 0 or w["s"] - W[i - 1]["e"] > 0.15:     # tras pausa: primer cruce de -40 dB
        lo = W[i - 1]["e"] + 0.05 if i else 0
        i0 = max(int(max(w["s"] - 0.45, lo) * 100), prev); i1 = int((w["s"] + 0.25) * 100)
        idx = [k for k in range(i0 + 1, i1) if env[k] > -38 and env[k - 1] <= -38]
        on = (idx[0] / 100) if idx else w["s"]
    else:
        i0 = max(int((w["s"] - 0.10) * 100), prev); i1 = int((w["s"] + 0.12) * 100)
        on = (i0 + int(np.argmax(der[i0:i1 + 1]))) / 100 if i1 > i0 else w["s"]
    w["on"] = round(on, 2); prev = int(on * 100) + 5
json.dump(W, open("plan/words_on.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
import sys; sys.stdout.reconfigure(encoding="utf-8")
print(" ".join(f"{w['w']}@{w['on']}" for w in W))
