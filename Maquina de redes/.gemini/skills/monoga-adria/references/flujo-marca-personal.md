# Flujo completo: video de marca personal (probado con el Día 4, 85,7 s, 3 fuentes)

Material típico: celular B (vertical, VFR ~29,6 fps), celular A (otra toma/cámara), mic del PC por OBS (audio bueno). Todo se lleva a 30 fps.

1. **Mapa** del crudo: transcripción `small` de todo + hoja de contacto + tabla de bloques, tomas repetidas y choques con `hechos.md` (lo hace el orquestador o tú).
2. **Guion de edición** (orquestador/usuario): bloques gancho -> prueba -> tensión -> giro -> prueba real -> convicción -> cierre; qué escena gráfica va en cada bloque.
3. **Bordes exactos:** `tr_medium.py` en los tramos (whisper medium) y `env.py` (envolvente 20 ms del mic del PC) en cada borde; confirma con `tr_chunks.py` qué palabra queda dentro de un trozo exacto (Whisper "corre" la primera palabra hasta 0,5 s). Corta en silencio (< -60 dB) con ~0,1 s antes y ~0,15 s después.
4. **EDL** en `plan/edl.py` (ejemplo: `scripts/edl_ejemplo_dia4.py`): id, cámara, t0, t1, clave de offset, `gap` (silencio antes). Quita aquí las frases que chocan con `hechos.md`; si el corte cae en una escena gráfica, no se ve.
5. **Sync:** `local_off.py CEL PC esperado t1 t2…` por tramo (B estable ±5 ms; A saltó +60 ms a mitad). `build_audio.py` arma la voz en la línea final (PC 100 % + cel 15 % HPF 80, fundidos 12 ms) y `cel_raw.wav` para verificar.
6. **Palabras en la línea final:** `tr_final.py` -> `onsets.py` -> `words_tl.py` (guarda tiempos de crudo para reubicar si cambia la EDL).
7. **Base de persona:** `faces.py` (cara por tramo) -> `make_base.py` (encuadre S0 1,10, programas de zoom por tramo, zoom-through, zoom-out radial, LUT 75 %). Los huecos siguen el crudo (no congelar).
8. **Escenas:** 2.5D (`depth.py`, `scene25d.py`), citas, motion graphic, placas: en la plantilla `references/plantilla_dia4.tpl.html` (datos inyectados por `build_html.py`).
9. **SFX** (`sfx.py`) y **voz** (`voz_adria.py` o `audio_final.py` del proyecto).
10. `npx hyperframes lint` (0 errores) -> snapshots de ~40 instantes -> corregir -> render (85 s ≈ 25–35 min con 2 workers).
11. **Post:** `post_fx.py` (invert flash + mezcla + H.264 CRF 18, AAC 320k 48 kHz, faststart).
12. **Verificación:** hoja a 2 fps, cuadros clave ampliados, ebur128 en el MP4, `lipsync.py` en 2–3 tramos de persona, xcorr voz final vs celular por tramo, último cuadro.

## Lecciones del Día 4
- Tarjetas de 2 líneas: `.cap .ln { display:block }` (sin eso las líneas se pegan: "de creermeel número uno").
- Clave serif 136 px se salió del cuadro ("verdaderamente"): con palabras de 14+ letras usa ≤118 px.
- Etiquetas pequeñas (30 px) bajo los objetos = ilegibles en el celular: quitadas.
- La lista sobre la persona tapaba la barbilla a y=930: bájala a y≥1000 y mira la cara de ese tramo.
- loudnorm 2 pasadas -> modo dynamic; usa ganancia lineal + limitador.
- Snapshots sin la base terminada fallan: espera a que `make_base.py` acabe.
