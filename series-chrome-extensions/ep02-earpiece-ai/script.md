# EP02 — Vibe Coding 101: Code App AI phức tạp bằng mồm!

## YOUTUBE METADATA

### Title (chọn 1 trong 10 bên dưới)
**Recommended:** Tôi CODE app phức tạp mà KHÔNG GÕ một dòng logic nào

### Description (copy paste khi upload)
```
AI code ngu? Không. Bạn chưa biết cách ra lệnh cho nó.

Trong video này, tôi dùng AI Agent để build Earpiece AI — một Chrome Extension nghe phỏng vấn real-time, transcribe và gợi ý câu trả lời — kiến trúc Service Worker + Offscreen Document cực kỳ phức tạp. Nhưng tôi gần như không tự gõ một dòng code logic nào. Bí mật nằm ở "Master Prompt" và tư duy kiến trúc.

Đây là Vibe Coding — lập trình bằng cách mô tả kiến trúc cho AI, không phải bằng cách gõ từng dòng.

🔗 Boilerplate từ EP01: https://github.com/nicolestandifer3/nicolestandifer3-chrome-extension-boilerplate-react-vite
🔗 Source code Earpiece AI: https://github.com/ptit9x/earpiece

⏱️ Timestamps:
0:00 — Demo Earpiece AI live
0:45 — Nỗi đau MV3: Service Worker + Offscreen
1:30 — Bước ngoặt: Master Prompt
2:00 — Giải mã Master Prompt — 3 lớp context
3:30 — AI generate code trên màn hình
5:00 — Review và debug code AI
6:15 — Kết: Dev là Kiến trúc sư

📌 Series "Vibe Coding Chrome Extensions":
▸ EP01: Boilerplate "bá đạo" nhất — https://youtu.be/[link]
▸ EP02: Vibe Coding — Code app AI bằng mồm! (video này)

💬 Bạn đã thử Vibe Coding chưa? Kết quả thế nào? Comment cho tôi biết!

📋 MASTER PROMPT (copy & chỉnh sửa cho project của bạn):
Dựa trên repo boilerplate chrome-extension-boilerplate-react-vite (React 18 + Vite + Turborepo + Tailwind), hãy giúp tôi xây dựng "Earpiece AI" - một Chrome Extension (MV3) giúp transcribe audio từ online meetings (Google Meet, Zoom) và dùng AI để gợi ý câu trả lời.
Core Architecture & Data Flow (Bắt buộc tuân thủ):
Kiến trúc MV3: Giao tiếp qua IcMessage contract (đặt trong packages/shared/lib/messages.ts).
Service Worker (src/background): Quản lý orchestrate chrome.tabCapture.getMediaStreamId và gửi streamId đi.
Offscreen Document (pages/offscreen): DOM duy nhất chạy Web Speech API. Cần có cơ chế auto-restart mỗi 30s để vượt giới hạn của Chrome. Trả transcript về UI.
Side Panel (pages/side-panel): UI chính hiển thị Transcript (bên trái) và AI Suggestion (bên phải).
Hệ thống Settings & Storage (packages/storage & pages/options):
Sử dụng pattern createStorage của boilerplate để quản lý file cấu hình EarpieceConfig.
Cần một trang Options page đẹp mắt chứa các cấu hình quan trọng. Ví dụ phần "Recognition & Conversation" cần có:
userName: Tên ứng viên (giúp Speech-to-text nhận diện đúng hơn).
sttLang: Ngôn ngữ STT (Hỗ trợ en-US, vi-VN, ja-JP, ko-KR, zh-CN).
Các toggle switches (boolean): oneOnOne (Call 1-1), showVietnamese (Hiện dịch tiếng việt), debugAllRemote.
minConfidence: Lọc nhiễu âm thanh.
Design System (packages/ui):
Đừng code UI trực tiếp vào file. Hãy tách các component cơ bản như Card, Field, Input, Select, Button vào package packages/ui để tái sử dụng ở cả Side Panel và Options Page.
Sử dụng TailwindCSS, thiết kế giao diện tối (Dark mode) hiện đại.
i18n (Đa ngôn ngữ):
Áp dụng hệ thống đa ngôn ngữ vào packages/i18n/locales/{en,vi}/messages.json. Mọi string UI (ví dụ: "Recognition & Conversation") cần phải lấy từ hệ thống i18n để đảm bảo tính đồng bộ.
Step-by-Step Execution Plan:
Bước 1: Định nghĩa EarpieceConfig trong storage và IcMessage contract. Setup component library cơ bản trong packages/ui.
Bước 2: Xây dựng trang Options với RecognitionSection để quản lý config.
Bước 3: Tạo Offscreen document và viết logic auto-restart cho Web Speech API.
Bước 4: Cấu hình Service worker kết nối luồng capture audio.
Bước 5: Xây dựng Side Panel hiển thị real-time transcript và AI suggestion.

#VibeCoding #ChromeExtension #AI #CursorAI #ManifestV3 #ServiceWorker #OffscreenDocument #LapTrinhLaCuocSong #Developer #React #TypeScript #AIAgent #MasterPrompt #CodeWithAI
```

### Tags (paste vào YouTube Studio)
```
vibe coding,chrome extension,ai coding,cursor ai,manifest v3,service worker,offscreen document,master prompt,earpiece ai,ai agent,lập trình,coding with ai,chrome extension tutorial,react,typescript,developer,lập trình là cuộc sống,ai code,chrome extension manifest v3,pair programming ai
```

### Upload Settings
- **Visibility:** Public
- **Category:** Science & Technology
- **Language:** Vietnamese
- **Playlist:** Vibe Coding Chrome Extensions

---

## PART 1 — SCRIPT

Đây là Earpiece AI. Một Chrome Extension nghe phỏng vấn online real-time. Bắt âm thanh, transcribe trực tiếp, ném cho AI gợi ý câu trả lời. Kiến trúc cực kỳ phức tạp — Service Worker, Offscreen Document, message passing chồng chéo. Nhưng tôi gần như không tự gõ một dòng code logic cốt lõi nào. Toàn bộ — AI viết.

Bạn thử tự code Manifest V3 đi. Service Worker — cái background process của extension — không có DOM. Không `document`, không `window.audio`. Muốn bắt âm thanh? Phải tạo Offscreen Document — một trang HTML ẩn chạy riêng. Rồi hai thằng này phải giao tiếp qua `chrome.runtime.sendMessage`. Một hệ thống message passing mà sai một chữ là im lặng — không error, không log, chỉ... không chạy.

Bạn Google. Stack Overflow. Docs Chrome cũng ghi mơ hồ. Bạn hỏi AI — nó generate code dùng API cũ của Manifest V2. Hoặc nó bịa ra method không tồn tại. Vì AI không có context kiến trúc của project bạn.

Và đó chính là bài học. AI code "ngu" không phải vì nó dở. Mà vì bạn chưa đưa cho nó bản thiết kế. Bạn đang bắt thợ xây xây nhà mà không cho bản vẽ.

Thay vì bảo AI "code cho tôi cái app này đi", tôi viết một thứ gọi là Master Prompt. Một bản thiết kế kiến trúc cho AI đọc. Ba lớp rõ ràng.

Lớp một — Context. Tôi chỉ cho AI đọc folder `packages/shared` trước. Ở đó có type definitions, có `IcMessage` — cái "hợp đồng giao tiếp" giữa các phần của extension. AI đọc xong, nó biết message nào hợp lệ, data shape ra sao. Nó không đoán mò nữa.

Lớp hai — Architecture. Tôi vẽ rõ luồng dữ liệu: Side Panel là UI → gửi lệnh qua `IcMessage` → Service Worker nhận và điều phối → Offscreen Document xử lý audio, chạy speech recognition. Ba thằng, ba trách nhiệm, giao tiếp qua một kênh duy nhất.

Lớp ba — Edge cases. Đây là chỗ kinh nghiệm Dev quan trọng nhất. Chrome tự kill Offscreen Document sau sáu mươi giây không hoạt động. AI không biết luật này. Nên tôi ghi rõ trong prompt: "Offscreen phải có cơ chế heartbeat — tự ping mỗi ba mươi giây để Chrome không kill." Mình là Dev, mình biết luật của Chrome mà AI hay quên.

Giờ tôi ném Master Prompt vào AI Agent. Bạn nhìn nó chạy. Nó đọc `packages/shared`, hiểu type system. Tự tạo file trong đúng folder. `RecognitionSection.tsx` — dùng component `Card`, `Input` từ `packages/ui`. Tailwind dark theme chuẩn. Options Page tự sinh layout đẹp. Service Worker setup đúng message routing. Offscreen Document có heartbeat restart.

Việc AI làm trong năm phút — tôi ước tính phải mất cả tuần nếu tự gõ tay.

Nhưng — và đây là phần quan trọng — tôi không tin AI một trăm phần trăm. Code đẻ ra xong, tôi đọc. Từng file. Kiểm tra message passing có khớp type không. Chạy `pnpm dev`, test thử. Có lỗi — AI quên import icon — tôi copy lỗi, dán lại cho nó: "Quên import cái này, sửa đi." Nó sửa trong hai giây. Tôi review lại. Xong.

Kỹ năng của Dev thời AI không phải gõ code nhanh. Mà là thiết kế kiến trúc chuẩn để AI hiểu, rồi đọc và phản biện code AI viết ra. Dev không mất việc. Dev thành Kiến trúc sư.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Lưu ý chung:** IDE theme Dracula/One Dark Pro, font JetBrains Mono ≥18px, ẩn minimap và sidebar khi không cần, terminal prompt minimal.

| Scene | Narration | Type | Nội dung trên màn hình | Thời lượng |
|-------|-----------|------|------------------------|------------|
| 1 | Beat 1 — VẤN ĐỀ (cold open demo): "Đây là Earpiece AI..." → "...AI viết." | **[BROWSER]** | Google Meet mở. Side Panel Earpiece AI hiện bên cạnh. Audio phát → transcription chạy real-time → AI suggestion hiện ra. Chạy demo sống. Wow factor mạnh ngay đầu. | ~30s |
| 2 | Beat 2 — LEO THANG: "Bạn thử tự code MV3 đi..." → "...context kiến trúc của project bạn." | **[IDE]** → **[BROWSER]** → **[TERM]** | Quick cuts: (1) Code Service Worker — highlight chỗ không có `document`/`window`, (2) Offscreen Document setup — show `chrome.offscreen.createDocument` API, (3) `chrome.runtime.sendMessage` code — highlight chỗ dễ sai, (4) Stack Overflow page với câu trả lời cũ MV2, (5) AI chat trả lời sai — dùng deprecated API. | ~45s |
| 3 | Beat 3 — BƯỚC NGOẶT: "Và đó chính là bài học..." → "...không cho bản vẽ." | **[B-ROLL]** → **[DIAGRAM]** | 2s ambient (tay trên bàn phím). Chuyển sang sơ đồ đơn giản: "AI + No Context = Bug" vs "AI + Architecture = Correct Code". Có thể vẽ Excalidraw nhanh. | ~15s |
| 4 | Beat 4a — KHAI SÁNG (Master Prompt overview): "Thay vì bảo AI..." → "...Ba lớp rõ ràng." | **[IDE]** | Mở file Master Prompt (markdown hoặc text file). Scroll overview — show 3 sections rõ ràng: Context, Architecture, Edge Cases. Zoom nhẹ vào tiêu đề mỗi section. | ~15s |
| 5 | Beat 4b — KHAI SÁNG (Lớp 1 — Context): "Lớp một — Context..." → "...Nó không đoán mò nữa." | **[IDE]** | Mở `packages/shared/` → show type definitions, đặc biệt `IcMessage` interface. Highlight các message types. | ~20s |
| 6 | Beat 4c — KHAI SÁNG (Lớp 2 — Architecture): "Lớp hai — Architecture..." → "...qua một kênh duy nhất." | **[DIAGRAM]** | Sơ đồ kiến trúc 3 khối: `Side Panel UI` ↔ `Service Worker` ↔ `Offscreen Document`. Mũi tên chỉ luồng data. Label `IcMessage` trên mỗi mũi tên. Vẽ trong Excalidraw dark theme. | ~20s |
| 7 | Beat 4d — KHAI SÁNG (Lớp 3 — Edge cases): "Lớp ba — Edge cases..." → "...AI hay quên." | **[IDE]** → **[BROWSER]** | Show đoạn Master Prompt ghi về heartbeat/restart. Có thể flash qua Chrome docs page về Offscreen lifetime limits. | ~20s |
| 8 | Beat 5a — THÀNH QUẢ (AI generate): "Giờ tôi ném Master Prompt..." → "...nếu tự gõ tay." | **[IDE]** | Mở AI Agent (Cursor Composer / Windsurf). Paste Master Prompt. Tua nhanh (2-4x speed) cảnh AI generate files: tạo folders, viết `RecognitionSection.tsx`, Options Page, Service Worker, Offscreen Document. Show file tree mở rộng dần. Sau đó slow-mo mở từng file highlight: component dùng `packages/ui`, Tailwind classes, heartbeat code. | ~60s |
| 9 | Beat 5b — THÀNH QUẢ (Review & Debug): "Nhưng — và đây là phần quan trọng..." → "...Review lại. Xong." | **[IDE]** → **[TERM]** → **[BROWSER]** | (1) Mở file, đọc code, scroll check message types. (2) Terminal `pnpm dev`. (3) Chrome — test extension hoạt động. (4) Có lỗi (import icon) → copy error → paste vào AI chat → AI fix → save → chạy lại OK. Demo workflow Review → Approve → Fix rõ ràng. | ~50s |
| 10 | Beat 6 — Ý NGHĨA: "Kỹ năng của Dev thời AI..." → "...Dev thành Kiến trúc sư." | **[IDE]** → **[B-ROLL]** | Show toàn cảnh project tree hoàn chỉnh — tất cả files AI đã generate. Zoom out. 3s ambient: desk setup, monitor glow, city lights. Kết. | ~15s |

**Tổng: ~290s ≈ 4:50 narration + ~80–130s visual breathing/tua nhanh = ~6:30–7:00 phút runtime.**

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

**Prompt 1:**
A cinematic photograph of a developer sitting at a dramatic desk setup with AI code agent generating code on an ultrawide monitor, green and cyan neon syntax-highlighted code streaming across the screen like a waterfall, the developer leaning back with arms crossed watching the AI work, dark moody room with purple ambient backlighting, shallow depth of field, city bokeh lights through rain-streaked window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 2:**
A cinematic photograph of two glowing holographic hands — one human hand and one digital wireframe AI hand — both reaching toward a floating Chrome browser extension icon made of neon green code, dark void background with particles and fog, dramatic cyan and purple rim lighting, high contrast, shallow depth of field, 8k, photorealistic, like a developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 3:**
A cinematic photograph of a dark IDE screen showing an AI coding agent conversation on the left and generated React TypeScript code on the right, the entire screen reflecting on a glass desk surface, mechanical keyboard with neon green backlit keys in foreground slightly out of focus, dark moody atmosphere with monitor as the only light source, cinematic lighting, film grain, anamorphic lens flare, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Tôi CODE app phức tạp mà KHÔNG GÕ một dòng logic nào
2. AI code ngu? KHÔNG — bạn chưa biết cách ra lệnh
3. "Master Prompt" — bí mật khiến AI viết code ĐÚNG từ lần đầu
4. Dev KHÔNG mất việc vì AI — Dev THÀNH Kiến trúc sư
5. 1 prompt thay thế 1 tuần code tay — Vibe Coding thực chiến
6. Tôi bảo AI code Chrome Extension — kết quả KHÔNG NGỜ
7. Earpiece AI: app nghe lén phỏng vấn mà AI code trong 10 phút
8. Vibe Coding 101: lập trình BẰNG MỒM có thật không?
9. Service Worker + Offscreen Document: nỗi đau MV3 mà AI giải cứu
10. 3 lớp context biến AI từ "code ngu" thành "senior developer"

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — "KHÔNG GÕ / 1 DÒNG CODE"

**5a. Image prompt:**
A cinematic photograph, developer leaning back in gaming chair with arms crossed, smiling confidently, three monitors showing AI-generated code streaming in neon green on dark background, dramatic neon lighting in green and purple, code text floating from the screens into the air like particles, dark moody room with city bokeh through large window, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **KHÔNG GÕ** — WHITE `#FFFFFF`
- Line 2: **1 DÒNG CODE** — NEON GREEN `#00FF41`
- Badge line: **VIBE CODING** — WHITE text in dark badge box `#1a1a2e` with neon green border

**5c. Typography:**
- Canvas 1280×720. Font **Anton** for impact.
- Text block: each line ~130px height, line spacing 0.85. Text block left 1/3.
- Neon glow: duplicate text, blur 10px `#00FF41`, opacity 65%. Black stroke 8px on all letters.
- Scan-line noise overlay on background. Text does NOT overlap developer face.
- Recommend Canva typesetting for brand consistency.

### Option 2 — "AI CODE / NGU?"

**5a. Image prompt:**
A cinematic photograph, close-up dramatic shot of an AI coding agent interface on a dark monitor screen with a visible "Master Prompt" text document and streaming code output, neon green and cyan reflections on a glass desk surface, dramatic purple side lighting, a developer's hand hovering over the keyboard in foreground out of focus, dark moody background with fog effect, high contrast, dramatic rim lighting, deep shadows, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **AI CODE** — WHITE `#FFFFFF`
- Line 2: **NGU?** — NEON GREEN `#00FF41`
- Badge line: **MASTER PROMPT** — WHITE text in dark badge box `#1a1a2e` with neon green border

**5c. Typography:**
- Canvas 1280×720. Font **JetBrains Mono** for code-feel + provocation.
- Text block: each line ~140px height (larger — fewer words), line spacing 0.85. Text block left 1/3.
- Neon glow: duplicate, blur 12px `#00FF41`, opacity 70%. Black stroke 10px.
- Scan-line overlay. "NGU?" should feel like it punches out of the screen.
- Recommend Canva typesetting.

### Option 3 — "DEV = / KIẾN TRÚC SƯ"

**5a. Image prompt:**
A cinematic photograph, dramatic silhouette of a developer standing in front of a massive curved monitor wall displaying architectural diagrams and flowing code in neon green and cyan, arms spread wide like conducting an orchestra, dark moody environment with purple and green neon strips on walls, reflective dark floor showing the glow, high contrast, dramatic rim lighting from behind, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **DEV =** — WHITE `#FFFFFF`
- Line 2: **KIẾN TRÚC SƯ** — NEON GREEN `#00FF41`
- Badge line: **AI THỜI ĐẠI** — WHITE text in dark badge box `#1a1a2e` with neon green border

**5c. Typography:**
- Canvas 1280×720. Font **Anton** for maximum impact.
- Text block: each line ~130px height, line spacing 0.85. Text block left 1/3.
- Neon glow: duplicate, blur 10px `#00FF41`, opacity 65%. Black stroke 8px.
- Scan-line noise overlay. Silhouette on right, text on left — clean separation.
- Recommend Canva typesetting for brand consistency across series.
