# ventas

The sales operation of Loovo: B2B outreach to aesthetic and dental clinics in Bucaramanga and Medellin. This folder has no product code. It holds the pipeline state, the prospect lists, the outreach and audit scripts, the offers and the agent prompts used to move a clinic from first contact to a paid deposit.

All clinic names, doctors, phone numbers and e-mail addresses in this snapshot are fictional placeholders. The original lists were replaced with generated demo records that keep the same structure.

## Contents

| Path | What it is |
|---|---|
| `state.json` | Pipeline state: each clinic, its status, current outreach step, detected failure, and the financial scoreboard. Source of truth for where each prospect stands. |
| `checklist_ejecucion.md` | The six phases of the commercial process, from setup to the financial scoreboard. |
| `flujo_maestro_reactivacion_loovo.md` | Technical protocol for reactivating leads: clinical system prompt, a four-label traffic-light rule and the templates for steps 1 and 2. |
| `orden_de_servicio_loovo.md` | One-page service order shown during the sales call. |
| `oferta_unica_2026-10-21.md`, `propuesta_ingresos_2026-10-20.md`, `piloto_*.md` | Offer, revenue proposal and pilot plans. |
| `toques_2_3_lote1.md`, `respuestas_2026-10-18.md`, `pendientes_doctores_2026-10-21.md`, `enlaces_fase1_lote1.md` | Outreach logs for the first batch: messages sent, replies received, open follow-ups and links. |
| `nichos_prospectos_2026-10-21.md`, `plan_ventas_rumbo_2026-10-21.md` | Niche analysis and the sales plan. |
| `agentes/` | Prompt files for the sales agents. See its README. |
| `playbooks/` | Consolidated sales playbooks: unified 6-stage funnel, objection matrix, generic agent rules. See its README. |
| `prospecting/` | Self-contained TypeScript sub-project: SQLite prospect store and synthetic lead generator, with tests. See its README. |
| `prospectos/` | Prospect lists. See its README. |
| `evolution-railway/` | Ops script for the hosted CRM. See its README. |
| `whatsapp-mcp/` | Third-party WhatsApp MCP bridge used for research. See its README. |
| `evidencia-auditorias/` | Audit screenshots, one subfolder per clinic (for example `01-clinica-demo`). Not included in this snapshot: the captures are removed and the folder is empty. |

## Flow

1. Build the prospect list (`prospectos/`).
2. Audit each clinic with a mystery-shopper test and record the failure in `state.json`.
3. Run the outreach sequence and log replies.
4. Book a call and present the service order.
5. On deposit, update `state.json` and create the client folder in `../clientes-activos/`.

The CRM used for live demos is in [omni-sales-crm](https://github.com/Monoga2025/omni-sales-crm).

## Conventions

- Screenshot names: `YYYY-MM-DD_<channel>_<what>.png`.
- Agents never invent results, testimonials or figures; they use only data in `state.json` and the evidence folder.
- Sending is manual. The AI drafts; a person sends.
