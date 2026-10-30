# Estilo visual que funcionó (y lo que el usuario rechazó)

## Rechazado ("la tipografía qué mierda", "esos zoom no son nada que ver")
- Subtítulos ASS en Arial Black/Impact en MAYÚSCULAS, con contorno grueso y palabra activa amarilla. Se ven baratos.
- Zoom en escalón fijo (plano normal / 1,12× alternos en cada corte).
- Gancho en texto como bloque estático de 3 líneas arriba.
- Color "igualado" con tinte cálido, curva S, grano y viñeta fuerte: "se ve re falso".
- **Lección:** pide un video de referencia ANTES de diseñar (sección Brief del SKILL). Con referencia, el usuario quedó encantado al primer intento.

## Aprobado: lenguaje tomado de la referencia del usuario
Analiza la referencia con `ffmpeg -vf "fps=2,scale=180:-1,tile=9x4"` y lee la hoja con Read.
- **Paleta:** crema `#F2EEE8` con retícula sutil de 72 px (alfa 0,035), negro `#070707` con resplandor radial rojo, rojo `#E3120B` como único acento, texto oscuro `#141414` y gris `#8A8784`.
- **Tipografía:** Inter (Google Fonts, cacheada por HyperFrames), tracking -0,03 a -0,055 em. Las palabras pequeñas van neutras (500–700) y la **palabra clave grande en rojo** (900), a veces con glow (`text-shadow` rojo).
- **Subtítulos cinéticos** (template `graphics.html` + `make_caps.py`):
  - frases de 2–4 palabras sobre el pecho, `top: 1170px`;
  - cada palabra entra con blur-in (y 26 → 0, blur 14 → 0, 0,24 s);
  - la palabra clave entra con pop (escala 1,45 → 1, `back.out(2)`), en rojo y a 104 px;
  - texto oscuro con halo blanco para leerse sobre ropa o pared;
  - la frase sale hacia arriba con blur;
  - en minúsculas, como se habla.
- **Zoom de tendencia** (helpers en `templates/hyperframes/index.html`):
  - push lento y continuo en cada plano (1,0 → 1,06–1,10, `ease: none`);
  - punch-in con `expo.out` en la palabra clave (1,15–1,28);
  - zoom látigo de salida con blur 16 px (`power3.in`, 0,22 s) antes de una escena FS;
  - aterrizaje con zoom-out desde 1,3–1,4 y blur al volver al video;
  - temblor de 6 pasos de 40 ms en los impactos.

## Catálogo de escenas FS (ejemplo completo: `templates/hyperframes/examples/graphics_dia1.html`)
| Técnica | Cuándo | Detalle |
|---|---|---|
| Odómetro de dígitos | números ("42 días") | tiras de dígitos en columnas con `overflow:hidden` que se trasladan en `y`; glow con `drop-shadow` en el contenedor |
| Iris | entrada/salida de escena | `clipPath: circle(150%→0% at 50% 42%)` revela el video debajo |
| Arco SVG que se dibuja | "lejos de…", recorridos | `pathLength="1"` + `strokeDashoffset 1→0` |
| Retícula que se ensambla | "montamos", "construimos" | 70 celdas, `stagger { from: "center", grid }` |
| Círculo rojo de transición | cambiar de negro a crema | escala 0→1 y luego 1→0 con la escena nueva debajo |
| Tarjeta con chincheta | listas ("vas a ver…") | cae con `back.out`, se balancea con `sine`, ítems con blur-in sincronizados; el último en píldora roja con temblor |
| Scramble | palabras técnicas ("inteligencia") | 6 spans prehechos que se alternan cada 0,06 s; nada de `Math.random` |
| Escalones | "paso a paso" | `scaleY 0→1` desde abajo, con SFX de tono ascendente |
| Segmentos 1/N | progreso ("día 1 de 42") | N celdas en cascada y la primera se llena de rojo |
| Cierre en iris a negro | final en loop con el inicio negro | círculo con `box-shadow: 0 0 0 3000px #070707` que se encoge |

## Motion sobre el video mientras habla (template `overlays.html`)
- **Stickers:** emoji en un círculo blanco con aro rojo, más un aro expansivo. Ejemplos: 🚫 "no se hace", 🎯 "meta", 🏆 "mejores".
- **Chips:** píldora blanca con emoji y texto literal ("ya existe", "hoy", "evento", "Día 1 / 42").
- **Otros:** signos "?" rojos en "ni idea", destellos ✦, barras de glitch RGB breves y una trayectoria SVG discontinua con punto final.
- **Posición:** a los lados de la cara (x < 330 o x > 750), nunca sobre ojos o boca, y fuera de la franja de subtítulos.

## Palabras gigantes detrás del hablante
Ver `color-y-recorte.md`.

## Ritmo
- Una idea nueva cada 1,5–2 s en las escenas FS y un SFX por golpe.
- Ningún plano de cabeza hablando dura más de 5 s sin un zoom, un overlay o una palabra de fondo.
- Un PiP circular en escenas FS de más de 4 s (regla de la skill). La referencia no lo usa: ofrece quitarlo.
