"""Pista de SFX (48 kHz estéreo) en los beats de plan/beats.json (los mismos de la composición): motor de ventas_ia
(sintetizados por código, scripts/make_sfx_lib.py) + glitch Mixkit 1022 (Mixkit SFX Free License) en cada invert flash.
Las señales por video están en plan/sfx_cues.py (usa c(t, tipo, ganancia), B, S, EN, F). Ejecutar en el proyecto."""
import os
H = os.path.dirname(os.path.abspath(__file__))
G = {"__name__": "sfx"}
exec(open(os.path.join(H, "sfx_head.py"), encoding="utf-8").read(), G)
E = G["E"]; G["S"] = lambda i: next(s for s in E["segs"] if s["id"] == i)["start"]; G["EN"] = lambda i: next(s for s in E["segs"] if s["id"] == i)["end"]
exec(open("plan/sfx_cues.py", encoding="utf-8").read(), G)
exec(open(os.path.join(H, "sfx_tail.py"), encoding="utf-8").read(), G)
