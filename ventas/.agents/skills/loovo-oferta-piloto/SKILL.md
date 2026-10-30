---
name: loovo-oferta-piloto
description: "Trigger: oferta, precio, cotizar, propuesta, piloto, anticipo, contrato, ICP, nicho. Define UNA oferta entregable de Loovo con precio-hipótesis, alcance cerrado y claim audit antes de proponerla."
license: Apache-2.0
metadata:
  author: "loovo"
  version: "1.0"
---

## Activation Contract
Usar antes de ofrecer, cotizar o redactar una propuesta. Complementa `sales-context` y `proposal-pricing` (globales); no los reemplaza.

## Hard Rules
- Una vertical y una oferta a la vez. Vender solo lo que ya se entregó de punta a punta por el canal real (🟢 en `SHARED_STATE.md`). Lo parcial se ofrece como piloto o prototipo rotulado, nunca como producto listo.
- Todo precio es hipótesis hasta que alguien pague. Marcar «no verificado» toda cifra que no salga de datos propios o de una fuente con URL y fecha.
- No prometer citas, ingresos ni resultados. La condición de éxito se acuerda por escrito antes de construir y debe poder medirse.
- Contratado no es caja: 3 contratos de 1.700.000 COP son 5.100.000 contratados y 2.550.000 en anticipos del 50 %. El porcentaje de anticipo lo decide Monoga; no es estándar legal ni de mercado.
- Calcular costos (modelo, servidor, soporte) antes de cotizar. No copiar precios enterprise (Salesforce, 11x, Gong).
- Contrato y tratamiento de datos (Ley 1581) requieren revisión de un abogado.

## Decision Gates
| Situación | Acción |
|---|---|
| Entregable 🟢 y probado | Ofrecer piloto de 7-14 días con anticipo |
| Solo prototipo | Lista de espera o piloto fundador rotulado; no cobrar como listo |
| Nadie lo ha pedido | Volver a conversar antes de construir |

## Execution Steps
1. Leer `SHARED_STATE.md` y `HANDOFF.md`; confirmar qué es 🟢.
2. Escribir el ICP en una línea: quién, dolor medible, quién paga.
3. Definir alcance, exclusiones, plazo, entregable verificable y métrica de éxito.
4. Fijar precio: costo + margen; entrada de bajo riesgo; variable solo si el resultado es verificable.
5. Redactar propuesta de una página con datos del cliente, no genéricos.
6. Claim audit: cada frase lleva fuente o la etiqueta «estimación».

## Output Contract
Propuesta de una página + tabla claim → fuente/estimación + riesgos abiertos. Es un borrador para Monoga; no se envía.

## References
- `references/evidencia-mercado.md`
