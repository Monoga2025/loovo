"""EDL 'Por qué monté Odoo en mi agencia' (canal). Fuente única: celular VID_20261013_110529.mp4 (sin mic PC: audio del celular).
Tiempos a/b en s del crudo; bordes en el mínimo de la envolvente (_comun/env.py) y cada pieza transcrita (_comun/snap.py).
kind: cam = persona a cámara (mira a cámara o tensión), scr = pantalla grabada (B-roll, cámara 2.5D), mg = motion (la base queda debajo).
Se cortó: "en los actuales", "de Odoo" (repetido), la repetición "tengo un CRM, tengo un CRM", "proyecto, marketing, correo, inventario, manufactura" de la lista (para no pasar de 60 s)
y todo lo de "facturar totalmente gratis" (no es un hecho de Loovo)."""
import sys; sys.path.insert(0, "../_comun"); from edl_lib import build
def V(src, *keys, look="scr"): return dict(src=src, keys=[list(k) for k in keys], look=look)
S = [  # id, a, b, gap, kind, view, texto (subtítulo limpio)
 ("G1a",  60.98,  63.22, 0.00, "mg",  None, "Me di cuenta que necesitaba organizar la información de la empresa,"),
 ("G1b",  63.22,  64.44, 0.00, "cam", V(63.22, (0, 760, 1150, 1.14), (1.3, 760, 1140, 1.19), look="cam"), "no sabía dónde montarlo."),
 ("G2",   68.98,  71.24, 0.40, "mg",  None, "Intenté integrarlo en los mejores ERP,"),
 ("G3",   73.09,  76.36, 0.30, "mg",  None, "pero me di cuenta que entre más instala cosas nuevas, peor funciona."),
 ("P1",   79.77,  82.94, 0.45, "cam", V(79.77, (0, 560, 1150, 1.10), (3.2, 570, 1140, 1.17), look="cam"), "Como yo manejo Odoo, porque yo fui integrador de Odoo,"),
 ("P2",   82.96,  85.76, 0.20, "mg",  None, "vamos a instalar Odoo para la agencia."),
 ("P3a",  89.46,  91.19, 0.35, "mg",  None, "Vamos a utilizar el módulo de"),
 ("P3b",  93.40,  99.19, 0.10, "mg",  None, "marketing con una vista kanban donde vamos a organizar los guiones."),
 ("T1a", 477.54, 479.50, 0.50, "mg",  None, "¿Saben qué pasa? Que normalmente la gente dice:"),
 ("T1b", 482.22, 484.05, 0.20, "cam", V(482.22, (0, 420, 1020, 1.06), (1.8, 410, 1000, 1.10), look="cam"), "tengo un CRM para manejar mis clientes,"),
 ("T1c", 484.46, 487.43, 0.10, "cam", V(484.46, (0, 410, 1000, 1.10), (2.9, 420, 960, 1.15), look="cam"), "tengo un módulo de contabilidad, tengo un módulo de inventario..."),
 ("T2",  495.90, 498.12, 0.45, "scr", V(499.0, (0, 560, 1000, 1.22), (2.6, 520, 960, 1.36)), "En Odoo se puede manejar absolutamente todo."),
 ("L1",  510.55, 514.97, 0.40, "mg",  None, "Tenemos módulo de contabilidad, tenemos módulo de punto de venta,"),
 ("L3",  521.58, 524.46, 0.15, "mg",  None, "tenemos ventas, tenemos compras."),
 ("D1",  546.60, 553.41, 0.45, "scr", V(546.9, (0, 540, 700, 1.12), (3.0, 560, 700, 1.25), (5.5, 800, 820, 1.45), (7.2, 700, 780, 1.75)), "De las cosas más interesantes que tiene Odoo es que tiene contabilidad compatible con la DIAN, tiene integración con la DIAN."),
 ("R1",  143.74, 146.66, 0.45, "cam", V(143.74, (0, 790, 1230, 1.12), (2.9, 790, 1215, 1.18), look="cam"), "Estamos montando Odoo dentro de Railway."),
 ("R2",  675.82, 678.20, 0.30, "scr", V(675.82, (0, 650, 1100, 1.32), (2.4, 680, 1060, 1.52)), "Revisamos el despliegue: sale exitoso."),
 ("PL",  None,   2.80,   0.35, "pl",  None, "(placa LOOVO)"),
]
BLUR = [dict(t0=553.35, t1=555.5, r=[0, 760, 1080, 1440], nota="tablero de contabilidad de odoo.com con montos y facturas de ejemplo (demo del sitio): se tapa por regla")]
S2 = []
for s in S:
    s = list(s)
    if s[5] is None and s[1] is not None: s[5] = dict(src=s[1], keys=[[0, 540, 960, 1.0]], look="scr")
    S2.append(tuple(s))
build(S2, BLUR)
