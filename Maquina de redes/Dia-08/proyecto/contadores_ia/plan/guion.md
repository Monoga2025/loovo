# Guion de grabación — Nicho Contadores · D1 / D2 / D3
Skill: `monoga-guionista` (comando `corto`, estructura B: gancho ajeno + giro). Duración objetivo: 42–45 s. Formato 9:16.
Reglas aplicadas: literal solo gancho y cierre (≈35 % del texto); resto en puntos; sin cifras de investigación; nada ⏳/🟡 dicho como hecho.

## Quién habla
- Gancho 0–4 s: **reportera generada con IA** (personaje de ficción, rotulada "SIMULACIÓN IA"). No es una persona real.
- 4–45 s: **el usuario**. Carolina solo si el usuario lo decide: la regla 3 de `CLAUDE.md` pide solo la voz del usuario, así que por defecto graba él.

## 0–4 s · GANCHO (literal, voz de la reportera)
> "Última hora: más de treinta mil contadores quedarán desempleados en Colombia en 2030."

Alternativas (elige una al generar en Higgsfield):
- B: "Urgente: en 2030, treinta mil contadores se quedan sin trabajo en Colombia."
- C: "Última hora: la inteligencia artificial deja sin empleo a treinta mil contadores en 2030."

## 4 s · CRUNCH
Pantalla de TV se rompe, flash invertido, corte seco al usuario. Sin voz 0,4 s.

## 4–10 s · PUENTE (puntos, el usuario lo dice con sus palabras)
- Situación: rompe la noticia y dice que estamos en 2026.
- Idea: si no quieres estar en esos treinta mil, usa estos 3 sistemas.
- Frase ancla (opcional, ≤14 palabras): "Estamos en 2026. Todavía estás a tiempo." — conector propio: "Así que…".

## 10–35 s · LOS 3 SISTEMAS (puntos; ~8 s cada uno)
1. **Sistema 1 — Agente de IA con la información de la DIAN** (Estatuto Tributario, conceptos, exógena).
   - Se ve: el chat y la respuesta con el artículo resaltado.
   - Dato: `[DATO: ¿ya responde con artículo citado? sí / lo estoy probando]`.
2. **Sistema 2 — Convertidor de facturas a Excel** (PDF o foto → tabla limpia).
   - Se ve: la foto arrugada entra, sale la tabla.
   - Dato: `[DATO: ¿cuánto tarda en una factura real? medirlo, no estimarlo]`.
3. **Sistema 3 — Conciliador bancario** (extracto vs. contabilidad).
   - Se ve: lo que cuadra en verde, el descuadre marcado.
   - Dato: `[DATO: ¿cuántos movimientos tenía el archivo de prueba?]`.
- Estado al hablar: si el hecho no está ✅ en `hechos.md`, dilo como "estoy probando" o "lo estamos armando". Ver `revision_hechos.md`.

## 35–45 s · CIERRE / CTA (literal, el usuario a cámara)
> "Comenta **D1** si quieres el primer sistema.
> Comenta **D2** si quieres dos.
> Y comenta **D3** si los quieres los tres."

Gestos: en D2 levanta **dos dedos** reales (no stock). Remate opcional en una línea (puente, sin inventar): `[REMATE: lo que viene mañana]`.

## Rúbrica (`references/calidad.md`) — autocrítica
- Gancho con tensión en <3 s: sí. Una sola idea: sí (3 sistemas = una lista). Literal ≤40 %: sí (~35 %).
- Cifras en cámara: solo "30.000", que es **ficción rotulada**, no un dato. Si no se rotula, se quita.
- Puntaje estimado propio: 8/10. No verificado: cómo suena en voz alta (Claude no oye) y retención real.
