# Guion definitivo — "30.000 contadores desempleados en 2030 · Comenta D1, D2 o D3"
Skill: `monoga-guionista` (comando `corto`, estructura C con gancho ajeno). 9:16, objetivo 42-44 s. Fecha: 2026-10-17. Reemplaza a `Dia-08/proyecto/contadores_ia/plan/guion.md` en tiempos, escenas de demo y reglas de B-Roll (el resto de ese paquete sigue vigente).

## Reglas aplicadas
- Literal solo el gancho (reportera) y el cierre (CTA). Lo demás va en puntos: el usuario lo dice con sus palabras. Literal total ≈ 33 %.
- Solo habla el usuario (regla 3), salvo la reportera, que es ficción rotulada "SIMULACIÓN IA".
- Tema de IA aplicada a un nicho. Nada motivacional, sin moraleja.
- **Regla dura de demos:** ninguna frase afirma que un sistema funciona más allá de lo que el B-Roll real muestre. Hasta tener B-Roll real, cada escena de demo es `PENDIENTE B-ROLL REAL` y se dice como "estoy armando / estoy probando". Los tres sistemas no tienen fila ✅ en `hechos.md` y los flujos n8n no se han importado ni probado.
- "30.000" viene del usuario. Va solo en boca de la reportera, rotulada como simulación. No se repite en cámara ni en caption, ni se respalda con fuentes.
- Datos de terceros (NIT, razón social, CUFE, nombres, saldos, extractos) siempre desenfocados o ficticios.

## 0:00-0:04 · GANCHO (literal, reportera IA)
> "Última hora: más de treinta mil contadores quedarán desempleados en Colombia en 2030."

Alternativas (elige una antes de generar):
- B: "Urgente: en 2030, treinta mil contadores se quedan sin empleo en Colombia."
- C: "Última hora: treinta mil contadores desempleados en Colombia en 2030."

Rótulos (los pone el editor, no el modelo): `ÚLTIMA HORA` · `COLOMBIA 2030` · `SIMULACIÓN IA`.

## 0:04-0:05 · CRUNCH
Pantalla de TV se rompe, flash invertido, corte seco al usuario. Voz en silencio 0,4 s.

## 0:05-0:10 · PUENTE (puntos, voz del usuario)
- Situación: rompe la noticia y aclara que estamos en 2026 y que eso lo dijo una IA en un set inventado.
- Idea: estoy armando tres sistemas para contadores, para que no tengan que digitar a mano.
- Frase ancla (≤14 palabras, opcional): "Estamos en 2026. Así que les enseño lo que estoy armando."
- Conector propio: "Así que…". Nada de "calma" ni "todavía estás a tiempo" (suena a motivacional).

## 0:10-0:18 · SISTEMA 1 — Agente tributario · `PENDIENTE B-ROLL REAL`
Contrato: agente de IA sobre el Estatuto Tributario y conceptos DIAN que cita artículos y calcula en UVT.
- Se ve: chat con una pregunta tributaria; la respuesta cita el artículo; un cálculo en UVT.
- Puntos: es un agente con el Estatuto Tributario y los conceptos de la DIAN; le preguntas y responde citando el artículo; también calcula en UVT.
- Si el flujo aún no está probado al grabar: "estoy armando un agente con el Estatuto Tributario y los conceptos de la DIAN".
- Prohibido: "te responde en tres segundos", "2,4 s", "entrenado con todo el Estatuto", "vigente 2026", salvo que el B-Roll lo muestre y se mida.
- `[DATO: tiempo real de respuesta, solo si se quiere decir]`

## 0:18-0:26 · SISTEMA 2 — Extractor de facturas · `PENDIENTE B-ROLL REAL`
Contrato: factura por WhatsApp o Telegram que queda en Google Sheets con Fecha, NIT, Razón Social, CUFE, Subtotal, IVA, Retefuente, ReteICA, Total y categoría PUC.
- Se ve: la factura entra al chat (NIT y razón social desenfocados) y aparece la fila en la hoja.
- Puntos: mandas la factura por WhatsApp o Telegram; sale una fila en Google Sheets con los campos contables; se le asigna categoría PUC.
- Prohibido: "tirillas arrugadas", "fotos borrosas", "listo para Siigo o Alegra", "en 2 segundos". El contrato dice Google Sheets, y la plantilla base entra por Gmail, no por WhatsApp.
- `[DATO: tiempo real por factura, medido]` · `[DATO: canal que funcionó en la prueba: WhatsApp o Telegram]`

## 0:26-0:34 · SISTEMA 3 — Conciliador bancario · `PENDIENTE B-ROLL REAL`
Contrato: conciliador determinista (no un LLM) de extractos Bancolombia/Davivienda contra el auxiliar contable; detecta GMF 4x1000, cuota de manejo, comisión ACH e IVA de la comisión.
- Se ve: extracto a la izquierda, auxiliar a la derecha (datos de ejemplo o desenfocados), líneas que cruzan y partidas sin cruzar marcadas con su motivo.
- Puntos: cruza el extracto con el auxiliar por reglas, no adivinando; lo que el banco cobró y no está contabilizado lo marca con el motivo (GMF, cuota de manejo, comisión ACH, IVA de la comisión).
- Prohibido: "1.420 movimientos en 4,8 s", "0 errores humanos", "100 % automatizada", "en segundos". Si el B-Roll muestra N movimientos reales, se dice N.
- `[DATO: cantidad de movimientos del archivo de prueba]` · `[DATO: probado con Bancolombia, Davivienda o ambos]`

## 0:34-0:36 · TRANSICIÓN
Una frase corta del usuario, sin cifras. Ej.: "Los tres los estoy probando con datos de prueba." (solo si es verdad al grabar).

## 0:36-0:44 · CIERRE / CTA (literal, usuario a cámara)
> "Comenta **D1** si quieres el primer sistema.
> **D2** si quieres dos.
> **D3** si los quieres los tres."

- Gestos: en D2, dos dedos reales de su mano (no stock).
- Remate opcional de una línea: "Y te escribo cuando estén listos." Si `CONTADORES_LINK_D1/D2/D3` ya existen y los flujos están probados, puede decir "te lo mando por mensaje".
- Asignación: D1 = sistema 1 · D2 = sistemas 1+2 · D3 = los tres (coincide con `SHARED_STATE.md` y el embudo CRM).

## Autocrítica (rúbrica `calidad.md`)
| # | Nota | Comentario |
|---|---|---|
| 1 Gancho | 2 | Tensión y número en <3 s |
| 2 Voz real | 1 | Falta que el usuario lo pase por su boca |
| 3 Especificidad | 1 | Faltan `[DATO]` medidos |
| 4 Un solo tema | 2 | IA para contadores colombianos |
| 5 En juego | 2 | Digitar a mano vs. sistemas |
| 6 Hechos | 2 | "estoy armando/probando"; 30.000 es ficción rotulada |
| 7 Causalidad | 2 | pero/por lo tanto entre tramos |
| 8 Bucle | 1 | Cierra en el CTA, sin puente a mañana |
| 9 Recompensa | 1 | Depende del B-Roll real |
| 10 Tics | 2 | Cero palabras prohibidas |
| 11 Ritmo | 2 | |
| 12 Humor seco | 1 | Solo el contraste noticiero falso / oficina real |
| 13 Se puede decir | 1 | No verificado (Claude no oye) |
| 14 Seguridad | 2 | Terceros desenfocados |
| 15 Libertad | 2 | ≈33 % literal |

Total estimado 24/30, sin ceros en 1, 3, 6, 10 ni 14. No medido: voz en alto y retención.

## Problemas
- "Te los envío por DM" no puede decirse hasta que existan los enlaces. Arreglo: remate "te escribo cuando estén listos".
- Los comentarios de Instagram no disparan el embudo (solo DMs, según `SHARED_STATE.md`). Arreglo: construir la ingesta de comentarios o cambiar el CTA a "escríbeme D1 por mensaje".
- Los tres sistemas no tienen fila en `hechos.md`. Arreglo: el orquestador agrega filas 🟡/✅ al probar cada flujo.
