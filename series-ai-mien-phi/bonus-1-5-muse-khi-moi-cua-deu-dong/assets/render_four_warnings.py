#!/usr/bin/env python3
"""Render a silent 28-second motion graphic for the four warnings section."""

from pathlib import Path
import math
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageFilter


W, H = 1920, 1080
FPS, DURATION = 30, 28
ROOT = Path(__file__).resolve().parent
OUT = ROOT / "bon-dieu-can-biet-28s.mp4"

BG = (4, 8, 18)
PANEL = (14, 22, 38)
WHITE = (248, 250, 255)
MUTED = (154, 169, 194)
GREEN = (0, 255, 65)
CYAN = (0, 212, 255)
RED = (255, 62, 86)
AMBER = (255, 184, 62)
PURPLE = (189, 147, 249)

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
MONO = "/System/Library/Fonts/Menlo.ttc"
f_kicker = ImageFont.truetype(MONO, 28)
f_number = ImageFont.truetype(BOLD, 92)
f_title = ImageFont.truetype(BOLD, 74)
f_body = ImageFont.truetype(REGULAR, 42)
f_small = ImageFont.truetype(BOLD, 28)

ITEMS = [
    {
        "number": "01",
        "title": "MẸO CỘNG ĐỒNG",
        "body": "Có thể bị vá bất cứ lúc nào",
        "color": AMBER,
        "icon": "patch",
    },
    {
        "number": "02",
        "title": "MÁY CỦA NGƯỜI KHÁC",
        "body": "Không nhập email, ngân hàng hay thẻ",
        "color": CYAN,
        "icon": "shield",
    },
    {
        "number": "03",
        "title": "FREE CÓ GIỚI HẠN",
        "body": "Đủ đăng ký — không đủ để farm",
        "color": PURPLE,
        "icon": "meter",
    },
    {
        "number": "04",
        "title": "ĐỪNG FARM TÀI KHOẢN",
        "body": "Lạm dụng một lần — cánh cửa hẹp thêm",
        "color": RED,
        "icon": "nodes",
    },
]


def clamp(v):
    return max(0.0, min(1.0, v))


def smooth(v):
    v = clamp(v)
    return v * v * (3 - 2 * v)


def ease(v):
    v = clamp(v)
    return 1 - (1 - v) ** 4


def centered(draw, text, y, font, fill):
    b = draw.textbbox((0, 0), text, font=font)
    draw.text(((W - (b[2] - b[0])) / 2, y), text, font=font, fill=fill)


def make_background():
    im = Image.new("RGBA", (W, H), (*BG, 255))
    lights = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lights)
    d.ellipse((-300, -300, 800, 800), fill=(0, 212, 255, 28))
    d.ellipse((1250, 350, 2300, 1400), fill=(150, 70, 255, 24))
    im.alpha_composite(lights.filter(ImageFilter.GaussianBlur(150)))
    ImageDraw.Draw(im).rounded_rectangle((50, 50, W - 50, H - 50), 25,
                                         outline=(0, 212, 255, 40), width=2)
    return im


BASE = make_background()


def icon_patch(d, cx, cy, c, a):
    d.rounded_rectangle((cx-82, cy-82, cx+82, cy+82), 22,
                        outline=(*c, a), width=8)
    d.line((cx-42, cy, cx-8, cy+34, cx+50, cy-38), fill=(*c, a), width=13)
    d.line((cx+70, cy-105, cx+70, cy-55), fill=(*RED, a), width=10)
    d.ellipse((cx+61, cy-128, cx+79, cy-110), fill=(*RED, a))


def icon_shield(d, cx, cy, c, a):
    pts = [(cx, cy-100), (cx+88, cy-65), (cx+70, cy+40),
           (cx, cy+105), (cx-70, cy+40), (cx-88, cy-65)]
    d.line(pts + [pts[0]], fill=(*c, a), width=10, joint="curve")
    d.line((cx-38, cy, cx-8, cy+32, cx+48, cy-36), fill=(*c, a), width=13)


def icon_meter(d, cx, cy, c, a):
    d.arc((cx-100, cy-80, cx+100, cy+120), 190, 350, fill=(*c, a), width=13)
    for ang in [200, 235, 270, 305, 340]:
        r1, r2 = 70, 92
        x1 = cx + math.cos(math.radians(ang)) * r1
        y1 = cy + math.sin(math.radians(ang)) * r1
        x2 = cx + math.cos(math.radians(ang)) * r2
        y2 = cy + math.sin(math.radians(ang)) * r2
        d.line((x1, y1, x2, y2), fill=(*c, a), width=7)
    d.line((cx, cy+20, cx+62, cy-42), fill=(*RED, a), width=12)
    d.ellipse((cx-13, cy+7, cx+13, cy+33), fill=(*WHITE, a))


def icon_nodes(d, cx, cy, c, a):
    pts = [(cx, cy-88), (cx-90, cy+10), (cx, cy+92), (cx+90, cy+10)]
    for i in range(1, 4):
        d.line((pts[0], pts[i]), fill=(*c, int(a * 0.7)), width=7)
    for x, y in pts:
        d.ellipse((x-25, y-25, x+25, y+25), fill=(*c, a))
    d.line((cx-105, cy-105, cx+105, cy+105), fill=(*RED, a), width=14)
    d.line((cx+105, cy-105, cx-105, cy+105), fill=(*RED, a), width=14)


ICONS = {"patch": icon_patch, "shield": icon_shield, "meter": icon_meter, "nodes": icon_nodes}


def draw_progress(d, active, alpha=255):
    total_w, gap = 620, 18
    seg_w = (total_w - gap * 3) / 4
    x0, y = (W - total_w) / 2, 935
    for i in range(4):
        color = ITEMS[i]["color"] if i <= active else (65, 76, 98)
        d.rounded_rectangle((x0 + i*(seg_w+gap), y,
                             x0 + i*(seg_w+gap) + seg_w, y+10), 5,
                            fill=(*color, alpha if i <= active else int(alpha*0.6)))


def draw_slide(im, item, index, local_t):
    # 0.6s in, 5.8s hold, 0.6s out within each seven-second chapter.
    enter = ease(local_t / 0.6)
    leave = 1 - smooth((local_t - 6.35) / 0.55)
    p = min(enter, leave)
    a = int(255 * p)
    shift = int(100 * (1 - enter) - 70 * (1 - leave))
    c = item["color"]
    d = ImageDraw.Draw(im)

    d.text((105, 92), "GIỜ NÓI THẲNG BỐN ĐIỀU", font=f_kicker,
           fill=(*MUTED, a))
    d.text((105, 145), item["number"], font=f_number, fill=(*c, a))
    d.text((290 + shift, 180), item["title"], font=f_title, fill=(*WHITE, a),
           stroke_width=4, stroke_fill=(0, 0, 0, a))
    d.text((295 + shift, 305), item["body"], font=f_body, fill=(*c, a))

    # Main glass panel.
    panel = (240 + shift, 430, W - 240 + shift, 820)
    d.rounded_rectangle(panel, 30, fill=(*PANEL, int(235*p)),
                        outline=(*c, int(200*p)), width=4)
    d.line((790 + shift, 480, 790 + shift, 770), fill=(255,255,255,int(24*p)), width=2)

    # Icon with glow.
    glow = Image.new("RGBA", (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    ICONS[item["icon"]](gd, 530 + shift, 625, c, int(220*p))
    im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(20)))
    ICONS[item["icon"]](ImageDraw.Draw(im), 530 + shift, 625, c, a)

    # Compact supporting labels in the right half of the panel.
    notes = [
        ["KHÔNG CHÍNH THỨC", "TRẠNG THÁI CÓ THỂ ĐỔI"],
        ["CHỈ DÙNG FORM CÔNG KHAI", "DỮ LIỆU NHẠY CẢM: KHÔNG"],
        ["ĐỦ CHO MỘT LẦN ĐĂNG KÝ", "KHÔNG PHẢI TÀI NGUYÊN VÔ HẠN"],
        ["FARM → BLACKLIST", "BLACKLIST → NGƯỜI THẬT MẮC KẸT"],
    ][index]
    for j, note in enumerate(notes):
        yy = 535 + j * 115
        d.ellipse((865+shift, yy+10, 887+shift, yy+32), fill=(*c, a))
        d.text((920+shift, yy), note, font=f_small, fill=(*WHITE, a))

    draw_progress(d, index, a)
    d.text((W-220, 940), f"{index+1:02d} / 04", font=f_kicker, fill=(*MUTED, a))


def render(frame):
    t = frame / FPS
    index = min(3, int(t // 7))
    local_t = t - index * 7
    im = BASE.copy()
    draw_slide(im, ITEMS[index], index, local_t)
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
