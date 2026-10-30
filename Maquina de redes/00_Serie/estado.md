# Estado de la serie

Última actualización: 2026-10-13, orquestador.

## Estado por día
| Día | Estado | Siguiente paso |
|---|---|---|
| 1 | Grabado y editado: v4 y v5 en `Dia-01/entregables/`. Portada minimalista 3:4 aprobada. Caption listo en `Dia-01/caption.md`. | El usuario publica y marca `Publicado: sí`. Después, decide cuál versión (v4 o v5) ganó. |
| 2 | Publicado (versión anterior). Rehecho como v10 con la marca IA MONOGA (dirección A Eléctrico), texto detrás de la persona y biblioteca de recursos: `Dia-02/entregables/final_*_v10.mp4`. | Usar la v10 como referencia de estilo para el Día 3. |
| 3 | Editado (2026-10-10) desde un clip de WhatsApp grabado caminando, habló libre (no el paquete DIAN): `Dia-03/entregables/Dia3_final_tiktok.mp4` y `_reels.mp4`, 56,6 s. La DIAN queda "pendiente" en el video. | El usuario revisa el corte; luego portada y caption con `monoga-serie`. |
| 4 (en pantalla "Día 5") | Grabado 2026-10-11: celular `VID20261011104512` (lectura de "Esencialismo" y comentarios) y `VID20261011112118` (a cámara), con el mic del PC en `CAMARA 10-45-16.mp4`. Entrenos de estilo aprobados (`entreno02_premium.mp4`: "Perfecto"). `Dia4_v1_numero1.mp4` (90,75 s) terminado pero **no se publica** (2026-10-13: suena motivacional y no tiene música). | Corte de IA (30-45 s, crudo B ~4:53-5:13, agente editor + CRM) tras estudio Haiku; el usuario elige estilo de música y confirma "Día 5 de 42". |
| 7 | Grabado 2026-10-13 (`Desktop/VID_20261013_110529.mp4`, celular, sin mic PC). Short "ventas con IA" (empleado de ventas en entrenamiento, La Nómina Viva): `Dia-07/entregables/Dia7_ventas_ia.mp4`, 52,7 s. Música Mixkit 464. | El usuario lo revisa en el celular y publica; caption con `monoga-serie`. Otros tramos posibles: NotebookLM "cerebro" (tapar datos), Odoo (tapar facturas). |

## Decisiones del usuario
- **Videos de canal (2026-10-14):** de cada crudo largo salen varios videos extra que NO son "Día X": van al canal, sin placa de la serie y sin contar en el máximo de 3 publicaciones de la serie.
- **Pantalla del computador (2026-10-14):** el usuario da permiso para mostrar su pantalla (Odoo, Railway, NotebookLM, Claude/Codex, repos) en los videos. Se siguen desenfocando claves/tokens y datos personales de terceros (nombres, teléfonos, correos, montos de clientes/proveedores), por la regla 4 de CLAUDE.md.
- **Estilo de edición nuevo (2026-10-11), reemplaza a "Eléctrico" en los videos:** minimalista **blanco pastel #F6F4EF con puntos grises + dorado suave (~#C8B07A)**, carbón #2A2926, nivel Adrià Solà (zoom de respiración, destello crema, invert flash con glitch a la salida de motion graphics, cámara 2.5D con parallax, títulos sincronizados con la voz). Prohibido: bordes redondos, recortar la silueta, fondos dorados, verde/lima, texto ilegible. Voz siempre a **-17,6 LUFS / LRA 4,5 / -2 dBTP** (medido en Adrià). Color: LUT tipo Adrià al 75 % sobre la persona. Audio: solo mic del PC (0 % celular) + **música baja bajo la voz** (2026-10-13). Skill `monoga-adria` (v2, pendiente de aprobación). Videos de marca personal **sobre IA y el canal, nada motivacional** (2026-10-13: teme bullying en la universidad). Se permiten mini citas de libros con atribución.
- **Marca IA MONOGA (anterior):** dirección A "Eléctrico" (carbón, azul eléctrico, lima, hueso; Space Grotesk + Instrument Serif cursiva). Nada de rojo. Ver `00_Serie/marca/marca.md`.
- **Texto detrás de la persona** en cada video.
- **Biblioteca de recursos** en `00_Serie/recursos/` (objetivo: crecer a 50+ recursos propios de la marca).
- **Guion (cambio del 2026-10-09):** el usuario pidió guiones para los 42 días. La skill `monoga-guionista` prepara el gancho y el cierre literales y el resto en puntos; él habla "como es él", con sus palabras. Los guiones completos de IA se rechazaron dos veces; por eso no se escriben párrafos para leer.
- **Personaje de la serie: La Nómina Viva** (aprobado el 2026-10-09: "aplícame el más recomendado"). Empleados de IA con carné y "sueldo $0", la audiencia decide a quién contratar, contador de horas devueltas (solo con medición real) y tablero de errores. Ver `monoga-guionista/references/nomina-viva.md`.
- **Formato nuevo:** videos largos de YouTube grabados trabajando (OBS: cámara y pantalla). De ahí salen los clips. El short "Día X" se graba al terminar cada sesión, con el resultado real. Máximo 3 publicaciones al día (E1 Día X, E2 clip, E3 opcional); se puede grabar hasta 10.
- **Tomas:** hace hasta 12 intentos por línea. El orquestador propone las mejores con datos (tono de voz, fluidez, completa, mira a cámara) y el usuario aprueba.
- **Audio (anterior a monoga-adria):** música épica y audible, que baje cuando él habla y suba en los huecos. Preset `v4` (1,5 dB bajo la voz) o `v5` (3 dB y 2 s de música al final). Sin decidir cuál.
- **Portada (cambio 2026-10-14):** estilo "Editorial Tech Luxury" del usuario: DÍA N dorado sobre bloque negro, titular negro extrabold, subtítulo dorado entre paréntesis, persona fotorrealista al centro y 5–8 paneles de software flotando con conexiones doradas. La genera el usuario con su prompt maestro: `00_Serie/portadas/prompt-maestro.md` (referencia `referencia_dia7.png`). Sin robots ni números abajo. Antes: minimalista hecha por Codex.
- **Caption:** gancho en dos líneas, "lo que no cabía en X segundos", marcador, pregunta para comentar, `#42DiasLoovo`.
- **Todo local** cuando se pueda: sin Docker, Postgres nativo, transcripción con la clave de OpenAI solo desde la variable de entorno.
- **Humor:** usa bromas como "explotar" y "esclavizar" a los empleados de IA. Es su estilo; el riesgo es la moderación de TikTok.

## Quién tiene qué
| Carpeta | Agente | Desde |
|---|---|---|
| `Dia-02/proyecto` | Editor (chat abierto en Loovo-42) | 2026-10-08 |
| `00_Serie/guiones/` | Orquestador (guiones) | 2026-10-09 |
| `Dia-04/proyecto` | Editor Opus (monoga-adria) | 2026-10-11 |
| `Dia-07/proyecto` | Editor Opus (monoga-adria), short "ventas con IA" | 2026-10-13 |
| `Dia-08/proyecto/contadores_ia` | Planeación lista (Claude); espera hook Higgsfield y crudo | 2026-10-17 |
| Resto de `Loovo-42` | Orquestador | |

## Pendientes abiertos
- Elegir v4 o v5 del Día 1 y mejorar la skill con la ganadora.
- Qué se dice sobre el CRM en cámara: "puede cerrar ventas" se quitó del corte. "Puede leer cada cliente, cada correo" y "cómo le gusta que le hablen" se quedaron (decisión del usuario, 🟡); el caption dice que se está probando.
- El chat del agente del CRM nunca se probó de punta a punta.
- Las dos claves de OpenAI pegadas en el chat siguen activas. Hay que revocarlas.
- Railway y el commit del CRM (modelo Codex) siguen pendientes.

## Herramientas listas
- `dia.py estado|portada|todo N`, `new_day.py N`, `clean_day.py N`, `portada.py N`.
- `audio_pro.py` (golpes de dedo, música épica, ducking por voz), `transcribe_openai.py` (necesita `OPENAI_API_KEY`).
