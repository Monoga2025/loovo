# Canal 2026-10-17 19h · contadores, 3 sistemas (fuera de la serie)

Crudo: copia en `crudo/` (original intacto en Downloads/VID20261017194137.mp4). Celular 1080x1920, 211,9 s, con muchas repeticiones.
Entregable: `entregables/contadores_3sistemas_9x16.mp4` (66,4 s) + `portada.png` (Codex, variante 1) + `portada_alternativa.png` + `descripcion.txt`.
- Tomas (s del WAV; video = WAV + 0,135): ver `proyecto/plan/edl.py` (15 tomas, la última versión completa de cada frase).
- Color: luz verde lateral corregida (`proyecto/scripts/grade_verde.py`, Lab) + LUT Adrià 75, solo en la persona.
- Audio: el celular grabó saturado (163 mil muestras recortadas); se reconstruyeron los picos (`declip.py`), voz con paso alto, reducción de ruido leve, de-esser, EQ y compresión 2:1. Final: -17,6 LUFS, LRA 1,9, pico -2,7 dBFS. Música por código 7 dB bajo la voz; 146 SFX a -15 dB.
- Motion: 8 escenas a pantalla completa (~55 %), 2 invert flash con glitch (6,12 y 49,45 s), 4 destellos crema, zoom-through, aterrizajes escala 4, cámara 2.5D, 13 cajas de palabra clave, subtítulos sincronizados (Whisper medium sobre el corte + envolvente).
- Por confirmar: "¿Por qué lo pregunto?" (6,2 s) y "rogándole que le entreguen" los oyó Whisper en el corte; en el crudo decía "Lo digo porque". "lobo" -> Loovo. "Estoy pendiente de/a sus comentarios".
- Frente al Día 1: no hay texto detrás de la persona ni objetos 3D; iconos planos.
