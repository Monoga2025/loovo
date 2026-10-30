# Propuesta para generar ingresos · 2026-10-20

Solo investigación y propuesta. No se envió nada a nadie. Cifras marcadas **(no verificado)** no salen de nuestros datos.

## Punto de partida (datos propios)

- Ahorros: $1.000.000 COP. Ingreso por IA: $0. Marcador en `ventas/state.json`: facturado $0, cobrado $0, clientes 0 de meta 5 ($5.000.000).
- Toque 1: 25 de 25 enviados el sábado 17 (`respuestas_2026-10-18.md`). 18 respondieron, 7 no. Tiempos de respuesta entre 2 segundos y 4 h 34 min.
- Ningún doctor ha hablado con Loovo todavía: no hay objeciones comerciales reales.
- `state.json` está desfasado (clínicas 6 a 25 siguen en `PENDIENTE_AUDITORIA`, Aurea y REAL figuran sin respuesta). No sé si los mensajes del lunes 19 salieron: **confirma qué se envió antes de usar este plan**.

## 1. Clínicas más cerca de pagar

Ninguna está cerca de pagar hoy: nadie ha hablado con Loovo. Ordeno por señal comercial (doctor identificado, ticket alto, falla clara de seguimiento):

| # | Clínica | Por qué | Mensaje manual (de `respuestas_2026-10-18.md`, adaptar si hubo chat nuevo) |
|---|---|---|---|
| 1 | Dr. Ricardo Castillo (Bucaramanga) | Carillas $4.000.000 (resina) a $16.000.000 (porcelana); no pidió nombre, no ofreció cita, no hizo seguimiento. Un solo paciente recuperado paga el servicio. | "Dr. Castillo, buenas. El sábado a las 9:27 le escribí a su WhatsApp como paciente preguntando por carillas. Me respondieron en 18 minutos con los precios y que la valoración es gratis, pero no me preguntaron el nombre ni me ofrecieron un horario. Cuando dije que lo pensaba, no me volvieron a escribir. Guardé la captura. ¿Quiere verla?" |
| 2 | Dra. Lorena Gil (Floridablanca) | Implantes (ticket alto). Respuesta de una línea sin precio ni horario. | "Dra. Gil, buenas. El sábado a las 11:15 le escribí a su WhatsApp como paciente preguntando por implantes. Me respondieron 'puedes venir a una valoración' y nada más: ni precio, ni horario, ni mi nombre. Guardé la captura. ¿Quiere verla?" |
| 3 | Oral Studio (Medellín) | Carillas en porcelana, respondieron en 4 min y ofrecieron valoración sin costo; no hubo seguimiento. | "Dr. Pardo, buenas. El sábado le escribí a su WhatsApp como paciente preguntando por carillas en porcelana. Me respondieron en 4 minutos y me ofrecieron valoración sin costo. Muy bien. Cuando no contesté, nadie me volvió a escribir. ¿Cuántos pacientes cree que se le quedan así al mes?" |
| 4 | Sonríe, Dra. Paula Restrepo (Floridablanca) | Respondió en 11 min y ofreció cita; luego silencio. Ticket bajo (limpieza $85.000, blanqueamiento $160.000), pero decide rápido. | "Dra. Restrepo, buenas. El sábado le escribí a su WhatsApp como paciente preguntando por blanqueamiento. Me respondieron en 11 minutos con precios y me ofrecieron cita. Muy rápido. Cuando no contesté, nadie me volvió a escribir. ¿Cuántos pacientes cree que se le quedan así al mes?" |
| 5 | AURORA, Dr. Jorge Alberto Vargas (Bucaramanga) | Botox frente $480.000; pide cédula antes de generar confianza y no sigue al "lo pienso". | "Dr. Vargas, buenas. El sábado a las 9:24 le escribí a su WhatsApp como paciente preguntando por botox en la frente. Me respondieron en 10 minutos con el precio y me pidieron nombre completo y cédula para agendar. Cuando dije que lo pensaba, nadie me volvió a escribir. Guardé la captura. ¿Quiere verla? Son 30 segundos." |

Menos prioritarias: Carolina Mendez y Natalia Ortiz (ya tienen bot y seguimiento; el ángulo es solo el "lo pienso" que se enfría) y las 7 sin respuesta (mensaje de la plantilla A).

Si un doctor contesta: detener la secuencia, mostrar la captura y ofrecer llamada a las 11:00 o 3:00 (Fase 3 del `checklist_ejecucion.md`). Horario permitido: lunes a viernes 7:00-19:00, sábados 8:00-15:00; nunca domingos ni festivos.

## 2. Tres ofertas (precios iniciales = hipótesis, **no verificado** que el mercado los pague)

| Oferta | Para | Precio inicial | Qué SÍ se entrega hoy | Qué NO prometer |
|---|---|---|---|---|
| **1. Auditoría Paciente Incógnito + plan de 7 días** | Clínicas | $300.000 COP (hipótesis) | Informe con capturas, tiempos de respuesta y fallos de su WhatsApp (método ya aplicado a 25 clínicas) y 5 mensajes de seguimiento redactados por la IA para que recepción los envíe a mano. | Respuesta automática 24/7. |
| **2. Sprint de Rescate (Opción B actual)** | Clínicas con chats en visto | $1.000.000 COP (anticipo $500.000, ya definido en `orden_de_servicio_loovo.md`) | Redacción de Toque 1 y 2 para hasta 100 chats antiguos, semáforo de 4 etiquetas en su WhatsApp Business, informe día 7, garantía de devolución. Los envíos los hace la clínica o se aprueban a mano. | Número de citas; envío automático. |
| **3. Piloto fundador para contadores** | Contadores | $200.000 COP (hipótesis) | **Nada hoy.** D1, D2 y D3 están importados en n8n pero inactivos y sin pruebas reales (SHARED_STATE 🟡; faltan credenciales y UVT 2026). Solo se vende cuando D2 o D3 pasen una prueba con datos reales. | Cualquier sistema D1-D3 antes de probarlo. |

Alerta: la **Opción A** ($2.500.000) promete "respuesta en menos de 45 segundos, 24/7", pero la regla de negocio 1 dice que la IA solo redacta y los envíos son manuales, y ese canal no está probado de punta a punta. **No la vendas hasta resolver eso.**

## 3. Plan de 14 días (martes 20 oct a lunes 2 nov)

Metas son objetivos propuestos, **no verificado** que sean alcanzables (no tenemos tasas de conversión propias todavía).

| Meta a 14 días | Objetivo |
|---|---|
| Conversaciones con un doctor o encargado (respuesta al Toque 2) | 6 |
| Llamadas o citas agendadas | 3 |
| Propuestas (orden de servicio) enviadas | 2 |
| Ventas cobradas | 1 (mínimo $300.000; ideal $1.000.000) |

| Día | Fecha | Venta (manual, en horario) | Video |
|---|---|---|---|
| 1 | mar 20 | Confirmar qué salió el lunes; Toque 2 pendiente | "Escribí como paciente a 25 clínicas" (datos propios: 18 respondieron, 7 no). Sin nombres. |
| 2 | mié 21 | Toque 4 | Corte: respuesta más lenta (4 h 34 min) |
| 3 | jue 22 | Toque 6; responder doctores | Corte: la que respondió en 2 segundos y aun así no cerró |
| 4 | vie 23 | Toque 7; llamadas | Qué pierde una clínica con "lo pienso" sin seguimiento |
| 5 | sáb 24 | Toque 8 (antes de las 15:00) | Día X de la serie |
| 6 | dom 25 | No se envía nada | Grabar audio con micrófono; editar |
| 7 | lun 26 | Nuevas clínicas (lote 2 de 20) | Revisar el correo de Coursera (beca) |
| 8 | mar 27 | Enviar propuestas a quien respondió | Tutorial corto: la auditoría paso a paso |
| 9 | mié 28 | Seguimiento de propuestas | Corte del lote 2 |
| 10 | jue 29 | Cierre y cobro del anticipo | Resultado parcial real (solo si es cierto) |
| 11 | vie 30 | Llamadas | Día X |
| 12 | sáb 31 | Último seguimiento (antes de las 15:00) | Corte reutilizado |
| 13 | dom 1 nov | No se envía nada | Grabar y editar |
| 14 | lun 2 nov (festivo) | No se envía nada | Balance de 14 días: ver abajo |

Contadores: no publicar videos de D1-D3 hasta probarlos (regla ya registrada). Tarea paralela, sin vender: probar D2 o D3 con datos de prueba reales.

Balance del día 14: contar conversaciones, citas, propuestas y ventas contra la tabla. Si hay cero conversaciones tras 25 + 20 contactos, cambiar el ángulo del mensaje antes de gastar más.

## Riesgos

- El audio saturado del celular sigue sin resolverse; los videos con mala voz cuestan credibilidad.
- Ahorros: $1.000.000 COP. Comprar equipo antes de la primera venta compromete todo el colchón.
