# servicios

The product layer of Loovo: code, automation flows and product documentation. Nothing in this folder holds client data; the CRM seeds fictional demo contacts and the n8n flows ship with fictional test files.

## Contents

| Folder | What it is | README |
|---|---|---|
| [`omni-sales-crm`](https://github.com/Monoga2025/omni-sales-crm) (own repo) | Omnichannel inbox with an AI sales agent, Kanban pipeline, flow builder, follow-up sequences and analytics. One deployment per client. | [README](https://github.com/Monoga2025/omni-sales-crm) |
| `Agentes de IA/` | n8n workflows promised in videos, starting with the accountant niche (D1, D2, D3). | [README](Agentes%20de%20IA/README.md) |
| `ERP IA/` | Placeholder folder, currently empty. | none |

## Connections

- The CRM is the sales engine that receives leads from the content funnel and from the `landings/` pages.
- The n8n flows in `Agentes de IA/` feed the accountant niche and are meant to connect to the CRM.
- Sales operations in `../ventas/` drive which clinics are contacted and which demo data the CRM is loaded with.

## Rules

The folder-level rules are in `AGENTS.md` (read it before editing). Each product has its own `AGENTS.md`, `MEMORY.md` and `odd/` specs. Secrets stay in environment variables, never in files.
