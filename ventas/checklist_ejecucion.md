# Loovo — Checklist de Ejecución Comercial

Proceso completo para vender y entregar el sistema de conversión y reactivación IA de Loovo a clínicas de Bucaramanga y Medellín.
Estado de cada clínica: `state.json`. Evidencia: `evidencia-auditorias/<NN-slug>/`. Protocolo técnico: `flujo_maestro_reactivacion_loovo.md`.

---

## Fase 0 — Alistamiento

### Nicho

- [ ] **Rehabilitación Oral / Diseño de Sonrisa** (tratamientos de ticket alto: carillas, coronas, implantes, diseño de sonrisa).
- [ ] **Medicina Estética** (armonización orofacial, toxina, rellenos, antiage).
- [ ] Ciudades: **Bucaramanga** (incluye Floridablanca) y **Medellín** (El Poblado, Envigado).

### Oferta (Orden de Servicio — `orden_de_servicio_loovo.md`)

| | Opción A — Sistema Completo de Conversión y Reactivación IA | Opción B — Sprint de Rescate Rápido de Pacientes en Visto |
| --- | --- | --- |
| Plazo | 14 días | 7 días |
| Inversión | **$2.500.000 COP** | **$1.000.000 COP** |
| Anticipo 50% | **$1.250.000 COP** | **$500.000 COP** |

- [ ] Orden de servicio revisada y lista para compartir pantalla.

### Protocolo de 3 horas y semáforo de 4 etiquetas

- [ ] Protocolo técnico listo (`flujo_maestro_reactivacion_loovo.md`).
- [ ] Las 4 etiquetas creadas en la cuenta de demo de WhatsApp Business / CRM:
  - `🟡 1_RESCATE_PENDIENTE` — chat antiguo aún sin reactivar.
  - `🔵 2_CALIFICANDO_IA` — la IA está precalificando al paciente.
  - `🟢 3_LISTO_PARA_AGENDAR` — paciente calificado; recepción debe agendar.
  - `🔴 4_CURIOSO_O_ARCHIVADO` — sin intención real o pidió no ser contactado.

### Datos de cobro

- [ ] Bancolombia: Cuenta de ahorros N.° `[completar]` — Titular `[completar]` — C.C./NIT `[completar]`
- [ ] Nequi: `[completar]`
- [ ] Llave Bre-B: `[completar]`
- [ ] QR de Bancolombia y QR de Nequi guardados como imagen para mostrar en la llamada.

### Bot Demo Clínico

- [ ] CRM levantado (`../servicios/omni-sales-crm`, `npm start`) con el System Prompt clínico cargado.
- [ ] Base de conocimiento de una clínica de ejemplo (servicios y rangos de precio).
- [ ] Link público del demo funcionando (`/widget-demo` vía túnel HTTPS) y probado desde el celular.

---

## Fase 1 — Auditoría de "Paciente Incógnito" (Lote #1)

**Objetivo:** escribir al WhatsApp de cada clínica como un paciente interesado y medir cómo responde. La captura es la "herida real" que se muestra al doctor.

**Mensaje de prueba (ejemplo):**
> Hola, buenas. Quería información sobre diseño de sonrisa / [tratamiento]. ¿Qué precio maneja y cómo es el proceso?

**Qué medir y registrar en `state.json`:**
- [ ] `hora_envio` (fecha y hora exacta del mensaje).
- [ ] Tiempo hasta la primera respuesta (minutos/horas, o "sin respuesta a 24 h").
- [ ] `fallo_detectado`: sin respuesta, respuesta tardía, respuesta genérica sin pregunta de seguimiento, no pidió datos, no propuso cita, solo mandó lista de precios, etc.
- [ ] Capturas en `evidencia-auditorias/<NN-slug>/` con nombre `AAAA-MM-DD_whatsapp_<que>.png`.
- [ ] Cambiar `estado` a `AUDITADA`.

**Reglas:** no agendar citas falsas ni ocupar agenda real; si ofrecen cita, agradecer y decir que confirmará después.

| # | Clínica | Ciudad | WhatsApp | Auditada |
| --- | --- | --- | --- | --- |
| 1 | Centro Integral Aurora de Medicina Estetica (Dr. Jorge Alberto Vargas) | Bucaramanga | +57 300 555 0001 | [ ] |
| 2 | Aurea Medical Spa (Dra. Valentina Ruiz — Cabecera) | Bucaramanga | +57 300 555 0002 | [ ] |
| 3 | Consultorio Dra. Carolina Mendez (Sotomayor) | Bucaramanga | +57 300 555 0003 | [ ] |
| 4 | REAL Medicina Estética (Dra. Paola Herrera — Sotomayor) | Bucaramanga | +57 300 555 0004 | [ ] |
| 5 | Dr. Ricardo Castillo Diseno de Sonrisa (Cabecera) | Bucaramanga | +57 300 555 0005 | [ ] |
| 6 | Sonrisa Norte Bucaramanga (Sotomayor) | Bucaramanga | +57 300 555 0006 | [ ] |
| 7 | Dra. Lorena Gil Rehabilitacion Oral (Canaveral) | Floridablanca | +57 300 555 0007 | [ ] |
| 8 | Dra. Natalia Ortiz Diseno de Sonrisa (Cabecera) | Bucaramanga | +57 300 555 0008 | [ ] |
| 9 | Dra. Patricia Lozano Estetica Antiage (Cabecera) | Bucaramanga | +57 300 555 0009 | [ ] |
| 10 | Los Especialistas en Sonrisas (Dr. Esteban Quintero — Cañaveral) | Floridablanca | +57 300 555 0010 | [ ] |
| 11 | Armonia Centro de Alta Estetica | Bucaramanga | +57 300 555 0011 | [ ] |
| 12 | Sonrie Clinica Demo Odontológica (Dra. Paula Restrepo — Cañaveral) | Floridablanca | +57 300 555 0012 | [ ] |
| 13 | Oral Studio Smile Makeover Demo (Dr. Andres Felipe Pardo / Dra. Angela Maya) | Medellín (El Poblado) | +57 300 555 0013 | [ ] |
| 14 | Dra. Sofia Bernal Medicina Estetica | Medellín (El Poblado) | +57 300 555 0014 | [ ] |
| 15 | FullDemo Armonización Orofacial (Dr. Gustavo Robles — El Tesoro) | Medellín (El Poblado) | +57 300 555 0015 | [ ] |
| 16 | Bonaventura Demo Medicina Estetica Demo | Medellín (El Poblado) | +57 300 555 0016 | [ ] |
| 17 | Clinica Demo Sede Poblado | Medellín (El Poblado) | +57 300 555 0017 | [ ] |
| 18 | Dra. Ana Londono Diseno de Sonrisa | Medellín (El Poblado) | +57 300 555 0018 | [ ] |
| 19 | MP Demo Medical Center (Dra. Monica Salazar — Milla de Oro) | Medellín (El Poblado) | +57 300 555 0019 | [ ] |
| 20 | Estetica Norte Clinica Estetica Demo | Medellín (El Poblado) | +57 300 555 0020 | [ ] |
| 21 | Balance Demo Demo | Medellín (El Poblado) | +57 300 555 0021 | [ ] |
| 22 | Clinica Quantum Demo Medicina Estetica (Dra. Diana / Dra. Paula) | Medellín (El Poblado) | +57 300 555 0022 | [ ] |
| 23 | Doctora Lucia Cardenas Medicina Estetica | Medellín (El Poblado) | +57 300 555 0023 | [ ] |
| 24 | Diseno de Sonrisa Dr. Mateo Villa | Envigado | +57 300 555 0024 | [ ] |
| 25 | Lina Caballero Odontologia | Medellín (El Poblado) | +57 300 555 0025 | [ ] |

---

## Fase 2 — Secuencia de 8 Toques (llegar al doctor sin pasar por recepción)

Registrar `toque_actual` (1–8) en `state.json` después de cada toque y cambiar `estado` a `EN_SECUENCIA`. Si el doctor responde en cualquier toque, saltar a la Fase 3.

| Toque | Cuándo | Canal | Acción |
| --- | --- | --- | --- |
| 1 | Día 0 | WhatsApp | **Captura de evidencia** (Fase 1). Ya está en la carpeta de la clínica. |
| 2 | Día 1 | Instagram DM al perfil personal del doctor | Mensaje corto con la herida real. |
| 3 | Día 1, 2 min después | Comentario en su último Reel | Comentario genuino sobre el contenido (no venta). Activa la notificación y da contexto al DM. |
| 4 | Día 2 | Instagram DM | **Caballo de Troya:** entregar valor gratis (mini-diagnóstico de su WhatsApp). |
| 5 | Día 3 | Instagram DM | **Link del Bot Demo** para que lo pruebe como paciente. |
| 6 | Día 4 | Nota de voz de 20 s | Voz humana, directa, una sola pregunta. |
| 7 | Día 5 | Instagram DM | **Prueba social:** resultado concreto de otra clínica o del demo. |
| 8 | Día 6 | Instagram DM | **Break-Up Sandler:** cerrar la puerta con respeto. |

### Plantillas

**Toque 2 — DM Día 1**
> Dr./Dra. [Apellido], buenas. Le escribí a su WhatsApp el [día] a las [hora] como paciente preguntando por [tratamiento]. [Fallo concreto: "Pasaron 6 horas sin respuesta" / "Me enviaron solo la lista de precios y no me preguntaron nada más"]. Le guardé la captura. ¿Le interesa verla? Son 30 segundos.

**Toque 3 — Comentario en Reel (2 min después)**
> [Comentario específico sobre el contenido del Reel, sin vender. Ej.: "Muy claro cómo explica la diferencia entre carillas en resina y en porcelana 👏"]

**Toque 4 — Caballo de Troya Día 2**
> Dr./Dra. [Apellido], le dejo esto sin compromiso: una mini-auditoría de cómo responde su WhatsApp a un paciente nuevo [adjuntar captura + 3 puntos de mejora]. Cada consulta que se enfría ahí es un tratamiento de [ticket promedio] que se va a otra clínica.

**Toque 5 — Bot Demo Día 3**
> Armé un asistente de prueba que responde como lo haría su clínica, en menos de 45 segundos, 24/7, y le pasa a recepción solo los pacientes listos para agendar. Pruébelo como si fuera un paciente: [link]

**Toque 6 — Nota de voz 20 s Día 4**
> "Dr./Dra. [Apellido], habla [Nombre] de Loovo. Le mandé la captura de cómo le respondieron a un paciente en su WhatsApp. Una sola pregunta: ¿cuántos pacientes cree que se le están quedando en visto al mes? Si me dice un número, le muestro en 20 minutos cómo recuperarlos."

**Toque 7 — Prueba social Día 5**
> [Resultado real y verificable: "En la demo con una clínica de [ciudad], la IA calificó [N] chats antiguos en una tarde y dejó [N] listos para agendar." — usar solo datos reales.]

**Toque 8 — Break-Up Sandler Día 6**
> Dr./Dra. [Apellido], supongo que recuperar pacientes en visto no es prioridad ahora mismo, y está bien. Cierro el tema por mi lado para no insistirle. Si más adelante quiere revisarlo, aquí queda la captura.

---

## Fase 3 — Conversión en Chat en 5 Minutos

Cuando el doctor responde:

- [ ] **Mostrar la herida real:** enviar la captura de su propia clínica y el tiempo de respuesta medido.
- [ ] **Probar el Bot Demo:** pedirle que escriba como paciente en el link y vea la respuesta en menos de 45 s.
- [ ] **Doble alternativa de horario:** "¿Le queda mejor mañana a las **11:00 AM** o a las **3:00 PM** para mostrarle en 20 minutos cómo quedaría en su clínica?"
- [ ] **Personalizar la Orden de Servicio** con nombre del doctor, clínica y su fallo detectado antes de la llamada.
- [ ] Cambiar `estado` a `LLAMADA_AGENDADA`.

---

## Fase 4 — Guion de Videollamada de 20 Minutos

| Minuto | Bloque | Qué decir / hacer |
| --- | --- | --- |
| 0–2 | **Contrato previo (Sandler)** | "Dr./Dra., en 20 minutos le muestro lo que encontré y cómo se resuelve. Al final usted me dice sí o no, cualquiera de las dos está bien. Lo único que le pido es que no sea un 'déjeme pensarlo': si no le sirve, me lo dice con confianza. ¿Le parece justo?" |
| 2–5 | **Volumen / fuga** | "¿Cuántos mensajes nuevos de pacientes le entran al mes por WhatsApp? ¿Cuántos cree que terminan agendando? ¿Cuántos chats tiene hoy sin responder o en visto?" |
| 5–7 | **Falla operativa de recepción** | Mostrar la captura de la auditoría. "¿Quién responde el WhatsApp? ¿Qué pasa después de las 6 PM y los fines de semana?" |
| 7–10 | **Matemática del sangrado** | Con SUS números: consultas perdidas/mes × % de cierre × ticket promedio. Ejemplo: 30 consultas perdidas × 20% × $2.500.000 = **$15.000.000/mes = $180.000.000/año**. "¿Ese número le parece real o me estoy quedando corto?" |
| 10–13 | **Los 3 Pilares en vivo con el CRM** | 1) Respuesta y precalificación 24/7 en menos de 45 s. 2) Reactivación de chats antiguos (Toque 1 y 2). 3) Semáforo de 4 etiquetas que le entrega a recepción solo los listos para agendar. Mostrarlo funcionando en el CRM. |
| 13–16 | **Orden de Servicio** | Compartir pantalla con `orden_de_servicio_loovo.md`. Opción A $2.500.000 vs. Opción B $1.000.000. "¿Cuál se ajusta mejor a lo que necesita hoy?" |
| 16–20 | **Cobrar el 50% en vivo** | Mostrar QR de Bancolombia / Nequi o llave Bre-B. "Apenas confirme el anticipo, agendamos la entrega de 3 horas esta misma semana." Pedir aprobación escrita por WhatsApp. |

- [ ] Al cobrar: `estado` = `ANTICIPO_PAGADO`, sumar a `marcador.facturado_cop` (valor total) y `marcador.cobrado_cop` (anticipo).
- [ ] Crear `../clientes-activos/<slug-clinica>/` desde la plantilla.

---

## Fase 5 — Entrega Técnica en 180 Minutos

Plantilla detallada por cliente: `../clientes-activos/README.md`. Protocolo técnico: `flujo_maestro_reactivacion_loovo.md`.

| Bloque | Tiempo | Entregable |
| --- | --- | --- |
| 1 | 0–45 min | **Coexistencia por QR** (WhatsApp Business app + plataforma) y creación de las **4 etiquetas**. |
| 2 | 45–90 min | **Precalificación 24/7** con respuesta en menos de 45 s (System Prompt clínico cargado y probado). |
| 3 | 90–135 min | **Toque 1 de reactivación** a 100 chats antiguos, en **lotes de 35 cada 2 horas**. |
| 4 | 135–180 min | **Semáforo a recepción:** cada `🟢 3_LISTO_PARA_AGENDAR` se atiende en menos de 15 min. Capacitación del equipo. |
| Día 3 | — | **Toque 2** de reactivación a quienes no respondieron. |
| Día 7 / 14 | — | Informe de resultados y **cobro del segundo 50%** (Día 7 en Opción B, Día 14 en Opción A). |

---

## Fase 6 — Marcador Financiero hacia $5.000.000 COP (5 clientes)

Fuente de verdad: `state.json` → `marcador`.

| # | Clínica | Opción | Valor total | Anticipo cobrado | Segundo 50% cobrado |
| --- | --- | --- | --- | --- | --- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| **Total** | | | **$0 / $5.000.000** | **$0** | **$0** |

Referencia: 5 clientes en Opción B = $5.000.000; 2 en Opción A = $5.000.000.
