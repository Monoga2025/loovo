"""EDL 'Así organizo mi empresa con agentes' (columnas, canal). Fuente única: celular VID_20261013_110529.mp4 (sin mic PC).
Tiempos a/b en s del crudo; bordes en el mínimo de la envolvente (_comun/env.py) y cada pieza transcrita (_comun/snap.py).
kind: scr = pantalla grabada (B-roll, cámara 2.5D), mg = motion (la base queda debajo). En esta zona no mira a cámara.
Se cortó: "Y desde acá, de una vez les adelanto", la pausa de "trabajando en... crear", "va a tener el prompt de orquestador",
la repetición "vamos creando subcar-", "Codex... incluso me gustaría utilizar Pi", "Pi lo tengo conectado con...", "muchísimo es muchísimo",
y las dudas del cierre ("se ponga a revisar todo el repositorio")."""
import sys; sys.path.insert(0, "../_comun"); from edl_lib import build
def V(src, *keys, look="scr"): return dict(src=src, keys=[list(k) for k in keys], look=look)
S = [  # id, a, b, gap, kind, view, texto (subtítulo limpio)
 ("K1a", 1264.80, 1266.20, 0.00, "mg",  None, "Básicamente estuve trabajando en"),
 ("K1b", 1267.92, 1274.30, 0.10, "mg",  None, "crear un prompt que me genera un empleado que se va a encargar de las ventas de la empresa."),
 ("K2a", 1285.83, 1291.40, 0.50, "scr", V(1288.4, (0, 420, 1000, 1.30), (5.8, 400, 1060, 1.48)), "¿Cómo va a quedar organizado todo el proyecto? Desde acá tengo el proyecto, tengo los agentes, tengo la información de Claude,"),
 ("K2b", 1291.40, 1297.55, 0.00, "mg",  None, "y dentro de la carpeta de ventas vamos a crear el subagente, que va a ser un orquestador que tiene sus diferentes agentes."),
 ("K3a", 1337.60, 1339.75, 0.50, "mg",  None, "de cada área. Yo lo llamo columnas:"),
 ("K3b", 1341.66, 1345.10, 0.20, "mg",  None, "está la columna de ventas, está la columna de marketing,"),
 ("K3c", 1349.18, 1350.66, 0.20, "mg",  None, "si la empresa tiene varias columnas,"),
 ("K3d", 1352.22, 1355.48, 0.10, "scr", V(1341.0, (0, 420, 900, 1.35), (3.5, 400, 980, 1.55)), "vamos creando subcarpetas dentro del proyecto."),
 ("K4a", 1502.60, 1507.62, 0.50, "mg",  None, "La verdad sí tenía pensado usar Claude, pero como lo estoy usando para edición de videos,"),
 ("K4b", 1513.20, 1515.42, 0.20, "scr", V(1513.2, (0, 420, 700, 1.45), (2.4, 440, 740, 1.65)), "entonces vamos a utilizar mejor Pi,"),
 ("K4c", 1524.50, 1526.32, 0.10, "mg",  None, "que optimiza muchísimo los tokens."),
 ("K5a", 1641.90, 1644.40, 0.50, "mg",  None, "Vamos a esperar que el agente edite los videos,"),
 ("K5b", 1645.70, 1649.90, 0.15, "mg",  None, "vamos a esperar también que el agente de ventas"),
 ("K5c", 1654.00, 1656.80, 0.15, "mg",  None, "termine de realizar su loop,"),
 ("K5d", 1658.10, 1660.40, 0.25, "mg",  None, "y por último vamos a esperar la integración de Odoo."),
 ("PL",  None,    2.80,   0.35, "pl",  None, "(placa LOOVO)"),
]
BLUR = []
S2 = []
for s in S:
    s = list(s)
    if s[5] is None and s[1] is not None: s[5] = dict(src=s[1], keys=[[0, 540, 960, 1.0]], look="scr")
    S2.append(tuple(s))
build(S2, BLUR)
