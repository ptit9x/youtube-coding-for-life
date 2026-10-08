# EP01 — Cài Đặt 9Router Trên Mac & Cách Dùng Cơ Bản

---

## PART 1 — SCRIPT

Hai giờ sáng. Claude Code đang chạy ngon lành — rồi đột ngột dừng. Bốn-hai-chín. Rate limit. Bạn chuyển sang Cursor — cũng hết quota. Mà mới xài có nửa ngày.

Bạn không thiếu tiền trả subscription. Bạn thiếu một thứ khác — một cách để không bao giờ bị dừng lại giữa chừng.

Thử quản lý thủ công. Bốn, năm API key khác nhau. Mỗi lần hết quota lại vào settings, đổi key, đổi model. Mệt. Mà vẫn bị gián đoạn.

Rồi bạn tìm thấy 9Router.

9Router là gateway chạy ngay trên máy bạn. Nó ngồi giữa — giữa tất cả AI coding tool và tất cả LLM provider ngoài kia. Bạn trỏ mọi thứ về một địa chỉ duy nhất: localhost hai-không-một-hai-tám. Vậy thôi. Open source, MIT license, miễn phí hoàn toàn.

Cài đặt thì đơn giản. Mở terminal. Kiểm tra Node.js — node đét-vi, phiên bản hai-sáu-chấm-ba. Chạy en-pi-em install đét-gi 9router. Mười package, hai mươi giây. Xong.

Gõ 9router. Nó hiện ra menu — Web UI mở trong browser, Terminal UI nếu bạn thích dòng lệnh, hoặc Hide to Tray chạy nền. Chọn Web UI. Dashboard mở ra ở localhost hai-không-một-hai-tám.

Việc đầu tiên — tạo API Key cho 9Router. Vào tab Điểm cuối. Bạn thấy endpoint là localhost hai-không-một-hai-tám slash v1. Bấm Create Key, đặt tên — ví dụ "Production Key". Bật Require API key để bảo mật. Lưu key này lại — bạn sẽ dùng nó cho mọi tool.

Tiếp theo — kết nối provider. Tab Nhà cung cấp. Bạn sẽ thấy ba loại. OAuth Providers — Claude Code, OpenAI Codex, GitHub Copilot, Cursor IDE, Kilo Code, Cline — đăng nhập một lần, 9Router tự refresh token. Free Providers — iFlow AI, Qwen Code, Gemini CLI, Kiro AI — connect miễn phí, không cần API key. Và API Key Providers — OpenRouter, GLM Coding, Minimax Coding, Alibaba — paste key vào là xong.

Bạn kết nối được bao nhiêu thì kết nối. Càng nhiều provider, càng ít khả năng bị gián đoạn.

Giờ đến phần quan trọng nhất — Kết hợp. Hay gọi là Combo. Vào tab Kết hợp. 9Router cho bạn bốn chiến lược. Fallback — thử model theo thứ tự, cái nào fail thì nhảy sang cái tiếp theo. Vòng tròn — Round Robin, xoay vòng đều giữa các model để chia tải. Fusion — query tất cả model song song rồi để một "judge" tổng hợp câu trả lời tốt nhất, chất lượng cao nhất nhưng tốn nhất. Và Capacity auto-switch — tự chuyển model khi cần đọc hình ảnh hay audio.

Mình tạo một combo tên "FreeModels". Chọn chiến lược Fallback. Thêm gh/claude-opus-bốn-chấm-bảy làm primary, kr/claude-opus-bốn-chấm-năm-thinking làm backup, gemini/gemini-ba-chấm-sáu-flash làm tier cuối. Khi model đầu hết quota, nó tự nhảy xuống model tiếp theo. Không gián đoạn.

Phía dưới combo là Vision Adapter. Bật lên, nếu model đang dùng không đọc được hình ảnh, 9Router tự chuyển sang model có vision. Tính năng này mới, khá hay.

Muốn xem nó hoạt động — vào tab Thống kê. Bạn thấy tổng request, token input, cached token, output token, và estimated cost. Provider graph ở giữa — 9Router kết nối tới từng provider như Kiro AI, OpenCode Free, GLM Coding, Gemini, OpenAI Codex. Bên phải là Recent Requests — model nào đang xử lý, bao nhiêu token, bao lâu trước. Mọi thứ transparent.

Và Token Saver. Vào tab Token Saver — nó tự động nén output từ các tool như git diff, grep, ls trước khi gửi cho LLM. Giảm hai mươi đến bốn mươi phần trăm token input. Không mất thông tin.

Cuối cùng — tab Cài đặt. Đổi ngôn ngữ sang tiếng Việt. Bật bảo mật — yêu cầu mật khẩu khi truy cập dashboard. Chọn chiến lược định tuyến mặc định. Đơn giản.

9Router không phải magic. Nó là engineering tốt — một proxy nhỏ chạy local, nhưng cho bạn thứ quan trọng nhất khi code với AI — sự liên tục. Không gián đoạn. Không lo quota. Chỉ code.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: ~6–7 phút**

**Cài đặt chung:** Dark terminal (iTerm2), font ≥18px, dark dashboard theme nếu có. Ẩn bookmark bar và tab không cần thiết trong browser.

| # | Thời lượng | Loại | Narration tương ứng | Footage | Ghi chú cắt ghép |
|---|-----------|------|---------------------|---------|-----------------|
| 1 | 10s | **[TERM]** | "Hai giờ sáng...Rate limit...cũng hết quota." | B-roll hoặc staged terminal error | Có thể dùng staged footage — hiện `429 Rate limit exceeded` |
| 2 | 8s | **[B-ROLL]** | "Thử quản lý thủ công...mệt." | Tay gõ bàn phím + montage settings | Quick cuts |
| 3 | 8s | **[BROWSER]** | "Rồi bạn tìm thấy 9Router." | **001-install.mov** ~0:00–0:20 | GitHub repo decolua/9router, README screenshot với Providers |
| 4 | 12s | **[DIAGRAM]** | "9Router là gateway...localhost:20128." | Excalidraw hoặc overlay | [Tools] → [9Router] → [Providers]. Vẽ hoặc dùng provider graph từ Thống kê |
| 5 | 20s | **[TERM]** | "Cài đặt thì đơn giản...Xong." | **001-install.mov** ~0:20–1:10 | Terminal: `node -v` → `npm install -g 9router` → output → `9router` |
| 6 | 10s | **[TERM]** | "Gõ 9router...Chọn Web UI." | **003_install_plugin.mov** ~0:00–0:10 | Menu Choose Interface: Web UI / Terminal UI / Hide to Tray |
| 7 | 20s | **[BROWSER]** | "Việc đầu tiên — tạo API Key...Lưu key này lại." | **002-9router_cach_dung_co_ban.mov** ~0:00–1:00 | Dashboard Endpoint tab → Create API Key dialog → "Production Key" |
| 8 | 25s | **[BROWSER]** | "Tab Nhà cung cấp...paste key vào là xong." | **001-install.mov** ~0:30–1:30 | Tab Providers: OAuth (Claude Code, Codex, Copilot...), Free (iFlow, Qwen, Kiro...), API Key (OpenRouter, GLM...) |
| 9 | 30s | **[BROWSER]** | "Giờ đến phần quan trọng nhất — Kết hợp...không gián đoạn." | **002-9router_cach_dung_co_ban.mov** ~1:30–3:00 | Tab Combos: 4 chiến lược. Tạo "FreeModels" combo, chọn Fallback, thêm 3 model |
| 10 | 10s | **[BROWSER]** | "Vision Adapter...tính năng này mới." | **002-9router_cach_dung_co_ban.mov** ~3:00–3:30 | Vision Adapter section bên dưới combo |
| 11 | 25s | **[BROWSER]** | "Vào tab Thống kê...transparent." | **002-9router_cach_dung_co_ban.mov** ~4:00–5:00 + **002-9router_multi_task.mov** | Usage tab: 7 requests/$0.10 → cut to heavy usage 255 requests/$18.76. Provider graph, Recent Requests |
| 12 | 10s | **[BROWSER]** | "Token Saver...không mất thông tin." | **002-9router_cach_dung_co_ban.mov** ~5:00–5:30 | Token Saver tab |
| 13 | 12s | **[BROWSER]** | "Tab Cài đặt...Đơn giản." | **002-9router_cach_dung_co_ban.mov** ~6:00–6:50 | Settings: ngôn ngữ VN, bảo mật, chiến lược định tuyến |
| 14 | 8s | **[B-ROLL]** | "9Router không phải magic...Chỉ code." | Tay gõ bàn phím, code trên monitor | Fade out |

**Tổng: ~208s visuals + pauses ≈ 6–7 phút**

**Lưu ý cắt ghép:**
- Video 001 và 002 quay ở version v0.5.40, video 002 (multi_task) và 003 ở v0.5.50 — sidebar hơi khác. Nên cắt consistent, tránh nhảy giữa 2 version nếu được.
- Dashboard đã ở tiếng Việt — script đã update tên tab tương ứng.
- Ẩn email/API key nhạy cảm khi edit (laptrinhlacuocsong@gmail.com hiện trong Codex provider).

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

**Prompt 1:**
A cinematic photograph of a developer sitting at a dark desk at night, three glowing monitors showing different AI dashboards with routing diagrams and provider connections in green and cyan, the developer's face lit by warm amber monitor glow, shallow depth of field, bokeh city lights through window, dark moody atmosphere, code visible on screens with syntax highlighting in green and cyan on dark background, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 2:**
A cinematic close-up photograph of a dark computer screen showing a network routing diagram with glowing neon green and cyan connection lines between circular provider nodes, dramatic rim lighting on the screen edges, dark moody background with purple ambient glow, code text reflecting on the glass surface of the monitor, shallow depth of field, 8k, photorealistic, like a developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 3:**
A cinematic photograph of a mechanical keyboard with neon green keycap backlighting in a dark room, a terminal window on the monitor behind showing a successful npm install log with green text on black background, dramatic low-key lighting with monitor glow illuminating the scene, coffee cup nearby, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Tool này cứu tôi khỏi cái bẫy rate limit lúc 2 giờ sáng | Lập trình là cuộc sống
2. Tại sao tôi KHÔNG BAO GIỜ bị hết quota AI nữa | Lập trình là cuộc sống
3. 1 proxy nhỏ, tiết kiệm 40% tiền AI mỗi tháng | Lập trình là cuộc sống
4. Rate limit killed my flow — cho đến khi tôi tìm ra thứ này | Lập trình là cuộc sống
5. Dev thông minh không trả tiền AI gấp đôi — họ dùng gateway | Lập trình là cuộc sống
6. 9Router: cách tôi chạy 5 AI tool chỉ với 1 endpoint | Lập trình là cuộc sống
7. Cài 1 tool, xóa nỗi sợ "quota exhausted" vĩnh viễn | Lập trình là cuộc sống
8. 40+ AI provider, 1 địa chỉ localhost — thay đổi cách tôi code | Lập trình là cuộc sống
9. Đừng trả tiền thêm cho AI — hãy route nó thông minh hơn | Lập trình là cuộc sống
10. Bí mật nhỏ giúp tôi code với AI 24/7 không gián đoạn | Lập trình là cuộc sống

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

### Option 1 — "Hết Quota"

**5a. Image prompt:**
A cinematic photograph, developer silhouette sitting in front of three monitors showing red error screens in a dark room, dramatic neon red and cyan lighting, code text floating and reflecting off the desk surface, dark moody background with city bokeh through rain-streaked window, high contrast, dramatic rim lighting from monitors, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **HẾT QUOTA** — `#00FF41` neon green
- Line 2: **LÚC 2 GIỜ SÁNG** — `#FFFFFF` white
- Line 3 (small badge): **1 TOOL CỨU TẤT CẢ** — `#00FF41` neon green, trên nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **JetBrains Mono**.
- Mỗi line cao 110–140px. Line spacing 0.85. Text block ~1/3 frame bên trái.
- Neon glow: duplicate layer, blur 10px, opacity 65%. Black outline 8px.
- Scan-line overlay. Giữ text-free version.

### Option 2 — "1 Endpoint"

**5a. Image prompt:**
A cinematic photograph, a single glowing neon green terminal window floating in a completely dark void, multiple faded provider logos orbiting around it like satellites, dramatic neon green and purple lighting, code fragments floating in the air, extreme contrast between the bright terminal and deep black surroundings, dramatic rim lighting, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **5 AI TOOL** — `#FFFFFF` white
- Line 2: **1 ENDPOINT** — `#00FF41` neon green
- Line 3 (small badge): **MIỄN PHÍ** — `#00FF41` neon green, nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **Anton**. Mỗi line cao 120–140px. Line spacing 0.85.
- Neon glow: duplicate layer, blur 12px, opacity 70%. Black outline 8px.
- Scan-line overlay. Giữ text-free version.

### Option 3 — "Tiết Kiệm 40%"

**5a. Image prompt:**
A cinematic photograph, dramatic close-up of a developer's hands on a mechanical keyboard with neon green backlighting, a monitor behind showing a routing dashboard with green success indicators and flowing data streams, dark moody background with purple and cyan ambient glow, code reflecting on the developer's glasses in the foreground slightly blurred, high contrast, dramatic lighting from below, deep shadows, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **GIẢM 40%** — `#00FF41` neon green
- Line 2: **TIỀN AI** — `#FFFFFF` white
- Line 3: **MỖI THÁNG** — `#FFFFFF` white

**5c. Typography specs:**
- Canvas 1280×720. Font **JetBrains Mono**. Mỗi line cao 110–130px. Line spacing 0.85.
- Neon glow: duplicate layer, blur 10px, opacity 65%. Black outline 8px.
- Scan-line overlay. Giữ text-free version.
