# Prompt Higgsfield — Reportera 2030 (gancho 0-4 s)

Formato: 9:16, 4 s, un plano con audio nativo y labial. Genera 3-4 tomas y elige. Canal ficticio "NOTICIAS 2030"; ningún logo real (Caracol, RCN, Noticias Uno). Guardar como `Dia-08/proyecto/contadores_ia/assets_src/hook_reportera.mp4`.

Decisión de diseño: **sin texto quemado en el clip**. Los modelos escriben mal en español; los rótulos (`ÚLTIMA HORA`, `COLOMBIA 2030`, `SIMULACIÓN IA`) los pone el editor en HyperFrames (ver `plan_hyperframes.md`). Así también se evita el rojo saturado, que la marca prohíbe.

## Prompt (inglés, copiar tal cual)
```text
Vertical 9:16, 4 seconds, photorealistic TV news broadcast, one continuous shot, no cuts.
A Colombian female news anchor in her early 30s, navy blazer, hair tied back, serious urgent expression, seated at a modern news desk speaking straight to camera. Medium close-up, 50mm lens, shallow depth of field, very slow push-in.
Background: a modern newsroom with blurred LED screens showing falling charts in warm amber and white, no readable text anywhere in the frame. Cool blue key light with a soft amber rim light.
No on-screen text, no logos, no captions, no lower-third, no watermark.
AUDIO: the anchor says in clear Colombian Spanish, urgent news-reader tone, accurate lip-sync: "Última hora: más de treinta mil contadores quedarán desempleados en Colombia en 2030." A very low newsroom tension bed underneath, no music with lyrics.
```

## Versión en español (si la plataforma rinde mejor así)
```text
Vertical 9:16, 4 segundos, noticiero de TV fotorrealista, un solo plano continuo sin cortes. Presentadora colombiana de unos 30 años, blazer azul marino, pelo recogido, expresión seria y urgente, sentada en un set de noticias moderno, hablando a cámara. Plano medio corto, lente 50 mm, poca profundidad de campo, avance de cámara muy lento. Fondo: sala de redacción con pantallas LED desenfocadas con gráficas en caída en ámbar y blanco, sin texto legible. Luz principal azul fría y contraluz ámbar suave. Sin texto en pantalla, sin logos, sin banner inferior, sin marca de agua. AUDIO: ella dice en español colombiano claro, tono urgente de presentadora y labial exacto: "Última hora: más de treinta mil contadores quedarán desempleados en Colombia en 2030." Cama de tensión de noticiero muy baja, sin música con letra.
```

## Negativo
`on-screen text, captions, logos, real TV channel branding, watermark, extra fingers, distorted hands, jump cuts, cartoon look, subtitles`

## Frase alternativa
Si el usuario elige B o C del guion, cambiar solo la frase entre comillas en AUDIO.

## Revisión antes de usar (la hace el usuario; Claude no oye ni ve)
1. Escuchar acento y labial. "Treinta mil" debe sonar sin trabarse.
2. Duración 4,0 s; si pasa de 4,5 s, recortar el final bajo el crunch.
3. Confirmar que no aparece texto ni logo; si aparece, regenerar.
4. La voz de la reportera es ficción: va siempre con el rótulo "SIMULACIÓN IA".
5. Si el modelo mete rojo fuerte, se neutraliza en edición.
