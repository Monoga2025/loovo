# Maquina de redes · índice

Contenido orgánico de Loovo: serie "Día X de 42" (TikTok/IG, Día 1 = 7 oct, hasta el Luque Business Summit del 17-19 nov 2026) y videos de nicho con CTA por comentario (`D1`/`D2`/`D3`). El usuario es el dueño y quien sale en cámara; una colaboradora aparece cuando él lo indica. Estado de campañas: `../SHARED_STATE.md`. Reglas generales: `../AGENTS.md`.

## Trabaja según la tarea (lee SOLO el archivo de tu área)
| Tarea | Área | Lee | Agente Pi (solo con razón nombrada) |
|---|---|---|---|
| Escribir guiones, ganchos, captions | `guiones/` | `guiones/AGENTS.md` | `loovo-guiones` |
| Editar video, motion, audio, portada, entregables | `edicion/` | `edicion/AGENTS.md` | `loovo-edicion` |

Si una tarea mezcla las dos, se separan: primero el guion, luego la edición. Son unidades secuenciales (la edición depende del guion), así que no cuentan como escritores paralelos.

## Mapa de archivos
- `00_Serie/`: `estado.md`, `relevo.md` (últimas 5 entradas), `hechos.md` (lo afirmable), `voz-y-estilo.md`, `aprendizajes.md`, `banco-frases.md`, `marcador.md`, `guiones/`, `portadas/prompt-maestro.md`, `recursos/`, `marca/`.
- `Dia-XX/`: `brief.md`, `caption.md`, `crudo/` (una sola copia), `proyecto/`, `entregables/`. `canal/<fecha>/`: videos de canal, fuera de la serie.
- `odd/plans/` y `odd/tasks/` (campañas y tareas), `qa/snapshots/` (verificación). Comando: `python .agents/skills/monoga-serie/scripts/dia.py estado N`.
- Prohibido escanear de forma recursiva: `Dia-01..04`, `build/`, `node_modules`, `.git`, `dist`, `__pycache__`.

## Skills
`monoga-guionista` y `monoga-serie` → `guiones/`. `monoga-adria` y `monoga-editor` → `edicion/`. Copia canónica: `.agents/skills/` (la leen Pi, Codex y el registro de Gentle AI). `.claude/skills/` y `.gemini/skills/` son espejos: si cambias una skill, resincroniza los espejos y corre `/skill-registry:refresh` en Pi o `gentle-ai skill-registry refresh`.

## Reglas comunes (valen para las dos áreas)
1. Solo se afirma lo ✅ de `00_Serie/hechos.md`; 🟡 = "estamos probando"; ⏳ = "próximamente". Un sistema que no existe nunca se muestra como demo real.
2. Solo la voz del usuario (o de una colaboradora, si él lo indica) en el video; se mide, no se adivina. Voces de personajes IA = ficción rotulada.
3. Sin datos de clientes reales en pantalla; CRM solo en modo demo. No modifiques el repo `monoga-os`.
4. Nada de claves en chat ni archivos (`OPENAI_API_KEY` solo en el entorno). Si el usuario pega una, que la revoque.
5. No borres ni muevas archivos del usuario sin que lo pida.
6. Máx. 3 publicaciones al día. Nada motivacional en la serie; los videos de nicho hablan del dolor del cliente.
7. Estilo: blanco pastel `#F6F4EF` + dorado `#C8B07A` + carbón `#2A2926`; voz a −17,6 LUFS.
8. Guiones y motion con el modelo más capaz; transcribir, medir y mezclar con el más barato.
9. Remotos (SSH, Railway, Odoo, sesiones ajenas): solo con autorización explícita del usuario.
10. Antes de "listo": `qa/snapshots/` y reporte de qué se midió y qué no (el agente no oye ni ve el celular).
11. Al cerrar un hito: entrada en `00_Serie/relevo.md`, `estado.md` si cambió algo, `../SHARED_STATE.md` si cambió una campaña y `mem_save` con `project: "loovo"`.
12. Respuestas al usuario: claras, cortas y completas, sin jerga técnica. Termina con la lista de problemas (uno por línea, con su arreglo).
