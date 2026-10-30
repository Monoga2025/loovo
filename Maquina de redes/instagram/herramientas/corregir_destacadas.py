"""Corrección SOLO de destacadas, sin red ni generación. No ejecuta componer.py.
Diámetro visible = 2 * radio máximo respecto al centro (540,960), píxeles
cuya diferencia máxima de canal respecto al carbón supera 30/255.
Incluye objetos neutros, no solo color. Halos inferiores al umbral no certificados.
"""
from pathlib import Path
import hashlib
import json
import math
from PIL import Image, ImageChops, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BG = (11, 11, 15)
NAMES = ['la_serie', 'loovo', 'el_editor', 'crm_local', 'sin_humo', 'modo_demo']
OUT = ROOT / 'destacadas/portadas'
ARCHIVE = ROOT / 'borradores/portadas_con_rotulo'


def progress(message):
    with (ROOT / 'PROGRESS.md').open('a', encoding='utf-8') as f:
        f.write('\n- Corrección destacadas: ' + message + '\n')


def mask(im):
    channels = ImageChops.difference(im, Image.new('RGB', im.size, BG)).split()
    return ImageChops.lighter(ImageChops.lighter(channels[0], channels[1]), channels[2]).point(lambda v: 255 if v > 30 else 0)


def radius(m, cx, cy):
    w = m.width
    return max(math.hypot(i % w - cx, i // w - cy) for i, v in enumerate(m.getdata()) if v)


def compose():
    OUT.mkdir(exist_ok=True, parents=True)
    ARCHIVE.mkdir(exist_ok=True, parents=True)
    # Fail closed: do not overwrite any archived original on a repeat invocation.
    paths = [OUT / f'destacada_{n:02d}_{name}.png' for n, name in enumerate(NAMES, 1)]
    assert all(p.exists() and not (ARCHIVE / p.name).exists() for p in paths)
    results = []
    prepared = []
    for n, path in enumerate(paths, 1):
        with Image.open(ROOT / f'borradores/destacada_{n:02d}/seleccion.png') as source:
            im = source.convert('RGB')
        # Same neutral-background integration as componer.py; no object clipping.
        pixels = []
        for rgb in im.getdata():
            mix = min(1, (max(rgb) - min(rgb)) / 35) if max(rgb) < 50 else 1
            pixels.append(tuple(round(a * mix + b * (1 - mix)) for a, b in zip(rgb, BG)))
        im.putdata(pixels)
        m = mask(im)
        x0, y0, x1, y1 = m.getbbox()
        cx, cy = (x0 + x1 - 1) / 2, (y0 + y1 - 1) / 2
        scale = 270 / radius(m, cx, cy)
        # Uniform affine: all source pixels retained in the large canvas.
        for _ in range(3):
            final = im.transform((1080, 1920), Image.Transform.AFFINE,
                (1 / scale, 0, cx - 540 / scale, 0, 1 / scale, cy - 960 / scale),
                Image.Resampling.BICUBIC, fillcolor=BG)
            measured = radius(mask(final), 540, 960)
            if abs(measured - 270) < 0.6:
                break
            scale *= 270 / measured
        assert 520 <= 2 * measured <= 560
        assert measured < 330
        assert all(0 <= 540 + (x - cx) * scale < 1080 and 0 <= 960 + (y - cy) * scale < 1920
                   for x in (0, im.width - 1) for y in (0, im.height - 1)), 'Source would be cropped'
        temp = OUT / (path.stem + '.temporal.png')
        final.save(temp)
        with Image.open(temp) as check:
            check.load()
            assert check.size == (1080, 1920) and check.format == 'PNG'
            actual_mask = mask(check.convert('RGB'))
            actual_radius = radius(actual_mask, 540, 960)
            assert actual_radius < 330
        results.append({'archivo': path.name, 'tamano': [1080, 1920],
            'diametro_visible_px': round(2 * actual_radius, 2),
            'bbox_visible': actual_mask.getbbox(), 'radio_maximo_px': round(actual_radius, 2),
            'margen_circulo_px': round(330 - actual_radius, 2), 'escala_uniforme': scale,
            'sha256_anterior': hashlib.sha256(path.read_bytes()).hexdigest()})
        prepared.append((path, temp))
    # Every new file validated before moving the first previous version.
    for path, temp in prepared:
        path.rename(ARCHIVE / path.name)
        temp.rename(path)
    progress('paso 2: seis portadas sin rótulos regeneradas; anteriores movidas intactas a borradores/portadas_con_rotulo/. Pillow confirma 1080×1920, escala uniforme, fuentes completas sin recorte y radio visible <330 px. Falta revisar previsualización.')
    report = {'criterio': __doc__, 'centro': [540, 960], 'circulo_diametro_px': 660,
              'advertencia': '660 px es una decisión propia, NO un recorte real de Instagram verificado.',
              'portadas': results}
    (ROOT / 'borradores/medidas_destacadas_sin_rotulo.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    preview = Image.new('RGB', (560, 6 * 150 + 100), BG)
    d = ImageDraw.Draw(preview)
    font = ImageFont.truetype(str(ROOT / 'herramientas/fuentes/space-grotesk-latin-500-normal.ttf'), 16)
    d.text((15, 10), 'Simulación propia: círculo 660 px; no verificado en Instagram', fill='#F4F2EE', font=font)
    d.text((260, 44), '110 px', fill='#F4F2EE', font=font)
    d.text((430, 44), '64 px', fill='#F4F2EE', font=font)
    circle = Image.new('L', (660, 660))
    ImageDraw.Draw(circle).ellipse((0, 0, 659, 659), fill=255)
    for j, row in enumerate(results):
        y = 85 + j * 150
        d.text((15, y + 44), f'{j+1:02d} {NAMES[j].replace("_", " ")}', fill='#F4F2EE', font=font)
        with Image.open(OUT / row['archivo']) as im:
            crop = im.convert('RGB').crop((210, 630, 870, 1290))
            for size, x in [(110, 260), (64, 430)]:
                thumb = crop.resize((size, size), Image.Resampling.LANCZOS)
                alpha = circle.resize((size, size), Image.Resampling.LANCZOS)
                preview.paste(thumb, (x, y + (110 - size) // 2), alpha)
    preview.save(OUT / 'previsualizacion_circulo.png')
    lines = ['## Corrección vigente · destacadas sin rótulo', '',
        'Esta sección sustituye SOLO la composición histórica de las seis destacadas descrita abajo. Posts y captions intactos; hoja.jpg queda como referencia histórica anterior.',
        'Motivo: el rótulo era ilegible en miniatura y redundante con el nombre mostrado por la interfaz; figuras demasiado pequeñas.',
        'Se reutilizaron las seis seleccion.png. Sin Codex ni publicación. Anteriores conservadas intactas en borradores/portadas_con_rotulo/.',
        'Variante reproducible: herramientas/corregir_destacadas.py (se detiene si ya existen archivos archivados).',
        'Centro (540,960); escala uniforme sin deformación ni recorte de la fuente. Fondo carbón #0B0B0F.',
        'Medición Pillow: diámetro del círculo centrado que contiene todos los píxeles con diferencia máxima de canal >30/255 respecto al carbón, incluyendo objetos neutros. Halos más tenues no certificados.',
        'Las seis imágenes se reabrieron y cargaron: 1080×1920 PNG; ninguna ilustración medida toca el círculo de radio 330.', '',
        '| Archivo | Diámetro visible px | Margen hasta r=330 px |', '|---|---:|---:|']
    lines += [f"| {r['archivo']} | {r['diametro_visible_px']} | {r['margen_circulo_px']} |" for r in results]
    lines += ['', 'Previsualización: destacadas/portadas/previsualizacion_circulo.png; recorte central circular 660 px reducido a 110 y 64 px lado a lado.',
        '**Sin verificar:** recorte real de Instagram, apariencia en celular y halos bajo el umbral. Los 660 px son decisión propia, no una especificación oficial.',
        'Detalle de tamaños, cajas y hashes de las anteriores: borradores/medidas_destacadas_sin_rotulo.json.', '']
    register = ROOT / 'borradores/REGISTRO.md'
    register.write_text('\n'.join(lines) + '\n' + register.read_text(encoding='utf-8'), encoding='utf-8')
    progress('paso 3: previsualización circular a 110 y 64 px y mediciones JSON guardadas; REGISTRO.md actualizado sin alterar registros históricos de posts. Pendiente lectura visual final. Círculo de 660 px propio, no verificado en Instagram.')
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    compose()
