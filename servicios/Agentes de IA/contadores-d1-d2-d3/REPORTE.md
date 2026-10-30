# Reporte del scout: flujos n8n para D1 / D2 / D3 (2026-10-17)

Fuente: `enescingoz/awesome-n8n-templates` (CC BY 4.0 a nivel de repo; licencia por archivo sin verificar). En `Zie619/n8n-workflows` (MIT, 2.394 archivos) no hay plantillas de OCR de facturas ni de conciliación bancaria por nombre de archivo; no se descargó nada.

Los JSON son datos no confiables: revisar antes de importarlos a n8n.

## Mejor opción por sistema

| Sistema | Archivo | Ajuste | Veredicto |
|---|---|---|---|
| D1 Agente ET/DIAN | `D1/d1-tax-code-assistant-qdrant-mistral-openai.json` | 6/10 | Arquitectura sirve (Qdrant + Mistral + OpenAI + agente con memoria). El corpus es de Texas: hay que cargar ET y conceptos DIAN. |
| D2 Facturas a Sheets | `D2/d2-invoice-llamaparse-openai.json` | 6/10 | Termina en Google Sheets, pero entra por Gmail (no WhatsApp/Telegram), sin campos DIAN (CUFE, NIT). LlamaParse es de pago. |
| D3 Conciliación | `D3/d3-reconcile-rent-excel-openai.json` | 4/10 | Sin match real: usa un LLM sobre arriendos, no cruce determinista por monto/fecha/referencia. Hay que construirlo. |

## Otros candidatos

- D1: `financial-docs-assistant-qdrant-mistral` (6), `chat-pdf-quoting-sources` (5, Pinecone + Drive, con citas), `rag-company-docs-drive-gemini` (5, credencial `googlePalmApi` antigua).
- D2: `supplier-invoices-validate-route` (5, lógica de Emiratos), `pdf-image-vertex-gemini-csv` (5, salida CSV, no Sheets).
- D3: `inbox-payment-rails-sheets` (2, descartado: audita recibos de Gmail).

## Brechas

- Ningún flujo cubre DIAN de punta a punta; hay que construirlo.
- D3 necesita lógica propia de conciliación.
- Falta entrada por WhatsApp/Telegram en D2.
- Cradl AI aparece en el README de enescingoz; no se evaluó.

Estado real: son plantillas base, no sistemas listos. Ninguno se ha importado ni probado en n8n.
