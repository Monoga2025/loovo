---
name: loovo-aprendizaje-ventas
description: "Trigger: resultados, métricas, qué funcionó, revisión semanal, experimento, pipeline, post-mortem. Mide cada experimento de ventas con metas previas y deja reglas transferibles, sin datos personales."
license: Apache-2.0
metadata:
  author: "loovo"
  version: "1.0"
---

## Activation Contract
Usar al cerrar una semana, un experimento o una conversación importante. Complementa `pipeline-review` (global).

## Hard Rules
- Definir la métrica y la meta ANTES del experimento. Una meta propuesta no es un pronóstico.
- Solo cifras observadas; lo demás es «no verificado». Separar evidencia de interpretación.
- Sin datos personales ni secretos en notas ni en memoria.
- Un envío no hecho cuenta como 0, no como «pendiente».

## Decision Gates
| Señal | Acción |
|---|---|
| 0 respuestas tras 20 contactos | Cambiar el ángulo del mensaje, no el volumen |
| Cualquier queja o baja | Pausar la secuencia y revisar |
| Respuesta positiva | Pasar a `loovo-conversacion-venta` |

## Execution Steps
1. Contar: contactos, respuestas, respuestas positivas, llamadas, propuestas, ventas cobradas, bajas y quejas.
2. Comparar con la meta fijada antes.
3. Para cada fallo: causa raíz → regla transferible → señal observable.
4. Buscar duplicados antes de añadir una regla.
5. Actualizar `HANDOFF.md` y `tablero/01_ventas.md`.

## Output Contract
Tabla de métricas, 1-3 reglas nuevas y el siguiente experimento con meta y costo máximo.
