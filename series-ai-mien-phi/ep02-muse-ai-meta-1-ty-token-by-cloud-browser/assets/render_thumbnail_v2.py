#!/usr/bin/env python3
"""Typeset the Bonus 1.5 thumbnail over the generated Muse-series artwork."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "thumbnail-02-muse-key-clean.png"
OUTPUT = HERE / "thumbnail-02-muse-key-with-text.jpg"
W, H = 1280, 720

FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
RED = (255, 68, 78)
GREEN = (58, 255, 82)
WHITE = (255, 255, 255)
CYAN = (0, 212, 255)


def fit_font(text, max_width, start, floor=40):
    probe = Image.new("RGB", (10, 10))
    draw = ImageDraw.Draw(probe)
    for size in range(start, floor - 1, -2):
        font = ImageFont.truetype(FONT, size)
        box = draw.textbbox((0, 0), text, font=font, stroke_width=0)
        if box[2] - box[0] <= max_width:
            return font
    return ImageFont.truetype(FONT, floor)


def add_text(canvas, text, xy, font, color, glow_color=None, stroke=8):
    glow_color = glow_color or color
    glow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.text(xy, text, font=font, fill=(*glow_color, 220), stroke_width=stroke,
            stroke_fill=(0, 0, 0, 255))
    canvas.alpha_composite(glow.filter(ImageFilter.GaussianBlur(12)))
    ImageDraw.Draw(canvas).text(xy, text, font=font, fill=(*color, 255),
                                stroke_width=stroke, stroke_fill=(0, 0, 0, 255))


source = Image.open(SOURCE).convert("RGB")
canvas = source.resize((W, H), Image.Resampling.LANCZOS).convert("RGBA")

# Darken only the text zone while keeping the generated artwork intact.
shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shade)
for x in range(0, 660):
    alpha = int(118 * (1 - x / 660))
    sd.line((x, 0, x, H), fill=(0, 0, 0, alpha))
canvas = Image.alpha_composite(canvas, shade)

max_w = 585
font_top = fit_font("VPN CHẾT?", max_w, 104)
font_mid = fit_font("CỬA CUỐI", max_w, 112)
font_big = fit_font("VẪN MỞ", max_w, 138)

add_text(canvas, "VPN CHẾT?", (48, 70), font_top, RED)
add_text(canvas, "CỬA CUỐI", (48, 210), font_mid, WHITE, CYAN)
add_text(canvas, "VẪN MỞ", (48, 350), font_big, GREEN)

# Small deterministic badge—the image model is never asked to draw text.
draw = ImageDraw.Draw(canvas)
badge = (50, 565, 620, 650)
draw.rounded_rectangle(badge, radius=15, fill=(8, 16, 30, 235),
                       outline=(*CYAN, 255), width=4)
badge_text = "CLOUD BROWSER MIỄN PHÍ"
badge_font = fit_font(badge_text, 510, 40, floor=26)
badge_box = draw.textbbox((0, 0), badge_text, font=badge_font, stroke_width=3)
badge_w = badge_box[2] - badge_box[0]
badge_h = badge_box[3] - badge_box[1]
badge_x = badge[0] + (badge[2] - badge[0] - badge_w) / 2
badge_y = badge[1] + (badge[3] - badge[1] - badge_h) / 2 - badge_box[1]
draw.text((badge_x, badge_y), badge_text, font=badge_font,
          fill=(*CYAN, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))

canvas.convert("RGB").save(OUTPUT, quality=96, subsampling=0, optimize=True)
print(OUTPUT)
