# Plan de ventas · rumbo (2026-10-21)

Fuentes: 3 investigaciones de subagentes (repos, inventario, métodos). Sin acceso web para cifras de mercado: lo marcado "no verificado" no sale de nuestros datos. Solo planificación; no se envió nada.

## Diagnóstico
- El problema número 1 es vender, no construir. Evidencia propia: 25 clínicas contactadas, 18 respondieron, 0 conversaciones comerciales, $0 facturado.
- Dolor comprobado en las 18: nadie hace seguimiento al "lo pienso".

## Qué se puede vender hoy (inventario)
| Activo | Estado | Venta |
|---|---|---|
| Sprint de reactivación manual (7 días, $1.000.000) | 🟡 protocolo listo, sin cliente | Sí, esta semana |
| CRM + sugerencias IA por chat web | 🟡 169/169 tests, sin prueba en canal real | Solo como piloto, tras prueba |
| Bandeja + semáforo + seguimiento manual | 🟡 | Parte del Sprint |
| D1-D3 contadores | 🟡 prototipos, flujos sin probar | No hasta probar (2-4 semanas) |
| Rediseño web | 🔴 sin muestra en `landings/` | Primero hacer 1 muestra real |
| Agentes de voz | 🔴 no existe | No (3-6 semanas) |

## Decisiones propuestas (pendientes de aprobar)
1. **Una sola oferta:** Sprint de reactivación para clínicas.
2. **Videos de repositorios = contenido de atracción**, no producto. Cada video termina en la oferta o en lista de espera de piloto fundador, y dice "prototipo" si no está probado.
3. **Embudo mínimo, todo manual:** video → comentario con palabra clave → DM manual → página con precio. El CRM hoy no lee comentarios de Instagram.
4. **Sin pauta** hasta tener 1 venta repetible (ahorros $1.000.000 COP).
5. **Sin equipo nuevo** antes de la primera venta (micrófono primero si se decide).

## Experimentos de 7 días (metas propuestas, no verificadas)
1. Auditoría clínica: 20 prospectos, captura + video de 60 s. Meta: 8 respuestas, 3 llamadas, 1 propuesta. Costo $0-80.000.
2. Mockup web: 3 rediseños parciales de homes. Meta: 3 reuniones, 1 piloto pagado. Costo $0-50.000.
3. Piloto IA transparente: 5 contadores en lista de espera. Meta: 1 anticipo condicionado a prueba. Costo $0-150.000.

## Herramientas open source (verificar licencia antes de usar)
- Auditar webs `.co`: Lighthouse CI (Apache-2.0), PageSpeed CLI (licencia no verificada), Wappalyzer fork (no verificado).
- Correo en frío: Quickly (MIT, no verificado en actividad); Mautic (GPL-3.0) si se necesita CRM; listmonk (AGPL-3.0).
- WhatsApp: Evolution API (Apache-2.0 con condiciones extra) + Chatwoot (MIT) + n8n (fair-code, no OSI).
- Voz: LiveKit Agents (Apache-2.0), luego. Twilio ~US$0,038/min móvil, ~US$0,07/min fijo (no verificado; sin STT/LLM/TTS).

## Legal (conservador)
Ley 1581 de 2012: nombres, teléfonos, correos y chats son datos personales; informar finalidad, ofrecer baja, lista de supresión. Ley 2300: lun-vie 7:00-19:00, sáb 8:00-15:00, nunca domingos ni festivos. Solo datos corporativos públicos para prospección. No es asesoría legal: validar con abogado.

## Pendiente
- Leer chats de Evolution (autorizado, solo lectura): falta URL y nombre de la variable de la API key.
- Decidir oferta única: reactivación clínicas vs rediseño web.
