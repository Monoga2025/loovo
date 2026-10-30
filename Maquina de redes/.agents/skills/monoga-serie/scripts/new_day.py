import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
START = date(2026, 10, 7)
TEMPLATES = ROOT / ".claude" / "skills" / "monoga-serie" / "templates"
FILES = ("brief.md", "guion.md", "caption.md", "resultados.md")


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Uso: new_day.py <N>")
        return 2
    n = int(sys.argv[1])
    if not 1 <= n <= 42:
        print("N debe estar entre 1 y 42.")
        return 2
    day = ROOT / f"Dia-{n:02d}"
    if day.exists():
        print(f"{day.name} ya existe. No se sobrescribe.")
        return 1
    fecha = (START + timedelta(days=n - 1)).isoformat()
    (day / "crudo").mkdir(parents=True)
    (day / "entregables").mkdir()
    for name in FILES:
        text = (TEMPLATES / name).read_text(encoding="utf-8")
        text = text.replace("{{DIA}}", str(n)).replace("{{FECHA}}", fecha)
        (day / name).write_text(text, encoding="utf-8")
    marcador = ROOT / "00_Serie" / "marcador.md"
    lines = marcador.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"| {n} |"):
            cells = line.split("|")
            cells[4] = " creado "
            lines[i] = "|".join(cells)
            break
    marcador.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{day.name} creado ({fecha}). Deja tu video en {day.name}/crudo/.")
    return 0


sys.exit(main())
