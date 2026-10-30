# PROGRESS-motion (B2)
- [ ] 1 person.webm
- [x] 1 build/person/person.webm 1189 fot vp9 yuva420p (mask_all.mkv)
- [x] 2a words: 159 palabras desde transcript/words.json + offsets (cues.json); IGUAL omitida (top mascara 328<330)
- [!] CAMBIO del padre: tiempos viejos (offset por toma) incorrectos; usar plan/cues.json corregido + plan/words_cut.json; entradas visuales -0.05 s
- [x] 2-4 motion/ generado (index/behind/graphics) con tiempos corregidos; IGUAL omitida (top 308<330); words_cut sin 1a palabra de 6 tomas (no inventada)
- [ ] 5 borrador en curso -> out/draft.mp4 (log qa/render_draft.log)
- [!] borrador fallo: stall en fotograma 104/1190 x2 (RAM libre 0.5 GB). Reintento: render final segmentado -> out/video_silent_raw.mp4 log qa/render_final.log
- [!] stall determinista en 104 (tambien segmentado). Snapshot 3.4-3.55 OK. Prueba: PRODUCER_FRAME_DATA_URI_CACHE_LIMIT=4 BYTES_MB=48
- [ ] render final: HF_DE_STALL_MS=600000, -w 1, log qa/render_final3.log
- [!] final3 colgado en 104 >9 min (HF_DE_STALL_MS no ayuda). Prueba: --no-low-memory-mode -w 2 log qa/render_final4.log
- [ ] render final4 avanza (paralelo 2 workers supera 104); salida out/video_silent_raw.mp4
- [!] final4 estancado en 461. Causa probable: keyframes ralos (8.33 s). Recodifico motion/assets con -g 30
- [ ] render final5 (assets g30, -w 2) log qa/render_final5.log
- [!] final5 fallo: timeout ffmpeg extrayendo person.webm (300 s). final6 con FFMPEG_PROCESS_TIMEOUT_MS=1800000, log qa/render_final6.log
- [ ] final6 en 470/1190 (paso el 461)
- [!] final6 colgado (worker0 en 230, worker1 en 836: cuelgue aleatorio de Chrome/GPU). final7: --no-browser-gpu, segmentado --resume, log qa/render_final7.log
- [!] final7 (--no-browser-gpu, segmentado) colgado en 211/1190 >10 min. Render NO logrado tras 7 intentos (stalls en 104,38,461,230/836,211: no deterministas).
- [x] 7b qa/contact_person.jpg (person.webm sobre gris, 1 fps, 8 col)
- RETOMA: motion/ completo y lint 0/0. Falta: render out/video_silent.mp4 (probar en equipo con mas RAM libre / sin B1 en paralelo, o --docker), luego portada (PRIMERO 12.8-13.4 s), contact_render, medidas. Assets en motion/assets ya con -g 30.

## Pasada de datos (2026-10-23, sin render)
- [x] graphics.html CAPS regenerado desde plan/words_cut.json final: 159/159 palabras, texto exacto, 52 grupos, 11 claves en rojo; palabras <0,16 s agrupadas con la siguiente.
- [x] behind.html y punch/shake de index.html = plan/cues.json - 0,05 s (sin cambios). IGUAL sigue omitida detrás (cabeza y=308).
- [x] lint hyperframes 0.8.140: 0 errores, 0 avisos.

## Historial de render (todos fallaron; logs en qa/)
| intento | log | flags | se atascó en |
|---|---|---|---|
| draft | render_draft.log | -q draft, auto (low-memory -> 1 worker) | 104 (x2 con reintento interno) |
| final | render_final.log | HF_SEGMENTED_CAPTURE=true, low-memory, -w 1 | 104 |
| final2 | render_final2.log | PRODUCER_FRAME_DATA_URI_CACHE_LIMIT=4 _BYTES_MB=48, -w 1 | 38, luego 104 |
| final3 | render_final3.log | HF_DE_STALL_MS=600000, -w 1 | 104 (>9 min) |
| final4 | render_final4.log | --no-low-memory-mode -w 2 (assets keyframes 8,3 s) | 461 |
| final5 | render_final5.log | idem, assets -g 30 | falló al extraer person.webm (timeout ffmpeg 300 s) |
| final6 | render_final6.log | + FFMPEG_PROCESS_TIMEOUT_MS=1800000 | 470/471 (worker0 en 230, worker1 en 836) — EL QUE MÁS AVANZÓ |
| final7 | render_final7.log | + --no-browser-gpu, segmentado --resume | 211 |
RAM libre durante los intentos: 0,5-1,7 GB (B1 corría en paralelo).

## Comando recomendado (ejecutar desde proyecto/motion, con >=4 GB libres y sin otros renders)
```
cd "Maquina de redes/canal/2026-10-21_21h/proyecto/motion"
FFMPEG_PROCESS_TIMEOUT_MS=1800000 HF_DE_STALL_MS=300000 nohup npx --yes hyperframes@0.8.140 render -q looks --no-low-memory-mode -w 2 --protocol-timeout 900000 -o ../out/video_silent_raw.mp4 > ../qa/render_final8.log 2>&1 &
```
Vigilar: `grep -o 'done.:[0-9]*' ../qa/render_final8.log | tail -1` cada 5 min; si no avanza en 5 min, matar y reintentar UNA vez con `-w 1`. Luego copiar/validar a out/video_silent.mp4 (1080x1920, 30 fps, 39,64 s), portada en ~12,8-13,4 s, hojas de contactos y medidas.
