"""Construye plan/edl.json desde la lista S del edl.py del proyecto. S: (id, a, b, gap, kind, view, texto); a/b en s del crudo (None = placa)."""
import json
def build(S, BLUR=(), extra=None):
    t = 0.0; out = []
    for sid, a, b, gap, kind, view, txt in S:
        t += gap; d = (b - a) if a is not None else b
        out.append(dict(id=sid, a=a, b=b if a is not None else None, dur=round(d, 4), gap=gap, start=round(t, 4), end=round(t + d, 4), kind=kind, view=view, texto=txt))
        t += d
    D = dict(fps=30, total=round(t, 4), segs=out, blur=list(BLUR)); D.update(extra or {})
    json.dump(D, open("plan/edl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for s in out: print(f"{s['id']:5s} {s['start']:6.2f}-{s['end']:6.2f}  {s['a'] if s['a'] is not None else '-':>8} {s['kind']:4s} {s['texto'][:70]}")
    print("total", round(t, 3)); return D
