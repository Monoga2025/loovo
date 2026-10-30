# Canal 2026-10-17 19h-b · "3 sistemas de IA para contadores" (fuera de la serie)

Crudo: copia en `crudo/VID20261017190855.mp4` (original intacto en Descargas). Celular 1080x1920, 30 fps, 323,8 s, audio AAC que empieza 0,1334 s después del video (compensado en `scripts/make_base2.py`, AOFF).

## Entregable
`entregables/Contadores_3sistemas_9x16.mp4`: 60,95 s, 1080x1920, 30 fps, H.264 CRF 18 + AAC 320k 48 kHz. Proyecto en `proyecto/` (plan/edl.py, scripts/make_base2.py, scripts/degreen.py, scripts/declip.py, scripts/audio_mix2.py, scripts/post_fx2.py, index.tpl.html -> motion/index.html).
- Tomas (crudo, s): 155,38-164,80 · 165,30-171,76 · 172,10-183,52 · 194,44-195,47 · 210,02-218,88 · 257,55-268,95 · 280,80-286,24 · 286,95-295,84 · 302,12-303,96. Pausas internas > 0,40 s quedan en 0,25 s. Fuera: tomas falladas, detrás de cámara (una colaboradora, detergente), "30 mil empleados" y la broma final.
- Persona ~45 %, motion ~55 %: 3 motion graphics 2.5D (manual -> pocos con IA; agente IA + Estatuto/DIAN + chat; extractor -> tabla NIT/CUFE/Impuestos; conciliador con columnas cruzadas y fila marcada), 6 cajas clave con cursor dorado, 2 invert flash con glitch Mixkit (9,50 y 35,72 s), 2 destellos crema, zoom-through, 3 zoom-out radiales, saltos de zoom en cada corte interno, CTA D1/D2/D3, placa final.
- Color: luz verde fuerte en la cara -> `degreen.py` (Lab, solo croma alto) + LUT Adrià 75 %.
- Audio: micrófono saturado (-8,9 LUFS, ~3,5 % de muestras recortadas) -> reconstrucción cúbica de picos (`declip.py`), HPF 75, afftdn suave, EQ -2,5 dB 3,4 kHz / -2 dB 6,5 kHz, compresor 2:1. Música por código 7 dB bajo la voz; 89 SFX a -15 dB.
- Medido en el MP4: I -17,6 LUFS, LRA 2,6 LU, pico real -4,4 dBTP.

## Decisiones mías (confirmar)
- "te marca en rojo": la fila se resalta en dorado (la marca no usa rojo); el subtítulo dice "rojo".
- Ortografía: DIAN, NIT, CUFE, Siigo, Alegra, 4x1000 (Whisper oyó "NID", "QFE", "SIGO").
- Los tres sistemas no figuran en `00_Serie/hechos.md`: se muestran solo como motion conceptual, sin demos.

## No verificado
- No oigo: si la reconstrucción de picos dejó distorsión audible, ni si música/SFX tapan la voz.
- Sincronía labios-voz: el script dio correlaciones ~0,1 (no concluyente); se confió en el start_time medido por ffprobe.
- Onsets de "Número uno / Sistema número dos / Y por último, sistema número tres" repartidos a mano (Whisper los fusionó): ±0,2 s.
- Queda un leve tono oliva en la mejilla derecha en algunos cuadros.
