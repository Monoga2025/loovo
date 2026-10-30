"""Composición local y reproducible. Sin red, generación IA ni cambios en originales.
Ejecutar: python herramientas/componer.py (desde cualquier directorio).
"""
from pathlib import Path
import json, math, colorsys
from PIL import Image, ImageDraw, ImageFont, ImageOps
ROOT=Path(__file__).resolve().parents[1]
FONT=ROOT/'herramientas/fuentes'
BG='#0B0B0F'; BONE='#F4F2EE'; LIME='#C6FF3D'
NAMES=['la_serie','loovo','el_editor','crm_local','sin_humo','modo_demo']
def font(weight,size):
    name={'700':'space-grotesk-latin-700-normal','500':'space-grotesk-latin-500-normal','italic':'instrument-serif-latin-400-italic'}[weight]
    return ImageFont.truetype(str(FONT/(name+'.ttf')),size)
def progress(s):
    with (ROOT/'PROGRESS.md').open('a',encoding='utf-8') as f: f.write('\n- Fase 1b: '+s+'\n')
def colored_bbox(im):
    # Umbral de ilustración azul/lima, no del fondo/grano casi negro.
    mask=Image.new('L',im.size)
    mask.putdata([255 if max(r,g,b)>65 and max(r,g,b)-min(r,g,b)>40 else 0 for r,g,b in im.getdata()])
    return mask.getbbox(),mask

def lines_for(text,f,width):
    lines=[]; current=''
    for word in text.split(' '):
        trial=current+' '+word if current else word
        if f.getlength(trial)>width and current: lines.append(current); current=word
        else: current=trial
    if current: lines.append(current)
    assert ' '.join(lines)==text
    return lines

def draw_block(im,text,y,weight,size,keyword=None):
    f=font(weight,size); d=ImageDraw.Draw(im)
    lines=lines_for(text,f,900)
    rendered=[]; boxes=[]
    for line in lines:
        x=90
        # Splits preserve every source character; only the keyword is lime.
        chunks=[]
        if keyword and keyword in line:
            before,after=line.split(keyword,1); chunks=[(before,BONE),(keyword,LIME),(after,BONE)]
        else: chunks=[(line,BONE)]
        for chunk,color in chunks:
            if chunk:
                box=d.textbbox((x,y),chunk,font=f,anchor='lt'); boxes.append(box)
                d.text((x,y),chunk,font=f,fill=color,anchor='lt')
                x+=f.getlength(chunk)
        rendered.append(line); y+=round(size*1.22)
    return y,{'original':text,'lineas':rendered,'reconstruido':' '.join(rendered),'cajas':boxes,'fuente':weight,'tamano':size}

def compose():
    data=json.loads((ROOT/'borradores/textos.json').read_text(encoding='utf-8'))
    records=[]
    for n,label in enumerate(data['destacadas'],1):
        source=ROOT/f'borradores/destacada_{n:02d}/seleccion.png'; im=Image.open(source).convert('RGB'); original_size=im.size
        # Integra el fondo neutro al carbón de relleno sin bordes rectangulares.
        base=(11,11,15); pixels=[]
        for rgb in im.getdata():
            mix=min(1,(max(rgb)-min(rgb))/35) if max(rgb)<50 else 1
            pixels.append(tuple(round(a*mix+b*(1-mix)) for a,b in zip(rgb,base)))
        im.putdata(pixels)
        bbox,_=colored_bbox(im); assert bbox
        # Reencuadre uniforme para que la ilustración y el título quepan en r=330.
        x0,y0,x1,y1=bbox; scale=min(490/(x1-x0),450/(y1-y0))
        cx=(x0+x1)/2; cy=(y0+y1)/2
        im=im.transform((1080,1920),Image.Transform.AFFINE,(1/scale,0,cx-540/scale,0,1/scale,cy-900/scale),Image.Resampling.BICUBIC,fillcolor=BG)
        _,art_mask=colored_bbox(im)
        max_radius=max(math.hypot(j%1080-540,j//1080-960) for j,v in enumerate(art_mask.getdata()) if v)
        assert max_radius<=330,(n,max_radius)
        d=ImageDraw.Draw(im); f=font('500',38)
        box=d.textbbox((540,1178),label,font=f,anchor='mt')
        assert all((x-540)**2+(y-960)**2<=330**2 for x in (box[0],box[2]) for y in (box[1],box[3]))
        d.text((540,1178),label,font=f,fill=BONE,anchor='mt')
        # Se comprueba el área cromática ANTES de añadir texto hueso.
        art_bbox=(540-(x1-x0)*scale/2,900-(y1-y0)*scale/2,540+(x1-x0)*scale/2,900+(y1-y0)*scale/2)
        path=ROOT/f'destacadas/portadas/destacada_{n:02d}_{NAMES[n-1]}.png'; path.parent.mkdir(parents=True,exist_ok=True); im.save(path)
        records.append({'id':f'destacada_{n:02d}','ruta':path.relative_to(ROOT).as_posix(),'tamano_original':original_size,'tamano':[1080,1920],'texto':[label],'texto_verificado':label==data['destacadas'][n-1],'caja_texto':box,'caja_ilustracion':art_bbox,'radio_maximo_ilustracion_cromatica':max_radius,'tratamiento':'Escala uniforme y traslación; relleno carbón. Ilustración centrada en (540,900); nombre bajo el aro, dentro del círculo solicitado.','limites':'Círculo geométrico r=330 comprobado para el texto y los píxeles de ilustración de saturación/valor significativos (umbral documentado en script; halo tenue no certificado); el recorte real de Instagram y su legibilidad en celular no están verificados.'})
    progress('paso 3a terminado: seis portadas 1080x1920 compuestas; nombres en Space Grotesk 500 hueso, reencuadre uniforme de ilustración para reservar espacio bajo el aro; círculo real de Instagram pendiente.')
    for n,post in enumerate(data['posts'][:3],1):
        im=Image.open(ROOT/f'borradores/post_{n:02d}/seleccion.png').convert('RGB'); original_size=im.size
        im=ImageOps.fit(im,(1080,1350),method=Image.Resampling.LANCZOS,centering=(.5,.5))
        # El foco lima generado pasa a azul EN LA COPIA para no competir con
        # la única palabra clave lima. No se toca seleccion.png.
        out=[]; changed=0
        for r,g,b in im.getdata():
            h,s,v=colorsys.rgb_to_hsv(r/255,g/255,b/255)
            strength=max(0,min(1,(h-.08)/.05,(.52-h)/.07)) if s>.01 else 0
            if strength:
                # Cambio de tono suave: conserva luminosidad y saturación,
                # incluidos halos, sin cortes de máscara ni nuevos focos lima.
                new=colorsys.hsv_to_rgb(h*(1-strength)+.635*strength,s,v)
                out.append(tuple(round(c*255) for c in new)); changed+=1
            else: out.append((r,g,b))
        im.putdata(out)
        title,support,detail=post[2]; key=['42 DÍAS','EDITOR','LOOVO'][n-1]
        size=96
        while font('700',size).getlength(title)>900: size-=1
        y,title_record=draw_block(im,title,110,'700',size,key)
        y,support_record=draw_block(im,support,y+38,'italic',57)
        y,detail_record=draw_block(im,detail,y+30,'500',34)
        assert y<650,'El texto invadiría la ilustración inferior'
        blocks=[title_record,support_record,detail_record]
        assert [b['reconstruido'] for b in blocks]==post[2]
        path=ROOT/f'posts/final/post_{n:02d}.png'; path.parent.mkdir(parents=True,exist_ok=True); im.save(path)
        records.append({'id':f'post_{n:02d}','ruta':path.relative_to(ROOT).as_posix(),'tamano_original':original_size,'tamano':[1080,1350],'texto':post[2],'bloques':blocks,'texto_verificado':True,'clave_lima':key,'pixeles_foco_recoloreados':changed,'tratamiento':'Recorte centrado sin deformación; foco lima del fondo pasado a azul en la copia, única palabra clave lima en titular. Texto en zona superior libre; ilustración inferior intacta en forma.','limites':'Texto cotejado carácter por carácter desde el JSON y cobertura de glifos comprobada; no se usa OCR como prueba independiente ni se ha comprobado en celular.'})
    (ROOT/'borradores/composicion.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    progress('paso 3b terminado: tres posts 1080x1350; textos leídos directamente de textos.json y reconstrucción exacta comprobada por carácter. Foco lima del fondo recoloreado a azul en copias para dejar una sola palabra clave lima.')
    return records

def review(records):
    sheet=Image.new('RGB',(1200,2100),BG); d=ImageDraw.Draw(sheet)
    register=['# Registro de composición · fase 1b','', 'No se generaron imágenes nuevas. Solo se usaron las nueve seleccion.png existentes. Los prompts siguientes son históricos, no se ejecutaron. Archivos finales PNG de composición; la API requiere JPEG según la fuente Meta aportada por el padre.','', '## Fuentes y ortografía', 'Tres TTF locales derivadas de las WOFF2 de marca, sin instalaciones. Las WOFF2 latin no incluían →: se añadió U+2192 como contorno geométrico local en cada TTF derivada. Originales intactos. Tildes, eñe, signos y flecha comprobados en cmap y con máscaras Pillow; prueba_fuentes.png revisada visualmente sin cuadros.','', '## Verificación y límites', 'Cada PNG final se reabrió con Pillow y se cargaron sus píxeles; tamaños exactos comprobados. El texto fuente se compara carácter por carácter (incluyendo tildes, flecha y punto medio) con textos.json. Las líneas partidas se reconstruyen con el espacio original. La inspección visual complementa estas comprobaciones, no es OCR independiente. No se verificaron app, publicación, celular ni límites oficiales restantes.','']
    for j,r in enumerate(records):
        path=ROOT/r['ruta']
        with Image.open(path) as im:
            im.load(); assert im.size==tuple(r['tamano']) and im.format=='PNG'
            thumb=ImageOps.contain(im.convert('RGB'),(370,640),Image.Resampling.LANCZOS)
        x=(j%3)*400; y=(j//3)*700
        sheet.paste(thumb,(x+(400-thumb.width)//2,y+40))
        d.text((x+15,y+10),r['id'],font=font('500',23),fill=BONE)
        prompt=(ROOT/'borradores'/r['id']/'prompt.txt').read_text(encoding='utf-8')
        register += [f"## {r['id']}",f"- Final: `{r['ruta']}` · {r['tamano'][0]}×{r['tamano'][1]} px · PNG reabierto con Pillow.",'- Texto compuesto exacto:','```text','\n'.join(r['texto']),'```','- Ortografía: coincidencia exacta con textos.json, tildes y signos incluidos; glifos cubiertos.', '- Composición: '+r['tratamiento'],'- Sin verificar / alcance: '+r['limites'],'- Prompt histórico usado:','```text',prompt.rstrip(),'```','']
    sheet.save(ROOT/'borradores/hoja.jpg',quality=94)
    (ROOT/'borradores/REGISTRO.md').write_text('\n'.join(register),encoding='utf-8')
    progress('paso 4: nueve PNG reabiertos y cargados con Pillow, tamaños exactos y texto cotejados. Hoja y registro con los nueve prompts históricos generados; pendiente lectura visual final de hoja.jpg.')
    print('9 PNG verificados; hoja.jpg y REGISTRO.md generados')
if __name__=='__main__': review(compose())
