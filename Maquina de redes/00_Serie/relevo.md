# Relevo entre agentes

Cada agente agrega una entrada AL FINAL al terminar una sesión de trabajo. No borres entradas de otros.

Formato:
```
## AAAA-MM-DD HH:MM · agente (rol)
- Hice:
- Archivos tocados:
- Decisiones del usuario:
- Pendiente / siguiente paso:
- Problemas:
```

## 2026-10-07 · orquestador
- Hice: Día 1 completo (audio v4/v5, portada con Codex, caption). Creé `Loovo-42`, la skill `monoga-serie` y el comando `dia`. Integré en `monoga-editor` el script `audio_pro.py`.
- Archivos tocados: toda la carpeta `Loovo-42`.
- Decisiones del usuario: música épica y audible; portada minimalista 3:4; el guion lo escribe él.
- Pendiente: elegir v4 o v5; publicar el Día 1.
- Problemas: dos claves de OpenAI pegadas en el chat.

## 2026-10-08 · orquestador
- Hice: análisis del Día 2. Verifiqué voces por tono (un fragmento ajeno descartado) y fotogramas (solo aparece el usuario). Plan de tomas en `Dia-02/proyecto/plan/takes_dia2.md`. Agregué a `hechos.md` que Loovo es una agencia de IA.
- Archivos tocados: `Dia-02/proyecto/plan/`, `Dia-02/proyecto/qa/tomas/`, `00_Serie/hechos.md`.
- Decisiones del usuario: seguir el Día 2 en el otro chat (editor).
- Pendiente: el editor une c1 y c2 y arma el corte. Falta brief, portada y caption del Día 2.
- Problemas: el editor no veía el contexto de la serie porque la memoria de Claude Code es por carpeta. Se resolvió con `CLAUDE.md`, `estado.md` y este archivo.

## 2026-10-08 · editor
- Hice: unir c1 y c2 en `input/clip.mp4` (30 fps fijos, audio con su desfase), `words.json` con desfase de c2, `takes.json` con tomas 1 a 15 (la 15 en dos partes), EDL validada (OK), corte de 62,33 s, `check_sync` OK. Motion nivel 3 (HyperFrames, 8 escenas FS, subtítulos cinéticos, zooms). Audio v4 y v5 con `audio_pro.py` (-14,2 y -14,3 LUFS, pico -2,6 dBTP). Portada A/B con Codex y caption.
- Archivos tocados: `Dia-02/proyecto/*`, `Dia-02/entregables/*`, `Dia-02/portada/*`, `Dia-02/brief.md`, `guion.md`, `caption.md`.
- Decisiones del usuario: nivel 3 como el Día 1; dejar la toma 12 tal cual (con lo 🟡); titular "NO LE PAGO".
- Pendiente: elegir v4/v5 y portada A/B; publicar. Escuchar los golpes que quedan (13 de 28 detectados). Confirmar rol en el evento y "40 días" del caption.
- Problemas: el piso de ruido de este cuarto (-35 dB) rompía el umbral de `audio_env.py` (-36): lo dejé configurable con `AUDIO_THR` (usé -28). Los tiempos por palabra de `whisper-1` salieron imprecisos; para los subtítulos usé faster-whisper (medium) sobre el corte. Sin PiP, sin texto detrás de la persona ni stickers.

## 2026-10-08 · editor (ronda 2)
- Hice: v6 (música a 14 dB bajo la voz, SFX a -17 dB, voz limpiada), color oscuro con viñeta, cola de 0,8 s con la boca cerrada al final (cut de 63,1 s), zoom final suavizado, portada regenerada con otro fotograma. Levanté el CRM (API y app) para grabarlo y lo apagué.
- Decisiones del usuario: música casi de fondo; más oscuro; verificar siempre el último fotograma y la portada.
- Pendiente: escena del CRM en el video. Bloqueado: el clasificador negó volcar el texto de contactos y empresas del CRM (posibles datos de clientes reales). Solo el panel principal se vio, y muestra "1 trato ganado $1,2 M", que no sé si es real.
- Problemas: el servidor del CRM tarda en compilar; Chrome del usuario no cargó las páginas locales por la herramienta (se usó Chrome headless de HyperFrames).

## 2026-10-08 · editor (ronda 3)
- Hice: v7. 23 stickers con emojis 3D (Fluent Emoji 3D, MIT) a la izquierda de la cara, emojis 3D en las 8 escenas, transiciones 3D de escena (giro con perspectiva), cortes con efecto (glitch, látigo, destello) en los 10 cortes visibles y SFX de cortes, stickers y giros (73 efectos). Analicé el video de referencia (`Dia-02/proyecto/ref/`). Nueva guía `monoga-editor/references/motion-nivel-pro.md` y regla 14 en `SKILL.md`.
- Pendiente: escena con la pantalla real del CRM (esperando confirmación de datos de demostración), objetos fotorrealistas recortados y Three.js.

## 2026-10-08 · editor (ronda 4)
- Hice: v8 de audio (`audio_pro.py --preset v8`): voz más grave (f0 125 → 117 Hz), más fuerte (-11,1 LUFS, pico -1,1 dBTP) y música a 7 dB bajo la voz. Video igual a v7.
- Pendiente: que el usuario escuche v8 y ajuste (`--under`, objetivo LUFS).

## 2026-10-08 · editor (ronda 5)
- Hice: v9. Emojis reemplazados por iconos Phosphor (MIT) en mosaicos y un billete de dominio público tintado de rojo; tipografía nueva (Anton oblicua + Montserrat 300 cursiva, Anton descargada de @creator, OFL); punto rojo recurrente que cruza todas las escenas y cierra en bucle; audio v8. Lo aprendido de claudevideo.org, motionpromptgallery.com e iart.ai quedó en `monoga-editor/references/motion-nivel-pro.md`.
- Pendiente: pantalla real del CRM (datos demo), objetos fotorrealistas recortados, Three.js; el usuario elige portada A/B y escucha el audio.

## 2026-10-09 · editor (ronda 6, Opus)
- Hice: identidad IA MONOGA (3 propuestas renderizadas con la cara del usuario; eligió A "Eléctrico"): `00_Serie/marca/` (marca.md, marca.json, fuentes OFL). Biblioteca `00_Serie/recursos/` con manifiesto de licencias: 41 iconos, 7 fotos (2 recortadas, duotono de marca), 3 texturas, 6 formas; scripts `recursos_pd.py` y `recursos_proc.py`. Día 2 v10 totalmente nuevo: texto detrás de la persona (13 palabras), escenas nuevas (editor de video, barra proporcional, celular con interfaz, red de nodos, filas 3D, factura), foco lima recorriendo las escenas, subtítulos con caja lima. Render con alfa se atascó; se usó el plan B (3 renders + máscara). Skill actualizada (reglas 9 y 10, marca y biblioteca).
- Pendiente: logo/monograma; objetos 3D propios con Codex (gasto de tokens a aprobar); pantalla real del CRM con datos demo; portada con la nueva marca.
- Problemas: Wikimedia Commons da 429 si se consulta rápido; pocas fotos de objetos aislados con licencia libre.

## 2026-10-09 · editor (ronda 7, skill)
- Hice: convertí el análisis de 10 referencias de Pinterest en `monoga-editor/references/tecnicas-referencias.md` (gramática, 9 recetas, fuentes de recursos con licencia) y un catálogo probado `templates/hyperframes/examples/tecnicas_referencias.html` (22 s, lint 0 errores, revisado con snapshots; corregí oclusión, contador, etiqueta). Regla 11 en `SKILL.md`. No toqué el video del Día 2 (el usuario lo pidió).
- Pendiente (cerrado en la misma ronda): T8 corregida (inclinación y giro en contenedores separados). 3D real funcionando: T10 con Three.js y reloj CC0 de Poly Haven (`examples/objeto3d_threejs.html`, `scripts/recursos_3d.py`, modelo en `00_Serie/recursos/3d/`). `aura.png` sin borde duro (regenerada; `recursos_proc.py` corregido).
- Ojo: el `aura.png` de `Dia-02/proyecto/motion10/assets/tex/` sigue siendo el viejo; no lo toqué (el video del Día 2 no se edita).

## 2026-10-09 · orquestador (marca: mascota y relación)
- Hice: 10 tableros de mascota con Codex (`marca/mascota/`, `los_10_conceptos.jpg`); el usuario pidió ideas totalmente distintas. 4 investigaciones con Sonnet 5.5 (competencia, ética Talking Tom, cliente ideal, ideas al revés) → `marca/investigacion/sintesis_marca_relacion.md`.
- Pendiente: el usuario elige dirección. ⚠ El "Luque Business Summit" no aparece en fuentes públicas: confirmar con el organizador antes de nombrarlo de nuevo.

## 2026-10-09 15:30 · orquestador (estudio OBS)
- Hice: OBS 32.2.2 configurado para grabar cámara y pantalla por separado con el plugin Branch Output (ya instalado). Al pulsar "Iniciar grabación" salen 3 archivos en `C:\Users\<user>\Videos`: `CAMARA_*.mp4` (1280x720, máximo de la webcam integrada, NVENC CQP 18), `PANTALLA_*.mp4` (1920x1080, CQP 20) y `AAAA-MM-DD hh-mm-ss.mp4` (respaldo compuesto con la cámara en la esquina; pista 1 micrófono, pista 2 audio del escritorio). Los tres llevan la voz del micrófono: el editor los sincroniza por audio. Todo a 30 fps, Hybrid MP4 (no se corrompe si se cae). Supresión de ruido RNNoise en el micrófono. Websocket encendido en el puerto 4455 (con contraseña). Prueba de 12 s: 0 fotogramas perdidos por el codificador, 16/1333 de render (1,2 %), CPU 4 %. Prueba borrada.
- Archivos tocados: `%APPDATA%\obs-studio\basic\` (perfil y escena) y `plugin_config\obs-websocket\config.json`. Copia previa en `%APPDATA%\obs-studio-backup-20261009-152354`.
- Pendiente: probar con voz real (no se midió el nivel hablando); la skill `monoga-editor` aún no tiene un flujo para YouTube horizontal (pantalla + cámara).
- Problemas: la webcam da 720p; recortada a 9:16 queda en 405x720 (se verá blanda en TikTok). Solo quedan 24,5 GB libres en C: (unas 3 h de grabación).

## 2026-10-09 · orquestador (guiones y skill monoga-guionista)
- Hice: 5 investigaciones con Sonnet 5.5 en `00_Serie/guiones/investigacion/` (inventario del CRM, retención en cortos con 18 subtítulos, YouTube largo con 10 subtítulos, series y reciclaje, prompts de guiones). Skill nueva `monoga-guionista` (paquete de sesión para YouTube + short Día X + clips; rúbrica de 15 criterios; palabras prohibidas; Nómina Viva). `banco-frases.md`. `plan-42.md` (calendario de los Días 3 a 42, 13 videos largos, 40 shorts evergreen). Paquete completo `dias/Dia-03.md`.
- Archivos tocados: `00_Serie/guiones/*`, `00_Serie/banco-frases.md`, `00_Serie/hechos.md` (7 filas del CRM), `estado.md`, `CLAUDE.md` (regla 1 y rutas), `monoga-serie/SKILL.md` (principio 1).
- Decisiones del usuario: guiones para los 42 días (gancho y cierre literales, el resto en puntos); se aplica La Nómina Viva; YouTube largo grabado trabajando, del que salen los clips; publicar máximo 3 al día y grabar hasta 10. La escritura la hace el modelo principal, no Sonnet.
- Pendiente: paquetes de los Días 4 y 5 (se generan con "paquete del día N"); que el usuario elija el gancho del Día 3 y grabe; probar `start.ps1 -Demo`; confirmar su papel en el evento.
- Problemas: el CRM es un fork open source y "Capturar lead" funciona con reglas (corregido en `hechos.md`). `CRM.bat` abre la base real con un cliente real: grabar solo con `-Demo`. El evento no aparece en fuentes públicas (pendiente desde antes).

## 2026-10-09 · orquestador (guionista: sesión CRM + SolidWorks)
- Hice: paquete de sesión del Día 3 con el trabajo real de hoy (revisar y arreglar el módulo de CRM con IA + pieza de SolidWorks de la universidad): `00_Serie/guiones/dias/Dia-03-crm-solidworks.md`. Largo con 9 bloques, 5 anclas, 3 ganchos largos y 3 del Día X, 4 clips y autocrítica (24/30 ambos).
- Archivos tocados: `00_Serie/guiones/dias/Dia-03-crm-solidworks.md`, este relevo. `Dia-03.md` (DIAN) no se tocó.
- Decisiones del usuario: la sesión de hoy es CRM + SolidWorks, no la DIAN.
- Pendiente / siguiente paso: el usuario decide cómo tratar la promesa de la DIAN del Día 2 (recomendado: decirlo en cámara y moverla al Día 4 o 5); el orquestador ajusta `plan-42.md` y `estado.md` y añade a `hechos.md` que es estudiante. Llenar los `[DATO]` después de grabar.
- Problemas: `start.ps1 -Demo` exige la base `crm_demo` creada y nadie lo ha corrido; la sesión mezcla dos temas, lo que baja "un solo tema".

## 2026-10-10 · editor (Día 3)
- Hice: Día 3 editado desde un clip de WhatsApp de 100 s (de noche, caminando) → `Dia-03/entregables/Dia3_final_tiktok.mp4` y `Dia3_final_reels.mp4` (56,6 s). Estilo v10 del Día 2: texto detrás de la persona (10 palabras), 11 escenas FS de marca (adelantar, pendiente, DIAN "próximamente", skill, tres videos, errores, consumo de IA, Claude/Opus, medidor pesado, tokens, 12 proyectos) y cierre "DÍA 3 de 42" con 3 casillas. Audio v8 (-11,4 LUFS, pico -1,4 dBTP) y 69 SFX.
- Archivos tocados: `Dia-03/*` (creado con `new_day.py`), `brief.md`, `proyecto/*`, `00_Serie/relevo.md`, `estado.md` (fila del Día 3). En la skill: `scripts/audio_env.py` ahora acepta `AUDIO_THR` (la copia de la skill no lo tenía).
- Decisiones de gusto pendientes: el usuario no eligió tomas ni escenas; se le muestran al entregar.
- Pendiente: portada y caption del Día 3 (`monoga-serie`). La DIAN prometida en el Día 2 queda "pendiente" en el video, sin fecha.
- Problemas: (1) en el crudo sale otra persona en 0-3 s y en 24-35 s; se tapó con escenas, no se usó su toma. (2) La calle no tiene silencios: `validate_edl` no sirve; se usó `plan/edl_calle.py` (bordes al mínimo de energía). (3) `audio_pro.py` de la skill no tiene el preset v8; se copió el del Día 2. La cadena v8 retrasa la voz 33 ms (rubberband): el Día 2 v10 probablemente lo tiene; aquí se compensó. Conviene llevar v8 y la compensación a la skill. (4) Imagen de 576 px escalada a 1080: se ve blanda.

## 2026-10-11 · editor (entreno01: ref3 en marfil + oro)
- Hice: clip de entrenamiento de 5,9 s que replica la estructura de ref3 (earnedits) con la frase "¿Cristiano Ronaldo piensa que es el número 1? No, él sabe…": `Dia-04/entregables/entreno01_ref3_premium.mp4`, `entreno01_hoja.jpg`, `entreno01_vs_ref.jpg`. HyperFrames en una sola composición (`Dia-04/proyecto/entreno01/motion/index.html`), usuario recortado con rembg sobre marfil, "Nº1" detrás de él, 5 fotos CC de Commons (licencias en `entreno01/recursos.md`), 22 SFX por código. -14,2 LUFS, pico -1,9 dBFS.
- Archivos tocados: solo `Dia-04/proyecto/entreno01/` y `Dia-04/entregables/`. Los crudos no se tocaron.
- Aprendido: (1) los tiempos que dio Whisper sobre el video largo estaban corridos hasta 0,5 s ("no" caía en silencio); al transcribir el clip solo y ubicar las "s" con energía por encima de 4 kHz, cuadraron. (2) Un `background-clip:text` dorado desaparece si a la palabra se le anima `filter: blur`: usar color sólido en las palabras que entran con desenfoque. (3) `data-media-start` funciona para enganchar el webm con alfa al corte.
- Pendiente: que el usuario lo vea y diga qué se acerca o se aleja de la referencia; atribución CC BY/BY-SA en el texto del post si se publica.

## 2026-10-11 · editor (entreno02: blanco pastel + dorado suave, estilo Adrià)
- Hice: `Dia-04/entregables/entreno02_premium.mp4` (6,3 s), `entreno02_hoja.jpg`, `entreno02_vs_r1.jpg`. Gancho de la ronda 1 (golpe, bloques, ráfaga con 4 esquinas, glitch) sobre blanco pastel con puntos; destello crema con corte en el pico (2,60 s); su video real a pantalla completa con zoom 1,00→1,07 easeInOutSine (Lanczos subpíxel), color medido (receta G), subtítulos Montserrat 86 px, "Nº1" en la pared que viaja a la placa final. Audio: mic del PC + 15 % celular, −13,8 LUFS, −3,2 dBTP. Sin bordes redondos, sin recortes, sin fondos dorados.
- Skill nueva `.claude/skills/monoga-adria/` (v1 pendiente de aprobación; SKILL.md + 5 scripts + plantilla HTML).
- Archivos tocados: `Dia-04/proyecto/entreno02/`, `Dia-04/entregables/entreno02_*`, `.claude/skills/monoga-adria/`. Crudos sin tocar.
- Pendiente: que el usuario lo vea y apruebe paleta, puntos, piel y la skill; atribución CC de las fotos si se publica.

## 2026-10-13 · editor (Día 4 final, marca personal, skill monoga-adria v2)
- Hice: `Dia-04/entregables/Dia4_final_tiktok.mp4` (85,7 s, 1080x1920, 30 fps), `Dia4_hoja.jpg`, `Dia4_edl.md`, `Dia4_recursos.md`. Bloques: gancho → entreno02 (Cristiano) → tensión (lista de fracasos sin "agencia de IA") → comentario sobre *Esencialismo* (cámara A) → 2 mini citas del libro con su voz → giro en biblioteca 2.5D (Commons CC BY-SA, profundidad con Depth Anything) → "agente editor de video" con motion graphic estilo Adrià 5:28 + invert flash + glitch Mixkit → convicción → cierre → placa "DÍA 5 de 42". LUT Adrià 75 % solo en la persona. Voz: -17,7 LUFS, LRA 4,5, TP -2,4 dBTP (medido en el MP4). Audio vs celular por tramo: ≤ 5 ms.
- Skill `monoga-adria` v2: SKILL.md (94 líneas), `references/` (voz-y-color, motion-graphic-528, camara-entorno-891, flujo-marca-personal, plantilla_dia4.tpl.html), `assets/` (3 LUT, SFX Mixkit + licencia, SFX sintético), scripts nuevos (voz_adria, make_base general, scene25d, depth, post_fx, build_audio, sfx, onsets, tr_*, env, local_off, faces, words_tl, build_html). Sigue "pendiente de aprobación".
- Archivos tocados: `Dia-04/proyecto/dia4_final/`, `Dia-04/entregables/Dia4_*`, `.claude/skills/monoga-adria/`, este relevo. Crudos sin tocar. No toqué estado.md ni hechos.md.
- Pendiente: que el usuario lo vea y apruebe (tomas, títulos, citas, nivel del glitch); caption con la atribución de `Dia4_recursos.md`; confirmar la licencia en la página del sonido Mixkit 1022; decidir si es "Día 4" o "Día 5" (la placa dice 5, variable `DIA`).
- Problemas: no se oyó el audio (todo medido); la sincronía labios-voz se verificó por audio (xcorr con el celular), no con `lipsync.py`; el render de HyperFrames tarda ~12 min para 85 s.

## 2026-10-13 · editor (Día 4 v1 "número 1", showreel de motion, Opus)
- Hice: `Dia-04/entregables/Dia4_v1_numero1.mp4` (90,75 s, 1080x1920, 30 fps, H.264 CRF 18, AAC 48 kHz), `Dia4_v1_hoja.jpg` (2 fps), `Dia4_v1_edl.md` (tramos + licencias). Proyecto `Dia-04/proyecto/v1_numero1/` (EDL `plan/edl.py`, plantilla `plan/index.tpl.html`, beats compartidos HTML/SFX en `plan/beats.json`). Una historia continua del celular B: número 1 → Cristiano (entreno02) → "los mejores se creen los mejores" → desde pequeño → fracasos (6 fichas tachadas, sin "agencia de IA") → "perdí la habilidad… es muy grave" → organizando mi vida → habilidades/fruto → "no va a ser suerte" → esfuerzo/años → 42 días → placa DÍA 5 de 42. Persona solo ~19 % (mira a cámara o tensión); 10 escenas de motion; 2 invert flash con glitch Mixkit.
- Audio: SOLO mic del PC (t_PC = t_B + 2161,9651; medido ±1,6 ms en 6 puntos), HPF 70 Hz, fundidos 12 ms, compresor 2:1, SFX −15 dB (≥4 dB bajo la voz, mediana 31 dB). MP4: −17,6 LUFS, TP −3,1 dBTP, LRA 6,9. Sincronía voz vs celular por tramo en el MP4: ≤ 1 ms.
- Crudos sin tocar. No toqué estado.md ni hechos.md.
- Pendiente: que el usuario lo vea/oiga y apruebe; atribución CC de las fotos de Cristiano en el caption; confirmar licencia Mixkit 1022.
- Problemas: loudnorm 2 pasadas cae en modo dynamic (se usó ganancia lineal + limitador, como dice la skill); LRA 6,9 (Adrià 4,5); `lipsync.py` no concluyente (manos frente a la boca), la sincronía se verificó por audio.

## 2026-10-13 · editor (Día 7 "ventas con IA", Opus)
- Hice: el proyecto `Dia-07/proyecto/ventas_ia/` completo hasta el render. EDL de 52,74 s (`plan/edl.py`, bordes medidos en la envolvente y cada pieza comprobada con whisper), base de la persona solo en B1–B3b (`scripts/base_dia7.py`, LUT 75 %), composición HyperFrames (`plan/index.tpl.html` → `motion/index.html`, lint con 0 errores, snapshots revisados y corregidos), SFX (`scripts/sfx.py`), mezcla (`scripts/mix_dia7.py`): voz del celular, música Mixkit 464 con ducking y `audio/final.wav` a -17,6 LUFS, LRA 4,6, TP -2,7. Entregables: `Dia7_edl.md` y `LICENCIA_musica.txt`.
- (Corregido por el orquestador) El primer render falló al escribir el MP4 porque el editor borró la carpeta temporal `.hf-transaction` mientras seguía vivo; no fue la memoria. El orquestador lo relanzó con `--low-memory-mode -w 1` + `post_fx.py`: `Dia7_ventas_ia.mp4` (52,74 s, 1080x1920, -17,6 LUFS, LRA 4,6, -2,7 dBTP) y `Dia7_hoja.jpg` listos el 2026-10-13.
- Para terminar (con memoria libre): `cd Dia-07/proyecto/ventas_ia/motion && npx --yes hyperframes@0.8.141 render -o ../build/motion.mp4 .` (unos 15 min), luego `cd .. && python scripts/post_fx.py ../../entregables/Dia7_ventas_ia.mp4` (invert flash en 3,40 s + mezcla), medir con ebur128 y sacar la hoja a 2 fps.
- Archivos tocados: solo `Dia-07/` y este relevo. El crudo no se tocó. No toqué estado.md ni hechos.md.
- Problemas: el cuadro del Agency Agents usa los nombres de los repos y no muestra cifras; el "empleado de ventas" sale "EN ENTRENAMIENTO" (🟡). El cuadro verde detrás de él se ve en las tomas de persona (fondo real, no se tocó).

## 2026-10-14 · portada Día 7 (subagente)
- Hice: `Dia-07/entregables/Dia7_portada_A_3x4.jpg` ("CONSTRUYO MUCHO / *no vendo nada*"), `Dia7_portada_B_3x4.jpg` ("ENTRENO A MI / *vendedor IA*"), sus `_9x16.jpg` (misma tarjeta 3:4 centrada en 1080x1920 + "#42DiasLoovo · LOOVO" abajo) y `Dia7_portada_miniatura_200px.jpg` (prueba de legibilidad). Foto: crudo `VID_20261013_110529.mp4` en t≈3,15 s (mira a cámara, el más nítido de 6 medidos por Laplaciano), LUT `adria_look_75.cube` + verdes desaturados al 85 %, rectángulo sin bordes redondos, fondo real. Fondo pastel con puntos, clave en Playfair cursiva dentro de caja carbón con cursor dorado. Render: HTML + chrome-headless-shell de Playwright, uno por uno.
- Archivos tocados: solo esos 5 JPG en `Dia-07/entregables/` y este relevo. Crudo sin tocar. No toqué estado.md ni hechos.md.
- Pendiente: que el usuario elija A o B.
- Problemas: reflejo azul de las gafas sobre los ojos (viene de la toma); "DÍA 7 de 42" no se lee a 200 px (solo el titular); B dice "vendedor IA", que está en entrenamiento (🟡).

## 2026-10-17 · Antigravity/Claude (Nicho Contadores D1/D2/D3)
- Hice: `GEMINI.md` y `AGENTS.md` reescritos como espejo de `CLAUDE.md` con ODD y el flujo serie→guionista→adria→editor; las 4 skills copiadas a `.gemini/skills/` y `.agents/skills/` (94 archivos c/u, sin `__pycache__`); `.atl/skill-registry.md` refrescado. Paquete en `Dia-08/proyecto/contadores_ia/` (brief, caption, `plan/`: guion, higgsfield, edición HyperFrames, sfx, portada, revisión de hechos).
- Corregí el plan anterior (`odd/plans/campana-contadores-01.md`): quitó cifras no medidas, bancos/Siigo/Alegra y el guion hablado completo.
- Archivos tocados: esta carpeta y este relevo. No toqué estado.md ni hechos.md (propuestas en `plan/revision_hechos.md`).
- Problemas: los 3 sistemas no están en `hechos.md`; el logo de Tiendas D1 es marca ajena; una colaboradora en cámara choca con la regla 3; falta el crudo, el hook de Higgsfield y la portada.

## 2026-10-17 · worker-redes (Claude Opus) · Canal 17h, corte 2 full motion
- Hice: `canal/2026-10-17_17h/entregables/corte2_fullmotion_9x16.mp4` (41,95 s, 9:16, cero cuadros de cámara, voz del crudo + inserts de pantalla + motion HyperFrames). I -17,6 LUFS, música 7 dB bajo la voz, 97 SFX a -15 dB, 2 invert flash.
- Archivos: `canal/2026-10-17_17h/proyecto/c2/` y `NOTAS.md`. Corte 1 y crudos intactos.
- Pendiente: confirmar "tokens" vs "toques" (107,2 s), aprobar música/SFX de oído; comparación con el Día 1 en NOTAS.md.

## 2026-10-17 · canal 17h · corte 3 split
Hecho `canal/2026-10-17_17h/entregables/corte3_split_9x16.mp4` (41,9 s): motion del corte 2 arriba, pantalla abajo con zoom que sigue al cursor y se acerca en "acá/aquí/esto". -17,6 LUFS, cero cámara, claves/rutas desenfocadas por OCR. Pendiente: que el usuario lo vea en el celular y confirme el diagrama de Reddit visible. Detalle en NOTAS.md.

## 2026-10-20 · worker-edicion · canal 2026-10-17_19h (contadores)
Editado VID20261017194137 -> canal/2026-10-17_19h/entregables/ (mp4 66,4 s, portada.png Codex, descripcion.txt). Verde corregido, audio saturado reparado, -17,6 LUFS. Pendiente: confirmar palabras dudosas (ver NOTAS.md) y que el usuario lo vea/oiga.
