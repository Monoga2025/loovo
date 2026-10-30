# QA · Día 3 (2026-10-10)

- Duración medida: 56,60 s (55,00 s de voz + 1,6 s de cierre "DÍA 3 de 42"). 1080×1920, 30 fps, H.264 + AAC.
- Audio: preset v8 (como Día 2 v10). -11,4 LUFS, pico -1,4 dBTP en los dos MP4 finales. No cumple el -14 de la regla 9: es el objetivo de v8 que pidió el usuario ("más fuerte").
- Sincronía: `check_sync` OK en el corte. La cadena de voz v8 (rubberband) retrasa la voz 33 ms (medido); se compensó recortando 33 ms al inicio del audio. Desfase final contra el corte: 4-5 ms en 2, 25 y 48 s.
- Cortes: la calle no tiene silencios (piso -35 dB, huecos con -9 a -20 dB), así que `validate_edl` falla por diseño. Bordes al mínimo de energía junto a cada palabra (`plan/edl_calle.py`); fade de 30 ms de `build_cut`.
- Voz: tono medido por frase (f0 112-147 Hz, todo el mismo hablante masculino). Otra persona en cuadro en 0-3 s (fuera del corte), en los s 24-29 del crudo (tapado por la escena A) y en 30,7-35,1 s del corte (tapado por las escenas F2 y F3).
- Zona segura: snapshot a 13 s, bien. Las palabras detrás de la cabeza en el tramo superior invaden un poco los 270 px de arriba (es el estilo).
- Último fotograma: cierre animado. A 54,93 s, "FERIA" queda justo bajo la boca, sin taparla.
- Golpes: 12 detectados (pasos y plosivas de la calle), quedan 3.
