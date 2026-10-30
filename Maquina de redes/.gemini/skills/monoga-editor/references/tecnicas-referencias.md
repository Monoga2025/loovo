# Técnicas de las 10 referencias de Pinterest (Día 2, ronda 7)

El usuario pasó un análisis cuadro a cuadro de 10 videos de motion. Claude no vio los videos: esto es la traducción de ese análisis a recetas para HyperFrames en la marca IA MONOGA. **Las referencias usan rojo; nosotros no** (lima = foco, azul = estructura, hueso/carbón = placas).

Catálogo probado: `templates/hyperframes/examples/tecnicas_referencias.html` (T1–T9) y `objeto3d_threejs.html` (T10, 3D real). Es una composición de 22 s con una escena por técnica. Pasa el linter (0 errores) y se revisó con snapshots. Copia la escena que necesites a `graphics.html` y pon palabras literales del usuario.

## Las 4 que más enseñan
| Ref | Qué estudiar |
|---|---|
| #4 Hormozi "hook" | Collage + tipografía cinética: retrato recortado, trazos que se dibujan, una ilustración por idea, revelado por máscara, aberración de canales leve |
| #7 Relato de negocios | Narración larga: **una composición por idea, corte duro entre ellas**, paleta y motivos constantes, movimiento solo en titulares, cifras y conexiones |
| #8 Sony vista explotada | Producto que se separa en capas en profundidad, se sostiene y converge |
| #1 Liquid Death | Profundidad sin 3D real: recortes en capas 2.5D, arco que se dibuja, **cambio de escena oculto tras un objeto que cruza** |

## Gramática que comparten (aplícala siempre)
1. **Una idea = una composición.** Entre ideas, corte duro. Dentro, se mueven texto y recortes; el fondo casi no.
2. **El texto llega después de la imagen** (0,1–0,15 s), nunca antes.
3. **Alternar placas oscuras y claras** en cortes de alto contraste (carbón con retícula azul ↔ hueso con retícula carbón).
4. **Objetos en primer plano desenfocados** = profundidad. Los cercanos llevan `blur(5–8px)`; los lejanos, nítidos.
5. **Un marco fijo puede sostener muchos cambios**: la tarjeta queda quieta y su contenido cambia con cada golpe.
6. **Tipografía:** grotesca pesada para datos y llamadas + serif cursiva para contraste (la nuestra: Space Grotesk 700 + Instrument Serif).

## Recetas (todas en el catálogo)
| # | Técnica | Ref | Cómo |
|---|---|---|---|
| T1 | Arco que se dibuja + titular por fragmentos | 1, 4 | `circle` SVG con `stroke-dasharray` = perímetro (2πr) y `strokeDashoffset` → 0; anillo punteado (`dasharray "2 22"`) que gira lento. Palabras con `y 120 → 0`, escalonadas 0,18 s |
| T2 | **Oclusión** (cambio de escena oculto) | 1, 5 | Billete de 5000 px de ancho (más alto que el cuadro) que cruza con `power1.inOut`; **su centro pasa por el centro del cuadro justo en el corte**. Revisa con snapshots en corte −0,1, corte y +0,1: el cuadro debe quedar 100 % tapado. Con 2300 px no tapaba: se veía la escena nueva |
| T3 | Palabra que crece hasta el borde y corte duro | 3, 7 | `scale 1 → 1.12` lineal y luego `→ 4.2` con `expo.in` en 0,55 s; el corte va al final |
| T4 | Contador 90 → 100 en < 1 s | 7 | **Rueda de números** (tira vertical en una ventana con `overflow:hidden`, `y` con `expo.out`). Solo transform: es determinista al buscar fotogramas. Ventana ≥ 640 px para 3 cifras de 330 px (con 560 px se cortaba el "1") |
| T5 | Marco fijo, contenido que cambia | 5, 6, 9 | Tarjeta redondeada con anillo azul; en cada golpe, destello hueso `opacity .9 → 0` en 0,25 s + cambio de foto + etiqueta lima con `back.out`. **Etiqueta de ancho fijo** (470 px), si no la palabra larga se desborda |
| T6 | Tarjeta pequeña y desenfocada → nítida → renglones → expansión que ocluye | 2, 10 | `scale .32 + blur 16 → 1`, renglones `scaleX 0 → 1` escalonados 0,16 s; para salir, `scale → 3.4` con `expo.in` y el texto delante cambia a carbón |
| T7 | Forma vectorial que barre | 3 | Triángulo lima gigante (2600 px) que sube y tapa la frase; la nueva aparece en carbón sobre lima |
| T8 | Vista explotada 2.5D | 8 | **Dos contenedores:** uno inclina (`rotationX 55`) y otro dentro gira (`rotationZ -40 → -20`), los dos con `preserve-3d` y `perspective` en el escenario. Cada capa `z: k*85` escalonada 0,05 s, se sostiene ~1 s y vuelve con `power3.in`. Con la inclinación y el giro en el mismo elemento, el eje se movía y la pila se corría de lado (corregido) |
| T9 | Revelado por máscara + aberración + subrayado | 4 | `clip-path: inset(100% 0 0 0) → inset(0%)`. Tres copias de la palabra (azul, lima con `mix-blend-mode:screen`, hueso encima) con `x ±14 → 0` en saltos de 0,06 s. Subrayado a mano que se dibuja |

## 3D real con luz (T10): Three.js + modelo CC0 de Poly Haven
Ejemplo probado: `templates/hyperframes/examples/objeto3d_threejs.html`. Un reloj despertador 3D sube y gira; las agujas corren (el tiempo pasa) y se separan de la esfera (vista explotada real). Lleva la palabra "7 MIN" detrás y la frase en cursiva delante. Se verificó en snapshots de HyperFrames.
- **Modelos:** `python scripts/recursos_3d.py 00_Serie/recursos buscar <palabra>` y luego `bajar <id>`. Quedan en `00_Serie/recursos/3d/<id>/`, anotados en el manifiesto. Hay 521 modelos, por ejemplo `alarm_clock_01`, `classic_laptop`, `Camera_01`, `vintage_video_camera`, `Megaphone_01`, `security_camera_01`.
- **Imports:** usa `three@0.184.0/+esm` y `examples/jsm/.../GLTFLoader.js/+esm` de jsdelivr. Con `build/three.module.js`, el cargador falla con "Failed to resolve module specifier three".
- **Redibujar en cada búsqueda:** `tl.seek()` de HyperFrames suprime los `onUpdate`, así que el 3D se quedaba congelado o invisible. La solución es envolver el render de la timeline:
  `const r0 = tl.render.bind(tl); tl.render = (...a) => { const r = r0(...a); render3d(); return r; };`
  La timeline anima un objeto de estado (`sube`, `giro`, `aguja`, `explota`) y `render3d()` lo lee. Nada de `requestAnimationFrame` libre.
- **Metales negros:** sin mapa de entorno, el PBR sale negro. Usa `scene.environment = new PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture` con `environmentIntensity 0.6`.
- **Vidrio negro:** el material `*Glass` del modelo tapaba la esfera. Ponle `transparent`, `opacity 0.12` y `depthWrite false`.
- **Marca:** recolorea las piezas rojas del modelo (el segundero) a lima. Luces: clave blanca cálida, contraluz azul #2F5BFF y relleno lima suave.
- **Escala:** centra el modelo con `Box3` y escálalo a una altura fija (0,21 unidades con la cámara a 1 y fov 28 ≈ 55 % del alto). La separación de la vista explotada va en unidades del modelo y debe ser pequeña (0,012 × k); con 0,045, las agujas salían de la esfera.
- **Canvas transparente** (`alpha: true`, `setClearColor(0, 0)`): así se pone texto detrás del objeto en HTML, igual que el texto detrás de la persona.
- En el primer fotograma el objeto puede no haber cargado aún. Haz que entre animado (sube desde abajo) para que no se note.

## Trampas encontradas al probarlas
- El linter avisa `duplicate_media_discovery_risk` si la misma imagen se repite (billetes). Es un aviso, no un error.
- `strokeDashoffset` sí pasa el linter (no lo marca como movimiento fuera de transform).
- La textura `aura.png` tenía un borde rectangular visible sobre fondo oscuro (el alfa no llegaba a 0). Está corregida en `recursos_proc.py` con una ventana radial y regenerada en la biblioteca.
- Oclusión: el objeto debe ser **más grande que el cuadro en ambos ejes** en el momento del corte, y casi sin rotación (±6°), si no quedan esquinas.

## Dónde conseguir recursos (con licencia)
| Necesidad | Fuente | Licencia y cuidado |
|---|---|---|
| Clips, personas y fondos | Pexels Videos | Uso comercial gratis (licencia Pexels). Sin API key no se descarga por script: pide el enlace al usuario o descárgalo con su permiso |
| Clips verticales y fondos abstractos | Mixkit Video | Solo los de **Video Free License** |
| Modelos, texturas y HDRI 3D | **Poly Haven** | **CC0**. Es la mejor fuente para la vista explotada real con Three.js |
| Modelos 3D | Sketchfab | Revisa **cada modelo**: algunos piden atribución o prohíben uso comercial |
| Tipografía | Fontshare, Google Fonts | Guarda la licencia de la familia. La marca ya fija Space Grotesk + Instrument Serif |
| SFX (whoosh, impacto, barrido) | Mixkit SFX | Revisa la licencia por tipo de recurso; anótalo en `credits.md` |
| Música | Mixkit Music | Tiene usos excluidos; preferimos la música generada por código (`make_epic.py`) |
| Iconos | Lucide (ISC), además de Phosphor (MIT) | En Iconify, el prefijo es `lucide/<nombre>` |
| Aprender | Adobe Learn (After Effects), manual de animación de Blender | Solo para la técnica |

**Pinterest es solo inspiración:** sus videos no tienen licencia para usarse en el video.

## Ejercicio base recomendado
Ref #1 en marca: producto recortado (celular de la biblioteca) sobre retícula, tres titulares cortos, un arco que se dibuja y un objeto grande que cruza delante para ocultar el cambio de escena (T1 + T2). Reúne varias técnicas sin el modelado del video de Sony.
