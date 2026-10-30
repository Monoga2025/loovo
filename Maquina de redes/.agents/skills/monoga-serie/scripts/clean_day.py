import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
TARGETS = ("build", "motion", "motion_all", "motion_mask", "motion_nob", "audio", "input", "seg")


def size(path):
    if path.is_file():
        return path.stat().st_size
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    confirm = "--yes" in sys.argv
    if len(args) != 1 or not args[0].isdigit():
        print("Uso: clean_day.py <N> [--yes]")
        return 2
    day = ROOT / f"Dia-{int(args[0]):02d}"
    resultados = day / "resultados.md"
    if not resultados.exists():
        print(f"No existe {resultados}.")
        return 1
    published = re.search(r"\*\*Publicado:\*\*\s*s[ií]", resultados.read_text(encoding="utf-8"), re.I)
    if not published:
        print("resultados.md no dice 'Publicado: sí'. No se limpia nada.")
        return 1
    if not any((day / "entregables").glob("*")):
        print("entregables/ está vacío. No se limpia nada.")
        return 1
    project = day / "proyecto"
    found = [project / t for t in TARGETS if (project / t).exists()]
    total = sum(size(p) for p in found)
    for p in found:
        print(f"{'BORRAR' if confirm else 'borraría'}: {p.relative_to(ROOT)}  {size(p) / 1e9:.2f} GB")
    print(f"Total: {total / 1e9:.2f} GB")
    if not confirm:
        print("Es una simulación. Agrega --yes para borrar.")
        return 0
    for p in found:
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
    print("Listo.")
    return 0


sys.exit(main())
