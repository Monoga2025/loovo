"""EDL: tramos de voz del crudo (s). Pausas internas > 0,40 s (envolvente 10 ms < -48 dB) quedan en 0,25 s.
Salida plan/edl.json: pieces [{seg,a,b,o}], segs, total."""
import json, numpy as np
env = np.load("build/env10.npy")
SEGS = [  # id, a, b, hueco tras el tramo (s)
    ("HOOK", 155.38, 164.80, 0.15),  # Mira, todavía estamos en 2026 ... como herramienta.
    ("TRES", 165.30, 171.76, 0.0),  # Así que te van tres sistemas que puedes utilizar para destacar como contador.
    ("S1",   172.10, 183.52, 0.30), # Número uno, un agente ... citando el artículo exacto.
    ("S2a",  194.44, 195.47, 0.22), # Sistema número dos,
    ("S2b",  210.02, 218.88, 0.30), # Un extractor ... lista para subir a Siigo o Alegra.
    ("S3",   257.55, 268.95, 0.30), # Y por último, sistema número tres ... hasta el 4x1000.
    ("CTA1", 280.80, 286.24, 0.25), # Si lo quieren usar, quiero que comenten D1 para que les demos el primer sistema.
    ("CTA2", 286.95, 295.84, 0.30), # Comentan D2 ... los tres sistemas.
    ("FIN",  302.12, 303.96, 0.0),  # Los amo muchachos, adiós.
]
TAIL = 1.2
def silences(a, b, thr=-48, mn=0.40):
    seg = env[int(round(a * 100)):int(round(b * 100))]; runs, st = [], None
    for k, x in enumerate(np.r_[seg < thr, False]):
        if x and st is None: st = k
        if not x and st is not None:
            if (k - st) / 100 >= mn: runs.append((a + st / 100, a + k / 100))
            st = None
    return [(s0, s1) for s0, s1 in runs if s0 > a + 0.05 and s1 < b - 0.05]
pieces, segs, t = [], [], 0.0
for sid, a, b, gap in SEGS:
    s_start = t; cur = a
    for s0, s1 in silences(a, b):
        ca, cb = s0 + 0.125, s1 - 0.125
        pieces.append(dict(seg=sid, a=round(cur, 3), b=round(ca, 3), o=round(t, 3))); t += ca - cur; cur = cb
    pieces.append(dict(seg=sid, a=round(cur, 3), b=round(b, 3), o=round(t, 3))); t += b - cur
    segs.append(dict(id=sid, start=round(s_start, 3), end=round(t, 3), gap=gap)); t += gap
total = round(t + TAIL, 3)
json.dump(dict(pieces=pieces, segs=segs, total=total), open("plan/edl.json", "w"), indent=1)
for s in segs: print(s, sum(1 for p in pieces if p["seg"] == s["id"]), "piezas")
print("piezas", len(pieces), "total", total)
