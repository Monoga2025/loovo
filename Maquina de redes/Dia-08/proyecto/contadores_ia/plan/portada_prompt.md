# Portada — monoga-serie (reglas de portada) + paleta monoga-adria
Formato **3:4, 1080×1440** (cuadrícula del perfil de TikTok); exporta también 9:16 si la quieres para Reels.

## Brief para Codex / generador de imagen
```text
Portada vertical 3:4 (1080x1440) para un video corto de TikTok dirigido a contadores colombianos. Estilo editorial minimalista y premium.
Fondo: blanco pastel #F6F4EF liso con puntos grises muy tenues; sin degradados dorados a pantalla completa, sin bordes redondeados.
Foto de referencia adjunta: el usuario mirando a cámara, a pantalla completa, sin recortar su silueta ni cambiar su fondo.
Texto EXACTO (con tildes), máximo 3 elementos:
 1. Titular grande en carbón #2A2926, Montserrat extrabold: "CONTADOR 2030"
 2. Secundario en dorado #A88F57, Playfair Display cursiva: "3 sistemas con IA"
 3. Etiqueta pequeña en caja carbón con texto crema: "D1 · D2 · D3"
Zona segura: el texto nunca tapa cara, ojos ni boca; titular en el tercio superior, etiqueta abajo. El titular debe leerse a 150 px de ancho.
Nada de rojo, verde, azul eléctrico ni neón. Revisa cada imagen con tu herramienta de vista y regenera si hay una letra mal. Genera 2 variantes. No escribas base64 a mano.
```

## Fotograma de referencia
Elige con hoja de contactos uno donde mire a cámara, sin otra persona al fondo y con las manos fuera de la cara. Alternativa con más gancho: fotograma con **dos dedos** levantados (guiño a D2), solo si no tapa la cara.

## Comando
`python .claude/skills/monoga-serie/scripts/portada.py 8 --titular "CONTADOR 2030" --secundario "3 SISTEMAS CON IA" --etiqueta "D1 · D2 · D3" --frame <imagen> --variantes 2`
(Tarda 5–8 min y gasta ~60–90 mil tokens de la suscripción de ChatGPT. Aún no lo ejecuté: falta el crudo.)

## Revisión obligatoria
Letra por letra, cara sin tapar, `ffprobe` = 1080×1440, miniatura a 200 px legible. Copia la elegida a `Dia-08/entregables/Dia8_portada_TikTok_3x4.png`.
