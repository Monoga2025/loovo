# odd

Organic Driven Development (ODD) working files: the specs, task logs and reports the agents use to plan and resume work.

| Folder | Contents |
|---|---|
| `tasks/` | One feature document per task: numbered specs (`S1..Sn`), a task list, and a log. Examples: `railway-exit.md` (exit plan for hosted services), `pi-voice.md` (push-to-talk voice input for the Pi harness). |
| `reports/` | Read-only inventories and readiness reports, for example the hosting inventory and backup readiness check. |

The workflow is defined in `../AGENTS.md`: authorize, explore, classify, track, implement task by task, and close with a risk line. Feature documents are the specs that delegated agents read by reference.

Connections: `tasks/` items point at code in `../servicios/` and at content work in `../Maquina de redes/`. Reports describe hosted services used by the CRM.
