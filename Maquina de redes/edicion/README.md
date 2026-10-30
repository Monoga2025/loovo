# edicion

Rules for editing and delivering the videos. The folder currently holds only the agent instructions (`AGENTS.md`) and its `CLAUDE.md` pointer; the edit projects themselves live in the day and channel folders.

## Key rules (from `AGENTS.md`)

- Two skills are used: `monoga-editor` (ffmpeg, Whisper transcription, HyperFrames motion) and `monoga-adria` (voice and style). Read both before editing.
- Motion graphics use the most capable model; transcription and measurement use the cheapest one.
- Every delivery is three files in `entregables/`: the `.mp4`, a `portada.png` cover and a `descripcion.txt` description.

Connections: edits are made inside `../Dia-XX/proyecto/` and `../canal/*/proyecto/`; final files go to the matching `entregables/`.
