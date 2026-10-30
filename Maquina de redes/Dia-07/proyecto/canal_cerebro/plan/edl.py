"""EDL 'Le hice un cerebro a mi empresa' (canal). Fuente única: celular VID_20261013_110529.mp4 (sin mic PC: audio del celular).
Tiempos a/b en s del crudo; bordes en el mínimo de la envolvente (_comun/env.py) y cada pieza transcrita (_comun/snap.py).
kind: mg = motion graphic (la base queda debajo), scr = pantalla grabada como B-roll (cámara 2.5D). No hay planos a cámara en esta zona."""
import sys; sys.path.insert(0, "../_comun"); from edl_lib import build
def V(src, *keys, look="scr"): return dict(src=src, keys=[list(k) for k in keys], look=look)
ST = V(None, (0, 540, 960, 1.0))
S = [  # id, a, b, gap, kind, view, texto (subtítulo limpio)
 ("H1", 753.62, 756.04, 0.00, "mg",  V(753.62, (0, 540, 960, 1.0)), "Vamos a hacer una base de conocimientos en NotebookLM,"),
 ("H2", 757.06, 759.97, 0.12, "mg",  None, "que es básicamente el cerebro de mi empresa."),
 ("C1", 731.95, 736.52, 0.45, "scr", V(745.0, (0, 600, 1040, 1.12), (5.0, 560, 860, 1.30)), "Algo bien interesante fue entrar a la carpeta donde tengo absolutamente todo"),
 ("C2a",743.57, 745.80, 0.30, "mg",  None, "y le dije al agente que hiciera un resumen de todo"),
 ("C2b",746.84, 751.44, 0.30, "mg",  None, "y me lo entregara en un formato .md para enviárselo a NotebookLM."),
 ("C3", 821.03, 824.50, 0.40, "scr", V(822.2, (0, 640, 900, 1.38), (3.8, 600, 880, 1.62)), "Subimos los cinco elementos y ya estamos creando nuestro primer cerebro."),
 ("C4", 896.46, 898.15, 0.35, "mg",  None, "Es demasiada información."),
 ("C5", 915.87, 919.22, 0.15, "mg",  None, "Esto es un agente de RAG, donde tenemos un montón de información."),
 ("C6", 930.33, 932.87, 0.40, "scr", V(937.9, (0, 600, 840, 1.28), (2.9, 570, 880, 1.42)), "Lo importante es que desde acá"),
 ("C7", 935.17, 940.66, 0.05, "mg",  None, "vamos a tener un mapa mental de la empresa, vamos a poder crear infografías y una tabla de datos."),
 ("C8", 946.30, 947.48, 0.45, "mg",  None, "Volvemos y preguntamos:"),
 ("C9", 950.42, 951.52, 0.20, "mg",  None, "¿qué servicios vendemos?"),
 ("C10",978.09, 979.31, 0.55, "scr", V(978.0, (0, 540, 900, 1.06), (1.6, 540, 820, 1.20)), "Perfecto, aquí está."),
 ("C11",979.85, 982.82, 0.10, "mg",  None, "Servicios empaquetados en documentación de venta,"),
 ("C12",990.20, 991.66, 0.15, "mg",  None, "soluciones web y pilotos de inteligencia artificial."),
 ("C13",1013.84,1017.50, 0.45, "mg",  None, "Ya desde acá tenemos una base de datos de toda nuestra empresa."),
 ("PL", None, 2.80, 0.35, "pl", None, "(placa LOOVO)"),
]
# la vista de los tramos mg sin vista sigue el último crudo visible (la base queda tapada por el motion)
BLUR = [dict(t0=976.0, t1=981.5, r=[0, 360, 1080, 1460], nota="respuesta de NotebookLM: nombres de terceros, clientes y montos")]
S2 = []; last = None
for s in S:
    s = list(s)
    if s[5] is None and s[1] is not None: s[5] = dict(src=s[1], keys=[[0, 540, 960, 1.0]], look="scr")
    S2.append(tuple(s))
build(S2, BLUR)
