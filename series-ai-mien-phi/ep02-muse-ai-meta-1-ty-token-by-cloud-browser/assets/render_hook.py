#!/usr/bin/env python3
"""Render a silent 15-second cinematic hook for Bonus 1.5."""

from pathlib import Path
import math
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageFilter


W, H = 1280, 720
FPS, DURATION = 30, 15
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "hook-15s-ba-cua-dong.mp4"

BG = (4, 7, 16)
WHITE = (242, 247, 255)
MUTED = (126, 139, 164)
RED = (255, 54, 82)
GREEN = (0, 255, 65)
CYAN = (0, 212, 255)
PURPLE = (189, 147, 249)

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_MONO = "/System/Library/Fonts/Menlo.ttc"
headline = ImageFont.truetype(FONT_BOLD, 76)
subhead = ImageFont.truetype(FONT_BOLD, 38)
label = ImageFont.truetype(FONT_BOLD, 29)
small = ImageFont.truetype(FONT_MONO, 18)
tiny = ImageFont.truetype(FONT_REG, 15)


def clamp(v, lo=0, hi=1):
    return max(lo, min(hi, v))


def ease(t):
    t = clamp(t)
    return 1 - (1 - t) ** 4


def smooth(t):
    t = clamp(t)
    return t * t * (3 - 2 * t)


def alpha_at(t, start, length=0.55):
    return ease((t - start) / length)


def center_text(draw, y, text, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    draw.text(((W - (box[2] - box[0])) / 2, y), text, font=font, fill=fill)


def glow_text(base, xy, text, font, color, alpha=255, blur=18):
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.text(xy, text, font=font, fill=(*color, int(alpha * 0.75)))
    base.alpha_composite(glow.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(base).text(xy, text, font=font, fill=(*color, alpha))


def make_background():
    im = Image.new("RGBA", (W, H), (*BG, 255))
    px = im.load()
    for y in range(H):
        for x in range(W):
            dx, dy = (x - W * 0.56) / W, (y - H * 0.42) / H
            r = math.sqrt(dx * dx + dy * dy)
            cyan = max(0, 1 - r / 0.7)
            scan = 2 if y % 4 == 0 else 0
            px[x, y] = (4 + int(3 * cyan), 7 + int(9 * cyan), 16 + int(17 * cyan) + scan, 255)
    return im


BG_IMAGE = make_background()


def background(t):
    im = BG_IMAGE.copy()
    d = ImageDraw.Draw(im)
    for i in range(22):
        x = (i * 173 + int(t * (7 + i % 4))) % (W + 200) - 100
        y = (i * 97 + 80) % H
        a = 18 + i % 4 * 7
        d.text((x, y), ["403", "WAITLIST", "IP BLOCKED", "RUN", "CHROMIUM"][i % 5],
               font=tiny, fill=(0, 212, 255, a))
    return im


def draw_status_card(im, x, y, name, start, t, detail):
    p = alpha_at(t, start)
    if p <= 0:
        return
    slide = int(70 * (1 - p))
    x += slide
    d = ImageDraw.Draw(im)
    box = (x, y, x + 330, y + 105)
    d.rounded_rectangle(box, 15, fill=(13, 17, 31, int(235 * p)), outline=(*RED, int(180 * p)), width=2)
    d.ellipse((x + 22, y + 23, x + 70, y + 71), fill=(*RED, int(235 * p)))
    d.line((x + 35, y + 36, x + 57, y + 58), fill=(255, 255, 255, int(255 * p)), width=5)
    d.line((x + 57, y + 36, x + 35, y + 58), fill=(255, 255, 255, int(255 * p)), width=5)
    d.text((x + 88, y + 18), name, font=label, fill=(*WHITE, int(255 * p)))
    d.text((x + 88, y + 61), detail, font=small, fill=(*MUTED, int(255 * p)))


def render(frame):
    t = frame / FPS
    im = background(t)
    d = ImageDraw.Draw(im)

    # 0–6s: the three familiar routes fail one after another.
    if t < 7.0:
        a = int(255 * alpha_at(t, 0.15))
        center_text(d, 58, "BA CÁNH CỬA. BA LẦN BỊ CHẶN.", subhead, (*WHITE, a))
        draw_status_card(im, 475, 145, "VPN MỸ", 0.5, t, "WAITLIST")
        draw_status_card(im, 475, 270, "CHATGPT", 2.2, t, "ACCESS BLOCKED")
        draw_status_card(im, 475, 395, "GEMINI", 3.9, t, "REGION DENIED")
        if t > 5.4:
            p = alpha_at(t, 5.4)
            center_text(d, 585, "Meta đang đóng từng cửa một.", label, (*RED, int(255 * p)))

    # 7–11s: transition through a narrow scan line.
    if 6.4 <= t < 11.4:
        p = smooth((t - 6.4) / 1.0)
        curtain = int(W * p)
        d.rectangle((0, 0, curtain, H), fill=(2, 5, 11, 255))
        if curtain < W:
            d.rectangle((curtain - 5, 0, curtain + 5, H), fill=(*CYAN, 210))
        if t >= 7.4:
            a = int(255 * alpha_at(t, 7.4))
            center_text(d, 235, "NHƯNG VẪN CÒN", subhead, (*MUTED, a))
            text = "MỘT CỬA ĐANG MỞ"
            box = d.textbbox((0, 0), text, font=headline)
            xy = ((W - box[2] + box[0]) / 2, 300)
            glow_text(im, xy, text, headline, GREEN, a, 22)
            if t > 9.2:
                q = alpha_at(t, 9.2)
                center_text(d, 420, "CLOUD BROWSER  •  MIỄN PHÍ", label, (*CYAN, int(255 * q)))

    # 11–15s: clean CTA slate, deliberately short and direct.
    if t >= 11.0:
        p = smooth((t - 11.0) / 0.7)
        d.rectangle((0, 0, W, H), fill=(3, 6, 13, int(255 * p)))
        a = int(255 * alpha_at(t, 11.4))
        center_text(d, 178, "KHÔNG VPN", subhead, (*WHITE, a))
        center_text(d, 238, "KHÔNG PLUS", subhead, (*WHITE, a))
        center_text(d, 298, "KHÔNG THẺ", subhead, (*WHITE, a))
        text = "LÀM LUÔN."
        box = d.textbbox((0, 0), text, font=headline)
        xy = ((W - (box[2] - box[0])) / 2, 405)
        glow_text(im, xy, text, headline, GREEN, a, 24)
        d.text((W - 235, H - 45), "MUSE AI  •  10/2026", font=small, fill=(*PURPLE, a))

    # Frame, grain-like scan lines and vignette.
    d = ImageDraw.Draw(im)
    d.rectangle((24, 24, W - 24, H - 24), outline=(0, 212, 255, 45), width=1)
    for y in range(0, H, 5):
        d.line((0, y, W, y), fill=(255, 255, 255, 5))
    vignette = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vignette)
    for i in range(170):
        vd.rectangle((i, i, W - i, H - i), outline=max(0, 150 - i))
    black = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    im = Image.composite(black, im, vignette)
    return im.convert("RGB")


def main():
    cmd = [
        "ffmpeg", "-y", "-loglevel", "warning",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
        "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
        "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p",
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
