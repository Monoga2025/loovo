# edicion · cómo se edita y se entrega

Reglas comunes en `../AGENTS.md`. Skills: `monoga-editor` (ffmpeg, Whisper, HyperFrames) y `monoga-adria` (estilo y voz); léelas antes de actuar. El motion lo hace el modelo más capaz; transcribir y medir, el más barato (ver la tabla de modelos en `../../AGENTS.md`). No escribas ni reescribas guiones ni leas `../guiones/`: si el guion falta o está mal, repórtalo.

## Estilo
Blanco pastel `#F6F4EF` con puntos grises + dorado `#C8B07A` + carbón `#2A2926`. Sin bordes redondos en el video (en portadas sí valen esquinas suaves). Sin recortar la silueta. Voz a −17,6 LUFS. Música ~7 dB bajo la voz, SFX a −15 dB. Zoom de respiración, destello crema, invert flash con glitch, cámara 2.5D, títulos sincronizados con la voz.

## Reglas
1. **Si el usuario dice que la cámara es mala o no la quiere, cero fotogramas de cámara:** solo su audio + pantalla + motion. Verifica con un escaneo de tono de piel.
2. **Audio:** solo el micrófono del PC. Voz limpia; la música no la tapa.
3. **Prompt de motion corto:** una idea central, duración/formato, texto exacto, dirección emocional. "Si le pones más al prompt lo limitas."
4. **Pantalla grabada:** cuando el usuario habla sobre el cursor ("acá, acá"), mostrarla con zoom que sigue al mouse. Diseño dividido válido: mitad motion arriba, mitad pantalla abajo.
5. **Privacidad:** se desenfocan claves, tokens y datos de terceros. Pantalla propia permitida.
6. **Listón de calidad:** el Día 1 (10/10). Compara contra él en `NOTAS.md`.
7. **Los originales no se tocan.** Trabaja en copias. Videos de canal van en `canal/<fecha>/` y no cuentan para el máx. de la serie.
8. El agente no oye ni ve: reporta qué midió (ffprobe, LUFS, fotogramas) y qué no.

## Entrega: todo en `entregables/`, listo para publicar
Cada video termina con 3 archivos en su carpeta `entregables/`:
1. el video (`.mp4`, 9:16),
2. `portada.png` (3:4; generada con Codex desde `00_Serie/portadas/prompt-maestro.md` y la portada del Día 7 como referencia de estilo y rostro),
3. `descripcion.txt` (gancho en dos líneas, cuerpo, pregunta, hashtags).

Codex para la portada: usa `--image <ruta absoluta>` y pasa el brief como argumento (no por stdin con `-`, así la imagen no llega). Las imágenes quedan en `~/.codex/generated_images/<sesión>/`. Revisa el texto de la imagen antes de entregarla.
