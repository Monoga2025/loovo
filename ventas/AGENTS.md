# ventas · outbound B2B a clínicas estéticas y odontológicas (Bucaramanga, Medellín)

Reglas generales en `../AGENTS.md`. Aquí no se escribe código de producto; eso va en `../servicios/`. Lo atiende la sesión principal; `loovo-ventas` solo se usa con una razón nombrada (ver la raíz).

## Mapa de archivos
- `state.json`: registro oficial por clínica. Estados: `PENDIENTE_AUDITORIA` → `AUDITADA` → `EN_SECUENCIA` → `LLAMADA_AGENDADA` → `ORDEN_ENVIADA` → `ANTICIPO_PAGADO` → `ENTREGADA` → `PAGADA_100` | `DESCARTADA`.
- `checklist_ejecucion.md`: fases y secuencia de 8 toques. `toques_2_3_lote1.md`: textos de los toques 2 y 3.
- `enlaces_fase1_lote1.md`: mensajes de auditoría y enlaces `wa.me` (una línea cada uno).
- `orden_de_servicio_loovo.md`: única fuente de precios, garantías y alcance.
- `evidencia-auditorias/<NN-slug>/`: capturas. `prospectos/`: listas de Google Maps (CSV con puntaje).
- `agentes/`: guiones de apoyo. `../SHARED_STATE.md`, sección `2.2 ventas`: relevo entre módulos.

## Skills por fase (leer antes de actuar)
- 0 Alistamiento: `sales-context`, `proposal-pricing` · 1 Auditoría: `lead-research`, `account-research`.
- 2 Secuencia: `cold-outreach`, `outbound-sequence`, `draft-outreach` · 3 Chat con el doctor: `objection-handling`, `call-prep`.
- 4 Videollamada: `discovery-call`, `demo-script`, `negotiation` · 5 Entrega: `monoga-project-os` · 6 Pipeline: `pipeline-review`.
- Creativos: `meta-ads-designer`, `marketing-loops`, `b2b-web-director`.
- Loovo (reglas, oferta y evidencia propias, en `.claude/skills/`): `loovo-oferta-piloto` (fase 0), `loovo-prospeccion-transparente` (fases 1-2), `loovo-conversacion-venta` (fases 3-4), `loovo-aprendizaje-ventas` (fase 6). Complementan a las skills globales, no las reemplazan.

## Operación
- CRM (Railway): `https://your-app-name.up.railway.app` → vista **Hoy** (secuencia "Lote 1 — 8 toques"), chat con "Sugerir con IA" y "Abrir en WhatsApp". Código en `../servicios/omni-sales-crm`.
- Evolution (`loovo-ventas`) solo registra chats de `EVOLUTION_ALLOWED_NUMBERS`; al sumar clínicas, amplía esa variable y redespliega.
- Railway: proyecto `evolution-api-loovo`; SSH `railway ssh -s omni-crm -i ~/.ssh/id_ed25519_railway` desde `../servicios/omni-sales-crm` (Git Bash, scripts node por stdin `-- node -`). Respalda la base de datos antes de tocar datos. Requiere autorización explícita.

## Reglas duras
- Secretos (`AUTHENTICATION_API_KEY`, `ADMIN_PASSWORD`, `EVOLUTION_WEBHOOK_TOKEN`, claves de IA) solo en variables de Railway; nunca en chat ni archivos.
- Ningún envío automático por WhatsApp (Evolution no es oficial: riesgo de baneo). El usuario envía a mano; la IA solo sugiere.
- Auditoría = paciente incógnito "Daniel Monoga": suena a paciente real colombiano, saludo según la hora, estilo chat (sin puntos ni comas, solo `?` final). Nunca da cédula ni agenda citas reales.
- No inventar personalización, precios, garantías ni resultados; solo datos reales y `orden_de_servicio_loovo.md`.
- Contacto comercial dentro del horario de la Ley 2300: lunes a viernes 7:00-19:00, sábados 8:00-15:00, nunca domingos ni festivos.
- No cambiar la estructura de `state.json`, solo valores. Datos de clientes nunca en `../servicios/`.
- Al recibir el 50 %: estado `ANTICIPO_PAGADO`, sumar `marcador.cobrado_cop` y crear `../clientes-activos/<slug>/` según su `AGENTS.md`.
- Cambiar `state.json` es un cambio de datos persistidos: muestra el diff al usuario antes de guardarlo.
