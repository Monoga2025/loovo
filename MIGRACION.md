# Migración de Loovo a la arquitectura Pi + ODD

Propuesta construida en `C:\Users\you\Desktop\Loovo-pi` (copia aislada del 2026-10-20). El original `C:\Users\you\Desktop\Loovo` no se tocó. La adopción copia solo archivos de configuración e instrucciones: ningún video, base de datos ni dato de cliente.

## 1. Qué cambió y por qué

| Cambio | Por qué |
|---|---|
| `AGENTS.md` pasa a ser la fuente única de reglas (raíz y un archivo por módulo) | Pi lee `AGENTS.md` primero y, si existe, ignora `CLAUDE.md` en esa carpeta (`resource-loader.js`, orden `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md`). Con dos archivos de reglas, uno siempre queda desactualizado. |
| Cada `CLAUDE.md` queda como puntero de una línea (`@AGENTS.md`, y `@MEMORY.md` en la raíz y en el CRM) | Claude Code sigue cargando las mismas reglas por import; Pi no expande `@` imports y lee `AGENTS.md` directamente. |
| `Maquina de redes/AGENTS.md` se reescribió desde el índice `CLAUDE.md` | El `AGENTS.md` anterior estaba desactualizado y es el que Pi carga hoy en el original. Su regla 1 ("nunca un texto completo") contradice el formato UGC de `guiones/CLAUDE.md`. |
| Se agregó la sección ODD a la raíz: inline por defecto y delegación solo por razón nombrada | Es el método de Gentle AI (gentle-pi 4.0.0, `docs/readme-reference.md`): mapeo, escritores paralelos, backstop de ~150k tokens y verificador independiente para riesgo alto. Se añade una quinta razón propia de Loovo: guiones y motion con el modelo más capaz. |
| Los `worker-*` de Claude Code tienen equivalentes en `.pi/agents/loovo-*.md` | gentle-pi descubre agentes de proyecto en `<cwd>/.pi/agents/*.md` (`lib/agents-config.ts`) y los lanza con `subagent_run`. El frontmatter admite `name`, `description`, `model`, `thinking`, `tools` y `mode`. |
| `loovo-verify` es nuevo | ODD exige un verificador independiente para cambios de riesgo alto (`state.json`, `omni.db`, webhooks, envíos, despliegues) y no existía ninguno con las reglas de Loovo. |
| Hay comandos nuevos en `.pi/prompts/`: `/retomar`, `/cerrar` y `/scout-n8n` | Son prompt templates de Pi: fijan el protocolo de arranque y cierre (handoff + Engram) sin depender de que el modelo se acuerde. |
| Se agregó `.pi/settings.json` con rutas de skills | Desde la raíz, Pi no ve `Maquina de redes/.agents/skills` (solo busca hacia arriba) ni `~/.codex/skills` (las skills de ventas). |
| Se agregó `.engram/config.json` con `project_name: "loovo"` | Fuera de un repositorio git, Engram usa el nombre de la carpeta. Además, las reglas obligan a pasar `project: "loovo"` explícito. |
| `.claude/agents/worker-*.md` ahora dicen "lee `AGENTS.md`" | Si leen el `CLAUDE.md` con la herramienta Read solo ven `@AGENTS.md`, porque Read no expande imports. |
| Retoques en `MEMORY.md`, `README.md`, `SHARED_STATE.md` (encabezado) y `HANDOFF.md` (pendiente de Gentle AI) | Ahora apuntan a `AGENTS.md`. El tablero ya no queda atado a un runtime (Gemini o Claude). |

Las reglas de negocio quedan intactas y centralizadas en la raíz: envíos siempre manuales, nada 🟢 sin una prueba de punta a punta por el canal real, ningún marcador hacia clientes, datos de clientes nunca en `servicios/`, guiones con el modelo más capaz y entregables de video en `entregables/`.

## 2. Archivo original → archivo nuevo

| Original | Nuevo | Acción |
|---|---|---|
| `CLAUDE.md` | `AGENTS.md` + `CLAUDE.md` (puntero) | reglas movidas y ampliadas con ODD |
| `MEMORY.md`, `README.md`, `SHARED_STATE.md`, `HANDOFF.md` | los mismos | retoque mínimo |
| `ventas/CLAUDE.md` | `ventas/AGENTS.md` + puntero | movido |
| `Maquina de redes/CLAUDE.md` + `Maquina de redes/AGENTS.md` (desactualizado) | `Maquina de redes/AGENTS.md` + puntero | fusionados, manda el índice |
| `Maquina de redes/guiones/CLAUDE.md` | `Maquina de redes/guiones/AGENTS.md` + puntero | movido ("Opus" → "modelo más capaz") |
| `Maquina de redes/edicion/CLAUDE.md` | `Maquina de redes/edicion/AGENTS.md` + puntero | movido |
| `landings/CLAUDE.md` | `landings/AGENTS.md` + puntero | movido |
| — | `servicios/AGENTS.md` + puntero | nuevo |
| `servicios/omni-sales-crm/CLAUDE.md` | `servicios/omni-sales-crm/AGENTS.md` + puntero (`@AGENTS.md`, `@MEMORY.md`) | movido |
| `clientes-activos/README.md` (sin reglas) | `clientes-activos/AGENTS.md` + puntero | nuevo |
| `.claude/agents/github-n8n-scout.md` | `.pi/agents/loovo-scout.md` (+ `/scout-n8n`) | equivalente Pi |
| `.claude/agents/worker-guiones.md` | `.pi/agents/loovo-guiones.md` | equivalente Pi |
| `.claude/agents/worker-edicion.md` | `.pi/agents/loovo-edicion.md` | equivalente Pi |
| `.claude/agents/worker-ventas.md` | `.pi/agents/loovo-ventas.md` | equivalente Pi |
| `.claude/agents/worker-sistemas.md` | `.pi/agents/loovo-sistemas.md` | equivalente Pi |
| — | `.pi/agents/loovo-verify.md`, `.pi/prompts/{retomar,cerrar,scout-n8n}.md`, `.pi/settings.json`, `.engram/config.json` | nuevo |
| `.claude/agents/worker-*.md` | los mismos | `CLAUDE.md` → `AGENTS.md` |

### Agentes Pi y cuándo se usan

| Agente | Modelo sugerido | Razón ODD para delegar |
|---|---|---|
| `loovo-scout` | `openai-codex/gpt-5.6-luna` · low | Mapeo: búsqueda en GitHub por encima del presupuesto inline |
| `loovo-guiones` | `openai-codex/gpt-6.1-sol` · high | Regla de modelo de Loovo, o unidad paralela |
| `loovo-edicion` | `openai-codex/gpt-6.1-sol` · high | Regla de modelo, render largo (backstop de contexto) o unidad paralela |
| `loovo-ventas` | `openai-codex/gpt-6-luna` · medium | Solo unidades paralelas o backstop; lo pequeño va inline |
| `loovo-sistemas` | `openai-codex/gpt-6-luna` · medium | Solo unidades paralelas o backstop |
| `loovo-verify` | `openai-codex/gpt-6.1-sol` · high (solo lectura) | Verificador independiente de riesgo alto |

Para el mapeo genérico se reutilizan los agentes globales de gentle-pi (`gentle-ai-explore`, `gentle-ai-worker`, `gentle-ai-verify`).

## 3. Qué se descartó

- **Skills de dominio por worker** (`loovo-ventas` como skill): duplicarían el `AGENTS.md` de cada módulo. Las reglas viven en `AGENTS.md` y las skills existentes (`monoga-*` y las de ventas) siguen siendo el conocimiento procedimental.
- **`.pi/APPEND_SYSTEM.md` o `.pi/SYSTEM.md`:** el contexto por carpeta ya cubre las reglas, y `SYSTEM.md` reemplazaría el prompt de gentle-pi.
- **`.pi/mcp.json` para Engram:** Engram entra por el paquete `gentle-engram` (herramientas nativas `mem_*` sobre HTTP), no por MCP. Su README advierte no duplicarlo.
- **Fijar el modelo del orquestador en `.pi/settings.json`:** el modelo queda en la configuración global. gentle-pi tampoco lo hace por repositorio.
- **Borrar los espejos `.claude/skills` y `.gemini/skills` de Maquina de redes:** se declaran espejos y `.agents/skills` queda como copia canónica, pero no se borra nada.
- **Datos en la copia:** se quitaron de `Loovo-pi` `ventas/whatsapp-mcp/whatsapp-bridge/store/{whatsapp.db,messages.db}` (sesión de WhatsApp y mensajes), la carpeta de medios del grupo y `servicios/omni-sales-crm/data/{crm.db,omni.db}`. También se excluyeron `.env*`, claves y archivos pesados. Nada de esto se copia de vuelta.

## 4. Qué no se pudo confirmar de Pi

1. Si gentle-pi exige confianza del proyecto (`/trust`) para cargar `.pi/agents/`. `discoverAgents` no la revisa en el código leído. Pi sí la exige para `.pi/settings.json` y `.pi/prompts/`.
2. Si la ruta relativa `../Maquina de redes/.agents/skills` (con espacio) y los `~/.codex/skills/<nombre>` de `.pi/settings.json` cargan sin advertencias. La documentación dice que las rutas de proyecto se resuelven desde `.pi/` y que aceptan `~`.
3. Si Engram respeta `.engram/config.json` fuera de un repositorio git. Su README dice "inside the current git repo", por eso la regla también pasa `project: "loovo"` explícito.
4. Si `openai-codex/gpt-6.1-sol` es de verdad el "modelo más capaz" disponible. Es el que el usuario ya asigna a jueces y verificadores. La alternativa es `openrouter/anthropic/claude-opus-latest` (pago por token). Pi no tiene sesión de Anthropic directa: `pi --list-models claude` solo muestra OpenRouter.
5. Si los nombres de herramientas de `loovo-verify` (`powershell`, `ls`) son válidos para gentle-agents. Son herramientas built-in de Pi, pero no se probó un lanzamiento real.
6. El comportamiento de `subagent_run` en modo background: requiere activar `/gentle:background-subagents enable` y no funciona en `pi -p`.
7. La revisión nativa de Gentle AI (RDD) solo aplica en repositorios git. La raíz de Loovo no es repo; `servicios/omni-sales-crm` sí lo es.
8. No se lanzó Pi sobre `Loovo-pi`: la carga se verificó leyendo el código y la documentación, no con una sesión real.

## 5. Adopción en el original (reversible)

Requisitos: cerrar las sesiones de Pi y Claude Code abiertas en `Loovo`. No hace falta detener el servidor del CRM, porque solo se copian `AGENTS.md` y `CLAUDE.md`. Ejecutar en PowerShell 7.

### 5.1 Respaldo y copia

```powershell
$src = 'C:\Users\you\Desktop\Loovo-pi'
$dst = 'C:\Users\you\Desktop\Loovo'
$bak = "C:\Users\you\Desktop\Loovo-respaldo-config-$(Get-Date -Format yyyyMMdd-HHmm)"
$files = @(
  'AGENTS.md','CLAUDE.md','MEMORY.md','README.md','SHARED_STATE.md','HANDOFF.md','MIGRACION.md',
  '.engram\config.json','.pi\settings.json',
  '.pi\agents\loovo-scout.md','.pi\agents\loovo-guiones.md','.pi\agents\loovo-edicion.md',
  '.pi\agents\loovo-ventas.md','.pi\agents\loovo-sistemas.md','.pi\agents\loovo-verify.md',
  '.pi\prompts\retomar.md','.pi\prompts\cerrar.md','.pi\prompts\scout-n8n.md',
  '.claude\agents\worker-ventas.md','.claude\agents\worker-guiones.md',
  '.claude\agents\worker-edicion.md','.claude\agents\worker-sistemas.md',
  'ventas\AGENTS.md','ventas\CLAUDE.md',
  'Maquina de redes\AGENTS.md','Maquina de redes\CLAUDE.md',
  'Maquina de redes\guiones\AGENTS.md','Maquina de redes\guiones\CLAUDE.md',
  'Maquina de redes\edicion\AGENTS.md','Maquina de redes\edicion\CLAUDE.md',
  'landings\AGENTS.md','landings\CLAUDE.md',
  'servicios\AGENTS.md','servicios\CLAUDE.md',
  'servicios\omni-sales-crm\AGENTS.md','servicios\omni-sales-crm\CLAUDE.md',
  'clientes-activos\AGENTS.md','clientes-activos\CLAUDE.md'
)
# Huella (SHA-256, 16 primeros) de cada archivo del original en el momento de la copia
$expected = @{
  'CLAUDE.md'='CDE131BC0B3768FC'; 'MEMORY.md'='3FE88F2F4CD0A846'; 'README.md'='865C29EF0B6D8299'
  'SHARED_STATE.md'='933CD5B63D67979E'; 'HANDOFF.md'='721D8A82FD67B068'; 'ventas\CLAUDE.md'='191D90BF282A434F'
  'Maquina de redes\AGENTS.md'='8C3ADA33EB3F8BD8'; 'Maquina de redes\CLAUDE.md'='6EE01244298A5F74'
  'Maquina de redes\guiones\CLAUDE.md'='41AB0502178A9BA2'; 'Maquina de redes\edicion\CLAUDE.md'='C638CD53CB7547AF'
  'landings\CLAUDE.md'='0AF8919335398F7B'; 'servicios\omni-sales-crm\CLAUDE.md'='DE1A333DD6691F65'
  '.claude\agents\worker-ventas.md'='062672D7CB576024'; '.claude\agents\worker-guiones.md'='5AE7F3AC1CD2370B'
  '.claude\agents\worker-edicion.md'='58717F6A45B13D13'; '.claude\agents\worker-sistemas.md'='2EC567B0E6D1CC98'
}
# 0. Guardia: un archivo vivo que cambió después de la copia NO se pisa
$changed = @(foreach ($k in $expected.Keys) {
  $p = Join-Path $dst $k
  if ((Test-Path -LiteralPath $p) -and (Get-FileHash -LiteralPath $p -Algorithm SHA256).Hash.Substring(0,16) -ne $expected[$k]) { $k }
})
if ($changed.Count) { "OMITIDOS (cambiaron desde la copia; aplicar el retoque a mano): $($changed -join ', ')" }
# 1. Respaldo de lo que existe y lista de lo que será nuevo
New-Item -ItemType Directory -Force $bak | Out-Null
$nuevos = foreach ($f in $files) {
  $p = Join-Path $dst $f
  if (Test-Path -LiteralPath $p) { $t = Join-Path $bak $f; New-Item -ItemType Directory -Force (Split-Path $t) | Out-Null; Copy-Item -LiteralPath $p $t }
  elseif ($changed -notcontains $f) { $f }
}
Set-Content -LiteralPath (Join-Path $bak 'nuevos.txt') -Value $nuevos
# 2. Copia solo de la lista
foreach ($f in $files) {
  if ($changed -contains $f) { continue }
  $t = Join-Path $dst $f
  New-Item -ItemType Directory -Force (Split-Path $t) | Out-Null
  Copy-Item -LiteralPath (Join-Path $src $f) $t -Force
}
"Respaldo en: $bak"
```

Después de copiar:
1. Abre Pi en `C:\Users\you\Desktop\Loovo` y acepta la confianza del proyecto (o usa `/trust`).
2. Ejecuta `/reload`, luego `subagent_list_agents` (deben aparecer los seis `loovo-*`) y `/retomar`.
3. En `servicios/omni-sales-crm` (repo git) quedan `AGENTS.md` nuevo y `CLAUDE.md` modificado sin commit. El commit es decisión del usuario, por ejemplo `docs: move agent rules to AGENTS.md`.

### 5.2 Reversión

```powershell
$dst = 'C:\Users\you\Desktop\Loovo'
$bak = 'C:\Users\you\Desktop\Loovo-respaldo-config-AAAAMMDD-HHMM'   # la ruta que imprimió 5.1
Get-Content -LiteralPath (Join-Path $bak 'nuevos.txt') | Where-Object { $_ } | ForEach-Object {
  Remove-Item -LiteralPath (Join-Path $dst $_) -Confirm:$false -ErrorAction SilentlyContinue }
robocopy $bak $dst /E /XF nuevos.txt /NFL /NDL /NJH /NP
foreach ($d in '.pi\agents','.pi\prompts','.pi','.engram') {
  $p = Join-Path $dst $d
  if ((Test-Path -LiteralPath $p) -and -not (Get-ChildItem -LiteralPath $p -Force)) { Remove-Item -LiteralPath $p -Confirm:$false } }
```

`robocopy` devuelve códigos 0 a 7 cuando termina bien. La reversión solo toca los archivos de la lista: no borra videos, bases de datos ni carpetas de clientes.
