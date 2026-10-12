#!/usr/bin/env python3
"""
Render BONUS 1.5 thumbnail — "Mọi cửa đều đóng, cửa cuối vẫn mở"
1376×768 (same as EP01/EP02 thumbnails), same series visual DNA:
BG #06060F · neon green #00FF41 · red #E8192C · cyan #00D4FF · scan-lines ·
vignette · code particles · Arial Bold (Vietnamese-safe) + Menlo.

Outputs:
  thumbnail-01-ba-cua-dong.jpg  (text-free base)
  thumbnail-01-with-text.jpg    (final, stacked neon text left)

Text (Part 5 — Option 1, khuyên dùng):
  VPN CHẾT?        #FF4444 red
  CỬA CUỐI MỞ      #00FF41 green
  MIỄN PHÍ — 10/2026  cyan badge #00D4FF on #1a1a2e
"""

import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

# ─── CONFIG ───
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1376, 768

BG_DARK = (6, 6, 15)
NEON_GREEN = (0, 255, 65)
RED = (232, 25, 44)
RED_TEXT = (255, 68, 68)
WHITE = (255, 255, 255)
CYAN = (0, 212, 255)
BADGE_BG = (26, 26, 46)
PANEL = (13, 20, 32)

ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
MENLO = "/System/Library/Fonts/Menlo.ttc"

OUT_BASE = os.path.join(HERE, "thumbnail-01-ba-cua-dong.jpg")
OUT_FINAL = os.path.join(HERE, "thumbnail-01-with-text.jpg")
MUSE_LOGO = os.path.join(
    HERE, "..", "..", "ep02-trai-nghiem-muse-app", "assets", "muse-logo.png"
)

# ─── HELPERS ───


def fit_font(path, text, max_w, start, floor=56):
    """Largest font size whose rendered width <= max_w."""
    size = start
    while size > floor:
        f = ImageFont.truetype(path, size)
        bb = ImageDraw.Draw(Image.new("RGB", (10, 10))).textbbox((0, 0), text, font=f)
        if bb[2] - bb[0] <= max_w:
            return f
        size -= 2
    return ImageFont.truetype(path, floor)


def glow_layer(draw_fn, blur, alpha=255):
    """Draw on transparent layer, blur it → returns RGBA glow layer."""
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(layer))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    if alpha < 255:
        a = layer.getchannel("A").point(lambda v: v * alpha // 255)
        layer.putalpha(a)
    return layer


def composite(canvas, *layers):
    out = canvas
    for l in layers:
        out = Image.alpha_composite(out, l)
    return out


def radial_mask(size, cx, cy, radius, power=1.0):
    """L-mode mask: 255 inside radius → 0 outside, smooth falloff."""
    mw, mh = size
    mask = Image.new("L", size, 0)
    px = mask.load()
    for y in range(mh):
        dy = (y - cy) / radius
        for x in range(mw):
            dx = (x - cx) / radius
            d = math.sqrt(dx * dx + dy * dy)
            if d < 1.0:
                px[x, y] = int(255 * (1.0 - d) ** power)
    return mask


# ─── 1. BACKGROUND ───
print("bg...")
canvas = Image.new("RGBA", (W, H), (*BG_DARK, 255))

# soft blue-ish glow center-right (subject area)
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([W * 0.52, H * 0.18, W * 1.02, H * 0.86], fill=(10, 40, 70, 160))
glow = glow.filter(ImageFilter.GaussianBlur(120))
canvas = composite(canvas, glow)

# faint green wash from the open door (right)
glow2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow2)
gd.ellipse([W * 0.66, H * 0.25, W * 1.05, H * 0.80], fill=(0, 90, 40, 110))
glow2 = glow2.filter(ImageFilter.GaussianBlur(90))
canvas = composite(canvas, glow2)

# ─── 2. CODE PARTICLES ───
print("particles...")
random.seed(7)
snippets = [
    "npx lexmount run", "browser.cd(() => muse.ai)", "cloudBrowser.start()",
    "await page.goto(url)", "session.new({clean: true})", "PIN = mail.await()",
    "const agent = chromium.launch()", "ip !== blacklist", "dob === gmail.dob",
    "invite.redeem('16NESL')", "for (door of doors) try(door)", "while (!open) next()",
    "region === 'US'", "verify.card === null", "token += 1e9",
]
particles = Image.new("RGBA", (W, H), (0, 0, 0, 0))
pd = ImageDraw.Draw(particles)
for i, snip in enumerate(snippets):
    f = ImageFont.truetype(MENLO, random.choice([15, 16, 18]))
    x = random.randint(470, W - 380)
    y = random.randint(30, H - 90)
    if 560 < x < 1330 and 100 < y < 680:  # keep door zone clean
        x = random.randint(470, 560)
    col = random.choice([(0, 255, 65), (0, 212, 255), (120, 130, 150)])
    pd.text((x, y), snip, font=f, fill=(*col, random.randint(38, 70)))
# a few dim neon dots
for _ in range(26):
    pd.point(
        (random.randint(440, W - 40), random.randint(20, H - 40)),
        fill=(*random.choice([(0, 255, 65), (0, 212, 255)]), random.randint(50, 110)),
    )
canvas = composite(canvas, particles)

# ─── 3. THREE DEAD DOORS (VPN / CHATGPT / SPARK) ───
print("dead doors...")
TILE_X, TILE_W, TILE_H = 575, 285, 168
rows = [(108, "VPN"), (303, "CHATGPT"), (498, "SPARK")]

dead_glow = glow_layer(
    lambda d: [
        d.rounded_rectangle([TILE_X, y, TILE_X + TILE_W, y + TILE_H], radius=14,
                            outline=(*RED, 220), width=6)
        or d.line([TILE_X + 62, y + 34, TILE_X + TILE_W - 62, y + TILE_H - 34],
                  fill=(*RED, 190), width=14)
        or d.line([TILE_X + TILE_W - 62, y + 34, TILE_X + 62, y + TILE_H - 34],
                  fill=(*RED, 190), width=14)
        for y, _ in rows
    ],
    blur=12,
)
dead = Image.new("RGBA", (W, H), (0, 0, 0, 0))
dd = ImageDraw.Draw(dead)
for y, label in rows:
    dd.rounded_rectangle([TILE_X, y, TILE_X + TILE_W, y + TILE_H], radius=14,
                         fill=(*PANEL, 235))
    dd.rounded_rectangle([TILE_X, y, TILE_X + TILE_W, y + TILE_H], radius=14,
                         outline=(*RED, 255), width=4)
    # big X
    dd.line([TILE_X + 62, y + 30, TILE_X + TILE_W - 62, y + TILE_H - 30],
            fill=(*RED_TEXT, 255), width=16)
    dd.line([TILE_X + TILE_W - 62, y + 30, TILE_X + 62, y + TILE_H - 30],
            fill=(*RED_TEXT, 255), width=16)
    # label chip bottom-left
    lf = ImageFont.truetype(MENLO, 30)
    bb = dd.textbbox((0, 0), label, font=lf)
    tw = bb[2] - bb[0]
    dd.rectangle([TILE_X + 14, y + TILE_H - 52, TILE_X + 26 + tw, y + TILE_H - 14],
                 fill=(30, 10, 12, 235))
    dd.text((TILE_X + 20, y + TILE_H - 48), label, font=lf, fill=(*RED_TEXT, 255))
canvas = composite(canvas, dead_glow, dead)

# ─── 4. CHEVRON ARROW → ───
print("arrow...")
cx, cy = 905, 384


def draw_chevrons(d, alpha):
    for i in range(3):
        x0 = 872 + i * 30
        a = int(alpha * (0.55 + 0.225 * i))
        col = (*NEON_GREEN, a)
        d.line([(x0, cy - 34), (x0 + 26, cy), (x0, cy + 34)], fill=col,
               width=12, joint="curve")


canvas = composite(
    canvas,
    glow_layer(lambda d: draw_chevrons(d, 200), blur=10, alpha=255),
)
chev = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_chevrons(ImageDraw.Draw(chev), 255)
canvas = composite(canvas, chev)

# ─── 5. THE LAST OPEN DOOR (LEXMOUNT) ───
print("open door...")
DX0, DY0, DX1, DY1 = 985, 138, 1330, 648


def door_outline(d, width, alpha):
    d.rounded_rectangle([DX0, DY0, DX1, DY1], radius=10,
                        outline=(*NEON_GREEN, alpha), width=width)


# light bursting out of the open door (drawn under the frame)
burst = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(burst)
bd.rounded_rectangle([DX0 + 14, DY0 + 14, DX1 - 14, DY1 - 14], radius=8,
                     fill=(0, 120, 55, 190))
burst = burst.filter(ImageFilter.GaussianBlur(46))
core = Image.new("RGBA", (W, H), (0, 0, 0, 0))
cd = ImageDraw.Draw(core)
cd.rounded_rectangle([DX0 + 60, DY0 + 55, DX1 - 60, DY1 - 55], radius=8,
                     fill=(120, 255, 170, 235))
core = core.filter(ImageFilter.GaussianBlur(52))
canvas = composite(canvas, burst, core)

# floor light spill
spill = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(spill)
sd.polygon([(DX0, DY1), (DX1, DY1), (DX1 + 30, H), (DX0 - 120, H)],
           fill=(0, 200, 90, 60))
spill = spill.filter(ImageFilter.GaussianBlur(30))
canvas = composite(canvas, spill)

# glowing frame
canvas = composite(
    canvas,
    glow_layer(lambda d: door_outline(d, 10, 230), blur=14),
)
frame = Image.new("RGBA", (W, H), (0, 0, 0, 0))
door_outline(ImageDraw.Draw(frame), 8, 255)
canvas = composite(canvas, frame)

# Muse logo floating inside the door
print("logo...")
logo = Image.open(MUSE_LOGO).convert("RGBA")
LS = 195
logo = logo.resize((LS, LS), Image.LANCZOS)
lx, ly = DX0 + (DX1 - DX0) // 2, DY0 + 92
logo_glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sil = Image.new("RGBA", (LS, LS), (0, 0, 0, 0))
sil.paste(logo, (0, 0))
green_sil = Image.new("RGBA", (LS, LS), (*NEON_GREEN, 0))
green_sil.paste(Image.new("RGBA", (LS, LS), (*NEON_GREEN, 200)), (0, 0),
                mask=logo.getchannel("A"))
logo_glow.paste(green_sil, (lx - LS // 2, ly - LS // 2))
logo_glow = logo_glow.filter(ImageFilter.GaussianBlur(22))
canvas = composite(canvas, logo_glow)
lg = Image.new("RGBA", (W, H), (0, 0, 0, 0))
lg.paste(logo, (lx - LS // 2, ly - LS // 2), mask=logo)
canvas = composite(canvas, lg)

# LEXMOUNT label under the door
lab = "LEXMOUNT"
lf = ImageFont.truetype(MENLO, 36)
bb = ImageDraw.Draw(canvas).textbbox((0, 0), lab, font=lf)
lw = bb[2] - bb[0]
lx0 = DX0 + (DX1 - DX0) // 2 - lw // 2
canvas = composite(
    canvas,
    glow_layer(lambda d: d.text((lx0, 668), lab, font=lf, fill=(*NEON_GREEN, 210)),
               blur=8),
)
labl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(labl).text((lx0, 668), lab, font=lf, fill=(*NEON_GREEN, 255))
canvas = composite(canvas, labl)

# ─── 6. SCAN-LINES + VIGNETTE (baked into base, under text) ───
print("overlays...")
scan = Image.new("RGBA", (W, H), (0, 0, 0, 0))
scd = ImageDraw.Draw(scan)
for sy in range(0, H, 4):
    scd.line([(0, sy), (W, sy)], fill=(255, 255, 255, 6), width=1)
canvas = composite(canvas, scan)

vmask = radial_mask((W // 4, H // 4), W // 8 * 0.95, H // 8, W // 4 * 0.78, 0.8)
vmask = vmask.resize((W, H)).filter(ImageFilter.GaussianBlur(40))
black = Image.new("RGBA", (W, H), (0, 0, 5, 255))
# mask 255 at center → keep canvas; 0 at edges → darken
canvas = Image.composite(canvas, black, vmask)

# ─── SAVE TEXT-FREE BASE ───
base = canvas.convert("RGB")
base.save(OUT_BASE, quality=92)
print("saved", OUT_BASE)

# ─── 7. STACKED NEON TEXT (left column, on top of everything) ───
print("text...")


def draw_stacked(d, stroke):
    d.text((42, 64), "VPN CHẾT?",
           font=f1, fill=(*RED_TEXT, 255), stroke_width=stroke,
           stroke_fill=(0, 0, 0))
    d.text((42, 200), "CỬA CUỐI",
           font=f2, fill=(*NEON_GREEN, 255), stroke_width=stroke,
           stroke_fill=(0, 0, 0))
    d.text((42, 362), "VẪN MỞ",
           font=f3, fill=(*NEON_GREEN, 255), stroke_width=stroke,
           stroke_fill=(0, 0, 0))


f1 = fit_font(ARIAL_BOLD, "VPN CHẾT?", 520, 124)
f2 = fit_font(ARIAL_BOLD, "CỬA CUỐI", 520, 158)
f3 = fit_font(ARIAL_BOLD, "VẪN MỞ", 520, 158)

glowtxt = glow_layer(lambda d: draw_stacked(d, 0), blur=13, alpha=175)
crisptxt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_stacked(ImageDraw.Draw(crisptxt), 10)
canvas = composite(canvas, glowtxt, crisptxt)

# badge — MIỄN PHÍ — 10/2026
badge_f = ImageFont.truetype(ARIAL_BOLD, 46)
badge_t = "MIỄN PHÍ — 10/2026"
bb = ImageDraw.Draw(canvas).textbbox((0, 0), badge_t, font=badge_f)
bw, bh = bb[2] - bb[0], bb[3] - bb[1]
bx, by = 42, 596


def draw_badge(d):
    d.rounded_rectangle([bx, by, bx + bw + 52, by + bh + 44], radius=12,
                        fill=(*BADGE_BG, 245), outline=(*CYAN, 255), width=3)
    d.text((bx + 26, by + 22), badge_t, font=badge_f, fill=(*CYAN, 255))


canvas = composite(canvas, glow_layer(draw_badge, blur=9, alpha=150))
badge = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_badge(ImageDraw.Draw(badge))
canvas = composite(canvas, badge)

final = canvas.convert("RGB")
final.save(OUT_FINAL, quality=92)
print("saved", OUT_FINAL)
