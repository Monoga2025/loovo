# clientes-activos · entrega a clínicas que pagaron

Reglas generales en `../AGENTS.md`. La plantilla de entrega (Fase 5, 180 minutos) está en `README.md`; el protocolo técnico, en `../ventas/flujo_maestro_reactivacion_loovo.md`. Skill: `monoga-project-os`.

- Una carpeta por clínica que pagó el 50 %: `clientes-activos/<slug-clinica>/`, con el mismo slug de `../ventas/evidencia-auditorias/`. Copia la plantilla en su `README.md` y márcala durante la entrega.
- Trabajo directo de la sesión principal; aquí no se delega.
- Los datos de la clínica viven solo aquí y en `../ventas/`; nunca en `../servicios/`.
- Los toques de reactivación los envía la clínica o el usuario a mano, por lotes y en el horario de la Ley 2300.
- Al cerrar una entrega: actualiza `../ventas/state.json` (`ENTREGADA` → `PAGADA_100`, marcador) y la sección de ventas en `../SHARED_STATE.md`.
