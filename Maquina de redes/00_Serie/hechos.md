# Hechos permitidos

Un guion o un texto solo puede afirmar lo que está en estado ✅. Lo 🟡 se dice como "estamos probando". Lo ⏳ se dice como "próximamente".

| Hecho | Estado | Nota |
|---|---|---|
| Loovo existe como empresa | ✅ | Lo dijiste en el Día 1 |
| El plazo es de 42 días: Día 1 = 7 oct, Día 42 = 17 nov | ✅ | Calculado |
| Luque Business Summit, Bucaramanga, 17 a 19 nov 2026, más de 2.000 empresarios | ✅ | Página del evento |
| Tu rol en el evento (asistes, expones, vas con tu empresa) | ❓ | Confirmar |
| Hay un CRM propio con IA corriendo en tu computador | ✅ | Verificado el 7 oct: app, API, agente y base de datos arriba. "Propio" = adaptado de open source (ver abajo). El agente de IA es el que trae el proyecto base y no se ha probado de punta a punta |
| El agente del CRM responde en la ficha de un contacto | 🟡 | Sin probar de punta a punta |
| El agente usa tu login de Codex (ChatGPT) como modelo | 🟡 | Configurado; backend experimental |
| Un "empleado" de IA te edita los videos (`monoga-editor`) | ✅ | Editó el Día 1: 7 min 37 s de grabación a 38 s |
| Integración con la DIAN para factura electrónica | ⏳ | No existe todavía |
| El CRM actúa solo (crea notas, tareas) | 🟡 | Existe en el código, sin probar en vivo |
| Hay datos de clientes reales en la base del CRM | ⚠️ | No mostrar en pantalla; usar modo demo |
| Publicado el Día 1 en TikTok e Instagram | ❓ | Actualizar en `marcador.md` |
| Loovo es una agencia de inteligencia artificial | ✅ | Lo dijiste en el Día 2 ("mi agencia de inteligencia artificial") |
| El CRM "puede cerrar ventas" y sabe "cómo le gusta que le hablen" | 🟡 | Dicho en el Día 2; no probado |
| El CRM "puede leer cada cliente y cada correo" | 🟡 | Existe en el código; sin probar en vivo |
| El CRM es una adaptación de un CRM open source (Comp AI CRM, licencia MIT) con cambios propios para Colombia: etapas en español, pesos COP, campos de lead, consentimiento | ✅ | `README.md` y 13 commits propios (5 y 6 oct). Se puede decir "mi CRM" o "adapté un CRM open source". **No** se puede decir "lo construí desde cero" |
| "Capturar lead" saca nombre, empresa, dolor y presupuesto de un mensaje y crea el contacto, el trato y la tarea | ✅ | Motor de **reglas**, no IA (`lead-intake.ts`, tests y QA). **No** decir "la IA entendió" hasta conectar un modelo |
| Modo demo con datos ficticios (9 tratos "Demo SAS") | ✅ | `start.ps1 -Demo`, tests. `CRM.bat` NO tiene modo demo: abre la base real. Verificarlo en la sesión 1 |
| El CRM respeta el consentimiento (Habeas Data) y bloquea a quien pidió no ser contactado | ✅ | Tests y QA del 6 oct |
| WhatsApp conectado al CRM | ⏳ | No existe en el código |
| Cotizaciones y cartera dentro del CRM | ⏳ | No existe; solo el campo manual "estado de pago" |
| El CRM está en la nube o en producción | ⏳ | Solo corre en el computador (127.0.0.1) |
