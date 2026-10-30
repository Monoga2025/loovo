# canal

Longer channel recordings, one folder per session. The session name is the date and the hour of the recording:

| Session | Contents |
|---|---|
| `2026-10-17_17h/` | Camera and screen capture, three cuts (9:16), an audio mix and a cover test. |
| `2026-10-17_19h/` | Camera capture, a 9:16 cut about three accounting systems, audio and motion assets. |
| `2026-10-17_19h-b/` | Second take of the 19h session, with a 9:16 cut, audio passes and motion assets. |
| `2026-10-21_11h/` | A single 9:16 video export. |
| `2026-10-21_21h/` | Full edit project: input clip, voice cleanup, music ducking, motion renders and QA logs. |

Each session follows the same layout: `crudo/` (raw, excluded), `entregables/` (final cuts, excluded as video), `proyecto/` (audio, motion, plans and QA logs; media excluded).

Connections: the editing rules are in `../edicion/`. Scripts are checked against `../00_Serie/hechos.md`.
