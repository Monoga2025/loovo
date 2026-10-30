---
name: monoga-adria
description: "Editor de video 'nivel Adrià Solà' para Loovo con la marca minimalista blanco pastel + dorado suave: persona real a pantalla completa con zoom de respiración y color LUT Adrià, voz al nivel medido de Adrià (-17,6 LUFS), destello crema, motion graphic con caja de palabra clave y salida 'invert flash' con glitch, cámara 2.5D que se mueve en el entorno con títulos cinéticos sincronizados con la voz. Para videos de marca personal y shorts (9:16) y YouTube (16:9). Úsala cuando el usuario pida 'estilo Adrià', 'premium/orgánico/minimalista', 'blanco y dorado', 'motion graphics como Adrià', 'invert flash', 'cámara en el entorno', o edite un video de cabeza hablando. Estado: v2 pendiente de aprobación del usuario."
---

# monoga-adria · v2 (pendiente de aprobación del usuario)

Probada en: `entreno02_premium.mp4` (6,3 s, el usuario: "perfecto") y **`Dia-04/entregables/Dia4_final_tiktok.mp4`** (85,7 s, 3 fuentes, todas las recetas de abajo marcadas PROBADO).
**[por probar]** = aún no se usó en un video real.
Complementa a `monoga-editor` (pipeline general, HyperFrames, Whisper). Contexto: `Loovo-42/CLAUDE.md`, `00_Serie/estado.md`, `relevo.md`, `hechos.md`. Claude no ve ni oye: todo se mide.

## 0. Qué modelo hace qué (instrucción del usuario, 2026-10-13)
- **Opus:** solo motion graphics y edición de video (composición HyperFrames, escenas, transiciones, render visual).
- **Haiku:** todo lo demás que no sea motion ni complejo: sincronizar y mezclar audio, medir (LUFS, color, cortes), transcribir, recortar, remux, hojas de contacto, copiar archivos y documentar.
- El orquestador solo razona y decide. Al delegar, se pasa `model: "haiku"` u `model: "opus"` explícito.

### 0.1 REGLA OBLIGATORIA del motion (usuario, 2026-10-13)
Para el motion graphic de cada video se abre un subagente **Opus** al que se le pasan los colores de la marca, el guion con tiempos y el material, y **este prompt literal** (no se reescribe ni se resume):

> make a dynamic motion graphics video that shows what an incredible motion designer you are, y muestra la persona hablando solo cuando mire la cámara y cuando genere tensión, like it's your showreel for a résumé. go all out.

Objetivo: retención. Más motion, no menos: la persona sale solo cuando mira a cámara o genera tensión; el resto es motion. Las prohibiciones de §1 siguen valiendo (son contexto, no límites a la ambición).

### 0.2 Antes de editar: estudio de contenido (Haiku)
El usuario dijo del Día 4: "no tiene contexto… no tiene sentido… cogiste re mal las partes". Nunca se arma un video con frases sueltas. Haiku extrae los subtítulos completos, estudia qué conecta con qué y revisa los fotogramas (mira a cámara, energía), y propone **3 a 5 videos por cada crudo largo**. Cada uno debe entenderse solo: gancho → contexto → tensión → resolución → cierre, sin saltos de tema. El orquestador revisa que la historia tenga sentido antes de pasar a Opus.

## 1. Prohibiciones (feedback literal del usuario)
1. **Bordes redondos: nunca.** `* { border-radius:0 !important; }`. Solo los puntos del fondo son redondos.
2. **No recortar su silueta ni cambiar su fondo.** Su video va real, a pantalla completa.
3. **Nada de fondos dorados** ni degradados oro a pantalla completa (el dorado es acento).
4. Nada de verde/lima, azul eléctrico, rojo, magenta, oro saturado. En fotos de B-roll, los verdes se neutralizan (`scene25d.py grade()`).
5. **Texto ilegible = fallo:** frases ≥ 80 px, claves ≥ 118–150 px en 1080x1920; tarjeta completa ≥ 0,5 s; nada de etiquetas de 30 px.
6. **Música (cambio 2026-10-13, decisión del usuario):** sí lleva cama musical, baja bajo la voz (ducking, la voz sigue a -17,6 LUFS) y sube en los huecos y en las escenas de motion; estilo según el usuario, licencia verificada. Sin punch-in seco sobre la persona.
7. Solo se afirma lo ✅ de `hechos.md`: si una frase choca, se corta (mejor si el corte cae bajo una escena gráfica).
8. **Tema (2026-10-13):** videos de IA y del canal (Loovo, CRM, agentes, cómo se construye). Nada que suene a motivacional o autoayuda: el usuario no lo publica.

## 2. Paleta y tipografía
| Rol | Valor |
|---|---|
| Fondo | blanco pastel `#F6F4EF` + puntos `radial-gradient(circle at 12px 12px, rgba(170,165,156,.42) 0 1.1px, transparent 1.6px) 0 0/24px 24px`; grano `multiply` 5 % |
| Dorado | base `#C8B07A` (líneas, cursor), sombra `#A88F57` (texto dorado sobre pastel), brillo `#E6D6AE` (clave sobre video o carbón) |
| Texto | carbón `#2A2926`, gris `#8C887F`, crema `#FBF8F1` sobre video |
| Cajas | carbón con texto crema y clave dorada, o crema con texto carbón. Nunca dorado de fondo |
| Fuentes | Montserrat 500/600 (OFL) + Playfair Display 700 cursiva (clave/serif) |
| Sombras | difusas cálidas `0 34px 70px -24px rgba(90,74,44,.34)`; texto sobre video `0 2px 6px` + `0 6px 26px rgba(20,16,10,.38)` |

## 3. Las 4 recetas "nivel Adrià" (detalle en `references/`)
### 3.1 Voz — PROBADO → `references/voz-y-color.md`, `scripts/voz_adria.py`
- Objetivo medido en Adrià: **I -17,6 LUFS, LRA ~4,5, TP ≤ -2 dBTP**, medido en el MP4 final.
- **Solo el audio del PC (micrófono), 0 % celular** (usuario, 2026-10-13: "se escucha mil veces mejor… solo dejas el del PC"). El celular sirve solo como referencia de sincronía.
- Sincronizar **por ondas** (GCC-PHAT, `scripts/sync_audio.py`) cada tramo contra **todos** los archivos del PC del día (`CAMARA *.mp4`, `PANTALLA *.mp4`; OBS puede tener varias sesiones) y usar el de correlación más alta. Medir el offset por tramo (puede haber saltos de ~60 ms).
- Procesado mínimo para que suene natural: HPF 70 Hz + loudnorm 2 pasadas al objetivo; compresor solo suave (≤ 2:1) y EQ ≤ 1,5 dB si hace falta → SFX → limitador.
### 3.2 Color — PROBADO
- `assets/adria_look_75.cube` (elegida por el usuario; hay 50 y 100) horneada en la base con `lut3d=...:interp=tetrahedral`. **Solo sobre la persona**, nunca sobre gráficos/placas.
### 3.3 Motion graphic 5:28 + invert flash — PROBADO → `references/motion-graphic-528.md`
- Entrada: zoom-out radial de la persona en 4 cuadros (horneado) + whoosh que se corta seco → corte al gráfico a escala 4 con blur 18 → 1,05 `expo.out` 0,5 s, sin rebote → deriva con parallax.
- Texto palabra por palabra; cada repetición hace aparecer un objeto; **palabra clave en caja carbón con cursor dorado** que crece y revela el texto de izquierda a derecha.
- Salida: **invert flash diagonal de 8 cuadros** (`scripts/post_fx.py`) + **glitch Mixkit 1022** (0,30 s, desde el cuadro del pico). Máx. 2 por video.
### 3.4 Cámara en el entorno 8:51 + títulos cinéticos — PROBADO → `references/camara-entorno-891.md`
- Foto con licencia → `depth.py` (Depth Anything V2) → `scene25d.py`: 3 capas, parallax **1 : 1,65 : 1,9**, fondo ~4x más borroso, paneo `expo.out` 2,7 s, dolly-out `power2.inOut`, empuje `power4.in`, sin rotación, desenfoque de movimiento por submuestreo, zoom-through con disolvencia 6 cuadros + whoosh 2–16 kHz.
- Títulos: frase maquetada, palabras en su sitio, **onset = voz - 2 cuadros**, entrada 5–7 cuadros con blur + subida (serif 0,6→1), se van escalándose con el empuje.

## 4. Persona (base) — PROBADO
- `scripts/faces.py` → `scripts/make_base.py`: encuadre S0 = 1,10 con la cara en y≈660 (recortado al margen), warpAffine Lanczos subpíxel (sin `zoompan`, que tiembla).
- Programas de zoom por tramo (diccionario `Z`): respiración **easeInOutSine** 1,00↔1,07–1,09 en 3–11 s; el gancho arranca en 1,14 bajando (movimiento desde el cuadro 0).
- **Sin jump cuts dentro de un bloque**; si se quita algo (repetición o frase que choca con hechos), el corte se cubre con un **salto de zoom 1,00↔1,08/1,09** o cae bajo un gráfico.
- Zoom-through hacia un gráfico: último 0,55 s `power4.in` hasta 1,42 + blur 6 cuadros (en HTML) + disolvencia.
- Los huecos (`gap`) siguen el crudo del tramo anterior: nunca congelar.

## 5. Subtítulos y títulos
- Sobre la persona: **tarjetas de 2–4 palabras** (o 2 líneas), Montserrat 600 86 px crema, clave `#E6D6AE`, clave enfática en Playfair 150 (`~palabra~`), tachado dorado (`_palabra_`). Aparecen enteras al onset de su primera palabra - 2 cuadros (fundido + blur 8 px, 2 cuadros), salida seca. Base del texto en y≈1420 (zona segura TikTok: abajo 480 px). Sombra inferior leve (`#shade`).
- Listas cinéticas (p. ej. "Fracasé con:"): cada ítem aparece cuando lo dice y se tacha en dorado 0,45 s después. Mira dónde está su cara en ese tramo (y ≥ 1000).
- Gancho: título cinético grande (100 px + clave serif 170) con la primera palabra ya visible en el cuadro 0.
- Citas de libros (máx. 2–3 por video, 1 frase corta cada una, su voz leyendo): placa pastel, Playfair cursiva 84 px carbón, claves 118 px `#A88F57`, comilla dorada grande con parallax, atribución "— Libro, Autor" Montserrat 44 px gris.
- Palabras: whisper `medium` por tramo + `onsets.py` (envolvente). Whisper corre la 1.ª palabra de cada tramo hasta 0,5 s: se fija al primer sonido.

## 6. Transiciones (resumen)
| Caso | Transición |
|---|---|
| Gráfico → persona | **destello crema** 0,33 s (fuga 3 cuadros + blanco `#FFFBF2` 3 → corte en el pico → 4 cuadros `sine.out`; base sale de blur 6 px) + whoosh -8 dB |
| Persona → cita / B-roll | zoom-through (empuje `power4.in` + disolvencia 6 cuadros) + whoosh 2–16 kHz con pico 4–7 cuadros tras el corte |
| B-roll → B-roll | zoom-through con el movimiento continuando a través del corte |
| Persona → motion graphic | zoom-out radial + corte + aterrizaje `expo.out` |
| Motion graphic → persona | invert flash + glitch (máx. 2 por video) |
| Persona → persona (otro bloque) | corte en la pausa + salto de zoom; J/L-cut mínimo |
Siempre: corte en la pausa de la voz, la frase arranca 0–0,3 s después.

## 7. Estructura de un video de marca personal (Día 4, 85,7 s)
Gancho persona + título cinético (4 s) → prueba gráfica (entreno02, 6 s) → tensión (persona + lista, 16 s) → comentario propio (8 s) → 2 citas del libro (10 s) → giro en 2.5D (7 s) → prueba real con motion graphic (8 s) → convicción (9,5 s) → cierre (12 s) → placa "DÍA N DE 42" + #42DiasLoovo (2,4 s). Persona ~70 %, un cambio cada ~8–13 s.
Placa final: variable `DIA` al inicio del script de la plantilla.

## 8. Flujo paso a paso → `references/flujo-marca-personal.md`
1. Lee contexto, mapa y guion de edición. Confirma solo su voz (regla 3) y lo prohibido.
2. Bordes exactos (`tr_medium.py`, `env.py`, `tr_chunks.py`) → `plan/edl.py` (ejemplo `scripts/edl_ejemplo_dia4.py`).
3. Sync por tramo (`local_off.py`) → `build_audio.py` → palabras (`tr_final.py`, `onsets.py`, `words_tl.py`).
4. Base (`faces.py`, `make_base.py`), escenas (`depth.py`, `scene25d.py`), SFX (`sfx.py`), voz (`voz_adria.py`).
5. Plantilla `references/plantilla_dia4.tpl.html` → `build_html.py` → `lint` 0 errores → snapshots (~40) → corrige → render (máx. 2 completos).
6. `post_fx.py` (invert flash + mezcla + H.264 CRF 18 + AAC 320k 48 kHz) → verificación → entregables + relevo.

## 9. Checklist de verificación
- [ ] `grep border-radius` solo `0 !important`; sin siluetas recortadas; sin fondos dorados ni verdes.
- [ ] Hoja a 2 fps + cuadros clave ampliados (gancho cuadro 0, motion graphic, invert flash, cierre, último cuadro).
- [ ] Texto ≥ 80 px, ninguna tarjeta < 0,5 s, nada fuera del cuadro, nada sobre ojos/boca, zona segura.
- [ ] ebur128 en el MP4: I -17,6 ±0,5, LRA ~4,5, TP ≤ -2.
- [ ] Sincronía: `lipsync.py` en 2–3 tramos de persona; xcorr voz final vs celular por tramo ≤ ±20 ms.
- [ ] Nada que choque con `hechos.md`; sin datos de clientes; solo su voz.
- [ ] Recursos con licencia anotados (fotos CC BY/BY-SA con atribución para el caption).
- [ ] Di qué se midió y qué no.

## 10. Pendiente / por probar
YouTube 16:9 (pantalla + cámara OBS); clips de video por IA en lugar de 2.5D; glitch cromático en destellos; luz de noche; versión Reels con otra zona segura; aprobación del usuario de: velocidad de los títulos, lista tachada, citas, nivel del glitch.
Plantilla corta anterior: `references/plantilla_entreno02.html` y `scripts/legacy/make_base_entreno02.py`.
