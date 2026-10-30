# HANDOFF · Loovo — relevo del 2026-10-23 (cierre del día)

Léelo primero, junto con `SHARED_STATE.md`. Cronología completa de estos días: `HANDOFF.pre-compactacion-2026-10-23.md` (copia exacta). Anterior: `HANDOFF.pre-consolidacion-2026-10-21.md`. Sin secretos en este archivo.

## 1. Cómo retomar

**Quién y cómo.** Monoga es el dueño de Loovo y quien sale en cámara. Habla en español de Colombia, quiere respuestas cortas y una pregunta a la vez, y se frustra cuando se afirma algo que no se probó o cuando un trabajo se pierde. Espera autonomía: hacer, medir y reportar; no prometer. Si algo no se pudo oír, ver o probar, decirlo.

**Reglas duras** (`AGENTS.md` raíz): los envíos a pacientes y leads son manuales (única excepción: responder como Loovo a quien ya escribió a Loovo; nunca como el paciente «Daniel»; nunca iniciar llamadas); horario Ley 2300 (L–V 7–19, sáb. 8–15); no inventar datos ni resultados; secretos solo en variables de entorno, jamás en chat o archivos; trabajo remoto solo con autorización explícita de destino, operación y credencial.

**Modelos y herramientas.** Codex por defecto (`gpt-6.1-sol`, `gpt-6-luna`). Claude tiene límite de sesión: `loovo-edicion` usa Opus 5.5 en esfuerzo **medium** (perfil `claude-ahorro` y su archivo en `.pi/agents/`). La memoria Engram no funciona (binario sin `instance-id`): todo se guarda en archivos. La carpeta no es un repositorio Git.

**Lecciones operativas.**
1. Las tareas en segundo plano mueren si se cierra Pi; cada agente guarda un `PROGRESS*.md`.
2. Una sola llamada de bash de más de 30 minutos detiene al agente: usar `nohup` y consultas cortas.
3. Nunca usar un dato de un agente (teléfono, tiempo, cifra) sin comprobarlo en la fuente: esta semana fallaron números de contacto y tiempos de palabras.
4. `python -I` oculta los paquetes del usuario (numpy, rembg, faster_whisper).
5. Con 7,7 GB de RAM, el Chrome abierto del usuario deja sin memoria al render.
6. Un agente que dice «listo» no lo está hasta medir el archivo.

## 2. Ventas — objetivo: primer cliente pagado

- Meta propuesta por Monoga: 5 millones COP en 30 días (no es pronóstico). Ahorros 1.000.000 COP, ingreso de IA 0, sin compras ni pauta aprobadas. El negocio no depende de John (su padre).
- **Auditoría de clínicas (17 de oct.):** 25 contactos y 140 mensajes leídos por la API del CRM (último 19-oct 14:27). Eran consultas como paciente, no interés comercial: 18 respuestas no son 18 compradores. 25 chats en atención humana, 0 respuestas de IA, **0 mensajes comerciales enviados** (el agente de ventas se bloqueó por la regla de envío manual). Informe: `ventas/pendientes_doctores_2026-10-21.md`.
- **Nicho propuesto (pendiente de Monoga): contadores y firmas contables pequeñas.** Primera oferta hipotética: recepción de documentos por WhatsApp a hoja de cálculo con revisión humana (D2), solo si pasa una prueba con 20 facturas anonimizadas (umbral propuesto 90 %, no verificado). Precio sin definir; 1,7M de instalación + 250k al mes es una hipótesis. 3 contratos de 1,7M = 5,1M contratados, pero solo 2,55M en anticipos del 50 %.
- **Lote 1:** 5 contadores con número verificado en su propia página y 1 de reserva, más un mensaje de 58 palabras (una entrevista, no una venta), en `ventas/prospectos/contadores_2026-10-21.md`. Los envía Monoga a mano, L–V de 7:00 a 19:00. Ninguno enviado.
- D1–D3 (sistemas para contadores) son prototipos inactivos, sin probar de punta a punta. **«Estamos probando un agente» no está verificado**; no publicarlo como hecho.
- Cuatro skills propias en `ventas/.claude/skills/` (`loovo-oferta-piloto`, `loovo-prospeccion-transparente`, `loovo-conversacion-venta`, `loovo-aprendizaje-ventas`; copia en `.agents/skills/`). No probadas en una conversación real.
- Otros documentos: `ventas/nichos_prospectos_2026-10-21.md`, `ventas/oferta_unica_2026-10-21.md` (clínicas, ahora descartada como primera apuesta), `ventas/plan_ventas_rumbo_2026-10-21.md`, `ventas/estudio_clinicas.xlsx` (métricas vacías). `ventas/state.json` sigue desactualizado.
- Evolution/CRM: Railway CLI ya autenticado; proyecto `evolution-api-loovo` vinculado en `%TEMP%/rw_evo`. Credenciales solo en memoria. La API del CRM se lee sin marcar chats como leídos; abrir un chat en la interfaz sí los marca. No insistir con SSH (timeout).

## 3. Video VID20261021162958 — PAUSADO (no hay mp4)

Método elegido: `monoga-editor` más los números de `receta-dia1`, con el zoom real del Día 1 (GSAP: punch, push, whip, shake; el alterno 1,0/1,12 de la receta fue rechazado). Seguimiento: `Maquina de redes/odd/tasks/edicion-dia1-vid20261021.md`. Proyecto: `Maquina de redes/canal/2026-10-21_21h/proyecto/`.
- **Hecho y verificado:** corte `build/clean.mp4` (39,64 s); recorte de persona en `build/person/person.webm` (1.189 fotogramas); `motion/` completo (lint 0/0, 11 punch, 2 shake, letras detrás; «IGUAL» omitida porque la cabeza llega a y=308); audio `audio/final_mix.wav` (-14,6 LUFS, pico -2,9 dBFS).
- **Falta:** el render (13 intentos, todos colgados). Chrome headless se cierra por falta de memoria (código 0xe0000008); se atasca en los fotogramas 324 y 211. Para retomar, en orden: cerrar Chrome y otras apps; quitar los `filter: blur` de `motion/index.html` líneas 70–83; probar 720×1280; probar `--docker`. Detalle y comando en `PROGRESS-motion.md`. Después: unir el audio, medir el MP4 (objetivo -14,5 ± 0,3 LUFS, pico ≤ -1,8), portada hacia 12,3–13 s, revisión de fotogramas por Luna (`openai-codex/gpt-6-luna`, su color no es fiable), entregar en `canal/2026-10-21_21h/entregables/` (hoy solo hay un borrador de `descripcion.txt`).
- **Tiempos:** usar `plan/edl.json`, `plan/cues.json` y `plan/words_cut.json`; nunca `build/words_out.json`.
- **Decidir:** la persona en cámara no es Monoga (confirmar de quién es el video); «9 PM» frente a «9 de la noche»; la frase «estamos probando». La voz no se ha oído, solo medido. El caché de HyperFrames ocupa ~10 GB en `%TEMP%`.
- No retomar el método con repositorio externo (descartado y borrado el 21-oct). `canal/2026-10-21_11h/` es el intento rechazado; sigue en disco.

## 4. Instagram

- Módulo `Maquina de redes/instagram/` (reglas en su `AGENTS.md`) y agente `loovo-instagram` (`.pi/agents/`, `gpt-6.1-sol`, esfuerzo medio). Prepara; **no publica** ni maneja credenciales.
- **Hecho (verificado):** inventario de 33 videos (0 listos, 15 por decidir, 18 excluidos); plan de 6 destacadas (La serie, Loovo, El editor, CRM local, Sin humo, Modo demo); 6 conceptos de post; 6 portadas de destacada (1080×1920, sin rótulo, figura de ~540 px) en `destacadas/portadas/`; 3 posts (1080×1350) en `posts/final/`; captions del Día 1 y 2 en `cola.md` (parten de los `Dia-NN/caption.md`). Imágenes por el puente Codex (marca «Eléctrico»: carbón #0B0B0F, azul #2F5BFF, lima #C6FF3D, hueso #F4F2EE; sin rojo; el texto lo compone un script con las fuentes de la marca).
- **Falta:** el Día 3 no tiene caption (`Dia-03/caption.md` dice «Pendiente»); el caption del Día 1 deja pendientes el nombre del evento y el rol de Monoga; elegir versión (Día 1: v4 o v5; Día 2: v10 u otra); ver las piezas en un celular. El marcador de la serie no registra ningún día como publicado.
- Las destacadas se arman con stories ya publicadas; ninguna API ni plataforma revisada las crea.
- **Conectar cuentas** (investigado el 23-oct, nada conectado): la API oficial de Instagram publica imágenes, videos, Reels, carruseles y stories en cuentas profesionales, gratis, sin App Review para la cuenta propia (100 publicaciones por 24 h). Plataformas con MCP y plan gratis: Metricool (1 marca con Instagram y TikTok, 20 publicaciones al mes) y Buffer (3 canales, 10 programadas por canal; MCP gratis, lo que crea el agente queda como borrador). Pi se conecta con `pi mcp add` y `pi mcp login`. Que publiquen en TikTok de forma pública sin auditoría propia es inferencia. Antes de conectar: usuario de TikTok e Instagram, cuántas cuentas, cuenta profesional, y autorización expresa.

## 5. Pi y herramientas

- **`/voice` (dictado local al mantener Espacio):** `.pi/extensions/voice.ts` y `.pi/voice/`; seguimiento en `odd/tasks/pi-voice.md`. **Estado: defecto grave corregido a mano, sin nueva verificación independiente y sin prueba real.** La verificación final (`mvlqzttu-9-bxoc`, 23-oct) dio BLOQUEADO: la variable `handle` nunca se asignaba, así que al soltar Espacio, al perder el foco o a los 60 s se lanzaba un error que cierra Pi entero. Corregido el mismo día: se asigna en el modal y todas las llamadas pasan por `send()`, que atrapa los errores; además, un fallo al detener un proceso ya no impide borrar el audio temporal. Copia anterior en `.pi/voice/voice.ts.bak-2026-10-23`. Pruebas: 20 de 20 (4 nuevas en `wiring.test.mjs`: una guarda estática que falla con el código viejo; `voice.ts` sigue sin ejecutarse en ninguna prueba) y el cargador oficial de Pi lo carga. **Sin verificar:** teclado y micrófono reales, que la terminal avise al soltar la tecla, y otros errores de cableado que solo se verían ejecutándolo. Si hay otro, Pi se cierra: probarlo en una sesión nueva sin trabajo abierto. Para probar: `/reload` (y `/trust` si hace falta), `/voice`; mantener Espacio, soltar para transcribir; Esc cancela. Todo local (ffmpeg y faster-whisper sin red); el texto queda editable y no se envía. Si Pi se cierra o falla, avisar y no insistir.
- **Tablero kanban en Pi:** pausado. `tablero/` (5 archivos) se conserva; `.pi/extensions/tablero.ts` está desactivado.
- **Chrome oficial con Codex:** funciona por `cmd.exe /d /c codex exec -m gpt-6.1-sol -c model_reasoning_effort="low" --sandbox read-only --ephemeral --skip-git-repo-check --color never -` con el prompt por entrada estándar; un agente de solo lectura no puede ejecutarlo.
- **Playwright:** su extensión de Chrome (`mmlmfjhmonkocbjadbfplnigmagldckm`) debe retirarla Monoga a mano desde `chrome://extensions`; no volver a usarla.
- **Skills de video:** se usa `monoga-editor` y `receta-dia1`. `monoga-videos` (creada el 21-oct con el zoom rechazado) NO usar y es candidata a borrarse con permiso de Monoga. `Maquina de redes/odd/lista_skills_a_borrar.OBSOLETA-no-usar.txt` está obsoleta: incluye skills que sí se usan.
- Cambios de configuración: `AGENTS.md` raíz (regla 1 y mapa; respaldos `AGENTS.md.bak-2026-10-21` y `-10-23`) y `~/.pi/gentle-ai/profiles.json` (respaldo `.bak-2026-10-22`).

## 6. Decisiones pendientes de Monoga

1. ¿Contadores como nicho? ¿Envía a mano el lote 1? Precio de la oferta.
2. Usuarios de TikTok e Instagram, cuántas cuentas, si Instagram es profesional, y qué plataforma conectar (Buffer o Metricool).
3. Versión del Día 1 (v4 o v5) y del Día 2; nombre del evento y su rol; caption del Día 3.
4. Video: retomar el render; de quién es la persona en cámara; «9 PM»; la frase «estamos probando».
5. Probar `/voice` y reportar.
6. Borrar `monoga-videos`; retirar la extensión de Playwright.
7. Comprar un micrófono solo después de la primera venta (el audio saturado de los videos fue la falla de fondo).
8. Recordatorios: resultado de la beca de Google/Coursera desde el 26-oct (revisar spam); correo de Carolina para crearle usuario en Odoo; la landing de contadores la hace Monoga.
