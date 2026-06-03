from pathlib import Path
import math
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont


OUT = Path(__file__).parent / "assets" / "title_handwritten.png"
OUT_ONLY = Path(__file__).parent / "assets" / "title_handwritten_only.png"
FONT = Path("C:/Windows/Fonts/meiryo.ttc")

random.seed(7)

scale = 3
width, height = 900 * scale, 330 * scale
canvas = Image.new("RGBA", (width, height), (255, 255, 255, 0))

font_large = ImageFont.truetype(str(FONT), 74 * scale)
font_small = ImageFont.truetype(str(FONT), 28 * scale)
ink = (63, 56, 48, 245)
soft_ink = (63, 56, 48, 80)
accent = (106, 168, 200, 220)


def draw_hand_line(text, x, y, font, tracking):
    draw = ImageDraw.Draw(canvas)
    cursor = x
    for i, ch in enumerate(text):
        bbox = draw.textbbox((0, 0), ch, font=font)
        char_w = bbox[2] - bbox[0]
        char_h = bbox[3] - bbox[1]
        pad = 28 * scale
        tile = Image.new("RGBA", (char_w + pad * 2, char_h + pad * 2), (255, 255, 255, 0))
        tile_draw = ImageDraw.Draw(tile)

        dx = pad - bbox[0]
        dy = pad - bbox[1]
        tile_draw.text((dx + 2 * scale, dy + 2 * scale), ch, font=font, fill=soft_ink)
        tile_draw.text((dx, dy), ch, font=font, fill=ink)

        angle = math.sin(i * 1.7) * 1.6 + random.uniform(-0.8, 0.8)
        tile = tile.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
        wave = int((math.sin(i * 1.35) * 4 + random.uniform(-2, 2)) * scale)
        canvas.alpha_composite(tile, (int(cursor), int(y + wave)))
        cursor += char_w + tracking + random.uniform(-1.5, 2.5) * scale


draw = ImageDraw.Draw(canvas)
draw.rounded_rectangle(
    [32 * scale, 40 * scale, 40 * scale, 260 * scale],
    radius=4 * scale,
    fill=accent,
)

draw_hand_line("はじめまして", 70 * scale, 54 * scale, font_large, 2 * scale)
draw_hand_line("ろてんちゃんです", 70 * scale, 150 * scale, font_large, 0)

subtitle = "水のふしぎを見つけるお話"
draw.text((76 * scale, 270 * scale), subtitle, font=font_small, fill=(79, 70, 61, 225))

canvas = canvas.filter(ImageFilter.UnsharpMask(radius=0.7 * scale, percent=70, threshold=3))
canvas = canvas.resize((width // scale, height // scale), Image.Resampling.LANCZOS)
OUT.parent.mkdir(parents=True, exist_ok=True)
canvas.save(OUT)

title_only = Image.new("RGBA", (860 * scale, 230 * scale), (255, 255, 255, 0))
canvas = title_only
draw_hand_line("はじめまして", 20 * scale, 18 * scale, font_large, 2 * scale)
draw_hand_line("ろてんちゃんです", 20 * scale, 112 * scale, font_large, 0)
title_only = title_only.filter(ImageFilter.UnsharpMask(radius=0.7 * scale, percent=70, threshold=3))
title_only = title_only.resize((860, 230), Image.Resampling.LANCZOS)
title_only.save(OUT_ONLY)

print(OUT)
print(OUT_ONLY)
