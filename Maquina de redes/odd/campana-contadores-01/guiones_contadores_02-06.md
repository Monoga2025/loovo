# Guiones Contadores 02 a 06 (borrador del orquestador, para que el usuario los diga con sus palabras)

Base: análisis del guion `Dia-08/proyecto/contadores_ia/plan/guion.md`. Reglas: gancho y cierre literales (≈35 %), resto en puntos; solo se afirma lo ✅ de `hechos.md` (lo demás: "estoy probando"); nada motivacional; sin cifras no verificadas; 9:16, 35-45 s.

## Qué funcionó en el guion base (el "oro" que se copia)
1. **Gancho ajeno**: la primera voz no es el usuario (reportera IA, rotulada), así que no suena a vendedor.
2. **Crunch**: corte seco de 0,4 s sin voz entre la ficción y el usuario.
3. **Una sola idea**: los 3 sistemas son una lista, no tres temas.
4. **Cada sistema = algo que se VE** (chat con artículo, foto que se vuelve tabla, descuadre marcado).
5. **CTA en escalera** (D1 uno, D2 dos con dedos reales, D3 los tres): el comentario mide cuál sistema activa.
6. **Honestidad de estado**: lo no probado se dice "estoy probando".

## Mapa: un sistema por video para medir cuál activa más
| # | Sistema | Estructura | Palabra |
|---|---|---|---|
| 02 | D2 Facturas a Excel | dolor del cliente (voz ajena) | D2 |
| 03 | D1 Agente DIAN | pregunta ajena + prueba en vivo | D1 |
| 04 | D3 Conciliador | reloj/viernes (ritual de dolor) | D3 |
| 05 | Los 3 | voz del cliente que regatea | D1 / D2 / D3 |
| 06 | Detrás de cámara | "se equivocó" (prueba pública) | D1 |

Regla común antes de grabar: el B-Roll de ese sistema debe ser real (flujo importado y corrido en n8n con datos de prueba). Hasta entonces el verbo es "estoy probando".

---
## 02 · Facturas a Excel (D2) · 38 s
- **Gancho (literal, voz ajena en mensaje de WhatsApp en pantalla, leída por el usuario con tono de cliente):** "Contador, le mando las facturas. Son como cuarenta fotos, ahí van." `[DATO: cambiar "cuarenta" si no es una situación que te ha pasado]`
- **Crunch:** notificación de WhatsApp, corte seco.
- **Puntos:** situación (foto arrugada, mala luz) · la mandas al sistema · se ve cómo sale la fila con fecha, NIT, IVA, total · qué marca para revisar (NIT con dígito de verificación mal) · `[DATO: segundos por factura, MEDIDO]`.
- **Estado:** D2 aún no probado con facturas reales: decir "lo estoy probando".
- **Cierre (literal):** "Comenta D2 y te digo cómo lo pruebas con tus propias facturas."

## 03 · Agente DIAN (D1) · 40 s
- **Gancho (literal, pregunta ajena):** "¿Esto lleva retención o no? Y cítame el artículo."
- **Crunch:** pregunta en la pantalla del chat, silencio 0,4 s.
- **Puntos:** haces la pregunta de verdad al agente · se ve la respuesta con Artículo del ET resaltado y el cálculo en UVT · lo que NO hace (no reemplaza tu criterio; las cifras de UVT las verificas tú) · `[DATO: ¿acertó? mostrarlo aunque falle]`.
- **Estado:** UVT 2026 aún sin cargar; no mostrar cifras en pesos hasta verificar la resolución.
- **Cierre (literal):** "Comenta D1 y te paso el agente para que lo rompas tú."

## 04 · Conciliador (D3) · 38 s
- **Gancho (literal):** "Viernes, cuatro de la tarde. Y el extracto no cuadra."
- **Crunch:** reloj marca la hora, corte seco.
- **Puntos:** subes extracto y auxiliar · lo que cuadra pasa solo · se marcan GMF 4x1000, cuota de manejo, comisión e IVA · quedan dos listas: "en bancos y no en libros", "en libros y no en bancos" · `[DATO: movimientos del archivo de prueba, REAL]`.
- **Estado:** lógica probada con Node y datos ficticios; en n8n falta importarlo. Decir "datos de prueba".
- **Cierre (literal):** "Comenta D3 y te muestro cómo cuadra tu extracto."

## 05 · El cliente que regatea (los 3) · 42 s
- **Gancho (literal, voz de cliente):** "¿Y por qué me cobra eso si eso lo hace la inteligencia artificial?"
- **Crunch:** corte seco al usuario.
- **Puntos:** la IA hace el trabajo repetitivo (digitar, cuadrar, buscar el artículo) · el contador sigue siendo quien firma y responde · por eso conviene tener los 3 sistemas · recorrido rápido de los 3 con una imagen cada uno.
- **Estado:** solo mostrar lo ✅; el resto "estoy probando".
- **Cierre (literal):** "D1 el agente, D2 las facturas, D3 el conciliador. Comenta la que quieras."

## 06 · Detrás de cámara: "se equivocó" · 35 s
- **Gancho (literal):** "El agente se equivocó con un artículo. Mira cómo lo arreglé." `[SOLO si ocurre de verdad en la prueba; si no, no grabar este video]`
- **Crunch:** pantalla con el error, corte seco.
- **Puntos:** qué preguntaste · qué respondió mal · qué cambiaste en el prompt o la ingesta · repites la pregunta y ahora cita bien.
- **Cierre (literal):** "Si quieres probarlo tú, comenta D1."

---
## Autocrítica y límites
- Puntaje propio estimado: 7/10. No verificado: cómo suena en voz alta ni la retención real.
- Los ganchos 02 y 04 dependen de situaciones que el usuario reconozca como suyas: si no suenan naturales, reemplazarlos.
- Comentarios de TikTok/IG: dispara el embudo solo cuando exista la automatización de comentarios (ver `SHARED_STATE.md`); mientras tanto, el CTA es "escríbeme D2 por mensaje".
- Estrategia sugerida: 5 videos de Contadores (1 por día) y luego 1 video por nicho; así el comentario mide el sistema y no mezcla nichos.
