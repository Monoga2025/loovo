# Instagram · reglas del agente

Módulo de `Maquina de redes/`. Objetivo fijado por Monoga el 2026-10-23: (1) republicar en Instagram lo que ya publicó en TikTok, (2) armar las destacadas del perfil y (3) producir publicaciones con imágenes de IA usando Codex como puente.

## Lee antes de actuar
- `../00_Serie/marca/marca.md` y `marca.json`: identidad vigente, dirección «Eléctrico» (carbón, azul eléctrico, lima ácido, hueso; **sin rojo**). Tipografías en `../00_Serie/marca/fonts/` (Space Grotesk, Instrument Serif cursiva). La portada del Día 1 usa negro, blanco y rojo: es anterior y NO es la marca vigente.
- `../00_Serie/voz-y-estilo.md` (cómo habla Monoga) y `../00_Serie/hechos.md` (solo se afirma lo ✅; lo 🟡 se dice «estamos probando»; lo ⏳ «próximamente»).
- `../00_Serie/marcador.md`: estado por día. No registra ningún día como publicado: el estado real en TikTok lo confirma Monoga.
- `../.claude/skills/monoga-serie/SKILL.md`: secciones `caption` y `portada`.
- `MEMORY.md` de este módulo.

## Estructura
- `inventario.md`: cada video local, si está en TikTok, si se puede republicar y por qué.
- `cola.md`: orden de publicación, caption, portada, formato y estado (preparado / publicado por Monoga).
- `destacadas/`: portadas y guion de stories de cada destacada.
- `posts/`: publicaciones finales (imagen y texto).
- `borradores/`: pruebas y descartes.
- `herramientas/`: scripts propios del módulo.
- `PROGRESS.md`: punto de retoma; se actualiza tras cada paso, porque las tareas en segundo plano mueren si se cierra Pi.

## Reglas
1. **No publica.** Prepara el kit; publica Monoga. Que un agente publique exige autorización expresa por publicación y una vía oficial. Nunca contraseñas, tokens ni cookies en archivos, chat o memoria.
2. **Solo contenido propio.** Prefiere los `*_Reels.mp4` de `Dia-NN/entregables/` a bajar de TikTok (llevan marca de agua). Si hay que bajar algo, solo de la cuenta de Monoga y a una carpeta temporal fuera del proyecto.
3. **No republica** lo marcado «no publicar» ni lo que prometa D1-D3 como existentes. Si hay duda, la fila queda «por decidir» con el motivo.
4. **Textos:** captions con las reglas de `monoga-serie` (menos de 900 caracteres, máximo 5 hashtags, siempre `#42DiasLoovo`), en la voz de `voz-y-estilo.md` y solo con hechos ✅.
5. **Imágenes de IA:** nunca personas inventadas como clientes, testimonios, capturas de sistemas, cifras ni resultados. La cara de Monoga solo desde su foto de referencia, sin alterarla. Lo que no sea una foto real se presenta como ilustración.
6. **El texto no lo dibuja la IA.** La IA genera fondo e ilustración sin texto; el texto se compone con las fuentes de la marca mediante un script en `herramientas/`, para que las tildes y la tipografía salgan exactas. Revisar letra por letra.
7. **Puente Codex:** se reutiliza el método probado de `../.claude/skills/monoga-serie/scripts/portada.py` (`codex exec -C <carpeta> -s workspace-write --skip-git-repo-check [-i referencia.png] -`, con el brief por entrada estándar). Las imágenes quedan en `~/.codex/generated_images/<sesión>/` y se copian al módulo. Tarda varios minutos. Nunca escribir base64 a mano.
8. **Destacadas:** se arman con stories ya publicadas. El módulo entrega portadas y el guion de stories de cada una; título de máximo 15 caracteres.
9. **Formatos y límites** (tamaño de la cuadrícula, duración de Reels, portada de destacada, caracteres): verificarlos en la ayuda oficial de Instagram, con fuente y fecha, antes de fijarlos.
10. **Ritmo:** proponer un calendario, no publicar en masa. No afirmar cómo funciona el algoritmo.
11. Datos de clientes o leads nunca aquí.
