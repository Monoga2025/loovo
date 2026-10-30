# tablero

A plain-Markdown shared board. Each file tracks the open items of one area, so any agent or person can see what is pending without reading the full history.

| File | Area |
|---|---|
| `01_ventas.md` | Sales: offers, outreach and reading the CRM channels |
| `02_crm_sistemas.md` | CRM and systems: automatic replies, tests of the n8n flows |
| `03_contenido_video.md` | Content and video: upcoming videos and audio fixes |
| `04_web.md` | Web and landing pages |
| `05_operacion.md` | Operations and handoff between sessions |

Items are checkboxes (`- [ ]`). Each area file is updated when a task starts or closes. This board is a coordination aid, not a source of truth for code or data; the source of truth for module status is `../SHARED_STATE.md`.
