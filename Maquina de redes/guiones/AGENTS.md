# guiones · cómo se escriben los guiones

Reglas comunes en `../AGENTS.md`. Antes de escribir, lee `../00_Serie/hechos.md` y `../00_Serie/voz-y-estilo.md`. Los guiones los escribe el modelo más capaz (ver la tabla de modelos en `../../AGENTS.md`), nunca uno barato. No leas ni edites nada en `../edicion/`.

## Dos formatos
| | Videos de NICHO que deben convertir (contadores, etc.) | Serie "Día X de 42" |
|---|---|---|
| Estilo | **UGC conversación**: texto completo toma por toma, como lo diría un amigo | Gancho y cierre literales, el resto en puntos |
| Skill | `monoga-guionista` + `references/ugc-ventas.md` | `monoga-guionista` (cortos) + `monoga-serie` |

El usuario manda sobre tomas, tono y titulares; él aprueba el guion.

## Reglas del formato UGC (el que más se usa ahora)
1. **Gancho = pregunta incómoda que el espectador reconoce**, no un anuncio. Entra directo, sin "hola, soy el fundador de Loovo".
2. **Tono de conversación en español colombiano**: "parce", "hermano", "bendita factura". Prohibido: "revoluciona", "soluciones digitales", enumerar funciones como vendedor, tono de IA.
3. **Un dolor concreto por sistema** y su resultado. Nunca tecnología.
4. **Honestidad:** si el sistema aún no existe, se dice que se está armando; la animación muestra cómo funcionaría, no una demo falsa. El CTA ofrece vista previa, lista de acceso o conversación, no entrega inmediata.
5. **El humano queda a cargo:** "tú revisas y entregas", nunca "se hace solo".
6. **CTA medible:** una palabra o números con la oferta en pantalla ("1 WhatsApp, 2 Vencimientos, 3 Informes"). Probar versión A (conversación) y B (conversión, palabra única).
7. **Estructura 50-65 s:** gancho con pregunta (0-9 s) → la idea en una frase (9-18 s) → un sistema por toma → regreso a cámara con pregunta y CTA.
8. **Formato de entrega por tomas:** TOMA n, tiempo, indicación de cámara entre paréntesis, texto completo entre comillas. Una sola persona; no memorizar palabra por palabra.
9. **Cifras:** lo que no sea del usuario se marca `[DATO]` o se quita; una cifra de ficción (p. ej. "30.000") va rotulada como ficción.
10. **Voces:** el usuario o Carolina (si él lo indica). Personajes IA = ficción rotulada.
11. **Mide lo comercial:** demos pedidas, leads calificados y ventas, no solo vistas.

## Entrega (siempre en Odoo, nunca suelto)
- Los guiones van al proyecto **Guiones** de Odoo (`odoo.grupomonoga.com`), columna "Guion listo", descripción en HTML (el Markdown se convierte; Odoo no lo lee). Etiquetas: nicho, quién habla (Daniel/Carolina), "Solo motion" si aplica.
- Credenciales: salen del CLI de Railway (servicio Odoo), nunca se imprimen ni se guardan. Subir a Odoo es trabajo remoto: requiere autorización explícita.
- Copia de respaldo en Markdown en `../odd/<campaña>/`.

## Autocrítica antes de entregar
Puntúa con `monoga-guionista/references/calidad.md`, di qué no verificaste (cómo suena en voz alta, retención) y reescribe solo lo que falle (máx. 2 vueltas).
