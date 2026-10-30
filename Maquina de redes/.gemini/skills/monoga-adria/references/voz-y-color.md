# Voz y color "nivel Adrià" (medidos en su video; probados en el Día 4)

## Voz — PROBADO (Día 4, 85,7 s)
Objetivo medido en Adrià ("Si eres inteligente pero sigues siendo pobre", 15 min): **I -17,6 LUFS, LRA 4,3 LU**, pico 0,0 (él sin margen; nosotros -2 dBTP).
Receta (`scripts/voz_adria.py`):
1. Mezcla base: **mic del PC 100 % + celular 15 % con HPF 80 Hz**, alineados por tramo (`build_audio.py`, `local_off.py`).
2. `highpass=80, EQ -2 dB@150, -1,5 dB@350, -2,5 dB@3,5 kHz, acompressor 3,5:1 umbral -30 dB, +4 dB, knee 6`.
3. Mezcla con SFX (sin normalizar; ganancias absolutas en `sfx.py`).
4. Ganancia lineal al objetivo + limitador x4 a -2,7 dBFS (con -2,25 el MP4 AAC dio -1,7 dBTP; con -2,7 dio -2,4). **No uses loudnorm** si el pico real no cabe: pasa a modo `dynamic` y deja el LRA en 4,1 (comprobado).
Resultado Día 4 medido en el MP4: **I -17,7 LUFS, LRA 4,5 LU, TP -2,4 dBTP**.
- Sin cama musical bajo la voz. Pausas naturales ~0,3 s; las de >1 s solo se recortan dentro de escenas gráficas (no hay jump cut visible).
- Ojo con los cortes de A: la cámara A tuvo un salto de +60 ms entre 13 y 17 min: mide el offset en cada tramo (`local_off.py`, ±1 s de búsqueda).

## Color — PROBADO
LUT `assets/adria_look_75.cube` (ajustada al look de Adrià y mezclada al 75 % con identidad; también hay 50 % y 100 %). El usuario eligió 75 %.
- Solo sobre el footage de la persona: se hornea en la base con `lut3d=file=...:interp=tetrahedral` dentro de `make_base.py`. **Nunca** sobre gráficos ni sobre las placas (romperían el blanco pastel).
- Fotos de B-roll (escena 2.5D): no llevan la LUT; `scene25d.py` les aplica `grade()` (saturación 0,62, cálido suave, negros levantados 8, verdes/teal casi neutros para no meter verde en la marca).
- Lo que hace la LUT en su oficina de pared blanca: más contraste en medios, piel algo más cálida/rosada, altas sin quemar. Comparativa: `look_comparacion.jpg` del análisis (scratchpad, no en el repo).
- **Por probar:** luz de noche/lámpara; pantalla del PC (OBS) con la LUT.
