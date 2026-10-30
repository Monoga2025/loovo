import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1920
SAFE = {"top": 270, "bottom": 480, "left": 65, "right": 120}
RED = (227, 18, 11)
WHITE = (255, 255, 255)
IMPACT = r"C:\Windows\Fonts\impact.ttf"
BLACK_FONT = r"C:\Windows\Fonts\ariblk.ttf"


def base(path):
    img = Image.open(path).convert("RGB")
    scale = W / img.width
    img = img.resize((W, round(img.height * scale)), Image.LANCZOS)
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    canvas.paste(img, (0, (H - img.height) // 2))
    return canvas


def gradient(canvas, y0, y1, peak=235):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    px = layer.load()
    for y in range(y0, y1):
        t = (y - y0) / (y1 - y0)
        a = int(peak * min(1.0, t * 2.2) if t < 0.5 else peak)
        for x in range(canvas.width):
            px[x, y] = (0, 0, 0, a)
    return Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB")


def text(draw, xy, s, font, fill, stroke=0, anchor="la"):
    draw.text(xy, s, font=font, fill=fill, stroke_width=stroke, stroke_fill=(0, 0, 0), anchor=anchor)


def glow(canvas, xy, s, font, color, radius=22, anchor="la"):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text(xy, s, font=font, fill=color + (255,), anchor=anchor)
    layer = layer.filter(ImageFilter.GaussianBlur(radius))
    return Image.alpha_composite(canvas.convert("RGBA"), layer).convert("RGB")


def cover_a(src, out):
    c = gradient(base(src), 930, 1500)
    c = glow(c, (W // 2, 1290), "42 DÍAS", ImageFont.truetype(IMPACT, 330), RED, 26, "ms")
    d = ImageDraw.Draw(c)
    text(d, (W // 2, 1085), "TENGO", ImageFont.truetype(IMPACT, 96), WHITE, 4, "ms")
    text(d, (W // 2, 1290), "42 DÍAS", ImageFont.truetype(IMPACT, 330), RED, 6, "ms")
    text(d, (W // 2, 1420), "PARA CAMBIAR LOOVO", ImageFont.truetype(IMPACT, 98), WHITE, 4, "ms")
    f = ImageFont.truetype(BLACK_FONT, 46)
    label = "DÍA 1 DE 42"
    tw = d.textlength(label, font=f)
    x0 = (W - tw) / 2 - 34
    d.rounded_rectangle((x0, 286, x0 + tw + 68, 360), radius=37, fill=RED)
    text(d, (W / 2, 323), label, f, WHITE, 0, "mm")
    c.save(out)


def cover_b(src, out):
    c = gradient(base(src), 930, 1500)
    c = glow(c, (W // 2, 1250), "42 DÍAS", ImageFont.truetype(IMPACT, 330), RED, 26, "ms")
    d = ImageDraw.Draw(c)
    text(d, (W // 2, 1250), "42 DÍAS", ImageFont.truetype(IMPACT, 330), WHITE, 6, "ms")
    text(d, (W // 2, 1365), "VS", ImageFont.truetype(IMPACT, 80), RED, 3, "ms")
    text(d, (W // 2, 1450), "2.000 EMPRESARIOS", ImageFont.truetype(IMPACT, 104), WHITE, 4, "ms")
    c.save(out)


def safe_check(path, out):
    img = Image.open(path).convert("RGBA")
    over = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(over)
    red = (255, 0, 0, 90)
    d.rectangle((0, 0, W, SAFE["top"]), fill=red)
    d.rectangle((0, H - SAFE["bottom"], W, H), fill=red)
    d.rectangle((0, SAFE["top"], SAFE["left"], H - SAFE["bottom"]), fill=red)
    d.rectangle((W - SAFE["right"], SAFE["top"], W, H - SAFE["bottom"]), fill=red)
    d.rectangle((0, 240, W, 1680), outline=(0, 255, 255, 255), width=4)
    Image.alpha_composite(img, over).convert("RGB").save(out)


if __name__ == "__main__":
    cover_a(sys.argv[1], sys.argv[3])
    cover_b(sys.argv[2], sys.argv[4])
    safe_check(sys.argv[3], "check_A.png")
    safe_check(sys.argv[4], "check_B.png")
    print("ok")
