# ventas/agentes

Prompt files for the sales agents that support the outreach operation. One Markdown file per agent. Each file defines the agent's role, the inputs it reads and the output it must produce.

| Agent file | Role | Reads |
|---|---|---|
| `auditor-incognito.md` | Drafts the first mystery-shopper message for each clinic and summarizes the detected failure. | `../state.json`, the evidence folder |
| `redactor-secuencia.md` | Personalizes the eight follow-up steps of phase 2 with each clinic's real failure. | `../checklist_ejecucion.md` |
| `preparador-llamada.md` | Prepares the phase 4 call: the clinic's own numbers and a personalized service order. | `../orden_de_servicio_loovo.md` |

The clinical system prompt that is delivered to a clinic is not stored here; it lives in `../flujo_maestro_reactivacion_loovo.md`.

## Rules for any agent in this folder

- Write in Colombian Spanish, using formal address with doctors.
- Never invent results, testimonials or figures. Use only real data from `state.json` and the evidence.
- Do not change the structure of `state.json`; update values only.
