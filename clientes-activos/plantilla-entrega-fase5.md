# Template: phase 5 delivery (180 minutes)

Una carpeta por cada clínica que pagó el 50% de anticipo: `clientes-activos/<slug-clinica>/` (usar el mismo slug de `../ventas/evidencia-auditorias/`, ej. `01-cime-cadena`).
Copy the template below into `<slug>/README.md` and fill it in during delivery. The detailed protocol is in `../ventas/flujo_maestro_reactivacion_loovo.md`.
Protocolo técnico detallado: `../ventas/flujo_maestro_reactivacion_loovo.md`.

---

## Plantilla — Fase 5: Entrega Técnica en 180 Minutos

**Clínica:** <nombre> · **Doctor(a):** <nombre> · **Ciudad:** <Bucaramanga | Medellín>
**Opción:** <A — 14 días $2.500.000 | B — 7 días $1.000.000> · **Anticipo recibido:** <AAAA-MM-DD> · **Fecha de entrega:** <AAAA-MM-DD>

### Antes de la sesión

- [ ] Orden de Servicio aprobada por WhatsApp (captura guardada en esta carpeta).
- [ ] Comprobante del anticipo guardado en esta carpeta.
- [ ] Información de la clínica: servicios, rangos de precio autorizados, horario, dirección, formas de pago, valoración.
- [ ] Lista de hasta 100 chats antiguos para reactivar.

### Bloque 1 — Coexistencia por QR y 4 etiquetas (0–45 min)

- [ ] WhatsApp Business conectado en modo coexistencia (QR).
- [ ] Etiquetas creadas: `🟡 1_RESCATE_PENDIENTE`, `🔵 2_CALIFICANDO_IA`, `🟢 3_LISTO_PARA_AGENDAR`, `🔴 4_CURIOSO_O_ARCHIVADO`.
- [ ] 100 chats antiguos etiquetados en `🟡`.

### Bloque 2 — Precalificación 24/7 en menos de 45 s (45–90 min)

- [ ] System Prompt clínico pegado y personalizado.
- [ ] Base de conocimiento cargada.
- [ ] 5 pruebas: precio, pedir cita, objeción, fuera de horario, urgencia. Respuesta < 45 s y ningún precio inventado.

### Bloque 3 — Toque 1 de reactivación (90–135 min)

- [ ] Lote 1: 35 chats enviados (hora: ____).
- [ ] Lote 2: 35 chats a las +2 h (hora: ____).
- [ ] Lote 3: 30 chats a las +4 h (hora: ____).

### Bloque 4 — Semáforo a recepción en menos de 15 min (135–180 min)

- [ ] Responsable de atender los `🟢` definido: ____________.
- [ ] Recepción atendió en vivo un `🟢` de prueba en menos de 15 min.
- [ ] Equipo capacitado en *Tomar control*.

### Seguimiento

- [ ] **Día 3:** Toque 2 enviado a los que siguen en `🟡`.
- [ ] Conteo: 🟡 ___ · 🔵 ___ · 🟢 ___ · 🔴 ___
- [ ] **Día 7 (Opción B) / Día 14 (Opción A):** informe enviado y segundo 50% cobrado.
- [ ] `../ventas/state.json` actualizado (`ENTREGADA` → `PAGADA_100`, marcador).

### Notas

<pendientes, incidencias, fecha de próximo seguimiento>
