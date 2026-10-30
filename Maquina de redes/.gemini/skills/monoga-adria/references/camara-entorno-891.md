# "La cámara que se mueve en el entorno" + títulos cinéticos (Adrià 8:51–9:05) — probado en el Día 4 (45,1–52,0 s)

Adrià usa clips generados por IA con cámara 3D real. Sin ese material, se hace **2.5D desde una foto**: `scripts/depth.py` + `scripts/scene25d.py`.

## Receta 2.5D (probada)
1. Foto con profundidad clara (primer plano + fondo lejano). Día 4: Long Room del Trinity College (Commons, CC BY-SA 4.0): un busto en primer plano y la sala completa. Vertical o recortable a 9:16 con ≥1,3x de margen.
2. `depth.py foto.jpg` -> `foto_depth.png` (Depth Anything V2 Small, Apache-2.0, transformers; ~100 MB la primera vez; corre en GPU o CPU en segundos).
3. Capas por umbral de profundidad: fondo (todo, con lo tapado relleno por inpaint Telea a 1/4) / medio (`d>t1`) / sujeto (`d>t2`), bordes suaves (σ 2,5–4 px). Si la foto casi no tiene primer plano, umbrales por **cuantil** (`quant=True`, p. ej. 0,50/0,86).
4. Desenfoque: fondo σ 6 (o 3 si es todo fondo), medio 1,6, sujeto 0 (fondo ~4x más borroso, como Adrià).
5. Parallax en x **1 : 1,65 : 1,9** (fondo : medio : sujeto) y escala por capa `s^1, s^1,15, s^1,3`.
6. Cámara (nunca a velocidad constante, sin rotación):
   - Plano A: **paneo `expo.out` 2,7 s** (fondo -140 px, sujeto ~-270 px) -> **empuje `power4.in`** a 1,45 en ~1,15 s.
   - Plano B: entra ya empujando y frena (`expo.out` 0,7 s) -> **dolly-out `power2.inOut`** (×0,86) -> empuje final `power4.in` ×1,40 hacia el destello.
   - Reposo de 2–3 s entre movimientos si la escena dura más (el Día 4 no tuvo tiempo).
7. Desenfoque de movimiento por submuestreo (hasta 8 subcuadros) cuando la velocidad es alta. Viñeta suave 22 %.
8. **Zoom-through entre planos:** empuje saliente + disolvencia de 6 cuadros (`xfade` 0,2 s smoothstep) + whoosh 2–16 kHz con pico 4–7 cuadros después del corte.
Render: 207 cuadros 1080x1920 en ~1,5 min (CPU).

## Títulos cinéticos (probado)
- Frase maquetada de antemano (las palabras aparecen en su sitio final, sin reflujo), 2–3 líneas.
- **Onset = onset de voz - 2 cuadros.** Entrada 5 cuadros (sans) / 7 cuadros (serif) con blur 10 px + subida 22 px; la serif además escala 0,6 -> 1.
- Sans Montserrat 600 88 px crema `#FBF8F1` con sombra; clave Playfair 700 cursiva 150 px dorado claro `#E6D6AE`.
- Se quedan 0,4–1,1 s tras la última palabra y **se van con el movimiento** (se escalan con el empuje y se desenfocan): el título está "pegado" a la cámara.
- Palabras: whisper `medium` por tramo + afinado con la envolvente (`onsets.py`); la primera palabra de cada tramo = primer sonido del tramo.

## Transiciones del video (resumen)
- Volver a la persona: destello crema 0,33 s con el corte en el pico (`destello()` en la plantilla).
- Persona -> gráfico/cita: zoom-through (empuje `power4.in` horneado en la base hasta 1,42 + blur 6 cuadros + disolvencia 6 cuadros) y el subtítulo se escala con el empuje.
- Entre bloques de persona: corte en la pausa + salto de zoom 1,00↔1,08/1,09.
- **Por probar:** clips de video generados por IA (imagen a video) en lugar de 2.5D; glitch cromático en el pico del destello.
