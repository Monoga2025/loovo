---
name: monoga-editor
description: "Edita, corta, subtitula y reencuadra videos verticales para TikTok, Instagram Reels y YouTube Shorts, y añade motion graphics (subtítulos cinéticos, zooms de tendencia, escenas animadas, stickers, texto detrás de la persona, showreels) con ffmpeg, Whisper, rembg y HyperFrames. Úsala cuando el usuario pida editar un video para redes, elegir tomas de un material en bruto, quitar silencios o muletillas, subtitular, pasar de 16:9 a 9:16, corregir sincronía de voz, igualar color, poner textos detrás de la persona o hacer motion graphics o un showreel. Use for short-form video editing, captions, reframing, A/V sync, color matching, text-behind-subject and motion graphics requests."
---

# Monoga Editor (TikTok · Reels · Shorts + Motion)

Convierte footage real en videos verticales que retienen, con capas de motion hechas con código. Esta versión incorpora lo aprendido en un proyecto real: video "Día 1 de 42", con cuatro rondas de feedback del usuario.

**Contexto de la serie Loovo-42 (si trabajas dentro de `Loovo-42`):** antes de editar, lee `Loovo-42/CLAUDE.md`, `00_Serie/estado.md`, las últimas 5 entradas de `00_Serie/relevo.md`, `00_Serie/hechos.md` y el `brief.md` y `plan/` del día. Ahí está qué es Loovo, qué se decidió y qué ya se hizo. Al terminar, agrega tu entrada al final de `relevo.md` (qué hiciste, qué archivos tocaste, qué falta). No edites `hechos.md` ni `estado.md` sin avisar al orquestador, salvo la fila de tu día.

Lee las secciones 1–5 siempre. El detalle técnico está en `references/` y se lee cuando toque:
| Archivo | Cuándo leerlo |
|---|---|
| `references/cortes-sync-audio.md` | Antes de cortar; siempre que haya dudas de sincronía o loudness |
| `references/estilo-motion.md` | Antes de diseñar subtítulos, zooms, escenas u overlays |
| `references/color-y-recorte.md` | Para color y para el texto detrás de la persona |
| `00_Serie/marca/marca.md` | **Siempre.** Identidad IA MONOGA: colores, tipografía, elementos de firma |
| `references/motion-nivel-pro.md` | **Siempre antes de diseñar.** Emojis 3D, transiciones 3D, cortes con efecto, lo que el usuario exige desde la primera versión |
| `references/tecnicas-referencias.md` | **Siempre antes de diseñar escenas.** 9 técnicas probadas de 10 referencias (oclusión, contador rueda, marco fijo, vista explotada, máscara…), gramática de cortes y dónde conseguir recursos con licencia. Catálogo en `templates/hyperframes/examples/tecnicas_referencias.html` |
| `references/hyperframes.md` | Antes de tocar HyperFrames y cuando falle el linter o el render |
| `references/entorno-windows.md` | En Windows o con poca RAM |
| `templates/hyperframes/` | Plantillas de composición. `examples/` tiene el proyecto real completo |

---

## 1. Principios (no negociables)
1. **Claude no ve ni oye el video.** Trabaja con transcripción, fotogramas (Read) y mediciones. Claude propone la intención; el código mide y valida. Esto aplica también al color y a la sincronía: **se miden, no se opinan.**
2. **Todo plan vive en archivos revisables:** `plan/takes.json`, `plan/edl.json`, `plan/storyboard.md`, `plan/sfx.json`, `plan/grade_*.txt`.
3. **Los originales no se tocan.** Se trabaja sobre copias.
4. **Los medios los procesan los scripts deterministas de `scripts/`.** Cópialos al proyecto al empezar y no los reescribas.
5. **El gusto es del humano.** Ofrece 2–3 opciones concretas (AskUserQuestion funcionó bien) y deja elegir. Recomendar está bien; decidir solo, no.
6. **Local primero.** Nada sale del equipo sin aprobación: tampoco `hyperframes snapshot` sin `--describe false`.
7. **Nada inventado en pantalla.** Todo texto es literal de lo que se dice o un dato del usuario. Ojo con los sinónimos: "JUNTOS" no vale por "acompañen".

**9. Marca IA MONOGA siempre.** Colores, fuentes y firma en `00_Serie/marca/marca.md` y `marca.json` (dirección A "Eléctrico": carbón, azul eléctrico #2F5BFF, lima #C6FF3D, hueso; Space Grotesk + Instrument Serif cursiva). **Nunca rojo** (el usuario lo asocia con peligro). Los recursos salen de la biblioteca `00_Serie/recursos/` (`manifest.json` con fuente y licencia); amplíala con `scripts/recursos_pd.py` + `scripts/recursos_proc.py`, y los modelos 3D con `scripts/recursos_3d.py` (Poly Haven, CC0).
**10. Texto detrás de la persona por defecto.** Segmenta en segundo plano al empezar (`segment.py`, ~0,6 s por fotograma) y usa palabras gigantes dichas por el usuario sobre la pared. El usuario lo enseñó en el Día 1 y se quejó cuando faltó en el Día 2.

**8. Nivel pro por defecto.** El usuario espera objetos de apoyo (emojis 3D, imágenes), transiciones 3D y cortes con efecto sin pedirlos. Lee `references/motion-nivel-pro.md`.
**11. Gramática de las referencias.** Una idea = una composición, con corte duro entre ideas. El texto llega 0,1 s después de la imagen. Se alternan placas oscuras y claras. Los objetos en primer plano van desenfocados. Al menos una transición por oclusión (un objeto que cruza tapa el cambio). Usa las técnicas del catálogo (`references/tecnicas-referencias.md`) antes de inventar otras. Cuando una idea tenga un objeto físico (reloj, portátil, cámara, megáfono), usa un **modelo 3D real** con luz de marca (T10: `scripts/recursos_3d.py` + `examples/objeto3d_threejs.html`) antes que una foto plana.

## 2. Reglas duras (si una falla, no se entrega)
1. Las duraciones las mide ffprobe o un script, nunca una suma propia.
2. **Ningún corte cae sobre voz medida** (`validate_edl.py` con `audio_env.py`), ni sobra aire (más de 0,12 s al inicio o 0,20 s al final).
3. **Sincronía verificada:** `check_sync.py` da OK (audio contra diseño en ~0, labios contra voz dentro de ±45 ms) y el MP4 final se comprueba contra el corte.
4. Fade de 30 ms en cada corte de audio.
5. Gancho en 1–3 s. Ningún plano dura más de 5 s sin un cambio (zoom, overlay, palabra o escena).
6. Subtítulos siempre, dentro de la zona segura (arriba 270, abajo 480, izquierda 65, derecha 120 px).
7. **Nombres propios confirmados por el usuario.** Whisper oyó "lobo"/"luego"/"logo" y era **Loovo**.
8. **Solo la voz del usuario:** confirma que ninguna toma elegida la dijo otra persona. Una frase la dijo su novia.
9. Audio a -14 LUFS (±1) y pico real ≤ -1 dBTP, **medido en el MP4 final**. La música va 18–20 dB bajo la voz, medida sobre el stem duckeado.
10. Música y SFX generados por código o con licencia clara, anotados en `credits.md`.
11. **Mira antes de entregar:** snapshots o hoja de contactos de cada escena, zona segura y un recorte de detalle donde haya riesgo (bordes, puntuación). Esa revisión encontró 6 bugs que el linter no vio.
12. Máximo 3 iteraciones automáticas por problema; después, reporta con evidencia.
13. Ningún elemento tapa ojos o boca, ni siquiera un glitch de 0,3 s. Los stickers van del lado donde no está la cabeza (mídelo).
14. **Mira el último fotograma y el de la portada a tamaño completo** antes de entregar: sin cara a mitad de palabra ni con zoom fuerte. Termina en un fotograma con la boca cerrada.

## 3. Intake / brief (una sola ronda de preguntas)
Escribe `brief.md`. Pregunta solo lo que falte, idealmente en **una AskUserQuestion**:
| Pregunta | Por qué (lección aprendida) |
|---|---|
| **¿Tienes un video de referencia del estilo?** | Sin referencia, los subtítulos y zooms por defecto fueron rechazados. Con referencia, el usuario quedó encantado al primer intento. |
| **¿Cómo se escribe tu marca o nombre?** | Whisper no conoce las marcas. |
| ¿Hay más personas que hablan o aparecen? | Evita usar tomas o fondos con otra persona. |
| Plataformas, duración y objetivo | Por defecto: TikTok + Reels, 20–40 s, educar. |
| Nivel (1 esencial / 2 pro / 3 motion) | El usuario puede saltar al 3 si trae referencia. |
| Qué NO debe aparecer | — |

Si el material es largo y con muchas tomas, dilo en el brief: en ese caso el Nivel 1 consiste en elegir tomas.

## 4. Estructura del proyecto
```
proyecto/
  brief.md  brand.json  credits.md
  input/ (copia del original)   audio/ (audio.wav, music.wav, music_ducked.wav, sfx.wav)
  transcript/ (words.json, transcript.txt)
  plan/ (takes.json, edl.json, validate.txt, storyboard.md, sfx.json, grade_natural.txt, timemap.json)
  build/ (cut.mp4, words_out.json, seg/mask.mp4, r_*.mp4, motion.mp4, final_audio.wav)
  motion/ (proyecto HyperFrames: index.html, compositions/, assets/)
  ref/ (referencia del usuario + hoja de contactos)
  qa/ (contact.png, safezone.png, report.md, comparativas de color)
  out/ (final_tiktok.mp4, final_reels.mp4)
  scripts/ (copia de los scripts de la skill)
```
`brand.json` guarda paleta, fuentes, zona segura y `vocab` con la ortografía correcta de las marcas.

## 5. Pipeline

### 5.1 Ingesta y transcripción
```bash
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate,start_time -show_entries format=duration -of compact input/clip.mp4
ffmpeg -y -i input/clip.mp4 -vn -ac 1 -ar 16000 audio/audio.wav
python scripts/transcribe.py audio/audio.wav transcript/words.json es auto
```
- Fíjate en el `start_time` del audio. Si es mayor que 0 (los celulares suelen dar ~0,18 s), `build_cut.py` lo compensa; no lo ignores.
- Haz una hoja de contactos del original (`fps=1/20,tile=8x3`) para ver encuadre, cara y personas al fondo.
- Corrige los nombres en `words.json` (solo el texto, nunca los tiempos) y genera `transcript.txt` con frases y pausas.

### 5.2 Selección de tomas y EDL
- `plan/takes.json`: una toma por línea del guion, con `start`, `end` y `note` (texto). Muestra al usuario la lista con los segundos de origen.
- `python scripts/make_edl.py plan/takes.json transcript/words.json plan/edl.json`. Parte las pausas internas de más de 0,45 s y ajusta cada borde a la voz medida.
- `python scripts/validate_edl.py plan/edl.json transcript/words.json | tee plan/validate.txt`. Revisa a mano los avisos (inicio con "y", frase partida) y justifícalos en el reporte.

### 5.3 Corte y verificación de sincronía
```bash
python scripts/build_cut.py plan/edl.json build/cut.mp4 transcript/words.json   # compensa start_time + ajusta a fotograma
python scripts/check_sync.py plan/edl.json build/cut.mp4 audio/audio.wav        # debe dar OK
```

### 5.4 Base para motion
```bash
ffmpeg -y -i build/cut.mp4 -vf "fps=30,scale=1080:1920,setsar=1" -an -c:v libx264 -crf 17 -g 15 -pix_fmt yuv420p motion/assets/base.mp4
```
- Si el origen es 16:9, recórtalo a 9:16 decidiendo la `x` con un fotograma.
- **Color:** mide primero (`measure_color.py`) y aplica por defecto la receta natural de `references/color-y-recorte.md`. Hornéala en `base_graded.mp4` y `pip_graded.mp4`, que va a 540×960.

### 5.5 Diseño (storyboard)
- **Analiza la referencia:** `ffmpeg -i ref/x.mp4 -vf "fps=2,scale=180:-1,tile=9x4" -frames:v 1 ref/contact.png`. Anota paleta, tipografía, motivos y transiciones.
- **Escribe `plan/storyboard.md`:** segundo, tipo (cabeza hablando o escena FS), texto literal, técnica y sonido. Las escenas FS van sobre las frases más visuales o sobre tomas con problemas (otra persona al fondo).
- **Catálogo de técnicas, zooms y overlays:** `references/estilo-motion.md`.

### 5.6 Composición (HyperFrames)
1. Instala, crea el proyecto y copia `templates/hyperframes/*` (ver `references/hyperframes.md`).
2. Escribe los zooms en `index.html`. Para los subtítulos, `python scripts/make_caps.py build/words_out.json motion/compositions/graphics.html --keys "..." --skip "<tramos FS>"`; elige las palabras clave con criterio.
3. Si hay texto detrás de la persona: `segment.py` en segundo plano → `person.webm` → `behind.html`.
4. Pasa `npx hyperframes lint` hasta tener 0 errores. Después, snapshots (`--describe false`) de cada escena y de cada palabra de fondo; corrige lo que veas.
5. **Render.** Si se atasca con el alfa, usa el plan B (`make_variants.py` → 3 renders → `composite_behind.py`).

### 5.7 Audio
- **Música:** `make_music.py`, con ducking (`sidechaincompress`) contra la voz del corte. Mide el stem duckeado: unos 19 dB bajo la voz.
- **SFX:** `make_sfx.py` con `plan/sfx.json`, un efecto por golpe visual.
- **Mezcla:** `amix normalize=0`, SFX a -8 dB, `loudnorm` en dos pasadas con `TP=-2`, `linear=true` y `alimiter=0.708`. Con `alimiter` agrega `level=disabled`: sin eso sube el nivel solo y el pico pasa de 0 dBFS.

#### 5.7b Audio pro (aprendido en el Día 1): `scripts/audio_pro.py`
Reemplaza la música suave y el ducking por compresión de 5.7 cuando el usuario quiere música audible y épica, y limpia los golpes del dedo en la mesa.
```bash
python scripts/audio_pro.py <carpeta del proyecto> --preset v4|v5 [--under <dB>] [--sufijo <nombre>]
```
Necesita `build/cut.mp4`, `build/words_out.json` y los `out/final_tiktok.mp4` y `out/final_reels.mp4` ya renderizados. Escribe `out/final_<plataforma>_<preset>.mp4` y deja los intermedios en `audio_pro/`.
1. **Golpes:** detecta golpes de dedo por forma de onda (banda 60 a 500 Hz, ataque de más de 10 dB y caída de más de 10 dB en 60 ms), los atenúa en esa banda y baja del todo los que caen en una pausa. Imprime los tiempos para que el usuario los escuche. Claude no oye, así que no declares el audio limpio; di cuántos se detectaron y cuántos quedan.
2. **Música épica** (`make_epic.py`, por código, libre de derechos): Re menor, 100 BPM, pad, sub, taiko, risers, metales, coro.
3. **Ducking por voz** (no por sidechain): la música baja mientras hablas y sube 9 dB en los huecos de más de 0,12 s. Recorta 300 Hz y 1,5 kHz de la música para no tapar la voz.
4. **Presets:** `v4` = música a 1,5 dB bajo la voz, final original, imagen sin recodificar (remux). `v5` = 3 dB bajo la voz, golpe de apertura a +4 dB los primeros 0,3 s y 2 s extra de música sola con desvanecido a negro (recodifica la imagen, tarda unos 4 minutos).
5. Si el video casi no tiene pausas (el Día 1: 157 palabras, 5 huecos), la música casi no sube. Dilo antes de prometer el vaivén.
6. Está pendiente saber cuál preset funcionó mejor (A/B del Día 1). Hasta saberlo, ofrece los dos.

### 5.8 Exportación
```bash
# TikTok
ffmpeg -y -i build/motion.mp4 -i build/final_audio.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart -shortest out/final_tiktok.mp4
# Reels
ffmpeg -y -i build/motion.mp4 -i build/final_audio.wav -map 0:v -map 1:a -c:v libx264 -profile:v high -level 4.2 -b:v 4500k -maxrate 5000k -bufsize 10000k -pix_fmt yuv420p -r 30 -c:a aac -b:a 128k -movflags +faststart -shortest out/final_reels.mp4
```
Si solo cambia el audio, remuxea; no vuelvas a renderizar.

## 6. QA y entrega
```bash
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate,duration -of compact out/final_tiktok.mp4
ffmpeg -i out/final_tiktok.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:"
ffmpeg -y -i out/final_tiktok.mp4 -vf "fps=1,scale=216:-1,tile=8x5" -frames:v 1 qa/contact.png
ffmpeg -y -ss <t> -i out/final_tiktok.mp4 -frames:v 1 -vf "drawbox=x=0:y=0:w=iw:h=270:color=red@0.35:t=fill,drawbox=x=0:y=1440:w=iw:h=480:color=red@0.35:t=fill,drawbox=x=960:y=270:w=120:h=1170:color=red@0.35:t=fill,drawbox=x=0:y=270:w=65:h=1170:color=red@0.35:t=fill" qa/safezone.png
```
**Checklist:**
- [ ] duración medida
- [ ] 1080×1920, 30 fps, H.264 + AAC
- [ ] -14 LUFS y pico ≤ -1 dBTP en el final
- [ ] `validate.txt` OK
- [ ] `check_sync` OK
- [ ] gancho antes de 1–3 s
- [ ] nombres correctos
- [ ] solo la voz del usuario
- [ ] texto literal
- [ ] nada sobre ojos o boca
- [ ] zona segura
- [ ] palabras de fondo legibles
- [ ] `credits.md`
- [ ] `qa/report.md` actualizado

**Entrega:**
- **El video:** envíalo con SendUserFile y sus rutas.
- **Qué cambió:** las cifras medidas.
- **Qué no se pudo verificar:** como mínimo, que Claude no oye la mezcla.
- **Decisiones de gusto pendientes:** 2–3 opciones.
- **Momentos concretos (segundo + palabra)** para que el usuario verifique la sincronía y los golpes.

## 7. Cómo interpretar el feedback del usuario (casos reales)
| Lo que dijo | Qué significaba | Qué se hizo |
|---|---|---|
| "los cortes están muy al empezar y terminar… empieza después y termina antes" | Sobra aire en los bordes | Ajustar bordes a la voz medida |
| "eso lo dijo mi novia, no yo" | Otra voz en una toma elegida | Buscar una toma del usuario y confirmar todas las tomas |
| "esos zoom no son nada que ver con tendencias" / "la tipografía qué mierda" + video de referencia | Quiere el lenguaje de la referencia | Estilo de `estilo-motion.md` |
| "se siente raro, como muy iluminado versus la animación" | El footage no casa con la paleta | **Medir** (estaba gris, frío y plano), no adivinar |
| "el tono se ve re falso… mover un poco la exposición, brillo, mini viñeta" | Prefiere lo natural a igualar el color | Receta natural, sin tinte |
| "quedó corrida la voz con el video" | Desfase de sincronía | `start_time` del audio (0,18 s); verificar con `check_sync` |
| "que los motion se sobrepongan cuando hablo… letras detrás de mí legibles" | Overlays sobre la cabeza hablando + texto detrás del sujeto | `overlays.html` + recorte con rembg + `behind.html` |

## 8. Niveles
- **Nivel 1 – Esencial:** elegir tomas o limpiar → corte validado y sincronizado → 9:16 → subtítulos → loudnorm → exportación. Si no hay HyperFrames, sirve `build_ass.py`, pero avisa que el estilo es básico.
- **Nivel 2 – Pro:** subtítulos cinéticos (`graphics.html`), zooms de tendencia, gancho, música con ducking, SFX y color natural.
- **Nivel 3 – Motion completo:** escenas FS de showreel, overlays mientras habla, texto detrás de la persona, PiP y cierre en loop.

## 9. Esfuerzo y ejecución larga
- **Tareas largas** (segmentar ~20 min, renders de 4–7 min, transcripción): en segundo plano, y avisa al usuario en una línea qué estás haciendo. Para esperar usa bucles `until`, no `sleep` encadenados.
- **No termines el turno** hasta entregar el MP4 y el reporte, salvo que falte una decisión del usuario.
- **Subagentes:** solo para trabajo grande y paralelizable. La verificación la hacen los scripts y los snapshots.

## 10. Scripts (`scripts/`)
| Script | Qué hace |
|---|---|
| `transcribe.py` | faster-whisper en CPU, `auto` = medium → small si no hay RAM |
| `audio_env.py` | Envolvente de voz (umbral -36 dB) para ajustar y validar cortes |
| `make_edl.py` | `takes.json` → EDL con bordes ajustados a la voz real |
| `validate_edl.py` | Rangos, voz en los cortes, aire sobrante, duración |
| `build_cut.py` | Corte con fades y compensación del `start_time` del audio, bordes a fotograma y `words_out.json` realineado |
| `check_sync.py` | Audio contra diseño y labios contra voz, por clip |
| `make_caps.py` | Frases de subtítulos cinéticos en `graphics.html` |
| `segment.py` | Máscara de la persona (rembg u2net, local) |
| `make_variants.py` + `composite_behind.py` | Plan B del texto detrás sin video alfa en Chrome |
| `measure_color.py` | Lab de pared, cara y esquinas, L* y percentiles |
| `make_music.py` / `make_sfx.py` | Música y efectos generados por código |
| `build_ass.py` | Subtítulos ASS básicos (solo si no hay motion) |
