"""EDL del Día 4 (final). Tiempos del crudo en reloj del celular. gap = silencio antes del tramo (s).
Genera plan/edl.json con la posición de cada tramo en la línea final (30 fps)."""
import json
B = "../../VID20261011112118.mp4"; A = "../../VID20261011104512.mp4"
# PC: t_PC = t_cel + off (medido localmente con scripts/local_off.py)
OFF = {"B": 2161.9651, "A1": -4.0060, "A2": -3.9485}
S = [  # id, cam, t0, t1, offkey, gap, bloque, qué se ve
 ("G",   "B", 27.44, 31.62, "B", 0.00, "1 gancho",     "persona + título cinético"),
 ("C1",  "B", 37.72, 39.90, "B", 0.15, "2 prueba",     "gráfico entreno02 (Cristiano)"),
 ("C2",  "B", 40.10, 43.44, "B", 0.00, "2 prueba",     "persona + Nº1"),
 ("CP",  None, 0, 0.78, None, 0.00,   "2 prueba",     "placa Nº1 (silencio)"),
 ("T1",  "B", 80.94, 83.62, "B", 0.00, "3 tensión",    "persona"),
 ("T2",  "B", 87.46, 98.70, "B", 0.00, "3 tensión",    "persona + lista fracasos (quitado: agencia de IA 84,1-87,4)"),
 ("T3",  "B", 107.92,109.92,"B", 0.00, "3 tensión",    "persona (quitado: imágenes y criptomonedas 98,7-107,9)"),
 ("A1",  "A", 218.56,226.96,"A1",0.00, "3b libro",     "persona cámara A"),
 ("Q2",  "A", 1255.14,1260.30,"A2",0.00,"3c cita",     "cita 1 Esencialismo (2.º intento)"),
 ("Q1",  "A", 1262.14,1266.84,"A2",0.30,"3c cita",     "cita 2 Esencialismo"),
 ("GI1", "B", 258.30,261.66,"B", 0.25, "4 giro",       "2.5D biblioteca (busto)"),
 ("GI2", "B", 266.62,268.00,"B", 0.00, "4 giro",       "2.5D biblioteca (sala); quitada pausa de 5 s"),
 ("GI3", "B", 269.10,270.74,"B", 0.00, "4 giro",       "2.5D biblioteca (sala); pausa 1,6 s -> 0,6 s"),
 ("PR1", "B", 293.62,296.74,"B", 0.25, "5 prueba real","persona → zoom-out radial"),
 ("PR2", "B", 306.40,310.96,"B", 0.00, "5 prueba real","motion graphic (quitado: agente consultor / mensajes 296,7-306,4)"),
 ("PR3", "B", 311.70,313.50,"B", 0.45, "5 prueba real","invert flash → persona"),
 ("CV",  "B", 154.80,164.26,"B", 0.00, "6 convicción", "persona"),
 ("CI1", "B", 643.52,649.32,"B", 0.00, "7 cierre",     "persona"),
 ("CI2", "B", 707.56,713.64,"B", 0.00, "7 cierre",     "persona"),
 ("PL",  None, 0, 2.40, None, 0.00,   "7 cierre",     "placa DÍA 5 DE 42"),
]
t = 0.0; out = []
for sid, cam, t0, t1, ok, gap, blk, what in S:
    t += gap
    d = t1 - t0
    out.append(dict(id=sid, cam=cam, src=(B if cam == "B" else A) if cam else None, t0=t0, t1=t1, dur=round(d, 4),
                    off=OFF.get(ok) if ok else None, gap=gap, start=round(t, 4), end=round(t + d, 4), bloque=blk, que=what))
    t += d
json.dump(dict(fps=30, total=round(t, 4), segs=out), open("plan/edl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for s in out: print(f"{s['id']:4s} {s['start']:6.2f}-{s['end']:6.2f}  {s['cam'] or '-'} {s['t0']:8.2f}-{s['t1']:8.2f}  {s['que']}")
print("total", round(t, 3))
