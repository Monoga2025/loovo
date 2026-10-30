## Corrección vigente · destacadas sin rótulo

Esta sección sustituye SOLO la composición histórica de las seis destacadas descrita abajo. Posts y captions intactos; hoja.jpg queda como referencia histórica anterior.
Motivo: el rótulo era ilegible en miniatura y redundante con el nombre mostrado por la interfaz; figuras demasiado pequeñas.
Se reutilizaron las seis seleccion.png. Sin Codex ni publicación. Anteriores conservadas intactas en borradores/portadas_con_rotulo/.
Variante reproducible: herramientas/corregir_destacadas.py (se detiene si ya existen archivos archivados).
Centro (540,960); escala uniforme sin deformación ni recorte de la fuente. Fondo carbón #0B0B0F.
Medición Pillow: diámetro del círculo centrado que contiene todos los píxeles con diferencia máxima de canal >30/255 respecto al carbón, incluyendo objetos neutros. Halos más tenues no certificados.
Las seis imágenes se reabrieron y cargaron: 1080×1920 PNG; ninguna ilustración medida toca el círculo de radio 330.

| Archivo | Diámetro visible px | Margen hasta r=330 px |
|---|---:|---:|
| destacada_01_la_serie.png | 539.96 | 60.02 |
| destacada_02_loovo.png | 540.57 | 59.72 |
| destacada_03_el_editor.png | 540.45 | 59.78 |
| destacada_04_crm_local.png | 540.63 | 59.69 |
| destacada_05_sin_humo.png | 540.24 | 59.88 |
| destacada_06_modo_demo.png | 539.64 | 60.18 |

Previsualización: destacadas/portadas/previsualizacion_circulo.png; recorte central circular 660 px reducido a 110 y 64 px lado a lado.
**Sin verificar:** recorte real de Instagram, apariencia en celular y halos bajo el umbral. Los 660 px son decisión propia, no una especificación oficial.
Detalle de tamaños, cajas y hashes de las anteriores: borradores/medidas_destacadas_sin_rotulo.json.

# Registro de composición · fase 1b

No se generaron imágenes nuevas. Solo se usaron las nueve seleccion.png existentes. Los prompts siguientes son históricos, no se ejecutaron. Archivos finales PNG de composición; la API requiere JPEG según la fuente Meta aportada por el padre.

## Fuentes y ortografía
Tres TTF locales derivadas de las WOFF2 de marca, sin instalaciones. Las WOFF2 latin no incluían →: se añadió U+2192 como contorno geométrico local en cada TTF derivada. Originales intactos. Tildes, eñe, signos y flecha comprobados en cmap y con máscaras Pillow; prueba_fuentes.png revisada visualmente sin cuadros.

## Verificación y límites
Cada PNG final se reabrió con Pillow y se cargaron sus píxeles; tamaños exactos comprobados. El texto fuente se compara carácter por carácter (incluyendo tildes, flecha y punto medio) con textos.json. Las líneas partidas se reconstruyen con el espacio original. La inspección visual complementa estas comprobaciones, no es OCR independiente. No se verificaron app, publicación, celular ni límites oficiales restantes.

## destacada_01
- Final: `destacadas/portadas/destacada_01_la_serie.png` · 1080×1920 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
La serie
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.
- Sin verificar / alcance: Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: anillo circular azul abstracto para la serie, centro libre para icono compuesto.
Formato final solicitado 1080x1920. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## destacada_02
- Final: `destacadas/portadas/destacada_02_loovo.png` · 1080×1920 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
Loovo
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.
- Sin verificar / alcance: Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: dos piezas modulares azules unidas, centro libre para icono de empresa compuesto.
Formato final solicitado 1080x1920. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## destacada_03
- Final: `destacadas/portadas/destacada_03_el_editor.png` · 1080×1920 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
El editor
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.
- Sin verificar / alcance: Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: aro azul de textura editorial inspirado en montaje audiovisual, centro libre para icono de edición.
Formato final solicitado 1080x1920. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## destacada_04
- Final: `destacadas/portadas/destacada_04_crm_local.png` · 1080×1920 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
CRM local
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.
- Sin verificar / alcance: Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: estructura modular azul abstracta que representa organización local, centro libre.
Formato final solicitado 1080x1920. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## destacada_05
- Final: `destacadas/portadas/destacada_05_sin_humo.png` · 1080×1920 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
Sin humo
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.
- Sin verificar / alcance: Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: bifurcación abstracta azul con un foco lima, centro libre para icono de reglas.
Formato final solicitado 1080x1920. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## destacada_06
- Final: `destacadas/portadas/destacada_06_modo_demo.png` · 1080×1920 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
Modo demo
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.
- Sin verificar / alcance: Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: envolvente abstracta azul protectora, centro libre para icono de modo demo.
Formato final solicitado 1080x1920. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## post_01
- Final: `posts/final/post_01.png` · 1080×1350 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
42 DÍAS
para mostrar Loovo
Día 1: 7 de octubre · Día 42: 17 de noviembre
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Recorte centrado sin deformación; foco lima del fondo pasado a azul en la copia, única palabra clave lima en titular. Texto en zona superior libre; ilustración inferior intacta en forma.
- Sin verificar / alcance: Texto cotejado carácter por carácter desde el JSON y cobertura de glifos comprobada; no se usa OCR como prueba independiente ni se ha comprobado en celular.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: anillo incompleto azul y un foco lima en la mitad inferior; mitad superior carbón completamente vacía para texto posterior.
Formato final solicitado 1080x1350. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## post_02
- Final: `posts/final/post_02.png` · 1080×1350 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
UN EDITOR CON IA
Editó el Día 1.
7 min 37 s de grabación → 38 s de video.
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Recorte centrado sin deformación; foco lima del fondo pasado a azul en la copia, única palabra clave lima en titular. Texto en zona superior libre; ilustración inferior intacta en forma.
- Sin verificar / alcance: Texto cotejado carácter por carácter desde el JSON y cobertura de glifos comprobada; no se usa OCR como prueba independiente ni se ha comprobado en celular.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: dos bloques azules de longitudes distintas en mitad inferior, sin números ni flechas; mitad superior carbón vacía.
Formato final solicitado 1080x1350. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## post_03
- Final: `posts/final/post_03.png` · 1080×1350 px · PNG reabierto con Pillow.
- Texto compuesto exacto:
```text
LOOVO YA EXISTE
Es una agencia de inteligencia artificial.
Esta serie muestra su construcción paso a paso.
```
- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.
- Composición: Recorte centrado sin deformación; foco lima del fondo pasado a azul en la copia, única palabra clave lima en titular. Texto en zona superior libre; ilustración inferior intacta en forma.
- Sin verificar / alcance: Texto cotejado carácter por carácter desde el JSON y cobertura de glifos comprobada; no se usa OCR como prueba independiente ni se ha comprobado en celular.
- Prompt histórico usado:
```text
Genera UNA imagen real con la herramienta integrada image_generation de Codex (no código, no SVG, no base64 manual, no otro proveedor). No delegues, no publiques, no inicies sesión ni navegues cuentas. Es una ilustración abstracta para Monoga/Loovo, no evidencia de productos ni resultados.
Marca Eléctrico: carbón #0B0B0F, azul #2F5BFF, un único foco lima #C6FF3D y hueso #F4F2EE. NADA rojo. Sin personas, rostros, manos, logos, pantallas, facturas, números, letras, texto, marcas de agua ni tipografía.
Tema: un nodo azul conectado a pequeñas formas azules, un foco lima; toda la ilustración en mitad inferior, mitad superior carbón vacía.
Formato final solicitado 1080x1350. Si el generador entrega otro tamaño, conserva original; el padre lo ajusta después con Pillow. Composición limpia, editorial, mucho vacío. Si es destacada, icono/objeto abstracto enteramente dentro del círculo centrado en el lienzo (50%,50%), diámetro 60% del ancho.
Usa exclusivamente image_generation. Si no está disponible o falla, informa el error exacto y detente; no simules imágenes con código ni uses servicios alternativos. Los archivos generados quedan en ~/.codex/generated_images/<session-id>/. Puedes copiar la imagen final a fondo.png dentro de esta carpeta de trabajo. No escribas fuera de esta carpeta salvo el almacenamiento automático de generated_images. No instales nada, no leas datos del usuario ni credenciales.
```

## Revisión visual de cierre
Hoja revisada: seis nombres correctos bajo las figuras, tres posts sin superposición sobre ilustraciones. Post 1 leído completo antes del ajuste suave de color y luego en la hoja; posts 2 y 3 también leídos completos. Texto y glifos coinciden con el JSON. Círculo geométrico comprobado para cajas de texto e ilustración cromática; no para halo tenue ni recorte de la app. Pendientes: caption Día 3, aprobación editorial evento/rol y prueba en celular. Engram no disponible por binario antiguo.

## Verificación final de la corrección
Revisión visual de previsualizacion_circulo.png completada: seis figuras completas y centradas, sin rótulos dentro de los círculos, sin recortes visibles a 110 y 64 px. Sin humo conserva trazos finos de contraste menor a 64 px; las figuras anulares son parecidas entre sí. Reapertura independiente con Pillow: seis tamaños y radios válidos; hashes de las seis versiones archivadas coinciden. Halos con diferencia de canal ≤30/255, recorte real de Instagram y celular no verificados. Sin Codex, posts, captions ni publicación. Risk: none (solo composición local reversible).

## Sustitución exclusiva Sin humo · 05b
- Una imagen nueva vía herramientas/puente_codex.py, método original codex exec; ejecución en segundo plano, sin alternativa. Prompt e invocación: destacada_05b/prompt.txt e invocacion.json; logs en esa carpeta.
- Brief: reglas, no IA; bloques azules 3D sólidos y gruesos (mínimo solicitado 6% del diámetro), UN punto lima, carbón liso, sin texto/números/personas/filigrana. Figura solicitada ~60% del alto en fuente.
- Final: destacadas/portadas/destacada_05_sin_humo.png; 1080×1920, sin rótulo, centro (540,960), diámetro medido 539.39 px. Afinidad uniforme y armonización neutra de componer.py; medición completa de corregir_destacadas.py.
- Filigrana anterior intacta: borradores/portadas_con_rotulo/destacada_05_filigrana.png (hash coincide). Otras cinco portadas intactas por SHA-256.
- Previsualización de seis portadas regenerada a 110 y 64 px. Medidas, umbral y hashes: destacada_05b/medidas.json. Pendiente lectura visual.
- Sin verificar: recorte real de Instagram, celular, halos bajo umbral y grosor mínimo exacto en proyección 3D. Sin posts, captions ni publicación.

- Sin humo 05b cierre: previsualización abierta y revisada a 110 y 64 px; bloques sólidos azules y un punto lima claramente distinguibles, sin filigrana ni rótulo. No se ve débil a 64 px. Reapertura Pillow independiente: 1080×1920, diámetro visible 539,39 px centrado (540,960); otras cinco portadas y filigrana archivada intactas por SHA-256. REGISTRO.md y medidas.json actualizados. No verificados: app/celular, halos bajo umbral y grosor mínimo exacto de proyección 3D; fuente ocupa aprox. 52% del alto por bbox visible, no el ~60% pedido al generador; final cumple diámetro solicitado. Engram no disponible (binario antiguo). Advertencia auxiliar de Codex: Failed to create unified exec process: helper_unknown_error: setup refresh had errors; no impidió obtener el PNG generado. Sin publicaciones, posts, captions ni cambios a otras portadas. Risk: none (composición local reversible).
