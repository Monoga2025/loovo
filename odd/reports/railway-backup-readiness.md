# Railway T2 — readiness previa (solo lectura)

## Comprobaciones observadas
- Docker CLI 29.7.2 instalado; daemon **no disponible** (Docker Desktop Linux engine named pipe ausente). Por ello, no se pudo consultar inventario local de imágenes: presencia de postgres/mysql/redis **no verificada**, no asumir caché.
- GPG 2.4.9 y OpenSSL 3.5.7 funcionan; `openssl rand` completó. GPG no reveló fingerprints públicos (`pub:`); no hay destinatario GPG público detectable en el keyring consultado. Ningún dato privado fue consultado/expuesto.
- Disco C: libre 34,166,368 KiB (~32.6 GiB), 94% usado. Atributos del directorio de usuario dicen `Directory`; ACL específica del destino **no verificada** (la consulta ACL falló por quoting de PowerShell). No afirmar que el destino tenga acceso exclusivo.
- `railway volume files download --help`: acepta remoto y destino local opcional; explícitamente permite rutas/descargas de directorio (concurrencia configurable); no ofrece argumento de stream/pipe. La ayuda no prueba consistencia de copia en vivo.

## Método por clase / bloqueos concretos
- Código de repos: preservar checkout local existente si se identifica; el inventario T1 solo da referencias y no acredita copias locales ni autoriza clonar. Próximo paso: cotejar repositorios locales contra las referencias T1.
- PostgreSQL/MySQL: dump lógico consistente con cliente nativo y credenciales solo en entorno de proceso; aún no listo: clientes no comprobados, daemon Docker apagado y destino protegido/cifrado no establecido. Si imágenes de dump ya están cacheadas, pueden habilitar tooling luego, pero su existencia no se verificó; no arrancar contenedores todavía.
- Redis: exportar snapshot mediante mecanismo consistente/RDB-AOF identificado; no hay estado/política comprobada. No tratar como dump SQL.
- Volúmenes (incluye Evolution, n8n, sesiones): CLI permite descargar archivo/directorio, pero copia de archivos de DB viva no es consistente; n8n config y sesiones Evolution pueden contener secretos. No descargar hasta método de consistencia y almacenamiento protegido aprobados.
- Cifrado: OpenSSL puede generar aleatoriedad, pero no se encontró clave pública GPG. Hace falta paso humano seguro para establecer/proveer recipient público o una contraseña robusta fuera de chat/archivo; después verificar que el destino local tenga ACL restrictiva.

## Siguiente paso mínimo
Activar Docker Desktop y repetir solo `docker info` + inventario local de imágenes; en paralelo, que el usuario establezca una clave pública de cifrado o contraseña por canal seguro y un directorio local con ACL privada verificable. Luego decidir método consistente para volúmenes vivos antes de cualquier descarga. No se descargaron datos, volúmenes, variables, credenciales ni contenidos de DB; no se hicieron pulls, instalaciones, SSH, exec remoto ni mutaciones.
