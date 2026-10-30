from pathlib import Path
import sys, json, hashlib, shutil
from PIL import Image, ImageDraw, ImageFont
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'herramientas'))
import corregir_destacadas as c
DEST=Path(__file__).resolve().parent
OUT=ROOT/'destacadas/portadas'
path=OUT/'destacada_05_sin_humo.png'
archive=ROOT/'borradores/portadas_con_rotulo/destacada_05_filigrana.png'
assert (DEST/'estado.txt').read_text().strip()=='0'
others={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob('destacada_*.png') if p!=path}
previous=hashlib.sha256(path.read_bytes()).hexdigest()
if archive.exists(): assert hashlib.sha256(archive.read_bytes()).hexdigest()==previous
else: shutil.copy2(path,archive)
with Image.open(DEST/'seleccion.png') as source: im=source.convert('RGB')
original_size=im.size
pixels=[]
for rgb in im.getdata():
    mix=min(1,(max(rgb)-min(rgb))/35) if max(rgb)<50 else 1
    pixels.append(tuple(round(a*mix+b*(1-mix)) for a,b in zip(rgb,c.BG)))
im.putdata(pixels)
m=c.mask(im); x0,y0,x1,y1=m.getbbox()
cx,cy=(x0+x1-1)/2,(y0+y1-1)/2
scale=270/c.radius(m,cx,cy)
for _ in range(4):
    final=im.transform((1080,1920),Image.Transform.AFFINE,(1/scale,0,cx-540/scale,0,1/scale,cy-960/scale),Image.Resampling.BICUBIC,fillcolor=c.BG)
    measured=c.radius(c.mask(final),540,960)
    if abs(measured-270)<.6: break
    scale*=270/measured
assert 520<=2*measured<=560
final.save(path)
with Image.open(path) as check:
    check.load()
    assert check.size==(1080,1920) and check.format=='PNG'
    actual=c.mask(check.convert('RGB'))
    diameter=2*c.radius(actual,540,960)
    bbox=actual.getbbox()
    assert 520<=diameter<=560
report={'archivo':str(path.relative_to(ROOT)),'tamano':[1080,1920],'tamano_fuente':original_size,'centro':[540,960],'diametro_visible_px':round(diameter,2),'bbox_visible':bbox,'criterio':'2 × radio máximo de píxeles con diferencia máxima de canal >30/255 contra carbón; incluye volumen y sombras visibles. Halos menores no certificados.','sha256_anterior':previous,'sha256_archivo_filigrana':hashlib.sha256(archive.read_bytes()).hexdigest(),'sha256_otras_portadas':others}
(DEST/'medidas.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
c.progress('Sin humo 05b paso 2: nueva portada sin rótulo 1080×1920 centrada (540,960), diámetro '+str(round(diameter,2))+' px; filigrana anterior copiada intacta a borradores/portadas_con_rotulo/destacada_05_filigrana.png.')
preview=Image.new('RGB',(560,1000),c.BG)
d=ImageDraw.Draw(preview)
font=ImageFont.truetype(str(ROOT/'herramientas/fuentes/space-grotesk-latin-500-normal.ttf'),16)
d.text((15,10),'Simulación propia: círculo 660 px; no verificado en Instagram',fill='#F4F2EE',font=font)
d.text((260,44),'110 px',fill='#F4F2EE',font=font)
d.text((430,44),'64 px',fill='#F4F2EE',font=font)
circle=Image.new('L',(660,660))
ImageDraw.Draw(circle).ellipse((0,0,659,659),fill=255)
for j,name in enumerate(c.NAMES):
    y=85+j*150
    d.text((15,y+44),f'{j+1:02d} {name.replace("_"," ")}',fill='#F4F2EE',font=font)
    with Image.open(OUT/f'destacada_{j+1:02d}_{name}.png') as source:
        crop=source.convert('RGB').crop((210,630,870,1290))
        for size,x in [(110,260),(64,430)]:
            thumb=crop.resize((size,size),Image.Resampling.LANCZOS)
            alpha=circle.resize((size,size),Image.Resampling.LANCZOS)
            preview.paste(thumb,(x,y+(110-size)//2),alpha)
preview.save(OUT/'previsualizacion_circulo.png')
assert all(hashlib.sha256((OUT/name).read_bytes()).hexdigest()==digest for name,digest in others.items())
assert hashlib.sha256(archive.read_bytes()).hexdigest()==previous
with (ROOT/'borradores/REGISTRO.md').open('a',encoding='utf-8') as f:
    f.write('\n## Sustitución exclusiva Sin humo · 05b\n- Una imagen nueva vía herramientas/puente_codex.py, método original codex exec; ejecución en segundo plano, sin alternativa. Prompt e invocación: destacada_05b/prompt.txt e invocacion.json; logs en esa carpeta.\n- Brief: reglas, no IA; bloques azules 3D sólidos y gruesos (mínimo solicitado 6% del diámetro), UN punto lima, carbón liso, sin texto/números/personas/filigrana. Figura solicitada ~60% del alto en fuente.\n- Final: destacadas/portadas/destacada_05_sin_humo.png; 1080×1920, sin rótulo, centro (540,960), diámetro medido '+str(round(diameter,2))+' px. Afinidad uniforme y armonización neutra de componer.py; medición completa de corregir_destacadas.py.\n- Filigrana anterior intacta: borradores/portadas_con_rotulo/destacada_05_filigrana.png (hash coincide). Otras cinco portadas intactas por SHA-256.\n- Previsualización de seis portadas regenerada a 110 y 64 px. Medidas, umbral y hashes: destacada_05b/medidas.json. Pendiente lectura visual.\n- Sin verificar: recorte real de Instagram, celular, halos bajo umbral y grosor mínimo exacto en proyección 3D. Sin posts, captions ni publicación.\n')
c.progress('Sin humo 05b paso 3: seis miniaturas regeneradas a 110 y 64 px; otras cinco portadas y filigrana intactas por SHA-256; REGISTRO.md actualizado. Pendiente lectura visual.')
print(json.dumps(report,ensure_ascii=False))
