# Railway exit: inventario T1 y plan seguro

**Solo lectura**, sesión Railway CLI 5.63.4; no variables, logs, customer contents, SSH/exec, conexiones a DB, mutaciones ni descargas. Workspace `<uuid>`; 16 proyectos, 16 entornos, 25 servicios asociados. Los 16 tienen `production`. Aunque usage muestre 11 con consumo, la lista también incluye proyectos vacíos.

La matriz refleja deployment status más reciente por instancia, source repo/image (sin userinfo/query), y volúmenes con capacidad asignada (`sizeMB`) versus ocupación reportada (`currentSizeMB`). Los conteos de ambientes, servicios, volúmenes y conexiones incluyen `pageInfo.hasNextPage=false` en todas las páginas consultadas (first:100); sin truncación/paginación pendiente. Service ID nulo se conserva como asociación sin servicio actual, no se descarta.

| Proyecto (ID) | Entorno (ID) | Servicios (estado; repo o imagen) | Volúmenes (ID: mount; asignado / usado MB; serviceId) |
|---|---|---|---|
| evolution-api-loovo (`<uuid>`) | production (`<uuid>`) | omni-crm SUCCESS; sin source. evolution-api SUCCESS; image `evoapicloud/evolution-api:v2.3.7`. Postgres SUCCESS; image `ghcr.io/railwayapp-templates/postgres-ssl:18`. Redis SUCCESS; image `redis:8.2`. | `<uuid>`: /evolution/instances; 5000 / 82.649; svc `<uuid>`. `<uuid>`: /var/lib/postgresql/data; 5000 / 232.767; svc `<uuid>`. `<uuid>`: /data; 5000 / 102.343; svc `<uuid>`. `<uuid>`: /data; 5000 / 150.479; svc `<uuid>`. |
| Maral Pagina web (`<uuid>`) | production (`<uuid>`) | maral-pagina-web SUCCESS; repo `Monoga2025/maral-pagina-web`. | Ninguno listado. |
| monoga-odoo (`<uuid>`) | production (`<uuid>`) | Odoo SUCCESS; image `odoo:19.0-20260926`. Postgres SUCCESS; image `postgres:17`. | `<uuid>`: /var/lib/odoo; 5000 / 128.082; svc `<uuid>`. `<uuid>`: /var/lib/postgresql/data; 5000 / 256.131; svc `<uuid>`. |
| OratorOS (`<uuid>`) | production (`<uuid>`) | oratoros-web SUCCESS; image `ghcr.io/railwayapp/function-bun:1.4.4`. | Ninguno listado. |
| n8n-automation (`<uuid>`) | production (`<uuid>`) | n8n SUCCESS; image `docker.n8n.io/n8nio/n8n:latest`. | `<uuid>`: /home/node/.n8n; 5000 / 168.280; svc `<uuid>`. |
| monoga-twenty-crm (`<uuid>`) | production (`<uuid>`) | Redis SUCCESS; image `redis:8.2`. twenty-worker SUCCESS; image `twentycrm/twenty:latest`. Postgres SUCCESS; image `ghcr.io/railwayapp-templates/postgres-ssl:18`. twenty-server SUCCESS; image `twentycrm/twenty:latest`. | `<uuid>`: /var/lib/postgresql/data; 5000 / 189.571; svc `<uuid>`. `<uuid>`: /data; 5000 / 106.889; svc `<uuid>`. `<uuid>`: /var/lib/postgresql/data; 5000 / 169.484; **serviceId null**. No asumir prescindible. |
| maral-os (`<uuid>`) | production (`<uuid>`) | spirited-nourishment SUCCESS; sin source. Postgres FAILED; image `ghcr.io/railwayapp-templates/postgres-ssl:18`. | `<uuid>`: /var/lib/postgresql/data; 5000 / 164.536; svc `<uuid>`. |
| eblock (`<uuid>`) | production (`<uuid>`) | eblock SUCCESS; source no configurado/null. | Ninguno listado. |
| m1-pro-las-vegas (`<uuid>`) | production (`<uuid>`) | prueba SUCCESS, m1-pro-las-vegas SUCCESS, campaign-landing-page-1 SUCCESS; los tres repo `Monoga2025/e-bikeglendale`. | Ninguno listado. |
| globalmedcare-staging (`<uuid>`) | production (`<uuid>`) | MySQL SUCCESS; image `mysql:9`. globalmedcare-web SUCCESS; sin source. | `<uuid>`: /var/lib/mysql; 5000 / 288.293; svc `<uuid>`. |
| universidad-os-jarvis (`<uuid>`) | production (`<uuid>`) | tema-daily-sync SUCCESS; sin source. jarvis-telegram SUCCESS; sin source. | `<uuid>`: /data; 5000 / 1661.895; svc `<uuid>`. |
| extraordinary-caring (`<uuid>`) | production (`<uuid>`) | Ninguno listado. | Ninguno listado. |
| affectionate-unity (`<uuid>`) | production (`<uuid>`) | Ninguno listado. | Ninguno listado. |
| terrific-tenderness (`<uuid>`) | production (`<uuid>`) | Bot-Whatsapp; latest deployment null; repo `Monoga2025/Bot-Whatsapp`. | Ninguno listado. |
| motivated-presence (`<uuid>`) | production (`<uuid>`) | MySQL; latest deployment null; image `mysql:9`. | Ninguno listado. |
| welcoming-light (`<uuid>`) | production (`<uuid>`) | Ninguno listado. | Ninguno listado. |

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
