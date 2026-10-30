# Motion nivel pro: lo que pidió el usuario después del Día 2

El usuario dijo: "solo diciéndote que seas experto en motion ya deberías crear cosas increíbles: transiciones 3D, objetos 3D que apoyen todo lo que digo, cortes geniales, emojis o imágenes de apoyo". Y dejó un video de referencia (`Dia-02/proyecto/ref/ref_estilo.mp4`, hoja en `ref/contact_a.png`).

**Regla nueva:** no esperes a que lo pida. Un video de la serie sale con objetos de apoyo, transiciones 3D y cortes con efecto desde la primera versión. Un video con solo subtítulos y zooms es un borrador.

## Qué tiene la referencia (analizado con hoja de contactos)
- Paleta negro / blanco / rojo. Fondos que alternan negro y gris claro con retícula.
- **Objetos recortados con sombra** en vez de texto solo: billetes que flotan, teléfonos con pantalla real, una estatua tintada de rojo, tarjetas con brillo. Cada idea hablada tiene su objeto.
- Tipografía mezclada: palabra clave pesada y en rojo, palabras de apoyo en cursiva fina ("You *run*", "Ads *bring* Attention").
- Líneas y arcos finos que se dibujan, números grandes (#1, #2…), cursores de mano.
- Movimiento constante: ningún plano estático más de 1,5 s.

## Kit que ya funciona (Día 2)
1. **Emojis 3D (Fluent Emoji 3D, MIT, Microsoft).** PNG con alfa y aspecto 3D real.
   - Fuente: `npm:@lobehub/fluent-emoji-3d@1.1.0`, archivos `assets/<codepoint>.webp` en jsdelivr (`https://cdn.jsdelivr.net/npm/@lobehub/fluent-emoji-3d@1.1.0/assets/1f916.webp`). El código es el del emoji en minúsculas (con `-fe0f` si lo trae; guarda sin él).
   - Descárgalos a una carpeta aparte (`Dia-XX/_dl_emoji`), conviértelos con ffmpeg (`-vf scale=512:512:force_original_aspect_ratio=decrease`) a `motion/assets/emoji/<codigo>.png`. PIL no está disponible con `python -I`.
   - Códigos usados: 1f4b8 💸, 23f0 ⏰, 1f634 😴, 1f4a4 💤, 1f916 🤖, 1f9e0 🧠, 1f3ac 🎬, 23f1 ⏱, 1f525 🔥, 1f4bc 💼, 1f4ac 💬, 1f50c 🔌, 1f9fe 🧾, 1f4c5 📅, 26d3 ⛓, 1f319 🌙, 1f4bb 💻, 1f4a1 💡, 1f3af 🎯, 1f4a5 💥, 1f608 😈, 2728 ✨, 1f464 👤, 2709 ✉, 1f50d 🔍, 1f9ed 🧭. Hay 3.393 en total.
2. **Stickers sobre la cabeza hablando** (`templates/hyperframes/compositions/overlays.html`, ejemplo en `examples/`): uno por idea, entrada con giro 3D (`rotationY -170 → 0`, `transformPerspective: 700`, pop con `back.out`), flotación y salida con giro. Con `drop-shadow` y un resplandor rojo leve.
   - **Colócalos siempre del lado donde NO está la cabeza.** En el Día 2 el usuario se sienta a la derecha: con zoom 1,2 la cabeza ocupa x 470–945. Los stickers de la derecha taparon el pelo; todos pasaron a la izquierda (x 62, 210 px). Mide la posición de la cabeza en un fotograma antes de decidir el lado.
   - Si hay dos a la vez, apílalos (y 360 y 640), no los pongas lado a lado.
3. **Transiciones 3D de escena** (en `graphics.html`):
   - `flipIn`: la escena crema entra girando desde el borde izquierdo (`rotationY -85 → 0`, `transformPerspective: 1400`, `transformOrigin: 0% 50%`). `flipOut`: sale girando hacia el borde derecho.
   - Escenas oscuras: entran con `scale 1.3 → 1` y salen en iris.
   - Ventana y tarjeta con inclinación 3D (`rotationX`, `rotationY`) y un balanceo lento.
4. **Cortes con efecto** (`cutfx` en `index.html`): en cada corte entre tomas, rotando: glitch (blur + brillo + `x` con `steps(4)`), látigo lateral (`x 120 → 0` con blur 16) y destello (`brightness 2.4 → 1`). Van sin escala para no chocar con los zooms. Con un `swish` de SFX en cada corte.
5. **Cortes exactos:** calcula las marcas de cada toma con la misma lógica de `build_cut.py` (bordes a fotograma) y guárdalas en `plan/cut_times.json`. Los `reset` de zoom y los efectos van en esos tiempos, no en estimaciones: un `reset` mal puesto produce un salto a mitad de plano.
6. **Emojis 3D dentro de las escenas FS:** un objeto grande que gira (`spin`, `rotationY +=360`) en la escena del empleado, un reloj que se balancea junto a "7 minutos", un enchufe en "conectado", iconos en cada fila de la tarjeta.

## Qué falta (para llegar a la referencia)
- **Pantalla real del producto** dentro de un teléfono o portátil 3D (el CRM, un editor de video). Requiere datos seguros: nunca clientes reales. Ver abajo.
- **Objetos fotorrealistas recortados** (estatua, billetes, teléfono): generar con Codex y recortar con rembg (`segment.py`/u2net local), como las portadas.
- ~~Three.js~~ **Resuelto en la ronda 7:** objetos 3D reales con luz funcionan en HyperFrames. Receta T10 en `tecnicas-referencias.md` y ejemplo `examples/objeto3d_threejs.html`.
- **Tipografía mezclada** (cursiva fina + pesada roja) en los subtítulos.

## Grabar el CRM para el video
- El CRM es de otro repositorio y no se modifica. Se enciende como `Desktop\CRM.bat` (Postgres, API en 3101, app en 3000). La herramienta de Chrome del usuario no cargó las páginas locales; se usó el Chrome headless de HyperFrames con `playwright-core` (hay una copia en `Desktop/Tutor Mecatronica/node_modules`): `executablePath` = `~/.cache/hyperframes/chrome/chrome-headless-shell/.../chrome-headless-shell.exe`, viewport 1440×900, entrar por `http://localhost:3000/api/dev-login`.
- **Antes de grabar, confirmar con el usuario que la base es de demostración.** El clasificador de permisos bloqueó volcar el texto de contactos y empresas: pueden ser clientes reales. El panel principal muestra cifras reales (por ejemplo "1 trato ganado $1,2 M"): no publicarlas sin permiso.
- Mostrar el chat del agente solo cuando `hechos.md` lo marque ✅.


## Actualización (Día 2, ronda 5): recursos reales en vez de emojis, tipografía y motivo

El usuario dijo que los emojis "hacen que se vea barato". Reemplazados por:
- **Iconos vectoriales Phosphor (MIT)** vía Iconify: `https://api.iconify.design/ph/<nombre>.svg?color=%23e3120b&height=256` (rojo) y `%23ffffff` (blanco). Se guardan en `motion/assets/ico/<nombre>_r.svg`. Nombres usados: robot-fill, brain-fill, alarm-fill, calendar-check-fill, calendar-star-fill, film-slate-fill, fire-fill, moon-stars-fill, bed-fill, lightning-fill, sun-fill, address-book-fill, cpu-fill, chat-circle-dots-fill, plugs-connected-fill, lightbulb-fill, chats-circle-fill, link-fill, timer-fill, sparkle-fill, receipt-fill, currency-dollar-fill, prohibit-fill, user-fill, envelope-simple-fill, magnifying-glass-fill, compass-fill, chats-fill. Otros sets: Tabler (MIT), Lucide (ISC), Iconoir (MIT), MingCute (Apache 2.0); Solar y Streamline son CC BY 4.0 (exigen atribución).
- **Mosaico**: cuadrado redondeado blanco con borde rojo de 4 px, resplandor rojo e icono rojo al 58 %. Es el lenguaje de las tarjetas de la referencia.
- **Billete real tintado**: foto de dominio público de Wikimedia Commons (`File:1957 one United States dollar star note.jpg`, "Public domain"; consulta la licencia por la API `prop=imageinfo&iiprop=extmetadata`). Se tiñe con `colorchannelmixer=rr=0.24:rg=0.48:rb=0.09:gr=0.03:gg=0.07:gb=0.015:br=0.03:bg=0.06:bb=0.01,eq=contrast=1.15` para el rojo oscuro de la referencia. Para otros objetos: Cleveland Museum of Art Open Access (CC0, API `openaccess-api.clevelandart.org/api/artworks/?cc0=1&has_image=1`), Openverse con `license=cc0,pdm`. La API del Met devolvió 410.
- **Tipografía de la referencia**: conectores en Montserrat 300 cursiva (`.tl`) y palabra clave en **Anton** mayúsculas con oblicua sintética (`.th`, `font-style: italic`). Anton no está en la lista automática del renderizador: hay que bajar el woff2 (`https://cdn.jsdelivr.net/npm/@fontsource/anton@5/files/anton-latin-400-normal.woff2` y `anton-latin-ext-400-normal.woff2`, OFL), guardarlo en `motion/assets/fonts/` y declarar `@font-face` **dentro de cada composición** que lo use; no pongas `Impact` en la pila de fuentes (el linter lo marca). Un `.th` pegado a un `.tl` en la misma línea se ve bien; el acento de "DÍA" choca con la línea de arriba: sepáralas 120 px.
- **Motivo recurrente: un punto rojo que viaja por todas las escenas** (idea tomada del análisis de iart.ai: "a red dot carries through every scene"). Vive en la esquina superior derecha (935, 312, dentro de la zona segura), late con cada palabra clave, aterriza en la primera casilla de "42", baja por la flecha de "7 minutos a 38", queda como notificación sobre el chat, recorre la retícula en "conectado", se posa en la chincheta de la tarjeta, avisa en el recibo de la DIAN, y se apaga al final para que el video cierre en bucle.

### Qué dicen los recursos que pasó el usuario (claudevideo.org, motionpromptgallery.com, iart.ai)
- Un buen brief fija **escenas, tiempos, color y texto exacto**; con **referencias** el resultado mejora mucho; casi nunca sale en una pasada: se dirige como un editor en varias rondas de notas.
- Prompt eficaz: duración y formato, **una sola idea central**, texto y cifras exactos, **dirección emocional**, y libertad creativa en la estética. El usuario lo resume: "si le pones más cosas al prompt lo limitas".
- Técnicas: tipografía cinética (una palabra por pulso), morfosis de elementos de UI, datos que se animan al aparecer, **un motivo que cruza todas las escenas**, formas que cambian en el tiempo fuerte, órbitas inclinadas para dar profundidad, **bucle perfecto** (el último fotograma encaja con el primero), audio sintetizado por código sincronizado al movimiento (128 bpm showreel, 120 bpm tipografía).
- Pendiente de probar: motor de proyección 3D propio sobre canvas (pack `iart-ai/javascript-animation-skills`) y música generada al compás de los cortes.


## Ronda 6 (Día 2 v10, con Opus): identidad de marca y biblioteca
- **El rojo y el estilo de la referencia quedaron atrás.** Ahora manda la marca IA MONOGA (`00_Serie/marca/`). La referencia sirve para el ritmo y la ambición, no para la paleta.
- **Biblioteca** `00_Serie/recursos/`: 41 iconos Phosphor (`iconos/`, sin color fijo: se pintan con CSS mask `background: currentColor; mask: var(--i)`), 7 fotos con licencia verificada (celular y portátil recortados con pantalla en blanco para meter interfaces; billete, cohete, satélite, servidores y Tierra de noche en duotono de marca), 3 texturas (grano, semitono, aura) y 6 formas (flecha, subrayado, esquinas, destello, rayo, círculo a mano). Fuentes que sirvieron: Openverse con `license=cc0,pdm` (rawpixel tiene objetos aislados), NASA Images (dominio público), Wikimedia Commons (cuidado: devuelve 429 si se consulta rápido). Smithsonian y Met no sirvieron.
- **Ojo con las rutas en `url()` dentro de variables CSS** de un `style` en línea: se resuelven contra `index.html`, así que van como `assets/ico/x.svg`, no `../assets/...`.
- **Escenas nuevas que funcionaron**: editor de video con pistas y cabezal (para "edita los videos"); barra proporcional real que se encoge de 457 s a 38 s; celular recortado con una interfaz en su pantalla, inclinado en 3D; red de nodos con la IA al centro y líneas que se dibujan ("conectado por dentro"); filas que suben en 3D con check lima ("puede leer…"); factura oscura inclinada para la DIAN.
- **El foco lima** (antes punto rojo) recorre esos elementos: cabezal, punta de la barra, notificación, nodos, checks, total de la factura.
- **Texto detrás**: con alfa en Chrome (`person.webm`, vp9 `yuva420p`) el render funcionó directo en este equipo; si se atasca, plan B (`make_variants.py` + `composite_behind.py`).
- **Pinterest** (con el Chrome del usuario) sirvió para tendencias: texto detrás en condensadas gigantes, contorno, paletas negro + lima/violeta/azul. Solo como inspiración: las imágenes de Pinterest no tienen licencia para usarlas en el video.
