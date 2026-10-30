# HANDOFF · Loovo (sesión del 2026-10-17 al 2026-10-18)

Léelo primero al retomar. Punto de verdad entre agentes: `SHARED_STATE.md`. Sin secretos en este archivo.

## Hecho ✅
### Estructura y agentes
- [x] `CLAUDE.md` raíz podado (mapa, tabla de modelos, límites).
- [x] Subagentes en `.claude/agents/`: `github-n8n-scout`, `worker-guiones` (opus), `worker-edicion` (opus), `worker-sistemas`, `worker-ventas`. `worker-redes` eliminado (reemplazado).
- [x] `Maquina de redes/CLAUDE.md` convertido en índice; reglas por área en `guiones/CLAUDE.md` y `edicion/CLAUDE.md` (respaldo: `CLAUDE.md.bak-2026-10-17`).
- [x] Gemini sin cupo: todo corre con Claude (documentado).
- [x] Hook `gentle-ai review stop-hook` quitado de `~/.claude/settings.json` (copia `.bak-stophook`); `C:\Users\you\.git` renombrado a `.git-disabled`.

### Sistemas para contadores (D1/D2/D3)
- [x] Scout: 9 plantillas n8n descargadas + `REPORTE.md` en `servicios/Agentes de IA/contadores-d1-d2-d3/`.
- [x] `D1-agente-dian-colombia.json`, `D2-extractor-facturas-dian-sheets.json`, `D3-conciliador-bancario-colombia.json` + `datos-prueba/`, `scripts/`, `README.md`. Lógica de D3 probada con Node (18 comprobaciones).
- [x] Importados en n8n (Railway) como flujos INACTIVOS.
- [x] `SHARED_STATE.md` corregido: CRM verificado; n8n y video en 🟡.

### Contenido y guiones
- [x] Guion Contadores 01 (D1/D2/D3, voz de Carolina), plan Hyperframes y prompt Higgsfield (`Maquina de redes/odd/campana-contadores-01/`).
- [x] Guiones 02-06 y V1-V5 (reescritos en UGC); skill `monoga-guionista/references/ugc-ventas.md`.
- [x] Video de canal 17-10: `canal/2026-10-17_17h/entregables/` con corte1, corte2 (full motion), corte3 (motion arriba + pantalla abajo), `portada.png`, `portada_alternativa.png`, `descripcion.txt`.

### Odoo (odoo.grupomonoga.com, Railway)
- [x] Proyecto **Guiones** (Kanban: Idea, Guion listo, Grabado, Editado, Publicado) con 11 tareas en HTML.
- [x] Módulo **CRM** instalado; etapas en español + embudo de contadores; proyecto **Sistemas contadores** (D1-D3).
- [x] Menú "CRM Omni" enlazado a omni-crm (abre en otra pestaña).

### Ventas
- [x] `ventas/respuestas_2026-10-18.md`: 18 clínicas respondieron al Toque 1; mensajes listos; envío manual el lunes 19 desde las 7:00.

### Becas Google
- [x] Postulación a "Crece con Google" enviada (Colnodo). Resultado desde el 26 de octubre por correo de Coursera.

## Pendiente ⬜
- [ ] REVISAR DESPUÉS (usuario: "audio quedó mal", no se publican por ahora): ediciones del 20-oct en `Maquina de redes/canal/2026-10-17_19h/entregables/` (`contadores_3sistemas_9x16.mp4`) y `canal/2026-10-17_19h-b/entregables/` (`Contadores_3sistemas_9x16.mp4`). Originales en Descargas: `VID20261017194137.mp4`, `VID20261017190855.mp4`. Causa probable: el celular grabó la voz saturada y el declip no la salvó; la mejor salida es regrabar el audio con el micrófono del PC. Además prometen D1–D3 por comentario y eso aún no existe.
- [ ] PENDIENTE (decisión del usuario): comprar equipo para redes, no por gusto: iPhone (cámara) + micrófono, para grabar con mejor calidad, subir videos y vender sistemas. Hoy: ahorros $1.000.000 COP, sin ingreso por IA. Pendiente definir cómo pagarlo (el crédito de ~$1,9M probablemente cae en "bajo monto", con tasa mayor al 25 % simulado; verificar). Prioridad práctica: micrófono primero, porque el audio saturado fue la falla de los dos videos.
- [ ] PENDIENTE: subir la calidad del editor de motion. Los cortes del 20-oct quedaron muy por debajo del Día 1 (música, efectos, zoom mientras habla). Rehacer usando el Día 1 como listón, con audio regrabado, antes de publicar nada.
- [ ] AUDIO (micrófono nuevo, igual con ruido y voz saturada): Adobe Podcast Enhance NO tiene API pública (solo socios B2B), así que no se automatiza con código. Opciones: (a) manual: subir el audio a Adobe Podcast y reemplazarlo en el video; (b) código local gratis: ffmpeg `arnndn` + `afftdn` + `adeclip` (ya instalados) o instalar DeepFilterNet/Resemble Enhance (probar con un audio real); (c) API de pago tipo Cleanvoice. Causa a revisar primero: ganancia del micrófono (saturación) y ruido del cuarto.
- [ ] MOTION: el usuario no quiere tocar código ni que lo haga un agente "a mano". Decidir herramienta (plantillas tipo CapCut/Descript, o flujo guiado con Día 1 como listón) antes de volver a editar.
- [ ] GENTLE AI / Pi: arquitectura ODD lista (`AGENTS.md` como fuente única, agentes en `.pi/agents/`, comandos en `.pi/prompts/`). Ver `MIGRACION.md`. Falta: `/trust` de la carpeta en Pi, confirmar modelos de `.pi/agents/` y probar `/retomar`.
- [ ] PI + CLAUDE: puente `pi-claude-bridge` instalado (modelos `claude-bridge/*`). Profiles creados en `~/.pi/gentle-ai/profiles.json`: `claude-ahorro` (Sonnet 5.5 orquestador, Opus solo verificador) y `claude-max` (Opus). Activar con `/gentle:profiles` + enter. Evitar `/compact` con el puente (reenvía toda la conversación): cerrar con `/cerrar` y abrir sesión nueva con `/retomar`.
- [ ] VIDEO: skill principal nueva `receta-dia1` (Sonnet midió Día 1 vs cortes del 20-oct con ffprobe/ffmpeg). Probar edición con Sonnet 5.5, prompt corto de una idea.
- [ ] Correo de Carolina para crearle usuario en Odoo.
- [ ] Confirmar "tokens" vs "toques" (seg. 38,2 del corte) y publicar el video del canal.
- [ ] Ventas, lunes 19 a las 7:00: enviar a mano (citas primero: Sonríe, Lina Caballero, Balance, REAL); actualizar `ventas/state.json` (desfasado vs CRM).
- [ ] D1-D3: UVT 2026, credenciales, pruebas reales, entrada por WhatsApp/Telegram en D2; luego B-Roll real.
- [ ] Comentarios de Instagram/TikTok: ManyChat para "comenta D#/CONTADOR" (hoy el embudo solo lee DMs); faltan `CONTADORES_LINK_D1/D2/D3`.
- [ ] Landing de contadores: la hace el usuario a mano.
- [ ] Decidir: módulo para incrustar omni-crm dentro de Odoo (requiere autorización).
- [ ] Decidir: reescribir en UGC los guiones 02-06 de Odoo.
- [ ] Beca Google: el 26 de oct revisar correo (incluido spam) y activar el mismo día; no pagar la prueba de Coursera antes. Canje de Google AI Pro solo después; no tocar el plan actual (20.000 COP/mes).
- [ ] Reiniciar Claude Code para que los subagentes nuevos se registren con su nombre.
- [ ] Cuando vuelva Gemini: avisar para reactivar `gemini`.
- [ ] Borrar `Maquina de redes/CLAUDE.md.bak-2026-10-17` cuando ya no haga falta.

## Reglas aprendidas
- Guiones los escribe el modelo más capaz, en estilo UGC; el Markdown se convierte a HTML antes de subirlo a Odoo.
- Entregable de video = `.mp4` + `portada.png` + `descripcion.txt` en `entregables/`.
- Nada se envía a pacientes/leads automáticamente y nunca en domingo (Ley 2300).
- Respuestas al usuario: claras, cortas y completas.

## Sesión 2026-10-20 (Claude Code, Sonnet 5.5)
### Tarea 2 · Plan de ingresos ✅ (solo propuesta, no se envió nada)
- [x] `ventas/propuesta_ingresos_2026-10-20.md`: top 5 clínicas, mensajes manuales, 3 ofertas, plan de 14 días con video diario. Cifras propias vs. no verificadas marcadas.
- Hallazgo: la Opción A ($2.500.000, "respuesta 24/7 en 45 s") choca con la regla de envíos manuales y no está probada; no venderla aún.
- `ventas/state.json` sigue desfasado; no sé si el lunes 19 salieron los mensajes.
### Tarea 1 · Monoga:Videos ✅ (pendiente tu aprobación para borrar skills viejas)
- [x] Referencias: 8 videos de @adriasolapastor (5 TikTok con yt-dlp gratis, 3 Instagram con Apify, costo real US$0,0088) en carpeta temporal `%TEMP%dria_ref` (no republicar; borrar cuando quieras).
- [x] Medidas (ffmpeg): cortes duros 14-47/min en 6 videos, 0 en 2 reels de Instagram (zoom digital); 2-16 flashes por video; LUFS Instagram -14,1/-14,5 (las bajadas de TikTok dan -19 a -28, no comparables). Descripción visual hecha por 2 subagentes `gentle-ai-explore` (no se pudo fijar Haiku: el agente no permite elegir modelo). Zoom 110-130 % es estimación visual; música y SFX no verificables.
- [x] Skill nueva: `Maquina de redes/.claude/skills/monoga-videos/SKILL.md` (466 palabras) + `scripts/` (ejemplo probado).
- [x] Prueba con `VID20261017194137.mp4` → `Maquina de redes/canal/2026-10-21_11h/entregables/` (`video_9x16.mp4`, `portada.png`, `descripcion.txt`). Audio -5,9 LUFS/pico +1,3 dBFS (original) → -14,8 LUFS/pico -1,6 dBTP; 15,8 cortes/min; 7 flashes.
- [ ] Aprobar borrado de `monoga-editor`, `monoga-adria` y `receta-dia1` (lista en `Maquina de redes/odd/lista_skills_a_borrar.txt`). No se borró nada.
- [ ] El video NO se debe publicar: promete D1-D3 (no existen) y el color tiene tinte verde de la luz del cuarto.

## Rumbo de ventas (2026-10-21)
- [x] 3 investigaciones de subagentes → `ventas/plan_ventas_rumbo_2026-10-21.md` (diagnóstico, inventario real, 5 decisiones propuestas, 3 experimentos de 7 días, herramientas, legal).
- [ ] DECIDIR: oferta única (Sprint de reactivación para clínicas es la recomendada) y aprobar las 5 decisiones del plan.
- [ ] Leer chats de Evolution (autorizado solo lectura): falta URL y variable de la API key. No hay variables de Evolution en el entorno de esta sesión.
- [ ] Edición con herk-edit-kit PAUSADA por decisión de Monoga: Claude sin créditos (`loovo-edicion`, tarea anterior mvie4zg3-1-b9a5) → `canal/2026-10-21_12h/entregables/`. Audio crudo saturado: no se da por arreglado.
- [ ] Pendiente de tu sí: borrar monoga-editor, monoga-adria y receta-dia1 (lista en `Maquina de redes/odd/lista_skills_a_borrar.txt`).

## Tablero por áreas (2026-10-21)
- `tablero/01_ventas.md` … `05_operacion.md`: una carpeta por área con columnas Por hacer / En curso / Hecho. HANDOFF.md queda como índice y relevo de sesión.
- `ventas/estudio_clinicas.xlsx`: una fila por clínica con columnas de métricas (vacías: por llenar al leer los chats).
- AGENTS.md regla 1 cambiada (respaldo `AGENTS.md.bak-2026-10-21`): la IA puede responder sola a doctores que escriben a Loovo; no se hace pasar por paciente ni inventa datos.

## Tablero por áreas (2026-10-21)
- `tablero/01_ventas.md` … `05_operacion.md`: una carpeta por área con columnas Por hacer / En curso / Hecho. HANDOFF.md queda como índice y relevo de sesión.
- `ventas/estudio_clinicas.xlsx`: una fila por clínica con columnas de métricas (vacías: por llenar al leer los chats).
- AGENTS.md regla 1 cambiada (respaldo `AGENTS.md.bak-2026-10-21`): la IA puede responder sola a doctores que escriben a Loovo; no se hace pasar por paciente ni inventa datos.

## Prioridad actual: ventas; video pausado
- No activar loovo-edicion ni usar Claude/claude-bridge: sin créditos.
- Conservar el trabajo parcial en `%TEMP%/herk_kit/repo/video-projects/contadores-1021/`. No hay entrega final verificada.
- loovo-ventas fijado a `openai-codex/gpt-6.1-sol`, esfuerzo low. Revisar esta semana de chats en Railway/Evolution, solo lectura; redactar sin enviar.
- Railway CLI ya autenticado; proyecto `evolution-api-loovo` vinculado en `%TEMP%/rw_evo`. No volver a pedir claves por chat: obtenerlas en memoria desde Railway, sin imprimirlas.

## Tablero Pi — PAUSADO por Monoga
- Extensión `.pi/extensions/tablero.ts` desactivada: no registra panel, comando ni atajo al recargar. Código y archivos de `tablero/` conservados.
- Pendiente: retomar integración kanban por áreas en columna derecha, colapsable, con prueba real dentro de Pi. No reactivar sin pedido explícito.
- Si el panel sigue visible en la sesión actual, ejecutar `/reload` para descargar la instancia anterior.

## Referencia pendiente para mejorar el editor de video
- [ ] Revisar el post de X compartido por Monoga: https://x.com/KinGao476942/status/2112729924943634602?s=20
- Objetivo: evaluar técnicas o herramientas aplicables al editor de video de Monoga. Post todavía no consultado; no se afirma qué contiene. Mantener video pausado hasta nueva autorización.

## Evolution/CRM — lectura bloqueada (resultado de ventas Codex)
- Informe: `ventas/pendientes_doctores_2026-10-21.md`. Evolution HTTP 200, pero búsquedas por JID de los 25 contactos devuelven cero incluso sin fecha. No prueba ausencia de chats; posible asociación LID pendiente de verificar.
- CRM: HTTP 401 sin sesión autenticada. Railway SSH: timeout puerto 22, un intento de recuperación agotado. No insistir por SSH.
- No se confirmó quién espera respuesta ni automatización activa. Sin envíos, sin marcar leído, state.json y XLSX intactos.
- Próximo paso: autorización de autenticación en CRM con credenciales del servicio obtenidas desde Railway en memoria; consultar API directamente sin abrir chats en UI (abrirlos marca leído). No enviar ni activar automatización en este paso.

## CRM — lectura completada; reemplaza bloqueos anteriores
- Login y lectura API exitosos: 25 clínicas, 140 mensajes. Último mensaje registrado: 19-oct-2026 14:27:55 America/Bogota; no prueba ausencia de mensajes fuera del CRM.
- Todos los hilos son auditorías como paciente; ninguna conversación comercial Loovo verificada. Preguntas abiertas: MP Demo Medical, Estetica Norte, FullDemo, REAL, Lina Caballero, Aurea y Villa. No equivalen a intención de compra.
- REAL, Sonríe, Lina y Balance ya recibieron rechazo de disponibilidad; no hay reservas confirmadas probadas. No repetir petición de liberar citas.
- 25 contactos con handler=human y cero respuestas IA registradas. Fuente local del webhook Evolution registra mensajes, no autoresponde; versión desplegada exacta no cotejada.
- Informe definitivo al final de `ventas/pendientes_doctores_2026-10-21.md` (sección Resultado actualizado definitivo). Sin envíos ni marcas de lectura. state.json/XLSX intactos.
- Próxima decisión: cerrar transparentemente la auditoría y abrir contacto comercial como Loovo; no automatizar personaje Daniel ni ofrecer sistemas no probados.

## Nueva propuesta: demo comercial con voz de Monoga
- [ ] Revisar referencia: https://x.com/ftcarpe/status/2110728002040365306?s=20 (lectura web directa HTTP 403; contenido sin verificar).
- [ ] Evaluar https://github.com/debpalash/VoiceStudio para clonar exclusivamente la voz propia de Monoga desde sus videos, autorizado por él. README declara AGPL-3.0 y motores con licencias propias a verificar; CPU posible pero más lento. No instalado, sin descargas de modelos ni generación. No subir muestras a terceros sin permiso.
- [ ] Aclarar qué herramienta/modelo llama Monoga «astra 6.1», elegir oferta y guion factual antes de producir. Motion conceptual no equivale a producto funcionando; entrega y envío todavía no autorizados en detalle.
- Video anterior herk-edit-kit y tablero continúan pausados; no usar Claude ni lanzar editor mientras se resuelven modelo y alcance de esta nueva pieza.

## Trabajo delegado mientras Monoga almuerza
- Solo Codex. Editor anterior y tablero siguen pausados. No compras, despliegues, instalaciones ni nuevas suscripciones.
- Explorador `mvih0deb-4-wdtc`: diagnóstico acotado del plugin Chrome oficial instalado; leer cinco posts X únicamente si la integración soportada funciona. No Playwright, extracción de cookies ni cambios de permisos/configuración.
- Ventas `mvih0mw7-5-kz8j`: preparar `ventas/piloto_comercial_clinicas.md`, máximo tres candidatos, apertura transparente como Loovo y storyboard conceptual. No hay video nuevo listo; no enviar el corte anterior rechazado ni presentar demos como sistemas funcionando.
- La autorización amplia de avanzar no se reporta como envío realizado. Antes de cualquier envío faltan: contexto actualizado, identidad comercial, permiso/canal aplicable, material verificado y prueba real de entrega. Espera 5–10 s es solo ritmo de cola, no protección contra bloqueos.
- No existe bucle permanente verificado: las tareas son de fondo y acotadas; si requieren aprobación o capacidad no disponible, deben devolver un bloqueo preciso.

## Chrome oficial Codex — diagnóstico terminado
- Plugin OpenAI Chrome instalado en `.codex/plugins/cache/openai-bundled/chrome/26.1013.40934/`; documentación requiere API browser-client/REPL. Pi no expone esa API en esta sesión.
- Ninguno de los cinco posts X fue abierto ni verificado. No concluir comparación ni recomendar repos de contenido desconocido.
- Próximo paso: sesión de Codex con herramientas del plugin Chrome expuestas para leer únicamente las cinco URLs ya indicadas. No hace falta reinstalar el plugin según la evidencia actual.
- No se usó Playwright, Claude, métodos alternativos, cambios de permisos ni configuración. Ventas continúa separadamente.

## Piloto comercial — borradores preparados, sin envío
- `ventas/piloto_comercial_clinicas.md`: tres mensajes transparentes solicitando permiso (Aurea, Carolina Mendez, Balance), evidencia y señales negativas por clínica. No son leads comerciales calificados ni venta validada.
- Alcance del piloto es propuesta, no decisión: revisión manual y borradores para recepción. No satisface todavía la automatización solicitada por Monoga; no vender ni mostrar un autorespondedor inexistente. Precio de referencia documental $1.000.000/7 días no validado para este alcance.
- Storyboard conceptual 25 s, rotulado MOCKUP y con datos ficticios, preparado. Voz/video aún no existen. No envíos, operaciones remotas ni cambios a state.json/XLSX.
- Siguiente decisión: validar oferta realmente entregable antes de producir motion o contactar clínicas. Prueba de envío futura con destinatario propio autorizado, no una clínica.

## Piloto de cinco clínicas — AUTORIZADO, ejecución delegada
- Pedido expreso: «Hagamos una prueba con 5 doctores sin enviar un video solo hablando con ellos». Ventas Codex: tarea `mvii6bf9-6-e176`. Candidatos: Aurea, Carolina Mendez, Balance, AURORA y Ricardo Castillo; no sustituir si algún hilo no es elegible.
- Un mensaje transparente como Monoga/Loovo por contacto, aclarando auditoría y pidiendo permiso; no continuar como paciente. Pausa aleatoria 5–10 s, horario de Bogotá, respetar rechazos y guardas del CRM. Sin compras, configuración, despliegues ni autorrespuesta continua.
- Registro/evidencia: `ventas/piloto_envios_5_clinicas.md`. No hay resultado confirmado todavía. Releer registro y CRM antes de reintentar para evitar duplicados.
- Nueva autorización explícita para investigación X: lanzar una sesión Codex CLI desde CMD con el plugin Chrome oficial. Explorador `mvii6t2i-7-k1vl`, un intento acotado, sin Claude/Playwright ni cambios de permisos. Posts y repos siguen sin verificar hasta devolver evidencia.

## ACTUALIZACIÓN: Codex CLI + Chrome SÍ FUNCIONA; reemplaza bloqueo anterior
- El explorador era solo lectura y no podía ejecutar shell. El padre ejecutó `cmd.exe /d /c` con `codex exec -m gpt-6.1-sol -c model_reasoning_effort="low" --sandbox read-only --ephemeral --skip-git-repo-check --color never -`, prompt por stdin. Sin flags que desactiven aprobaciones ni sandbox.
- Exit 0: Codex reportó 8 llamadas al plugin oficial Chrome; leyó los cinco posts. Kin fue leído en traducción española automática, original chino sin leer; repos enlazados allí solo nombres/shortlinks, destinos no resueltos. No afirmar revisión del código de esos ocho repos.
- Post angel 2112899427891323103: enlace en respuesta del autor a https://github.com/affaan-m/ECC (README declara MIT; sistema de harness/skills para desarrollo, no prueba de ingresos).
- Post ftcarpe 2110728002040365306: https://github.com/charlie947/social-media-skills (17 skills públicas; redacción/estilo, investigación y prompts; no clona voz acústica).
- Posts RegalosDigitals y angel 2095849798209286198: guías de coordinación Grok Bots, no enlace de repositorio visible. Recomiendan límites y control humano de acciones importantes.
- Sin instalaciones ni compras. El CLI reportó 77.490 tokens usados; no equivalen a dólares facturados. Evitar sesiones de navegador repetidas/contextos gigantes.
- Piloto cinco clínicas: registro `ventas/piloto_envios_5_clinicas.md` solo borrador; 0 intentos, 0 aceptados y 0 entregados. El agente informó restricción de prioridad mayor de envío manual. No hubo falla de WhatsApp ni se probó elegibilidad; no eludir por otra ruta. Resolver alcance de regla antes de reintentar.
