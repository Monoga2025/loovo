"""Palabras con tiempo en la línea final a partir de tr/words_med.json (whisper small sobre el crudo, tiempos del crudo):
cada palabra del tramo [a,b] -> start + (t - a); inicio afinado a la subida de la envolvente de audio/voz_raw.wav (10 ms);
primera palabra = primer sonido del tramo. Respaldo: si un tramo no tiene palabras, usa plan/words_tl.json (words.py). -> plan/words_tl.json"""
import json, os, numpy as np, soundfile as sf
E = json.load(open("plan/edl.json", encoding="utf-8"))
R = json.load(open("tr/words_med.json", encoding="utf-8")); allw = [w for r in R for w in r["words"]]
# whisper deforma nombres (brief): se corrigen para alinear con el texto limpio
FIX = {"odo": "Odoo", "odio": "Odoo", "ojo": "Odoo", "hodo": "Odoo", "cdrm": "CRM", "molo": "módulo", "modo": "módulo", "campan": "kanban", "cambal": "kanban",
       "npsr": "ERP", "roleway": "Railway", "cloud": "Claude", "codecs": "Codex", "coex": "Codex", "pin": "Pi", "prom": "prompt", "notokl": "NotebookLM"}
import re as _re
allw = [[FIX.get(_re.sub(r"[^a-z]", "", w[0].lower()), w[0])] + list(w[1:]) for w in allw]
old = {w["id"]: w for w in json.load(open("plan/words_tl.json", encoding="utf-8"))} if os.path.exists("plan/words_tl.json") else {}
x, sr = sf.read("audio/voz_raw.wav"); h = int(0.01 * sr)
n = len(x) // h; env = 20 * np.log10(np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1)) + 1e-9)
env = np.convolve(env, np.ones(3) / 3, "same"); der = np.r_[0, np.diff(env)]
out = []
for s in E["segs"]:
    if s.get("a") is None: continue
    a, b, st, en = s["a"], s["b"], s["start"], s["end"]
    ws = [(w[0], st + (w[1] - a)) for w in allw if a - 0.25 <= w[1] < b - 0.05]
    if not ws and s["id"] in old: out.append(old[s["id"]]); continue
    ia, ib = int(st * 100), int(en * 100); first = ia + int(np.argmax(env[ia:ib] > -45)); prev = first; res = []
    for k, (w, t) in enumerate(ws):
        i0 = max(int((t - 0.12) * 100), prev); i1 = min(int((t + 0.15) * 100), ib - 1)
        on = (i0 + int(np.argmax(der[i0:i1 + 1]))) / 100 if i1 > i0 else i0 / 100
        if k == 0: on = first / 100
        res.append(dict(w=w, on=round(on, 2))); prev = int(on * 100) + 5
    out.append(dict(id=s["id"], start=st, end=en, words=res))
    print(s["id"], " ".join(f"{w['w']}[{w['on']:.2f}]" for w in res))
json.dump(out, open("plan/words_tl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
