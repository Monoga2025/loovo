# Plan de composiciones HyperFrames — Contadores 2030 · D1 / D2 / D3
Skills: `monoga-adria` v2 (pendiente de aprobación del usuario) + `monoga-editor`. 1080x1920, 30 fps, ~44 s. Guion: `guion_definitivo.md`. Config previa: `produccion_config.py` (sus tiempos y nombres de b_roll quedan reemplazados por este plan; actualizarla al implementar).

## 0. Reglas visuales (de `monoga-adria`)
- Fondo blanco pastel `#F6F4EF` con puntos grises `radial-gradient(circle at 12px 12px, rgba(170,165,156,.42) 0 1.1px, transparent 1.6px) 0 0/24px 24px`, grano multiply 5 %.
- Dorado `#C8B07A` (líneas, cursor), `#A88F57` (texto dorado sobre pastel), `#E6D6AE` (clave sobre carbón o video). Carbón `#2A2926`, gris `#8C887F`, crema `#FBF8F1`.
- Montserrat 500/600 + Playfair Display 700 cursiva. Sombras cálidas difusas. `* { border-radius:0 !important; }` en cada composición (solo los puntos del fondo son redondos).
- No recortar la silueta del usuario ni cambiar su fondo; LUT `adria_look_75.cube` solo sobre la persona.
- Sin fondos dorados, sin verde/lima, sin azul eléctrico, sin rojo saturado. Estados: "cuadra" = carbón con check dorado; "no cruza" = dorado oscuro `#A88F57` con marca y motivo. Nada de verde/rojo (cambia lo que decía el plan anterior).
- Texto: frases >= 80 px, claves >= 118-150 px; tarjeta >= 0,5 s; zona segura TikTok: nada importante en los 480 px inferiores.
- Voz a -17,6 LUFS / LRA ~4,5 / TP <= -2 dBTP, solo mic del PC; música baja con ducking. Invert flash máx. 2 en el video.
- Motion graphic: Opus, con el prompt literal de `monoga-adria` §0.1 sin reescribirlo. Audio, medición, transcripción: Haiku.

## 1. Regla de B-Roll de los sistemas
Cada escena de sistema (S1-S3) se compone con material real: capturas o grabación de pantalla de los flujos funcionando. Hasta entonces, la composición queda como **plantilla con marcadores `PENDIENTE B-ROLL REAL`** y el slot de video vacío; no se renderiza un mock animado que simule resultados. Los textos de overlay solo muestran cifras medidas en la captura real. Datos de terceros (NIT, razón social, CUFE, nombres, saldos) desenfocados (blur >= 24 px) o ficticios, verificar cuadro a cuadro.

## 2. Línea de tiempo
| t (s) | Cuadros | Composición | Contenido |
|---|---|---|---|
| 0,00-4,00 | 0-120 | `c00_hook` | Clip de la reportera (Higgsfield). Rótulos HTML: banda carbón `ÚLTIMA HORA` + `COLOMBIA 2030` en crema, etiqueta `SIMULACIÓN IA` en dorado, logo ficticio "NOTICIAS 2030" tipográfico. Esquinas rectas. |
| 4,00-4,50 | 120-135 | `c01_crunch` | Grietas de cristal desde el centro (6 cuadros) + invert flash diagonal 8 cuadros + glitch Mixkit 1022 (flash 1 de 2). |
| 4,50-10,00 | 135-300 | `c02_persona_puente` | Usuario a pantalla completa, respiración 1,00-1,07. Título cinético `ESTAMOS EN 2026` (onset = voz - 2 cuadros, clave serif). |
| 10,00-18,00 | 300-540 | `c10_sistema1` | Ver 3.1 |
| 18,00-26,00 | 540-780 | `c20_sistema2` | Ver 3.2 |
| 26,00-34,00 | 780-1020 | `c30_sistema3` | Ver 3.3 |
| 34,00-36,00 | 1020-1080 | `c40_vuelta` | Salida con invert flash (2 de 2) hacia el usuario; frase de transición con tarjeta de 2-4 palabras. |
| 36,00-44,00 | 1080-1320 | `c50_cta` | Ver 4 |
| 44,00-44,50 | 1320-1335 | `c60_placa` | Placa final: `#LoovoContadores` o la que decida el usuario (sin "DÍA N", este es video de nicho/canal). |

Transiciones: persona -> sistema = zoom-through (empuje power4.in + disolvencia 6 cuadros + whoosh); sistema -> sistema = zoom-through continuo; gráfico -> persona = destello crema 0,33 s. Corte siempre en la pausa de la voz.

## 3. Los tres sistemas (misma gramática, tres cajas)
Estructura común de cada `cNN_sistemaX`: fondo pastel + puntos con deriva parallax; ventana del B-Roll real (rectángulo recto, sombra cálida, marco hairline dorado 2 px); a la izquierda o arriba una **caja carbón** con el nombre del sistema en crema y cursor dorado que crece revelando el texto; entrada `expo.out` 0,5 s desde escala 4 con blur 18, sin rebote; salida por zoom-through.

### 3.1 Sistema 1 — `AGENTE DIAN` · `PENDIENTE B-ROLL REAL`
- Slot: grabación del chat del agente con una pregunta y su respuesta con el artículo citado.
- Overlay: resaltado dorado `#C8B07A` al 35 % sobre el artículo citado (sin cambiar el texto); chip rectangular `ART. [N] ET` con el número tomado de la captura; si calcula en UVT, chip `UVT` con la cifra de la captura.
- Prohibido: contador de "2,4 s" u otro tiempo, salvo medido sobre la captura real.
- Audio: teclas suaves + whoosh + ding bajo (-8 dB).

### 3.2 Sistema 2 — `FACTURA -> SHEETS` · `PENDIENTE B-ROLL REAL`
- Slot: grabación del chat (WhatsApp o Telegram, el que funcione) enviando la factura y de la hoja de Google Sheets con la fila creada.
- Overlay: encabezados de la hoja resaltados en dorado conforme aparecen: Fecha, NIT, Razón Social, CUFE, Subtotal, IVA, Retefuente, ReteICA, Total, Categoría PUC. Valores de NIT, razón social y CUFE desenfocados.
- Prohibido: logos de Siigo o Alegra, "2 segundos", barrido láser simulado si el flujo no lo hace.
- Audio: mensaje entrante + pop corto.

### 3.3 Sistema 3 — `CONCILIADOR` · `PENDIENTE B-ROLL REAL`
- Slot: captura del resultado de la conciliación (extracto vs. auxiliar, con datos de ejemplo o desenfocados).
- Overlay: líneas doradas hairline que unen filas cruzadas (carbón con check dorado); partidas no cruzadas en dorado oscuro con chip de motivo tomado de la captura: `GMF 4x1000`, `CUOTA DE MANEJO`, `COMISIÓN ACH`, `IVA COMISIÓN`. Texto bancario: nombre en tipografía propia, sin logos vectoriales de Bancolombia ni Davivienda (marcas ajenas).
- Prohibido: "1.420 movimientos en 4,8 s", "0 errores", barra de progreso inventada. Si se muestra un contador, es el real.
- Audio: proceso digital suave + dos bips bajos.

## 4. CTA visual D1 / D2 / D3 (36-44 s)
Base: usuario a pantalla completa, a cámara, energía alta, LUT y respiración. Tres momentos, cada uno cuando lo dice (onset = voz - 2 cuadros). Cada sticker entra con rebote cero (`expo.out`), sin bordes redondos, sin recortar la silueta (se coloca a un lado, nunca sobre la cara).

| Momento | Voz | Visual | SFX |
|---|---|---|---|
| D1 (~36,0 s) | "Comenta D1…" | **Logo Tiendas D1** como chiste de marca: sticker `assets_src/d1_logo.png` (lo aporta el usuario) con el `D1` de la palabra clave en Playfair 150 dorado `#E6D6AE`. **Plan B recomendado:** tarjeta tipográfica propia (rectángulo crema, `D1` grande en carbón y filete dorado, sin colores ni tipografía de la tienda) por riesgo de reclamo de marca registrada en cuenta comercial. | Ka-ching corto |
| D2 (~39,0 s) | "D2 si quieres dos" | **Dedos**: la mano real del usuario con dos dedos, con `D2` en serif dorado junto a ella; si no se logra el gesto, sticker vectorial propio de dos dedos, trazo carbón, sin contorno redondeado. | Pop de caricatura |
| D3 (~41,5 s) | "D3 si los quieres los tres" | **Badge**: sello rectangular (esquinas rectas) carbón con filete dorado, `D3` en serif y la leyenda `LOS 3 SISTEMAS`, con tres marcas pequeñas que encienden en dorado una a una (una por sistema). Sin la palabra "VIP" ni "pack completo con auditoría" (oferta no dicha en el video). | Whoosh con brillo ascendente |

Cada trigger deja visible su sticker hasta el siguiente; al decir D3 se apilan los tres a un costado como tablero de elección. Texto de apoyo fijo en la zona segura alta (no en los 480 px inferiores): `COMENTA D1 · D2 · D3`.

## 5. Audio
Gancho: voz de la reportera + cama de tensión. Crunch: silencio 0,4 s + SFX cristal + glitch. Resto: solo voz del usuario (mic del PC, 0 % celular), sincronizada por ondas (`sync_audio.py`), HPF 70 Hz + loudnorm 2 pasadas a -17,6 LUFS; música baja con ducking que sube en los huecos y en las escenas de sistema. Licencia de la música verificada y anotada.

## 6. Pendientes que dependen de los flujos reales
1. B-Roll real de S1, S2 y S3 (grabación de pantalla con datos de prueba). Sin esto no hay render final.
2. Qué dice cada overlay (artículo, UVT, campos, motivos de descuadre, tiempos, cantidad de movimientos): se toma de las capturas, no se inventa.
3. Canal real de D2 (WhatsApp o Telegram) y bancos reales probados en D3.
4. Logo de Tiendas D1: decisión del usuario (sticker real o plan B tipográfico).
5. Enlaces `CONTADORES_LINK_D1/D2/D3` y ingesta de comentarios: afectan lo que puede decir el CTA.
6. Aprobación del usuario de `monoga-adria` v2, del invert flash y del glitch.

## 7. Verificación antes de "listo" (guardar en `qa/snapshots/`)
`grep border-radius` solo `0 !important`; hoja a 2 fps + cuadros clave (0, crunch, S1, S2, S3, CTA, último); ebur128 en el MP4 final; lipsync en 2-3 tramos; terceros desenfocados cuadro a cuadro; nada que choque con `hechos.md`. Claude no oye ni ve el celular: lo medido y lo no medido se reporta.
