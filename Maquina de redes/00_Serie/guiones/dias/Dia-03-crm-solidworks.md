# Día 3 de 42 · 2026-10-09 (viernes) · Reviso mi CRM con IA y entrego una pieza de SolidWorks

**Trabajo de hoy:** revisar y arreglar el módulo de CRM con IA + hacer una pieza de SolidWorks para dibujo computarizado (universidad).
**Tiempo:** `[DATO: N h]` · **Pilar:** construcción + detrás de cámaras (dueño y estudiante a la vez).
**Faltan:** 39 días. **Nómina:** #001 ✅ · #002 🟡 (es el que se revisa hoy) · #003 ⏳ "aún no nace".

> Esta versión **reemplaza la sesión** de `Dia-03.md` (la DIAN). Del otro paquete se aprovechan el modo demo, las anclas de origen open source y la regla de seguridad. Ver "Decisión pendiente: la promesa de la DIAN" abajo.

**Antes de grabar:**
- [ ] CRM con `tools\monoga\start.ps1 -Demo`, **no** con `CRM.bat`. Ojo: `-Demo` pide que la base `crm_demo` ya exista (si no, el script se detiene; está en `docs/monoga-local-runbook.md`, sección Demo mode). Prueba el arranque antes de darle a grabar.
- [ ] Abrir una vez todas las páginas del CRM (la primera carga tarda)
- [ ] OBS grabando (3 archivos) y una palmada al empezar y otra al volver de cada pausa larga
- [ ] Sin `.env`, `HANDOFF*.md` ni `docs/overnight-*`; navegador sin pestañas personales ni correo
- [ ] Portal de la universidad, nombre del profesor y código estudiantil fuera de pantalla
- [ ] SolidWorks abierto en una ventana separada, con el archivo de la pieza nuevo (para que se vea el croquis desde cero)

---

## 1 · YouTube (largo): "Mi CRM con IA contra mi tarea de SolidWorks: el mismo día, dos entregas"
(Título de trabajo. Alterno de resultado primero cuando lo sepas: "Probé el agente de mi CRM de punta a punta (y `[RESULTADO REAL]`)".)

**Apuesta:** hoy no paro hasta que (1) el agente de mi CRM responda una vez de punta a punta, en modo demo, y (2) la pieza de SolidWorks quede lista para entregar. Si algo falla, se queda en el video.

**Gancho (literal, 0:00-0:10, elige uno):**
- A: "Hoy tengo dos entregas: mi CRM con IA y una pieza de SolidWorks para la universidad."
- B: "Faltan 39 días para el evento y hoy también me toca entregar una tarea de la universidad."
- C: "Hoy no paro hasta que el agente de mi CRM responda una vez de verdad."

Ojo: C solo si el agente de verdad no se ha probado. Está así en `hechos.md` (🟡), así que hoy es honesto.

**Promesa y lo que está en juego (con tus palabras):**
- Quién eres en una frase: dueño de Loovo, agencia de IA, y estudiante. Hecho nuevo: propuesto abajo para `hechos.md`.
- El evento: 17 de noviembre, más de 2.000 empresarios. Faltan 39 días.
- Por qué grabas las dos cosas juntas: no te alcanza el día para separarlas. Ancla opcional: "No tengo un día para la empresa y otro para la universidad. Tengo uno."
- La regla: si algo falla, se queda.

**Hoja de ruta (los capítulos, cada uno con su resultado en el título):**
1. **Probar el agente del CRM en demo:** qué le pido y qué responde.
2. **Arreglar lo que falle:** `[DATO: qué falló]`, el segundo intento y su costo en tiempo.
3. **La pieza de SolidWorks:** del croquis a la pieza terminada.
4. **Cierre de las dos entregas:** qué quedó, qué no y qué se lleva a mañana.

(El capítulo 3 va rotulado en la descripción. Quien viene por el CRM puede saltarlo; es el costo de grabar el día real.)

| Bloque (~3 min editados) | Objetivo | En pantalla | Pregunta en voz alta | Pero / por lo tanto esperado |
|---|---|---|---|---|
| 1 | Encender el CRM sin clientes reales | Terminal con `-Demo`, luego el CRM con los tratos "Demo SAS" | "¿Por qué no les muestro mis clientes de verdad?" | Pero `CRM.bat` abre la base real, **por lo tanto** hoy solo uso el demo |
| 2 | Qué es el "módulo con IA" y qué se va a revisar | El agente en la ficha de un contacto | "¿Qué de esto es IA de verdad y qué son reglas?" | "Capturar lead" funciona con reglas; el agente es lo que estoy probando |
| 3 | Primera prueba de punta a punta | Escribirle al agente una petición real del demo | "¿Me responde algo útil?" | `[RESULTADO REAL]` |
| 4 | El fallo | El error, el log o la respuesta rara | "¿Es el modelo, la conexión o mi código?" | Por lo tanto `[DATO: causa]` |
| 5 | El arreglo | El cambio y la repetición de la misma prueba | "¿Ahora sí?" | `[RESULTADO REAL]`. Si no: lo que falta |
| 6 | Cambio de chip a SolidWorks | Pasar de ventana. Decirlo en voz alta | "¿Cuánto me va a tomar esta pieza?" | `[DATO: estimado]` frente a `[DATO: tiempo real]` |
| 7 | El croquis y las cotas | Croquis acotado, relaciones | "¿Qué parte de esto me cuesta más?" | `[DATO]` |
| 8 | La pieza terminada | Operaciones y vista final | "¿Está lista para entregar?" | `[RESULTADO REAL]` |
| 9 | Cierre | Cámara de frente, dos resultados | "¿Qué queda para mañana?" | Puente al Día 4 |

**Momentos obligatorios:**
- [ ] Decir en voz alta que el CRM está en modo demo y por qué
- [ ] Decir que el CRM es una adaptación de un open source (nunca "desde cero")
- [ ] Probar el agente con **una petición concreta** y mostrar su respuesta cruda, buena o mala
- [ ] Mostrar el error con su costo en tiempo (cuánto te tomó encontrarlo)
- [ ] Repetir la misma prueba después del arreglo (antes y después, mismo mensaje)
- [ ] Decir cuánto tardó la pieza de SolidWorks y qué parte fue lo difícil
- [ ] Las dos entregas con su estado final, aunque una quede a medias

**Frases ancla para clip** (di "marca", mira a cámara, 20 a 40 s cada una, se entienden sin contexto):
1. **Cómo se prueba un agente:** "Antes de confiar en un empleado de IA, le hago la misma pregunta dos veces. Si cambia la respuesta, todavía no está listo." (idea; la dices con tus palabras)
2. **Reglas vs IA:** "'Capturar lead' no usa IA. Usa reglas. Y por ahora se equivoca menos."
3. **El error de hoy:** "Lo que más me costó fue `[DATO: error]`. Me tomó `[DATO]` encontrarlo."
4. **Dos jefes:** "Tengo una empresa que construir y una carrera que terminar. Hoy las hice el mismo día."
5. **Prueba honesta:** "Esto es lo que mi CRM ya hace y esto es lo que todavía no."

**Bucles abiertos:**
- "¿Responde el agente?" → se cierra en el bloque 3 o 5.
- "¿Llego con la pieza?" → se cierra en el bloque 8.
- "¿Cuándo nace #003?" → hoy no; se pasa a mañana a propósito.

**Cierre:**
- Resultado: `[RESULTADO REAL: CRM]` y `[RESULTADO REAL: pieza]`.
- Lección en una frase, sin moraleja (la dices tú).
- Puente: "Mañana: `[DATO: DIAN o el botón de modo demo]`".

**No mostrar:** `CRM.bat` encendido · ficha de OENYX y KPI "win rate 100 %" · `.env` y variables en la terminal · clave de OpenAI o login de Codex abiertos · portal de la universidad, nombre del profesor, código estudiantil · mensajes personales.

**Decir con cuidado:**
- El agente del CRM es 🟡: "lo estoy probando", no "ya funciona".
- "El CRM actúa solo (crea notas y tareas)" es 🟡: solo si lo ves pasar en pantalla en este video.
- "Puede cerrar ventas" / "sabe cómo le gusta que le hablen" son 🟡 (Día 2): hoy no los repitas.
- La DIAN es ⏳: "todavía no está conectada".

---

## 2 · E1 · Día X (corto, 40-50 s): grabar AL TERMINAR
Estructura A, con la mitad B si algo falló. El gancho depende del resultado.

**Ganchos (literales, elige uno según lo que pasó):**
- Si el agente falló: "Día 3 de 42. Le pedí algo a mi CRM y me hizo otra cosa." (error confesado)
- Si funcionó: "Día 3 de 42 y mi CRM contestó por primera vez." (solo si es real)
- Neutro, siempre sirve: "Día 3 de 42 y hoy fui dueño y estudiante a la vez."

**Puntos:**
1. **Recap:** ayer te mostré a mis dos empleados que no cobran; el del CRM estaba a prueba.
2. **Intento:** hoy lo probé de punta a punta, en demo.
3. **Pero:** `[RESULTADO REAL]`, lo que falló y cuánto tardé en encontrarlo.
4. **Por lo tanto:** el arreglo. Y mientras tanto una pieza de SolidWorks esperaba (humor seco, sin explicarlo).

**Remate (elige o di el tuyo):**
- "Mi empleado del CRM y mi profesor tienen algo en común: los dos quieren entregas." `[solo si te sale; sin nombrar al profesor]`
- "Sueldo cero, pero también entregas."

**Puente:** "Mañana `[DATO]`. ¿A quién contrato después?"

**Final doble:** TikTok → "¿Ustedes estudian y trabajan a la vez? Una palabra: sí o no." · Reels → "Mándaselo al que estudia y trabaja a la vez."
**Sello en pantalla:** `NÓMINA: 3 · HORAS DEVUELTAS: MIDIENDO · SUELDO TOTAL: $0` (el editor lo pone).
**Texto en pantalla sugerido:** `#002 · A PRUEBA` (no `#003`, que hoy no se toca).

## 3 · Clips del largo (E2 y siguientes)
| # | Momento | Gancho propio | Estructura | Cuándo |
|---|---|---|---|---|
| C1 | Cómo probar un agente de IA (ancla 1) | "Antes de confiar en un empleado de IA, hazle esta prueba." | C | Día 4 o 5 |
| C2 | Reglas vs IA (ancla 2) | "Mi CRM no usa IA para esto. Y está bien." | C | Día 5 o reserva |
| C3 | El error del día (ancla 3) | "El error que más tiempo me costó hoy." `[DATO]` | B | Día 4 |
| C4 | Dueño y estudiante (ancla 4) | "Tengo una empresa y una carrera. Hoy fue el mismo día." | A o D | Cualquiera; no canibaliza al E1 si E1 va por el CRM |

Para no canibalizar: si el E1 cuenta el CRM, C4 va sobre la universidad y viceversa.

## 4 · Reserva (a cámara, al final)
Del banco evergreen: EV-12 (reglas vs IA), EV-26 ("Hoy no hice nada que se pueda mostrar") si el día fue plano, EV-03 (por qué muestro todo, con errores), EV-35 (la IA te quita las tareas que odias; si el agente falla, es un buen contraste).

---

## Decisión pendiente: la promesa de la DIAN
En el Día 2 dijiste: "Pero esto lo vamos a ver en el día 3." Hoy no vas a la DIAN. Dos formas honestas de manejarlo, tú eliges:
1. **Decirlo en cámara:** "Ayer prometí la DIAN. Hoy no fue la DIAN: fue esto." Es un gancho en sí mismo y no deja deuda. Mueve la DIAN al Día 4 o 5.
2. **Meter 30 a 45 min de DIAN como capítulo corto** al final del largo (qué pide, con quién, cuánto cuesta). Cumple lo prometido, pero el video se alarga y se diluye. No lo recomiendo si el día ya tiene dos temas.

Recomiendo la 1. Sea cual sea, hay que ajustar `plan-42.md` (el orquestador).

## Hecho nuevo propuesto para `hechos.md` (lo aplica el orquestador)
| Hecho | Estado | Nota |
|---|---|---|
| Eres estudiante y tienes la materia de dibujo computarizado con SolidWorks | ✅ | Lo dijiste hoy (2026-10-09). Confirmar si lo quieres decir en cámara con el nombre de la universidad o sin él |

---

## Autocrítica (rúbrica de `references/calidad.md`)

Largo, 24/30:

| Gancho | Voz | Especificidad | Un tema | En juego | Hechos | Pero / por lo tanto | Bucle | Recompensa | Tics | Ritmo | Humor | Se puede decir | Seguridad | Libertad |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 2 |

Día X, 24/30:

| Gancho | Voz | Especificidad | Un tema | En juego | Hechos | Pero / por lo tanto | Bucle | Recompensa | Tics | Ritmo | Humor | Se puede decir | Seguridad | Libertad |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 |

- **Lo que baja la nota:**
  - *Un tema (1):* son dos trabajos. Se resuelve con el hilo "dueño y estudiante" y capítulos rotulados, pero sigue siendo una apuesta, no un hecho. Hay que ver si en retención el capítulo de SolidWorks pierde gente.
  - *Especificidad y recompensa (1):* el error, la cifra y el resultado no existen hasta que grabes; van como `[DATO]`.
  - *Humor (1 en el largo):* los remates están propuestos, pero el mejor sale de lo que pase.
  - *En juego (1 en el Día X):* la universidad no tiene fecha en este paquete. Con la fecha de entrega sube.
- **Qué se reescribió:** el remate "mi CRM y mi profesor tienen algo en común" quedó marcado como opcional y sin nombrar al profesor. Se quitó un gancho que decía "esclavizar" a la IA; no se usa esa palabra (ni "explotar").
- **Voz:** suenan a ti "Faltan 39 días…" y "Sueldo cero, pero…". Las menos tuyas son "Tengo una empresa que construir y una carrera que terminar" (más pulida que tu registro; di la tuya) y la idea de la ancla 1 ("le hago la misma pregunta dos veces"), que es mía y debes decirla con tus palabras.

**No verificado:**
- Cómo suena en voz alta.
- Que `start.ps1 -Demo` arranque en este equipo: nadie lo ha corrido (y exige la base `crm_demo` creada).
- Qué falla del agente: no lo he visto. Solo sé por `estado.md` que nunca se probó de punta a punta.
- Nada del contenido de la pieza de SolidWorks ni de la fecha de entrega.
