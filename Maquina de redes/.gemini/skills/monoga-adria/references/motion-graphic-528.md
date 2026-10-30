# Motion graphic estilo Adrià 5:28 + salida "invert flash" (probado en el Día 4, 55,1–60,2 s)

Referencia medida: Adrià 5:26–5:38 (25 fps). Su escena es oscura/azul/roja; aquí va en la paleta Loovo.

## Entrada (persona -> gráfico)
1. Últimos 4 cuadros de la persona: **zoom-out con desenfoque radial** (escala relativa 0,98 / 0,94 / 0,88 / 0,78; Adrià 0,98/0,94/0,88/0,76).
   Se hornea en la base: `make_base.py`, diccionario `RADIAL = {"TRAMO": [0.98, 0.94, 0.88, 0.78]}` (promedio de 12 copias escaladas, BORDER_REPLICATE).
2. Whoosh corto que sube y se corta seco en el corte (`swish` en `sfx.py`, inicio = corte - 0,5 s).
3. **Corte duro** al gráfico, que entra **a escala 4 con blur 18 px y aterriza a 1,05 con `expo.out` en 0,5 s** (sin rebote). Luego deriva lenta a 1,0 con `sine.inOut` y parallax: fondo de puntos se mueve poco, objetos más.

## Escena (paleta Loovo)
- Fondo: blanco pastel con puntos. Objetos: cajas cuadradas carbón `#2A2926` con icono crema `#E6D6AE`, o crema `#FBF8F1` con icono carbón (iconos Phosphor por `mask-image`). Sombras difusas. Sin bordes redondos.
- Texto arriba a la izquierda, Montserrat 600 84 px carbón, **palabra por palabra** (blur 10 px + subida 20 px, 4 cuadros, onset de voz - 2 cuadros). Repeticiones de muletilla en gris `#8C887F`.
- Cada palabra repetida ("creo, creo…") hace aparecer un objeto (escala 0,6 -> 1, blur, 7 cuadros `power3.out`) = sincronía visual con la voz.
- **Palabra clave en caja carbón con cursor dorado:** cursor `#C8B07A` 12 px aparece 6 cuadros antes; la caja crece de 0 a su ancho en 5 cuadros (`power3.out`) mientras el cursor viaja; el texto (140 px, dorado claro `#E6D6AE`) se revela de izquierda a derecha con `clip-path` en 5 cuadros. Fija hasta la salida (≥0,5 s).
- Plantilla: `references/plantilla_dia4.tpl.html`, bloque "motion graphic".

## Salida: invert flash (lo que el usuario llamó "el efecto que usan casi todos los influencers con ese sonido")
Hecho en post sobre el render (`scripts/post_fx.py`), 8 cuadros a 30 fps (Adrià: 7 a 25 fps, con retenciones de 2 cuadros):
| cuadro vs corte | qué |
|---|---|
| -3, -2 | entra por abajo-derecha un borde diagonal (~20°) con el gráfico en negativo sobreexpuesto |
| -1 (pico) | casi todo el cuadro en negativo + destello blanco 45 %; queda una cuña abajo-izquierda |
| 0 | ya es la persona; arriba aún negativa (borde "\") |
| +1, +2 | triángulo arriba-derecha en negativo |
| +3 | rebote: mitad superior negativa un cuadro |
| +4 | limpio |
- El HTML oculta el gráfico en el cuadro 0 (`CUT = inicio del tramo + 3 cuadros`); el tramo de persona empieza con ~0,25 s de silencio para que la voz entre después del flash.
- **SFX:** glitch/estática de banda ancha 0,27–0,30 s que empieza en el cuadro del pico. Archivo: `assets/sfx_mixkit_1022_trim.wav` (Mixkit "Cinematic sci fi glitch", id 1022, Mixkit Free License: uso comercial sin atribución; ver `assets/LICENCIA_sfx.txt`), remuestreado a 48 kHz, recortado a 0,30 s con fundido de 0,1 s. Alternativa sin licencia: `assets/sfx_efecto.wav` (sintetizado; menos grave).
- Máximo 2 invert flash por video. Al invertir, el dorado se vuelve azul 1–2 cuadros: es el efecto, aceptado.
- **Por probar:** versión con el clip de persona ANTES del gráfico (invert de entrada); glitch cromático RGB en el pico.
