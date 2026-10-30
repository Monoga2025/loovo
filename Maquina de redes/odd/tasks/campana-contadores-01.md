# TASKS: Producción Campaña Contadores 01 (D1 / D2 / D3)
## Branch: main | Test Runner: local scripts | Objective: Paquete listo para grabar y renderizar

## Specs
- S1: Prompt Maestro para Higgsfield AI (0s - 4s) con especificaciones exactas (inglés/español), cámara de noticiero, banner rojo urgente y sincronización labial.
- S2: Guion técnico segundo a segundo (0s - 45s) con corte brusco, puente de retención, 3 sistemas en B-Roll y CTA de identidad memética D1/D2/D3.
- S3: Activos de edición, prompt de portada y overlays de los 3 sistemas.
- S4: Copy persuasivo para publicación + respuestas DM automáticas por variante.
- S5: Preconfiguración de scripts locales de edición de video para la campaña.
- S6: Registro en Engram (`mem_save`, `project: "loovo"`) y en `../SHARED_STATE.md` de los disparadores.

## Tasks
- [x] T1: Migración de Contexto Claude -> Gemini 3.8 (`GEMINI.md` y `AGENTS.md`) | inline | DONE
- [x] T2: Creación de `../SHARED_STATE.md` para sincronización inter-agentes | inline | DONE
- [x] T3: Especificación y plan maestro en `odd/plans/campana-contadores-01.md` (S1, S2, S3, S4) | inline | DONE
- [x] T4: Configurar paquete de producción local y scripts en `odd/campana-contadores-01/` (S5) | inline | DONE
- [x] T5: Registrar disparadores en Engram (`project: "loovo"`) (S6) | inline | DONE

## Log
- L1: 2026-10-17: Solicitud inicial de migración de contexto a Antigravity (Gemini 3.8) bajo ODD y producción completa de Video #1 Nicho Contadores Colombia con disparadores D1/D2/D3.
- L2: 2026-10-17: Creado SHARED_STATE.md, GEMINI.md, AGENTS.md y plan detallado con prompts de Higgsfield, guion técnico, portada y copys.
- [x] T6: Espejos GEMINI.md/AGENTS.md + skills en .gemini/.agents + registry | inline | DONE (94 archivos c/u, registry 84 skills)
- [x] T7: Paquete `Dia-08/proyecto/contadores_ia/` (guion, higgsfield, edición, portada, copy) | inline | DONE (planeación; sin render)
- [ ] T8: Generar hook en Higgsfield y grabar toma | usuario | PENDIENTE
- [ ] T9: Render HyperFrames + QA en `qa/snapshots/` | Opus (motion) / Haiku (audio) | PENDIENTE
- L3: 2026-10-17: Segunda solicitud: sincronizar skills a .gemini/.agents y producir paquete en Dia-08/proyecto/contadores_ia/ según las reglas reales de las skills.
