# Prompt Higgsfield — HOOK 0–4 s (visual + audio)

Formato: 9:16, **4 s**, un solo plano con audio nativo y labial. Genera 3–4 tomas y elige la mejor.
Canal ficticio: **"NOTICIAS 2030"**. No uses logos de Caracol, RCN ni de ningún canal real: es una noticia falsa y no debe parecer de un medio existente.

## Prompt (copiar tal cual)
```text
Vertical 9:16, 4 seconds, photorealistic TV news broadcast, single continuous shot.
A Colombian female news anchor in her 30s, navy blazer, hair tied back, serious and urgent expression, sitting at a modern news desk and speaking straight to camera. Slow subtle push-in, medium close-up, 50mm lens, shallow depth of field.
Background: modern newsroom with LED screens showing red falling charts. Cool blue key light with red emergency rim light.
On-screen graphics: a red breaking-news lower-third reading "ÚLTIMA HORA" and below it "COLOMBIA 2030". A small corner tag reads "SIMULACIÓN IA". Fictional channel logo "NOTICIAS 2030" top left.
AUDIO: the anchor says, in Colombian Spanish, clear urgent news-reader voice with accurate lip-sync: "Última hora: más de treinta mil contadores quedarán desempleados en Colombia en 2030." Soft newsroom tension bed underneath. No music with lyrics.
```

## Versión en español (si la plataforma rinde mejor así)
```text
Vertical 9:16, 4 segundos, noticiero de TV fotorrealista, un solo plano continuo. Presentadora colombiana de unos 30 años, blazer azul marino, expresión seria y urgente, sentada en un set de noticias moderno hablando a cámara. Plano medio corto, lente 50 mm, fondo desenfocado, avance lento de cámara. Fondo: sala de redacción con pantallas LED con gráficas rojas en caída; luz azul fría y contraluz rojo de emergencia. Gráficos: banner rojo "ÚLTIMA HORA" con "COLOMBIA 2030" debajo, etiqueta pequeña "SIMULACIÓN IA" y logo ficticio "NOTICIAS 2030". AUDIO: ella dice con acento colombiano y labial exacto: "Última hora: más de treinta mil contadores quedarán desempleados en Colombia en 2030." Cama de tensión de noticiero muy baja.
```

## Negativo
`extra fingers, distorted hands, garbled text, wrong spelling, real channel logos, watermark, subtitles burned in, jump cuts, cartoon look`

## Revisión antes de usarla
1. Reproduce y comprueba **letra por letra** "ÚLTIMA HORA", "COLOMBIA 2030", "SIMULACIÓN IA", "NOTICIAS 2030". Si el modelo escribe mal, regenera o tapa los rótulos con motion en HyperFrames (plan B recomendado: el texto lo pone el editor).
2. Acento y labial: escúchalo tú. Claude no oye.
3. Duración exacta 4,0 s; si sale 5 s, recorta el final bajo el crunch.
4. Guarda el archivo en `assets_src/hook_reportera.mp4`.
