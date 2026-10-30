---
name: monoga-serie
description: "Coordina la serie de videos 'Día X de 42' de Loovo: crea la carpeta de cada día, revisa el guion contra los hechos y la voz del usuario, escribe el texto para TikTok e Instagram, genera la portada con Codex, registra resultados y limpia archivos pesados. Úsala cuando el usuario hable de 'día N', guion, caption, texto de la red, portada, cover, resultados, marcador o limpiar. La edición del video la hace la skill monoga-editor."
---

# Monoga Serie (Loovo · Día X de 42)

La serie cuenta 42 días hasta el Luque Business Summit (Bucaramanga, 17 a 19 de noviembre de 2026). El Día 1 es el 7 de octubre de 2026 y el Día 42 es el 17 de noviembre. El protagonista es **Loovo**, no el CRM.

**Contexto compartido (obligatorio):** al empezar, lee `CLAUDE.md` (raíz de `Loovo-42`), `00_Serie/estado.md` y las últimas 5 entradas de `00_Serie/relevo.md`. Al terminar, agrega tu entrada al final de `relevo.md` y actualiza `estado.md` si cambió algo. Otros agentes (por ejemplo el editor) trabajan en paralelo y solo ven lo que quede escrito ahí.

Lee siempre, antes de escribir nada:
1. `00_Serie/voz-y-estilo.md`: frases reales del usuario y lo que NO dice.
2. `00_Serie/hechos.md`: lo que se puede afirmar (✅), lo que se dice como prueba (🟡) y lo que es próximamente (⏳).
3. `00_Serie/aprendizajes.md` y las últimas filas de `00_Serie/marcador.md`.

## Principios
1. **El guion lo dice y lo aprueba el usuario.** Los guiones completos de ChatGPT y de Claude sonaron genéricos y se rechazaron. Desde el 2026-10-09, la preparación (gancho literal y puntos) la hace `monoga-guionista`. Esta skill revisa lo que se grabó de verdad y propone cambios puntuales.
2. **Nada se afirma sin estar en `hechos.md` con ✅.** Si el usuario dice algo 🟡 o ⏳ ("el CRM actúa", "ya integramos la DIAN"), Claude lo marca y propone la frase honesta.
3. **Nada de cifras inventadas.** Las métricas las pega el usuario. Claude no las estima.
4. **Frases del usuario, no del asistente.** No uses "el caso es que", "literalmente" ni "mira" salvo que el usuario las diga. Los conectores propios son "Así que", "normalmente no se hace", los números primero.
5. **Cero datos de clientes reales en pantalla.** Si el video muestra el CRM, debe ser la base demo.
6. **Una sola copia del crudo.** Se guarda en `Dia-XX/crudo/`. El proyecto de edición lo enlaza, no lo duplica.

## Comandos (el usuario los pide con sus palabras)
### dia (todo el día de una vez)
Cuando el usuario diga "haz el día N", "arma el día N" o "ya grabé el día N", recorre este flujo en orden y no saltes pasos. Tras cada paso, corre `python .claude/skills/monoga-serie/scripts/dia.py estado <N>`: muestra una lista [x]/[ ] con el siguiente paso y actualiza `marcador.md`.

1. **Preparar:** si `Dia-NN/` no existe, `new_day.py N`. Completa `brief.md` (tema, gancho, dato real y los campos `Portada titular`, `Portada secundario`, `Portada etiqueta`, `Portada fotograma`). Pregunta solo lo que falte, en una sola ronda.
2. **Crudo y transcripción:** el video va a `Dia-NN/crudo/`. Transcribe con `monoga-editor/scripts/transcribe.py` y guarda en `proyecto/transcript/`.
3. **Guion:** comando `guion` (revisión contra `hechos.md` y `voz-y-estilo.md`). Si el usuario cambió algo 🟡 o ⏳, díselo antes de editar.
4. **Editar:** `monoga-editor` dentro de `Dia-NN/proyecto/` (corte, subtítulos, motion). Después, el audio con `scripts/audio_pro.py` (golpes y música épica con ducking por voz). Ofrece v4 y v5 hasta que el usuario elija. Guarda los finales en `entregables/`.
5. **Portada:** `python .claude/skills/monoga-serie/scripts/dia.py portada N`. Lee los campos del brief y llama a Codex. Tarda de 5 a 8 minutos. Copia la variante recomendada a `entregables/DiaN_portada_TikTok_3x4.png`; el usuario decide cuál queda.
6. **Caption:** comando `caption`, con la transcripción y el marcador real.
7. **Entrega:** lista de archivos en `entregables/`, qué se midió (LUFS, pico, golpes) y qué no se pudo verificar (Claude no oye ni ve la miniatura en el celular). Cierra con la lista de problemas.
8. **Después de publicar:** el usuario marca `Publicado: sí`; a las 24 h pega cifras y se corren `resultados` y `limpiar`.

`dia.py todo N` hace los pasos automáticos que ya se pueden (muestra el estado y genera la portada si hay crudo y falta la portada). Los pasos que requieren juicio (guion, edición, caption) los hace Claude siguiendo la lista.

Pregunta al usuario solo estas decisiones de gusto: el titular de la portada y la versión de audio (v4 o v5). Todo lo demás se decide con las reglas de esta skill.

### estado
`python .claude/skills/monoga-serie/scripts/dia.py estado <N>` sin hacer nada más.

### nuevo
`python .claude/skills/monoga-serie/scripts/new_day.py <N>`
Crea `Dia-NN/` con `brief.md`, `guion.md`, `caption.md`, `resultados.md`, `crudo/` y `entregables/`, con la fecha correcta, y marca el día como "creado" en `marcador.md`. No sobrescribe un día que ya existe.

### bitacora
Reúne lo que pasó de verdad ese día para que el usuario escriba el guion:
- `git -C <repo monoga-os> log --since="midnight" --oneline` (sin Co-Authored-By; solo lectura).
- Tareas Median del día: `mdn tasks --agent claude` si la CLI está disponible.
- Notas en `Dia-NN/brief.md`.
Entrega una lista corta de "cosas que pasaron hoy" con el estado de cada una (hecha, probada, sin probar). No inventes.

### guion
1. Si hay video grabado, transcríbelo con `monoga-editor` (`transcribe.py`) y trabaja sobre esa transcripción.
2. Revisa cada afirmación contra `hechos.md`. Marca 🟡 y ⏳.
3. Compara con `voz-y-estilo.md`: señala frases que el usuario no diría.
4. Revisa la estructura: gancho en 3 s con un hecho o número real, una sola idea, un dato concreto, algo que salió mal, una promesa para mañana.
5. Si el usuario pide un guion nuevo, escríbelo con sus frases reales y deja `[placeholders]` donde falte un dato.
Guarda en `Dia-NN/guion.md`.

### caption
Texto para TikTok e Instagram, mismo para ambos, menos de 900 caracteres:
1. Dos primeras líneas = gancho (es lo único visible antes del "más").
2. "Lo que no cabía en X segundos": información nueva, no repetida del video.
3. Tres viñetas con emoji: plazo, meta, regla.
4. Marcador del día con cifras reales de `marcador.md`.
5. Línea de mañana (confirmada por el usuario).
6. Pregunta concreta para comentar.
7. 5 hashtags máximo, siempre `#42DiasLoovo`.
Guarda en `Dia-NN/caption.md`.

### portada
Genera la portada de TikTok con **Codex** (`codex.exe`, sesión de ChatGPT del usuario), no con código propio.

`python .claude/skills/monoga-serie/scripts/portada.py <N> --titular "42 DÍAS" --secundario "PARA CAMBIAR LOOVO" --etiqueta "DÍA 1" [--frame 2.2] [--variantes 2]`

Qué hace el script: extrae un fotograma del video (o usa `--frame <imagen>`), arma el brief desde `templates/portada_brief.md`, ejecuta `codex exec` con la foto adjunta, espera y copia las imágenes a `Dia-NN/portada/`. Tarda unos 5 a 8 minutos y gasta unos 60.000 a 90.000 tokens de la suscripción de ChatGPT.

**Reglas de diseño (aprendidas en el Día 1):**
1. **Minimalista.** Fondo liso negro, UN solo acento rojo #E3120B, máximo 3 elementos de texto, mucho espacio. La primera tanda (neón: aro de luz, retícula, resplandores, texto en rojo) se descartó por cargada.
2. **Formato 3:4 vertical, 1080×1440.** Es el recorte de la cuadrícula del perfil de TikTok. Si el usuario pide otro formato, cámbialo con `--ancho` y `--alto`.
3. **El titular es un número o dato real** del video ("42 DÍAS"), legible a 150 px de ancho.
4. **El texto nunca tapa la cara, los ojos ni la boca.**
5. **Fotograma de referencia:** mirando a la cámara, sin otra persona al fondo, manos fuera de la cara. Haz una hoja de contactos con `ffmpeg` y elige con ojos; no uses el primer fotograma.

**Cómo se le habla a Codex (lo que funcionó):**
- Un brief completo, como a un diseñador senior: contexto, público, objetivo, texto exacto con tildes, paleta, tipografía, formato, zona segura, cuántas variantes y cómo guardar. Tener el texto exacto en el brief hace que Codex lo escriba bien; pedirle solo el fondo y poner el texto con código dio resultados peores.
- Pídele que **revise cada imagen con su herramienta de vista** y regenere si hay una letra mal.
- Dile que **no escriba base64 a mano**: en el primer intento falló al guardar los archivos. Las imágenes siempre quedan en `~/.codex/generated_images/<id de sesión>/`; el script las copia a `portada/intento_NN.png`.
- Adjunta solo `referencia.png`. Adjuntar el fondo anterior ayuda a mantener un estilo, pero encarece.

**Revisión obligatoria antes de entregar:**
1. Mira cada variante (hoja de contactos) y comprueba el texto letra por letra, la cara y que nada se cruce.
2. Comprueba que mide el formato pedido (`ffprobe`).
3. Dile al usuario cuál recomiendas y por qué, qué costó y qué no verificaste (cómo se ve en el celular a miniatura).
4. Copia la elegida a `entregables/DiaN_portada_TikTok.png`.
5. Mueve las descartadas a `portada/v1_.../` para no mezclarlas.

### resultados
El usuario pega las cifras a las 24 h. Claude:
1. Las copia a `Dia-NN/resultados.md` y a la fila del día en `marcador.md`.
2. Compara con los días previos (gancho, duración, música, versión) y escribe 2 a 3 hallazgos en `aprendizajes.md`, separando lo medido de lo supuesto.
3. Si hubo versiones A/B, anota la ganadora y propone qué mejorar en `monoga-editor`. Pregunta antes de editar la skill.

### limpiar
`python .claude/skills/monoga-serie/scripts/clean_day.py <N>` muestra qué se borraría y cuánto espacio libera. Solo funciona si `resultados.md` dice `Publicado: sí` y `entregables/` tiene archivos. Con `--yes` borra `proyecto/build`, `motion*`, `audio` y `input`. Nunca borra `crudo/`, `entregables/`, `plan/`, `qa/` ni `fix/`.

## Estructura
```
Loovo-42/
  00_Serie/ (voz-y-estilo, hechos, aprendizajes, marcador, recursos)
  Dia-NN/   (brief, guion, caption, resultados, crudo/, proyecto/, entregables/)
  .claude/skills/ (monoga-editor, monoga-serie)
```

## Reglas de entrega
- Di qué archivo cambiaste y qué quedó sin verificar.
- Cierra con una lista de problemas, uno por línea.
- Si falta un dato, usa `[placeholder]` y pregunta una sola vez.
