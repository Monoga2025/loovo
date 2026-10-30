# Resultado prioritario — 21 de octubre de 2026

**Estado: bloqueado para determinar pendientes actuales. No equivale a ausencia de mensajes.**

## Evidencia y cobertura real
- Se consultaron los 25 contactos de state.json en la instancia loovo-ventas. Evolution devolvió HTTP 200 y total 0 para cada JID telefónico, tanto en la ventana 12–21 de octubre como sin filtro temporal. No se recibió ningún mensaje para leer.
- Inicio exacto consultado: 2026-10-12 00:00:00 America/Bogota. Corte exacto UTC en el registro conservado abajo; corresponde al 21 de octubre, UTC−05:00. Último día disponible de mensajes remotos: **indeterminado**, no hubo resultados. No es posible afirmar que se revisó íntegramente el historial real.
- La referencia local respuestas_2026-10-18.md describe auditorías del sábado 17 bajo identidad Daniel y no conversaciones comerciales confirmadas. No demuestra el estado al día 21 ni el envío de los borradores del lunes.
- No se pudieron verificar mensajes entrantes sin respuesta, identidad comercial actual, horas de último mensaje ni tiempo de espera. El tiempo de espera es **no calculable**, no cero. Tampoco se verificó si hay otros identificadores de WhatsApp (LID) asociados a los mismos contactos; no se hicieron búsquedas globales para evitar chats privados.
- Las variables indican persistencia de mensajes/chats habilitada en Evolution; el CRM tiene los 25 números del lote en su lista permitida. Esto no prueba que los registros estén sincronizados.

## Bloqueos exactos
1. CRM: GET /api/contacts?search=3005550001 devolvió **401**; la sesión HTTP no está autenticada. No se hizo POST de login ni se abrió la interfaz de conversación.
2. Base del CRM: acceso Railway SSH no disponible, **exit 255; ssh.railway.com puerto 22: Connection timed out**. Un único intento de recuperación acotado también falló; sin más reintentos. Ninguna consulta SQL llegó a ejecutarse.
3. Evolution: acceso autorizado funciona, pero las búsquedas exactas por los JID telefónicos del lote arrojan cero registros. No se ha determinado si hay diferencia de identificador, retención, importación o sincronización; ninguna de esas causas está probada.
4. Engram: proveedor incompatible con el binario instalado (falta instance-id); no se guardaron datos personales en memoria.

## Ruta mínima y guardas para responder
- CRM existente: https://your-app-name.up.railway.app. El usuario puede autenticarse manualmente y comprobar la identidad antes de redactar o enviar. **Abrir un chat en la interfaz dispara POST /api/contacts/:id/read si está no leído**; por eso no se abrió durante esta auditoría y esa ruta no sirve como inspección sin cambios.
- Bundle público inspeccionado: GET /api/contacts/:id consulta detalle; POST /api/contacts/:id/read marca leído; POST /api/contacts/:id/suggest solicita texto; POST /api/contacts/:id/reply envía respuesta; POST /api/contacts/:id/inbound crea entrada; POST /api/contacts/:id/note crea nota. No se ejecutó ninguno de estos POST. Guardas de negocio del backend y horarios no verificadas.
- Evolution: POST /chat/findMessages/:instance es consulta demostrablemente de solo lectura (count/findMany); requiere API key. No se utilizaron rutas de envío, presencia, lectura ni edición.
- **Automatización activa: no confirmada.** El CRM muestra controles de pausar/reanudar IA y tiene clave de IA configurada, pero no se leyó el handler de los contactos ni la configuración efectiva. Disponibilidad de interfaz/clave no significa que responda solo. No activar ni reanudar nada.

## Priorización provisional y separación de identidades
- **Comercial Loovo:** ningún pendiente actual confirmado; no presentar a ningún contacto como doctor que ya respondió comercialmente.
- **Daniel / auditoría:** la referencia del 18 identifica ofertas de horario en Balance (21-oct 15:30), REAL (23-oct 08:30), Sonríe y Lina Caballero (19-oct, ya pasado). Prioridad humana: comprobar si fueron meras ofertas o reservas y si se cerraron. No afirmar citas confirmadas, no reservar ni continuar como paciente.
- Las otras 21 clínicas quedan también sin verificación actual. Los 25 resultados individuales se conservan abajo; cero registros no permite priorizar interés comercial.

## Borrador comercial condicional — no enviar
Solo tras confirmar el hilo correcto y la identidad; no es respuesta a un entrante verificado:
> Hola, soy Monoga de Loovo. Quiero hablar con la persona encargada de la atención y el seguimiento por WhatsApp de la clínica. ¿Con quién podría revisarlo?

Si el hilo corresponde a Daniel, **no pegar este texto como continuación del paciente**: revisar con el usuario cómo cerrar transparentemente esa auditoría y separar el contacto comercial. Sin promesas de resultados, precios, personalizaciones o datos clínicos no verificados. Envío exclusivamente manual dentro del horario de Ley 2300.

## Cambios locales
- Único archivo escrito: ventas/pendientes_doctores_2026-10-21.md (no existía al iniciar).
- state.json: **sin cambios; diff vacío**. XLSX: sin cambios. No se envió ni marcó leído ningún mensaje ni se cambió configuración remota.

---



# Auditoría de mensajes — corte 2026-10-21T18:29:50.116Z

## Evidencia acotada Evolution
- Runtime: openai-codex/gpt-6.1-sol; fecha local verificada 2026-10-21 (America/Bogota).
- Ventana consultada: 2026-10-12T00:00:00-05:00 a 2026-10-21T18:29:50.116Z (semana lunes 12–domingo 18 que contiene el contacto del sábado 17, extendida al corte actual).
- Solo los 25 números de state.json; consultas paginadas POST /chat/findMessages por JID y fecha, sin marcar leído.
- Naturaleza de solo lectura comprobada en fuente pública tag 2.3.7: src/api/routes/chat.router.ts → chat.controller.ts → src/api/services/channel.service.ts, fetchMessages: únicamente message.count y message.findMany. Versión del servidor: 2.3.7.
- No se modificaron state.json ni xlsx; no se enviaron mensajes. Credenciales obtenidas en memoria mediante Railway CLI.
- Consulta finalizada: true; contactos cubiertos: 25/25.

```json
[
  {
    "id": 1,
    "total": 0,
    "messages": []
  },
  {
    "id": 2,
    "total": 0,
    "messages": []
  },
  {
    "id": 3,
    "total": 0,
    "messages": []
  },
  {
    "id": 4,
    "total": 0,
    "messages": []
  },
  {
    "id": 5,
    "total": 0,
    "messages": []
  },
  {
    "id": 6,
    "total": 0,
    "messages": []
  },
  {
    "id": 7,
    "total": 0,
    "messages": []
  },
  {
    "id": 8,
    "total": 0,
    "messages": []
  },
  {
    "id": 9,
    "total": 0,
    "messages": []
  },
  {
    "id": 10,
    "total": 0,
    "messages": []
  },
  {
    "id": 11,
    "total": 0,
    "messages": []
  },
  {
    "id": 12,
    "total": 0,
    "messages": []
  },
  {
    "id": 13,
    "total": 0,
    "messages": []
  },
  {
    "id": 14,
    "total": 0,
    "messages": []
  },
  {
    "id": 15,
    "total": 0,
    "messages": []
  },
  {
    "id": 16,
    "total": 0,
    "messages": []
  },
  {
    "id": 17,
    "total": 0,
    "messages": []
  },
  {
    "id": 18,
    "total": 0,
    "messages": []
  },
  {
    "id": 19,
    "total": 0,
    "messages": []
  },
  {
    "id": 20,
    "total": 0,
    "messages": []
  },
  {
    "id": 21,
    "total": 0,
    "messages": []
  },
  {
    "id": 22,
    "total": 0,
    "messages": []
  },
  {
    "id": 23,
    "total": 0,
    "messages": []
  },
  {
    "id": 24,
    "total": 0,
    "messages": []
  },
  {
    "id": 25,
    "total": 0,
    "messages": []
  }
]
```

## Contraste sin filtro temporal (solo los mismos JID)
```json
[
  {
    "id": 1,
    "total": 0,
    "records": []
  },
  {
    "id": 2,
    "total": 0,
    "records": []
  },
  {
    "id": 3,
    "total": 0,
    "records": []
  },
  {
    "id": 4,
    "total": 0,
    "records": []
  },
  {
    "id": 5,
    "total": 0,
    "records": []
  },
  {
    "id": 6,
    "total": 0,
    "records": []
  },
  {
    "id": 7,
    "total": 0,
    "records": []
  },
  {
    "id": 8,
    "total": 0,
    "records": []
  },
  {
    "id": 9,
    "total": 0,
    "records": []
  },
  {
    "id": 10,
    "total": 0,
    "records": []
  },
  {
    "id": 11,
    "total": 0,
    "records": []
  },
  {
    "id": 12,
    "total": 0,
    "records": []
  },
  {
    "id": 13,
    "total": 0,
    "records": []
  },
  {
    "id": 14,
    "total": 0,
    "records": []
  },
  {
    "id": 15,
    "total": 0,
    "records": []
  },
  {
    "id": 16,
    "total": 0,
    "records": []
  },
  {
    "id": 17,
    "total": 0,
    "records": []
  },
  {
    "id": 18,
    "total": 0,
    "records": []
  },
  {
    "id": 19,
    "total": 0,
    "records": []
  },
  {
    "id": 20,
    "total": 0,
    "records": []
  },
  {
    "id": 21,
    "total": 0,
    "records": []
  },
  {
    "id": 22,
    "total": 0,
    "records": []
  },
  {
    "id": 23,
    "total": 0,
    "records": []
  },
  {
    "id": 24,
    "total": 0,
    "records": []
  },
  {
    "id": 25,
    "total": 0,
    "records": []
  }
]
```


## Continuación autorizada: login CRM — 2026-10-21T18:39:38.770Z

- Runtime comprobado: openai-codex/gpt-6.1-sol.
- Fuente local revisada antes de autenticar: server/auth.ts, app.ts, crm.ts, channels.ts. POST /api/auth/login acepta JSON password y devuelve cookie HttpOnly; credencial y cookie conservadas únicamente en memoria del proceso. Login exitoso; GET /api/auth/status confirma authenticated=true. No se imprimieron secretos.
- **Corrección del bloqueo anterior:** autenticación CRM resuelta; ya no es correcto decir que falta sesión.
- **Bloqueo de alcance detectado en fuente:** GET /api/contacts llama crm.listContacts() SIN aceptar filtros; ignora search. La consulta SELECT incluye último mensaje de TODOS los contactos. Por eso NO se llamó este endpoint, ni siquiera con search, pues podría leer chats ajenos. GET /api/contacts/:id sí es de solo lectura, pero state.json no contiene IDs del CRM y no hay ruta de búsqueda por número en la fuente revisada. No se adivinaron IDs ni se enumeraron conversaciones.
- GET /api/ai/status respondió 200; proveedor configurado=openai:gpt-6-luna, live=true. Esto prueba configuración de proveedor, no automatización activa para estas clínicas; no se ejecutó ping ni sugerencia ni ninguna IA.
- Asociación LID/número: channels.ts acepta remoteJid o remoteJidAlt terminados en @s.whatsapp.net; un LID sin número alterno se descarta. Es comportamiento de código, NO explicación comprobada de la ausencia de historial.
- Se contrastaron contactos Evolution con POST /chat/findContacts por los mismos 25 JID telefónicos. Fuente pública tag 2.3.7, channel.service.ts fetchContacts: únicamente contact.findMany, filtro remoto exacto. Resultado: 25 contactos consultados; 25 registros asociados encontrados. No hubo enumeración global.
- No se repitió SSH. No se abrió UI, no se marcó leído, no hubo mensajes/notas/sugerencias ni cambios remotos excepto la autenticación expresamente autorizada. state.json y xlsx siguen intactos.
- Pendientes, separación Daniel/Loovo y espera actual: siguen **no verificables** por falta de historial accesible dentro del alcance. No hay borradores personalizados nuevos sustentables.
- Próximo paso mínimo: obtener de Monoga un mapeo de IDs CRM de las 25 clínicas (sin abrir chats que marque leído), o autorización específica para un listado global de contactos que contiene último mensaje; esa autorización NO se presume. Con IDs verificados se puede GET /api/contacts/:id sin marcar leído.

### Contraste individual de asociaciones
```json
[
  {
    "id": 1,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto015@example.com",
        "id": "cmvchn8x302tut45ki7d9t9up"
      }
    ]
  },
  {
    "id": 2,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto016@example.com",
        "id": "cmvcho3lr02u3t45k7nnr64px"
      }
    ]
  },
  {
    "id": 3,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto017@example.com",
        "id": "cmvchonki02uat45kv0n337vc"
      }
    ]
  },
  {
    "id": 4,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto018@example.com",
        "id": "cmvchq9g002urt45kxg6ych21"
      }
    ]
  },
  {
    "id": 5,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto019@example.com",
        "id": "cmvchr0sh02uyt45kcx86ckc4"
      }
    ]
  },
  {
    "id": 6,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto020@example.com",
        "id": "cmvclkch3033lt45kc2s2c99g"
      }
    ]
  },
  {
    "id": 7,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto021@example.com",
        "id": "cmvcllh4k033st45k6ajqc7ml"
      }
    ]
  },
  {
    "id": 8,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto022@example.com",
        "id": "cmvclmks70341t45k0ir88wqm"
      }
    ]
  },
  {
    "id": 9,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto023@example.com",
        "id": "cmvclnkkh034qt45k6a06q557"
      }
    ]
  },
  {
    "id": 10,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto024@example.com",
        "id": "cmvclop6k0359t45kmqsxifbp"
      }
    ]
  },
  {
    "id": 11,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto025@example.com",
        "id": "cmvclpo86035et45kpqb8nann"
      }
    ]
  },
  {
    "id": 12,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto026@example.com",
        "id": "cmvclquwp035nt45kalljcbqk"
      }
    ]
  },
  {
    "id": 13,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto027@example.com",
        "id": "cmvclrwpx0362t45k6126ito3"
      }
    ]
  },
  {
    "id": 14,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto028@example.com",
        "id": "cmvclszvi036bt45kip2q2ncc"
      }
    ]
  },
  {
    "id": 15,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto029@example.com",
        "id": "cmvclu024036qt45k8jwqyuet"
      }
    ]
  },
  {
    "id": 16,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto030@example.com",
        "id": "cmvclv48l036xt45kx4ykaiql"
      }
    ]
  },
  {
    "id": 17,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto031@example.com",
        "id": "cmvclw3hs037et45k3evmg1qr"
      }
    ]
  },
  {
    "id": 18,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto032@example.com",
        "id": "cmvclxd5d037vt45k9dbocjmv"
      }
    ]
  },
  {
    "id": 19,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto033@example.com",
        "id": "cmvcly2f3038ct45k8hsuyuaw"
      }
    ]
  },
  {
    "id": 20,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto034@example.com",
        "id": "cmvclyx2p038vt45k01rvbfky"
      }
    ]
  },
  {
    "id": 21,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto035@example.com",
        "id": "cmvclzsgb039kt45kd3zdljwa"
      }
    ]
  },
  {
    "id": 22,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto036@example.com",
        "id": "cmvcm0ok8039zt45kq7od11lx"
      }
    ]
  },
  {
    "id": 23,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto037@example.com",
        "id": "cmvcm1ks003a6t45kyvbhuo6f"
      }
    ]
  },
  {
    "id": 24,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto038@example.com",
        "id": "cmvcm2dvl03aht45kw8ojj8em"
      }
    ]
  },
  {
    "id": 25,
    "count": 1,
    "metadata": [
      {
        "remoteJid": "contacto039@example.com",
        "id": "cmvcm39ax03aot45kqsprloq2"
      }
    ]
  }
]
```


## Lectura CRM autenticada y filtrada en memoria — 2026-10-21T18:40:57.886Z

Listado recibido solo en memoria y descartados contactos ajenos antes de cualquier detalle. Coincidencia exacta de número normalizado; no coincidencias parciales. GET /api/contacts/:id verificado previamente en fuente: consulta contacto, mensajes, eventos y secuencia; marcar leído es POST separado, no ejecutado. Ventana: 2026-10-12 00:00 America/Bogota hasta 2026-10-21T18:40:57.886Z.

```json
[
  {
    "clinicId": 14,
    "crmId": 19,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 6,
    "messages": [
      {
        "id": 70,
        "sender": "human",
        "at": 1792254081000,
        "body": "Hola buen día la encontré en Instagram quiero ponerme botox en la frente y el entrecejo tiene cupo esta semana?",
        "meta": {
          "external_id": "3EB08C663AE50E1B037411",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254081000
          }
        }
      },
      {
        "id": 71,
        "sender": "customer",
        "at": 1792254084000,
        "body": "¡Hola! ✨ Te damos la bienvenida a la clínica de la Dra. Paula Bernal. 🌸\n ¿En qué podemos ayudarte hoy?\n\nSi deseas agendar tu cita, conocer nuestros servicios o revisar disponibilidad, puedes hacerlo de forma fácil y rápida a través de nuestro sitio web:\n🌐 https://www.drapastrana.com/\n\n💬 Looking for consultation in English? Dr. Paula Bernal is fluent in English and offers bilingual medical appointments. 🇺🇸✨\n\n📍 Ubicación: Edificio Colmena, consultorio 101- El Poblado.\n\nEn un momento te atenderemos 👩‍⚕️",
        "meta": {
          "external_id": "A5A55BA6A32CE7BAA5B7CF24E8A900B0",
          "source": "evolution"
        }
      },
      {
        "id": 107,
        "sender": "customer",
        "at": 1792258291000,
        "body": "Buenas Tardes, mi nombre es Liz soy la auxiliar administrativa del consultorio Dra.Bernal.",
        "meta": {
          "external_id": "A5AA479F850AAB530F9BF3A836FD5BE0",
          "source": "evolution"
        }
      },
      {
        "id": 108,
        "sender": "customer",
        "at": 1792258297000,
        "body": "La unidad de toxina botulínica *botox®️* tiene un costo de $20.000 cop (5,20 usd).\nLas unidades totales requeridas dependen de cada paciente, de la anatomía de cada paciente (no tanto de la edad); usualmente se aplica en la frente, entrecejo y patas de gallina. \nOtros sitios de aplicación es en el masetero para bruxismo, en el jawl y cuello. \n*Finalmente las unidades que requieras las defines con la dra también con tus expectativas del tratamiento*",
        "meta": {
          "external_id": "A554C33A58B82C5BA4C037FAF0E75E33",
          "source": "evolution"
        }
      },
      {
        "id": 109,
        "sender": "customer",
        "at": 1792258299000,
        "body": "por ejemplo:\nPara un *babybotox* 35 unidades serían $700.000 (226 usd)\n*45 unidades* por ejemplo serían $900.000 cop (291 usd)\nPara *65 unidades* serían $1.300.000 (420usd)\nY como te digo las unidades que requieres las definen entre tu anatomia, lo que estas buscando y al dra te indicaría cuántas unidades requieres",
        "meta": {
          "external_id": "A578ACB07F4529C29DE3ED1EA51C13FC",
          "source": "evolution"
        }
      },
      {
        "id": 135,
        "sender": "human",
        "at": 1792349333000,
        "body": "Hola buenas tardes Liz muchas gracias por la información lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB0D37533E0166DEABF13",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792349333000
          }
        }
      },
      {
        "id": 136,
        "sender": "customer",
        "at": 1792349336000,
        "body": "¡Hola! ✨ Gracias por escribirnos al consultorio de la Dra. Paula Bernal. En este momento no nos encontramos disponibles, te responderemos tan pronto reanudemos actividades . 🌸\n\n⏰ Nuestro horario de atención:\nLunes a viernes: 9:00 a.m. a 6:00 p.m./ Sábados: 9:00 a.m. a 4:00 p.m.\n\n📅 ¡No tienes que esperar!\nPuedes consultar la disponibilidad de agenda y agendar tu cita directamente en nuestro sitio web:\n👉 https://www.drapastrana.com/\n\n🇺🇸The doctor speaks English\n\n ¡Que tengas un excelente día! 👩‍⚕️✨",
        "meta": {
          "external_id": "A5B99C25BD6876CFBFF1191FF3562A56",
          "source": "evolution"
        }
      },
      {
        "id": 169,
        "sender": "customer",
        "at": 1792438075000,
        "body": "Buenas tardes , mi nombre es Liz soy la auxiliar administrativa del consultorio Dra.Bernal. Claro que si, estaremos atentas! Cualquier duda que tengas nos escribes 🙏🏻",
        "meta": {
          "external_id": "A5BB2507BD93AD730298D34F810508DF",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 9,
    "crmId": 14,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 5,
    "messages": [
      {
        "id": 61,
        "sender": "human",
        "at": 1792253828000,
        "body": "Hola buen día la vi en Instagram me interesa un tratamiento para rejuvenecer la cara tiene valoración esta semana?",
        "meta": {
          "external_id": "3EB0A188AFBD4374063B37",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253828000
          }
        }
      },
      {
        "id": 105,
        "sender": "customer",
        "at": 1792255678000,
        "body": "Hola buen día, gracias por comunicarte con el consultorio de la Dra Patricia Lozano 💕\nEs todo un gusto atenderte, mi nombre es Ana y estoy aquí para ti 🤗",
        "meta": {
          "external_id": "3EB0BFD1C543F7FF7A84D6",
          "source": "evolution"
        }
      },
      {
        "id": 106,
        "sender": "customer",
        "at": 1792255692000,
        "body": "Con quien tengo el gusto de hablar?",
        "meta": {
          "external_id": "3EB06FB585A1A7271B924B",
          "source": "evolution"
        }
      },
      {
        "id": 132,
        "sender": "human",
        "at": 1792349036000,
        "body": "Hola buenas tardes con Daniel quería saber cuánto vale la valoración para rejuvenecer la cara?",
        "meta": {
          "external_id": "3EB0A09C7F7605C5D9CBEA",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792349036000
          }
        }
      },
      {
        "id": 166,
        "sender": "customer",
        "at": 1792437808000,
        "body": "Hola buena tarde Daniel, nos alegra tenerte con nosotras ☺️",
        "meta": {
          "external_id": "3EB0EF359CC9951C11EC40",
          "source": "evolution"
        }
      },
      {
        "id": 167,
        "sender": "customer",
        "at": 1792437820000,
        "body": "Claro si señor con todo el gusto",
        "meta": {
          "external_id": "3EB0B44CBECED0CDC90339",
          "source": "evolution"
        }
      },
      {
        "id": 168,
        "sender": "customer",
        "at": 1792437829000,
        "body": "En nuestra consulta de diagnóstico recibirás la atención y asesoría personalizada de la Dra Martha, quién dedicará un tiempo solo para ti y escuchará tus dudas, para asi definir la mejor opción de tratamiento para lo que deseas corregir.\n\nEsta consulta tiene un  valor de $200.000 en efectivo o transferencia y se tendrá en cuenta para ser descontado del costo del primer tratamiento que te realices dentro de los primeros 30 días siguientes a la valoración.\n\nNota: Si te realizas el tratamiento el mismo día de la valoración, solo pagas el valor del tratamiento. Nuestras consultas de control de tratamiento no tienen costo 💕",
        "meta": {
          "external_id": "3EB0FA639BC55715AD34FE",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 4,
    "crmId": 9,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 2,
    "messages": [
      {
        "id": 46,
        "sender": "human",
        "at": 1792247234000,
        "body": "Hola, buenos días los vi en Instagram, me interesan los bioestimuladores de colágeno tienen espacio esta semana para una valoración?",
        "meta": {
          "external_id": "3EB0EEE52E0ABCBE377592",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792247234000
          }
        }
      },
      {
        "id": 117,
        "sender": "customer",
        "at": 1792263692000,
        "body": "Hola buen día, te saluda Sol, cómo estás ?🤩",
        "meta": {
          "external_id": "3EB0605F547C58DC13E59B",
          "source": "evolution"
        }
      },
      {
        "id": 118,
        "sender": "customer",
        "at": 1792263795000,
        "body": "el dia viernes 23 a las 8:30am",
        "meta": {
          "external_id": "3EB09240D5A69976D8B583",
          "source": "evolution"
        }
      },
      {
        "id": 119,
        "sender": "customer",
        "at": 1792263797000,
        "body": "puedes?",
        "meta": {
          "external_id": "3EB0F7017A1CE5BFC79806",
          "source": "evolution"
        }
      },
      {
        "id": 120,
        "sender": "customer",
        "at": 1792263802000,
        "body": "La Dra. es médico estético especializada en armonización facial, calidad de piel, tratamientos capilares y corporales, con un enfoque médico y personalizado para lograr resultados naturales y armónicos ✨\n\nhttps://www.instagram.com/reel/DQ-OQVzjjmb/?igsh=MTRyaHRkZ2ZtdXhzZg==\n\n💰 Valor de la valoración: $200.000\n📄 Incluye informe completo del análisis facial y orientación profesional.\n\nSerá un gusto acompañarte en este proceso.\n¿Deseas que te indique disponibilidad de agenda? ✨",
        "meta": {
          "external_id": "3EB087B77DB89D99DB6F07",
          "source": "evolution"
        }
      },
      {
        "id": 126,
        "sender": "human",
        "at": 1792348944000,
        "body": "Hola buenas tardes Sol muchas gracias por la información el viernes no me queda posible lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB023D87872DAF7290A75",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792348944000
          }
        }
      },
      {
        "id": 164,
        "sender": "customer",
        "at": 1792426681000,
        "body": "Hola buen día, te saluda Sol, cómo estás ?🤩",
        "meta": {
          "external_id": "3EB04FA28170D9159E7530",
          "source": "evolution"
        }
      },
      {
        "id": 165,
        "sender": "customer",
        "at": 1792426693000,
        "body": "quedo atenta para indicarte disponibilidad de agenda?",
        "meta": {
          "external_id": "3EB005D124A8B3F99E9ACE",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 19,
    "crmId": 24,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 2,
    "messages": [
      {
        "id": 81,
        "sender": "human",
        "at": 1792254317000,
        "body": "Hola buenos días me interesa la armonización facial tienen valoración disponible esta semana?",
        "meta": {
          "external_id": "3EB06B1D74E4807AA3430B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254317000
          }
        }
      },
      {
        "id": 162,
        "sender": "customer",
        "at": 1792421617000,
        "body": "Buenos días, ¿cómo estás? Espero que te encuentres muy bien el día de hoy, te saluda Alejandra💛✨",
        "meta": {
          "external_id": "3EB0575C2AE9A49C5106AF",
          "source": "evolution"
        }
      },
      {
        "id": 163,
        "sender": "customer",
        "at": 1792421663000,
        "body": "Claro que sí, con mucho gusto,  la disponibilidad más cercana que te puedo ofrecer es para mañana a las 9:00 am con la Dra Kelly, te va bien esta disponibilidad?",
        "meta": {
          "external_id": "3EB08BD1C59F616C0ACB20",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 20,
    "crmId": 25,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 3,
    "messages": [
      {
        "id": 84,
        "sender": "human",
        "at": 1792254357000,
        "body": "Hola buen día los vi en Instagram quiero relleno de ojeras qué precio tiene?",
        "meta": {
          "external_id": "3EB0030E2E6F4FB751D1EF",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254357000
          }
        }
      },
      {
        "id": 85,
        "sender": "customer",
        "at": 1792254359000,
        "body": "¡Hola!\nMuchas Gracias por comunicarte con Estetica Norte Clínica. Al continuar en este canal y dando cumplimiento a la ley 1581 de 2012, estas aceptando y aprobando nuestra política de protección y tratamiento de datos publicada en nuestra página web: https://massaiclinica.com/politica-de-tratamiento-de-datos/",
        "meta": {
          "external_id": "A507DB23E8FF2068E4AF6271913B02AC",
          "source": "evolution"
        }
      },
      {
        "id": 87,
        "sender": "customer",
        "at": 1792254423000,
        "body": "Hola, Muchas gracias por escribirnos.  Estamos ubicados en la ciudad de Medellín, sector Poblado Cl 7 sur # 42 - 70 Consultorio 1105, Edificio Fórum contiguo al Centro Comercial Santafé. ¿Con quien tenemos el gusto de hablar?",
        "meta": {
          "external_id": "3EB04DC2BB89BE59DE3607",
          "source": "evolution"
        }
      },
      {
        "id": 139,
        "sender": "human",
        "at": 1792351308000,
        "body": "Hola buenas tardes, con Daniel. Gracias por responder.",
        "meta": {
          "external_id": "3EB0AC51EC522A5B260BA8",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792351308000
          }
        }
      },
      {
        "id": 161,
        "sender": "customer",
        "at": 1792420302000,
        "body": "Buenos dias Sr. Daniel, ¿Como esta? Le habla Milena, cuentenos en que ciudad se encuentra ubicado?",
        "meta": {
          "external_id": "3EB04015A60F8AE7F4167C",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 13,
    "crmId": 18,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 4,
    "messages": [
      {
        "id": 69,
        "sender": "human",
        "at": 1792254030000,
        "body": "Hola buenos días vi su Instagram quiero un diseño de sonrisa con carillas en porcelana cuánto cuesta más o menos?",
        "meta": {
          "external_id": "3EB0EBDBA9B8F8CF1A557B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254030000
          }
        }
      },
      {
        "id": 77,
        "sender": "customer",
        "at": 1792254245000,
        "body": "Buenos días 👋, Hoy tiene el gusto de atenderte Alexandra de OralStudio 🦷¿Cuál es tu nombre?",
        "meta": {
          "external_id": "3EB0E5ED6E8526CA478B86863CE908F1D37B",
          "source": "evolution"
        }
      },
      {
        "id": 79,
        "sender": "customer",
        "at": 1792254288000,
        "body": "El diseño de sonrisa con carillas en porcelana es un tratamiento personalizado, y su costo depende de la cantidad de carillas que necesites y de las características de tu sonrisa.\n\nPara brindarte información más precisa, te invitamos a una cita de valoración sin costo, en la que nuestro especialista podrá evaluar tu caso y recomendarte la mejor opción según tus necesidades y expectativas. \n\n¿Qué día y en qué horario te gustaría visitarnos? Así podemos verificar nuestra disponibilidad y ayudarte a programarla. ",
        "meta": {
          "external_id": "3EB022BD317604A048D8B0755ACBB3219708",
          "source": "evolution"
        }
      },
      {
        "id": 133,
        "sender": "human",
        "at": 1792349062000,
        "body": "Hola buenas tardes con Daniel muchas gracias por la información esta semana tengo complicado lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB003AE272650B716E74B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792349062000
          }
        }
      },
      {
        "id": 134,
        "sender": "customer",
        "at": 1792349130000,
        "body": "¡Gracias por contactarnos! En este momento no estamos disponibles, pero te responderemos lo más pronto posible.\n🕘 *Nuestro horario de atención es: Lunes a Viernes: 8:30a.m. a 6:00 p.m. Sábados: 8:00 a.m. a 12:00 p.m.*\n¿Cuál es tu nombre? Cuéntanos cómo podemos ayudarte 🦷💙\n\nWe’re glad you contacted us. We're currently out of the office, but we'll get back to you as soon as possible.\n🕘 *You can reach us during: Monday to Friday: 8:30a.m. – 6:00 p.m. Saturday: 8:00 a.m. – 12:00 p.m.*\nMay we know your name? Let us know how we can help you! 🦷💙",
        "meta": {
          "external_id": "6A315FC7425CF3F13BDA",
          "source": "evolution"
        }
      },
      {
        "id": 160,
        "sender": "customer",
        "at": 1792418743000,
        "body": "¡Hola, Daniel! 😊 Buenos días. Claro que sí, no te preocupes. Muchas gracias por tenernos en cuenta. Cuando tengas disponibilidad, estaremos encantados de ayudarte a agendar tu cita de valoración sin costo para conocer tus expectativas y brindarte la mejor opción para tu diseño de sonrisa. 🦷✨\n\n¡Quedamos atentos a tu mensaje! 💙",
        "meta": {
          "external_id": "3EB073F11B0A3E3841C28336E168E36D9D64",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 15,
    "crmId": 20,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 1,
    "messages": [
      {
        "id": 72,
        "sender": "human",
        "at": 1792254128000,
        "body": "Hola buenos días quiero información del relleno de labios con ácido hialurónico tienen cita esta semana?",
        "meta": {
          "external_id": "3EB02E36D15B2AB939F699",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254128000
          }
        }
      },
      {
        "id": 159,
        "sender": "customer",
        "at": 1792418224000,
        "body": "Hola muy buenos días, espero te encuentres muy bien.✨  \nTe habla Cristina asesora de FullDemo, estoy aquí para brindarte toda la información y asesoría de nuestros procedimientos.\n\nCuál es tu nombre?",
        "meta": {
          "external_id": "3EB0D961B1E9C6F9CAD88E",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 16,
    "crmId": 21,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 5,
    "messages": [
      {
        "id": 73,
        "sender": "human",
        "at": 1792254180000,
        "body": "Hola buen día los vi en Instagram me interesan los bioestimuladores de colágeno qué precio tienen?",
        "meta": {
          "external_id": "3EB0C6BC37D397605E7001",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254180000
          }
        }
      },
      {
        "id": 80,
        "sender": "customer",
        "at": 1792254305000,
        "body": "✨ ¡Hola! Bienvenido(a) a Bonaventura Demo Medicina Estetica Demo y Bienestar.\n\nSoy Ana María, gerente comercial. \n\n¡Será un gusto atenderte! 😊",
        "meta": {
          "external_id": "A528C6758BA36CA8236E80E9AD4677E1",
          "source": "evolution"
        }
      },
      {
        "id": 82,
        "sender": "customer",
        "at": 1792254344000,
        "body": "Los bioestimuladores de colágeno cómo sculptra y radiesse tienen un valor de $2'550.000",
        "meta": {
          "external_id": "A5A1DC8ED3526DD96F155EB9473C9634",
          "source": "evolution"
        }
      },
      {
        "id": 83,
        "sender": "customer",
        "at": 1792254351000,
        "body": "Te los has realizado anteriormente?",
        "meta": {
          "external_id": "A576EC6FDC08C93A16850A10150BA2ED",
          "source": "evolution"
        }
      },
      {
        "id": 137,
        "sender": "human",
        "at": 1792349362000,
        "body": "Hola buenas tardes no nunca me los he hecho lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB07843DEF6C362892013",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792349362000
          }
        }
      },
      {
        "id": 138,
        "sender": "customer",
        "at": 1792349365000,
        "body": "¡Hola! Gracias por contactarte con *Bonaventura Demo Medicina Estetica Demo y Bienestar* \n\nHemos recibido tu mensaje con éxito y nos  comunicaremos contigo a la brevedad posible. Agradecemos tu paciencia.🧖‍♀️🧖‍♂️\n\n*Horario de atención:* 🕛\n*Lunes 10:15 am a 6:00pm*\nMartes y miércoles \n*9:15 am a 6:00 pm.*\nJueves y viernes\n *9:15 am a 7:00 pm*\nSábados\n *9 am a 1 pm* \n\nConoce aquí nuestros servicios y elige el que más te guste ⬇️\nhttps://wa.me/c/573005550016",
        "meta": {
          "external_id": "A5C27DF26403F74B526A74F8497800A7",
          "source": "evolution"
        }
      },
      {
        "id": 158,
        "sender": "customer",
        "at": 1792417955000,
        "body": "Buenos días. Estaremos disponibles si tiene alguna duda o pregunta",
        "meta": {
          "external_id": "A54D9EB275827425B27F2F0000CA3642",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 25,
    "crmId": 30,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 7,
    "messages": [
      {
        "id": 91,
        "sender": "human",
        "at": 1792254559000,
        "body": "Hola buenos días me interesa un diseño de sonrisa tiene agenda esta semana?",
        "meta": {
          "external_id": "3EB06C6733C5BF8389F3C1",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254559000
          }
        }
      },
      {
        "id": 92,
        "sender": "customer",
        "at": 1792254565000,
        "body": "¡Hola! 💚 Gracias por escribir a *Lina Caballero Odontologia*.\n\nYa recibimos tu mensaje y pronto te responderemos personalmente. ✨\n\nCuéntanos, ¿qué tratamiento te interesa?\n\n🦷 Diseño de sonrisa / Carillas\n✨ Blanqueamiento dental\n💬 Otro\n\n¡Estamos felices de ayudarte! 😊",
        "meta": {
          "external_id": "A52DFA806571DA8DA5C911BDCA81C1D8",
          "source": "evolution"
        }
      },
      {
        "id": 114,
        "sender": "customer",
        "at": 1792262733000,
        "body": "Hola buenas tardes! \nUn gusto saludarte 🙏🏻",
        "meta": {
          "external_id": "A5E6849B60A0E429234B3AE8EDD9AE37",
          "source": "evolution"
        }
      },
      {
        "id": 115,
        "sender": "customer",
        "at": 1792262775000,
        "body": "Claro que sí. Tengo espacio el lunes 2:00pm",
        "meta": {
          "external_id": "A55FB3598E1E38102A56E9DF3F864AC9",
          "source": "evolution"
        }
      },
      {
        "id": 116,
        "sender": "customer",
        "at": 1792262842000,
        "body": "Cuentame si ese día y horario está bien para ti 🤗",
        "meta": {
          "external_id": "A582A0C8FBB4B11503702530C80902F9",
          "source": "evolution"
        }
      },
      {
        "id": 123,
        "sender": "human",
        "at": 1792348850000,
        "body": "Hola buenas tardes muchas gracias mañana no me queda posible lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB055A550A2FC6F8E49AF",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792348850000
          }
        }
      },
      {
        "id": 124,
        "sender": "customer",
        "at": 1792348855000,
        "body": "🌙 ¡Hola! Gracias por escribir a *Lina Caballero Odontologia* 💚\n\nEn este momento no estamos disponibles. Nuestro horario de atención es de lunes a sábado, de 8:00 a.m. a 6:00 p.m. Te responderemos personalmente tan pronto estemos de regreso. ✨\n\nMientras tanto, cuéntanos, ¿qué tratamiento te interesa?\n\n🦷 Diseño de sonrisa / Carillas\n✨ Blanqueamiento dental\n💬 Otro\n\n¡Gracias por confiar en nosotros! 😊",
        "meta": {
          "external_id": "A5B57F254E24B55A0C0CC45CA07B1E6B",
          "source": "evolution"
        }
      },
      {
        "id": 156,
        "sender": "customer",
        "at": 1792417498000,
        "body": "Hola buenos días!",
        "meta": {
          "external_id": "A5EEB9D30071D8B0767C591E328B235C",
          "source": "evolution"
        }
      },
      {
        "id": 157,
        "sender": "customer",
        "at": 1792417532000,
        "body": "Perfecto, si quieres me cuentas en qué horario te queda mejor am o pm y te busco el espacio",
        "meta": {
          "external_id": "A54FA491953B2A4F7C41F2CA52F6AC46",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 7,
    "crmId": 12,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 6,
    "messages": [
      {
        "id": 57,
        "sender": "human",
        "at": 1792253730000,
        "body": "Hola buen día la encontré en Instagram me interesan los implantes dentales tiene cita esta semana?",
        "meta": {
          "external_id": "3EB0DC0A3DC6354591D612",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253730000
          }
        }
      },
      {
        "id": 68,
        "sender": "customer",
        "at": 1792254005000,
        "body": "Gracias por comunicarte con Odontologia Lorena Gil. Por favor, haznos saber cómo podemos ayudarte.",
        "meta": {
          "external_id": "6A9C26083C74A94F8681",
          "source": "evolution"
        }
      },
      {
        "id": 74,
        "sender": "customer",
        "at": 1792254204000,
        "body": "Buen día",
        "meta": {
          "external_id": "2A95D38633328F0CB56D",
          "source": "evolution"
        }
      },
      {
        "id": 76,
        "sender": "customer",
        "at": 1792254230000,
        "body": "Claro q si puedes venir a una valoracion",
        "meta": {
          "external_id": "2A9A71CF78F14B10B9D7",
          "source": "evolution"
        }
      },
      {
        "id": 127,
        "sender": "human",
        "at": 1792348970000,
        "body": "Hola buenas tardes gracias quería saber cuánto vale la valoración para los implantes?",
        "meta": {
          "external_id": "3EB025F76B1CBB267D3FD0",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792348970000
          }
        }
      },
      {
        "id": 128,
        "sender": "customer",
        "at": 1792348981000,
        "body": "Gracias por tu mensaje. En este momento no estamos disponibles, pero te responderemos tan pronto regresemos.",
        "meta": {
          "external_id": "6A08E1F68EBC1EE2141F",
          "source": "evolution"
        }
      },
      {
        "id": 154,
        "sender": "customer",
        "at": 1792417470000,
        "body": "Buen día",
        "meta": {
          "external_id": "2AA08114C342FCC5405C",
          "source": "evolution"
        }
      },
      {
        "id": 155,
        "sender": "customer",
        "at": 1792417479000,
        "body": "La\nValoración tiene un precio de 100",
        "meta": {
          "external_id": "2A98E7150501C3242517",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 21,
    "crmId": 26,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 3,
    "messages": [
      {
        "id": 86,
        "sender": "human",
        "at": 1792254398000,
        "body": "Hola buenos días quiero información del botox cuánto cuesta y tienen cita esta semana?",
        "meta": {
          "external_id": "3EB00AB4601A76C98EC24E",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254398000
          }
        }
      },
      {
        "id": 93,
        "sender": "customer",
        "at": 1792254611000,
        "body": "Buenos días! ☀️ ¿Cómo estás? Espero que te encuentres muy bien. Te habla Carolina de Balance.\n\nPara poder darte el valor exacto del procedimiento, es muy importante que tengamos primero una cita de valoración y así definir lo que mejor se adapte a tus necesidades. Te cuento que tenemos disponibilidad para este *miércoles 21 de octubre a las 3:30 p.m.* Cuéntame, ¿te queda bien este espacio? 💚✨",
        "meta": {
          "external_id": "3EB03CF9006F34DAAD50DF",
          "source": "evolution"
        }
      },
      {
        "id": 140,
        "sender": "human",
        "at": 1792351338000,
        "body": "Hola buenas tardes Carolina muchas gracias el miércoles no me queda posible lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB0BA92BA04446D554825",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792351338000
          }
        }
      },
      {
        "id": 142,
        "sender": "customer",
        "at": 1792351369000,
        "body": "💚 ¡Gracias por escribirnos! Nuestro horario de atención es de Lunes a Viernes de 8:00am a 5:00pm, Sábados de 8:00am a 12:00pm \nDéjanos saber cómo podemos ayudarte, estaremos felices de atenderte tan pronto estemos de vuelta…😃",
        "meta": {
          "external_id": "6AA7539642BDAAA4C2EA",
          "source": "evolution"
        }
      },
      {
        "id": 153,
        "sender": "customer",
        "at": 1792415428000,
        "body": "Buenos días! ☀️ ¿Cómo estás? Espero que te encuentres muy bien. Te habla Carolina de Balance.\n\nEstá bien! Quedamos súper atentas a cuando nos confirmes tu disponibilidad. Te deseo un excelente inicio de semana. 💚✨",
        "meta": {
          "external_id": "3EB035D72468D26AD51518",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 12,
    "crmId": 17,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 3,
    "messages": [
      {
        "id": 67,
        "sender": "human",
        "at": 1792253981000,
        "body": "Hola buen día me interesa el blanqueamiento dental tienen cita esta semana?",
        "meta": {
          "external_id": "3EB0510919ACC45D1A20D3",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253981000
          }
        }
      },
      {
        "id": 94,
        "sender": "customer",
        "at": 1792254618000,
        "body": "Buenos días cómo estás claro que si",
        "meta": {
          "external_id": "3AEB6CAEA74209AB54DA",
          "source": "evolution"
        }
      },
      {
        "id": 95,
        "sender": "customer",
        "at": 1792254628000,
        "body": "Limpieza 85.000",
        "meta": {
          "external_id": "3AB9AA7AFA108AE663F8",
          "source": "evolution"
        }
      },
      {
        "id": 96,
        "sender": "customer",
        "at": 1792254635000,
        "body": "Blanqueamiento 160.000",
        "meta": {
          "external_id": "3A9EE2D9EACF30BA055F",
          "source": "evolution"
        }
      },
      {
        "id": 97,
        "sender": "customer",
        "at": 1792254639000,
        "body": "Cada sección",
        "meta": {
          "external_id": "3A0CA0662697A63C2F03",
          "source": "evolution"
        }
      },
      {
        "id": 98,
        "sender": "customer",
        "at": 1792254642000,
        "body": "Una por semana",
        "meta": {
          "external_id": "3AD2CBBC3A59A979327D",
          "source": "evolution"
        }
      },
      {
        "id": 99,
        "sender": "customer",
        "at": 1792254650000,
        "body": "Maximo hacemos 5 secciones",
        "meta": {
          "external_id": "3ADB2FEB5B5FF93CB4BA",
          "source": "evolution"
        }
      },
      {
        "id": 100,
        "sender": "customer",
        "at": 1792254663000,
        "body": "Lunes en la mañana tengo espacio",
        "meta": {
          "external_id": "3A652AC34613FDD96C91",
          "source": "evolution"
        }
      },
      {
        "id": 101,
        "sender": "customer",
        "at": 1792254666000,
        "body": "A las 8 am",
        "meta": {
          "external_id": "3AF02B50197B98362267",
          "source": "evolution"
        }
      },
      {
        "id": 102,
        "sender": "customer",
        "at": 1792254670000,
        "body": "Quedo pendiente",
        "meta": {
          "external_id": "3A678E26B685F4F27982",
          "source": "evolution"
        }
      },
      {
        "id": 122,
        "sender": "human",
        "at": 1792348827000,
        "body": "Hola buenas tardes muchas gracias por la información mañana no alcanzo a ir lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB0A64B8F0126F493768E",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792348827000
          }
        }
      },
      {
        "id": 150,
        "sender": "customer",
        "at": 1792368898000,
        "body": "Buenas tardes gracias por avisarme",
        "meta": {
          "external_id": "3A52F60FC3D9FE82E938",
          "source": "evolution"
        }
      },
      {
        "id": 151,
        "sender": "customer",
        "at": 1792369206000,
        "body": "Quedo peny",
        "meta": {
          "external_id": "3A51363A58B5AD1B5311",
          "source": "evolution"
        }
      },
      {
        "id": 152,
        "sender": "customer",
        "at": 1792369207000,
        "body": "Pendiente",
        "meta": {
          "external_id": "3AC4452358FE75CC1920",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 2,
    "crmId": 7,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 6,
    "messages": [
      {
        "id": 44,
        "sender": "human",
        "at": 1792247133000,
        "body": "Hola, buenos días vi su perfil en Instagram, me interesa el relleno de labios tienen agenda esta semana?",
        "meta": {
          "external_id": "3EB0D6EF43839DF091B264",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792247133000
          }
        }
      },
      {
        "id": 110,
        "sender": "customer",
        "at": 1792259715000,
        "body": "Hola +27, muy buen día. ¿Cómo estás? gusto en saludarte ☀️ ¡Bienvenid@ a nuestra clínica Aurea Medical Spa! Seré tu asesora de Bienestar y Salud.",
        "meta": {
          "external_id": "3EB07B90B0E58EDDEDA6",
          "source": "evolution"
        }
      },
      {
        "id": 125,
        "sender": "human",
        "at": 1792348879000,
        "body": "Hola buenas tardes con Daniel quería saber cuánto vale el relleno de labios?",
        "meta": {
          "external_id": "3EB0F8363C4FB589520D7D",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792348879000
          }
        }
      },
      {
        "id": 143,
        "sender": "customer",
        "at": 1792352117000,
        "body": "Hola muy buenas tardes claro que si.  ",
        "meta": {
          "external_id": "3EB0F79FECDC2FE56B52",
          "source": "evolution"
        }
      },
      {
        "id": 144,
        "sender": "customer",
        "at": 1792352143000,
        "body": "Dame un momento ya te damos respuesta.  ",
        "meta": {
          "external_id": "3EB0B494A29DE766D3BE",
          "source": "evolution"
        }
      },
      {
        "id": 145,
        "sender": "customer",
        "at": 1792352215000,
        "body": "1.450.000 La jeringa, pero esta semana tenemos un descuento espacial que te quedaría en $1.300.000 ",
        "meta": {
          "external_id": "3EB0CB274C7C20839FCC",
          "source": "evolution"
        }
      },
      {
        "id": 146,
        "sender": "customer",
        "at": 1792352221000,
        "body": "Cuando tienes disponibilidad , ? ",
        "meta": {
          "external_id": "3EB04DCD8A0833584C3C",
          "source": "evolution"
        }
      },
      {
        "id": 147,
        "sender": "customer",
        "at": 1792355517000,
        "body": "? ",
        "meta": {
          "external_id": "3EB08E0648AC6DFA3DEA",
          "source": "evolution"
        }
      },
      {
        "id": 149,
        "sender": "customer",
        "at": 1792367477000,
        "body": "Hola buenas noches quedamos muy atentas ",
        "meta": {
          "external_id": "3EB039C069C176497AC3",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 23,
    "crmId": 28,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 3,
    "messages": [
      {
        "id": 89,
        "sender": "human",
        "at": 1792254481000,
        "body": "Hola buenos días la encontré en Instagram quiero ponerme botox cuánto vale?",
        "meta": {
          "external_id": "3EB0D58BF0B6A52FC1FDD4",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254481000
          }
        }
      },
      {
        "id": 112,
        "sender": "customer",
        "at": 1792261384000,
        "body": "Buenas tardes cómo estás mucho gusto",
        "meta": {
          "external_id": "2A9C2DC61D5A324444F3",
          "source": "evolution"
        }
      },
      {
        "id": 113,
        "sender": "customer",
        "at": 1792261443000,
        "body": "¡Hola! 🌸 Muy buenos días. Qué gusto saludarte y gracias por encontrarme en Instagram. 💕\n\nTe cuento que durante este mes tenemos un precio especial de $1.000.000 en la aplicación de toxina botulínica (Botox) en las 3 zonas del tercio superior del rostro: frente, entrecejo y patas de gallina. ✨\n\nEs uno de mis tratamientos favoritos para suavizar las líneas de expresión, prevenir que las arrugas se marquen más y conseguir una apariencia más fresca, descansada y natural, sin perder tu expresión. 💉\n\nLa aplicación la realizo personalmente, previa valoración para adaptar el tratamiento a tus necesidades.\n\n¿Ya te has aplicado Botox anteriormente o sería tu primera vez? 🥰\n\n¡Me encantará asesorarte y ayudarte a conseguir ese resultado natural que buscas!",
        "meta": {
          "external_id": "2A2D26C35F7E7646A124",
          "source": "evolution"
        }
      },
      {
        "id": 141,
        "sender": "human",
        "at": 1792351365000,
        "body": "Hola buenas tardes sería mi primera vez lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB007999D0A8B416DB310",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792351365000
          }
        }
      },
      {
        "id": 148,
        "sender": "customer",
        "at": 1792363059000,
        "body": "Claro que si 👍🏻 quedó súper atenta se que te va a encantar!",
        "meta": {
          "external_id": "2AACC09E271B2A8B4516",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 8,
    "crmId": 13,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 2,
    "messages": [
      {
        "id": 58,
        "sender": "human",
        "at": 1792253781000,
        "body": "Hola buenos días vi su perfil quiero información de carillas en resina qué precio tienen?",
        "meta": {
          "external_id": "3EB0E4C52CF86DA83FB4AB",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253781000
          }
        }
      },
      {
        "id": 59,
        "sender": "customer",
        "at": 1792253783000,
        "body": "Hola!☺️, muchas gracias por escribirnos. Mi nombre es Juliana y soy parte del equipo Clínica Natalia Ortiz. Cuéntame, ¿Que problema has estado presentando con tu sonrisa?👩🏻‍⚕️🦷🙌🏻",
        "meta": {
          "external_id": "A5603776393985276BB2736120431151",
          "source": "evolution"
        }
      },
      {
        "id": 62,
        "sender": "customer",
        "at": 1792253837000,
        "body": "Hola, hablas con Juliana de Clinica Natalia Ortiz ☺️\n\nAntes de continuar, te informamos que el tratamiento de tus datos personales se realiza conforme a nuestro Aviso de Privacidad. Al continuar con la atención, aceptas nuestras políticas:\n\nhttps://clinicasilviahoyos.dentalink.cl/politicas-privacidad/ZlWpfhXLdD9AnCyxcLzk1_9IyziYAz8W",
        "meta": {
          "external_id": "CED9811943F2150642F0",
          "source": "evolution"
        }
      },
      {
        "id": 63,
        "sender": "customer",
        "at": 1792253837000,
        "body": "Sobre las carillas en resina, te cuento que son una excelente opción para mejorar la forma y el color de tus dientes. No manejamos un precio fijo o aproximado de forma general, ya que el tratamiento es totalmente personalizado según tus necesidades. Por eso, el primer paso que debemos hacer es una cita de valoración, donde nuestra Dra. experta revise tu caso y te brinde una solución precisa.☺️\n\nLa consulta tiene un valor de $100.000 COP e incluye:\n- Consulta personalizada con nuestra Dra. experta.\n- Equipos de alta tecnología para un diagnóstico preciso y cómodo.\n- Plan de tratamiento acorde a tus necesidades y presupuesto",
        "meta": {
          "external_id": "CE0CE154E2C4EFE36CE8",
          "source": "evolution"
        }
      },
      {
        "id": 64,
        "sender": "customer",
        "at": 1792253838000,
        "body": "Para orientarte mejor, cuéntame, ¿qué te gustaría mejorar realmente de tu sonrisa? ☺️",
        "meta": {
          "external_id": "CE827B3D1B2DDF9EED89",
          "source": "evolution"
        }
      },
      {
        "id": 111,
        "sender": "customer",
        "at": 1792261040000,
        "body": "Hola, me gustaría saber qué te gustaría mejorar de tu sonrisa para poder orientarte mejor.",
        "meta": {
          "external_id": "CEEFB80436CBE164CFA7",
          "source": "evolution"
        }
      },
      {
        "id": 121,
        "sender": "customer",
        "at": 1792335684000,
        "body": "Quedo atenta por si deseas retomar la información más adelante, puedes escribirme cuando gustes.",
        "meta": {
          "external_id": "CE9D0FF7FFCA11222366",
          "source": "evolution"
        }
      },
      {
        "id": 129,
        "sender": "human",
        "at": 1792349007000,
        "body": "Hola buenas tardes quisiera mejorar el color y la forma de los dientes de adelante lo pienso y les confirmo",
        "meta": {
          "external_id": "3EB0731F11ABE7B437F958",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792349007000
          }
        }
      },
      {
        "id": 130,
        "sender": "customer",
        "at": 1792349034000,
        "body": "Entiendo perfectamente. Tómate el tiempo que necesites para pensarlo y revisar qué es lo que más te gustaría mejorar en tu sonrisa",
        "meta": {
          "external_id": "CEF10DF258D6362166D6",
          "source": "evolution"
        }
      },
      {
        "id": 131,
        "sender": "customer",
        "at": 1792349035000,
        "body": "Cuando estés listo para dar el siguiente paso o si tienes alguna otra duda, aquí estaré para ayudarte. ¡Que tengas una excelente tarde! ☺️",
        "meta": {
          "external_id": "CE515861C45DFD8CB76D",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 24,
    "crmId": 29,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 2,
    "messages": [
      {
        "id": 90,
        "sender": "human",
        "at": 1792254519000,
        "body": "Hola buen día vi su Instagram quiero arreglarme la sonrisa con carillas tiene cita esta semana?",
        "meta": {
          "external_id": "3EB0AAB79882768016CD43",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254519000
          }
        }
      },
      {
        "id": 103,
        "sender": "customer",
        "at": 1792254779000,
        "body": "¡Hola! Gracias por escribir al Consultorio del Dr. Mateo Villa.🦷\n\nDéjanos tu nombre completo para agendar tu cita.",
        "meta": {
          "external_id": "6AEE106456422AAA14A4",
          "source": "evolution"
        }
      },
      {
        "id": 104,
        "sender": "customer",
        "at": 1792255134000,
        "body": "Estamos ubicados:\n\n-📍Cra 48 # 46a sur 107 oficina 1013 Envigado\nTorres del Sur o Torre Oncologica\nEn frente del polideportivo Sur por la Av las Vegas.",
        "meta": {
          "external_id": "2A40688CCE42311C8D51",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 22,
    "crmId": 27,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 88,
        "sender": "human",
        "at": 1792254439000,
        "body": "Hola buen día me interesa el relleno de labios tienen valoración esta semana?",
        "meta": {
          "external_id": "3EB0B12AA9F8B1780DD33B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254439000
          }
        }
      }
    ]
  },
  {
    "clinicId": 18,
    "crmId": 23,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 78,
        "sender": "human",
        "at": 1792254284000,
        "body": "Hola buen día vi su perfil quiero hacerme carillas cuánto vale el diseño de sonrisa?",
        "meta": {
          "external_id": "3EB070FA074DC31092FDD4",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254284000
          }
        }
      }
    ]
  },
  {
    "clinicId": 17,
    "crmId": 22,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 75,
        "sender": "human",
        "at": 1792254225000,
        "body": "Hola buenos días quiero una valoración para botox tienen espacio esta semana en la sede Poblado?",
        "meta": {
          "external_id": "3EB0D7F830BB9C9AD3294B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792254225000
          }
        }
      }
    ]
  },
  {
    "clinicId": 11,
    "crmId": 16,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 66,
        "sender": "human",
        "at": 1792253926000,
        "body": "Hola buenos días quiero información de armonización facial cuánto vale?",
        "meta": {
          "external_id": "3EB03C2555B062BFE4921F",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253926000
          }
        }
      }
    ]
  },
  {
    "clinicId": 10,
    "crmId": 15,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 65,
        "sender": "human",
        "at": 1792253880000,
        "body": "Buenos días quiero arreglarme los dientes con carillas tienen agenda esta semana?",
        "meta": {
          "external_id": "3EB0B5AAE9F0E32EB34E6B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253880000
          }
        }
      }
    ]
  },
  {
    "clinicId": 6,
    "crmId": 11,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 1,
    "messages": [
      {
        "id": 56,
        "sender": "human",
        "at": 1792253677000,
        "body": "Hola buenos días los vi en Instagram quiero hacerme diseño de sonrisa cuánto cuesta y tienen cita esta semana?",
        "meta": {
          "external_id": "3EB0CBA7CB2F627381F259",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792253677000
          }
        }
      },
      {
        "id": 60,
        "sender": "customer",
        "at": 1792253794000,
        "body": "Gracias por comunicarte con Sonrisa Real Odontología Integral Especializada. ¿Cómo podemos ayudarte?",
        "meta": {
          "external_id": "2A8F9FF0ABF8E304B209",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 1,
    "crmId": 6,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 43,
        "sender": "human",
        "at": 1792247094000,
        "body": "Hola, buenos días. Los vi en Instagram quiero ponerme botox en la frente tienen cupo esta semana?",
        "meta": {
          "external_id": "3EB0ECAE41CF90DAD86864",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792247094000
          }
        }
      },
      {
        "id": 31,
        "sender": "customer",
        "at": 1792247676900,
        "body": "Hola buenos días",
        "meta": {
          "external_id": "2A7831C8F3D3F18F3A9C",
          "source": "evolution"
        }
      },
      {
        "id": 32,
        "sender": "customer",
        "at": 1792247685967,
        "body": "Con quien tengo el gusto de hablar?",
        "meta": {
          "external_id": "2AFE7C1F4B051627C1AF",
          "source": "evolution"
        }
      },
      {
        "id": 48,
        "sender": "human",
        "at": 1792248017000,
        "body": "Buenos días, con Daniel quería saber cuánto vale el botox en la frente y si tienen cita esta semana.",
        "meta": {
          "external_id": "3EB00CCD5EF2D4A47F0B16",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792248017000
          }
        }
      },
      {
        "id": 40,
        "sender": "customer",
        "at": 1792248904839,
        "body": "Claro señor Daniel, es primera vez que la aplicas?",
        "meta": {
          "external_id": "3EB0A8C9010FDBE2116D48",
          "source": "evolution"
        }
      },
      {
        "id": 41,
        "sender": "customer",
        "at": 1792248928466,
        "body": "el precio de la toxina en la zona de la frente es de 480.000",
        "meta": {
          "external_id": "3EB08709950AB4FB4404CB",
          "source": "evolution"
        }
      },
      {
        "id": 42,
        "sender": "customer",
        "at": 1792248942779,
        "body": "me confirmas nombre completo y cedula para agendarte por favor!",
        "meta": {
          "external_id": "3EB020C1F713C9604F8EB5",
          "source": "evolution"
        }
      },
      {
        "id": 51,
        "sender": "human",
        "at": 1792250300000,
        "body": "Listo, muchas gracias lo pienso y les confirmo.",
        "meta": {
          "external_id": "3EB019943D9591591F4A32",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792250300000
          }
        }
      },
      {
        "id": 55,
        "sender": "customer",
        "at": 1792250469000,
        "body": "Vale, quedo súper atenta",
        "meta": {
          "external_id": "2AD409ED2EB83B04719C",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 3,
    "crmId": 8,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 45,
        "sender": "human",
        "at": 1792247159000,
        "body": "Hola, buenos días la encontré en Instagram, quiero información de armonización facial tiene citas disponibles esta semana?",
        "meta": {
          "external_id": "3EB016F52ABCA21F9A5F71",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792247159000
          }
        }
      },
      {
        "id": 30,
        "sender": "customer",
        "at": 1792247163992,
        "body": "Buen día, te damos la Bienvenida a Dra. Carolina Mendez, medicina estética y funcional, *por favor indícame tu nombre y apellido* para brindarte una atención más personalizada.",
        "meta": {
          "external_id": "A5D730DA8383408A916636D98A683B2F",
          "source": "evolution"
        }
      },
      {
        "id": 49,
        "sender": "human",
        "at": 1792248045000,
        "body": "Daniel Monoga quería información sobre armonización facial qué precio tiene?",
        "meta": {
          "external_id": "3EB0AED9988EA93CDEF9FD",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792248045000
          }
        }
      },
      {
        "id": 33,
        "sender": "customer",
        "at": 1792248061284,
        "body": "Daniel, los tratamientos de armonización facial tienen valores desde $650.000 para zonas pequeñas. El valor final depende de las zonas y el protocolo ideal, que se define en una valoración médica personalizada. ¿Te gustaría agendar una cita para valoración?",
        "meta": {
          "external_id": "CE9C9B9DF3135B88486F",
          "source": "evolution"
        }
      },
      {
        "id": 50,
        "sender": "human",
        "at": 1792248172000,
        "body": "La valoración tiene costo? Lo pienso y les confirmo.",
        "meta": {
          "external_id": "3EB0600A5B528762E513FA",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792248172000
          }
        }
      },
      {
        "id": 34,
        "sender": "customer",
        "at": 1792248184929,
        "body": "Claro que sí, Daniel. Una persona del consultorio te puede confirmar el costo de la valoración y orientarte con ese dato.",
        "meta": {
          "external_id": "CECF147D5F62AA791AF6",
          "source": "evolution"
        }
      },
      {
        "id": 35,
        "sender": "customer",
        "at": 1792248334242,
        "body": ".Hola Daniel buenas tardes,  te  saludamos del equipo de atencion a pacientes de la Dra Carolina Mendez.    Te amplio informacion sobre :\n\n*Valoración médica especializada*\n\nIncluye evaluación médica, análisis de la piel con dermatoscopio, diagnóstico, rutina facial personalizada, plan de tratamiento y fórmula médica si la requieres.\n\n*Valor: $150.000*\n\nSi inicias tu tratamiento el mismo día, *abonamos el 50 % de la valoración al procedimiento elegido.*\n\n¿Prefieres agendar en la mañana o en la tarde?",
        "meta": {
          "external_id": "3EB08CD4D67D87EF96B3C7",
          "source": "evolution"
        }
      },
      {
        "id": 53,
        "sender": "human",
        "at": 1792250351000,
        "body": "Listo, muchas gracias. Lo pienso y les confirmo.",
        "meta": {
          "external_id": "3EB0AC2CB8A408B48FA92B",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792250351000
          }
        }
      },
      {
        "id": 54,
        "sender": "customer",
        "at": 1792250437000,
        "body": "'Estamos para servirte",
        "meta": {
          "external_id": "CEE2FF54BE4AD1B30791",
          "source": "evolution"
        }
      }
    ]
  },
  {
    "clinicId": 5,
    "crmId": 10,
    "handler": "human",
    "ai_mode": "qualify",
    "unread": 0,
    "messages": [
      {
        "id": 47,
        "sender": "human",
        "at": 1792247270000,
        "body": "Hola, buenos días vi su Instagram, quiero arreglarme la sonrisa con carillas tiene cita disponible esta semana?",
        "meta": {
          "external_id": "3EB0D4B71AF0D46644E5E6",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792247270000
          }
        }
      },
      {
        "id": 36,
        "sender": "customer",
        "at": 1792248335491,
        "body": "Buenos días",
        "meta": {
          "external_id": "3EB06420EFB0707E84190E",
          "source": "evolution"
        }
      },
      {
        "id": 37,
        "sender": "customer",
        "at": 1792248353394,
        "body": "primero debes venir a valoración, esa cita es gratuita",
        "meta": {
          "external_id": "3EB0D2D8921BF6FD6A42C4",
          "source": "evolution"
        }
      },
      {
        "id": 38,
        "sender": "customer",
        "at": 1792248391506,
        "body": "20 dientes en resina 4.000.000",
        "meta": {
          "external_id": "3EB0A8D9A620C7CDC1F400",
          "source": "evolution"
        }
      },
      {
        "id": 39,
        "sender": "customer",
        "at": 1792248399824,
        "body": "20 dientes en porcelana 16.000.000",
        "meta": {
          "external_id": "3EB0C1AE3FA808741768D3",
          "source": "evolution"
        }
      },
      {
        "id": 52,
        "sender": "human",
        "at": 1792250322000,
        "body": "Listo muchas gracias lo pienso y les confirmo.",
        "meta": {
          "external_id": "3EB021D36CE6EBB4C5CAC6",
          "source": "evolution",
          "delivery": {
            "status": "sent",
            "at": 1792250322000
          }
        }
      }
    ]
  }
]
```


# Resultado actualizado definitivo — lectura del CRM

**25/25 clínicas identificadas por coincidencia exacta; 140 mensajes revisados.**
- Ventana consultada: lunes 12-oct-2026 00:00:00 America/Bogota a 2026-10-21 13:40:57 America/Bogota (2026-10-21T18:40:57.886Z UTC).
- Mensajes efectivamente disponibles en la ventana: 2026-10-17 09:24:54 a 2026-10-19 14:27:55, America/Bogota. No se encontraron mensajes del 20–21 en estos detalles; no prueba que otros canales o el teléfono carezcan de ellos.
- **Identidad: los 25 hilos pertenecen al contexto de auditoría/paciente Daniel; cero hilos comerciales Loovo identificados en los mensajes revisados.** No todos lo nombran, pero los salientes son consultas como paciente; ninguno presenta a Loovo. No inferir interés comercial de respuestas sobre tratamientos.
- 19 hilos terminan en entrante; eso no equivale a 19 preguntas pendientes. Siete conservan preguntas o solicitud de datos/agenda; los demás contienen información, cierres o automatismos. Cinco hilos no tienen entrantes; uno termina en mensaje propio.
- **Automatización:** los 25 contactos tienen handler=human; no hay mensajes sender=ai en los 140. La fuente local app.ts documenta e implementa el webhook Evolution como registro de ambos lados, sin responder IA ni reenviar mensajes propios (deliver:false). No está implementado allí un autorespondedor Evolution. La equivalencia exacta de fuente local y versión desplegada no fue verificada; el handler humano sí es dato remoto actual.
- Borradores comerciales personalizados: **no corresponden como respuesta a estos entrantes**, porque no hay diálogo comercial Loovo verificado. No se redactan respuestas de paciente ni se promete tratamiento, agenda o resultados. Cualquier transición comercial requiere decisión humana y presentación transparente como Loovo, no continuar fingiendo ser Daniel.
- Prioridad humana: revisar preguntas abiertas de MP Demo Medical, Estetica Norte, FullDemo, REAL, Lina Caballero, Aurea y Villa; no enviar desde Daniel. REAL, Sonríe, Lina y Balance ya tienen rechazo de disponibilidad enviado el 18; se corrige la prioridad histórica de “liberar citas”. No hay reserva confirmada probada.
- Las columnas de tiempo indican antigüedad desde el último entrante, incluso si fue cierre; **no son SLA ni obligación de responder**.

| ID | Clínica | Último emisor y fecha Bogotá | Antigüedad último entrante | Resumen / siguiente paso factual |
|---|---|---|---|---|
| 1 | Centro Integral Aurora de Medicina Estetica | Clínica · 2026-10-17 10:21:09 | 4 d 3 h 19 min | Cierre: «Vale, quedo súper atenta». No exige respuesta. |
| 2 | Aurea Medical Spa (Cabecera) | Clínica · 2026-10-18 18:51:17 | 2 d 18 h 49 min | **Pregunta/solicitud abierta de auditoría.** Pregunta de disponibilidad seguida de recordatorios. No reservar ni continuar como paciente. |
| 3 | Consultorio Dra. Carolina Mendez (Sotomayor) | Clínica · 2026-10-17 10:20:37 | 4 d 3 h 20 min | Cierre: «Estamos para servirte». No exige respuesta. |
| 4 | Vital Medicina Estetica (Sotomayor) | Clínica · 2026-10-19 11:18:13 | 2 d 2 h 22 min | **Pregunta/solicitud abierta de auditoría.** Pregunta si indica disponibilidad, pese al rechazo previo del viernes. No pedir agenda. |
| 5 | Dr. Ricardo Castillo Diseno de Sonrisa (Cabecera) | Propio / paciente · 2026-10-17 10:18:42 | 4 d 3 h 54 min | Último mensaje propio: «lo pienso». Sin entrante posterior registrado; no pendiente de responder. |
| 6 | Sonrisa Norte Bucaramanga (Sotomayor) | Clínica · 2026-10-17 11:16:34 | 4 d 2 h 24 min | Solo saludo automático sin respuesta sustantiva a la consulta; no confundir con interés comercial. |
| 7 | Dra. Lorena Gil Rehabilitacion Oral (Canaveral) | Clínica · 2026-10-19 08:44:39 | 2 d 4 h 56 min | Respuesta literal: «La / Valoración tiene un precio de 100». Unidad monetaria/magnitud no aclarada; no convertirlo en $100.000. |
| 8 | Dra. Natalia Ortiz Diseno de Sonrisa (Cabecera) | Clínica · 2026-10-18 13:43:55 | 2 d 23 h 57 min | Cierre: invita a retomar cuando esté listo. No exige respuesta. |
| 9 | Dra. Patricia Lozano Estetica Antiage (Cabecera) | Clínica · 2026-10-19 14:23:49 | 1 d 23 h 17 min | Resolvió precio de valoración; no hay nueva pregunta ni obligación de contestar. |
| 10 | Los Especialistas Dentales del Norte (Canaveral) | Propio / paciente · 2026-10-17 11:18:00 | Sin entrante | Sin entrante registrado. |
| 11 | Armonia Centro de Alta Estetica | Propio / paciente · 2026-10-17 11:18:46 | Sin entrante | Sin entrante registrado. |
| 12 | Sonrie Clinica Demo Odontologica Norte (Canaveral) | Clínica · 2026-10-18 19:20:07 | 2 d 18 h 20 min | Agradece el aviso de no asistir; no cita confirmada ni pendiente de cancelar probado. |
| 13 | Oral Studio Smile Makeover Demo | Clínica · 2026-10-19 09:05:43 | 2 d 4 h 35 min | Acepta que se retome cuando haya disponibilidad. No exige respuesta. |
| 14 | Dra. Sofia Bernal Medicina Estetica | Clínica · 2026-10-19 14:27:55 | 1 d 23 h 13 min | Cierre del 19: «estaremos atentas». No exige respuesta. |
| 15 | FullDemo Armonizacion Orofacial Demo (El Tesoro) | Clínica · 2026-10-19 08:57:04 | 2 d 4 h 43 min | **Pregunta/solicitud abierta de auditoría.** Pregunta el nombre; no continuar identidad de paciente. |
| 16 | Bonaventura Demo Medicina Estetica Demo | Clínica · 2026-10-19 08:52:35 | 2 d 4 h 48 min | Cierre: disponibles ante dudas. No exige respuesta. |
| 17 | Clinica Demo Sede Poblado | Propio / paciente · 2026-10-17 11:23:45 | Sin entrante | Sin entrante registrado. |
| 18 | Dra. Ana Londono Diseno de Sonrisa | Propio / paciente · 2026-10-17 11:24:44 | Sin entrante | Sin entrante registrado. |
| 19 | MP Demo Medical Center Demo (Milla de Oro) | Clínica · 2026-10-19 09:54:23 | 2 d 3 h 46 min | **Pregunta/solicitud abierta de auditoría.** Ofreció «mañana a las 9:00 am» el 19: corresponde al 20, ya pasado; sin aceptación registrada. No cita confirmada. |
| 20 | Estetica Norte Clinica Estetica Demo | Clínica · 2026-10-19 09:31:42 | 2 d 4 h 9 min | **Pregunta/solicitud abierta de auditoría.** Pregunta ciudad; no inventar ubicación ni continuar como paciente. |
| 21 | Balance Demo Demo | Clínica · 2026-10-19 08:10:28 | 2 d 5 h 30 min | Aceptó el aviso de no disponibilidad del miércoles. No cancelación adicional sustentada. |
| 22 | Clinica Quantum Demo Medicina Estetica | Propio / paciente · 2026-10-17 11:27:19 | Sin entrante | Sin entrante registrado. |
| 23 | Doctora Lucia Cardenas Medicina Estetica | Clínica · 2026-10-18 17:37:39 | 2 d 20 h 3 min | Cierre de cortesía tras «lo pienso». No exige respuesta. |
| 24 | Diseno de Sonrisa Dr. Mateo Villa | Clínica · 2026-10-17 11:38:54 | 4 d 2 h 2 min | **Pregunta/solicitud abierta de auditoría.** Pidió nombre para agendar y envió dirección; no aportar datos ni reservar. |
| 25 | Lina Caballero Odontologia | Clínica · 2026-10-19 08:45:32 | 2 d 4 h 55 min | **Pregunta/solicitud abierta de auditoría.** Pregunta horario am/pm tras rechazar el lunes. No pedir nuevo espacio. |

## Ruta mínima existente y límites
1. Con el mapeo exacto de IDs obtenido en memoria, GET /api/contacts/:id permite volver a leer solo estas clínicas; no ejecutar POST /read. Cookie de esta ejecución ya no se conserva al terminar el proceso.
2. Para responder, Monoga puede usar manualmente su WhatsApp/CRM tras decidir la identidad y el texto. El CRM tiene ruta POST /api/contacts/:id/reply, pero no se ejecutó ni se autoriza por este informe; abrir UI marca leído.
3. No se usaron IA externa, Claude, Chrome, SSH, sugerencias, notas ni envíos. Solo POST login y GET listado/detalles en esta pasada. No hubo recuperación de conexión. state.json y XLSX intactos, diff vacío; único archivo editado: este informe.
4. Limitaciones: detalle CRM sin paginación en fuente; se revisó todo el arreglo messages retornado dentro de la ventana. Historial fuera de CRM, eventos perdidos de webhook, asociaciones LID internas y otros canales no contrastados. Los 25 contactos Evolution encontrados antes no explican los cero mensajes por JID.

Los bloques anteriores se conservan como trazabilidad; este resultado supersede sus bloqueos de identificación y sus prioridades históricas no verificadas.
