# clientes-activos

One folder per clinic that has paid the 50% deposit, named with the same slug as its audit folder in `../ventas/evidencia-auditorias/` (for example `01-clinica-demo`). Each folder holds the delivery record of that client.

## Contents of this repository

- `plantilla-entrega-fase5.md`: the delivery template for phase 5 (technical delivery in 180 minutes). Copy it into `<slug>/README.md` and fill it in as the delivery progresses. It records the clinic, the chosen option (A: 14 days; B: 7 days), the deposit date and the delivery date.
- `AGENTS.md` and `CLAUDE.md`: rules for agents working in this folder.

No real client folder is included in this snapshot. Client identities are anonymized in every published example.

## Connections

- The sales pipeline in `../ventas/state.json` moves a clinic here once its deposit is received.
- The detailed technical protocol is in `../ventas/flujo_maestro_reactivacion_loovo.md`.
- Each delivered clinic uses the CRM in [omni-sales-crm](https://github.com/Monoga2025/omni-sales-crm).
