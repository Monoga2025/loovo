# Marca IA MONOGA · dirección A "Eléctrico"

Elegida por el usuario el 2026-10-08 entre tres propuestas (`propuestas/propuestas_ABC.png`). Datos de máquina en `marca.json`.

## Por qué así
- **Nada de rojo.** El usuario lo asocia con peligro.
- **No un solo color.** Dos acentos con roles distintos, más neutros.
- Al ver un video en el feed, la lima sobre carbón con el azul eléctrico debe decir "eso es IA MONOGA".

## Colores y su trabajo
| Color | Hex | Uso |
|---|---|---|
| Carbón | `#0B0B0F` | Fondos de escena, texto sobre lima |
| Azul eléctrico | `#2F5BFF` | Estructura: bordes, chips, líneas de conexión, barras, anillos |
| Lima ácido | `#C6FF3D` | **El foco.** La palabra clave, el dato, el punto que viaja. Máximo un elemento lima importante a la vez |
| Hueso | `#F4F2EE` | Texto secundario, fondos claros, palabras grandes detrás |
| Gris | `#8C8C99` | Texto terciario |

## Tipografía (archivos en `fonts/`, licencia OFL)
- **Space Grotesk 700**: palabra clave, titulares, palabras detrás de la persona. Tracking -0,05 em. En los subtítulos va en mayúsculas, carbón sobre una caja lima.
- **Instrument Serif cursiva**: conectores y frases de apoyo ("hoy es el", "no hace", "de la plataforma").
- **Space Grotesk 500**: textos de interfaz (filas, etiquetas).
- La mezcla serif cursiva fina + grotesca pesada es la firma.

## Elementos de firma
1. **Texto detrás de la persona**: palabra gigante en Space Grotesk sobre la pared, la cabeza tapa la parte de abajo. En lima, hueso, azul o solo contorno. Solo palabras que el usuario dice.
2. **Caja lima** en la palabra clave del subtítulo, con una leve rotación de -2°.
3. **El foco**: un punto lima con anillo azul que vive arriba a la derecha (935, 312) y entra en cada escena (cabezal del editor, punta de una barra, notificación, nodo, check). Se apaga al final para cerrar en bucle.
4. **Mosaicos de icono**: cuadrado redondeado lima con icono carbón y anillo azul, o carbón con icono lima. Iconos Phosphor (MIT).
5. **Escenas**: carbón con retícula azul de 90 px, aura azul y lima difusa y grano; o hueso con retícula carbón. Entran girando en 3D o con zoom.
6. **Fotos en duotono** (carbón → azul → lima) de la biblioteca `00_Serie/recursos/`.

## Biblioteca de recursos
`00_Serie/recursos/manifest.json` lista cada recurso con su fuente y licencia. Se amplía con `monoga-editor/scripts/recursos_pd.py` (descarga solo dominio público o CC0) y `recursos_proc.py` (recorte, duotono de marca, iconos, texturas, formas).

## Pendiente
- Logo o monograma de IA MONOGA (por ahora el nombre en Space Grotesk 700 con un punto lima).
- Portada con la nueva marca (la del Día 2 se hizo antes).
- Objetos 3D propios de la marca (generados con Codex y recortados) cuando el usuario apruebe el gasto de tokens.
