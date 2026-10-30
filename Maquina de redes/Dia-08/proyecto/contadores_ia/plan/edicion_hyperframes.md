# Plan de edición — monoga-adria + monoga-editor (HyperFrames)
1080×1920, 30 fps, ~45 s. Base: `monoga-editor/templates/hyperframes/` (`behind.html`, `graphics.html`, `overlays.html`).

## Reparto de modelos (regla del usuario, 2026-10-13)
- **Opus:** solo el motion/edición HyperFrames. Se le pasa este plan, la paleta y el prompt literal de `monoga-adria` §0.1 ("make a dynamic motion graphics video that shows what an incredible motion designer you are…"), sin reescribirlo.
- **Haiku:** transcribir, sincronizar y mezclar audio, medir LUFS, hojas de contacto, copiar archivos.

## Material que debe existir antes
| Archivo | Quién lo hace |
|---|---|
| `assets_src/hook_reportera.mp4` (4 s) | Higgsfield, ver `higgsfield_prompt.md` |
| `Dia-08/crudo/` toma del usuario (audio del PC, no del celular) | El usuario |
| Capturas/clips de los 3 sistemas **en modo demo**, sin datos reales | El usuario (ver "No mostrar") |
| Logo Tiendas D1 en `assets_src/d1_logo.png` | El usuario o, si no, el plan B de abajo |
| Mano real con dos dedos | Sale de la toma del usuario en el CTA |

## Línea de tiempo
| t (s) | Cuadros | Capa | Qué pasa | Audio |
|---|---|---|---|---|
| 0,00–4,00 | 0–120 | Hook | Clip de la reportera tal cual. Rótulos en HTML si el modelo los escribió mal | Voz reportera + cama de tensión |
| 4,00 | 120 | **Crunch** | Cristal que se rompe sobre el clip (grietas desde el centro, 6 cuadros) + flash invertido (`post_fx.py`) + glitch | SFX crunch + glitch Mixkit 1022 (0,30 s). Voz en silencio 0,4 s |
| 4,40–10,00 | 132–300 | Persona | Usuario a pantalla completa, LUT `adria_look_75`, respiración 1,00↔1,07. Título cinético: "ESTAMOS EN 2026" (onset = voz − 2 cuadros) | Voz −17,6 LUFS; entra la música baja |
| 10,00–18,00 | 300–540 | Sistema 1 | Zoom-through a gráfico. Chat: pregunta → respuesta con el artículo resaltado en dorado. Caja carbón con cursor dorado: **"AGENTE DIAN"** | SFX teclas + whoosh + ding suave |
| 18,00–26,00 | 540–780 | Sistema 2 | Foto arrugada entra, barrido láser, se vuelve tabla limpia. Caja: **"FACTURA → EXCEL"** | SFX mensaje + scan + pop |
| 26,00–34,00 | 780–1020 | Sistema 3 | Extracto a la izq., contabilidad a la der., líneas cruzan; verde = cuadra, 1–2 filas en alerta. Caja: **"CONCILIACIÓN"** | SFX proceso + 2 bips suaves |
| 34,00 | 1020 | Salida | Invert flash diagonal 8 cuadros + glitch (2.º y último del video) | SFX corto |
| 34,50–45,00 | 1035–1350 | CTA | Persona a pantalla completa mirando a cámara; ver abajo | Voz + música sube en huecos |

## CTA (identidad visual y humor)
| Momento | Frase | Visual | SFX |
|---|---|---|---|
| ~36,0 s | "Comenta **D1**…" | Aparece el **logo de Tiendas D1** sobre carta crema, entra con pop-in y rebote corto (≤1,5 s). Palabra "D1" en caja carbón | Caja registradora "ka-ching" |
| ~39,0 s | "Comenta **D2**…" | El usuario levanta **dos dedos reales**; sobre la mano, texto kinético **"DE-DOS"** (separa "DE" / "DOS" con un corte). Sin stock | Pop de caricatura |
| ~42,0 s | "Comenta **D3**…" | Insignia **D3** con tres casillas: AGENTE · FACTURAS · BANCO, que pasan de candado a desbloqueado una a una (0,25 s c/u) | Tres clics ascendentes + whoosh con brillo |
| 44,5–45,0 | — | Fundido a crema + `D1 · D2 · D3` fijo | Cola de música |

Plan B si el logo de Tiendas D1 no se puede usar: caja plana rojo-naranja con "D1" en blanco, evocadora, no copia exacta.

## Estilo (reglas de `monoga-adria`)
- Fondo gráfico blanco pastel `#F6F4EF` + puntos grises; carbón `#2A2926`; dorado `#C8B07A` solo como acento. Montserrat + Playfair cursiva.
- **Bordes sin redondear** (`border-radius:0`), no recortar la silueta ni cambiar su fondo, frases ≥80 px, claves ≥118 px.
- Excepciones **intencionales** a la paleta: rojo del hook (es la reportera falsa) y el color del logo D1 (≤1,5 s). El usuario debe aprobarlas.
- Audio solo del PC; voz −17,6 LUFS, LRA ~4,5, TP ≤ −2 dBTP medido en el MP4 final. Música con ducking; licencia verificada.
- Máx. 2 invert flash (aquí: crunch en 4 s y salida en 34 s).

## Pantalla de los 3 sistemas — datos
- Mostrar solo resultados que el usuario haya visto funcionar de verdad. Cero cifras de rendimiento ("2,4 s", "1.420 movimientos") salvo que las mida: `[DATO: …]`.
- No poner nombres de bancos ni de Siigo/Alegra como si hubiera integración: no existe en `hechos.md`.

## No mostrar
Datos de clientes reales, `.env`, claves, extractos y facturas reales, CRM fuera de modo demo (`start.ps1 -Demo`).

## QA antes de entregar (`qa/snapshots/`)
1. Hoja de contactos con `ffmpeg` (1 fotograma/s) → `qa/snapshots/hoja.jpg`; fotogramas clave en 4,0 / 36 / 39 / 42 s.
2. Revisa letra por letra todos los rótulos y que nada tape cara, ojos ni boca.
3. `loudnorm`/`ebur128` sobre el MP4 final → pega el resultado en el relevo.
4. Copia el final a `Dia-08/entregables/contadores_ia_tiktok.mp4`.
Claude no ve la miniatura en el celular ni oye el audio: eso lo valida el usuario.

## Cues de SFX
Ver `sfx_cues.json` (misma carpeta).
