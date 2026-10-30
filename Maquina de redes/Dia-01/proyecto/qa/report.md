# Reporte de QA — Nivel 3 (motion sobre footage)

## Entregables
- `out/final_tiktok.mp4` — H.264 1080×1920, 30 fps, CRF 18, AAC 128k 48 kHz
- `out/final_reels.mp4` — H.264 High 4.2, 1080×1920, 30 fps, 4,5 Mb/s, AAC 128k 48 kHz
- Proyecto editable: `motion/` (HyperFrames). Storyboard: `plan/storyboard.md`. Efectos: `plan/sfx.json`.

## Mediciones (sobre los archivos finales)
| Comprobación | Resultado | Estado |
|---|---|---|
| Duración | 38,13 s | OK |
| Formato | 1080×1920, h264, aac, 30/1 | OK |
| Loudness integrado | -14,8 LUFS | OK |
| Pico real | -2,0 dBTP | OK |
| Música bajo la voz | 19 dB (medido en el Nivel 2, misma pista) | OK |
| Linter de HyperFrames | 0 errores (1 aviso: archivo largo) | OK |
| Cortes | `plan/validate.txt` OK (voz medida) | OK |
| Datos inventados | ninguno; todo el texto en pantalla es lo que se dice | OK |
| Persona del fondo (~33 s) | tapada por la escena "Día 1 de 42" | OK |

## Escenas y técnica (showreel)
1. 0–1,8 s: odómetro 00→42 con glow rojo y cierre en iris.
2. 8,3–10,2 s: arco SVG que se dibuja de "Loovo hoy" a la idea 💡, con "cabeza" en spring.
3. 12,6–14,8 s: retícula de bloques que se ensambla desde el centro y "empresa" en slam con glow; sale con un círculo rojo.
4. 14,8–20,6 s: tarjeta con chincheta que cae y se balancea, checklist sincronizada y temblor en "y qué sale mal".
5. 28,4–32,5 s: "inteligencia" decodificada en scramble, "artificial" con glow, escalones "paso a paso".
6. 32,5–34,8 s: "Día 1 de 42" con 42 segmentos en cascada y el primero lleno en rojo; abre en iris.
7. Entre escenas: subtítulos palabra a palabra con blur-in y la palabra clave en rojo. Zooms con push lento, punch-in con easing expo, zoom látigo con desenfoque y temblor; glitch RGB en "totalmente diferente".

## Errores encontrados y corregidos en la revisión de fotogramas
- "inteligencia" quedaba visible sobre la cara de 32,5 s al final, porque el hijo con `visibility: visible` ignoraba el padre oculto. Corregido.
- El glow del "42" se recortaba en rectángulos por la máscara del odómetro. Se movió a un `drop-shadow` en el contenedor.
- "Qué decisiones tomamos" saltaba a dos líneas y sacaba la píldora roja de la tarjeta. Corregido con tamaño y `nowrap`.

## Corrección de sincronía (iteración 4)
- **Causa:** en el MP4 del celular el audio arranca 0,1786 s después que el video. El WAV de la transcripción empieza en 0, así que todos los tiempos de palabra iban 0,18 s corridos respecto al video.
- **Efecto en la versión anterior:** labios y voz seguían sincronizados entre sí, pero la voz llegaba 0,18 s después que los subtítulos y las animaciones. Además el final de cada frase se cortaba un poco.
- **Medición:** correlación del audio del corte contra el WAV. Antes daba -0,179 a -0,187 s en los 10 clips; ahora da 0.
- **Arreglo:** `build_cut.py` lee el desfase con ffprobe y lo suma a los trims. También ajusta cada borde a un fotograma real del original (fuente VFR) para que audio y video midan igual y no haya deriva entre clips.
- **Verificación labios/voz** (fotograma del corte contra el original): entre -19 y +37 ms en los 10 clips, sin tendencia. Equivale a ≤ 1 fotograma.
- Los tiempos de animaciones y SFX se remapearon al corte nuevo (`plan/timemap.json`); la corrección máxima fue de 0,08 s.

## Igualación de color (iteración 4)
- **Medido** (Lab, pared): video L* 73, b* -1,6 (gris frío, plano; negros p5 L* 17). Animación crema L* 94, b* +3,4; negro L* 3.
- Se compararon 4 grades (`qa/grade_compare.png`, `qa/grade_final.png`). **Elegido "D Contraste cálido":** negros p5 L* 5,8, pared b* +2,1 (cálida), contraste en curva S, viñeta 0,38 y grano 0,12. La luminosidad media no cambia (63,5).
- Se aplica a `#base` y `#pip` con `media-treatment` de HyperFrames (parámetros en `plan/grade_final.json`).

## Iteración 5: Loovo, texto detrás del hablante, motion sobre el video, color natural
- **Marca:** "Lobo" → **Loovo** en la transcripción, los subtítulos, la escena del arco, `brand.json` y los documentos.
- **Texto detrás del hablante:** silueta recortada fotograma a fotograma con rembg/u2net (local, 1.142 fotogramas, ~1,2 s/fotograma) y suavizado temporal de 3 fotogramas (`scripts/segment.py`). Con eso se generó `motion/assets/person.webm` (VP9 con alfa). Capas, de atrás hacia adelante: fondo → `compositions/behind.html` (palabras gigantes) → silueta (mismo zoom que el fondo) → `compositions/overlays.html` → gráficos/subtítulos → PiP.
- **Legibilidad:** se revisó en fotogramas renderizados. "NO SE HACE" pasó a una sola línea, "DIFERENTE" y "MEJORES" se subieron, y "+2.000" se cambió a "+2 MIL" (el punto bajo el pelo se leía como coma). En el último tramo (34,6–38 s) la cabeza llega casi al borde superior, así que ahí no hay palabras detrás.
- **Motion sobre el video mientras habla:** ? en "ni idea", chip "ya existe", sticker 🚫 en "no se hace", 🎯 en "meta", chip "hoy", barras de glitch, 🏆 con destellos en "mejores", chip "evento", chip "Día 1 / 42" y trayectoria en "qué tan lejos". Todo fuera de la cara y de la franja de subtítulos. Se añadieron 9 SFX (total 50).
- **Color:** se descartó el "contraste cálido". Ahora va horneado con ffmpeg y es natural: brillo -0,02, contraste 1,05 y viñeta suave (`plan/grade_natural.txt`). Medido: cara L* 47→44, esquinas 74→60, sin cambio de tono.
- **Render:** el primero falló por timeout de Chrome (poca RAM). Se rehízo con `--low-memory-mode` y timeouts ampliados.

## Para el humano
- Claude no oye: la sincronía de los efectos se basa en los tiempos de las palabras, que se desvían unos 0,1–0,2 s. Revisa con sonido que los golpes caigan bien; se ajustan en `plan/sfx.json` y se regenera en segundos.
- Los emoji son de Windows (Segoe), más planos que los 3D de la referencia.
- El PiP circular aparece en las dos escenas largas (regla de la skill). Si prefieres pantalla completa pura como la referencia, se quita.

## Ajuste de audio v2 (solo audio, sin re-renderizar el video)

| Punto | Antes | Ahora |
|---|---|---|
| Música bajo la voz | ~16 dB (stem -36,1 LUFS) | ~9 dB (stem -29,5 LUFS), ducking suave (ratio 3) |
| Golpes del dedo en la mesa | 13 detectados (6,73 · 6,88 · 8,21 · 9,21 · 19,84 · 20,00 · 23,28 · 32,34 · 33,00 · 34,68 · 35,20 · 36,26 · 37,56 s) | Atenuados en la banda 60–500 Hz (y 8,21 s, que era pausa, bajado a -20 dB). Detector: 20 → 0 sobre la voz sola |
| Loudness final | -14,9 LUFS | -14,5 LUFS |
| Pico real | -2,3 dBTP | -2,8 dBTP |

- Archivos: `out/final_tiktok_v2.mp4` y `out/final_reels_v2.mp4`. Los v1 no se tocaron. El video se copió sin recodificar (`-c:v copy`).
- La regla de 18–20 dB bajo la voz no se cumplió a propósito: el usuario no oía la música.
- Scripts: `fix/find_taps.py`, `fix/taps2.py`, `fix/clean_voice.py`.
- No verificado: Claude no oye la mezcla. Los golpes se detectaron por forma de onda (ataque brusco y caída en menos de 60 ms), no por oído. Revisar a oído 6,7 s, 8,2 s, 19,8 s, 23,3 s y 37,6 s.

### v3 (música al doble, +6 dB en amplitud)
- Stem de música -23,5 LUFS contra voz -20,6 LUFS (unos 3 dB bajo la voz en promedio; antes 9 dB). Final -14,3 LUFS, pico real -2,6 dBTP.
- Archivos: `out/final_tiktok_v3.mp4`, `out/final_reels_v3.mp4`. Receta repetible: `fix/mix.sh <dB de música> <nombre>`; v2 = `fix/mix.sh -5.8 v2`.

### v4 (música épica nueva con ducking por voz)
- Música generada por código (`fix/make_epic.py`, Re menor, 100 BPM: pad, sub, taiko, riser, brass, coro). Libre de derechos. Sustituye a `audio/music.wav` en esta versión.
- Ducking por actividad de voz (`fix/duck_epic.py`): cuando hablas la música queda 1,5 dB bajo la voz; en los 5 huecos de más de 0,12 s sube 9 dB. Ataque 40 ms, release 160 ms.
- Recorte de mediosa la música (-3 dB a 300 Hz, -4 dB a 1,5 kHz) para que la voz siga clara (`fix/mix2.sh`).
- Final -14,4 LUFS, pico real -2,5 dBTP. Archivos: `out/final_tiktok_v4.mp4`, `out/final_reels_v4.mp4`.
- Límite real: el video casi no tiene pausas (157 palabras, 5 huecos, el mayor de 0,31 s), así que la música solo "respira" en esos 5 puntos.

### v5 (para comparar con v4)
- Cambios sobre v4: música a 3 dB bajo la voz (v4: 1,5 dB); golpe de apertura con +4 dB durante los primeros 0,30 s (v4: se bajaba desde el primer instante); 2,0 s extra al final con música sola (+9 dB) y golpe final a 38,15 s; la imagen se congela en el último fotograma y se desvanece a negro. Ese fotograma es el cierre en iris del diseño (loop con el inicio negro); la palabra roja "empresa" que se ve en el borde es parte del diseño, no un error.
- Duración 40,03 s (v4: 38,03 s). El video se recodificó (x264 crf 18); v4 conserva la imagen original sin recodificar.
- Final -14,5 LUFS, pico real -1,8 dBTP.
- Pendiente de decidir por el usuario: cuál de v4 o v5 funciona mejor, para mejorar la skill.
- Entregables: carpeta `Desktop/Dia1_para_publicar` (v4 y v5, TikTok y Reels).
