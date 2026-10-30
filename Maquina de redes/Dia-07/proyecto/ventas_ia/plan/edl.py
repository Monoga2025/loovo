"""EDL Día 7 'ventas con IA'. Fuente única: celular VID_20261013_110529.mp4 (rotación -90 -> 1080x1920, 120 fps).
Audio: SOLO el celular (hoy no hay mic del PC). Tiempos en reloj del crudo (región tr/ = crudo - 1095).
Bordes ajustados a la envolvente (scripts/env.py) y verificados transcribiendo cada pieza (scripts/chk.py).
gap = silencio antes del tramo (s). cam = True si la persona se ve (mira a cámara)."""
import json
SRC = "C:/Users/you/Desktop/VID_20261013_110529.mp4"; R = 1095.0
S = [  # id, t0, t1 (región), gap, cam, bloque, texto
 ("A",  61.18, 64.50, 0.00, False, "1 gancho",   "Normalmente lo que me pasa es que yo construyo un montón de cosas, pero no vendo nada."),
 ("B1",  9.64, 10.88, 0.55, True,  "2 contexto", "Mientras estoy en la universidad,"),
 ("B2", 11.30, 16.42, 0.12, True,  "2 contexto", "yo utilizo Codex dentro de la máquina virtual que me dan y adelanto bastantes cosas."),
 ("B3a",18.84, 19.58, 0.30, True,  "2 contexto", "Hoy estuve"),
 ("B3b",20.62, 22.48, 0.10, True,  "2 contexto", "investigando sobre embudos B2B"),
 ("B4", 24.06, 26.14, 0.22, False, "2 contexto", "y encontré estos dos repositorios que son muy buenos."),
 ("C2a",47.88, 50.66, 0.45, False, "3 marketing","investigan al cliente, consiguen la información, el copy, el CRO,"),
 ("C2c",52.02, 52.62, 0.22, False, "3 marketing","los correos"),
 ("C2b",53.86, 55.24, 0.25, False, "3 marketing","y hacen un embudo de ventas."),
 ("C3a",56.22, 59.04, 0.30, False, "3 marketing","Porque lo más importante de una empresa es"),
 ("C3b",60.02, 60.48, 0.40, False, "3 marketing","las ventas."),
 ("D1", 68.50, 71.58, 0.85, False, "4 agentes",  "Y el otro que tenemos es este de Agency Agents,"),
 ("D2", 73.54, 76.50, 0.20, False, "4 agentes",  "que son agentes de inteligencia artificial capacitados para vender."),
 ("D3", 77.80, 80.00, 0.20, False, "4 agentes",  "Servicio B2B, es lo que nosotros estamos vendiendo."),
 ("D4a",83.60, 84.42, 0.40, False, "4 agentes",  "Le metí varios prompts"),
 ("D4b",85.80, 87.36, 0.40, False, "4 agentes",  "que hacen que él actúe como si fuera yo."),
 ("D5", 95.36, 98.40, 0.30, False, "4 agentes",  "Va a trabajar como orquestador y va a tener sus agentes."),
 ("E1",214.58,215.86, 0.50, False, "5 cierre",   "Ahorita lo estoy entrenando"),
 ("E2",216.06,217.44, 0.10, False, "5 cierre",   "para que haga un buen prompt"),
 ("E3",217.70,222.46, 0.10, False, "5 cierre",   "y me cree un buen subagente, un buen orquestador que trabaje con unos buenos subagentes."),
 ("PL", None, 3.00,   0.30, False, "5 cierre",   "(placa DÍA 7 de 42)"),
]
t = 0.0; out = []
for sid, a, b, gap, cam, blk, txt in S:
    t += gap
    d = (b - a) if a is not None else b
    out.append(dict(id=sid, cam=cam, src=SRC if a is not None else None, t0=round(R + a, 3) if a is not None else 0, t1=round(R + b, 3) if a is not None else 0,
                    r0=a, r1=b if a is not None else None, dur=round(d, 4), gap=gap, start=round(t, 4), end=round(t + d, 4), bloque=blk, texto=txt))
    t += d
json.dump(dict(fps=30, total=round(t, 4), segs=out), open("plan/edl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for s in out: print(f"{s['id']:4s} {s['start']:6.2f}-{s['end']:6.2f}  {s['t0']:8.2f}-{s['t1']:8.2f} {'CAM' if s['cam'] else '   '} {s['texto'][:60]}")
print("total", round(t, 3))
