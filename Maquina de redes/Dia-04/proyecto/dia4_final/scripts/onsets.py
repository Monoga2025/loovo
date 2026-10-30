"""Afina el inicio de cada palabra: máximo de subida de la envolvente (10 ms) en [st-0,12, st+0,15],
sin salir del tramo ni antes del primer sonido del tramo. -> plan/words_fixed.json"""
import json, numpy as np, soundfile as sf
E = {s["id"]: s for s in json.load(open("plan/edl.json", encoding="utf-8"))["segs"]}
W = json.load(open("plan/words_final.json", encoding="utf-8"))
x, sr = sf.read("audio/voz_raw.wav"); h = int(0.01 * sr)
n = len(x) // h; env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
out = []
for seg in W:
    s = E[seg["id"]]; a = int(s["start"] * 100); b = int(s["end"] * 100)
    first = a + int(np.argmax(env[a:b] > -42))            # primer sonido del tramo
    prev = first
    for k, w in enumerate(seg["words"]):
        st = w["st"]
        i0 = max(int((st - 0.12) * 100), prev, first); i1 = min(int((st + 0.15) * 100), b - 1)
        on = (i0 + int(np.argmax(der[i0:i1 + 1]))) / 100 if i1 > i0 else i0 / 100
        if k == 0: on = first / 100
        w["on"] = round(on, 2); prev = int(on * 100) + 5
    out.append(seg)
    print(seg["id"], " ".join(f"{w['w']}[{w['on']:.2f}]" for w in seg["words"]))
json.dump(out, open("plan/words_fixed.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
