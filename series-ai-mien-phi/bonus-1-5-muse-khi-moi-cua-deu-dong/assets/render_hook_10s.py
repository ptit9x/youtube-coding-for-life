#!/usr/bin/env python3
"""Render a clean, high-legibility 15-second hook at 1920x1080."""

from pathlib import Path
import math
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageFilter


W, H = 1920, 1080
FPS, DURATION = 30, 15
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "hook-15s-ba-cach-khong-duoc-v2.mp4"

NAVY = (5, 9, 20)
PANEL = (15, 22, 39)
WHITE = (248, 250, 255)
MUTED = (166, 177, 199)
RED = (255, 60, 86)
GREEN = (0, 255, 65)
CYAN = (0, 212, 255)

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
font_title = ImageFont.truetype(BOLD, 82)
font_card = ImageFont.truetype(BOLD, 62)
font_status = ImageFont.truetype(BOLD, 34)
font_final = ImageFont.truetype(BOLD, 112)
font_sub = ImageFont.truetype(REGULAR, 36)


def clamp(v):
    return max(0.0, min(1.0, v))


def ease(v):
    v = clamp(v)
    return 1 - (1 - v) ** 4


def fade(t, start, duration=0.4):
    return ease((t - start) / duration)


def text_size(draw, text, font):
    b = draw.textbbox((0, 0), text, font=font)
    return b[2] - b[0], b[3] - b[1]


def centered(draw, text, y, font, fill):
    tw, _ = text_size(draw, text, font)
    draw.text(((W - tw) / 2, y), text, font=font, fill=fill)


def glow_text(im, text, y, font, color, alpha=255):
    d = ImageDraw.Draw(im)
    tw, _ = text_size(d, text, font)
    x = (W - tw) / 2
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text((x, y), text, font=font, fill=(*color, int(alpha * 0.8)))
    im.alpha_composite(layer.filter(ImageFilter.GaussianBlur(24)))
    ImageDraw.Draw(im).text((x, y), text, font=font, fill=(*color, alpha))


def background():
    im = Image.new("RGBA", (W, H), (*NAVY, 255))
    d = ImageDraw.Draw(im)
    # Subtle cyan/purple light pools; no scan lines or background text.
    lights = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(lights)
    ld.ellipse((-250, -250, 750, 750), fill=(0, 212, 255, 30))
    ld.ellipse((1250, 400, 2250, 1400), fill=(125, 70, 255, 26))
    im.alpha_composite(lights.filter(ImageFilter.GaussianBlur(120)))
    d.rounded_rectangle((48, 48, W - 48, H - 48), 24, outline=(0, 212, 255, 38), width=2)
    return im


BG = background()


def draw_cross(draw, cx, cy, alpha):
    r = 31
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(*RED, alpha))
    draw.line((cx-12, cy-12, cx+12, cy+12), fill=(*WHITE, alpha), width=8)
    draw.line((cx+12, cy-12, cx-12, cy+12), fill=(*WHITE, alpha), width=8)


def draw_card(im, x, y, title, start, t):
    p = fade(t, start, 0.38)
    if p <= 0:
        return
    alpha = int(255 * p)
    y += int(45 * (1 - p))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((x, y, x + 500, y + 230), 26,
                        fill=(*PANEL, int(245 * p)), outline=(*RED, int(210 * p)), width=4)
    draw_cross(d, x + 65, y + 70, alpha)
    d.text((x + 115, y + 39), title, font=font_card, fill=(*WHITE, alpha))
    d.line((x + 40, y + 130, x + 460, y + 130), fill=(255, 255, 255, int(28 * p)), width=2)
    d.text((x + 40, y + 160), "KHÔNG VÀO ĐƯỢC", font=font_status, fill=(*RED, alpha))


def render(frame):
    t = frame / FPS
    im = BG.copy()
    d = ImageDraw.Draw(im)

    # First 9.5 seconds: introduce each failed route slowly enough for mobile.
    if t < 9.7:
        a = int(255 * fade(t, 0.05, 0.35))
        centered(d, "BA CÁCH ĐỀU KHÔNG ĐƯỢC", 128, font_title, (*WHITE, a))
        centered(d, "Muse vẫn đưa tài khoản vào waitlist", 235, font_sub, (*MUTED, a))
        draw_card(im, 150, 385, "VPN MỸ", 0.65, t)
        draw_card(im, 710, 385, "CHATGPT", 2.45, t)
        draw_card(im, 1270, 385, "GEMINI", 4.25, t)
        if t >= 6.2:
            q = fade(t, 6.2, 0.5)
            d = ImageDraw.Draw(im)
            centered(d, "WAITLIST", 750, font_title, (*RED, int(255 * q)))

    # Wipe to a clean Lexmount reveal.
    if 9.1 <= t < 10.3:
        p = ease((t - 9.1) / 1.0)
        edge = int(W * p)
        d.rectangle((0, 0, edge, H), fill=(3, 8, 16, 255))
        if edge < W:
            d.rectangle((edge - 8, 0, edge + 8, H), fill=(*CYAN, 235))

    if t >= 10.0:
        p = fade(t, 10.0, 0.55)
        d.rectangle((0, 0, W, H), fill=(3, 8, 16, int(255 * p)))
        a = int(255 * p)
        centered(d, "NHƯNG CÒN MỘT CỬA", 230, font_title, (*WHITE, a))
        glow_text(im, "LEXMOUNT", 395, font_final, GREEN, a)
        centered(ImageDraw.Draw(im), "CLOUD BROWSER  •  MIỄN PHÍ", 565, font_status, (*CYAN, a))
        centered(ImageDraw.Draw(im), "LÀM LUÔN.", 730, font_title, (*WHITE, a))

    return im.convert("RGB")


def main():
    cmd = [
        "ffmpeg", "-y", "-loglevel", "warning",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
        "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
        "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p",
        "-movflags", "+faststart", str(OUT),
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    assert proc.stdin is not None
    for frame in range(FPS * DURATION):
        proc.stdin.write(render(frame).tobytes())
        if frame % FPS == 0:
            print(f"Rendering {frame // FPS:02d}/{DURATION}s")
    proc.stdin.close()
    if proc.wait() != 0:
        raise SystemExit("ffmpeg encode failed")
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
