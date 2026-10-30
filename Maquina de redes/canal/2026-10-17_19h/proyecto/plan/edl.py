"""EDL: mejores tomas del crudo (tiempos del WAV; video = WAV + 0,135 s por el start_time del audio).
Pausas internas > 0,40 s se acortan a 0,25 s. -> plan/edl.json"""
import json, numpy as np, soundfile as sf
AOFF = 0.135
T = [  # id, a, b, hueco tras el tramo, texto
 ("T1", 0.45, 2.95, 0.12, "Parce, yo tengo una pregunta para los contadores"),
 ("T2", 21.10, 24.30, 0.30, "ustedes cómo hacen para manejar 10, 20 clientes y no volverse locos"),
 ("T3", 69.74, 75.54, 0.30, "Lo digo porque normalmente los contadores están detrás de cada cliente rogándole ... facturas"),
 ("T4", 87.42, 93.62, 0.28, "Mira, yo soy ingeniero mecatrónico ... para los contadores"),
 ("T5", 120.60, 123.58, 0.30, "Así que estos son los tres sistemas que les van a optimizar el trabajo"),
 ("T6", 130.40, 143.10, 0.30, "El primero ... dejas de estar detrás de todo el mundo"),
 ("T7", 148.24, 156.24, 0.30, "El segundo ... qué se viene"),
 ("T8", 159.82, 166.98, 0.22, "Y el tercero está buenísimo ... organizados"),
 ("T9", 175.67, 178.80, 0.34, "Tú solo revisas, corrige si hace falta y envías"),
 ("T10", 181.10, 182.94, 0.20, "Y yo les pregunto algo en serio"),
 ("T11", 189.97, 191.48, 0.30, "¿A ustedes qué les quita más trabajo?"),
 ("T12", 193.77, 195.82, 0.30, "Comenta uno, dos o tres"),
 ("T13", 199.66, 201.68, 0.26, "Porque estamos empezando a construir Loovo"),
 ("T14", 206.33, 208.16, 0.20, "Y quiero saber cuál les serviría más"),
 ("T15", 209.40, 211.10, 0.0, "Estoy pendiente de sus comentarios"),
]
v, sr = sf.read("audio/audio48.wav"); h = sr // 100
def silences(a, b, thr=-48, mn=0.40):
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
for sid, a, b, gap, _ in T:
    cur = a
    for s0, s1 in silences(a, b):
        ca, cb = s0 + 0.125, s1 - 0.125
        pieces.append(dict(seg=sid, a=round(cur, 3), b=round(ca, 3), o=round(t, 3), gap=0)); t += ca - cur; cur = cb
    pieces.append(dict(seg=sid, a=round(cur, 3), b=round(b, 3), o=round(t, 3), gap=gap)); t += b - cur + gap
total = round(t + 1.2, 3)
json.dump(dict(pieces=pieces, total=total, aoff=AOFF, takes=[list(x) for x in T]), open("plan/edl.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("piezas", len(pieces), "voz hasta", round(t, 2), "total", total)
for p in pieces: print(p)
