# Aprendizajes

## Audio
- Música a 16 dB bajo la voz no se oye. Preferencia tuya: audible, entre 1,5 y 3 dB bajo la voz, con recorte de medios para no tapar la voz.
- Los golpes del dedo en la mesa se detectan por forma de onda: ataque brusco y caída en menos de 60 ms (`Dia-01/proyecto/fix/taps2.py`).
- El Día 1 tiene 157 palabras y 5 huecos (el mayor de 0,31 s). Si quieres que la música "respire", deja pausas al grabar.

## Guiones
- Los guiones de ChatGPT y los míos sonaron genéricos. Escribes tú el guion y Claude lo revisa.
- "El caso es que" y "literalmente" no son tuyas. Ver `voz-y-estilo.md`.

## Pendiente
- Prueba A/B Día 1: v4 (música a 1,5 dB, golpe inicial bajado, final original) contra v5 (3 dB, golpe inicial fuerte, 2 s de música al final). Anotar la ganadora en `Dia-01/resultados.md` y mejorar `monoga-editor` con eso.

## Portada (Día 1)
- La portada neón (aro rojo, retícula, resplandor, titular rojo) se descartó por cargada. Ahora: minimalista, fondo liso, un solo acento rojo, máximo 3 textos, formato 3:4 (1080×1440).
- Codex genera la portada completa con el texto si el brief es de diseñador (texto exacto, formato, zona segura, variantes). El texto salió bien escrito con la tilde de "DÍAS".
- Codex falla al guardar si intenta escribir base64 a mano. Las imágenes quedan en `~/.codex/generated_images/<sesión>/`. `portada.py` las recoge.
- Coste: unos 8 minutos y 90.000 tokens de ChatGPT por 3 variantes.

## Verificar siempre (Día 2)
- **El último fotograma y el de la portada hay que mirarlos a tamaño completo antes de entregar.** El Día 2 terminó en una cara a mitad de palabra con zoom 1,2 y la portada salió con la boca abierta. Arreglo: cola de 0,8 s con la boca cerrada tras la última palabra (el crudo sigue grabando) y fotograma de portada con boca cerrada.
- Audio: la música a 1,5 dB bajo la voz (v4) más SFX a -8 dB tapaban la voz. `v6`: música a 14 dB bajo la voz, SFX a -17 dB, voz con filtro de graves, reducción de ruido leve, compuerta, EQ de presencia y compresión suave.
- Color: más oscuro y con viñeta negra = `eq=brightness=-0.08:contrast=1.10:saturation=1.06:gamma=0.94,vignette=angle=PI/6` (`plan/grade_oscuro.txt`). En `vignette`, un ángulo mayor da más viñeta.

## Volumen y voz (Día 2, v8)
- En TikTok el video sonaba suave junto a los demás aunque estaba a -14 LUFS. v8: objetivo -11 LUFS, pico real -1,1 dBTP, compresión en dos etapas (3,2:1 y 2:1) y limitador a 0,85.
- Voz más grave: `rubberband=pitch=0.944:formant=preserved` (-1 semitono; f0 mediano 125 → 117 Hz), +3 dB de graves a 120 Hz, -2 dB a 300 Hz, presencia +1,5 dB a 3 kHz.
- Música: v4 (1,5 dB bajo la voz) tapaba, v6 (14 dB) no se oía. Punto medio v8: 7 dB bajo la voz; SFX a -15 dB. Ajustar con `--under`.
- Claude no oye: lo medido es LUFS, pico, f0 y centroide; la decisión final es de oído del usuario.

## Marca y motion (Día 2 v10)
- El usuario no quiere rojo (peligro) ni un solo color. Se eligió A "Eléctrico" viendo las 3 propuestas sobre su propia cara: decidir la marca con mocks reales funcionó en una sola ronda.
- El texto detrás de la persona es parte de la firma: segmentar al empezar el día, en segundo plano (~20 min para 63 s).
- En este equipo el render con `person.webm` (alfa) se atascó al 82 %: usar directo el plan B (`make_variants.py` + 3 renders + `composite_behind.py`, ~15 min).

## Referencias de motion (Día 2, ronda 7)
- Análisis de 10 videos de Pinterest (pasado por el usuario) convertido en 9 técnicas probadas: `monoga-editor/references/tecnicas-referencias.md` y catálogo `templates/hyperframes/examples/tecnicas_referencias.html`.
- Lo que más cambia el nivel: una idea por composición con corte duro, texto después de la imagen, placas claro/oscuro, primer plano desenfocado y transición por oclusión.
- La oclusión solo funciona si el objeto es más grande que el cuadro en el corte; se comprueba con snapshots en el corte ±0,1 s.
- Cuando el usuario pide "entrenar la skill", no se re-edita el video: se documenta y se deja la plantilla.
- 3D real sí funciona en HyperFrames: Three.js + glTF CC0. Claves: imports `+esm`, envolver `tl.render` (el seek suprime onUpdate), mapa de entorno para los metales.
