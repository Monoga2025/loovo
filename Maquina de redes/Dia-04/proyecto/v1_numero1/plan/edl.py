"""EDL v1 'número 1' (Día 4 / en pantalla Día 5). Todo del celular B; audio SOLO mic del PC: t_PC = t_B + OFF.
Tiempos en reloj del celular, bordes ajustados a la envolvente del mic del PC (scripts/snap.py, scripts/env.py).
gap = silencio antes del tramo (s). Genera plan/edl.json (línea final, 30 fps)."""
import json
B = "../../VID20261011112118.mp4"; OFF = 2161.9651
S = [  # id, t0, t1, gap, bloque, texto
 ("H1", 19.08, 20.62, 0.00, "1 gancho",  "Por querer ser el número uno,"),
 ("H2", 21.98, 23.78, 0.15, "1 gancho",  "por querer ser el mejor,"),
 ("H3", 26.02, 31.62, 0.12, "1 gancho",  "lo he sido, porque si yo mismo no creo que soy el mejor, ¿quién lo va a creer por mí?"),
 ("C1", 37.72, 39.90, 0.15, "2 Cristiano","Cristiano Ronaldo piensa que es el número uno?"),
 ("C2", 40.10, 43.44, 0.00, "2 Cristiano","No, él sabe que es el número uno y por eso es el número uno."),
 ("CP", None, 0.90, 0.00,   "2 Cristiano","(placa Nº1, silencio)"),
 ("C3a",51.36, 52.30, 0.00, "2 mejores",  "Y los que llegan"),
 ("C3b",54.24, 56.22, 0.12, "2 mejores",  "a ser los mejores del mundo"),
 ("C4", 57.18, 61.55, 0.15, "2 mejores",  "es porque piensan y se creen que son los mejores del mundo."),
 ("D1", 63.42, 66.20, 0.35, "3 giro",     "Desde pequeño yo tuve esa habilidad de"),
 ("D2", 67.74, 70.02, 0.15, "3 giro",     "creerme el número uno en absolutamente todo,"),
 ("D3", 70.76, 72.10, 0.30, "3 giro",     "hasta que crecí."),
 ("F0a",77.66, 79.30, 0.45, "4 fracasos", "antes de llegar a la universidad,"),
 ("F0b",80.96, 83.62, 0.20, "4 fracasos", "en realidad siento que tuve muchos fracasos."),
 ("F1a",87.40, 91.80, 0.20, "4 fracasos", "fracasé con la agencia de marketing, fracasé"),   # quitado 84,0-87,4: 'agencia de inteligencia artificial'
 ("F1b",92.36, 94.40, 0.00, "4 fracasos", "con la empresa de cámaras de seguridad,"),
 ("F1c",94.80,100.32, 0.00, "4 fracasos", "fracasé con la reparación de celulares, con el diseño de logos, con la edición de imágenes,"),
 ("F1d",100.92,104.32,0.00, "4 fracasos", "fracasé con las criptomonedas"),
 ("P1", 107.90,110.00,0.45, "5 tensión",  "y perdí la habilidad de creerme el número uno"),
 ("P2", 118.12,119.96,1.10, "5 tensión",  "y eso es grave, es muy grave"),
 ("R1", 131.34,137.02,0.50, "6 resolución","Pero en este momento estoy organizando mi vida, estoy organizando las cosas, y yo sé que en algún momento,"),
 ("R2", 138.30,140.57,0.12, "6 resolución","por todo lo que he hecho, por todo lo que he aprendido,"),
 ("R3", 141.36,145.14,0.10, "6 resolución","por las distintas habilidades que tengo, yo sé que esto tendrá fruto."),
 ("R4a",153.10,159.40,0.35, "7 cierre",   "algún día lo voy a lograr, y cuando lo logre, todo el mundo va a decir que esto va a ser suerte, y no va a ser suerte,"),
 ("R4b",160.20,172.06,0.30, "7 cierre",   "va a ser demasiado esfuerzo, demasiada constancia, esto fueron años de trabajo. Yo estuve aprendiendo durante muchos años esto, yo no llego a mi casa a reírme o a hacer cualquier cosa, todos los días llego a aprender algo nuevo."),
 ("PL", None, 2.70, 0.25,   "7 cierre",   "(placa DÍA 5 de 42)"),
]
t = 0.0; out = []
for sid, t0, t1, gap, blk, txt in S:
    t += gap
    d = (t1 - t0) if t0 is not None else t1
    out.append(dict(id=sid, cam="B" if t0 is not None else None, src=B if t0 is not None else None, t0=t0 if t0 is not None else 0, t1=t1 if t0 is not None else 0,
                    dur=round(d, 4), off=OFF if t0 is not None else None, gap=gap, start=round(t, 4), end=round(t + d, 4), bloque=blk, texto=txt))
    t += d
json.dump(dict(fps=30, total=round(t, 4), segs=out), open("plan/edl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for s in out: print(f"{s['id']:4s} {s['start']:6.2f}-{s['end']:6.2f}  {s['t0']:7.2f}-{s['t1']:7.2f}  {s['texto'][:60]}")
print("total", round(t, 3))
