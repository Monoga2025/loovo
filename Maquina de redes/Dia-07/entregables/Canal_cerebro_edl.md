# Canal · Le hice un cerebro a mi empresa · EDL

Crudo (solo lectura, no se movió): C:/Users/you/Desktop/VID_20261013_110529.mp4 (celular, rotación -90 → 1080x1920, 30 fps).
Línea final 52.43 s, 9:16 1080x1920, 30 fps, H.264 CRF 18 + AAC 320k 48 kHz.
Audio: solo el del celular (ese día no hubo mic del PC): HPF 70 Hz + afftdn 6 dB + compresor 2:1, fundidos 12 ms; voz a -17,6 LUFS; música bajo la voz con ducking.

| Tramo | Línea final (s) | Crudo (s) | Imagen | Texto |
|---|---|---|---|---|
| H1 | 0.00–2.42 | 753.62–756.04 | motion | Vamos a hacer una base de conocimientos en NotebookLM, |
| H2 | 2.54–5.45 | 757.06–759.97 | motion | que es básicamente el cerebro de mi empresa. |
| C1 | 5.90–10.47 | 731.95–736.52 | pantalla (B-roll 2.5D) · imagen desde 745.00 | Algo bien interesante fue entrar a la carpeta donde tengo absolutamente todo |
| C2a | 10.77–13.00 | 743.57–745.80 | motion | y le dije al agente que hiciera un resumen de todo |
| C2b | 13.30–17.90 | 746.84–751.44 | motion | y me lo entregara en un formato .md para enviárselo a NotebookLM. |
| C3 | 18.30–21.77 | 821.03–824.50 | pantalla (B-roll 2.5D) · imagen desde 822.20 | Subimos los cinco elementos y ya estamos creando nuestro primer cerebro. |
| C4 | 22.12–23.81 | 896.46–898.15 | motion | Es demasiada información. |
| C5 | 23.96–27.31 | 915.87–919.22 | motion | Esto es un agente de RAG, donde tenemos un montón de información. |
| C6 | 27.71–30.25 | 930.33–932.87 | pantalla (B-roll 2.5D) · imagen desde 937.90 | Lo importante es que desde acá |
| C7 | 30.30–35.79 | 935.17–940.66 | motion | vamos a tener un mapa mental de la empresa, vamos a poder crear infografías y una tabla de datos. |
| C8 | 36.24–37.42 | 946.30–947.48 | motion | Volvemos y preguntamos: |
| C9 | 37.62–38.72 | 950.42–951.52 | motion | ¿qué servicios vendemos? |
| C10 | 39.27–40.49 | 978.09–979.31 | pantalla (B-roll 2.5D) · imagen desde 978.00 | Perfecto, aquí está. |
| C11 | 40.59–43.56 | 979.85–982.82 | motion | Servicios empaquetados en documentación de venta, |
| C12 | 43.71–45.17 | 990.20–991.66 | motion | soluciones web y pilotos de inteligencia artificial. |
| C13 | 45.62–49.28 | 1013.84–1017.50 | motion | Ya desde acá tenemos una base de datos de toda nuestra empresa. |
| PL | 49.63–52.43 | — | placa | (placa LOOVO) |

Invert flash + glitch Mixkit 1022 en: 5.70 s, 39.07 s.

## Desenfoques de privacidad
- Crudo 976.0–981.5 s, zona [0, 360, 1080, 1460] (px del crudo 1080x1920): respuesta de NotebookLM: nombres de terceros, clientes y montos. Pixelado 1/28 + gauss 18 px.

## Cortes y decisiones
- Cortado: "Entonces" (inicio del gancho), "para hacer toda la información" (después de "mi empresa"), "que es esta... acá donde tengo absolutamente todo" (repetición), 1 s de silencio dentro de "un resumen de todo / y me lo entregara", "para la inicial" (whisper), "por eso estamos utilizando NotebookLM y es lo mejor para organizar mucha información" y "eso básicamente es un..." (para que quepa en 52 s), "vamos a poder organizar muchísima información" y "que es lo más importante" (repetía "importante"), todo el tramo de espera ("responde súper rápido... 10 segundos"), y en la respuesta: "páginas web, tarjetas físicas, hospedaje, botonero, mantenimiento" (audio confuso), el ERP de un tercero, "proyecto de la universidad" y "un proyecto de Estados Unidos donde estamos vendiendo unas ciclas" (datos de terceros / no están en hechos.md).
- Subtítulo: whisper oye "le dije a una gente que performe hiciera"; se puso "le dije al agente que hiciera" (brief: "una gente" = "el agente"; "performe" no se entiende y se omitió en el texto).
- Servicios: se presentan como "lo que encontró en mis documentos" (etiqueta), solo los que él dice claro: "servicios empaquetados en documentación de venta, soluciones web y pilotos de inteligencia artificial". No se afirma que Loovo los venda (no está en hechos.md).
- En esta zona del crudo no mira a cámara: no hay planos de persona; todo es pantalla 2.5D + motion.

## Escenas
Gancho ("cerebro" ya visible en el cuadro 0, red de 6 nodos que se conectan, pulso + partículas en "cerebro") · invert flash → carpeta (explorador de Monoga OS, panel 2.5D) · rejilla de 16 archivos que escanea una línea dorada → se comprimen en "resumen.md" → baja a NotebookLM · pantalla: 5 fuentes subiendo + contador 0→5 · lluvia de 42 hojas "demasiada información" → se ordenan → caja RAG + Pregunta / Busca en tus docs / Responde · pantalla: Studio de NotebookLM (panel 2.5D) · Mapa mental / Infografías / Tabla de datos + mapa mental que se dibuja · caja de pregunta con tecleo "¿Qué servicios vendemos?" · invert flash → respuesta desenfocada · "lo que encontró en mis documentos" · cerebro central con 8 fuentes orbitando → caja "empresa" · destello → placa LOOVO / el cerebro de mi empresa / #Loovo.

## Privacidad (revisado cuadro a cuadro en los planos de pantalla)
- Explorador de Monoga OS (carpetas propias), fuentes de NotebookLM (nombres de archivos propios), Studio de NotebookLM: sin claves ni datos de terceros.
- Respuesta de NotebookLM (crudo 976–981,5 s): menciona nombres de personas, clientes y montos → desenfoque fuerte de todo el cuerpo de la respuesta; solo queda legible la pregunta.
- 27,48–27,72 s de la línea final: en la transición asomaba la lista de fuentes con el resumen del cuaderno (crudo ~919 s) → desenfocado en post (plan/postblur.json). En el proyecto, base.py ya arranca cada plano en la pausa previa; el render final se hizo antes de ese cambio y un segundo render falló por falta de RAM, por eso se tapó en post.
- No hay persona en cámara en este video (solo su voz).

## Licencias
- Música: "Sci-Fi Score" (Mixkit 464, Arulo), Mixkit Stock Music Free License: redes sociales y YouTube, uso comercial, sin atribución; prohíbe TV/radio, CD/DVD, videojuegos, remezclarla o registrarla en Content ID. Texto en LICENCIA_musica.txt.
- Glitch: Mixkit SFX 1022, Mixkit Sound Effects Free License (heredado del Día 4; la página individual no abrió: verificar en el listado antes de publicar).
- Resto de SFX: sintetizados por código. Íconos: Phosphor (MIT). Fuentes: Montserrat y Playfair Display (OFL). Pantallas: grabadas por el usuario en el crudo.
