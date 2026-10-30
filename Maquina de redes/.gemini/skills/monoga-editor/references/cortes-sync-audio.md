# Cortes, sincronía y audio (lo que falló y cómo se arregló)

## 1. El MP4 de celular trae el audio desfasado
- `ffprobe -show_entries stream=codec_type,start_time` en un video de Android: video `start_time=0`, audio `start_time=0.1786`.
- `ffmpeg -i clip.mp4 -vn audio.wav` pega el audio a 0. Todos los tiempos de Whisper quedan en "tiempo WAV", corridos 0,18 s respecto a los PTS del MP4.
- Si se corta el MP4 con esos tiempos, labios y voz siguen sincronizados entre sí, pero:
  - **la voz llega 0,18 s después que subtítulos y animaciones**, que van con los tiempos de palabra;
  - cada clip arranca con 0,18 s de audio anterior y **corta el final de la última palabra**.
- **Arreglo** (ya en `build_cut.py`): `OFFSET = start_audio - start_video`, que se suma a ambos trims.
- Síntoma que reporta el usuario: "quedó corrida la voz con el video".

## 2. Fuente VFR → ajustar bordes a fotogramas reales
- Los celulares graban a fotograma variable (28 fps con huecos de 0,07–0,25 s). Con `trim` el video se redondea a fotograma y el audio no; con `concat`, la diferencia se acumula clip a clip (se midió hasta -40 ms).
- **Arreglo** (en `build_cut.py`): cada borde se ajusta al PTS de fotograma más cercano (`ffprobe packet=pts_time`). `words_out.json` se remapea con esos mismos bordes.

## 3. Los timestamps de Whisper no sirven para cortar
- Medido contra la energía del audio: error mediano de 0,17 s con `small` y 0,21 s con `medium`, p90 de 0,30 s. **Un modelo más grande no mejora los tiempos**, solo el texto (medium acertó "lobo"/"Loovo" donde small oyó "logo").
- Whisper suele estirar una palabra para cubrir una pausa (p. ej. "noviembre" de 4 s, "y" de 0,8 s) y cierra la palabra antes de su cola real.
- **Arreglo:** `audio_env.py`, con una envolvente de 10 ms, umbral -36 dB (calibrar: piso ~-44, voz -12 a -30) y mínimo 3 fotogramas para contar como voz. `make_edl.py` ajusta cada borde a la voz medida: entrada 40 ms antes, salida 80 ms después, y mira 150 ms hacia adelante para no comerse colas.
- Síntoma que reporta el usuario: "los cortes están muy... empieza después y termina antes". Quiere decir "sobra aire al principio y al final, recórtalo".
- `validate_edl.py` falla si un corte cae sobre voz medida y avisa si sobra aire (más de 0,12 s al inicio o 0,20 s al final).
- Subtítulos: `build_cut.py` estira linealmente el tramo de Whisper de cada clip (`ws–we`) sobre la voz medida (`vs–ve`).

## 4. Material en bruto con muchas tomas
- Lo normal es que el usuario traiga 5–8 min con cada frase del guion repetida 2–6 veces y comentarios entre tomas ("ok", "listo", "suena muy anuncio").
- En el Nivel 1 "limpiar" significa **elegir una toma por línea del guion**: casi siempre la última completa y fluida, o la que sigue a "ya lo tengo". El plan va en `plan/takes.json` y `make_edl.py` lo convierte en EDL.
- **Puede haber otras voces.** Una toma "Así que este es el día 1 de 42" la dijo la novia del usuario. Claude no distingue voces: antes de entregar, lista las tomas elegidas con su segundo de origen y pide al usuario que confirme que todas son suyas. Revisa también quién aparece al fondo del encuadre.
- Si una frase va dicha de un tirón ("Así que la meta…"), no intentes separar el "Así que": empieza el clip ahí.

## 5. Verificación (obligatoria tras cada `build_cut`)
`python scripts/check_sync.py plan/edl.json build/cut.mp4 audio/audio.wav` mide dos cosas:
- **Audio contra diseño:** correlación cruzada; debe dar ±0,005 s.
- **Labios contra voz:** busca el fotograma del corte en la fuente; tolerancia ±45 ms. Se midió entre -7 y +29 ms.

Para el **archivo final** (con zooms y color encima) no compares fotogramas directamente, porque falla con el zoom. Correlaciona la curva de movimiento (diferencia media entre fotogramas) del final contra la del video base en tramos con movimiento; en tramos quietos el resultado es ruido. El audio del final contra el corte debe dar unos 0,002 s.

## 6. Mezcla y loudness
- `amix ... normalize=0`: por defecto amix divide el volumen entre el número de entradas.
- **Música:** genérala con `make_music.py` (libre de derechos). Mide el **stem ya duckeado**: voz en -17 LUFS, música en -36 LUFS, 19 dB por debajo. Primer intento a -15,1 dB: quedó 23 dB debajo; se subió a -11,1 dB.
- **Pico real:** el AAC sube el pico al codificar. Con `TP=-1.5` el final medía -0,8 dBTP. Usa `loudnorm TP=-2` (linear, dos pasadas) + `alimiter=limit=0.708` y vuelve a medir el MP4 final con `ebur128=peak=true`. Resultado: -14,8 a -14,9 LUFS y -2,0 a -2,3 dBTP.
- **SFX:** `make_sfx.py` con cues en `plan/sfx.json` (whoosh, hit, pop, click, swish, riser, glitch, scramble, step, ding). Mezcla a -8 dB. Un efecto por cada golpe visual. Si cambian los tiempos del corte, remapea los cues; no los reescribas a mano.
- Si solo cambia el audio, remuxea (`-c:v copy` o reencodar solo el video ya renderizado) en lugar de volver a renderizar.
