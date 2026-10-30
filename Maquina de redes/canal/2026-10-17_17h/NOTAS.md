# Canal 2026-10-17 17h (fuera de la serie "Día X de 42")

Crudo: copias en `crudo/` (originales intactos en `C:\Users\<user>\Videos\17-10 17h\`). CAMARA 1280x720 y PANTALLA 1920x1080, 149,6 s, misma voz (micrófono del PC) en ambos.

## Contenido (transcripción Whisper medium, 384 palabras, ok)
Explica por qué pasó de n8n (flujo que inicia y termina, sin loop) a Claude Code con un agente orquestador y subagentes; el problema de organizar carpetas/terminales; la solución (un agente principal que recibe respuestas de texto de los subagentes sin revisar sus archivos); cierra con Gentle AI, Engram y ODD. En pantalla: diagrama n8n (0-45 s), explorador de archivos, terminales de Claude Code.

## Entregable
`entregables/corte1_subagentes_9x16.mp4`: 42,3 s, 1080x1920, 30 fps, H.264 + AAC. Segmento crudo 67,3-113,5 s: problema (terminales sueltas sin contexto) -> solución (orquestador principal) -> beneficio. Se quitaron 5 pausas largas (4,5 s) cortando solo dentro de silencios medidos y tapando el corte con salto de zoom.
Incluye: color LUT Adrià 75 solo en persona, zoom de respiración, subtítulos en tarjetas (clave en serif dorado), un insert de pantalla (barra lateral "Monoga OS / Ventas / Videos / CRM", recortada: no se ve ningún texto de terminal ni claves), música generada por código (libre de derechos), salida a blanco pastel.
Medido en el MP4: I -17,6 LUFS, LRA 1,8, pico real -5,0 dBTP; música ~20 dB bajo la voz en habla (stems medidos).

## Corte 2 full motion (rehecho; el corte 1 se calificó 1/10)
`entregables/corte2_fullmotion_9x16.mp4`: 41,95 s, 1080x1920, 30 fps, H.264 + AAC 320k. Proyecto en `proyecto/c2/` (edl.py, voz.py, audio_mix.py, index.tpl.html -> motion/index.html, post_fx.py).
- Cero cámara: la composición no carga ningún video de CAMARA (solo su audio). Escaneo de piel en los 1.258 cuadros: máx. 3,9 % del cuadro (dorado/crema) contra 31,7 % en un cuadro real de la cámara.
- Idea central: n8n (flujo que inicia y termina, sin loop) -> Claude Code -> orquestador que recibe texto de los subagentes sin revisar sus archivos -> ahorra tokens y es más rápido.
- Voz (crudo, s): 32,51-41,12 · 41,97-44,74 · 76,78-82,34 · 83,11-84,28 · 84,95-86,20 · 87,19-93,40 · 94,66-110,33. Pausas internas > 0,40 s acortadas a 0,25 s. El final corta en 110,33 (mínimo de f0 al cerrar "rápido"; "normalmente" va pegado: puede quedar un roce de "n" de ~20 ms, no verificado de oído).
- 12 escenas, cambio visual cada ~1-3 s, alternando pastel y carbón: título cinético del gancho -> flujo n8n con punto dorado "inicia/termina" -> loop tachado -> Claude Code (insert real del encabezado) -> agente + subagentes -> "problemas"/"contexto" con insert real de la barra lateral (Monoga OS/Ventas/Videos/CRM) -> "solucionar" -> orquestador y subagentes en 2.5D, insert real "general-purpose Inspecting…" + contador de tokens, documento de texto que sube al orquestador, archivos bloqueados -> "tokens" (fichas que caen) -> loop rápido con rayo y "más rápido".
- Transiciones: zoom-through, 2 destellos crema, flip 3D, aterrizaje escala 4 + blur 18 -> 1,05, 2 invert flash con glitch Mixkit (17,20 y 36,95 s), 8 cajas de palabra clave con cursor dorado, cámara 2.5D (rotationX) en el flujo y el diagrama.
- Audio medido en el MP4: I -17,6 LUFS, LRA 2,0, pico -4,5 dBFS. Voz sola -17,6 antes de mezclar (en la mezcla queda ~0,9 dB más baja porque se normalizó el total). Música por código (Re menor, 112 BPM: bombo suave, hats, sub, arpegio, pad; corte de batería 0,55 s antes de cada invert flash) a 7 dB bajo la voz en el habla (RMS medido: voz -16,9, música -23,9). 97 SFX (make_sfx.py del Día 1 + glitch Mixkit) a -15 dB. Voz: paso alto 85 Hz, afftdn leve, compuerta suave, EQ presencia +1,5 dB 3,2 kHz, compresor 2:1.
- Inserts de pantalla: solo recortes propios sin claves ni rutas con usuario; no usé el diagrama de n8n de Reddit (contenido de terceros): el flujo n8n es motion propio.

### "tokens" vs "toques" (107,2 s) — MARCADO, confirmar
Whisper medium lo vuelve a oír "toques" (probabilidad 0,99, también sin pista). Por contexto es "tokens" (la frase habla de no revisar archivos del subagente, y en pantalla en ese momento hay contadores "105.6k tokens"). En pantalla quedó "tokens" (subtítulo y caja clave). Si dijo "toques", hay que cambiar la escena 36,95-38,7 s.

### Corte 2 frente al Día 1 (10/10), punto por punto
| | Día 1 (40 s) | Corte 2 (42 s) | Dónde queda por debajo |
|---|---|---|---|
| Densidad de motion | 11 cambios de escena detectados, palabras gigantes, objetos, PiP | 12 escenas y ~60 eventos animados (cajas clave, iconos, líneas que se dibujan, puntos que viajan, inserts) | Sin persona no hay contraste humano ni texto detrás del sujeto; iconos planos (Phosphor), sin objetos 3D/fotorrealistas; el diagrama del orquestador dura 16,8 s (cámara se mueve, pero es la misma escena) |
| Transiciones | iris, látigo, círculo que se expande, glitch | zoom-through, flip 3D, aterrizaje escala 4, 2 destellos, 2 invert flash + glitch | Sin iris/círculo; sin transición por oclusión |
| Música | épica por código, 1,5-3 dB bajo la voz (v4/v5) | 7 dB bajo la voz (punto medio de aprendizajes), sube ~1 dB en huecos | Con pocas pausas casi no "respira"; no oigo si agrada ni si el ritmo encaja |
| SFX | 50 cues (riser, hit, whoosh, pop, scramble, ding…) | 97 cues, mismos tipos + glitch Mixkit | Puede sonar cargado: está a -15 dB, sin verificar de oído |

### No pude verificar (corte 2)
- No oigo ni veo en el celular: sincronía fina de subtítulos (onsets por envolvente, error típico de Whisper ~0,1-0,2 s), si la música/SFX tapan la voz, el roce final de "normalmente".
- Hojas de contacto revisadas a 2 fps y ~40 cuadros sueltos, no todos los cuadros.
- El motion lo escribí yo (Opus) directo, sin subagente con el prompt literal de la skill §0.1.
- Afirmaciones del flujo propio sin fila en `hechos.md`.

## Propuestas sin renderizar
- B (0,6-41,3 s, ~40 s): n8n vs Claude Code, con el diagrama de la pantalla de fondo. Pantalla del diagrama sin datos sensibles a la vista.
- C (42-93,8 s, ~50 s): "organización tediosa" -> solución; se solapa con el corte 1, no publicar ambos.
- D (124-140 s, 16 s): stack Gentle AI + Engram + ODD (corto; sirve de cierre o story).

## Decisiones tomadas por mí (confirmar)
- "toques" (107,2 s) lo subtitulé "tokens": Whisper falló; por el contexto casi seguro, pero no confirmado.
- No usé placa "Día X" ni cuenta en la serie.
- No hay "hechos.md" revisado para estas afirmaciones (son su descripción de su propio flujo).
- Aparece sin camisa en cámara; decide si lo publica así.

## No pude verificar
- No veo ni oigo: sincronía de subtítulos (afinada con envolvente de voz, error Whisper ~0,2 s), limpieza de la voz, ni si la música agrada.
- Los subtítulos pueden rozar la barbilla/micrófono (base y~1410); la boca queda por encima en los cuadros revisados (6 cuadros vistos, no todos).
- El último cuadro con voz tiene la boca abierta (frase termina en coma); luego el fade a pastel.
- Cara de 65 % del ancho del encuadre 9:16 (cámara 720p recortada y ampliada: se ve algo blanda).
- Nombres de herramientas (Argon/"rate .md") no aparecen en este corte; no confirmados.
- No usé HyperFrames/Opus para motion: fue ffmpeg + OpenCV + PIL (Gemini no disponible).

## Corte 3 split (pedido: "mostrar más la pantalla, mitad motion arriba, mitad grabación abajo con seguimiento al mouse")
`entregables/corte3_split_9x16.mp4`: 41,93 s, 1080x1920, 30 fps, H.264 CRF 17 + AAC 320k. Proyecto en `proyecto/c3/` (build_top.py, track.py, ocr_blur.py, compose.py). Corte 1 y 2 intactos.
- Arriba (0-960): el motion del corte 2 re-renderizado en HyperFrames a 1080x960 (banda y 250-1480 del lienzo original x0,78; escenas ensanchadas para que el fondo llene). Invert flash solo arriba (17,20 y 36,95 s).
- Abajo (960-1920): PANTALLA en los mismos tiempos de la voz (EDL del corte 2; pantalla va 138 ms antes que la cámara, medido con GCC-PHAT en 3 puntos). Zoom base 1,32x; 2,0-2,3x en "acá" (35,02 y 35,76), "ahí", "esto", "aquí" (91,50), "acá" (94,92); 1,6-2,3x en "subagentes", "texto", "archivos", "tokens". Paneo suavizado ida y vuelta (sin retraso); con zoom fuerte el encuadre se clava en lo que nombra. Aro dorado en el puntero en los deícticos.
- Puntero: plantillas (flecha y lupa) cuadro a cuadro. Desde 94,7 s el puntero no está visible: foco manual alineado a la frase (línea del subagente, el prompt, "Read 2 files", contador de tokens) con caja dorada fina.
- Privacidad: siempre desenfocados pestañas/título (hostname, "Cámara IMOU", "Cuentas personal") y barra de tareas; en el navegador, URL/marcadores/encabezado de Reddit y título del post. OCR (RapidOCR, 3 fps) desenfoca líneas con rutas C:\Users, localhost, ADMIN_PASSWORD/API_KEY, .env, Secretos.
- Medido: I -17,6 LUFS, LRA 2,0, pico -4,5 dBFS (mismo audio final.wav del corte 2). Cero cámara: compose.py no abre CAMARA; escaneo de piel en los 1.258 cuadros: máx. 2,3 %.
- Decisión mía (confirmar): el diagrama n8n de Reddit SÍ aparece abajo (es lo que señala con "acá, acá"); desenfoqué la marca/título del post, no el diagrama.
- No verificado: no oigo ni veo en el celular; la zona inferior queda bajo la UI de TikTok (botones a la derecha); el texto de terminal a 1,32x se lee justo.
