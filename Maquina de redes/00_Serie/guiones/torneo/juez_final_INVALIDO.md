Las cuatro rondas devolvieron `fetch failed`. **No hay propuestas ni ataques disponibles para juzgar.** Esta es una selección provisional construida desde el brief; no atribuyo ideas a los equipos ni declaro ganador.

## 1. Tabla de las 10 mejores ideas

**Nota máxima: 55**, aplicando los pesos 3, 3, 2, 2 y 1. Son valoraciones de las propuestas, no resultados medidos.

Los minutos extra son **estimaciones** para marcar un fragmento del trabajo ya grabado. No incluyen nuevas tomas: si toca repetir trabajo para cámara, se descarta.

| Idea | Equipo de origen | Nota ponderada | Por qué / trabajo y documentación |
|---|---|---:|---|
| **Definir qué vamos a vender** | Juez, provisional | 53/55 | Falta catálogo: cerrar alcance y exclusiones del primer servicio; mostrar esa ficha. **1 min extra.** |
| **Probar al empleado del CRM** | Juez, provisional | 53/55 | El agente sigue 🟡: probar un recorrido completo en demo y registrar resultado, incluso si falla. **1 min.** |
| **DIAN: decidir la ruta** | Juez, provisional | 52/55 | Cumple la investigación prometida sin fingir integración: revisar requisitos, alternativas y dependencias. Mostrar la decisión. **1 min.** |
| **Costos antes del precio** | Juez, provisional | 51/55 | Construir la hoja de costos necesaria para cotizar; mostrar categorías y cifras verificadas autorizadas. **1 min.** |
| **Ensayar la venta con Don Armando** | Juez, provisional | 51/55 | Preparar una conversación comercial y probar la demo; Don Armando queda identificado como ficticio. **0–1 min.** |
| **Comprobar el bloqueo de contacto** | Juez, provisional | 50/55 | Hacer una prueba de regresión del consentimiento con datos ficticios; registrar el bloqueo observado. **0–1 min.** |
| **Capturar lead no es IA** | Juez, provisional | 50/55 | Validar la captura por reglas y explicar qué ofrece hoy; mostrar mensaje ficticio y registros creados. **0–1 min.** |
| **Tablero de errores reales** | Juez, provisional | 50/55 | Registrar fallas, corregir y repetir pruebas; documentar desde el mismo registro de trabajo. **0–1 min.** |
| **Una ficha comercial entendible** | Juez, provisional | 49/55 | Preparar el documento para compradores: problema, alcance, requisitos y límites; reutilizarlo en pantalla. **0–1 min.** |
| **Definir entrega y soporte** | Juez, provisional | 47/55 | Resolver instalación, permisos, respaldo y responsabilidades antes de ofrecer el servicio; mostrar la lista. **0–1 min.** |

**Empates:** catálogo/prueba; costos/ensayo; consentimiento/captura/errores. Los ordeno por dependencia del trabajo, no por superioridad demostrada.

**Evidencia:** los hechos respaldan las necesidades técnicas. El scraper aporta una pista de formato: trabajo real —153.100 vistas— y precios —119.800— aparecen entre los destacados. Son 60 resultados no aleatorios y no se vieron los videos; no prueban ventas ni garantizan alcance.

## 2. Las 5 que se hacen YA

**Regla común:** OBS mientras se trabaja, solo voz del usuario y sin tomas adicionales. Para el CRM: iniciar con `start.ps1 -Demo`, verificar datos ficticios y no usar `CRM.bat`, que abre la base real. Nada de claves, correos ni clientes reales.

### 1. Definir qué vamos a vender
- **Trabajo:** escoger un primer servicio, comprador, alcance, exclusiones y prueba de aceptación.
- **Documentación:** ① trabajar en la ficha; ② marcar la decisión final; ③ mostrar qué entra y qué todavía no.
- **Extra estimado:** 1 minuto.
- **Gancho:** “Tengo un CRM, pero todavía no he decidido qué voy a vender.”

### 2. Probar al empleado del CRM
- **Trabajo:** preparar un caso ficticio, ejecutar el recorrido completo y contrastar lo esperado con lo observado.
- **Documentación:** ① marcar entrada y respuesta; ② comprobar cualquier cambio que diga haber hecho; ③ conservar el fallo si ocurre.
- **Extra estimado:** 1 minuto.
- **Gancho:** “Al empleado del CRM todavía no lo he probado de principio a fin.”

### 3. DIAN: decidir la ruta
- **Trabajo:** consultar documentación vigente, alternativas de integración, costos y requisitos. Sigue ⏳.
- **Documentación:** ① registrar fuentes; ② comparar opciones; ③ mostrar la decisión o el bloqueo pendiente, no una integración inexistente.
- **Extra estimado:** 1 minuto.
- **Gancho:** “Ayer prometí la DIAN. Hoy toca averiguar qué hace falta.”

### 4. Costos antes del precio
- **Trabajo:** calcular implementación, uso, alojamiento y soporte.
- **Datos pendientes:** `[DATO — proveedores]` tarifas; `[DATO — usuario]` tiempo, margen y precio aprobado.
- **Documentación:** ① completar la hoja durante el trabajo; ② separar costos medidos de estimaciones; ③ mostrar solo cifras autorizadas.
- **Extra estimado:** 1 minuto.
- **Gancho:** “Todavía no tengo precios. Primero voy a sacar las cuentas.”

### 5. Ensayar la venta con Don Armando
- **Trabajo:** practicar cómo explicar y demostrar el servicio que realmente se puede entregar.
- **Documentación:** ① grabar el ensayo necesario; ② mostrar una función validada; ③ anotar dónde la oferta no se entiende. Solo habla el usuario.
- **Extra estimado:** 0–1 minuto.
- **Gancho:** “Voy a ensayar la venta con Don Armando. Don Armando no existe.”

**Si el agente falla, no entra al catálogo como IA operativa.** Primero se corrige o se reduce el alcance.

## 3. Lo que se descarta y por qué

- Listas de “mejores IA”: no construyen los servicios del evento.
- Guiones completos para leer: ya fueron rechazados y no suenan al usuario.
- Carnés, sketches o piezas nuevas que exijan producción aparte del trabajo.
- Presentar DIAN, WhatsApp, cotizaciones o cartera como funcionalidades existentes.
- Llamar IA al capturador por reglas o presentar el CRM como construido desde cero.
- Precios, ingresos u horas ahorradas sin respaldo; “sueldo $0” no significa operación gratis.
- Clientes reales, claves visibles y humor con “explotar” o “esclavizar”.

## 4. Decisiones que solo el usuario puede tomar

- `[DATO — usuario]` Primer servicio, comprador objetivo y problema prioritario.
- `[DATO — usuario]` Alcance, exclusiones y condiciones para aceptar una entrega.
- `[DATO — usuario]` Presupuesto y horas disponibles esta semana.
- `[DATO — usuario]` Precio, forma de cobro y qué cifras autoriza publicar.
- `[DATO — usuario]` Rol en el Summit: asistir, exponer u otra participación.
- `[DATO — usuario]` Si cuenta que estudia; solo cuando aporte contexto al trabajo real.
- `[DATO — usuario]` Cuánto soporte está dispuesto a comprometer después de vender.

## 5. Plan semanal de 7 días

- **Día 3 · 9 oct:** investigar DIAN y esbozar el servicio prioritario; documentar requisitos y pendientes, no una conexión.
- **Día 4 · 10 oct:** aprobar alcance y prueba de aceptación; mostrar qué se ofrecerá y qué queda fuera.
- **Día 5 · 11 oct:** probar el agente de punta a punta en demo; registrar el resultado real.
- **Día 6 · 12 oct:** comprobar captura por reglas y consentimiento; corregir bloqueos y documentar una prueba.
- **Día 7 · 13 oct:** construir costos y proponer precio al usuario; mostrar únicamente datos verificados autorizados.
- **Día 8 · 14 oct:** preparar ficha comercial, condiciones de entrega y soporte; registrar los límites del servicio.
- **Día 9 · 15 oct:** ensayar la venta con Don Armando ficticio; documentar la demo y ajustar lo que no se entiende.

## 6. Los 5 ataques que más pesaron

**No se recuperó ningún ataque ni su autor.** A_bitacora, B_evento, C_retencion y D_marca fallaron. Estos cinco reparos son del **Juez**, no intervenciones de los equipos:

1. **Juez:** sin propuestas recibidas, atribuir ganadores o procedencias sería inventar el torneo.
2. **Juez:** si una idea exige trabajo solo para publicar, contradice la misión.
3. **Juez:** un agente sin prueba completa no puede venderse como funcionalidad validada.
4. **Juez:** confundir reglas con IA falsea lo que ya existe.
5. **Juez:** vistas ajenas no justifican precios, resultados ni promesas comerciales propias.
