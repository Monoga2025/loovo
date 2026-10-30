# Día 3 de 42 · 2026-10-09 (viernes) · La DIAN que prometí ayer

**Trabajo de hoy:** encender el CRM en modo demo y averiguar qué hace falta para emitir factura electrónica desde el CRM.
**Tiempo:** 4 h en 3 bloques.
**Pilar:** construcción con un error probable.
**Faltan:** 39 días.
**Nómina:** #001 ✅ · #002 🟡 · #003 ⏳ ("aún no nace").

**Por qué este tema:** en el Día 2 dijiste "lo de la DIAN lo vamos a ver en el día 3". Hoy se cumple, pero con honestidad: hoy no se integra nada. Hoy averiguas qué hace falta y #003 empieza a nacer. Que no salga todo hoy también es contenido.

**Antes de grabar:**
- [ ] OBS grabando (salen 3 archivos) y una palmada al empezar
- [ ] CRM con `tools\monoga\start.ps1 -Demo`, **no** con `CRM.bat` (ese abre la base real con un cliente real)
- [ ] Todas las páginas del CRM abiertas una vez antes de grabar (la primera carga tarda)
- [ ] Sin `.env`, sin `HANDOFF*.md`, sin la carpeta `docs/overnight-*` (tiene prospectos reales)
- [ ] El navegador sin pestañas personales ni correo

## Bloques de las 4 horas
| Bloque | Tiempo | Qué se graba | Qué sale |
|---|---|---|---|
| 1 | 0:00-1:00 | Encender el CRM en modo demo y elegir cuál arranque es el oficial | Capítulo 1 del largo |
| 2 | 1:00-3:00 | Investigar la factura electrónica: qué pide la DIAN, quién da la API, cuánto cuesta y cuánto tarda | Capítulos 2 y 3 del largo |
| 3 | 3:00-3:15 | Descanso: anota los "marca" que dijiste | |
| 4 | 3:15-4:00 | A cámara: E1 Día 3, E3 y la reserva | Los shorts |

---

## 1 · YouTube (largo): "Prometí conectar la DIAN a mi CRM. Esto es lo que encontré."
**Apuesta:** hoy no paro hasta saber qué necesito exactamente para que mi CRM emita una factura electrónica de prueba: con quién, cuánto cuesta y cuántos días tarda. Si la respuesta es "no se puede todavía", lo vas a ver.

**Gancho (literal, elige uno):**
- A: "Ayer prometí conectar mi CRM a la DIAN. Hoy descubrí que no era tan fácil."
- B: "Faltan 39 días para el evento y le prometí a internet una factura electrónica."
- C: "Día 3. Mi empleado número tres todavía no nace, y hoy les muestro por qué."

Ojo: el gancho A sirve solo si de verdad aparece una traba. Si no aparece, usa el B.

**Promesa y lo que está en juego (con tus palabras):**
- Qué es Loovo en una frase y qué es el evento: 17 de noviembre, más de 2.000 empresarios.
- Por qué la DIAN. Ancla opcional: "Un empresario no necesita otro chat. Necesita facturar sin perder la tarde."
- La regla del video: si algo falla, se queda en el video.

**Hoja de ruta:**
1. Prender mi CRM sin mostrar clientes reales.
2. Averiguar qué pide la DIAN para facturar desde un software.
3. Elegir con quién conectarlo y cuánto cuesta.

| Bloque (~3 min editados) | Objetivo | En pantalla | Pregunta en voz alta | Pero / por lo tanto |
|---|---|---|---|---|
| 1 | Mostrar el CRM en modo demo | Terminal arrancando, luego el CRM con los tratos "Demo SAS" | "¿Por qué no les muestro mis clientes de verdad?" | Pero tengo dos formas de prenderlo y una abre la base real, **por lo tanto** hoy dejo una sola |
| 2 | Contar de dónde viene el CRM | El repositorio y el README | "¿Lo hice desde cero?" | No: adapté un CRM open source y le cambié lo que necesita una empresa en Colombia |
| 3 | Qué es la factura electrónica para un software | Navegador: página de la DIAN | "¿Puede mi CRM mandarle una factura directo a la DIAN?" | `[RESULTADO REAL]`: lo que encuentres |
| 4 | Proveedores con API | Búsqueda y comparación | "¿Con quién lo conecto y cuánto me cuesta al mes?" | `[DATO: proveedores, precio, ambiente de pruebas]` |
| 5 | La traba | Lo que bloquee: registro, habilitación, resolución de facturación, días de espera | "¿Qué me falta que no es código?" | Por lo tanto, #003 no nace hoy: nace el día `[DATO]` |
| 6 | La decisión | Tabla de 3 opciones en una nota o una hoja | "¿Cuál elijo y por qué?" | La decisión y su porqué en una frase |

**Momentos obligatorios:**
- [ ] Decir en voz alta que el CRM se ve en modo demo y por qué (confianza con los empresarios)
- [ ] Decir de dónde viene el CRM: "adapté un CRM open source". Nunca "lo hice desde cero"
- [ ] Mostrar lo primero que te sorprenda de la DIAN, con la fuente en pantalla
- [ ] Decir cuánto cuesta: precio real o "todavía no lo sé"
- [ ] La traba con su costo en días
- [ ] La decisión y su porqué

**Frases ancla para clip** (di "marca", mira a cámara, entre 20 y 40 s):
1. **Modo demo:** "Nunca van a ver un cliente mío real en estos videos. Para eso tengo un CRM de mentiras con empresas que se llaman 'Demo'."
2. **El origen:** "No hice el CRM desde cero. Tomé uno open source y lo volví colombiano: pesos, etapas en español y consentimiento de datos."
3. **La DIAN:** "Lo que nadie te dice de la factura electrónica…" → **cambia la primera frase**, porque "lo que nadie te dice" está prohibido. Usa: "Pensé que conectar la factura electrónica era código. Lo difícil es [RESULTADO REAL]."
4. **Costo:** "Facturar desde mi CRM me va a costar `[DATO]` al mes. Esto es lo que incluye."
5. **#003:** "Mi empleado número tres todavía no nace. Le faltan papeles, como a todo el mundo en Colombia."

**Bucles abiertos:**
- "¿Cuánto cuesta?" → se cierra en el bloque 4.
- "¿Cuándo nace #003?" → queda para el día que dé la traba (el plan lo tiene en los Días 9 y 10).

**Cierre:**
- Resultado: `[RESULTADO REAL]`.
- Lección en una frase, sin moraleja.
- Puente: "Mañana: le pongo un botón al CRM para grabar siempre sin datos reales."

**No mostrar:**
- `CRM.bat` encendido en pantalla.
- La ficha de OENYX y el KPI "win rate 100 %".
- `.env` y la terminal con variables.
- Tu cédula, RUT o NIT si te los pide un proveedor: apaga la cámara de pantalla o tápalos.

**Decir con cuidado:**
- La DIAN ⏳: "todavía no está conectada".
- El agente de IA 🟡: "lo estoy probando".
- "Capturar lead" funciona con reglas, no con IA.

---

## 2 · E1 · Día 3 (corto, 40-50 s): se graba AL TERMINAR
Estructura A. El gancho depende de lo que pase, así que hay una versión para cada caso.

**Ganchos (literales):**
- Si apareció una traba: "Ayer prometí conectar la DIAN. Hoy me di cuenta de que no es código."
- Si salió mejor de lo esperado: "Día 3 de 42 y ya sé cuánto cuesta facturar desde mi CRM."
- Neutro, para la serie: "Día 3 de 42. Mi empleado número tres todavía no nace."

**Puntos:**
1. **Recap:** en el Día 2 te mostré a mis dos empleados que no cobran; el tercero iba a facturar.
2. **Intento:** prendiste el CRM, en modo demo, y te fuiste a la DIAN.
3. **Pero:** `[RESULTADO REAL]`. Lo que falta, cuánto cuesta, cuántos días.
4. **Por lo tanto:** #003 nace el día `[DATO]`. Mientras tanto, `[lo que sí hiciste hoy]`.

**Remate (elige o di el tuyo):**
- "Por ahora mi empleado número tres está haciendo fila, como todos."
- "Sueldo cero, pero papeles igual."

**Puente:** "Mañana les muestro cómo grabo el CRM sin enseñar un solo cliente."

**Final doble:**
- TikTok: "¿Ustedes facturan con software o todavía a mano? Una palabra."
- Reels: "Mándaselo al que todavía hace la factura a mano."

**Texto en pantalla:** `#003 · DIAN · AÚN NO NACE` y el sello `NÓMINA: 3 · HORAS DEVUELTAS: MIDIENDO · SUELDO TOTAL: $0`.

## 3 · Clips del largo (E2 y siguientes): salen de las frases ancla
| # | Momento | Gancho propio | Estructura | Cuándo publicar |
|---|---|---|---|---|
| C1 | Modo demo (ancla 1) | "Nunca vas a ver un cliente mío en estos videos." | C | Día 4 (encaja con el tema) |
| C2 | El origen open source (ancla 2) | "No hice mi CRM desde cero, y está bien." | C | Día 5 o reserva |
| C3 | La traba de la DIAN (ancla 3) | "Pensé que la factura electrónica era código." | B | Día 6 o 7 |
| C4 | Costo (ancla 4) | "Esto cuesta facturar desde tu propio software." | C | Cuando haya cifra real |

## 4 · E3 opcional y reserva (a cámara, en el bloque 4)
Del banco evergreen de `plan-42.md`, los que mejor encajan hoy:
- **EV-01, "Por qué no construí mi CRM desde cero"**: complementa C2. Graba solo uno de los dos.
- **EV-05, "Presentación de la Nómina"**: sirve para quien llega nuevo.
- **EV-12, "Reglas vs IA"**.

Si sobran fuerzas: EV-20 y EV-21 (Habeas Data).

---

**Autocrítica (rúbrica de `references/calidad.md`):**

Largo, 25/30:

| Gancho | Voz | Especificidad | Un tema | En juego | Hechos | Pero / por lo tanto | Bucle | Recompensa | Tics | Ritmo | Humor | Se puede decir | Seguridad | Libertad |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 |

Día 3, 25/30:

| Gancho | Voz | Especificidad | Un tema | En juego | Hechos | Pero / por lo tanto | Bucle | Recompensa | Tics | Ritmo | Humor | Se puede decir | Seguridad | Libertad |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 |

- **Lo que baja la nota:** especificidad y recompensa dependen del resultado real, porque no se inventa. En el Día 3 hay 3 ganchos condicionales, así que la libertad queda en 1.
- **Lo que se reescribió:**
  - El ancla 3 empezaba con "lo que nadie te dice", que está prohibido.
  - El remate "sueldo cero pero muchos papeles" se acortó.
- **Voz:** suenan a ti "Faltan 39 días…" (número y plazo) y "Sueldo cero, pero papeles igual" (humor seco del Día 2). Las dos más riesgosas son "Le faltan papeles, como a todo el mundo en Colombia" (puede sonar a queja genérica: dila solo si te sale) y "Hoy les muestro por qué" (cercana a "hoy te voy a mostrar", aunque es tuya: "les voy a mostrar" está en el Día 2).

**No verificado:**
- Cómo suena en voz alta.
- Lo que de verdad pida la DIAN o cobre un proveedor.
- Que `start.ps1 -Demo` arranque en este equipo, porque nadie lo ha corrido aquí.
