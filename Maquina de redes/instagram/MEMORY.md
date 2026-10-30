# Memoria del módulo Instagram

- 2026-10-23: módulo creado a pedido de Monoga. Objetivo: republicar lo de TikTok en Instagram, armar destacadas y generar publicaciones con imágenes de IA vía Codex.
- Falta el usuario de TikTok y el de Instagram de Monoga: no están en el repositorio (los usuarios que aparecen en `00_Serie/` son de otros creadores). Sin ellos no se puede confirmar qué hay publicado.
- `00_Serie/marcador.md` no registra ningún día como publicado. `hechos.md` tiene «Publicado el Día 1 en TikTok e Instagram» como ❓.
- Marca vigente: «Eléctrico» (sin rojo). La portada del Día 1 con rojo es anterior.
- Existen exportaciones `*_Reels.mp4` en `Dia-01`, `Dia-02` y `Dia-03`.
- Fuentes de marca originales en WOFF2: para Pillow se convierten con fontTools/brotli a TTF dentro de `herramientas/fuentes/`, sin instalar ni tocar originales. La cobertura se comprueba con cmap y máscaras, no solo abriendo la fuente. Las tres variantes latin carecen de → (U+2192): los derivados locales añaden un contorno geométrico para ese signo; las tildes y la eñe ya están cubiertas. Reproducible con `python herramientas/fase1b.py fonts`.
- Una sola llamada bash prolongada puede detener al agente. Dividir el trabajo en pasos cortos, con timeout inferior a 120 s y avance persistido tras cada paso; nunca envolver generación de imágenes en un bucle largo.
- Los captions se basan en `../Dia-NN/caption.md`, no se reescriben por defecto. Un original que solo diga «Pendiente.» no autoriza inventar un caption; conservar pendientes editoriales de Monoga separados del texto publicable.
- `herramientas/componer.py` reutiliza fondos existentes y compone el texto desde `borradores/textos.json`: no necesita Codex ni red. Para mantener un único elemento lima en posts, pasa el foco del fondo a azul solo en la copia compuesta. Los PNG son másteres; no equivalen a archivos aceptados por la API JPEG.
