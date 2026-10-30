"""Corte 2 (full motion): EDL sobre la voz del crudo CAMARA (solo audio).
Bordes medidos con envolvente 10 ms y f0 (ver NOTAS). Pausas internas > 0,40 s se acortan a 0,25 s.
Salida: plan/edl.json (piezas fuente->salida) y plan/words.json (palabras en tiempo de salida)."""
import json, numpy as np, soundfile as sf, os
os.makedirs("plan", exist_ok=True)
SEGS = [  # (id, a, b, hueco tras el tramo)
    ("A", 32.51, 41.12, 0.28),   # ¿Qué pasa con n8n? ... comenzamos a trabajar con Claude Code
    ("B", 41.97, 44.74, 0.34),   # ¿Qué tiene Claude Code? tiene agentes con subagentes
    ("C", 76.78, 82.34, 0.22),   # pero esto daba problemas ... contexto de cada subagente
    ("D", 83.11, 84.28, 0.26),   # ¿Qué se hace en ese caso?
    ("E", 84.95, 86.20, 0.22),   # y es lo que acabo de solucionar
    ("F", 87.19, 93.40, 0.24),   # es utilizar un agente principal ... parte de abajo
    ("G", 94.66, 110.33, 0.0),   # desde acá ... muchísimo más rápido (f0 cae hasta 110,33)
]
v, sr = sf.read("../audio/CAMARA.wav"); v = v if v.ndim == 1 else v.mean(1)
h = sr // 100
def silences(a, b, thr=-50, mn=0.40):
    seg = v[int(a * sr):int(b * sr)]; m = len(seg) // h
    e = 20 * np.log10(np.sqrt((seg[:m * h].reshape(m, h) ** 2).mean(1)) + 1e-9)
    runs, st = [], None
    for k, x in enumerate(np.r_[e < thr, False]):
        if x and st is None: st = k
        if not x and st is not None:
            if (k - st) / 100 >= mn: runs.append((a + st / 100, a + k / 100))
            st = None
    return runs
pieces, t = [], 0.0
for sid, a, b, gap in SEGS:
    cur = a
    for s0, s1 in silences(a, b):
        cut_a, cut_b = s0 + 0.125, s1 - 0.125          # deja 0,25 s de pausa
        pieces.append(dict(seg=sid, a=round(cur, 3), b=round(cut_a, 3), o=round(t, 3))); t += cut_a - cur; cur = cut_b
    pieces.append(dict(seg=sid, a=round(cur, 3), b=round(b, 3), o=round(t, 3), gap=gap)); t += b - cur + gap
total = round(t + 0.9, 3)   # cola de 0,9 s de música / cierre
def o2t(x):
    for p in pieces:
        if p["a"] - 0.02 <= x <= p["b"] + 0.02: return p["o"] + min(max(x, p["a"]), p["b"]) - p["a"]
    return None
W = json.load(open("../transcript/words.json", encoding="utf-8"))
words = []
for w in W:
    s, e = o2t(w["s"]), o2t(w["e"])
    if s is None and e is None: continue
    if w["s"] > 110.27: continue   # "normalmente" queda fuera
    if s is None: s = e - 0.15
    if e is None: e = s + 0.15
    words.append(dict(w=w["w"], s=round(s, 3), e=round(e, 3), src=w["s"]))
for w in words:   # corrección de texto (tiempos intactos)
    if w["w"].lower().startswith("toques"): w["w"] = "tokens"; w["nota"] = "Whisper: 'toques' (0,99). Contexto: tokens. Sin confirmar de oído."
    if w["w"].lower().startswith("cloud"): w["w"] = "Claude"
    if w["w"].startswith("N8N"): w["w"] = w["w"].replace("N8N", "n8n")
json.dump(dict(pieces=pieces, total=total, segs=[s[0:3] for s in SEGS]), open("plan/edl.json", "w"), indent=1)
json.dump(words, open("plan/words.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("piezas", len(pieces), "voz hasta", round(t, 3), "total", total)
for p in pieces: print(p)
print(" ".join(f"{w['w']}@{w['s']}" for w in words))
