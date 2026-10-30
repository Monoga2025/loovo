"""Afina inicios: máximo de subida de la envolvente (10 ms) en [s-0,12, s+0,15] sobre audio/voz_cut.wav -> plan/words_on.json"""
import json, numpy as np, soundfile as sf
x, sr = sf.read("audio/voz_cut.wav"); h = sr // 100; n = len(x) // h
env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
W = json.load(open("transcript/words_cut.json", encoding="utf-8"))
E = json.load(open("plan/edl.json")); starts = [s["start"] for s in E["segs"]]
FIX = {"1.": ["Número", "uno,"], "2.": ["Sistema", "número", "dos,"], "3.": ["Y", "por", "último,", "sistema", "número", "tres,"]}
REP = {"listas": "lista", "limpia,": "limpia", "Excel,": "Excel", "impuestos": "impuestos,"}
out = []; prev = 0
for w in W:
    s = w["s"]; seg0 = max([t for t in starts if t <= s + 0.25] or [0])
    first = int(seg0 * 100) + int(np.argmax(env[int(seg0 * 100):int(seg0 * 100) + 80] > -40))
    i0 = max(int((s - 0.12) * 100), prev); i1 = int((s + 0.15) * 100)
    on = (i0 + int(np.argmax(der[i0:i1 + 1]))) / 100 if i1 > i0 else i0 / 100
    if abs(s - seg0) < 0.3 or (w["w"] in FIX): on = first / 100
    if w["w"] in FIX:   # palabras fusionadas: reparto proporcional entre el primer sonido y el fin
        parts = FIX[w["w"]]; e = w["e"]; d = (e - on) / len(parts)
        for k, p in enumerate(parts): out.append(dict(w=p, on=round(on + k * d, 2), e=round(on + (k + 1) * d, 2)))
        prev = int(e * 100); continue
    out.append(dict(w=REP.get(w["w"], w["w"]), on=round(on, 2), e=w["e"])); prev = int(on * 100) + 5
json.dump(out, open("plan/words_on.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(" ".join(f"{w['w']}[{w['on']}]" for w in out))
