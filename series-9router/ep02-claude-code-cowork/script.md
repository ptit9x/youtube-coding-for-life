# EP02 — 9Router + Claude Code & Claude Cowork

---

## PART 1 — SCRIPT

Bạn đang chạy Claude Code. Một task phức tạp — refactor cả module, fix hàng chục bug. Token chạy lên nhanh. Rồi giữa chừng — bốn-hai-chín. Rate limit. Code viết dở. Context mất.

Nếu bạn đã xem tập trước, bạn biết 9Router giải quyết vấn đề này. Hôm nay mình setup cụ thể cho Claude Code — và cả Claude Cowork. Hai tool, một gateway, không tốn thêm đồng nào.

Bắt đầu với Claude Cowork. Mở dashboard 9Router, vào tab Công cụ. Bạn thấy danh sách tool — chọn Claude Cowork. Trang config hiện ra bốn mục. Select Endpoint — trỏ về localhost một-hai-bảy-không-không-một hai-không-một-hai-tám slash v1. Khóa API — copy key từ tab Điểm cuối. Models — bấm nút Combo, chọn combo "FreeModels" đã tạo ở tập trước.

Phần hay — MCP và Tools. 9Router cho bạn gắn MCP server thẳng vào Cowork từ đây. Ví dụ Tavily cho web search, hoặc Exa cho Web Search & Fetch. Bạn cũng bật được Browser Control nếu muốn Cowork điều khiển Chrome. Config xong, bấm Áp dụng.

Mở Claude Desktop app. Góc dưới bên trái — bạn thấy "richard · Gateway". Nghĩa là đang chạy qua 9Router. Model dropdown hiện "claude-free-models" — đó là combo của bạn. Miễn phí.

Demo thật. Mình mở project vibe-tube-atlas trong Cowork. Gõ "Review code and make a plan fix". Cowork bắt đầu — searched bốn patterns, read bốn files, ran hai commands. Rồi nó viết ra plan — Severity Summary với chín issues. Bốn HIGH, năm MED. Mỗi issue có file, mô tả, code snippet.

Tiếp. Mình bảo "Fix HIGH issue". Cowork bắt đầu fix từng task. Task một — fix analyzeKeyword dùng real totalResults. Task hai — Trending dùng videos.chart=mostPopular thay vì broken empty-keyword search. Nó thêm helper, rewrite component, verify, tự commit.

Chuyện ở đây — toàn bộ process này chạy trên free model qua 9Router. Nếu model hiện tại hết quota, 9Router tự nhảy sang model tiếp theo trong combo. Cowork không biết. Workflow không gián đoạn.

Giờ Claude Code. Cũng trong tab Công cụ của 9Router — chọn Claude Code. Config tương tự. Hoặc nếu bạn thích dòng lệnh — mở terminal, set ba biến môi trường. ANTHROPIC_BASE_URL trỏ về localhost hai-không-một-hai-tám slash v1. ANTHROPIC_API_KEY dùng key từ dashboard. NO_PROXY bằng localhost. Bỏ vào .zshrc, source lại.

Một lưu ý quan trọng — nếu bạn đã đăng nhập Claude Code bằng OAuth trước đó, terminal sẽ báo vàng: "Both ANTHROPIC_AUTH_TOKEN and ANTHROPIC_API_KEY set — auth may not work as expected." Giải pháp — unset ANTHROPIC_AUTH_TOKEN, hoặc claude /logout rồi chọn "No" khi hỏi API key approval.

Gõ claude. Claude Code khởi động — "Welcome back!" Model hiện "FreeModels · API Usage Billing". Mọi request giờ đi qua 9Router.

Demo. Mình chạy /init trên project vibe-tube-atlas. Claude Code bắt đầu — analyze codebase, read README, đọc core architecture files, đọc schema, hooks, supabase client. Sau gần hai phút — nó viết sáu mươi bốn dòng CLAUDE.md. Architecture, commands, non-obvious gotchas, conventions. Tất cả tự động.

Rồi mình dùng /model để chuyển sang glm/glm-năm-chấm-một — model rẻ hơn cho task nhẹ. Tiếp tục update CLAUDE.md, proof, thêm chi tiết. Mọi thứ vẫn chạy qua 9Router.

Một tính năng nữa — Claude Code plugins. Trong 9Router terminal, bạn thấy Plugins tab. Discover, install plugin như context7 — MCP server của Upstash cho documentation lookup. Install cho repo cụ thể, local scope. Xong.

Quay lại dashboard 9Router. Tab Thống kê — bạn thấy tổng usage. Hai trăm năm mươi lăm requests, mười hai triệu rưỡi input tokens, chi phí ước tính mười tám đô bảy mươi sáu cent. Nhưng phần lớn chạy trên free tier — Kiro AI, OpenCode Free, GLM Coding. Chi phí thực tế? Gần bằng không.

Setup mất khoảng năm phút. Nhưng nó thay đổi cách bạn làm việc. Claude Cowork review và fix code với free model. Claude Code init project, viết CLAUDE.md, coding — cũng free model. 9Router xử lý routing, fallback, token saving. Bạn chỉ cần tập trung vào thứ quan trọng nhất — code.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: ~7–8 phút**

**Cài đặt chung:** Dark terminal (iTerm2), Claude Desktop app dark mode, 9Router dashboard. Font ≥18px.

| # | Thời lượng | Loại | Narration tương ứng | Footage | Ghi chú cắt ghép |
|---|-----------|------|---------------------|---------|-----------------|
| 1 | 10s | **[TERM]** | "Bạn đang chạy Claude Code...Rate limit." | Staged hoặc b-roll | Terminal hiện 429 error |
| 2 | 5s | — | "Nếu bạn đã xem tập trước..." | Cut nhanh | Dashboard 9Router flash |
| 3 | 25s | **[BROWSER]** | "Mở dashboard 9Router...bấm Áp dụng." | **003_connect_claude01.mov** ~0:00–1:30 | Tab Công cụ → Claude Cowork config: endpoint, API key, models (+Combo), MCP (Tavily), Tools (Exa, Browser Control) |
| 4 | 8s | **[BROWSER]** | "Mở Claude Desktop app...'richard · Gateway'." | **003_use_with_claude_app.mov** ~0:00–0:15 | Claude Desktop: Cowork tab, bottom left "richard · Gateway", model "claude-free-models" |
| 5 | 20s | **[BROWSER]** | "Demo thật...Severity Summary với chín issues." | **003_use_with_claude_app.mov** ~0:15–2:00 | Cowork: "Review code and make a plan fix" → "Working on it..." → plan output |
| 6 | 20s | **[BROWSER]** | "Tiếp...bảo 'Fix HIGH issue'." | **003_use_with_claude_app002.mov** ~0:00–2:00 | Cowork: Severity Summary table (9 issues), "Fix HIGH issue" prompt, plan document open |
| 7 | 30s | **[BROWSER]** | "Cowork bắt đầu fix...tự commit." | **003_use_with_claude_app002.mov** ~3:00–7:00 | Cowork fixing tasks: edit files, add helpers, update components, commit + push. Cắt highlights |
| 8 | 8s | — | "Toàn bộ process...không gián đoạn." | Dashboard 9Router | Flash Usage tab — show requests flowing |
| 9 | 15s | **[BROWSER]** | "Giờ Claude Code...config tương tự." | **003_connect_claude01.mov** ~1:30–1:51 | 9Router Công cụ → Claude Code config (hoặc env vars) |
| 10 | 15s | **[TERM]** | "Mở terminal...source lại." + warning ANTHROPIC_AUTH_TOKEN | **003_use_with_claude_code.mov** ~0:00–0:30 | Claude Code launch, warning yellow text, /model set |
| 11 | 25s | **[TERM]** | "Gõ claude...Model hiện 'FreeModels'." + "/init...CLAUDE.md" | **003_use_with_claude_code.mov** ~0:30–5:00 | Claude Code: Welcome back, FreeModels, /init → analyze codebase → Write 64 lines CLAUDE.md. Cắt highlights |
| 12 | 15s | **[TERM]** | "/model chuyển sang glm-5.1...update CLAUDE.md." | **003_use_with_claude_code.mov** ~5:00–9:00 | /model → glm/glm-5.1 → update CLAUDE.md → proof. Cắt highlights |
| 13 | 10s | **[TERM]** | "Claude Code plugins...context7." | **003_install_plugin.mov** ~0:00–1:19 | 9Router CLI → Claude Code Plugins → Discover → context7 → install local scope |
| 14 | 15s | **[BROWSER]** | "Tab Thống kê...gần bằng không." | **002-9router_multi_task.mov** | Usage: 255 requests, 12.5M tokens, $18.76. Provider graph. Highlight free providers |
| 15 | 8s | **[B-ROLL]** | "Setup mất khoảng năm phút...code." | Tay gõ bàn phím, fade out | |

**Tổng: ~229s visuals + pauses ≈ 7–8 phút**

**Lưu ý cắt ghép:**
- Video 003_use_with_claude_app và 003_use_with_claude_app002 là 2 phần liên tiếp của cùng session Cowork — cắt nối tự nhiên
- Claude Code video dài 9:48 — cần cắt nhiều, giữ highlights: /init, Write CLAUDE.md, /model, proof
- Ẩn sensitive data: email, API keys, project secrets
- iTerm2 có 2 tab: "9router (tray_darwin_release)" và "Claude Code" — show cả 2 để viewer thấy 9Router chạy background

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

**Prompt 1:**
A cinematic photograph of a developer at a dark desk with three terminal windows on the monitor showing Claude Code running with green text output, a routing dashboard visible on a second monitor with neon cyan connection lines, dark moody lighting with monitor glow illuminating the developer's face from below, shallow depth of field, bokeh rain on window behind, code visible with syntax highlighting in green and cyan on dark background, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 2:**
A cinematic photograph of a split-screen monitor setup in a dark room, one screen showing a CLI terminal with green code output and the other showing a sleek desktop app with a chat interface, dramatic neon purple and cyan ambient lighting, shallow depth of field, reflections on the glossy desk surface, mechanical keyboard in foreground slightly blurred, 8k, photorealistic, like a developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 3:**
A cinematic photograph of three floating holographic terminal windows in a dark void, each showing different AI agent outputs with green text, connected by glowing neon green routing lines to a central hub node, dramatic rim lighting, deep shadows, code fragments floating in the air between the terminals, purple and cyan ambient glow, 8k, photorealistic, like a high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Claude Code + Cowork MIỄN PHÍ — 9Router biến free model thành vũ khí | Lập trình là cuộc sống
2. 255 requests, 12 triệu tokens, 0 đồng — đây là cách tôi làm | Lập trình là cuộc sống
3. Setup 5 phút biến Claude Code thành cỗ máy code không giới hạn | Lập trình là cuộc sống
4. Claude Cowork fix 9 bugs trong 1 session — bằng free model | Lập trình là cuộc sống
5. Tại sao Claude Code của tôi KHÔNG BAO GIỜ hết quota | Lập trình là cuộc sống
6. Claude Code + Claude Cowork + 9Router = AI coding miễn phí | Lập trình là cuộc sống
7. 429 Rate Limit — lỗi đáng sợ nhất và cách tôi xóa sổ nó | Lập trình là cuộc sống
8. 1 gateway nhỏ cứu cả coding workflow của tôi | Lập trình là cuộc sống
9. Tôi dùng Claude Code với free model — và kết quả bất ngờ | Lập trình là cuộc sống
10. Đừng chạy Claude Code mà không có gateway — bài học đắt giá | Lập trình là cuộc sống

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

### Option 1 — "Free Model"

**5a. Image prompt:**
A cinematic photograph, a developer silhouette sitting at a desk with a monitor showing a terminal with green "Welcome back!" text and a Claude robot mascot, dramatic neon green lighting from the monitor contrasting with purple ambient glow from behind, code text floating and reflecting off the desk surface, dark moody background with rain streaks on window, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **CLAUDE CODE** — `#FFFFFF` white
- Line 2: **FREE MODEL** — `#00FF41` neon green
- Line 3 (small badge): **VẪN CODE NGON** — `#00FF41` neon green, nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **JetBrains Mono**.
- Mỗi line cao 110–140px. Line spacing 0.85. Text block ~1/3 frame bên trái.
- Neon glow: duplicate layer, blur 10px, opacity 65%. Black outline 8px.
- Scan-line overlay. Giữ text-free version.

### Option 2 — "255 Requests"

**5a. Image prompt:**
A cinematic photograph, a glowing analytics dashboard floating in a dark space showing large neon green numbers "255" and token count graphs, multiple provider logos connected by bright routing lines orbiting around the dashboard, dramatic neon green and cyan lighting, extreme contrast, dark void background with subtle code matrix rain, dramatic lighting from the dashboard casting volumetric light beams, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **255 REQUESTS** — `#00FF41` neon green
- Line 2: **0 ĐỒNG** — `#FFFFFF` white
- Line 3 (small badge): **FREE TIER** — `#00FF41` neon green, nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **Anton**. Mỗi line cao 120–140px. Line spacing 0.85.
- Neon glow: duplicate layer, blur 12px, opacity 70%. Black outline 8px.
- Scan-line overlay. Giữ text-free version.

### Option 3 — "Code + Cowork"

**5a. Image prompt:**
A cinematic photograph, a dramatic split-composition showing a dark CLI terminal on the left half and a sleek light-themed chat app interface on the right half, both connected by glowing neon green data streams flowing through a central routing node, dark moody background, dramatic neon purple and green lighting, code fragments and document icons floating between the two halves, high contrast, deep shadows, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **CODE +** — `#00FF41` neon green
- Line 2: **COWORK** — `#FFFFFF` white
- Line 3: **1 GATEWAY** — `#00FF41` neon green

**5c. Typography specs:**
- Canvas 1280×720. Font **JetBrains Mono**. Mỗi line cao 110–130px. Line spacing 0.85.
- Neon glow: duplicate layer, blur 10px, opacity 65%. Black outline 8px.
- Scan-line overlay. Giữ text-free version.
