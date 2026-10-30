# Loovo — Flujo Maestro de Reactivación (Protocolo de 3 Horas)

Protocolo técnico de la Fase 5. Se ejecuta en la sesión de entrega con la clínica.
Herramientas: `omni-sales-crm` (`../servicios/omni-sales-crm`) o WhatsApp Business con coexistencia.

---

## 1. Antes de empezar

- [ ] WhatsApp Business de la clínica conectado en **modo coexistencia** (escaneo de QR desde la app; la clínica sigue usando su app normal).
- [ ] Base de conocimiento cargada: servicios, rangos de precio autorizados, horarios, dirección, formas de pago, política de valoración.
- [ ] Nombre del asistente y nombre del doctor(a) definidos.
- [ ] Lista de hasta 100 chats antiguos exportada (nombre, número, último tratamiento consultado, fecha del último mensaje).

> **Ventana de 24 h de WhatsApp:** por la API solo se puede enviar texto libre dentro de las 24 h siguientes al último mensaje del paciente. Para escribir a chats antiguos por la API, el Toque 1 y el Toque 2 deben enviarse como **plantillas aprobadas por Meta** (categoría marketing). Si se envían manualmente desde la app de WhatsApp Business, respetar los lotes para no arriesgar la línea.
>
> **Datos personales (Ley 1581 de 2012):** escribir solo a pacientes que ya tuvieron conversación con la clínica, e incluir siempre la opción de no recibir más mensajes. Quien responda "NO" va a `🔴 4_CURIOSO_O_ARCHIVADO` y no se le vuelve a escribir.

---

## 2. Semáforo de 4 etiquetas

| Etiqueta | Cuándo se asigna | Quién actúa | Siguiente paso |
| --- | --- | --- | --- |
| `🟡 1_RESCATE_PENDIENTE` | Chat antiguo cargado para reactivar, aún sin respuesta. | Sistema | Recibe Toque 1 (Día 0) y, si no responde, Toque 2 (Día 3). |
| `🔵 2_CALIFICANDO_IA` | El paciente respondió o escribió por primera vez; la IA está preguntando. | IA | Completar las 4 preguntas de precalificación. |
| `🟢 3_LISTO_PARA_AGENDAR` | Tratamiento claro + quiere agendar en las próximas 4 semanas + aceptó valoración o pidió cita. | **Recepción, en menos de 15 min** | Llamar o escribir para confirmar día y hora. |
| `🔴 4_CURIOSO_O_ARCHIVADO` | Solo pregunta precio sin intención, no responde tras Toque 2, pidió no ser contactado, o está fuera de la ciudad sin intención de viajar. | Nadie | No se vuelve a contactar en esta campaña. |

**Reglas de transición:**
- `🟡` → `🔵` cuando el paciente responde a cualquier toque.
- `🔵` → `🟢` cuando se cumplen los 3 criterios de "listo" (ver System Prompt).
- `🔵` → `🔴` si tras 2 preguntas no hay intención o pide no ser contactado.
- `🟡` → `🔴` si no responde 72 h después del Toque 2.
- Urgencia médica, queja o pregunta clínica específica → asignar `🟢` y marcar "pasar a humano" de inmediato.

---

## 3. System Prompt Clínico (listo para pegar)

Pegar en **Configuración → Personalidad del agente / Flujos e IA** del CRM. Reemplazar lo que está entre corchetes.

```text
Eres [NOMBRE_ASISTENTE], asistente virtual de [NOMBRE_CLINICA] en [CIUDAD], la clínica de [DR_DRA] [NOMBRE_DOCTOR], especialista en [ESPECIALIDAD: diseño de sonrisa / rehabilitación oral / medicina estética].

OBJETIVO
Responder a cada paciente en menos de 45 segundos, entender qué necesita y dejar listos para agendar a los pacientes con intención real. Tú no agendas: la recepción confirma día y hora.

ESTILO
- Español de Colombia, trato de "usted", cálido y profesional.
- Mensajes cortos (1 a 3 frases). Una sola pregunta por mensaje.
- Empatía primero, datos después. Sin frases de call center, sin markdown.
- Si el paciente pregunta si eres una persona, di con honestidad que eres el asistente virtual de la clínica y que hay un equipo humano detrás.

PRECALIFICACIÓN (en este orden, de forma natural, sin parecer formulario)
1. Tratamiento de interés y qué le gustaría mejorar.
2. Hace cuánto lo está pensando o para cuándo lo quiere (próximas 4 semanas / 1-3 meses / solo averiguando).
3. Si ya ha tenido una valoración o tratamiento previo.
4. Nombre y si prefiere valoración presencial en [SEDE/DIRECCIÓN].

PRECIOS
- Solo das precios o rangos que estén en la base de conocimiento. Si no está, di: "El valor exacto lo define [el doctor / la doctora] en la valoración, porque depende de cada caso" y ofrece la valoración.
- Nunca inventes precios, descuentos, financiación, promociones ni disponibilidad.

LÍMITES CLÍNICOS
- No das diagnósticos, no recomiendas medicamentos y no prometes resultados.
- No afirmas "no duele", "garantizado" ni "sin riesgo".
- Ante dolor fuerte, sangrado, inflamación, reacción a un procedimiento o cualquier urgencia: pide su número, indica que un miembro del equipo lo contactará de inmediato y marca PASAR A HUMANO.

CRITERIOS "LISTO PARA AGENDAR" (los 3 deben cumplirse)
- Tratamiento de interés claro.
- Quiere hacerlo en las próximas 4 semanas o pidió cita / valoración.
- Dio su nombre y aceptó que recepción lo contacte.
Cuando se cumplan, responde: "Perfecto, [Nombre]. Ya le paso su información a nuestra recepción para que le confirme día y hora en los próximos minutos." y asigna la etiqueta 🟢 3_LISTO_PARA_AGENDAR.

ETIQUETAS (asigna exactamente una)
- 🔵 2_CALIFICANDO_IA: mientras haces las preguntas.
- 🟢 3_LISTO_PARA_AGENDAR: cuando se cumplen los 3 criterios, o ante urgencia / queja (con PASAR A HUMANO).
- 🔴 4_CURIOSO_O_ARCHIVADO: sin intención tras 2 preguntas, fuera de la ciudad sin intención de viajar, o si pide no ser contactado (respóndele con respeto y no vuelvas a escribir).

DATOS DE LA CLÍNICA
Horario: [HORARIO]
Dirección: [DIRECCIÓN]
Formas de pago: [FORMAS_DE_PAGO]
Valoración: [VALOR O "SIN COSTO"]
```

---

## 4. Plantillas de reactivación de los 100 chats antiguos

**Envío:** lotes de **35 chats cada 2 horas** (35 + 35 + 30). Personalizar `[Nombre]` y `[tratamiento]`. Todos los chats parten en `🟡 1_RESCATE_PENDIENTE`.

### Toque 1 — Día 0

> Hola [Nombre], le saluda [Nombre_Asistente] de [Nombre_Clínica] 😊 Hace un tiempo nos escribió preguntando por [tratamiento]. ¿Todavía lo tiene en mente? Este mes [el Dr. / la Dra.] [Apellido] tiene espacios de valoración y con gusto le resolvemos cualquier duda.
> _Si prefiere no recibir más mensajes, responda NO._

**Variante sin tratamiento conocido:**
> Hola [Nombre], le saluda [Nombre_Asistente] de [Nombre_Clínica]. Hace un tiempo hablamos por aquí y quería saber si aún le interesa mejorar su sonrisa / su piel. ¿Le cuento cómo es la valoración con [el Dr. / la Dra.] [Apellido]?
> _Si prefiere no recibir más mensajes, responda NO._

### Toque 2 — Día 3 (solo a quienes no respondieron el Toque 1)

> [Nombre], no quiero insistirle, solo dejarle la información a la mano: la valoración con [el Dr. / la Dra.] [Apellido] dura unos [N] minutos y ahí sale el plan y el valor exacto para su caso. ¿Le gustaría que le reserváramos un espacio esta semana o la próxima?
> _Si prefiere no recibir más mensajes, responda NO._

**Después del Toque 2:** quien no responda en 72 h pasa a `🔴 4_CURIOSO_O_ARCHIVADO`.

---

## 5. Cronograma de las 3 horas

| Tiempo | Acción | Verificación |
| --- | --- | --- |
| 0–45 min | Coexistencia por QR + crear las 4 etiquetas + cargar lista de 100 chats en `🟡`. | Las 4 etiquetas existen; 100 chats etiquetados. |
| 45–90 min | Pegar el System Prompt, cargar base de conocimiento, 5 conversaciones de prueba (precio, cita, objeción, fuera de horario, urgencia). | Respuesta < 45 s; ningún precio inventado; urgencia pasa a humano. |
| 90–135 min | Toque 1, lote 1 (35 chats). Programar lote 2 (+2 h) y lote 3 (+4 h). | Lote 1 enviado sin errores. |
| 135–180 min | Semáforo a recepción: quién atiende los `🟢`, en menos de 15 min. Capacitación en *Tomar control*. | Recepción atendió en vivo un `🟢` de prueba. |
| Día 3 | Toque 2 a los que siguen en `🟡`. | Conteo de 🟡 / 🔵 / 🟢 / 🔴 registrado. |
| Día 7 / 14 | Informe: chats reactivados, listos para agendar, citas confirmadas por la clínica. Cobro del segundo 50%. | Informe enviado; pago recibido. |
