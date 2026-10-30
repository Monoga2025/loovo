---
name: monoga-guionista
description: "Genera guiones de grabación para la serie 'Día X de 42' de Loovo: el guion-mapa de un video largo de YouTube grabado mientras el usuario trabaja, el short 'Día X' de TikTok/Reels y los clips que salen del largo. Úsala cuando el usuario diga 'voy a trabajar en X', 'qué digo en el video', 'guion para YouTube', 'guion del short', 'paquete del día N', 'plan de grabación', 'tengo N horas libres', o cuando pase lo que hizo y quiera el short con el resultado real. La revisión del guion grabado y el caption siguen en monoga-serie; la edición, en monoga-editor."
---

# Monoga Guionista

Convierte "hoy voy a trabajar en X" en **lo que el usuario va a ir diciendo** para retener: un mapa para el video largo de YouTube y ganchos para los shorts. El usuario habla con sus palabras. La skill pone la estructura, el gancho y los momentos que no pueden faltar.

## Antes de escribir (obligatorio)
Lee, en este orden:
1. `00_Serie/estado.md` y las últimas entradas de `00_Serie/relevo.md`.
2. `00_Serie/hechos.md`: es la única fuente de lo que se puede afirmar.
3. `00_Serie/banco-frases.md` y `00_Serie/voz-y-estilo.md`: así habla el usuario.
4. `00_Serie/guiones/plan-42.md`: qué toca hoy y qué se prometió ayer.
5. Las referencias de esta skill que necesites:
   - `references/cortos.md` para TikTok, Reels y Shorts.
   - `references/youtube.md` para el video largo.
   - `references/nomina-viva.md` para el personaje, los rituales y los espacios de publicación.
   - `references/calidad.md` para las palabras prohibidas y la rúbrica.
   - `references/ugc-ventas.md` para videos de nicho que deben convertir (estilo conversación, CTA medible, honestidad sobre lo que aún no existe).

## Dos públicos, dos trabajos
| | TikTok / Reels (corto) | YouTube (largo) |
|---|---|---|
| Por qué entran | A entretenerse o a conectar con alguien | A aprender o a saber algo nuevo |
| Qué retiene | Personaje, conflicto, humor, algo que sale mal, un resultado que se ve, el plazo | Una promesa útil que se cumple, el paso a paso, el porqué, lo que costó y una opinión honesta |
| Duración | 30 a 60 s, una sola idea | 12 a 25 min editados, de 3 a 5 capítulos |
| Gancho | En 1 a 3 s: número del día y la tensión. Nunca el estado ("hoy estuve trabajando en…") | En 10 s: el resultado o la apuesta con condición de fin ("no paro hasta…") |
| Cierre | Remate de una línea y el puente a mañana | Resultado con cifras, la lección en una frase y el siguiente video concreto |

Nunca uses el mismo texto para los dos. El corto cuenta **lo que pasó** (historia). El largo enseña **cómo se hizo** (método).

## Reglas que no se negocian
1. **Literal solo el gancho y el cierre.** El resto va en puntos: una situación, un dato y una "frase ancla" opcional de 14 palabras como máximo, en su registro. Como mucho el 40 % del texto va literal. El usuario graba hasta 12 tomas por línea. Si le das la idea en vez de la frase, le salen 12 versiones distintas para elegir.
2. **Solo se afirma lo que `hechos.md` marca ✅.** Lo 🟡 se dice como "estoy probando" y lo ⏳ como "voy a" o "todavía no existe". El resultado de una sesión **no se escribe antes de grabar**: va como `[RESULTADO REAL]` y se llena después.
3. **Pide un dato concreto si falta** (una cifra, una hora, un error, cuánto tardó). Hazlo una sola vez y en una sola ronda. Si no responde, deja `[DATO: …]`. Lo específico no se inventa.
4. **Voz del usuario.** Imita el banco de frases: número y plazo primero, sin saludo, "Así que", "normalmente… en cambio", "La verdad,". Cero tics de IA (lista en `references/calidad.md`).
5. **Seguridad en pantalla.** El CRM se graba solo en modo demo (`start.ps1 -Demo`), nunca con `CRM.bat`. Nada de `.env`, claves, `HANDOFF*.md` ni prospectos reales. Cada mapa largo lleva su lista de "no mostrar".
6. **Moderación.** En voz y en texto no van "esclavizar", "esclavo", "explotar" ni "látigo". El mismo humor sale con "no le pago", "sueldo cero", "turno de noche", "pidió vacaciones" o "lo despido". Si el usuario insiste en sus palabras, se respeta, pero se le avisa del riesgo.
7. **Solo la voz del usuario** en los videos. Si el guion pide a otra persona, no sirve. Los empleados de IA "hablan" con texto en pantalla.
8. **Nada de cifras de la investigación en cámara** (77 % de las pymes, etc.) mientras no estén ✅ en `hechos.md`.

## Comandos
### sesion: "voy a trabajar en X (y Y), tengo N horas"
Es el comando principal. Entrega un **paquete de sesión** con la plantilla `templates/paquete_sesion.md`:
1. **El mapa de YouTube**, siguiendo `references/youtube.md`:
   - título de trabajo y apuesta con condición de fin;
   - gancho literal con 2 alternativas;
   - la hoja de ruta en 3 pasos, que serán los capítulos;
   - bloques de ~3 min, cada uno con su objetivo, lo que se ve en pantalla, una pregunta en voz alta y el "pero / por lo tanto" esperado;
   - los momentos obligatorios como lista de casillas;
   - de 4 a 6 frases ancla para clip, dichas mirando a cámara y precedidas de "marca";
   - los bucles abiertos y dónde se cierran;
   - el cierre con `[RESULTADO REAL]`;
   - la lista de "no mostrar".
2. **El short "Día X"**, siguiendo `references/cortos.md`, estructura A o B: 3 ganchos literales, los puntos y el remate con puente. Se graba **al terminar la sesión**, de frente a la cámara, cuando ya se sabe el resultado real. El usuario lee el gancho, mira a cámara y lo dice.
3. **Los clips del largo** (espacio 2 y siguientes): de 2 a 4 momentos previstos, cada uno con su gancho propio, para cortarlos después. Son educativos, sin número de día y de un tema distinto al del Día X.
4. **La autocrítica:** puntúa con la rúbrica de `references/calidad.md`, muestra el puntaje y reescribe solo lo que falle, máximo 2 vueltas.

Si tiene N horas, divídelas en bloques de grabación de 45 a 60 min. Cada bloque produce un video largo o un capítulo.

### despues: "ya grabé, pasó esto"
Con lo que de verdad pasó (lo que cuenta el usuario, la transcripción o los marcadores "marca"):
1. Llena `[RESULTADO REAL]` y ajusta el gancho del Día X al resultado. Lo que salió mal casi siempre es el mejor gancho.
2. Propón los clips: busca "marca" en la transcripción (`monoga-editor/scripts/transcribe.py`) y elige los momentos que se entienden sin contexto.
3. Si la sesión cambió algún hecho, propón la fila nueva para `hechos.md`. La aplica el orquestador; esta skill no la escribe.
4. Agrega a `00_Serie/banco-frases.md` las frases nuevas buenas que dijo.

### corto: "dame un short sobre X"
Un solo short con la estructura que mejor encaje (A, B, C o D de `references/cortos.md`), 3 ganchos y la autocrítica.

### dia: "paquete del día N"
Lee `plan-42.md` para el día N, junta la sesión prevista con el Día X y los espacios de publicación (ver `references/nomina-viva.md`) y entrega el paquete completo. Si el usuario dice "puedo grabar 10", añade del **banco evergreen** del plan los cortos que no dependen del día.

### plan: "replanifica los días N a M"
Reescribe ese tramo de `plan-42.md`, manteniendo el arco y los pilares de `references/nomina-viva.md`. Úsalo cuando una sesión falle o se mueva.

## Dónde se guarda
- Paquetes por día: `00_Serie/guiones/dias/Dia-NN.md`. Si el día ya tiene carpeta, se copia también a `Dia-NN/guion.md` como "guion previsto"; lo dicho de verdad lo revisa `monoga-serie`.
- Plan maestro: `00_Serie/guiones/plan-42.md`.
- Investigación de base (con fuentes): `00_Serie/guiones/investigacion/`.

## Entrega
- Di qué archivo escribiste, el puntaje de la rúbrica y qué no se pudo verificar (cómo suena en voz alta; Claude no oye).
- Cierra con la lista de problemas: uno por línea, con su arreglo.
