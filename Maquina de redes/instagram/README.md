# instagram

Instagram content for the brand: posts, highlight covers, the drafts queue and the scripts that compose the images.

| Path | What it is |
|---|---|
| `AGENTS.md`, `MEMORY.md`, `PROGRESS.md` | Rules, memory and progress of this channel. |
| `cola.md`, `inventario.md` | Publishing queue and inventory of assets. |
| `posts/` | Post concepts (`conceptos.md`) and final images. |
| `destacadas/` | Highlight plan (`plan.md`) and cover images. |
| `borradores/` | Drafts: captions and layout JSON (`textos.json`, `composicion.json`, `medidas.json`), per-post and per-highlight folders, and a log (`REGISTRO.md`). |
| `herramientas/` | Python scripts: `componer.py` (compose), `preparar.py` and `fase1b.py` (prepare), `corregir_destacadas.py` (fix highlights), `puente_codex.py` (bridge script for the Codex image step), plus the font files they use. |

Connections: the captions and covers follow the series rules in `../00_Serie/`. Nothing in this folder publishes content on its own; posting is a manual step.
