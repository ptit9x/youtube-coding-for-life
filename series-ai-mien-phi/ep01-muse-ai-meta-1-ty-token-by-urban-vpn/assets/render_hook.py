#!/usr/bin/env python3
"""
Render 15-second hook overlay animation → MP4
1280×720 @ 30fps = 450 frames
Uses Arial Bold for Vietnamese diacritics support.
"""

import os, math, random
from PIL import Image, ImageDraw, ImageFont

# ─── CONFIG ───
W, H = 1280, 720
FPS = 30
DURATION = 15
TOTAL_FRAMES = FPS * DURATION
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frames")
os.makedirs(OUT_DIR, exist_ok=True)

# Colors
BG_DARK    = (6, 6, 15)
NEON_GREEN = (0, 255, 65)
RED_BADGE  = (232, 25, 44)
WHITE      = (255, 255, 255)
CYAN       = (0, 212, 255)

# ─── FONTS (Arial Bold = Vietnamese-safe) ───
ARIAL_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
MENLO      = "/System/Library/Fonts/Menlo.ttc"

font_headline = ImageFont.truetype(ARIAL_BOLD, 92)
font_badge    = ImageFont.truetype(ARIAL_BOLD, 54)
font_code     = ImageFont.truetype(MENLO, 12)

# ─── CODE PARTICLES ───
code_snippets = [
    "const token = await fetch();",
    "import { Agent } from 'muse';",
    "model.generate(prompt);",
    "return response.data;",
    "async function run() {",
    "export default config;",
    "await muse.resume();",
    "git checkout -b feature",
    "npm install @meta/muse",
    "class LLM extends Model {",
    "const api = new MetaAPI();",
    "pipeline.execute(tasks);",
]

random.seed(42)
particles = []
for snip in code_snippets:
    particles.append({
        "text": snip,
        "x": random.randint(30, W - 300),
        "y_base": random.randint(50, H - 50),
        "phase": random.random() * math.pi * 2,
        "speed": random.uniform(8, 20),
    })

dots = [{"x": random.randint(20, W-20), "y_base": random.randint(20, H-20),
         "phase": random.random()*math.pi*2, "speed": random.uniform(5,15)}
        for _ in range(15)]


def ease_out_expo(t):
    return 1 if t >= 1 else 1 - math.pow(2, -10 * t)

def ease_out_back(t):
    c1, c3 = 1.70158, 1.70158 + 1
    return 1 + c3 * pow(t - 1, 3) + c1 * pow(t - 1, 2)

def clamp(v, lo=0, hi=255):
    return max(lo, min(hi, int(v)))


# ─── PRE-COMPUTE STATIC LAYERS ───
print("Pre-computing background + vignette...")

bg_cache = Image.new("RGBA", (W, H), (*BG_DARK, 255))
bg_draw = ImageDraw.Draw(bg_cache)

# Radial gradient
for gy in range(0, H, 3):
    for gx in range(0, W, 3):
        dx = (gx - W * 0.3) / W
        dy = (gy - H * 0.4) / H
        dist = math.sqrt(dx*dx + dy*dy)
        if dist < 0.55:
            brightness = int(18 * (1 - dist / 0.55))
            c = tuple(min(255, BG_DARK[i] + brightness) for i in range(3))
            bg_draw.rectangle([gx, gy, gx+2, gy+2], fill=(*c, 255))

# Scan lines
for sy in range(0, H, 4):
    bg_draw.line([(0, sy), (W, sy)], fill=(255, 255, 255, 5), width=1)

# Vignette
vignette_cache = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vdraw = ImageDraw.Draw(vignette_cache)
for vy in range(0, H, 2):
    for vx in range(0, W, 2):
        dx = (vx - W/2) / (W/2)
        dy = (vy - H/2) / (H/2)
        dist = math.sqrt(dx*dx + dy*dy)
        if dist > 0.55:
            va = int(min(200, 200 * (dist - 0.55) / 0.7))
            vdraw.rectangle([vx, vy, vx+1, vy+1], fill=(0, 0, 0, va))

print("Pre-computation done.")


def render_frame_fast(frame_idx):
    t = frame_idx / FPS

    img = bg_cache.copy()
    draw = ImageDraw.Draw(img)

    # ── Code particles ──
    for p in particles:
        cycle = (t * p["speed"] * 0.05 + p["phase"]) % 1.0
        alpha = int(55 * math.sin(cycle * math.pi))
        if alpha > 5:
            y_off = -40 * cycle + 20
            draw.text((p["x"], p["y_base"] + y_off), p["text"],
                      font=font_code, fill=(*NEON_GREEN, clamp(alpha)))

    # ── Green dots ──
    for d in dots:
        cycle = (t * 0.15 + d["phase"] / (2 * math.pi)) % 1.0
        alpha = int(90 * math.sin(cycle * math.pi))
        if alpha > 10:
            y_off = -25 * math.sin(cycle * math.pi)
            r = 3
            draw.ellipse([d["x"]-r, d["y_base"]+y_off-r,
                          d["x"]+r, d["y_base"]+y_off+r],
                         fill=(*NEON_GREEN, clamp(alpha)))

    # ══════════════════════════════════════════════════
    # HEADLINE: "META TẶNG 1 TỶ TOKEN" — appear at t=0.3s
    # ══════════════════════════════════════════════════
    hl_start = 0.3
    headline_y = 170

    if t >= hl_start:
        progress = min(1, (t - hl_start) / 0.8)
        ep = ease_out_expo(progress)
        alpha = int(255 * ep)

        text_full = "META TẶNG 1 TỶ TOKEN"

        # Glitch at t=0.9–1.2s
        gx_off, gy_off = 0, 0
        if 0.9 <= t <= 1.2:
            gp = ((t - 0.9) / 0.1) % 1.0
            gx_off = int(5 * math.sin(gp * math.pi * 6))
            gy_off = int(3 * math.cos(gp * math.pi * 4))

        # Measure text
        bbox = draw.textbbox((0, 0), text_full, font=font_headline)
        tw = bbox[2] - bbox[0]
        base_x = (W - tw) // 2

        # Neon glow (soft green halo)
        for gdx in range(-8, 9, 2):
            for gdy in range(-8, 9, 2):
                dist_g = math.sqrt(gdx*gdx + gdy*gdy)
                if dist_g <= 8:
                    ga = int(alpha * 0.10 * (1 - dist_g / 8))
                    if ga > 2:
                        draw.text((base_x + gdx + gx_off,
                                  headline_y + gdy + gy_off),
                                 text_full, font=font_headline,
                                 fill=(*NEON_GREEN, ga))

        # Main white text
        draw.text((base_x + gx_off, headline_y + gy_off),
                  text_full, font=font_headline, fill=(*WHITE, alpha))

        # Overlay "1 TỶ" in neon green
        prefix = "META TẶNG "
        prefix_w = draw.textbbox((0, 0), prefix, font=font_headline)[2]
        green_text = "1 TỶ"
        draw.text((base_x + prefix_w + gx_off, headline_y + gy_off),
                  green_text, font=font_headline, fill=(*NEON_GREEN, alpha))

        # Red glitch slice
        if 0.9 <= t <= 1.2 and int((t-0.9)*30) % 3 == 0:
            draw.text((base_x - 4, headline_y + 3), text_full,
                      font=font_headline, fill=(255, 0, 76, 70))
        # Cyan glitch slice
        if 0.95 <= t <= 1.25 and int((t-0.95)*30) % 3 == 0:
            draw.text((base_x + 4, headline_y - 2), text_full,
                      font=font_headline, fill=(0, 212, 255, 50))

    # ══════════════════════════════════════════════════
    # NEON LINE at t=1.5s
    # ══════════════════════════════════════════════════
    if t >= 1.5:
        progress = min(1, (t - 1.5) / 1.0)
        ep = ease_out_expo(progress)
        line_w = int(550 * ep)
        line_y = H - 75
        cx = W // 2
        for lx in range(-line_w//2, line_w//2, 1):
            ratio = abs(lx) / max(1, line_w // 2)
            lr = int(NEON_GREEN[0] * (1-ratio) + CYAN[0] * ratio)
            lg = int(NEON_GREEN[1] * (1-ratio) + CYAN[1] * ratio)
            lb = int(NEON_GREEN[2] * (1-ratio) + CYAN[2] * ratio)
            la = int(255 * (1 - ratio * 0.4))
            px = cx + lx
            if 0 <= px < W:
                draw.line([(px, line_y), (px, line_y+2)], fill=(lr,lg,lb,la))
                # Soft glow
                draw.line([(px, line_y-3), (px, line_y+5)], fill=(lr,lg,lb,la//5))

    # ══════════════════════════════════════════════════
    # CORNER DECORATIONS at t=1.8s
    # ══════════════════════════════════════════════════
    if t >= 1.8:
        progress = min(1, (t - 1.8) / 0.5)
        ca = int(140 * progress)
        cs, mg = 40, 28
        gc = (*NEON_GREEN, ca)
        # TL
        draw.line([(mg, mg), (mg+cs, mg)], fill=gc, width=2)
        draw.line([(mg, mg), (mg, mg+cs)], fill=gc, width=2)
        # TR
        draw.line([(W-mg-cs, mg), (W-mg, mg)], fill=gc, width=2)
        draw.line([(W-mg, mg), (W-mg, mg+cs)], fill=gc, width=2)
        # BL
        draw.line([(mg, H-mg), (mg+cs, H-mg)], fill=gc, width=2)
        draw.line([(mg, H-mg-cs), (mg, H-mg)], fill=gc, width=2)
        # BR
        draw.line([(W-mg-cs, H-mg), (W-mg, H-mg)], fill=gc, width=2)
        draw.line([(W-mg, H-mg-cs), (W-mg, H-mg)], fill=gc, width=2)

    # ══════════════════════════════════════════════════
    # BADGES
    # ══════════════════════════════════════════════════
    def draw_badge(text, start_t, y_pos):
        if t < start_t:
            return
        progress = min(1, (t - start_t) / 0.6)
        ep = ease_out_back(min(1, progress))
        alpha_b = int(255 * min(1, progress / 0.25))

        x_off = int(-160 * (1 - ep))

        bbox = draw.textbbox((0, 0), text, font=font_badge)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        px_pad, py_pad = 44, 14
        bx = (W - tw) // 2 + x_off - px_pad
        by = y_pos - py_pad

        # Pulsing glow
        pulse = 0.5 + 0.5 * math.sin((t - start_t) * 3.5)
        ge = int(14 * pulse)
        for gi in range(ge, 0, -2):
            ga = int(alpha_b * 0.06 * (1 - gi / max(1, ge)))
            if ga > 1:
                draw.rounded_rectangle(
                    [bx-gi, by-gi, bx+tw+2*px_pad+gi, by+th+2*py_pad+gi],
                    radius=12, fill=(RED_BADGE[0], RED_BADGE[1], RED_BADGE[2], ga))

        # Badge body
        draw.rounded_rectangle(
            [bx, by, bx+tw+2*px_pad, by+th+2*py_pad],
            radius=10, fill=(*RED_BADGE, alpha_b))

        # Badge text
        draw.text(((W - tw) // 2 + x_off, y_pos),
                  text, font=font_badge, fill=(255, 255, 255, alpha_b))

        # Shine sweep
        if progress < 0.8:
            shine_x = bx + int((tw + 2*px_pad) * progress / 0.8)
            for sx in range(shine_x - 20, shine_x + 20):
                if bx <= sx <= bx + tw + 2*px_pad:
                    sa = int(40 * (1 - abs(sx - shine_x) / 20))
                    draw.line([(sx, by+2), (sx, by+th+2*py_pad-2)],
                             fill=(255, 255, 255, sa))

    draw_badge("VN CHƯA MỞ?", 2.5, 345)
    draw_badge("Ô MÃ BÍ ẨN?", 4.0, 440)

    # ── Vignette ──
    img = Image.alpha_composite(img, vignette_cache)

    return img


# ─── RENDER ALL FRAMES ───
print(f"Rendering {TOTAL_FRAMES} frames at {W}x{H} @ {FPS}fps...")

for i in range(TOTAL_FRAMES):
    frame = render_frame_fast(i)
    frame_rgb = Image.new("RGB", (W, H), (0, 0, 0))
    frame_rgb.paste(frame, mask=frame.split()[3])
    frame_rgb.save(os.path.join(OUT_DIR, f"frame_{i:04d}.png"))
    if (i + 1) % 30 == 0:
        sec = (i + 1) / FPS
        print(f"  Frame {i+1}/{TOTAL_FRAMES} ({(i+1)*100//TOTAL_FRAMES}%) — {sec:.1f}s")

print("Frames done. Encoding MP4...")

# ─── ENCODE WITH FFMPEG ───
mp4_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hook-15s-overlay.mp4")
frames_pattern = os.path.join(OUT_DIR, "frame_%04d.png")
cmd = (
    f'ffmpeg -y -framerate {FPS} -i "{frames_pattern}" '
    f'-c:v libx264 -pix_fmt yuv420p -crf 17 -preset medium '
    f'-movflags +faststart "{mp4_path}"'
)
os.system(cmd)

# Cleanup frames
import shutil
shutil.rmtree(OUT_DIR, ignore_errors=True)

print(f"\n✅ Video saved: {mp4_path}")
print(f"   Resolution: {W}x{H} @ {FPS}fps")
print(f"   Duration:   {DURATION}s")
