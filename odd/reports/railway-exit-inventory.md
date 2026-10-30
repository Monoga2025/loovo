# Railway exit: inventario T1 y plan seguro

**Solo lectura**, sesión Railway CLI 5.63.4; no variables, logs, customer contents, SSH/exec, conexiones a DB, mutaciones ni descargas. Workspace `14770308-00f0-4652-839d-90720c2e041e`; 16 proyectos, 16 entornos, 25 servicios asociados. Los 16 tienen `production`. Aunque usage muestre 11 con consumo, la lista también incluye proyectos vacíos.

La matriz refleja deployment status más reciente por instancia, source repo/image (sin userinfo/query), y volúmenes con capacidad asignada (`sizeMB`) versus ocupación reportada (`currentSizeMB`). Los conteos de ambientes, servicios, volúmenes y conexiones incluyen `pageInfo.hasNextPage=false` en todas las páginas consultadas (first:100); sin truncación/paginación pendiente. Service ID nulo se conserva como asociación sin servicio actual, no se descarta.

| Proyecto (ID) | Entorno (ID) | Servicios (estado; repo o imagen) | Volúmenes (ID: mount; asignado / usado MB; serviceId) |
|---|---|---|---|
| evolution-api-loovo (`79cf1891-7f44-45bc-8d7a-54d8e25b1a74`) | production (`5054e1d1-76e8-435c-bb07-565749c25548`) | omni-crm SUCCESS; sin source. evolution-api SUCCESS; image `evoapicloud/evolution-api:v2.3.7`. Postgres SUCCESS; image `ghcr.io/railwayapp-templates/postgres-ssl:18`. Redis SUCCESS; image `redis:8.2`. | `1723918a-60cb-45e6-ae85-4853ca04185e`: /evolution/instances; 5000 / 82.649; svc `9b0464b1-9915-47b4-a550-213879174b57`. `249589f8-99d0-40fb-9350-c23f0e0167bc`: /var/lib/postgresql/data; 5000 / 232.767; svc `a93b60a4-d0be-4e52-93dd-9da12d643c92`. `8dc1d13c-9553-494a-ba1b-db4ecea81cd8`: /data; 5000 / 102.343; svc `3d92a400-39eb-4376-8bb8-d42a8d673a16`. `944354c1-45bc-466e-b37f-e3c333f87594`: /data; 5000 / 150.479; svc `deedd50e-0586-4c14-885f-ebf71fd53c64`. |
| Maral Pagina web (`bbe01570-fc70-40c1-8824-863b915fa65e`) | production (`024eb864-7464-483c-a294-5e7d3aa82cc2`) | maral-pagina-web SUCCESS; repo `Monoga2025/maral-pagina-web`. | Ninguno listado. |
| monoga-odoo (`ac9949fb-0b27-4dae-bdea-2de97921a09a`) | production (`b6603c17-d842-4d5f-8a36-5240af704ae3`) | Odoo SUCCESS; image `odoo:19.0-20260926`. Postgres SUCCESS; image `postgres:17`. | `997c1ca7-6827-4ece-85d9-a7ef1e666342`: /var/lib/odoo; 5000 / 128.082; svc `0dbcbd3a-b5ce-4913-998f-5234a8cf72d2`. `d055e527-7ff8-4f2d-b747-935f8a827f7d`: /var/lib/postgresql/data; 5000 / 256.131; svc `83f3b1d6-17f2-4201-af87-e2a6e83f992c`. |
| OratorOS (`f10f8f70-0c28-4a92-9938-f81ef9c2ba90`) | production (`73019b45-8de7-4d36-9235-73374e9bd16a`) | oratoros-web SUCCESS; image `ghcr.io/railwayapp/function-bun:1.4.4`. | Ninguno listado. |
| n8n-automation (`dfd66f8d-5649-4f05-b2b8-60afa86f0f6f`) | production (`2df73c8a-72cf-4b06-b499-8152f5411f5d`) | n8n SUCCESS; image `docker.n8n.io/n8nio/n8n:latest`. | `bdbe0b05-169c-45e3-be86-bb548ca52d9b`: /home/node/.n8n; 5000 / 168.280; svc `fadf4aab-3b3b-430b-bbda-1a92500125ef`. |
| monoga-twenty-crm (`7fd83a15-9301-487a-a591-2f091841eadc`) | production (`1fb74e82-7ffc-4eb7-82c5-9e512857bf3a`) | Redis SUCCESS; image `redis:8.2`. twenty-worker SUCCESS; image `twentycrm/twenty:latest`. Postgres SUCCESS; image `ghcr.io/railwayapp-templates/postgres-ssl:18`. twenty-server SUCCESS; image `twentycrm/twenty:latest`. | `13b3c43b-95cf-4084-97a4-97a4dc88a0fe`: /var/lib/postgresql/data; 5000 / 189.571; svc `8ef126e2-2fd1-4627-a9ca-31a94655219e`. `77786d16-96ce-4848-8853-3049264f1fcc`: /data; 5000 / 106.889; svc `09f32f10-6d47-492f-a087-77f478a14d2d`. `e7325902-015a-43b0-92e2-d3e5ab3f973f`: /var/lib/postgresql/data; 5000 / 169.484; **serviceId null**. No asumir prescindible. |
| maral-os (`69cb0fee-7daa-4c7a-851f-30d7393163b4`) | production (`742b1e66-8324-405a-bb92-b98b7cb356e9`) | spirited-nourishment SUCCESS; sin source. Postgres FAILED; image `ghcr.io/railwayapp-templates/postgres-ssl:18`. | `5df21dc5-b532-41b7-8328-596375c2f811`: /var/lib/postgresql/data; 5000 / 164.536; svc `ff9b8565-599e-41e8-bce5-4b1ceb974858`. |
| eblock (`1bb9535b-bbc5-4965-ab9c-56b5d09e32a0`) | production (`04c02132-bf56-4237-9702-4548c19f85c4`) | eblock SUCCESS; source no configurado/null. | Ninguno listado. |
| m1-pro-las-vegas (`26231b96-422e-4061-9246-7243497d0069`) | production (`781aad5a-f896-4977-9c97-5b2caee92d19`) | prueba SUCCESS, m1-pro-las-vegas SUCCESS, campaign-landing-page-1 SUCCESS; los tres repo `Monoga2025/e-bikeglendale`. | Ninguno listado. |
| globalmedcare-staging (`108de9e1-0e27-4178-b88f-43ee54b3df7c`) | production (`a856a5d5-66a3-484b-b02f-b99d7d7c73c0`) | MySQL SUCCESS; image `mysql:9`. globalmedcare-web SUCCESS; sin source. | `2d6b0886-e85a-4415-811a-240532fd1d59`: /var/lib/mysql; 5000 / 288.293; svc `3c029252-972f-4400-b3ab-132adf9ceaff`. |
| universidad-os-jarvis (`a7e458bf-8f9c-41b7-8440-72988cc75d7f`) | production (`e74b052f-e606-4c47-b47b-2ea1b9276558`) | tema-daily-sync SUCCESS; sin source. jarvis-telegram SUCCESS; sin source. | `2cfbaddc-13d8-4b11-b836-aac837c27e57`: /data; 5000 / 1661.895; svc `d1145cb3-4d27-43aa-92a5-541b2a6f7495`. |
| extraordinary-caring (`f91b65b5-2f6c-4383-a09a-286bd350d21a`) | production (`7f0bf092-8e8e-4bfe-9b44-e7fdac3395b7`) | Ninguno listado. | Ninguno listado. |
| affectionate-unity (`9d3b7d45-60e0-4256-90a9-a706cfcfe33f`) | production (`993e219b-56a1-49b4-b7be-a1ef5338b44d`) | Ninguno listado. | Ninguno listado. |
| terrific-tenderness (`75c294e5-ed0b-4b6c-a89d-a8e177710b72`) | production (`fedfe83f-f246-4f3b-aa65-3e79c8523518`) | Bot-Whatsapp; latest deployment null; repo `Monoga2025/Bot-Whatsapp`. | Ninguno listado. |
| motivated-presence (`0f198e66-cf04-40dc-babe-b64830cdd62f`) | production (`7b0dfa75-ad0f-4cd1-8d0c-d5143f3095e8`) | MySQL; latest deployment null; image `mysql:9`. | Ninguno listado. |
| welcoming-light (`0aaaec4f-d4d3-4935-b88c-f4a5b72f18e7`) | production (`be645443-8705-4c17-a371-ac21f2b849bf`) | Ninguno listado. | Ninguno listado. |

**Recuento:** 25 servicios, 22 deployment `SUCCESS`, 1 `FAILED`, 2 sin latest deployment y 13 volúmenes. De 13 volúmenes, 12 asociados a un servicio y 1 sin asociación actual. Capacidad asignada total 65,000 MB; `currentSizeMB` reportado total ≈3,701.399 MB. Son tamaños/capacidad de metadatos, no medición independiente de datos ni garantía de bytes exportables. “Ninguno listado” significa query completa vacía, no UNKNOWN. La fuente `null` indica ausencia de repo/image configurado; refs de repositorio se registran sin descargar.

## Plan y requisitos de respaldo

- Código/repos: preservar desde checkout local existente o clonar refs solo con autorización independiente de descarga. Una referencia de repo/deployment image no es copia de código. Imágenes no se descargaron.
- PostgreSQL/MySQL: usar dump lógico consistente con herramienta nativa (`pg_dump`, `mysqldump`) una vez identificada base, credenciales utilizables solo en entorno de proceso y destino local protegido. No se conectó a DB ni se consultaron variables.
- Redis: identificar política RDB/AOF y método de snapshot consistente antes de respaldar; no asumir dump SQL.
- Volúmenes: snapshots/copia de archivos con método y destino aprobados. Prioridad explícita a los 13 volúmenes, incluyendo el huérfano Twenty de 169.484 MB usados reportados. No inspeccionados ni descargados.
- Cliente/datos fuera de `servicios/` y `landings/`; secretos nunca en archivos. Metadatos de restauración dependientes de credenciales requieren almacén cifrado aprobado o provisión manual segura.

**Siguiente fase:** solo tras autorización expresa de T2 para descargas/copias, comenzar con dumps/copia local en destino protegido, usando credenciales en entorno de proceso, hashes y prueba de restauración aislada. No detener/borrar Railway; apagado requiere confirmación separada después de verificar backups. Nada respalda aún: no prometer preservación completa.

### Query segura reproducible (metadatos T1)

Esta forma de consulta usa selección explícita no sensible; la versión ejecutada usa cada ID devuelto por `railway list --json`, `--compact`, y filtra/sanea en Python antes de output. No ejecutar una consulta de backup ni descarga como parte de T1:

```sh
railway api 'query { project(id:"<PROJECT_ID>") { ...Inventory } } fragment Inventory on Project { id name workspaceId environments(first:100) { pageInfo { hasNextPage } edges { node { id name } } } services(first:100) { pageInfo { hasNextPage } edges { node { id name serviceInstances(first:100) { pageInfo { hasNextPage } edges { node { id environmentId source { image repo } latestDeployment { id status } } } } } } } volumes(first:100) { pageInfo { hasNextPage } edges { node { id name volumeInstances(first:100) { pageInfo { hasNextPage } edges { node { id environmentId serviceId mountPath region sizeMB currentSizeMB } } } } } } }' --compact
```
