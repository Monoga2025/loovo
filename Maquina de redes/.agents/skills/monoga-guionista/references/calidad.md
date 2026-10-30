# Calidad: palabras prohibidas y rúbrica

Fuente: `00_Serie/guiones/investigacion/prompts_guiones.md`. Si el usuario dice en cámara alguna palabra de esta lista, se saca de aquí: manda su voz.

## Prohibidas (tics de IA y palabras que no son suyas)
- **Del usuario:** "el caso es que", "literalmente", "mira", "llevar al siguiente nivel", "documentar absolutamente todo".
- **Vocabulario:** "cabe destacar", "es importante señalar", "en el panorama actual", "en el mundo actual", "hoy en día", "sin fisuras", "holístico", "vanguardia", "primordial", "asimismo", "adicionalmente", "profundizar", "sumergirnos", "potenciar", "optimizar", "revolucionar", "game changer", "un antes y un después", "cambia las reglas del juego", "en conclusión", "en resumen".
- **Aperturas y puentes:** "sin más preámbulos", "¿y sabes qué?", "spoiler:", "y aquí viene lo mejor", "pero espera, hay más", "prepárate", "quédate hasta el final", "hoy te voy a enseñar", "en este video vas a descubrir", "descubre", "te voy a contar un secreto", "lo que nadie te dice", "esto cambiará tu vida".
- **Estructuras:**
  - tríadas perfectas ("rápido, simple y efectivo");
  - 2 o más preguntas retóricas seguidas;
  - "no es X, es Y" o "no solo X, sino Y" más de una vez por guion;
  - cascadas de una palabra ("Rápido. Directo. Efectivo.");
  - cierres de moraleja ("al final del día…", "y esa es la lección");
  - gerundios de relleno al final de una frase;
  - "¿tú qué opinas? Cuéntame en comentarios" (la pregunta tiene que ser concreta);
  - cifras redondas sin fuente.
- **Moderación:** "esclavizar", "esclavo", "explotar", "látigo".

Ojo: él sí enumera en cuatro ("los servicios, cómo los armamos, cómo los construimos, qué decisiones tomamos"). Una enumeración suya larga e irregular está bien. La que suena a IA es la tríada pulida de adjetivos.

## Regla pero / por lo tanto
Entre dos puntos seguidos debe caber "pero" o "por lo tanto", nunca "y luego". Si solo cabe "y luego", el punto sobra o falta un conflicto.

## Rúbrica (cada criterio vale de 0 a 2; aprueba con 22 de 30 y sin ningún 0 en 1, 3, 6, 10 ni 14)
1. **Gancho:** el número, el plazo o la tensión se entiende en menos de 3 s, con una promesa concreta.
2. **Voz real:** suena al banco de frases. Cita 2 líneas que sí suenan a él y 2 que no.
3. **Especificidad:** cada punto tiene una cifra, una hora, el nombre de una herramienta o un error real (o un `[DATO]` pendiente).
4. **Un solo tema:** el video se resume en una frase.
5. **Lo que está en juego:** se entiende qué se pierde si falla (el evento, el plazo).
6. **Hechos:** cada afirmación es ✅. Lo demás está redactado como 🟡 ("estoy probando") o ⏳ ("voy a").
7. **Causalidad:** se cumple la regla pero / por lo tanto.
8. **Bucle:** se abre una pregunta y se cierra (o se pasa a mañana a propósito).
9. **Recompensa:** el final entrega lo prometido, sin moraleja.
10. **Tics:** cero palabras de la lista de prohibidas.
11. **Ritmo:** frases de largo variado, ninguna de más de 25 palabras en un corto.
12. **Humor seco:** al menos un momento, sin explicar el chiste.
13. **Se puede decir:** se dice sin trabarse y sin gerundios de relleno.
14. **Seguridad:** sin datos de clientes reales ni claves, solo la voz del usuario y el CRM en modo demo.
15. **Libertad:** puntos con frase ancla opcional, no párrafos. Como mucho el 40 % del texto es literal.

Procedimiento:
1. Puntúa los 15 criterios.
2. Cita la línea que baja la nota.
3. Reescribe solo esa línea.
4. Vuelve a puntuar. Máximo 2 vueltas.
5. Muestra el puntaje final en la entrega.

Para un mapa de YouTube, los criterios 11 y 15 se miden sobre el gancho y las frases ancla, no sobre los bloques.
