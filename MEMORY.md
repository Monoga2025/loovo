# Memoria viva del orquestador de Loovo

Lo que vale para todos los módulos. Las reglas estables están en `AGENTS.md` (los `CLAUDE.md` solo apuntan a él); el tablero entre agentes, en `SHARED_STATE.md`; el estado y las decisiones de cada módulo, en su propio `MEMORY.md`. Última actualización: 2026-10-20.

## Mapa de memoria
- Raíz (este archivo): usuario, decisiones transversales, protocolos y aprendizajes.
- `servicios/omni-sales-crm/MEMORY.md`: embudo Contadores D1/D2/D3, pendientes del CRM. Los demás módulos crean el suyo con la misma estructura (Estado, Pendiente, Decisiones, Aprendizajes).
- Engram (`project: "loovo"`) es el índice de búsqueda de respaldo, no la fuente principal.

## Usuario
Monoga, dueño de Loovo. Español (Colombia). Respuestas cortas, una pregunta a la vez, sincero y con evidencia. Commits convencionales sin atribución de IA; no commit ni push sin pedirlo. Código y comentarios en inglés, conversación y documentación comercial en español. Envíos a leads siempre manuales.

## Decisiones transversales
- **Chatwoot (2026-10-17):** sin fork. Chatwoot hace de bandeja y canales por Agent Bots; `omni-sales-crm` es el motor comercial. Falta verificar licencia y Agent Bots.
- Campaña Contadores 01: disparadores `D1`/`D2`/`D3`. El CRM los lee hoy por DM y chat web; los comentarios de Instagram aún no (ver el MEMORY del CRM).

## Protocolo al delegar
Delegar solo por una razón nombrada (ver `AGENTS.md`, sección ODD). Al llamar a un subagente, pásale la ruta de `MEMORY.md` y de `AGENTS.md` del módulo, la tarea concreta y su `## Allowed edit surfaces`. El subagente lee ambos primero, anota la tarea "en curso" en `SHARED_STATE.md` y, al cerrar, actualiza el `MEMORY.md` del módulo y su sección del handoff (máx. 15 líneas).

## Aprendizajes transversales
- Nada va en 🟢 sin probarlo de punta a punta por el canal real; lo parcial es 🟡 y dice qué falta.
- Prueba primero y observa el fallo antes de implementar.
- Nunca se envían marcadores a un cliente; si falta un dato, lo toma un humano.
- Verifica licencias, APIs y estados antes de recomendar o afirmar.
- Antes de cerrar o de un `/clear`: commit, `MEMORY.md` del módulo, `SHARED_STATE.md` y Engram al día.
