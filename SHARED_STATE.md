# ESTADO GLOBAL COMPARTIDO DE LOOVO (SHARED_STATE)

## Resumen vigente — 2026-10-23 (relevo compactado: `HANDOFF.md`; los puntos 1-10 siguen vigentes salvo lo que el HANDOFF actualice)
1. Objetivo principal: primer cliente pagado; meta propuesta 5M COP/30 días, no pronóstico. Sin compras ni pauta aprobadas; Codex, no Claude.
2. Canal base propuesto: venta digital Monoga/Loovo, demo real y cierre remoto; negocio no depende de John. Oferta propuesta (pendiente de confirmar por Monoga): diagnóstico de atención por WhatsApp para clínicas, precio hipótesis $300.000 COP; ver `ventas/oferta_unica_2026-10-21.md`.
3. CRM: 25 clínicas, 140 mensajes; hilos de auditoría como paciente, cero interés comercial Loovo confirmado. 18 respuestas ≠ compradores.
4. Siete preguntas abiertas; REAL/Sonríe/Lina/Balance declinaron disponibilidad; reservas no confirmadas. Handler humano 25/25, cero respuestas IA.
5. Piloto cinco clínicas autorizado, pero 0 intentos/aceptados/entregados por conflicto con envío manual; elegibilidad actual no verificada.
6. D1-D3 prototipos inactivos, sin runtime E2E probado. `state.json` desfasado; métricas XLSX vacías.
7. Editor y tablero Pi pausados; no activar ni borrar skills. Sin demo audiovisual nueva verificada.
8. Chrome oficial funciona por Codex CLI/CMD read-only; cinco posts X leídos con límites detallados en HANDOFF.
9. Instagram (2026-10-23): módulo `Maquina de redes/instagram/` y agente `loovo-instagram` creados para republicar lo de TikTok, armar destacadas y generar posts con imágenes de IA vía Codex. No publica; falta el usuario de TikTok e Instagram de Monoga. Detalle en `HANDOFF.md`.
10. Los snapshots y estados de abajo son históricos y pueden estar obsoletos; ante contradicción prevalece este resumen y el HANDOFF vigente, no reescribir el archivo histórico.

> **Regla de oro inter-agentes**: Este archivo es el punto de verdad y sincronización entre módulos, sin importar qué agente trabaje (Pi, Claude Code, Codex o Gemini). Reglas de uso: `AGENTS.md`, sección "Handoff y memoria".
> 1. `ventas-redes` (`Maquina de redes/`): Producción de contenido orgánico, viralidad, hooks, guiones, portadas y campañas.
> 2. `ventas`: Listas de prospectos, secuencias WhatsApp / Evolution API, auditorías y reactivación.
> 3. `servicios/omni-sales-crm`: Motor omnicanal, webhooks de entrada, automatización de DMs, estados de leads y pipeline.

---
## 0. Estado operativo real (2026-10-17, orquestador)

Relevo completo con checks: `HANDOFF.md` (raíz).

| Pieza | Estado | Evidencia / pendiente |
|---|---|---|
| Embudo CRM D1/D2/D3 (`omni-sales-crm`) | 🟡 Listo solo para DM/chat web; los comentarios de Instagram NO disparan | 169/169 tests. Faltan `CONTADORES_LINK_D1/D2/D3` en `.env`. |
| Flujos n8n D1, D2 y D3 | 🟡 En construcción sobre plantillas base | Base y brechas en `servicios/Agentes de IA/contadores-d1-d2-d3/REPORTE.md`. Ninguno importado ni probado en n8n. |
| Odoo (odoo.grupomonoga.com) | 🟢 Proyecto "Guiones" (Kanban: Idea, Guion listo, Grabado, Editado, Publicado) con 6 guiones de Contadores | Carolina aún no es usuario de Odoo: su tarea lleva la etiqueta Carolina. Los guiones viven en Odoo. |
| n8n (Railway) | 🟡 D1, D2 y D3 importados INACTIVOS | Faltan credenciales, UVT 2026 y pruebas reales. |
| Video Campaña Contadores 01 | 🟡 En pre-producción | Solo `Maquina de redes/odd/campana-contadores-01/produccion_config.py`. No publicar hasta que D1/D2/D3 estén probados. |
---

## 1. Campañas Activas y Triggers de Entrada

| Campaña | Disparador (Palabra clave) | Destino / Embudo | Responsable Inbound | Estado |
|---|---|---|---|---|
| **Contadores Colombia 01 (Crisis 2030)** | `D1` | Entrega de Guía / Demostración Sistema 1 (Agente Tributario DIAN + Exógena en 3s) | `omni-sales-crm` / `ventas` | 🟡 Embudo CRM (solo DM/chat, no comentarios) · 🟡 Flujo n8n en construcción |
| **Contadores Colombia 01 (Crisis 2030)** | `D2` | Entrega de Sistema 1 + Sistema 2 (Extractor Tirillas/Facturas WhatsApp a Excel/Siigo) | `omni-sales-crm` / `ventas` | 🟡 Embudo CRM (solo DM/chat, no comentarios) · 🟡 Flujo n8n en construcción |
| **Contadores Colombia 01 (Crisis 2030)** | `D3` | Oferta VIP: Pack Completo (3 Sistemas: DIAN + Extractor + Conciliador Bancario) + Auditoría Despacho | `omni-sales-crm` / `ventas` | 🟡 Embudo CRM (solo DM/chat, no comentarios) · 🟡 Flujo n8n en construcción |

---

## 2. Definición Técnica de Disparadores para `omni-sales-crm`

### Disparador: `D1`
- **Mensaje Usuario:** "D1" o contiene "D1"
- **Respuesta Automática Inmediata (Instagram DM / TikTok):**
  > *"¡Hola colega! 📊 Aquí tienes el acceso al **Sistema 1 (Agente Estatuto Tributario & DIAN)** entrenado con conceptos vigentes 2026. Te responde artículos y cálculos de exógena en 3 segundos: [LINK_SISTEMA_1]. ¿Manejas clientes personas naturales o jurídicas principalmente?"*
- **Tag en CRM:** `lead-contador-d1`, `interes-agente-tributario`
- **Etapa Pipeline:** `Interesado - Sistema DIAN`

### Disparador: `D2`
- **Mensaje Usuario:** "D2" o contiene "D2"
- **Respuesta Automática Inmediata (Instagram DM / TikTok):**
  > *"¡Buenísimo! 🚀 Te preparé el acceso a los **2 Sistemas**: 1️⃣ El Agente Tributario DIAN y 2️⃣ El Extractor Inteligente de Tirillas y WhatsApp a Excel para Siigo/Alegra. Descárgalos aquí: [LINK_SISTEMAS_D2]. ¿Actualmente digitas facturas a mano en tu despacho?"*
- **Tag en CRM:** `lead-contador-d2`, `dolor-digitacion`
- **Etapa Pipeline:** `Interesado - Automatización Extractor`

### Disparador: `D3`
- **Mensaje Usuario:** "D3" o contiene "D3"
- **Respuesta Automática Inmediata (Instagram DM / TikTok):**
  > *"¡Excelente jugada! ⚡ Quieres el despacho en piloto automático completo: 1️⃣ Agente DIAN, 2️⃣ Extractor de Facturas/Tirillas a Excel y 3️⃣ Conciliador Bancario Automático (Bancolombia/Davivienda). Aquí tienes el paquete completo: [LINK_SISTEMAS_D3]. Además, como pediste los 3, ¿quieres que agendemos 15 min y te muestro cómo conectarlo a tu Siigo/Alegra en vivo?"*
- **Tag en CRM:** `lead-contador-d3`, `alta-intencion-compra`
- **Etapa Pipeline:** `Lead Calificado - Propuesta Despacho 3 Sistemas`

---

## 2.1 `omni-sales-crm` (2026-10-17)

- **Estado:** embudo D1/D2/D3 listo y probado (169/169 tests). Detecta la clave en DM/chat web, etiqueta `embudo-contadores`, sube score, mueve de etapa y responde en 2 burbujas. Clínicas intacto.
- **Etapas reales (fuente de verdad):** D1 → `Contadores · Interesado DIAN` (35) · D2 → `Contadores · Interesado Extractor` (50) · D3 → `Contadores · Cierre / Demo` (75, `lead-caliente`).
- **Archivos clave:** `servicios/omni-sales-crm/server/funnels.ts`, `server/agent.ts`, `tests/funnels.test.ts`, `.env.example`. Commits `a53d06a` y `26b2a0d` en `feat/omni-sales-crm` (sin push).
- **Bloqueos:** faltan `CONTADORES_LINK_D1/D2/D3` en `.env` (sin ellos el lead pasa a un humano, nunca se envía el placeholder). Los comentarios de Instagram NO disparan nada: el webhook solo lee DMs; `ventas` debe pedir que escriban la clave por DM.
- **Próximo paso:** definir los 3 enlaces y decidir si se construye la ingesta de comentarios (Meta Private Reply). Después, verificar licencia y Agent Bots de Chatwoot (arquitectura aprobada: Chatwoot = canales, CRM = motor comercial).

## 2.2 `ventas` — Clínicas Lote 1 (2026-10-17)

- **Estado:** Toque 1 (auditoría paciente incógnito) enviado a 5 clínicas; 20 restantes inscritas y pendientes de envío manual en la vista **Hoy** del CRM de Railway (mensajes con saludo de mañana).
- **Resultados Toque 1:** Carolina Mendez = bot 1 min + humano hace seguimiento (la mejor; pitch distinto, ya tiene bot). AURORA = 10 min, precio $480.000, pide cédula. Ricardo Castillo = precios, valoración gratis, sin ofrecer cita. Aurea y REAL sin respuesta.
- **CRM desplegado (`feat/omni-sales-crm`):** guarda ambos lados del chat (Evolution `fromMe`, sin reenviar), "Sugerir con IA" en estilo chat (sin puntos/comas/¿, 2-3 partes) + "Abrir en WhatsApp"; simulador quitado. Commits a159f9c…cc20637, sin push.
- **Archivos clave:** `ventas/state.json` (1-5 en `AUDITADA`), `ventas/enlaces_fase1_lote1.md` (01-25), `ventas/prospectos/google_maps_2026-10-17.csv` (309 clínicas nuevas, 82 con puntaje ≥8; Apify USD $2.53).
- **Bloqueos:** no hay clave de IA en Railway `omni-crm` (el usuario la agrega; nunca por chat). El envío automático por WhatsApp Web fue bloqueado por el modo auto: envíos siempre manuales. `EVOLUTION_ALLOWED_NUMBERS` solo cubre las 25 del Lote 1.
- **Próximo paso:** enviar las 20 de Hoy; armar Lote 2 con las top 30 del CSV (mensajes + alta en CRM + ampliar allowed numbers + redeploy); evaluar correo como canal (Ley 2300: L-V 7-19, sáb 8-15).

---

## 3. Protocolo de Relevo entre Agentes
1. **Cuando `ventas-redes` publica un video:**
   - Registra en este archivo la fecha de publicación, enlaces de la pieza y los disparadores activos.
   - Sube el log a Engram (`project: "loovo"`).
2. **Cuando `omni-sales-crm` detecta un lead con estos tags:**
   - Notifica la conversión en el inbox omnicanal y ejecuta la regla del flujo automatizado.
3. **Cuando `ventas` hace seguimiento:**
   - Asume las conversaciones donde el usuario responde la pregunta de calificación posterior al enlace.

---

## 5. `ventas-redes` · Maquina de redes (actualizado 2026-10-17)

**Estado actual:** serie "Día X de 42" en curso. Día 7 `Dia7_ventas_ia.mp4` + portadas A/B listas (el usuario elige y publica). Día 4 `v1` terminado pero NO se publica (suena motivacional). Nicho Contadores (`Dia-08/proyecto/contadores_ia/`): brief, caption y plan listos; falta crudo, hook Higgsfield y portada.
**Archivos clave listos:** `Maquina de redes/00_Serie/{estado,relevo,hechos}.md`, `Dia-07/entregables/`, `Dia-08/proyecto/contadores_ia/{brief,caption}.md` y `plan/` (guion, higgsfield, edición, sfx, portada, `revision_hechos.md`), `odd/plans/campana-contadores-01.md`.
**Bloqueos para publicar D1/D2/D3:** los 3 sistemas no están en `hechos.md` (🟡 hasta probarlos); logo Tiendas D1 es marca ajena; Carolina en cámara choca con "solo voz del usuario"; faltan `CONTADORES_LINK_D1/D2/D3` en el `.env` del CRM.
**Próximo paso:** el usuario graba el crudo del Día 8 y genera el hook en Higgsfield; el orquestador decide qué pasa a ✅ en `hechos.md`, edita con `monoga-adria` y entrega portada. Aparte: revocar las 2 claves OpenAI pegadas en chat.


