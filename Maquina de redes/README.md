# Maquina de redes

The content machine of Loovo: a daily video series, channel cuts, Instagram posts and the tooling that turns raw recordings into publishable short-form video. The founder records, writes the script, and the agents help edit, caption and track results.

## The series: "Loovo-42"

A "Day X of 42" series that runs toward the Luque Business Summit (Bucaramanga, 17 to 19 November 2026). Day 1 is 7 October 2026 and Day 42 is 17 November 2026. Each day has its own folder and a fixed workflow: brief, script, record, edit, cover and caption, publish, then record 24-hour results.

## Folders

| Folder | What it is | README |
|---|---|---|
| `00_Serie/` | Series bible: facts that may be claimed on air, voice and style, scoreboard, lessons, scripts and brand assets. | [README](00_Serie/README.md) |
| `Dia-01/` to `Dia-08/` | One folder per series day (Days 5 and 6 are not present). Each holds a brief, script, caption, results and project files. | [README](Dia-01/README.md) |
| `canal/` | Longer channel recordings, one folder per session, with cuts and audio work. | [README](canal/README.md) |
| `edicion/` | Editing and delivery rules. | [README](edicion/README.md) |
| `guiones/` | Script-writing rules for niche videos and the series. | [README](guiones/README.md) |
| `instagram/` | Instagram posts, highlights, drafts and the compose scripts. | [README](instagram/README.md) |
| `investigacion/` | Research notes. | [README](investigacion/README.md) |
| `odd/` | Campaign plans and tasks for this content work. | [README](odd/README.md) |
| `qa/` | Visual QA snapshots. | [README](qa/README.md) |

## Flow for one day

1. Write the brief and read the facts in `00_Serie/hechos.md`.
2. Record the raw clip into `Dia-XX/crudo/`.
3. Edit inside `Dia-XX/proyecto/`; finished files go to `Dia-XX/entregables/`.
4. Make the cover and the caption.
5. Publish and record the 24-hour results in `resultados.md`.

## Connections

- `Maquina de redes/` produces the videos that point to [omni-sales-crm](https://github.com/Monoga2025/omni-sales-crm) and to the landing pages in `../landings/`.
- Claims made on air must match `00_Serie/hechos.md`; anything not verified is presented as "coming soon", not as done.

## Not included

Raw footage, rendered videos, audio stems and any file over 20 MB are excluded from this repository. Agent runtime folders (`.claude`, `.agents`, `.gemini`) are excluded too.
