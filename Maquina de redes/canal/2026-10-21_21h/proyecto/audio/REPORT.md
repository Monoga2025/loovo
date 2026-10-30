# Audio B1 · informe (todo medido; nada escuchado)

Archivo final: `audio/final_mix.wav` (estéreo, 48 kHz, 39,64 s; `build/clean.mp4` = 39,637 s).

## 1. Juntas entre tomas (`step1_joints.txt`)
Posición de cada junta = suma acumulada de duraciones de `plan/edl.json` (la fórmula de cues.json difería hasta 0,5 s en varias juntas, así que no la usé). Ventanas RMS de 20 ms en los 50 ms previos, umbral -36 dB. `build_cut.py` aplica fade de 30 ms en cada borde.
- Juntas en 3,690 · 5,200 · 8,850 · 12,980 · 17,820 · 20,710 · 26,650 · 29,780 · 34,740 s.
- **3 de 9 con voz activa** justo antes de la junta: **8,850 s, 12,980 s, 17,820 s** (la ventana final marca -22,3 / -26,0 / -26,6 dB; las anteriores están en silencio). Las otras 6 terminan en silencio (< -43 dB). No se corrigió nada. Esos tres finales pueden ser el final de una palabra mordido por el fade de 30 ms; no lo oí.

## 2. Voz (`step2_measure.txt`)
| | piso p5 (100 ms) | habla (ventanas > -36 dB) | LUFS | pico real |
|---|---|---|---|---|
| original `voice-cut.wav` | -42,11 dB | -18,07 dB | -15,8 | -0,4 |
| A: highpass 80 + afftdn nr=8 nf=-35 | -42,73 dB | -18,12 dB | -15,8 | -0,4 |
| B: A + arnndn mix 0,8 (`sh.rnnn`) | -49,69 dB | -20,34 dB | -17,8 | **+11,0** |
- B baja el piso 7,0 dB pero el habla cae 2,2 dB (> 1 dB), pierde 26 ventanas de habla (359→333 vs 361 en A) y mide pico real +11 dBFS (anómalo). **Elegida A.** A baja el piso solo 0,6 dB.
- `voice_clean.wav` = A con -3 dB: piso -45,73, habla -20,96, -18,8 LUFS, pico -3,4 dBFS.
- **NO la oí.** Artefactos de denoise o de highpass no se pueden descartar por medidas.

## 3. Música (`make_epic_b1.py`, diff en `make_epic_b1.diff`)
Copia de `Dia-01/.../make_epic.py` con DUR 39,64. Constantes cambiadas: intensidad (33,6→38,0), riser final (31,6→37,26), crash final (33,6→39,257), taiko grande final (33,6→39,257), fundido 1,0→0,8 s. La envolvente de la música en los últimos 0,7 s alcanza su máximo en t = 39,26 s (-8,9 dB; el fundido la atenúa ≈ -6 dB en ese instante). Último 20 ms: -50,5 dB.

## 4. Efectos (`sfx.json`, 37 cues; `sfx.wav` con `make_sfx.py` del Día 1 sin cambios)
whoosh 11 · pop 8 · hit 4 · click 9 · swish 4 · riser 1 = **37** (Día 1: 50 en 38 s; rango pedido 35–50, quedé en el límite bajo, ≈ 56/min vs 79/min).
- whoosh a cut_t - 0,12 s en las 11 palabras; pop en 8; hit en IA, PRIMERO y COMENTARIOS (+ hit inicial a 0,119 s); click en las 9 juntas; swish a 6,6 · 14,0 · 22,5 · 32,0 s; riser a 0 s. Ganancias 0,5–1,0 por cue.
- Cues puestos con `cut_t` de `plan/cues.json` (versión corregida por el padre; ver nota de corrección).

## 5. Mezcla
- Ducking `duck_epic_b1.py` (3 dB bajo la voz, +9 dB en huecos > 0,12 s, ataque 40 ms, release 160 ms). **Desviación:** la máscara de voz sale de la envolvente de `voice_clean.wav` (RMS 20 ms > -45 dB, huecos < 0,12 s unidos; `words_duck_env.json`), no de `words_out.json`, porque con las palabras de Whisper (finales inflados) solo salían 4 tramos y 3 huecos; con la envolvente, 9 tramos y 8 huecos. Música objetivo -21,8 LUFS vs voz -18,8 LUFS.
- Música con -3 dB a 300 Hz y -4 dB a 1,5 kHz; efectos a -8 dB; `mix_pre.wav` -17,4 LUFS.
- loudnorm dos pasadas (I -14,5, TP -1,8, LRA 11) + alimiter 0,708. Pasada 1 (`loudnorm_pass1.json`): input -17,50 LUFS, TP -2,68; loudnorm cae en modo dinámico (la ganancia lineal de +3 dB rebasaría -1,8 dBTP).
- loudnorm recorta 0,06 s del final (39,58 s); se rellenó con 0,06 s de silencio (`apad`) hasta 39,64 s. Sin cola.
- **Medido sobre `final_mix.wav` (ebur128 peak=true), versión corregida: I = -14,6 LUFS · LRA = 1,9 LU · pico real = -2,9 dBTP · duración 39,64 s** (antes de la corrección: LRA 1,8; el resto igual). Cumple I -14,5 ± 0,3, pico ≤ -1,8, duración ±0,03. La medición sobre el MP4 final queda para el padre.
- Archivos intermedios que no borré: `mix_pre.wav`, `mix_ln.wav`, `music_ducked.wav`, `_tmp.wav`, `voice_A.wav`, `voice_B.wav`, `words_duck.json` (no usado).

## No verificado
- Calidad subjetiva de voz, música y efectos: no se oyó nada.
- Que la música no tape la voz: solo hay diferencia de LUFS globales (3 dB); falta medir por tramo y oír.
- Sincronía fina de los efectos con la voz/imagen (±0,06 s de cues.json; el 8,85/12,98/17,82 s son posibles palabras cortadas).
- 7 palabras faltan en `words_out.json`; el ducking no depende de ellas (usa la envolvente).
- LRA de 1,8 LU es muy comprimido; no sé cómo suena.

## Corrección (padre, 23-oct)
`plan/cues.json` traía `cut_t` mal (desvío hasta 0,5 s). Regeneré los 22 cues ligados a palabras clave (11 whoosh a cut_t-0,12 s; 8 pop y 3 hit en cut_t; hit en IA, PRIMERO, COMENTARIOS) con el `cut_t` nuevo; el resto de `sfx.json` (riser, hit inicial, 9 clicks, 4 swish) quedó igual. Conteo sin cambios: whoosh 11 · pop 8 · hit 4 · click 9 · swish 4 · riser 1 = 37. Copia anterior: `sfx_v1_old.json`. Se re-sintetizó `sfx.wav` y se remezcló con la misma cadena (voz, música y ducking intactos). Pasada 1 de loudnorm: input -17,48 LUFS, TP -2,68.
- Golpe final de la música: caída en 39,257 s; COMENTARIOS corregido = 39,25 s → coinciden (7 ms). El hit SFX de COMENTARIOS está en 39,25 s.
- Juntas 8,85 / 12,98 / 17,82 s: el padre verificó con transcripción del audio cortado que no se corta ninguna palabra (colas de respiración/silencio bajo -36 dB). Mi alerta de «voz activa» queda descartada.
- Sigue sin verificarse: audición, sincronía fina (sin oír), música vs voz por tramo.
