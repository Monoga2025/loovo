# Inventario del CRM de Loovo/Monoga (para la serie "Día X de 42")

Fecha de la investigación: 2026-10-09. Solo lectura. No se ejecutó nada, no se abrió la base de datos ni el `.env`.
Marcas: **[HECHO]** lo vi en código/docs; **[SUPUESTO]** lo deduzco y no lo verifiqué.

Rutas base:
- Repo: `C:\Users\you\Desktop\Monoga OS\trabajo\monoga\proyectos\monoga-os` (rama `monoga-event-crm`, 16 commits en total, 13 son de Monoga del 2026-10-05 al 06).
- Docs del sprint: `C:\Users\you\Desktop\Monoga OS\docs\` (sobre todo `MORNING_BRIEF.md`, `overnight-2026-10-06\QA_REPORT.md`, `SALES_KIT.md`, `NEXT_ACTIONS_DANIEL.md`).

## 0. Hallazgo que cambia lo que se puede decir en cámara

1. **El CRM es un fork del CRM open source "Comp AI CRM" (trycompai/crm, licencia MIT)** [HECHO: `README.md`, `CHANGELOG.md` apunta a github.com/trycompai/crm, versión 1.15.3]. Lo propio de Monoga son ~13 commits: campos de lead, moneda COP, etapas en español, seed demo, y la página "Capturar lead". Decir "construí un CRM desde cero" no es verificable. Decir "tomé un CRM open source y lo adapté a ventas por eventos en Colombia" sí lo es.
2. **El "agente" de la página Capturar lead NO es un LLM: es un motor de reglas con expresiones regulares** (`apps/app/lib/lead-intake.ts`, 744 líneas). Lo confirman `MORNING_BRIEF.md` sección C ("hoy es un motor de reglas") y `QA_REPORT.md`. El agente LLM real existe en `apps/agent` pero es el de investigación/enriquecimiento heredado del fork, y localmente está apagado.
3. **Nada de WhatsApp, DIAN/factura electrónica, cotizaciones ni cartera existe en el código** [HECHO: grep sin resultados en `apps/`, `packages/` fuera de textos de ejemplo del seed y la UI]. Solo hay un campo manual "Payment status".
4. **No está desplegado.** Todo corre en `127.0.0.1`. No hay ninguna referencia a Railway en el repo del CRM (Railway aparece solo en el `HANDOFF.md` de Jarvis/Telegram, otro proyecto) [HECHO].
5. El CRM remoto antiguo "Twenty" (`crm.grupomonoga.com`) sigue existiendo y hay que exportarlo antes de apagarlo (`NEXT_ACTIONS_DANIEL.md` sección 2).

## 1. Qué es el CRM en 5 líneas

1. Monorepo con Bun 1.3.12 + Turborepo; Node >= 22; base PostgreSQL con Prisma [HECHO: `package.json`, `packages/db`].
2. Tres apps: `apps/app` (Next.js, la interfaz), `apps/api` (NestJS + tRPC, puerto 3101) y `apps/agent` (framework "eve" de Vercel, el agente de investigación y los agentes personalizados). Paquetes: `auth` (Better Auth), `db`, `env`, `telemetry`, `ui`, `validation`, `typescript-config`.
3. Corre en local: PostgreSQL + API en 127.0.0.1:3101 + App en 127.0.0.1:3100. Dos formas de encender: `tools\monoga\start.ps1` (real) o `start.ps1 -Demo` (datos sintéticos); y `Desktop\CRM.bat` (menú Encender/Apagar).
4. **Ojo, `CRM.bat` difiere del runbook**: usa Postgres portable en `C:\Users\you\crm-pg` (sin Docker), puerto de la app 3000, abre `/api/dev-login`, pregunta si inicia el agente (~2 GB de RAM) y NO tiene modo demo. El runbook (`docs/monoga-local-runbook.md`) usa Docker, puerto 3100 y dice que el 3000 pertenece a otro proceso. Hay que decidir cuál es el oficial antes de grabar [HECHO: `CRM.bat`, runbook].
5. Modelo del agente: por defecto `zai/glm-5.2-fast` vía AI Gateway; en desarrollo se puede usar ChatGPT/Codex con `AGENT_USE_CODEX=1` (archivo `apps/agent/agent/lib/codex-model.ts`, aún sin commit). `git status` del repo muestra cambios sin commit en `agent.ts`, `package.json`, `turbo.json`, `bun.lock`, `.env.example` [HECHO].

## 2. Tabla de funciones

Leyenda de estado: **A** hecho y probado / **B** existe en código sin probar (por mí; heredado del fork o sin evidencia de uso) / **C** a medias / **D** solo planeado o inexistente.
"Probado" = hay tests automáticos o un QA documentado, no que yo lo haya corrido.

| Función | Estado | Evidencia | ¿Se ve bien en cámara? |
|---|---|---|---|
| Pipeline de ventas con etapas en español (Nuevo lead, Contactado, Calificado, Propuesta, Ganado, Perdido, No encaja) | A | commit `442178c`; mapa en `docs/monoga-event-workflow.md`; QA final lo vio en UI. Pega: las etapas internas siguen con nombres del fork (`DEMO_BOOKED`=Nuevo lead) y los leads sin calificar caen en `DEMO_BOOKED` | Sí: tabla de deals con etapas y monto en COP. Evitar mostrar la ficha del deal con "Closed" de OENYX (fecha falsa) |
| Contactos y empresas (lista, ficha, asociaciones, campos propios) | A (heredado, con tests) | `apps/app/app/(app)/[slug]/companies`, `contacts`; `apps/api/test/*`; campos Monoga en `packages/db/src/monoga-event-fields.ts` | Sí con datos demo; no con la base real |
| Campos de lead (fuente, evento, dolor, nivel de interés, próxima acción, fecha de seguimiento, estado de pago) | A | commit `ab2f6eb`, `1efb3f9`; `docs/monoga-event-workflow.md`; test `monoga-event-fields.spec.ts` | Sí |
| Consentimiento (estado, método, fecha) para Habeas Data | A | `docs/monoga-event-workflow.md` sección Consent; `lead-intake.ts` | Sí, buen tema para empresarios (Ley 1581) |
| Moneda COP y reportes en pesos; dashboard | A | commit `49db84b`; `packages/db/src/currency.ts`; test `currency-totals.integration.spec.ts`; commit `14086b3` (formato es-CO) | Sí: "$ 1,2 M" en el panel |
| Panel "Follow-ups" (tareas abiertas por fecha de vencimiento) | A | commit `757fe31` | Sí, muy visual |
| **Capturar lead** (`/monoga/capture`): escribes una nota o mensaje entrante y devuelve persona, empresa, dolor, presupuesto, interés, consentimiento, borrador de respuesta; crea empresa+contacto+deal+nota+tarea | A como motor de reglas; D como IA | commits `98a62b5`, `ab12040`, `f4aeb08`, `ae0a77b`, `c20309a`; `apps/app/lib/lead-intake.ts`; `capture-agent.tsx` (704 líneas); tests `lead-intake.spec.ts`; QA en `QA_REPORT.md` | Sí, es la mejor pantalla. **No decir "IA" ni "entendió"**: es reglas. Fallos conocidos aún: "Pedro Gómez, CEO de Tecnoplast Ltda" toma el cargo como empresa; apellidos compuestos ("de la Cruz"); empresas sin SAS/Ltda; si un espectador escribe libre puede fallar en vivo |
| Borrador de respuesta + escalamiento de quejas a persona (sin envío) | A (reglas) | commit `ab12040`; `QA_REPORT.md` "inbound draft + escalation works on the 3 scripted inputs" | Sí. Solo registra el borrador, no lo envía |
| No registrar a quien pidió no ser contactado (opt-out) | A | commit `c20309a`; QA final: botón crear bloqueado | Sí, buen momento de "hacerlo bien" |
| **Modo demo / datos semilla** | A | commit `baae2e0`; `packages/db/prisma/monoga-demo-pipeline.ts` (9 deals sintéticos, empresas con "Demo" en el nombre); `monoga-seed.ts` (`--demo-pipeline`, `--with-demo-lead`); `tools/monoga/start.ps1 -Demo`; se niega a correr en una base cuyo nombre no termine en `_demo`; test `monoga-demo-pipeline.spec.ts` | Sí. Los nombres dicen "Demo SAS": honesto y seguro en cámara |
| Agente de investigación/enriquecimiento (logo, descripción, redes, historial laboral, brief) | B (heredado, localmente apagado) | `apps/agent/agent/tools/*` (enrich_company, research_person, find_contact_socials, get_linkedin_profile, write_brief, record_fact, set_field_value, search_crm, list_deals, schedule_recheck, etc.); `apps/agent/test/*` (30+ specs); `docs/agent.md`. Necesita claves externas (Context, Perplexity, Blob). Runbook: "el agente de investigación no corre local" | Parcial. Con claves podría verse bien (la ficha se llena sola) pero la regla del repo es "no se adivina nada" y exige claves de terceros |
| Constructor de agentes por chat ("describe un agente en una frase", disparadores MANUAL/SCHEDULE/EVENT/WEBHOOK) | B (heredado) | rutas `agents`, `chat`; `apps/agent/agent/subagents/agent_builder`; `apps/api/src/agent/agents.contracts.ts`; test `apps/agent/evals/agent-builder.eval.ts` | **Es la función más cercana a "agente de IA que ejecuta acciones".** Un agente creado puede: leer el CRM (`query_crm`, `read_crm_record`), **crear actividades/notas/tareas** (`create_crm_activity`), **publicar en Slack** (`post_slack_message`), buscar en la web (`web_search`, `web_fetch`), hacer preguntas (`ask_question`) [HECHO: `subagents/agent_runner/tools`]. Nunca lo vi probado por Monoga. Riesgo alto |
| Modelo del agente: `zai/glm-5.2-fast` por defecto; Codex/ChatGPT solo en dev con `AGENT_USE_CODEX=1` | B | `packages/db/src/settings.ts:10`; `apps/agent/agent/lib/codex-model.ts`; `.env.example` líneas 163-170. Sin commit aún | Mostrar solo si funciona. El modelo se elige en un ajuste de la base de datos |
| Correos: Gmail y Calendar (sincronizar, enviar) | B (heredado, requiere OAuth de Google Cloud) | `apps/api/src/google/gmail-sync.service.ts`, `calendar-sync.service.ts`, `gmail-mime.ts`; `docs/plan/gmail-calendar-plan.md`; pantalla `settings/connections/google` | Cuidado: el runbook dice NO configurar Google (modo "sin integraciones"). Mostraría correos reales |
| Outlook/Microsoft | B (heredado) | `apps/api/src/microsoft`, `settings/connections/microsoft` | Mismo cuidado |
| Slack (leer/publicar, personas) | B (heredado) | `apps/api/src/slack`, `settings/connections/slack`; `docs/connections.md` | Sí si se crea un Slack de pruebas |
| Endpoint de entrada de leads ("intake") y script de seguimiento web (tracking) | B (heredado) | `settings/connections/intake`, `settings/tracking`; `docs/tracking.md`; `apps/api/src/tracking` | **Es el gancho para WhatsApp/formulario**: un webhook que crea el lead. No lo vi probado |
| **WhatsApp** | D | Sin código. `MORNING_BRIEF.md` C: "no prometer conexión a WhatsApp"; sección E lo describe como MVP "no implementado" (proveedor oficial de WhatsApp Business, costo estimado USD 0-50/mes) | No existe |
| **Automatizaciones** (workflows, secuencias) | C | `docs/crm-plan.md` sección 15 deja fuera "sequences and workflow automation". Lo único automático: los agentes personalizados con disparador programado/evento y el tick cada minuto de `apps/agent/agent/schedules/dispatch.ts` | Solo vía agentes personalizados |
| **Facturación / DIAN** | D | Sin código ni proveedor nombrado en el repo. Solo el campo manual `Payment status` (Invoice pending / Invoice sent / Payment confirmed) y la nota "El CRM nunca envía la factura". `MORNING_BRIEF.md` G: falta "proveedor de facturación electrónica que usa Monoga" | El campo sí se ve; DIAN no existe |
| **Cotizaciones y su seguimiento** | D | Sin código. La etapa "Propuesta" (`CONTRACT_SENT`) y las tareas manuales son lo más cercano | Etapa visible; la función no existe |
| **Cartera (cuentas por cobrar)** | D | Sin código. Cercano: `Payment status` + tareas. En el demo hay un dolor de ejemplo "cartera" solo en texto | No existe |
| Reportes | C | Dashboard: pipeline por etapa, cierres, tareas vencidas, actividad reciente; reporte en COP. Sin reportes semanales (`MORNING_BRIEF.md` C lo marca "no prometer") | Dashboard sí |
| Importar HubSpot CSV | D | Planeado en `crm-plan.md` Fase 10; no vi código en `apps/api/src` | No |
| Despliegue (Railway/VPS) | D | Sin Dockerfile de la app ni config Railway. Existe `apps/api/vercel.json` heredado. `NEXT_ACTIONS_DANIEL.md` sección 3: "Hosting del CRM con copias de seguridad" pendiente | No existe |
| Inicio de sesión local de un clic (`/api/dev-login`) | A | commit `9b19250`; variable `DEV_LOGIN_EMAIL` | Sí, evita mostrar claves |

Pruebas automáticas reportadas al cierre del sprint (`MORNING_BRIEF.md`): 199 de la app, 22 de db, 16 de integración API, typecheck limpio. No las corrí.

## 3. Roadmap y pendientes encontrados

De `MORNING_BRIEF.md`, `NEXT_ACTIONS_DANIEL.md`, `QA_REPORT.md`, `docs/`:

- Cobrar OENYX: pedir razón social/NIT/dirección/correo, emitir factura electrónica, marcar "Payment confirmed". Falta definir qué proveedor de factura electrónica usa Monoga.
- Corregir la fecha de cierre de OENYX en la ficha ("Closed 5 de oct" es la fecha de carga, produce "win rate 100% / ciclo 0 días").
- Exportar los prospectos del CRM Twenty remoto (`crm.grupomonoga.com`) y decidir un solo sistema (el local).
- Ensayar la demo dos veces con `start.ps1 -Demo`; fijar precio del piloto (hipótesis 1,5 a 2,5 M COP; operación 0,6 a 1,2 M COP/mes).
- Corregir la web: quitar "En producción", "100%", "<1.5 s", "99.98%", "40%" (`WEBSITE_CLAIMS_FIX.md`).
- Confirmar con el organizador si hay stand/contacto con asistentes; revisión corta de Habeas Data.
- Piloto pagado Lead Desk (no implementado): entrada WhatsApp o formulario -> CRM; análisis con LLM con respaldo de reglas; bandeja de aprobación antes de enviar; escalamiento; consentimiento/opt-out; métricas (tiempo a primera respuesta); deduplicar por teléfono/correo; hosting (VPS, HTTPS, backups); proveedor de LLM con clave de Monoga.
- Pendientes técnicos del QA (SHOULD FIX): cargo capturado como empresa, apellidos compuestos, empresas sin sufijo, "Dr." como nombre, etapa `DEMO_BOOKED` para no calificados, quejas que se vuelven deals, dedupe de contactos, la línea "No contactar... el 2026-10-19" aún muestra fecha.
- Plan heredado del fork sin construir: HubSpot import, vistas guardadas, tablero kanban, deal intelligence (`docs/crm-plan.md`, fases 10 y 11); Gmail/Calendar (`docs/plan/gmail-calendar-plan.md`); list-building (`docs/list-building-roadmap.md`).
- `openspec/` de Monoga OS: solo existe `changes/archive`, `specs` vacío. No hay roadmap ahí [HECHO].
- Sin `TODO`/`FIXME` relevantes en el código propio (el grep no devolvió archivos).
- Cambios sin commit: integración Codex en `apps/agent` (ver arriba).

## 4. Propuesta: 30 sesiones grabables para 35 días

Supuestos de la propuesta: 1 sesión por día aprox. con 5 días de colchón; el usuario trabaja con un asistente de código; el LLM será el que Daniel elija (OpenAI vía `OPENAI_API_KEY` ya existe como variable de entorno, según CLAUDE.md de la serie); los nombres de proveedores DIAN no aparecen en el repo, así que en la sesión 17 se investigan desde cero y todo lo que ahí diga es **[SUPUESTO]**.
Duración entre paréntesis. Riesgo: A/M/B = alto/medio/bajo.

Semana 1: base y demo seguro
1. **Encender y recorrer el CRM real vs demo** (1 h). Probar `start.ps1 -Demo` y `CRM.bat`, decidir cuál es el oficial y unificar puertos. Visible: el CRM demo abierto con 9 deals en 30 s. Riesgo B. Dep.: Docker o Postgres portable.
2. **Botón único "Modo demo"** (2 h). Un `.bat`/atajo que apaga el real, levanta `crm_demo` y pone un banner "DEMO". Visible: banner rojo "DATOS DE PRUEBA" en la barra. Riesgo M. Dep.: 1.
3. **Reiniciar el demo en un clic** (1,5 h). Script que borra y vuelve a sembrar `crm_demo`. Visible: pipeline vuelve a su estado inicial. Riesgo B. Dep.: 2.
4. **Ampliar los datos ficticios** (2 h). Más deals, cotizaciones y cobros ficticios, sin tocar el real. Visible: dashboard con cifras redondas en COP. Riesgo B. Dep.: 3.
5. **Pasar a español la interfaz** (3 h). Navegación y rótulos aún en inglés ("Qualified", "Won", "Capture"). Visible: pantalla toda en español. Riesgo M (hereda 1000+ textos del fork). Dep.: 1.
6. **Arreglar los fallos del QA de Capturar lead** (3 h). Cargo vs empresa, apellidos compuestos, "800 mil", empresas sin sufijo. Visible: 20 mensajes de prueba antes/después. Riesgo B. Dep.: 1.
7. **Revisión de datos reales en pantalla** (1 h). Lista de qué mostrar y qué ocultar; la base real solo tiene OENYX. Visible: checklist pegada en el monitor. Riesgo B. Dep.: 1.

Semana 2: el agente de verdad
8. **Conectar un LLM real al agente** (3 h). Probar `AGENT_USE_CODEX=1` o clave de OpenAI y ver si `apps/agent` arranca sin errores (necesita ~2 GB RAM). Visible: el agente responde una pregunta sobre un deal. Riesgo A (cambios sin commit, dependencias de eve, AI Gateway). Dep.: 1.
9. **Probar el agente de punta a punta con el constructor** (3 h). Crear por chat un agente "avisa cuando un deal lleva 3 días sin respuesta". Visible: una tarea creada sola en el CRM. Riesgo A. Dep.: 8.
10. **Agente que crea notas y tareas** (2 h). Usar `create_crm_activity` y `query_crm`. Visible: nota nueva con firma del agente en la ficha. Riesgo M. Dep.: 9.
11. **Capturar lead con LLM + respaldo de reglas** (4 h). El LLM extrae, las reglas validan; si falla, reglas. Visible: mensaje desordenado que antes fallaba, ahora bien. Riesgo M. Dep.: 6 y 8.
12. **Bandeja de aprobación de borradores** (4 h). Aprobar/editar antes de "enviar". Visible: botón Aprobar. Riesgo M. Dep.: 11.
13. **Dedupe por teléfono y correo** (2 h). Visible: el segundo mensaje de la misma persona se une al contacto. Riesgo B. Dep.: 6.
14. **Seguimiento automático de leads fríos** (3 h). Agente programado diario que crea tareas. Visible: panel Follow-ups lleno al amanecer. Riesgo M. Dep.: 9.

Semana 3: canales (WhatsApp) e ingresos
15. **Webhook de entrada de leads (intake)** (3 h). Probar `settings/connections/intake` con un formulario. Visible: enviar el formulario y ver el lead aparecer. Riesgo M. Dep.: 1.
16. **Elegir proveedor de WhatsApp Business** (2 h). Investigación y decisión de costo; no hay código. Visible: tabla comparativa. Riesgo B. Dep.: ninguna.
17. **Recibir un WhatsApp en el CRM** (4 h). Webhook del proveedor -> intake -> Capturar lead. Visible: escribir desde el celular y ver el lead. Riesgo A (verificación de Meta, número, plantillas) [SUPUESTO]. Dep.: 15, 16.
18. **El agente redacta la respuesta de WhatsApp (con aprobación)** (4 h). Visible: borrador listo en 5 s tras el mensaje. Riesgo A. Dep.: 12, 17.
19. **Enviar la respuesta aprobada por WhatsApp** (3 h). Visible: respuesta llega al celular. Riesgo A (ventana de 24 h, plantillas) [SUPUESTO]. Dep.: 18.
20. **Escalamiento de quejas y opt-out en WhatsApp** (2 h). Visible: "no me escriban más" -> sin deal y marca de no contactar. Riesgo M. Dep.: 17.

Semana 4: cobrar y vender
21. **Cotizaciones: etapa Propuesta con monto y vencimiento** (3 h). Campos de cotización y fecha de validez. Visible: lista de cotizaciones por vencer. Riesgo B. Dep.: 4.
22. **Seguimiento de cotizaciones** (3 h). Agente que crea tarea 2 días después de enviar una cotización y redacta el recordatorio. Visible: tarea "recordar cotización a Ferretería Demo". Riesgo M. Dep.: 14, 21.
23. **Cartera: facturas pendientes y días de atraso** (3 h). Campos de factura (número, valor, vencimiento) y vista "Cartera". Visible: tabla con barras de atraso. Riesgo M. Dep.: 4.
24. **Recordatorio de cobro con aprobación** (3 h). Visible: borrador de cobro amable listo. Riesgo M. Dep.: 12, 23.
25. **Investigar facturación electrónica DIAN** (2 h). Proveedores colombianos con API (nombrarlos solo si se verifican; el repo no nombra ninguno [HECHO]); costo, ambiente de pruebas, habilitación DIAN. Visible: tabla de 3 opciones. Riesgo B. Dep.: ninguna.
26. **Emitir una factura de prueba (habilitación)** (4 h). Conectar el CRM al ambiente de pruebas del proveedor elegido y emitir una factura ficticia. Visible: PDF/XML de prueba generado desde un deal Ganado. Riesgo A (habilitación y resolución DIAN pueden tardar días) [SUPUESTO]. Dep.: 25. Si no sale, se graba como "lo que falló".
27. **Reporte semanal automático** (3 h). Resumen por correo o pantalla: leads nuevos, cotizaciones, cartera. Visible: resumen de 5 líneas. Riesgo M. Dep.: 22, 23.

Semana 5: despliegue y evento
28. **Desplegar el CRM en Railway** (4 h). Postgres + API + app en la nube con HTTPS y variables sin exponer claves. Visible: URL pública con el demo. Riesgo A (el repo no tiene Dockerfile ni config; monorepo con tres apps; migraciones; cookies/CORS; `ALLOWED_SIGN_IN`) [SUPUESTO]. Dep.: 2. Alternativa: dejar solo el demo en la nube.
29. **Copias de seguridad y usuario de demo para el evento** (2 h). Respaldo diario y usuario de solo lectura. Visible: restaurar un respaldo en 1 min. Riesgo M. Dep.: 28.
30. **Ensayo de la demo de 3 minutos** (2 h). Guion de `SALES_KIT.md`, dos ensayos con cronómetro, con el celular a mano para WhatsApp. Visible: demo completa en 3:00. Riesgo M. Dep.: 11, 18, 2.
31. **Plan B sin internet para el evento** (2 h). Todo local, demo cargada, video de respaldo. Visible: laptop en modo avión corriendo la demo. Riesgo B. Dep.: 3.
32. **Captura de leads en el stand** (3 h). Formulario/QR que crea el lead con consentimiento (Habeas Data). Visible: escanear un QR y ver el lead entrar. Riesgo M. Dep.: 15, 20.

Orden sugerido si falla algo: el núcleo imprescindible para el evento es 1-7, 11, 12, 30, 31. WhatsApp (17-19), DIAN (26) y Railway (28) son las tres apuestas de mayor riesgo; conviene intercalarlas con sesiones fáciles para que cada semana haya algo que mostrar.

## 5. Riesgos para grabar

1. **Datos reales en pantalla.** La base `crm` tiene datos reales (OENYX: empresa y contacto "Sebastián"; sin teléfono/correo según QA). Grabar siempre con `-Demo`. `CRM.bat` NO tiene modo demo y abre la base real [HECHO]. Los correos de Gmail/Outlook, si se conectan, muestran correos reales.
2. **Datos reales en archivos.** `HANDOFF.md` (Monoga OS) y `HANDOFF_2026-10-01.md` contienen nombre, correo y teléfono personales y de terceros; no abrirlos en cámara. `docs/overnight-2026-10-06/PROSPECT_RESEARCH.*` e `ICP2_TARGETS.*` listan empresas reales de Santander.
3. **Claves.** Hay un `.env` en la raíz del repo (existe; no lo abrí). Hay también trazas y snapshots del agente en `apps/agent/.eve/` que pueden contener datos; no mostrarlos. Mostrar `.env` o la terminal con `echo $env:OPENAI_API_KEY` está prohibido. Usar `.env.example` para explicar.
4. **Afirmaciones en cámara.** No decir: "IA que entiende" para Capturar lead (es reglas), "WhatsApp conectado", "en producción", "factura electrónica automática", ni casos de éxito con nombre (OENYX, RFI) sin permiso escrito. Es el propio `MORNING_BRIEF.md` sección C. Decir "fork de un CRM open source" cuando se pregunte de dónde viene.
5. **Tiempos de compilación.** Next en modo dev compila cada ruta la primera vez (30 s al arrancar, según el runbook; más en la primera visita a cada página); `CRM.bat` usa `next dev --webpack`, más lento. El agente consume ~2 GB de RAM. Precalentar todas las rutas antes de grabar y cortar la espera en edición. `bun install`/primer arranque puede tardar varios minutos [SUPUESTO].
6. **Dependencias externas que fallan en vivo.** AI Gateway/ChatGPT (cuota, red), Meta/WhatsApp (verificación, plantillas), DIAN (habilitación). Grabar cada intento; el fallo también es contenido.
7. **Conflicto de puertos.** El runbook reserva el 3000 para otro proceso; `CRM.bat` lo usa y mata lo que escuche en 3000, 3101 y 2000 (`Stop-Process -Force`). Cuidado si hay otro servicio importante en esos puertos.
8. **El repo tiene cambios sin commit** (Codex). Antes de grabar sesiones que cambien código, hacer commit del estado actual o se mezclará con el trabajo del día.
9. **Fecha falsa de OENYX** en la ficha ("Closed 5 de oct") y el "win rate 100%". No mostrar esa ficha ni el KPI.
10. **Datos demo duplicados.** El QA encontró contactos demo archivados que aún aparecían en el feed de actividad; verificar en el demo antes de grabar.

## Problemas

1. El CRM es un fork de Comp AI CRM y el "agente" de Capturar lead no es IA: no se puede decir en cámara que lo construiste de cero ni que "entiende". Arreglo: decir "adapté un CRM open source" y "motor de reglas, el modelo viene después"; o hacer primero la sesión 11.
2. `CRM.bat` y el runbook se contradicen (puerto 3000 vs 3100, Postgres portable vs Docker, sin demo). Arreglo: sesión 1 y 2.
3. WhatsApp, DIAN, cotizaciones, cartera y despliegue no existen en el código. Arreglo: sesiones 15 a 28; marcar como "próximamente" en `hechos.md`.
4. Hay cambios sin commit en `apps/agent` (Codex). Arreglo: commit o stash antes de la primera sesión.
5. La base real contiene un cliente real (OENYX). Arreglo: grabar siempre con `-Demo` y un banner de "DATOS DE PRUEBA".
6. Hay un `.env` con secretos en `monoga-os\.env`. Arreglo: no abrirlo en cámara; usar `.env.example`.
7. No verifiqué que nada corra: todo "A" se basa en tests y QA documentados por otros agentes. Arreglo: la sesión 1 debe ser arrancar y comprobar.
