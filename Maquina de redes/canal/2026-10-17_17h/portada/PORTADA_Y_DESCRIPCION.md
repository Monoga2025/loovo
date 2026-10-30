# Portada y descripción · corte2_fullmotion (fuera de la serie "Día X")

## 1. Portada

Cómo generarla: pega el **PROMPT MAESTRO** de `00_Serie/portadas/prompt-maestro.md` en tu generador, adjunta `referencia_dia7.png` y la foto tuya, y reemplaza la sección "DATOS DE ESTA PORTADA" por esto. Claude no genera la imagen fotorrealista.

```
Nivel 1 (etiqueta, sin "DÍA"): LOOVO
Título: PASÉ DE N8N A CLAUDE CODE
Subtítulo: (UN ORQUESTADOR CON SUBAGENTES)
Tema visual: un panel central "orquestador" conectado con hilos dorados a 4 paneles más pequeños (subagentes) que le devuelven una tarjeta de texto; a un lado un flujo n8n lineal (inicia -> termina); fichas pequeñas de "tokens". Sin números adicionales, sin robots.
Pose: reflexivo, mano en el mentón, mirando a cámara.
```

Nota: usa el nivel 1 "LOOVO" y quita cualquier número. Esquinas suaves en los paneles sí valen en portada.

### Foto de referencia
Dejé 3 cuadros en esta carpeta (`foto_ref_1_t134s.png`, `_2_t122s.png`, `_3_t96s.png`): los más nítidos del crudo medidos por contraste.
- Aviso: son de la cámara de 720p, ángulo desde abajo, con movimiento de manos y sin camisa. Sirven para que el generador conserve tu rostro, gafas y cabello (el prompt ya pide ropa oscura), pero la calidad es baja.
- Mejor foto: si tienes una de buena cámara (la del Día 7 u otra frontal nítida), úsala en su lugar.

## 2. Descripción (caption)

```
Pasé de n8n a Claude Code.
Un agente orquestador y varios subagentes.

n8n es un flujo: inicia, termina y no hace loop.
Con Claude Code, el agente principal solo recibe el texto de sus subagentes, sin revisar sus archivos. En mi caso, menos tokens y más rápido.

Lo que no cabía en 42 segundos: sigo usando n8n para los flujos fijos. [CONFIRMAR]

¿Tú ya trabajas con agentes o todavía con flujos?

#IA #ClaudeCode #n8n #Automatizacion #Loovo
```

Revisa antes de publicar:
1. "Menos tokens y más rápido" es lo que dices en el video; no está medido. Por eso va como "en mi caso".
2. La línea de "lo que no cabía" asume que sigues usando n8n para flujos fijos (hoy tienes D1, D2 y D3 importados ahí). Si no es así, bórrala.
3. No lleva `#42DiasLoovo` ni marcador porque está fuera de la serie.
4. "tokens" vs "toques" a los 38,2 s del video: confírmalo antes de publicar.
