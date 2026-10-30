"""Torneo de ideas: 4 equipos generan, se critican entre sí y un juez decide.
Cada equipo es un proceso de pi (modelo Codex) sin herramientas ni escritura.
Uso: python -I run_torneo.py
"""
import concurrent.futures as cf
import pathlib
import shutil
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent  # 00_Serie
PI = shutil.which("pi")
MODEL = "openai-codex/gpt-6.1-sol"

CONTEXT = [
    HERE / "brief.md",
    ROOT / "hechos.md",
    ROOT / "estado.md",
    ROOT / "aprendizajes.md",
    ROOT / "banco-frases.md",
    ROOT / "voz-y-estilo.md",
    ROOT / "guiones" / "investigacion" / "tiktok_nicho_apify_2026-10-09.md",
]

TEAMS = {
    "A_bitacora": (
        "Equipo BITÁCORA (build in public).",
        "Tu lente: documentar el trabajo mientras se hace, con el menor costo extra posible. Formatos que salen "
        "solos de una sesión de trabajo grabada con OBS (cámara y pantalla). Piensa en el flujo: trabajar, marcar, cortar.",
    ),
    "B_evento": (
        "Equipo EVENTO Y VENTAS B2B.",
        "Tu lente: que los 39 días terminen en conversaciones y clientes en el Luque Business Summit. Qué servicios "
        "llevar (a partir de lo que ya existe o es realista construir), cómo se prueban, cómo se muestran en 3 minutos y "
        "cómo el contenido va calentando a los empresarios antes del evento. Incluye cómo tocar el tema de precios sin inventarlos.",
    ),
    "C_retencion": (
        "Equipo ALGORITMO Y RETENCIÓN.",
        "Tu lente: los datos del scraper. Qué formatos, duraciones y ganchos rinden por encima del tamaño de la cuenta "
        "para un público de empresarios hispanos, y cómo adaptarlos a trabajo real sin caer en listas genéricas ni en el cliché.",
    ),
    "D_marca": (
        "Equipo MARCA PERSONAL Y DIFERENCIACIÓN.",
        "Tu lente: que el usuario sea reconocible y creíble. Qué lo hace distinto del resto de agencias de IA en TikTok, "
        "cómo usar la Nómina Viva, sus errores y su historia (dueño, estudiante, Colombia) sin fingir ni exagerar.",
    ),
}


def pi_run(name: str, prompt: str, out: pathlib.Path, thinking: str = "high") -> str:
    prompt_file = out.with_suffix(".prompt.md")
    prompt_file.write_text(prompt, encoding="utf-8")
    cmd = [PI, "-p", "--no-session", "--no-extensions", "--no-skills", "--no-context-files",
           "--no-tools", "--model", MODEL, "--thinking", thinking]
    cmd += [f"@{p}" for p in CONTEXT if p.exists()]
    cmd += [f"@{prompt_file}", "Cumple exactamente las instrucciones del último archivo adjunto (el .prompt.md)."]
    t0 = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=1500, cwd=str(HERE))
    text = r.stdout.strip()
    if r.returncode != 0 or not text:
        text = f"[ERROR {name}] código {r.returncode}\n{r.stderr[-800:]}"
    out.write_text(text + "\n", encoding="utf-8")
    print(f"{name}: {len(text)} caracteres en {time.time() - t0:.0f}s", flush=True)
    return text


def round1(key: str) -> str:
    title, lens = TEAMS[key]
    prompt = f"""# Ronda 1 · {title}
{lens}

Eres un equipo de {title.split('.')[0].lower()} que compite contra otros tres equipos. Gana el que aporte las ideas que
más acerquen al usuario a llegar al evento con servicios listos y una marca personal creíble, sin trabajo de contenido aparte.

Entrega EXACTAMENTE 8 ideas, numeradas {key[0]}1 a {key[0]}8. Cada idea con estos campos:
- **Nombre** (corto)
- **Trabajo real que ya hay que hacer** (qué estaría haciendo el usuario de todas formas)
- **Qué se documenta y cómo** (formato, duración, dónde se publica) y **minutos extra que cuesta**
- **Gancho ejemplo** (máx. 15 palabras, solo con hechos ✅ o marcado como 🟡/⏳)
- **Por qué funcionaría** (cita el dato del scraper, un hecho o el brief; si es opinión, dilo)
- **Riesgo o dato que falta** (`[DATO]` y quién lo tiene)

Después, una sección **Mi mejor apuesta** con la idea que más recomendarías y por qué las otras 7 son peores.
Escribe en español de Colombia, sin relleno. No escribas guiones completos."""
    return pi_run(f"R1-{key}", prompt, HERE / f"r1_{key}.md")


def round2(key: str, r1: dict) -> str:
    title, _ = TEAMS[key]
    others = "\n\n".join(f"## Propuesta del equipo {k}\n{v}" for k, v in r1.items() if k != key)
    mine = r1[key]
    prompt = f"""# Ronda 2 · {title} · A PELEAR
Estas son las propuestas de los otros tres equipos y la tuya. Ahora eres crítico y defensor.

{others}

## Tu propuesta de la ronda 1
{mine}

Entrega, en español de Colombia y sin relleno:
1. **Ataque.** Para cada uno de los otros tres equipos, elige sus 2 ideas más débiles y mátalas con una razón concreta
   (no cumple la misión, cuesta tiempo extra, inventa datos, suena a cliché, riesgo de moderación, depende de un dato que no existe, etc.).
   Sé duro pero honesto: si una idea ajena es mejor que la tuya, dilo.
2. **Defensa.** Qué ataques te harían a tus ideas y cuáles son ciertos. Mata tú mismo tus 3 ideas más flojas.
3. **Robo legítimo.** Hasta 3 ideas de otros equipos que mejorarías y harías tuyas, con la mejora.
4. **Tu lista final de 5 ideas** (nombre, trabajo real, qué se documenta, minutos extra, gancho de ejemplo de máx. 15 palabras).
Marca con `[DATO]` lo que no se pueda saber."""
    return pi_run(f"R2-{key}", prompt, HERE / f"r2_{key}.md")


def judge(r2: dict) -> str:
    body = "\n\n".join(f"## Ronda 2 del equipo {k}\n{v}" for k, v in r2.items())
    prompt = f"""# Juez
Eres el juez del torneo. Cuatro equipos propusieron, se atacaron y defendieron. Aquí está todo:

{body}

Criterios, con peso (cada idea de 0 a 5 en cada uno):
1. Sirve para construir y vender los servicios del evento (peso 3).
2. Sale del trabajo real, con casi cero tiempo extra de documentación (peso 3).
3. Solo afirma hechos ✅ o los marca 🟡/⏳ y no inventa cifras ni precios (peso 2).
4. Suena a la voz del usuario y lo diferencia del cliché (peso 2).
5. Tiene evidencia (datos del scraper o hechos) y no solo opinión (peso 1).

Entrega en español de Colombia, sin relleno:
1. **Tabla de las 10 mejores ideas** con nombre, equipo de origen, nota ponderada y una línea de por qué.
2. **Las 5 que se hacen YA** (esta semana), con: qué trabajo hay detrás, cómo se documenta (pasos), minutos extra, gancho de ejemplo.
3. **Lo que se descarta y por qué** (máximo 8 líneas).
4. **Decisiones que solo el usuario puede tomar** (catálogo de servicios, precios, si dice que estudia, etc.), una por línea.
5. **Un plan semanal de 7 días** (una línea por día) que combine trabajo en servicios y qué se documenta.
6. **Los 5 ataques que más pesaron** y quién los hizo.
Si hay empate o dudas, di cuál es y por qué."""
    return pi_run("JUEZ", prompt, HERE / "juez_final.md", thinking="xhigh")


def main() -> int:
    if not PI:
        print("No encuentro pi", file=sys.stderr)
        return 1
    keys = list(TEAMS)
    def reuse_or(fn, f, *a):
        path = HERE / f
        if path.exists() and not path.read_text(encoding="utf-8").startswith("[ERROR"):
            return path.read_text(encoding="utf-8")
        return fn(*a)
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        r1 = dict(zip(keys, ex.map(lambda k: reuse_or(round1, f"r1_{k}.md", k), keys)))
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        r2 = dict(zip(keys, ex.map(lambda k: reuse_or(round2, f"r2_{k}.md", k, r1), keys)))
    malos = [k for k, v in r2.items() if v.startswith("[ERROR")]
    if malos:
        print("ABORTO: fallaron las rondas 2 de", malos, "- no se llama al juez", flush=True)
        return 2
    judge(r2)
    print("LISTO", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
