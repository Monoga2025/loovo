# Edición como el Día 1 · VID20261021162958

Objetivo: editar el crudo nuevo con los mismos métodos del Día 1. Entrega en `canal/2026-10-21_21h/entregables/`. Ejecutor: `loovo-edicion` (Opus 5.5, esfuerzo bajo). Sin Git ni corredor de pruebas: se verifica con mediciones y fotogramas.

## Specs

S1. Pedido de Monoga, textual: «mira editaras este video como si fuera el video del dia 1 con los mimos metodos y todo creo que hay una skill sobr eeso metodica». Confirmación: «Perfecto intestemoslo asi» (skill `monoga-editor` con los números de `receta-dia1`). Crudo: `C:\Users\you\Downloads\VID20261021162958.mp4` (no se modifica ni se mueve).

S2. Método: pipeline de `monoga-editor`. Los números de `receta-dia1` valen, **excepto el zoom alterno 1,0/1,12, que Monoga rechazó**. El zoom real del Día 1 está en `Dia-01/proyecto/motion/index.html:75-122` (`land`, `push`, `punch`, `whip`, `shake` con GSAP). Prohibido: `monoga-videos`, `monoga-adria`, skills o repos externos.

S3. Entregable: `.mp4`, `portada.png` y `descripcion.txt` en `canal/2026-10-21_21h/entregables/`.

S4. Verdad: no prometer sistemas inexistentes (D1-D3 se dicen «estamos construyendo»), sin datos inventados ni marcadores, subtítulos con lo dicho.

S5. Medir y reportar sobre el MP4 final: cortes por minuto, LUFS, pico, destellos y efectos de sonido contados. Si la voz suena distorsionada o el audio quedó saturado, decirlo; no darlo por arreglado.

S6. Dos fases con punto de control: **Fase 1** transcribir, medir y proponer tomas, y detenerse; **Fase 2** producir solo tras la aprobación de Monoga.

S7. Revisión de fotogramas (control visual del render): la hace Luna (`openai-codex/gpt-6-luna`) mediante un agente de solo lectura, por orden de Monoga el 22-oct. El editor no se autoevalúa. Verificado el 22-oct: Luna lee imágenes (composición, desenfoque, encuadre), pero su juicio de color no es fiable (dijo «tinte amarillo/verde» en un crudo de colores naturales). Por eso Luna revisa composición, recortes, texto legible y artefactos; el color se decide con measure_color.py y una revisión del padre.

## Tasks

| ID | Specs | Ruta | Estado |
|---|---|---|---|
| T1 | S1, S2, S6 | delegado | hecho: 10 tomas = 39,08 s, 11 palabras, medidas (Fase 1, verificado por el padre) |
| T2 | S2, S5 | delegado | hecho (unidad A): cortes y sincronía OK, color base; limpieza de voz pasa a B1 |
| T3 | S2 | delegado | recorte hecho (10 máscaras, 1.189 fotogramas); persona.webm, letras, zoom GSAP y subtítulos en curso en B2 (`mvl9aq1k-1-yq5s`) |
| T4 | S2, S5 | delegado | en curso en B1 (`mvl9aq1m-2-1g9z`, Sonnet): voz limpia, música, efectos y mezcla a -14,5 LUFS |
| T5 | S3, S5 | padre + delegado | render sin audio en B2; el padre une audio y video, mide el MP4 final, pasa la revisión de Luna y entrega |

## Log

L1. «mira editaras este video como si fuera el video del dia 1 con los mimos metodos y todo creo que hay una skill sobr eeso metodica».
L2. «Perfecto intestemoslo asi».
L3. Crudo medido: 187,3 s, 1080x1920, -15,7 LUFS, pico +0,1 dBFS, LRA 10,1 LU. Sin transcribir.
L4. Tres ediciones previas en segundo plano se cancelaron al cerrarse la sesión de Pi. El agente guarda `PROGRESS.md` en `proyecto/` tras cada paso para poder retomar. Espejo en Engram pendiente: el proveedor no está disponible.
- 2026-10-22 T1 Fase 1: transcripción, medidas, 10 tomas y 11 palabras en canal/2026-10-21_21h/proyecto/ (PROGRESS.md). Espera aprobación.
L5. 2026-10-22: «la parte de revisar los fotogramas lo hara con chagpt luna 6 okey?». «Luna 6» = `openai-codex/gpt-6-luna` (confirmado el 22-oct al pedir editar el perfil).
L6. 2026-10-22 «Listo dale al video ponte amnos a la obra». Interpretado como aprobación del plan de la Fase 1 (10 tomas, 11 palabras), de la descarga de u2net y de mantener la frase «estamos probando un agente». Fase 2 en dos unidades: A (corte, audio, color, recorte de persona) y B (motion, música, efectos, render, entrega). Revisión de fotogramas por Luna (S7) tras cada unidad.
L7. 2026-10-22: en la hoja de contactos del crudo se ve a otra persona en cámara, no a Monoga (parece la persona del guion de Contadores 01; por confirmar). La toma 7 dice «estamos probando un agente basado en el Estatuto Tributario»: D1 no está probado de punta a punta, así que «probando» no está verificado (S4). Pendiente de decisión de Monoga: quitar las tomas 7-9, cambiar su texto o confirmar que de verdad se prueba. Unidad A recorta las tomas 7-9 al final para no perder tiempo.
L8. 2026-10-22 10:30: unidad A (`mvjnqe71-1-oo9k`) agotó el tiempo por un error del asistente, pero dejó hecho: `build/clean.mp4` (39,64 s, 1080x1920, 30 fps, base de color del Día 1), `build/voice-cut.wav`, `qa/sync.log` (audio 0,000 s, labios +0,005 s, OK en las 10 tomas) y color medido (piel neutra; el verde de la zona alta son las plantas, no un tinte). El recorte de persona sigue en un proceso independiente (`build/seg/run_seg.sh`, reanudable; hechas t01-t03 = 266 de ~1.190 fotogramas; orden t01-t06, t10, t07-t09). `audio_pro.py` de monoga-editor no es usable (ejecuta main() al importar y exige archivos de música): la limpieza de ruido NO está hecha; la voz solo recibió -3 dB (`build/voice-gain.wav`). Revisión de Luna sobre la hoja del corte: sin cortes de cuerpo ni invasiones; manos con desenfoque en 13-14 s; un primer plano a los 20 s (la persona se inclina hacia la cámara, no es un corte). Encuadre consistente.
L9. 2026-10-23 12:50: pregunté si quitaba las tomas 7-9 y Monoga respondió «No dale de una me gusto». Interpretado como: NO quitarlas, mantener las 10 tomas y arrancar ya. Aun así la frase «estamos probando un agente basado en el Estatuto Tributario» sigue sin verificarse (D1 no probado de punta a punta): el video NO se publica hasta probar D1 o cambiar esa frase.
L10. 2026-10-23: plan/cues.json calculado por el padre (tiempo de las 11 palabras sobre el corte). Hallazgo: build/words_out.json omite la última palabra de cada toma (7 de 159) porque Whisper infla su final; los subtítulos deben añadirlas. Fase 2 en dos unidades paralelas con superficies disjuntas: B1 audio (carpeta `audio/`, `PROGRESS-audio.md`) y B2 movimiento y render sin audio (`motion/`, `out/`, `qa/`, `build/person/`, `PROGRESS-motion.md`, `entregables/portada.png`).
L11. 2026-10-23: ERROR DEL PADRE detectado y corregido. El `plan/cues.json` inicial (tiempos de las 11 palabras sobre el corte) se calculó con un desplazamiento por toma y se desviaba hasta 0,5 s; el EDL (`plan/edl.json`, 10 clips con start/end reales) es la fuente de verdad del corte. Verificado con una transcripción (faster-whisper small) del audio ya cortado: el EDL acierta con error residual <= 0,15 s. Correcciones: `plan/cues.json` rehecho (el anterior queda como `cues.v1_incorrecto.json`) y `plan/words_cut.json` nuevo (152 palabras sobre el corte, final recortado al final de su clip, última palabra de cada toma incluida). `build/words_out.json` NO es fiable para tiempos. B2 (`mvl9aq1k-1-yq5s`) avisado para recalcular letras, zoom y subtítulos; B1 reanudado (`mvl9ohbe-3-a4wi`) para rehacer los efectos ligados a palabras clave y volver a mezclar.
L12. 2026-10-23: las 3 juntas marcadas por B1 como «voz activa» (8,85; 12,98; 17,82 s) NO cortan palabras: según la transcripción del audio cortado, pijama termina en 8,58, primero en 12,46 y vence en 17,48; son colas de respiración o silencio por encima del umbral de -36 dB. Audio B1 medido: I -14,6 LUFS, LRA 1,8, pico -2,9 dBTP, 37 efectos (a rehacer parcialmente por L11). Voz variante A (casi idéntica al original: el piso de ruido ya era -42 dB); la variante B se descartó (habla -2,2 dB, pico +11 dBFS).
L13. 2026-10-23 ~14:10: B1 reanudado terminó: 22 cues de efectos corregidos, mezcla -14,6 LUFS, LRA 1,9, pico -2,9 dBTP, 39,64 s, verificada por el padre. B2 NO logró renderizar: 7 intentos colgados (fotogramas 104, 38, 461, 230/836, 211), probable falta de RAM (máquina de 7,7 GB con ~1,4 GB libres, Chrome del usuario abierto). B2 dejó hecho: `build/person/person.webm` (1.189 fotogramas, ninguna máscara vacía), `motion/` completo con lint 0/0, 11 punch, 2 shake, 1 whip y `qa/contact_person.jpg`. Letra IGUAL omitida a propósito (cabeza a y=308 < 330).
L14. El padre rehízo `plan/words_cut.json` (final; el anterior en `words_cut.v2.json`): 159 palabras con la primera de cada toma; tiempos del audio cortado. Verificado con la energía de la voz original: en las tomas 4, 5, 7, 8 y 10 hay silencio real entre el inicio que da Whisper y el inicio del corte, y la voz arranca justo en el corte: el corte es correcto y no se pierde ninguna palabra (incluido el «No» de «No es un chatbot»). Pendiente: subtítulos actualizados (B2, sin render), liberar RAM, render, unir audio, medir MP4 final, Luna, entrega.
L15. 2026-10-23 19:30: Monoga pausa la edición por hoy. Estado, hallazgos del render (13 intentos colgados, cierres de chrome-headless con 0xe0000008) y pasos para retomar quedan en `HANDOFF.md`, sección «Video VID20261021162958 — PAUSADO». T5 (render, unión de audio, medición del MP4, Luna, entrega) sigue pendiente; no hay mp4.

