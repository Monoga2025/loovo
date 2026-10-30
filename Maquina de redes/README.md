# Loovo-42

Serie "Día X de 42" hacia el Luque Business Summit (Bucaramanga, 17 a 19 de noviembre de 2026). El Día 1 es el 7 de octubre y el Día 42 es el 17 de noviembre.

## Atajo
Di "haz el día N" en Claude Code. La skill `monoga-serie` (comando `dia`) recorre todos los pasos de abajo y te muestra el estado con `python .claude/skills/monoga-serie/scripts/dia.py estado N`.

## Un día, paso a paso
1. **Bitácora:** pídele a Claude la bitácora del día (qué cambió en el CRM y qué tareas se cerraron).
2. **Guion:** lo escribes tú. Claude lo revisa contra `00_Serie/hechos.md` y `00_Serie/voz-y-estilo.md`.
3. **Grabar:** pon el video original en `Dia-XX/crudo/`. Una sola copia.
4. **Editar:** skill `monoga-editor`, dentro de `Dia-XX/proyecto/`. Los finales van a `Dia-XX/entregables/`.
5. **Portada y texto:** skill `monoga-serie`, comandos `portada` (Codex, minimalista 3:4) y `caption`.
6. **Publicar** y marcar `Publicado: sí` en `Dia-XX/resultados.md`.
7. **A las 24 h:** pega las cifras en `resultados.md` y pide el comando `resultados`.
8. **Limpiar:** el comando `limpiar` borra lo pesado del proyecto (pide confirmar).

## Carpetas
- `00_Serie/`: voz, hechos, marcador, aprendizajes, recursos.
- `Dia-XX/`: `brief.md`, `guion.md`, `caption.md`, `resultados.md`, `crudo/`, `proyecto/`, `entregables/`.
- `.claude/skills/`: `monoga-editor` y `monoga-serie`. Abre Claude Code desde esta carpeta para que las cargue.

## Espacio
Cada día crudo pesa más de 1 GB. Con 42 días no cabe en el disco C (42 GB libres al empezar). Archiva `crudo/` en un disco externo o en la nube cada pocos días, y limpia `proyecto/` al publicar.
