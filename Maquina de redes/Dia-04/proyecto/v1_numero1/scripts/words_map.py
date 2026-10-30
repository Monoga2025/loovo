"""Palabras en la línea final: texto y tiempos de faster-whisper medium sobre el mic del PC (tr/B_pc_medium.json, reloj del celular)
reubicadas con la EDL y afinadas con la envolvente del mic (inicio = subida más fuerte en [s-0,15, s+0,20], monótono, >= primer sonido del tramo).
-> plan/words_tl.json [{id,start,end,words:[{w,src,on}]}]"""
import json, numpy as np, soundfile as sf
E = json.load(open("plan/edl.json", encoding="utf-8"))["segs"]
T = json.load(open("tr/B_pc_medium.json", encoding="utf-8"))
allw = [w for r in T for w in r["words"]]
x, sr = sf.read("audio/B_pc15.wav"); B = 15.0; h = int(0.01 * sr)
n = len(x) // h; env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
I = lambda t: int(round((t - B) * 100))
out = []
for s in E:
    if not s["cam"]: continue
    ws = [w for w in allw if s["t0"] - 0.25 <= w["s"] < s["t1"] - 0.05 and w["e"] > s["t0"] + 0.03]
    a, b = I(s["t0"]), I(s["t1"])
    first = a + int(np.argmax(env[a:b] > -45)); prev = first; res = []
    for k, w in enumerate(ws):
        i0 = max(I(w["s"] - 0.15), prev); i1 = min(I(w["s"] + 0.20), b - 1)
        on = i0 + int(np.argmax(der[i0:i1 + 1])) if i1 > i0 else i0
        if k == 0: on = first
        src = on / 100 + B
        res.append(dict(w=w["w"], src=round(src, 3), on=round(s["start"] + src - s["t0"], 3)))
        prev = on + 6
    out.append(dict(id=s["id"], start=s["start"], end=s["end"], words=res))
    print(s["id"], " ".join(f"{i}:{w['w']}[{w['on']:.2f}]" for i, w in enumerate(res)))
json.dump(out, open("plan/words_tl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
