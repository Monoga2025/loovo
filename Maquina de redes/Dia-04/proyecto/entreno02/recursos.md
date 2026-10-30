# entreno02 · recursos, licencias y medidas
- Fotos f1–f5 y box.jpg: las mismas de entreno01 (ver `../entreno01/recursos.md`; CC BY 2.0 / CC BY-SA 4.0, atribución obligatoria en el post). La estatua dorada no se usó.
- Fuentes: Playfair Display (OFL, de entreno01), Montserrat 500/600 (@fontsource/montserrat, OFL).
- SFX: `scripts/make_sfx.py` (por código), 15 efectos, solo en el gancho + whoosh del destello + ding en la placa. Sin música.
- Audio: `audio/mezcla_cand1.wav` (100 % mic PC + 15 % celular) → `scripts/cut_audio.py` (cortes 0,42–2,60 + 2,80–6,14, fundidos 12 ms).
- Base de video: `scripts/make_base.py` (encuadre 1,12 + zoom 1,00→1,07 easeInOutSine 2,60–5,52 s, Lanczos subpíxel, color G). Registro por cuadro: `motion/assets/base_zoom.json`.
- Color G: curves master 0/0.015 0.25/0.25 0.5/0.535 0.8/0.85 1/0.965 + colorbalance rm .06 gm -.035 bm -.005 rh .015 bh -.02 + eq sat 1.03 contraste 1.02.
## Palabras medidas (envolvente de audio/voz_cut.wav, línea del corte)
Cristiano 0,10 · Ronaldo 0,32–0,82 · piensa 0,90 · que es 1,22 · el número uno 1,32–1,90 · silencio 1,92–2,64 · No, él 2,64 · sabe 2,94–3,25 · que es 3,32 · el número uno 3,46–4,11 · y por eso 4,20–4,50 · es 4,52 · el número uno 4,68–5,21.
