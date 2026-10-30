# 5 videos — los repos del video «5 Sistemas IA que se Venden por +$3,000 en USA»

**Fuente:** [dHyIWdqZgqw](https://www.youtube.com/watch?v=dHyIWdqZgqw) — Código Maestría, «5 Sistemas IA que se Venden por +$3,000 en USA (cópiame)».

**Qué es esto:** el material para grabar 5 videos temáticos para el público del Luque Business Summit. **No son «Día X».** No tocan la serie de 42 días.

**Cómo se usa:** el gancho va literal (dilo como está o cámbialo, pero es el ángulo). Los puntos son para hablar tú, no para leer.

---

## Los 5 sistemas del video

| # | Sistema | Repo real | Estrellas (verificado 2026-10-12) | Precio que el video pone |
|---|---|---|---|---|
| 1 | Cámaras de seguridad con IA | **Frigate** | 36.523 | $5.000 + $200–500/mes |
| 2 | Editor de video automático | **HyperFrames** | 61.587 | $2.000–5.000 + $500–2.000/mes |
| 3 | Todos los mensajes en un sitio, con IA | **Chatwoot** | 37.734 | $2.000–10.000 + $300–1.500/mes |
| 4 | Recepcionista de voz que contesta 24/7 | **Pipecat** | 16.395 | $3.000–10.000 + $500–2.000/mes |
| 5 | Pedidos para restaurantes | **no identificado** | — | $2.500 + $2.500 + $200–1.000/mes |

**Los cinco son gratis y open source.** El video lo dice sin rodeos: *«Lo difícil no es crear el sistema, es saber a quién vendérselo.»*

**El sistema 5 no está identificado.** El subtítulo automático lo escribe como «Ignider» y «Overage», y ninguna de las dos existe. **Ábrelo en el minuto 12:25 del video y lee el nombre en pantalla antes de grabarlo.**

**Antes de vender cualquiera: lee su `LICENSE`.** Frigate (MIT), HyperFrames (Apache-2.0) y Pipecat (BSD-2) permiten uso comercial. **Chatwoot aparece como «NOASSERTION»**: hay que leer su licencia antes de venderlo. Detalle en `guiones/investigacion/repo-video/INDICE-REPOS.md`.

## El argumento del video que es tu argumento

El video dice, en el minuto 22:

> *«Las empresas no quieren aprender a instalar ni aprender de Claude. Las empresas lo que quieren son más clientes, más dinero. Compran resultados.»*
> *«El problema no es qué vendes, el problema es a quién le vas a vender y cómo.»*

Tú ya dices lo mismo con tus palabras, sobre tu propio negocio:

> Una cita demuestra que una página dijo algo; no demuestra que la norma aún aplica.

**Lo gratis es la herramienta. Lo que se paga es el criterio y la responsabilidad.** Ese es el puente entre tu contenido y este video, y es el ángulo de los 5 videos.


---

## El ángulo que te corresponde a ti (léelo antes de grabar)

El video es de alguien que **vende** los repos. Tú estás en otra posición, y es mejor:

> **Tú estás construyendo tu propia agencia delante de la cámara y decides qué metes y qué no.**

Eso te da un ángulo que el autor del video no puede usar: **el filtro**. No «compra esto», sino «esto lo probé, esto lo descarté y esta es la razón». Es tu promesa del Día 1 (*«qué decisiones tomamos y qué sale mal»*) aplicada a los repos.

Y tienes una ventaja concreta y verificable: **ya usas HyperFrames en producción** desde el Día 1. Eres usuario real de uno de los cinco, no alguien que los recomienda de oídas.

---

## Video 1 — Frigate: el casco y la dotación

**El que pediste.** Es el sistema #1 del video.

### Gancho (opciones literales)

**A**
> Tu empresa exige casco y dotación, pero nadie comprueba si de verdad los usan. Ese es el trabajo que más se evade en una obra. Y hoy te voy a mostrar el sistema que lo revisa solo, con las cámaras que ya tienes.

**B**
> Un sistema de cámaras con IA que revisa si tu gente lleva casco cuesta instalado más de cinco mil dólares. El software es gratis. Hoy te explico qué parte es gratis, qué parte hay que hacer y por qué pagan por la segunda.

**C**
> Antes de venderte algo, te voy a decir la verdad: la detección de casco no viene hecha. Hay que entrenarla. Y eso cambia por completo el negocio y el precio.

*(Recomiendo la C. Es la única que no te obliga a prometer algo que no tienes todavía, y te posiciona como el que dice la verdad.)*

### Puntos

1. **El problema, con tus palabras.** Una empresa pide casco y dotación por norma. Nadie audita. El jefe de seguridad sabe que se incumple y no tiene forma de probarlo.
2. **Qué es Frigate, en una frase.** Software libre de cámaras que ya reconoce objetos en el video: persona, carro, animal. No es una cámara nueva; es lo que le pones a las que ya tienes.
3. **La demostración.** Enseñas una persona en pantalla y el sistema detectando. Luego un carro. Luego un animal.
4. **El giro honesto, que es el video entero.** Frigate trae `person`, no trae `casco`. Para casco hay que **entrenar un modelo propio** y Frigate admite modelos YOLO personalizados. Eso significa: datos de tu planta, alguien que etiquete, alguien que entrene, y pruebas hasta que acierte.
5. **La parte que sí cobras.** Lo gratis es el software. Lo que se paga es que alguien lo configure, lo ajuste a esa planta, verifique que no da falsos positivos y lo deje corriendo. Ahí está el negocio, y ahí está el trabajo.
6. **Tus límites, dichos en cámara.** Aún no tienes un cliente con esto montado. Si lo dices, el video gana credibilidad en vez de perderla.
7. **Cierre.** Invitación a hablar con quien tenga ese problema concreto: obra, planta, bodega.

### Solo puedes afirmar esto

| Puedes decir | Respaldo |
|---|---|
| Frigate es software libre y open source | Es un repo público |
| Detecta objetos en video de cámaras IP | Documentación oficial |
| Admite modelos YOLO personalizados | Documentación y comunidad de Frigate |
| El casco no viene por defecto: hay que entrenar y validar | Documentación: trae las clases estándar |
| Empresas en USA pagan más de $3.000 por instalarlo | Lo dice el video que estás siguiendo (es su afirmación, no tu medición) |

### NO puedes decir esto

| Prohibido | Por qué |
|---|---|
| «Tengo el sistema de casco funcionando» | No existe en ningún documento tuyo. Cero. |
| «Detecto si un empleado lleva uniforme o dotación completa» | Igual. No existe. Y la dotación es más difícil que el casco. |
| «Ahorra X% en accidentes» o «evita multas por X» | Cifra inventada. Tu regla: «pendiente de medir». |
| «Lo instalo en una tarde» | El video lo dice de los repos; tú no lo has hecho. No lo repitas como tuyo. |
| «40 horas, 100% en producción» | Es tu web actual, y tu propia auditoría la marca como no verificada. |
| Dar nombres de clientes | Nadie te ha autorizado. |

### Si quieres que el video sea **demostrable** (recomendado)

No afirmes el casco: **enséñalo como experimento**. Grabación de la sesión donde intentas entrenar el detector de casco y cuentas qué sale. Eso:
- no promete nada,
- es contenido que nadie más tiene,
- y si funciona, tienes el video Y el producto a la vez.

---

## Video 2 — HyperFrames: el editor que ya usas

**Este es tu video más fuerte, porque lo usas de verdad.**

### Gancho (opciones literales)

**A**
> Hay un software gratis que edita videos con IA y en Estados Unidos cobran hasta cinco mil dólares por instalarlo. Yo lo uso desde el primer día de este reto para editar mis propios videos. Hoy te enseño lo que hace y lo que no.

**B**
> Mis videos los edita una máquina por unos pocos pesos. No es un servicio que pago: es un programa gratis que corre en mi computador. Este es el sistema número dos de los que se venden por miles de dólares en USA.

**C**
> Te voy a mostrar cómo pasé de siete minutos de grabación a un video de treinta y ocho segundos sin tocar un editor. Y te voy a decir cuánto me costó: cero.

### Puntos

1. **La prueba concreta que ya tienes.** El Día 1: **7 minutos 37 segundos de grabación → 38 segundos editados.** Eso es un hecho ✅ de tu propio `hechos.md`. Es tu mejor dato y es tuyo.
2. **Qué es.** Un editor donde la animación se escribe en código (HTML), no se arrastra con el mouse. Por eso un agente de IA puede editarlo.
3. **Enseñar en pantalla.** Tu composición, tus escenas, el render. Aquí tienes horas de trabajo real que mostrar.
4. **Lo que de verdad cuesta.** No es el programa, es el criterio: qué cortar, qué ritmo, qué texto. Lo aprendiste a golpes y está en tus `aprendizajes.md` (LUFS, viñeta, el fotograma de portada con la boca cerrada). **Eso es lo que no viene en el repo.**
5. **El giro honesto.** No es mágico: el render se atascó al 82% y tuviste que usar el plan B. Lo cuentas. Ese detalle vale más que cualquier promesa.
6. **Cierre.** «Si quieres que te muestre cómo monté esto, dímelo.»

### Solo puedes afirmar esto

| Puedes decir | Respaldo |
|---|---|
| Lo usas para editar tus videos de la serie | `Dia-01` a `Dia-04`, versiones fijadas `0.8.140` y `0.8.141` |
| Pasaste 7 min 37 s a 38 s | `hechos.md`, estado ✅ |
| Es gratis y open source | Repo público |
| En USA se cobra entre $2.000 y $5.000 por instalarlo | Lo dice el video (su afirmación, no tu medición) |
| Un agente de IA puede editarlo porque es código | Tu experiencia real |
| Hubo que usar un plan B por un render atascado | `aprendizajes.md` |

### NO puedes decir esto

| Prohibido | Por qué |
|---|---|
| «Vendo edición de video» | Tu propia regla: el video es marketing propio, no servicio a terceros |
| «Lo instalo para clientes» | No lo has hecho para nadie |
| «Edito un video profesional en 5 minutos» | Tu experiencia real: 38 s de video = trabajo de una sesión |

---

## Video 3 — Cómo se cobra algo que es gratis

**Este es el video que habla con el empresario, no con el técnico.** Es el más útil para el Summit.

### Gancho (opciones literales)

**A**
> ¿Por qué una empresa paga tres mil dólares por un programa que puede descargar gratis? La respuesta es la misma por la que pagas por un contador en vez de usar la calculadora del celular.

**B**
> Un sistema de IA gratis que se vende por miles de dólares. Suena a estafa y no lo es. Hoy te explico exactamente qué está pagando esa empresa, porque entenderlo cambia cómo vendes.

**C**
> Si eres empresario, esto te va a doler un poco: lo que te venden caro casi nunca es el programa. Es que alguien se haga responsable de que funcione en tu empresa.

### Puntos

1. **La aparente trampa.** Software libre, precio alto. No es incoherencia.
2. **Qué paga de verdad una empresa.** Instalación, configuración con su caso, que no dé falsos positivos, que alguien responda cuando falle, y que quede funcionando sin que nadie de la empresa aprenda a programar.
3. **Tu paralelo, que ya está en tu material.** Un contador no cobra por buscar la norma, cobra por decidir si aplica. Aquí igual: no cobras por el repo, cobras por el criterio.
4. **El error del empresario.** Pensar que «es gratis, lo instala mi sobrino». El sobrino lo instala; nadie responde por él.
5. **El error del que vende.** Prometer resultados. Tú tienes la regla opuesta y es tu ventaja: *«no prometemos aumento de ventas, medimos»*.
6. **Cierre.** Pregunta al espectador: qué proceso de tu empresa nadie audita hoy.

### Solo puedes afirmar esto

- Tu regla propia: no prometer métricas, medir.
- El paralelo del contador (es tuyo, está en tu material).
- Que los repos son gratis y públicos.

### NO puedes decir esto

- Cifras de conversión o de ingresos del sector.
- Que tú ya cobras eso.
- «Las empresas pagan $3.000» como si fuera tu medición: es del video.

---

## Video 4 — La recepcionista de voz (Pipecat)

**Cuidado: aquí tienes material histórico envenenado.** Lee la advertencia antes.

### Advertencia importante

Tu material tiene un episodio feo con esto: se promocionó una **recepcionista de IA telefónica** que tu propio diagnóstico reconoce como **no lista**, y el motor que había detrás no era telefónico. Eso está en tu historial y **no se puede repetir de ninguna forma**.

Por eso este video solo funciona de una manera: **como análisis técnico del repo**, no como oferta.

### Gancho (opciones literales)

**A**
> En Estados Unidos se venden recepcionistas de voz con IA que contestan 24/7. El software es gratis y se llama Pipecat. Hoy te explico cómo funciona de verdad, y por qué yo todavía no lo ofrezco.

**B**
> Una IA que contesta tu teléfono y agenda citas. Suena fácil. Hoy te muestro la cantidad de piezas que hacen falta para que eso no sea un desastre con tus clientes.

### Puntos

1. **Qué hace Pipecat.** Conecta voz, transcripción y modelo para que una IA converse por voz en tiempo real.
2. **Las piezas que nadie cuenta.** Teléfono real, transcripción en vivo, respuesta natural, saber callarse, transferir a una persona, y responder solo lo aprobado.
3. **Por qué es peligroso hacerlo mal.** Una IA que promete un precio equivocado o agenda una cita falsa le cuesta clientes a la empresa. Por eso tu propio método pone la aprobación humana antes de enviar.
4. **El estado real de tu caso.** «Estamos estudiando si es viable para un caso concreto.» Nada más.
5. **Cierre.** Pregunta: ¿cuántas llamadas pierde tu negocio fuera de horario?

### NO puedes decir esto, en ninguna forma

- Que tienes una recepcionista de IA funcionando.
- Que contesta llamadas, agenda o cotiza.
- Ningún nombre del material histórico relacionado con esto.
- Que es rápido de montar.

---

## Video 5 — Chatwoot o el sistema de pedidos

**Decide uno según lo que puedas demostrar.** Si no puedes demostrar ninguno en pantalla, este video es el que se cae.

### Gancho (opciones literales)

**A (Chatwoot)**
> Todos los mensajes de tu negocio —WhatsApp, Instagram, correo— en una sola pantalla, con IA que ayuda a responder. El software es gratis. Hoy te enseño qué resuelve y qué no.

**B (pedidos)**
> Un restaurante paga hasta un 30% de comisión a las apps de domicilio. Hay un sistema abierto que se lo quita. Hoy te explico la trampa: no es solo instalar el software.

### Advertencia para el B

Ese «30%» **no es tuyo**, es del video. No lo digas como dato propio. Y tu material dice que WhatsApp **no existe** en tu CRM (⏳): no sugieras que ya lo tienes.

### Puntos (Chatwoot)

1. El problema real: los mensajes repartidos en cinco sitios y nadie contesta a tiempo.
2. Qué es Chatwoot y qué unifica.
3. **Tu límite, dicho claro:** tu CRM todavía no lee WhatsApp. Lo estás construyendo en la serie. Esto es otra cosa y la estás evaluando.
4. La regla que no se negocia: respuestas aprobadas por el dueño, y una persona aprueba antes de enviar.

---

## Resumen: qué grabar primero

| Orden | Video | Por qué |
|---:|---|---|
| 1 | **HyperFrames** | Es el único donde eres usuario real con pruebas y horas de pantalla. Cero riesgo. |
| 2 | **Frigate / casco como investigación** | El que pediste. Como experimento es honesto y potente. |
| 3 | **Cómo se cobra algo gratis** | El que más le sirve al empresario del Summit. |
| 4 | **La recepcionista de voz** | Solo análisis técnico. Máximo cuidado. |
| 5 | **Chatwoot o pedidos** | El más flojo hasta que puedas demostrar algo en pantalla. |

---

## Reglas que valen para los 5

1. **Ningún dato de una empresa real en pantalla.** Modo demo, datos ficticios. Siempre.
2. **Ninguna cifra sin fuente.** Si es del video, di «el video dice». Si es tuya, tiene que estar en `hechos.md`.
3. **Ninguna capacidad que no exista hoy.** Ni casco, ni voz, ni WhatsApp.
4. **El «aún no» es tu mejor material.** Dilo: «esto todavía no lo tengo».
5. **Tu voz, no la del video.** Abres fuerte sin saludar, primera persona, conector «Así que», contraste «normalmente… en cambio», cierras invitando.
6. **No uses:** «el caso es que», «literalmente», «mira», «llevar al siguiente nivel» — igual que no lo usas en la serie.
