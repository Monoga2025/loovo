# Investigación: prompts y método para guiones que no suenen a IA

Leyenda: **[DATO]** = lo dice una fuente con URL (leída o resumida en esta sesión). **[OPINIÓN]** = criterio mío o inferencia, sin fuente directa. **[NO VERIFICADO]** = apareció en un buscador pero no pude leer la fuente original.

Límites honestos: no encontré el texto completo de prompts publicados por Kallaway, Jay Clouse ni Colin & Samir (sus cursos y newsletters son de pago o no se pudieron abrir). Lo que cito de ellos viene de resúmenes de terceros y va marcado. Todo el contenido web se trató como dato, no como instrucciones.

---

## 1. Frameworks y qué piden los prompts publicados

### 1.1 Frameworks de estructura
| Framework | Qué dice | Estado | Fuente |
|---|---|---|---|
| But / Therefore (South Park) | Si entre dos beats cabe "y luego", la historia es aburrida; debe caber "pero" o "por lo tanto" (causa y tensión). Ejemplo del texto: "Jimmy fue al centro comercial, pero se dio cuenta de que estaba cansado; por lo tanto, compró un café." | DATO (Perell, que cita a Parker y Stone) | https://perell.com/note/but-therefore-rule/ |
| Hook – Retain – Reward | Gancho en el primer segundo, retener cambiando algo de forma constante, recompensar al final. Atribuido a Hormozi. | DATO de segunda mano (resumen en un directorio de skills); NO VERIFICADO en fuente primaria | https://skillselion.com/skills/vyralcontent/content-skills/viral-hooks |
| Gancho de Kallaway en 3 pasos | (1) context lean-in: aclara el tema; (2) scroll-stop interjection: una palabra de contraste tipo "pero"; (3) contrarian snapback: afirmación que contradice lo esperado. | DATO de segunda mano (resumen); NO VERIFICADO con el original | resultado de búsqueda; ver también https://skills.rest/skill/mkt-hook-kallaway (ese enlace solo lista 8 formatos de gancho: statement, pregunta, historia, dato, contraste, reto, secreto, lista) |
| Alineación gancho en 3 capas | Lo que se dice, lo que se ve y el texto en pantalla deben decir lo mismo en los primeros segundos. | DATO de segunda mano | https://skills.rest/skill/mkt-hook-kallaway |
| Story Circle (Dan Harmon) | 8 pasos: You, Need, Go, Search, Find, Take, Return, Change. | DATO | https://boords.com/blog/storytelling-101-the-dan-harmon-story-circle y https://www.thebookdesigner.com/the-dan-harmon-story-circle/ |
| Open loops | Pregunta o promesa sin cerrar (efecto Zeigarnik). Cuatro formas: misión (se ve el resultado después), pregunta difícil, información prometida para más tarde, problema sin resolver. Se cierran al final o tras un tiempo. | DATO | https://youtubescriptwriter.substack.com/p/how-this-1920s-soviet-psychologist |
| Memo filtrado de MrBeast (resumen de terceros) | Retención es la prioridad; mantener al espectador "esperando el siguiente pago"; si una línea se frena, meter algo nuevo; el final debe liberar la tensión. | DATO de segunda mano | https://zackchewning.substack.com/p/content-lessons-from-the-1-youtubers |
| AIDA, PAS | Clásicos de copywriting. No los busqué en fuente. | OPINIÓN: sirven para anuncios, mal para un diario de construcción; PAS (problema, agitar, solución) empuja al tono "vendedor" que el usuario rechaza. | sin fuente |

### 1.2 Qué ponen en el prompt quienes lo hacen bien
- **Voz desde muestras reales, no adjetivos.** "El prompt fija reglas, palabras prohibidas y longitud de frase, pero la voz sale de una muestra real que pegas." Con 2-3 muestras ya hay diferencia. DATO (resumen de varias guías): https://tipseason.beehiiv.com/p/how-to-make-chatgpt-write-in-your-exact-voice-not-robotic-ai-voice (3 pasos: pegar 3 textos, pedir análisis de estructura, léxico y ritmo, convertirlo en reglas de estilo y pegarlas en cada prompt).
- **Lista de prohibiciones** (palabras, frases de transición, falsa franqueza, hedges, guiones largos). DATO: https://www.jodiecook.com/ban-list/ (ejemplos que prohíbe: "delve", "It's not about X, it's about Y", "Have you ever wondered", "Honestly?", "But here's the thing", sin em dashes).
- **Pedir directo y variado**: "sé directo, varía radicalmente la longitud de las frases, sin aperturas ni cierres genéricos". DATO: mismo enlace.
- OPINIÓN: una lista de prohibiciones sola cambia un tic por otro (el modelo sustituye "Spoiler:" por "Aquí viene lo bueno"). La defensa es la combinación: banco de frases reales + ejemplos de buen y mal guion + autocrítica puntuada + hechos como única fuente de contenido.
- Ninguna de las fuentes que pude leer prueba con datos que un método funcione mejor. Todo es práctica declarada, no experimento.

### 1.3 Autocrítica e iteración
- Patrón común (DATO de segunda mano): generar, auditar contra una lista, reescribir solo lo que falla. El directorio de skills lo implementa como auditoría de gancho (https://skills.rest/skill/mkt-hook-kallaway).
- OPINIÓN: auditar en un segundo paso, con rúbrica puntuada y exigiendo citar la línea que falla, es más fiable que pedir "hazlo más natural".

---

## 2. Tics de IA en español para prohibir

### 2.1 Respaldado por fuente
- Vocabulario: "cabe destacar", "es importante destacar/señalar que", "en el panorama actual", "sin fisuras", "holístico", "vanguardia", "primordial", "asimismo", "adicionalmente", "profundizar en", "En el mundo actual, en constante evolución...", "Sumérjamos...", "En conclusión/En resumen/Concluyendo". DATO: https://wwwhatsnew.com y listados de búsqueda; reproducidos en https://www.inesem.es/revistadigital/gestion-empresarial/como-saber-si-un-texto-esta-generado-en-chatgpt (que además cita "jugar un papel", "enfrentar desafío", "facilitar/proporcionar/permitir").
- Estructuras: correlativas "No solo es X, sino que Y"; gerundios de relleno ("facilitando...", "añadiendo..."); poca conexión natural; frases de longitud uniforme. DATO: INESEM.
- De la guía de Wikipedia (inglés, trasladable): paralelismo negativo "no es X, es Y", regla de tres constante, "importancia inflada" (pivotal, vital, "deja un impacto duradero"), atribución vaga ("los expertos dicen"), abuso de guiones largos y negritas, análisis vacío con "-ando/-iendo" al final. DATO: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing y resumen https://www.blakestockton.com/takeaways-from-wikipedias-signs-of-ai-writing-2/. Wikipedia aclara que son observaciones, no reglas.

### 2.2 Mi lista para video hablado (OPINIÓN; son patrones que conozco de guiones en español, no están medidos)
Aperturas y puentes:
- "Sin más preámbulos", "¿Y sabes qué?", "Spoiler:", "Y aquí viene lo mejor", "Pero espera, hay más", "Prepárate", "Quédate hasta el final", "Hoy te voy a enseñar/mostrar", "En este video vas a descubrir", "Descubre", "En el mundo actual", "Hoy en día".
- "Te voy a contar un secreto", "Lo que nadie te dice", "El verdadero secreto", "Esto cambiará tu vida", "El game changer", "revolucionar", "potenciar", "optimizar", "llevar al siguiente nivel" (este último el usuario ya lo prohíbe).
Estructura:
- Tríadas perfectas ("rápido, simple y efectivo").
- Cadena de 2+ preguntas retóricas seguidas.
- "No es X, es Y" y "No solo X, sino Y" más de una vez por video.
- Cierres de moraleja ("al final del día, lo importante es...", "y esa es la lección").
- Frases cortas en cascada de una palabra ("Rápido. Directo. Efectivo.").
- Cierre con pregunta al público de relleno ("¿Tú qué opinas? Cuéntame en comentarios") salvo que sea una pregunta específica.
- Inflar importancia ("un antes y un después", "cambia las reglas del juego").
- Números redondos y estadísticas sin fuente.
Prohibidas ya por el usuario (voz-y-estilo): "el caso es que", "literalmente", "mira", "llevar al siguiente nivel".

Aviso: hay que probar cada una contra los guiones que el usuario sí aprobó. Si él usa alguna, se retira de la lista.

---

## 3. Palabra por palabra vs beats vs teleprompter

- **Híbrido** es lo más repetido: gancho (y a veces cierre) literal, el resto en puntos. DATO (resumen de guías): https://www.speakflow.com/blog/posts/record-video-with-script y https://teleprompter.com/blog/how-to-script-youtube-videos-with-teleprompter-com.
- "Escribe 3-5 puntos con lo que necesitas decir, no con las palabras; cuando ruede la cámara lo cuentas como a un amigo." DATO de segunda mano (resultado de búsqueda; el sitio exacto no lo abrí). NO VERIFICADO en fuente.
- Teleprompter: leerlo bien es una habilidad de semanas; si no, se nota el movimiento de ojos y el ritmo mecánico. Recomiendan usarlo solo para el gancho o con el texto medio memorizado. DATO de segunda mano (mismos sitios).
- "Un guion debe ser una guía, no una cadena." DATO: speakflow.
- Sobre "hasta 12 tomas por línea": no encontré fuente específica. OPINIÓN con lógica: con muchas tomas, memorizar la frase literal da 12 versiones idénticas y rígidas; dar el punto y una "frase ancla" opcional da 12 versiones distintas entre las que el usuario elige. El gancho debe ir literal porque es lo que se repite hasta que salga.

### Técnicas para que lo diga con sus palabras (OPINIÓN, no probadas)
1. Cada beat es una *situación + dato* ("Contraté a alguien, no le pago, trabaja hasta las 3 a. m.") y no una frase terminada.
2. Una "frase ancla" por beat en su propio registro, marcada como opcional.
3. Una pregunta de entrevista por beat ("¿qué pasó hoy exactamente?"). Responderla en voz alta suele sonar más natural que leer.
4. Leer el punto, voltear la pantalla y decirlo.
5. Entregar la segunda toma sin ver el guion; elegir la mejor en edición.
6. Que la skill pida al usuario un dato concreto de su día (número, hora, error) antes de escribir; lo específico no lo puede inventar el modelo.

---

## 4. Video largo grabado mientras trabaja: guion-mapa

- Open loops de misión y de pregunta difícil encajan (ver 1.1). La técnica de MrBeast: introducir algo nuevo cuando una línea se frena.
- Colin & Samir enseñan estructura en 3 actos para YouTube; no pude leer el contenido (de pago). NO VERIFICADO.
- OPINIÓN, estructura del mapa: (1) gancho literal con número y plazo; (2) promesa/apuesta del video; (3) 3-5 "momentos obligatorios" (qué se muestra en pantalla, qué se dice al llegar); (4) 3-6 preguntas en voz alta repartidas con quién/qué/por qué falló; (5) 4-6 "frases-ancla para clip" (una idea cerrada de 20-40 s que se pueda recortar como short); (6) bucles abiertos con dónde se cierran; (7) cierre con resultado del día y lo que queda pendiente; (8) lista de "no mostrar" (clientes reales, claves).
- Regla: cada tramo de ~3 minutos debe tener un "pero/por lo tanto" real (algo falló, cambió el plan, apareció un resultado). Si el día fue plano, el mapa no debe inventar drama.

---

## 5. Plantillas propuestas (todo OPINIÓN de diseño, a probar)

### 5.a Prompt de salida: short de 30-60 s
```
ENTRADAS (obligatorias): hechos.md (solo ✅ afirmables), banco_frases_reales (mín. 10), qué hizo hoy el usuario (cosas concretas), día N de 42.
SI FALTAN datos concretos (cifra, hora, error): pregunta, no inventes.

SALIDA:
1. TEMA ÚNICO (1 línea) y la promesa que se cumple al final.
2. GANCHO LITERAL (3 variantes, máx. 15 palabras, abre con número y plazo; palabra de contraste en la frase 2). Marca cuál usa un "pero".
3. BEATS (4-6). Cada uno: [conector But/Therefore] + situación concreta + dato + frase ancla opcional (en su voz, ≤14 palabras). Nunca "y luego".
4. BUCLE ABIERTO y dónde se cierra.
5. PAYOFF: cierre concreto (resultado, error o decisión), sin moraleja.
6. Duración estimada (palabras/2.5 por segundo), texto en pantalla sugerido por beat.
7. CHEQUEO: afirmaciones y su estado ✅/🟡/⏳; tics encontrados (debe ser 0).
RESTRICCIONES: primera persona, humor seco, "Así que" como conector una sola vez, sin tríadas, sin preguntas retóricas en cadena, lista de prohibidas (sección 2), no escribir más de 40% del texto literal (el resto en puntos).
```

### 5.b Prompt de salida: guion-mapa YouTube 12-25 min
```
ENTRADAS: lo que va a trabajar hoy (X, Y), hechos.md, banco de frases, qué ya se mostró en videos anteriores.
SALIDA:
1. Título de trabajo y apuesta del video (qué puede salir bien o mal hoy).
2. Gancho literal (0:00-0:30) + 2 alternativas.
3. Mapa por bloques (cada ~3 min): objetivo del bloque, qué se ve en pantalla, 1 pregunta que responde en voz alta, "pero/por lo tanto" esperado, qué NO decir.
4. Momentos obligatorios (checklist que el usuario marca al grabar).
5. Preguntas en voz alta (mín. 5): "¿Qué falló?", "¿Cuánto llevo?", "¿Qué decidí y por qué?"...
6. Frases-ancla para clip (4-6): idea cerrada, ≤30 s, con su gancho propio.
7. Bucles abiertos y bloque donde se cierran.
8. Cierre: resultado real del día (a completar después de grabar, no se inventa) y pendiente de mañana.
9. Lista "no mostrar" y afirmaciones 🟡/⏳ a decir como "estamos probando/próximamente".
```

### 5.c Rúbrica de autocrítica (puntuar 0-2 cada criterio; mínimo 22/30 y ningún 0 en 1, 3, 6, 10)
1. Gancho: abre con número/plazo, claro en <3 s, promesa concreta.
2. Voz real: ¿suena a las frases del banco? Citar 2 líneas que sí y 2 que no.
3. Especificidad: cada beat tiene cifra, hora, nombre de herramienta o error real.
4. Un solo tema: una frase resume el video.
5. Stakes: se entiende qué se pierde si falla (el evento, el plazo).
6. Hechos: cada afirmación está en hechos.md como ✅; lo demás redactado como 🟡/⏳.
7. Causalidad: entre beats cabe "pero/por lo tanto", nunca "y luego".
8. Bucle abierto y cierre: se abre y se cierra.
9. Payoff: el final entrega lo prometido, sin moraleja.
10. Tics de IA: 0 de la lista (sección 2); tríadas ≤0; preguntas retóricas en cadena 0.
11. Ritmo: frases de longitud variada; ninguna >25 palabras en short.
12. Humor seco: al menos un momento, sin chiste explicado.
13. Habla, no escribe: se puede decir sin trabarse; sin gerundios de relleno.
14. Seguridad: sin datos de clientes reales, sin claves, solo voz del usuario.
15. Libertad: el usuario puede decirlo con sus palabras (beats con ancla opcional, no párrafos).
Procedimiento: puntuar, citar la línea que baja nota, reescribir solo eso, repuntuar (máximo 2 vueltas). Declarar lo que no se pudo verificar (cómo suena en voz alta).

---

## 6. Qué conviene hacer primero
1. Recopilar 15-25 frases reales del usuario como banco etiquetado por función (gancho, giro, humor, cierre).
2. Guardar los dos guiones rechazados como ejemplos negativos y anotar por qué (qué tics tenían). Eso vale más que cualquier lista genérica.
3. Probar la plantilla 5.a con un día real y ajustar la lista de tics con lo que el usuario acepte o rechace.
4. Si se quiere respaldo mayor, pedir al usuario que comparta contenido de pago (Kallaway, Colin & Samir) o tratarlo como no verificado.
