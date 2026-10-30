# Color y texto detrás del hablante

## Color: medir primero, y por defecto natural
- Claude no debe juzgar el color "a ojo". Mide con `scripts/measure_color.py` antes y después: Lab de la pared, la cara y las esquinas, L* medio y percentiles 5/95.
- Interpreta lo que dice el usuario con los datos. Cuando dijo "se ve muy iluminado frente a la animación", lo medido era un video **gris, frío y plano** (pared L* 73 con b* -1,6; negros p5 L* 17), no sobreexpuesto.
- **Lección:** igualar al crema de la animación (tinte cálido, curva S, viñeta 0,38, grano) dio buenos números, pero **el usuario lo vio falso**. Lo que pidió después fue "mover un poco la exposición, el brillo, una mini viñeta oscura".
- **Receta aprobada** (`plan/grade_natural.txt`): `eq=brightness=-0.02:contrast=1.05:saturation=1.02,vignette=angle=PI/9:mode=forward`. Medido: cara L* 47→44, esquinas 74→60, sin cambio de tono.
  - Ojo: `vignette=PI/5.5` ya es demasiado (esquinas a L* 52, media 66→50).
- **Hornea el color con ffmpeg** en `base_graded.mp4` y `pip_graded.mp4`, en vez de usar `data-color-grading` de HyperFrames. Así la silueta recortada, el fondo y el PiP tienen exactamente el mismo color.
- Para elegir, genera una comparación (`hyperframes grade-compare --for frame.png --grades grades.json`, o `hstack` de ffmpeg) con 2–3 opciones y mídelas. Las opciones de gusto las elige el usuario.

## Texto detrás del hablante (efecto "text behind subject")
1. **Máscara:** `scripts/segment.py motion/assets/base.mp4 build/seg/mask.mp4`.
   - rembg con `u2net`, local; en este equipo estaba en `~/.rembg/models/u2net/u2net.onnx`, sin descargar nada.
   - ~1,0–1,3 s por fotograma en CPU (20–25 min para 38 s). Ejecútalo en segundo plano y prueba antes 3 fotogramas con `--test`.
   - Mediana temporal de 3 fotogramas y feather de 1,5 px. La calidad en pelo y hombros fue buena.
   - Segmenta el video **sin zoom**: el zoom se aplica igual a fondo y silueta dentro de la composición.
2. **Silueta con alfa:** `alphamerge` de `base_graded.mp4` y la máscara → `libvpx-vp9 -pix_fmt yuva420p` → `person.webm`. Comprueba con ffprobe que tenga `alpha_mode=1`.
3. **Capas:** fondo → `behind.html` → `#person` → overlays → gráficos. El zoom va a `"#base, #person"`.
4. **Si Chrome se ahoga con el alfa** ("Sequential screenshot capture stalled", "Runtime.callFunctionOn timed out", reinicios en bucle aunque uses `--low-memory-mode`), usa el **plan B**, que dio el mismo resultado visual:
   - `scripts/make_variants.py motion build/seg/mask.mp4` crea `motion_all`, `motion_nob` y `motion_mask`;
   - renderiza los tres con `-w 2` (unos 7 + 7 + 4 min);
   - `scripts/composite_behind.py build/r_all.mp4 build/r_nob.mp4 build/r_mask.mp4 build/motion.mp4`.
   - La mezcla va en RGB (`gbrp`). En YUV la máscara deja el croma al 50 %.
5. **Legibilidad**, verificada en snapshots reales:
   - La palabra va **arriba, sobre la pared**, con el borde inferior por encima de la coronilla **en ese tramo**. Cada punch-in sube la cabeza: en un zoom de 1,28 la coronilla quedó en y≈384.
   - Una sola línea: en "NO SE / HACE" la segunda línea quedó tapada.
   - Si la cabeza llega al borde superior (el usuario se acercó a la cámara en el cierre), **no pongas palabra detrás** en ese tramo.
   - Cuidado con la puntuación donde pasa el pelo: el punto de "+2.000" quedó bajo un mechón y se leía "2,000". Se cambió a "+2 MIL".
   - Revisa el borde con un recorte a resolución completa (`crop`). Lo normal es un halo suave aceptable.
6. Las palabras de atrás también deben ser **literales**: "JUNTOS" se cambió por "ACOMPAÑEN".
