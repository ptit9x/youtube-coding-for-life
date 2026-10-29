# EP02 — Thumbnail Package (Assets + AI Prompts)

## Đã render sẵn (dùng ngay)

| File | Mô tả |
|---|---|
| `thumbnail-01-ba-cua-dong.jpg` | Base text-free 1376×768 — 3 cửa chết (VPN / CHATGPT / SPARK, X đỏ) → chevron neon → cửa cuối sáng xanh lá + Muse logo phát sáng, nhãn LEXMOUNT |
| `thumbnail-01-with-text.jpg` | Bản final — stack chữ neon bên trái: `VPN CHẾT?` (đỏ) / `CỬA CUỐI` (xanh lá) / `VẪN MỞ` (xanh lá) + badge cyan `MIỄN PHÍ — 10/2026` |
| `render_thumbnail.py` | Script render (PIL) — chạy lại bất cứ lúc nào: `python3 render_thumbnail.py` |

Đồng bộ với EP01/EP02: cùng kích thước 1376×768, cột trái tối dành cho chữ, subject sáng bên phải, palette `#06060F` / `#00FF41` / `#00D4FF` / đỏ `#FF4444`, scan-lines + vignette, Muse logo thật (tái dùng `ep02.../assets/muse-logo.png`). Font render: Arial Bold (dấu tiếng Việt an toàn) + Menlo — tương đương JetBrains Mono.

## AI Image Prompts (Flow / Nano Banana — muốn bản photorealistic như EP01/EP02)

**Option 1 — Ba cửa, một cửa sáng (khuyên dùng):**
A cinematic photograph of a dark corridor with three massive vault doors, two of them sealed shut with red chains of light and one glowing wide open with neon green light spilling out, a small glowing asterisk-shaped AI logo hovering above the open door, a developer silhouette walking toward the light, purple ambient fog, dramatic rim lighting, deep shadows, high contrast, vivid saturated colors, subject on the right leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Option 2 — Cloud browser:**
A cinematic over-the-shoulder photograph of a developer in a dark room watching a laptop where a browser window floats inside a glowing cyan cloud, the page inside loading a radiant green portal with a glowing asterisk-shaped logo, neon green particles flowing from the cloud into the portal, cyan and purple rim lighting, shallow depth of field, bokeh city lights through window, 8k, 16:9. Photorealistic, like a developer documentary.

**Option 3 — Tường waitlist:**
A cinematic photograph of a developer silhouette facing a massive wall of glowing red waitlist tickets in a dark room, one small green door glowing at the far end of the wall, dramatic low-key lighting, purple fog, deep shadows, high contrast, vivid saturated neon colors, subject positioned low on the right leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

## Text spec (ghép trong Canva nếu dùng AI base)

- Line 1: `VPN CHẾT?` — `#FF4444` neon red
- Line 2: `CỬA CUỐI` — `#00FF41` neon green
- Line 3: `VẪN MỞ` — `#00FF41` neon green
- Badge: `MIỄN PHÍ — 10/2026` — `#00D4FF` cyan, nền `#1a1a2e` viền neon

**Typography:** Canvas 1280×720 (hoặc 1376×768 như các tập trước). Anton cho line 1–3, JetBrains Mono cho badge. Line 110–140px, spacing 0.85, text block ~1/3 trái. Neon glow: duplicate layer blur 10–12px opacity 60–70%; black stroke 8px. Không đè chữ lên subject. Scan-line overlay nhẹ. Luôn giữ bản text-free.
