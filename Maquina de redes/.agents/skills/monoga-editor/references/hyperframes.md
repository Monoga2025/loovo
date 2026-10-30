# HyperFrames: cómo se usó y sus trampas (v0.8.140)

## Setup
- `npx -y hyperframes --version` lo instala. El Chrome headless y las fuentes (Inter, Roboto) quedan en `~/.cache/hyperframes`.
- **Si el usuario ya usó HyperFrames,** revisa `~/.hyperframes` para saber que hay caché.
- **Proyecto:** `HYPERFRAMES_SKIP_SKILLS=1 npx -y hyperframes init motion --example kinetic-type --resolution portrait --non-interactive --skip-transcribe`.
  - El ejemplo `video-edit` ya no existe; los nombres válidos salen en el error.
  - Después reemplaza `index.html` y `compositions/` por `templates/hyperframes/`.
- **Docs offline:** `npx hyperframes docs data-attributes|compositions|gsap|rendering|troubleshooting`.
- **Registro de bloques útiles:** `kinetic-type`, `cinematic-zoom`, `iris-reveal`, `blur-in`, `count-up`, `number-wheel`, `caption-editorial-emphasis`, `whip-pan-cut`, `marker-checklist-card`.

## Reglas de estructura
- **Los `<video>` van como hijos directos de la raíz.** Dentro de una subcomposición no se decodifican.
- **Footage mudo:** usa `muted` y haz la mezcla de audio en ffmpeg; así se puede medir.
- **Timelines:** una timeline pausada por composición, registrada en `window.__timelines[id]`.
- **Nada no determinista:** sin `Math.random`, `Date.now` ni `fetch`. El DOM se puede generar al cargar con datos embebidos.
- **Medios distintos:** si hay dos `<video>` con el mismo `src`, el linter avisa (`duplicate_media_discovery_risk`). Usa un archivo aparte para el PiP, con menor resolución.

## Errores del linter y bugs reales que salieron
| Problema | Arreglo |
|---|---|
| `gsap_css_transform_conflict`: `transform: scale(0)` en CSS | Usa `gsap.set(el, {scale: 0})` |
| `gsap_non_transform_motion`: animar `letterSpacing` | Usa `scaleX` o separa por caracteres |
| `font_family_without_font_face` con emoji | Declara `@font-face { font-family: "Emoji"; src: local("Segoe UI Emoji"); }` |
| `tl.set(..., 0)` no pinta el fotograma 0 | Pon el estado inicial con `gsap.set` o en CSS |
| Varios `fromTo` sobre el mismo elemento | Añade `immediateRender: false` a todos menos el primero |
| **Bug:** un hijo con `visibility: visible` sigue visible con el padre `hidden` ("inteligencia" quedó sobre la cara hasta el final) | Oculta también a los hijos al salir de la escena |
| **Bug:** un glow con `text-shadow` dentro de `overflow:hidden` se recorta en rectángulos | Pon `filter: drop-shadow()` en el contenedor |
| Texto que salta de línea y desborda la tarjeta | Usa `white-space: nowrap` y mide en el snapshot |

`npx hyperframes lint` debe dar **0 errores**. El aviso `composition_file_too_large` se puede aceptar o resolver dividiendo en subcomposiciones.

## Verificación visual (fotogramas sueltos antes de renderizar)
- `npx hyperframes snapshot --describe false --no-end --timeout 30000 --at 0.1,0.6,…`
  - **`--describe false` siempre:** si hay `GEMINI_API_KEY` configurada, sin esa opción manda los fotogramas a Gemini, lo que rompe la regla de trabajar en local.
  - `--zoom "x,y,w,h"` sirve para revisar detalles (puntuación, bordes).
- Lee `snapshots/contact-sheet*.jpg` con Read y revisa escena por escena. **Ese paso encontró 3 bugs que el linter no ve.**

## Render
- Un render normal: `npx hyperframes render -q high -f 30 -w 2 -o ../build/motion.mp4`. Tarda 4–7 min para 38 s en este equipo de 8 GB.
- **En equipos con poca RAM:** `--low-memory-mode --protocol-timeout 900000 --player-ready-timeout 180000`.
- **Si se atasca** ("capture stalled" y reintentos en bucle): detén el proceso y mata sus Chrome/node, que quedan huérfanos y comen RAM. Luego simplifica; con video alfa, usa el plan B de `color-y-recorte.md`.
- La salida va filtrada con `tail`, así que el progreso solo se ve al final. Mejor redirige a un log (`> build/render.log 2>&1`) y vigila los `@hf-progress`.
- **Si cambian los tiempos del corte** después de escribir las animaciones, no reescribas cada tiempo a mano. Envuelve `tl` con una función `T()` que remapee linealmente por tramos de clip (ver `examples/index_dia1.html` y `plan/timemap.json`). Remapea también los SFX.

## media-treatment / grade-compare
- `media-treatment --capabilities`; las claves del grading son `adjust`, `wheels`, `curves`, `hueCurves`, `secondaries`, `lut` y `details` (aquí van `vignette` y `grain`). `--grading` exige `--apply`; para validar, usa `--apply --dry-run`.
- `--analyze` solo diagnostica problemas técnicos ("no obvious imbalance"). No sabe nada de estilo.
- Para estas piezas es mejor hornear el color con ffmpeg (ver `color-y-recorte.md`).
