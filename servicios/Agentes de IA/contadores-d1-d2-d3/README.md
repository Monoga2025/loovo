# Contadores D1 / D2 / D3 — flujos n8n para Colombia

Estado real: los 3 JSON son borradores adaptados de las plantillas del scout. **No se han importado ni ejecutado en n8n.** Lo que sí se probó con Node (el JavaScript de los nodos Code) está en la sección "Pruebas".

| Archivo | Qué hace |
|---|---|
| `D1-agente-dian-colombia.json` | Agente de chat (Estatuto Tributario) con Qdrant + embeddings Mistral + OpenAI. Ingesta rápida de 25 artículos clave. Cita artículo y calcula en UVT. |
| `D2-extractor-facturas-dian-sheets.json` | Webhook → visión de OpenAI (sin LlamaParse) → validación (DV del NIT, CUFE, Subtotal+IVA=Total) → Google Sheets. |
| `D3-conciliador-bancario-colombia.json` | Webhook con extracto + auxiliar (CSV/XLSX) → conciliación **determinista** en Code → resumen ejecutivo con IA (la IA no concilia). |
| `datos-prueba/` | Factura PDF ficticia, extracto Bancolombia CSV y auxiliar CSV, todo inventado. |
| `scripts/` | Código fuente de los nodos Code, pruebas en Node y `construir-flujos.js` (regenera los JSON). |

## Cómo importar

1. n8n → Workflows → Import from File → elige el JSON.
2. En cada nodo con credencial (aparecen como `REEMPLAZAR - ...`) crea y asigna la tuya.
3. Los webhooks usan **Header Auth**: crea la credencial con un token propio y envíalo en cada llamada.
4. Activa el flujo solo después de probar con `datos-prueba/`.

## Credenciales requeridas (todas son placeholders, ninguna incluida)

- D1: OpenAI, Mistral Cloud, Qdrant. Qdrant debe responder en `http://qdrant:6333` (si no, cambia la URL en los nodos "Use Qdrant ...").
- D2: OpenAI, Google Sheets OAuth2, Header Auth. Reemplaza `REEMPLAZAR_ID_DE_LA_HOJA_DE_GOOGLE` y crea la pestaña `Facturas` con los encabezados de la nota del flujo.
- D3: OpenAI (solo para el resumen; si falla, igual se entrega la conciliación) y Header Auth.

## Uso rápido

- D1: ejecuta "Ingesta rapida" una vez; luego abre el chat. Edita `UVT_2026` en el nodo "Calculadora UVT y retencion".
- D2: `curl -H "Authorization: <token>" -F file=@datos-prueba/factura-ejemplo-FICTICIA.pdf -F canal=directo <url-webhook>/d2-factura` (el nombre del header es el que definas en la credencial).
- D3: `curl -H "..." -F extracto=@datos-prueba/extracto-bancolombia-ejemplo.csv -F auxiliar=@datos-prueba/libro-auxiliar-bancos-ejemplo.csv "<url-webhook>/d3-conciliar?ventana=3"`.

## Pruebas (qué se corrió)

- Los 3 JSON parsean (`JSON.parse`), sin conexiones rotas, ids y nombres únicos; el código de cada nodo Code compila.
- `node scripts/probar-d3.js`: lógica del nodo de D3 contra `datos-prueba/` (18 comprobaciones: 7 conciliadas = 4 exactas + 3 en ventana, 10 solo banco con GMF/cuota/ACH/IVA, 3 solo libros, totales cuadran, ventana 0/1/3, Excel simulado, errores).
- `node scripts/probar-d1-d2.js`: tabla del Art. 383 (la UVT no está configurada, así que no calcula pesos), validaciones de D2 con una respuesta del modelo **simulada**, y construcción del cuerpo para visión con el PDF de prueba.

## Lo que NO se probó

- Importación y ejecución en n8n (estructura de nodos, versiones, parámetros de `Extract From File`, `Merge`, `toolWorkflow`, Google Sheets).
- Llamadas reales a OpenAI, Mistral, Qdrant o Google. La precisión de la extracción sobre facturas reales es desconocida.
- Formatos reales de extracto Bancolombia/Davivienda: el lector detecta columnas por nombre (Fecha, Descripción, Valor o Débito/Crédito); los ejemplos son ilustrativos.
- Render visual del PDF de prueba (estructura validada, no abierto en un visor).

## Pendientes y valores a VERIFICAR

- **UVT 2026**: no configurada. Poner el valor de la resolución DIAN en `UVT_2026` (nodo "Calculadora UVT y retencion"). Mientras sea `null`, el agente responde en UVT y avisa.
- Los resúmenes del ET son de apoyo, no texto literal; los marcados `[VERIFICAR]` (tabla del Art. 241, topes de Art. 206/336/387, Art. 437 par. 3, 437-1, 477, 485/488, GMF y su exención, sanciones 641/651, exógena 631, obligados a declarar 592/594-3, y tarifas/bases de retención del DUR 1625/2016) deben confirmarse contra la norma vigente.
- Cuentas PUC en D2 y D3 son **sugerencias** para el contador (en especial GMF e IVA de comisiones).
- Entrada por WhatsApp/Telegram: el webhook de D2 acepta `file_url`; falta construir el flujo que reciba el mensaje del proveedor y entregue esa URL.
- Seguridad: el webhook de D2 descarga `file_url` (riesgo SSRF): mantener Header Auth y no exponer sin control.
- Alternativa Gemini Flash para D2 no implementada (se cambia el nodo HTTP y el formato del cuerpo).
- D3: solo `.xlsx` (no `.xls` antiguo); salida en JSON, sin exportar aún a Excel/Sheets.
- Licencia de las plantillas base: CC BY 4.0 a nivel de repo (`enescingoz/awesome-n8n-templates`), por archivo sin verificar; conservar atribución.
