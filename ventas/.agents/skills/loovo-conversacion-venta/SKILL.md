---
name: loovo-conversacion-venta
description: "Trigger: respondió, objeción, lo pienso, discovery, demo, llamada, negociar, precio, cierre. Conduce la conversación comercial con datos del cliente, demo honesta y un siguiente paso fechado."
license: Apache-2.0
metadata:
  author: "loovo"
  version: "1.0"
---

## Activation Contract
Usar cuando un prospecto ya respondió. Complementa `discovery-call`, `objection-handling`, `demo-script` y `negotiation` (globales).

## Hard Rules
- Hablar como Loovo; si el prospecto pide una persona, pasar a Monoga.
- Demo real con datos propios o autorizados; todo lo demás va rotulado «simulación». No mostrar D1-D3 ni el CRM como listos hasta que estén probados.
- No inventar capacidades, precios ni resultados. Lo no probado se dice «estamos construyendo».
- No presionar. Un seguimiento con valor y parar.
- Sin documentos reales de terceros sin permiso.

## Decision Gates
| Objeción | Principio de respuesta |
|---|---|
| «Lo pienso» | Preguntar qué falta; un seguimiento con valor; parar |
| «Ya tenemos bot o recepcionista» | Pasar al seguimiento posterior, no al primer contacto |
| «Muy caro» | Volver a su costo actual; ofrecer alcance menor |
| «Mándame información» | Ofrecer 15 min con su caso, no un folleto |
| Desconfianza | Piloto corto, alcance escrito, garantía solo si Monoga la aprueba |

## Execution Steps
1. Discovery: cómo atienden hoy, qué pasa fuera de horario, cuántos chats al mes (sus cifras).
2. Cuantificar con SUS números; si no hay, decir «estimación».
3. Demo mínima en su caso.
4. Propuesta con `loovo-oferta-piloto`.
5. Cierre: siguiente paso con fecha; anticipo como condición para empezar.
6. Tras entregar: pedir testimonio solo con permiso.

## Output Contract
Borrador de respuesta como Loovo + próxima acción con fecha + dato nuevo para `loovo-aprendizaje-ventas`.
