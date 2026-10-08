# EP01 — Khám phá Boilerplate Chrome Extension "bá đạo" nhất

## YOUTUBE METADATA

### Title (chọn 1 trong 10 bên dưới)
**Recommended:** Cái "móng nhà" 4000⭐ BIẾN tôi thành Kiến trúc sư Chrome Extension

### Description (copy paste khi upload)
```
Setup Chrome Extension bằng Vanilla JS? Webpack config rối nùi? HMR không có? Quên đi.

Trong video này, tôi chia sẻ cái boilerplate đã thay đổi hoàn toàn cách tôi làm Chrome Extension — từ code rời rạc sang kiến trúc Monorepo chuẩn chỉnh với React 18, Vite, Turborepo và TailwindCSS. Cái "móng nhà" mà AI Agent thực sự hiểu và generate code chuẩn.

🔗 Boilerplate: https://github.com/nicolestandifer3/nicolestandifer3-chrome-extension-boilerplate-react-vite
🔗 Source code demo: [link repo của bạn]

⏱️ Timestamps:
0:00 — Nỗi đau setup Chrome Extension
0:40 — Thử đủ cách và đều thất bại
1:15 — Bước ngoặt: Monorepo
1:35 — AI scan toàn bộ codebase
2:00 — Deep-dive kiến trúc theo output AI
4:10 — Demo HMR trực tiếp
5:20 — Kết: Móng nhà xịn, AI mới cất cánh

📌 Series "Vibe Coding Chrome Extensions":
▸ EP01: Boilerplate "bá đạo" nhất (video này)
▸ EP02: Vibe Coding — Code app AI bằng mồm! (coming soon)

💬 Bạn đang dùng boilerplate nào cho Chrome Extension? Comment cho tôi biết!

#ChromeExtension #React #Vite #Turborepo #ManifestV3 #VibeCoding #LapTrinhLaCuocSong #WebDev #Developer #Monorepo #TypeScript #TailwindCSS #HMR #BoilerplateCode
```

### Tags (paste vào YouTube Studio)
```
chrome extension,chrome extension tutorial,manifest v3,react chrome extension,vite chrome extension,turborepo,monorepo,boilerplate,hmr,hot module replacement,vibe coding,lập trình,typescript,tailwindcss,chrome extension boilerplate react vite,web development,developer,coding,chrome extension manifest v3,react vite,lập trình là cuộc sống
```

### Upload Settings
- **Visibility:** Public
- **Category:** Science & Technology
- **Language:** Vietnamese
- **Playlist:** Vibe Coding Chrome Extensions

---

## PART 1 — SCRIPT

Bạn mở Chrome Extension docs lên. Manifest V3. Rồi bắt đầu setup Webpack. Config xong file này, lại phải config file khác. Vanilla JS, `document.createElement` hàng chục dòng chỉ để tạo một cái nút bấm.

Sửa một dòng chữ — reload nguyên cái extension. Sửa thêm — reload lại. Vòng lặp vô tận.

Bạn thử dùng Parcel. Config nhẹ hơn, nhưng build extension vẫn lỗi manifest. Chuyển sang Webpack 5 — plugin `CopyWebpackPlugin` xung đột với `chrome.runtime`. Thử CRX CLI — cũng bỏ cuộc vì thiếu React support.
Chưa kể, con AI bạn đang xài — bạn bảo nó viết Vanilla JS thao tác DOM — nó "ngáo" liên tục. Vì AI thời này sinh ra để viết React, viết TypeScript. Bắt nó viết `document.querySelector` chồng chéo là nó tự bịa bug.

Rồi tôi tìm được một thứ thay đổi tất cả. Không phải framework mới. Không phải tool mới. Mà là một cái "móng nhà" — một Monorepo đã thiết kế sẵn mọi thứ bạn cần.

Đây là repo `chrome-extension-boilerplate-react-vite` trên GitHub. Hơn bốn ngàn sao. Nhưng hàng trăm file — bắt đầu đọc từ đâu?

Tôi mở project trong VS Code, bật Antigravity lên, paste một câu: "Scan toàn bộ codebase này, giải thích cho tôi như senior dev đang onboard junior." Vài giây — bản phân tích kiến trúc hiện ra.

AI chỉ ra đây là Monorepo dùng Turborepo — code chia thành nhiều package riêng biệt, giống tòa nhà có từng tầng, từng phòng rõ ràng. Tôi dẫn bạn đi theo output của nó.

Folder `chrome-extension` — AI gọi đây là "linh hồn". File `manifest.ts` nằm ở đây. Mọi quyền hạn, background worker, content script đều khai báo tại chỗ này.

Folder `pages` — giao diện UI. Có sẵn `popup`, `options`, `side-panel`, `new-tab`. Muốn thêm trang — tạo folder, viết React component, xong.

Folder `packages` — code dùng chung. AI phân tích từng cái: `shared` chứa TypeScript types, `ui` chứa component library, `storage` wrap Chrome Storage API, `hmr` lo Hot Module Replacement. Import từ package, không duplicate.

Và đây là insight quan trọng nhất AI chỉ ra: khi bạn cho AI Agent đọc `packages/shared`, nó hiểu ngay type system. Nó biết message nào được phép gửi, data shape ra sao. AI không đoán mò — nó code theo luật bạn đặt.

Giờ chạy thử. `pnpm run dev`. Mở extension trong Chrome. Tôi đổi màu cái nút từ xanh sang đỏ. Ấn save. Trình duyệt tự update. Không F5. Không reload extension. Hot Module Replacement trong Chrome Extension.

Bạn sửa text trong popup — update ngay. Đổi layout trong side panel — update ngay. Cảm giác như đang code web app bình thường, không phải đang code extension.

Đây mới là điểm mấu chốt: có "móng nhà" chuẩn, AI mới xây được "biệt thự". Ở video tiếp theo, tôi sẽ dùng chính cái codebase này, kết hợp với AI Agent, để Vibe Coding ra một app cực kỳ phức tạp — Earpiece AI — chỉ bằng cách mô tả kiến trúc cho AI.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Lưu ý chung:** IDE theme Dracula/One Dark Pro, font JetBrains Mono ≥18px, ẩn minimap và sidebar khi không cần, terminal prompt minimal.

| Scene | Narration | Type | Nội dung trên màn hình | Thời lượng |
|-------|-----------|------|------------------------|------------|
| 1 | Beat 1 — VẤN ĐỀ: "Bạn mở Chrome Extension docs lên..." → "...vòng lặp vô tận." | **[BROWSER]** → **[IDE]** | Mở Chrome Extension docs (MV3). Lướt qua 1 file `content_script.js` vanilla dài ngoằng với `document.createElement`. Highlight đoạn code rối. Sau đó cắt sang terminal `npm run build` → phải F5 reload extension. | ~40s |
| 2 | Beat 2 — LEO THANG: "Bạn thử dùng Parcel..." → "...nó tự bịa bug." | **[IDE]** → **[TERM]** | Quick cuts: (1) Parcel config → build error manifest, (2) Webpack 5 config → CopyWebpackPlugin error, (3) Cursor/AI chat — paste prompt "viết vanilla JS DOM manipulation" → AI output code dài, highlight chỗ sai. | ~35s |
| 3 | Beat 3 — BƯỚC NGOẶT: "Rồi tôi tìm được..." → "...mọi thứ bạn cần." | **[B-ROLL]** → **[BROWSER]** | Cảnh tay gõ bàn phím (2s ambient). Chuyển sang mở GitHub repo page — show tên repo, star count, tech stack badges. | ~20s |
| 4 | Beat 4a — KHAI SÁNG (AI scan): "Đây là repo..." → "...kiến trúc hiện ra." | **[BROWSER]** → **[IDE]** | GitHub repo — show tên, star count (5s). Chuyển sang VS Code đã mở project. **Bật Antigravity chat panel** (sidebar hoặc Cmd+Shift+P). Paste prompt: _"Scan toàn bộ codebase này, giải thích cho tôi như senior dev đang onboard junior."_ AI bắt đầu output — để camera quay lúc text đang chạy ra, scroll nhẹ cho viewer thấy AI đang phân tích. **Đây là cảnh "wow" — AI đọc hàng trăm file trong vài giây.** | ~25s |
| 5 | Beat 4b — KHAI SÁNG (AI-guided tour): "AI chỉ ra đây là Monorepo..." → "...không duplicate." | **[IDE]** | VS Code **split view**: Antigravity output panel bên phải, file tree bên trái. Host đọc output AI và **đồng thời click explore** folder tương ứng: (1) AI nhắc `chrome-extension/` → host expand, mở `manifest.ts` (2) AI nhắc `pages/` → host expand sub-folders popup/options/side-panel (3) AI nhắc `packages/` → host mở từng sub-package: shared, ui, storage, hmr. **Hiệu ứng: AI giải thích + host verify live = workflow "AI nói, mình kiểm".** ~5s mỗi folder. | ~65s |
| 6 | Beat 4c — KHAI SÁNG (AI insight): "Và đây là insight..." → "...code theo luật bạn đặt." | **[IDE]** → **[DIAGRAM]** | **Highlight đoạn AI output** nói về `packages/shared` và type system (dùng chuột bôi đen hoặc zoom). Mở file type definitions trong `packages/shared` để **verify AI nói đúng**. Overlay sơ đồ đơn giản: `shared types` → AI Agent reads → code chuẩn. | ~20s |
| 7 | Beat 5 — THÀNH QUẢ (HMR demo): "Giờ chạy thử..." → "...không phải đang code extension." | **[TERM]** → **[BROWSER]** → **[IDE]** | Terminal gõ `pnpm run dev`. Mở Chrome → load extension. IDE: sửa màu button (xanh→đỏ), ấn Save → Chrome auto-update. Sửa text popup → update. Sửa layout side-panel → update. Camera lật qua lật lại IDE ↔ Chrome để thấy HMR live. | ~50s |
| 8 | Beat 6 — Ý NGHĨA + teaser: "Đây mới là điểm mấu chốt..." → "...mô tả kiến trúc cho AI." | **[IDE]** → **[B-ROLL]** | Show toàn cảnh project tree đã mở (visual recap). Cuối cùng: flash 2s preview Earpiece AI side panel UI (teaser cho EP02). | ~15s |

**Tổng: ~270s ≈ 4:30 phút narration + ~60–90s visual breathing = ~5:30–6:00 phút runtime.**

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

**Prompt 1:**
A cinematic photograph of a developer's hands on a mechanical keyboard with neon green and cyan code reflecting off the keycaps, a large ultrawide monitor showing a dark IDE with a Monorepo folder structure glowing in syntax-highlighted colors, dark moody room with warm amber desk lamp, coffee cup steaming, city bokeh lights through window, shallow depth of field, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 2:**
A cinematic photograph of a glowing architectural blueprint overlaid on a dark code editor screen, neon green wireframe lines forming a Chrome browser icon shape, purple and cyan accent lights, dark moody background with fog, the blueprint hovering in mid-air above a desk with monitor and keyboard, dramatic rim lighting, shallow depth of field, 8k, photorealistic, like a developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 3:**
A cinematic photograph of a dark developer desk setup from above at 45-degree angle, ultrawide monitor displaying a vibrant dark IDE with folder tree and React component code in green and cyan syntax highlighting, mechanical keyboard with RGB lighting, Chrome Extension icon glowing on a second smaller monitor, neon purple ambient light from behind, city rain on window in background, cinematic lighting, film grain, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Cái "móng nhà" 4000⭐ BIẾN tôi thành Kiến trúc sư Chrome Extension
2. Tôi BỎ Webpack và không bao giờ quay lại — Chrome Extension Setup đỉnh nhất
3. Chrome Extension + React + Vite: Boilerplate mà DEV nào cũng nên biết
4. Tại sao 90% DEV setup Chrome Extension SAI từ đầu?
5. 1 Monorepo thay đổi cách tôi code Chrome Extension mãi mãi
6. Chrome Extension mà code như Web App? Đây là cách
7. HMR trong Chrome Extension — trải nghiệm KHÔNG THỂ QUAY LẠI
8. Repo GitHub 4000⭐ đã "cứu" dự án Chrome Extension của tôi
9. AI code GIỎI hay DỞ — phụ thuộc vào cái "móng nhà" bạn đặt
10. Đừng code Chrome Extension từ đầu — hãy dùng cái NÀY

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — "ĐỪNG SETUP / TỪ ĐẦU"

**5a. Image prompt:**
A cinematic photograph, developer silhouette sitting at a dramatic coding setup with three monitors, dramatic neon lighting in green and cyan, Chrome browser logo and React logo floating in the air as glowing holograms, dark moody background with city bokeh and rain on window, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **ĐỪNG SETUP** — WHITE `#FFFFFF`
- Line 2: **TỪ ĐẦU** — NEON GREEN `#00FF41`
- Badge line: **CHROME EXTENSION** — WHITE text in dark badge box `#1a1a2e` with neon green border

**5c. Typography:**
- Canvas 1280×720. Font **Anton** for impact.
- Text block: each line ~130px height, line spacing 0.85. Text block left 1/3 of frame.
- Neon glow: duplicate text, blur 10px in `#00FF41`, opacity 65%. Black stroke 8px on all letters.
- Scan-line noise overlay on background. Text does NOT overlap silhouette.
- Recommend Canva typesetting for brand consistency.

### Option 2 — "MÓNG NHÀ / 4000 ⭐"

**5a. Image prompt:**
A cinematic photograph, dramatic overhead shot of a developer desk with mechanical keyboard and ultrawide monitor showing a glowing Monorepo folder tree structure in neon green on dark background, code text floating upward from the screen like particles, dramatic purple and cyan accent neon lighting from sides, dark moody room with fog, high contrast, deep shadows, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **MÓNG NHÀ** — WHITE `#FFFFFF`
- Line 2: **4000 ⭐** — NEON GREEN `#00FF41`
- Badge line: **BOILERPLATE** — WHITE text in dark badge box `#1a1a2e` with neon green border

**5c. Typography:**
- Canvas 1280×720. Font **JetBrains Mono** for code-feel.
- Text block: each line ~120px height, line spacing 0.85. Text block left 1/3.
- Neon glow: duplicate, blur 10px `#00FF41`, opacity 65%. Black stroke 8px.
- Scan-line overlay. Text clear of key visual elements.
- Recommend Canva typesetting.

### Option 3 — "AI CẦN / KIẾN TRÚC"

**5a. Image prompt:**
A cinematic photograph, close-up of a developer's face illuminated only by monitor glow showing Chrome Extension code in green and cyan syntax highlighting, reflection of code visible on eyeglasses, neon purple rim light on one side of face, dark moody background completely black, high contrast, dramatic rim lighting, deep shadows, vivid neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9, cinematic lighting, film grain, anamorphic lens flare. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **AI CẦN** — WHITE `#FFFFFF`
- Line 2: **KIẾN TRÚC** — NEON GREEN `#00FF41`
- Badge line: **VIBE CODING** — WHITE text in dark badge box `#1a1a2e` with neon green border

**5c. Typography:**
- Canvas 1280×720. Font **Anton** for impact.
- Text block: each line ~130px height, line spacing 0.85. Text block left 1/3.
- Neon glow: duplicate, blur 12px `#00FF41`, opacity 70%. Black stroke 8px.
- Scan-line noise overlay. Text does NOT overlap face/glasses.
- Recommend Canva typesetting for brand consistency across series.

---

## PROMPT — SCAN CODEBASE (dùng trong Antigravity)

> Paste prompt bên dưới vào Antigravity khi đã mở workspace chứa boilerplate. Antigravity sẽ scan toàn bộ codebase và giải thích chi tiết.

```
Tôi vừa clone repo "chrome-extension-boilerplate-react-vite" về máy.
Hãy scan toàn bộ codebase này và giải thích cho tôi — như một senior dev
đang onboard junior vào dự án. Cụ thể:

1. **Kiến trúc tổng quan:**
   - Đây là Monorepo hay Polyrepo? Dùng tool gì để quản lý (Turborepo, Lerna, Nx...)?
   - Vẽ sơ đồ cây thư mục cấp 1-2, chú thích mỗi folder/package làm gì.
   - Các package phụ thuộc lẫn nhau như thế nào? (dependency graph)

2. **Manifest V3 — "linh hồn" extension:**
   - File manifest nằm ở đâu? Cấu trúc ra sao?
   - Permissions nào được khai báo mặc định? Tại sao?
   - Background service worker, content scripts, popup, side panel —
     mỗi thứ được wire vào manifest như thế nào?

3. **Từng package/page quan trọng:**
   - `chrome-extension/` — vai trò, file chính, entry points.
   - `pages/popup/`, `pages/side-panel/`, `pages/options/`, `pages/new-tab/`
     — mỗi page build bằng gì (React? Vanilla?), entry file nào, 
     và output đi đâu khi build?
   - `packages/shared/` — chứa gì? Types, utils, constants? 
     Giải thích 2-3 file quan trọng nhất.
   - `packages/ui/` — component library gồm những gì?
     Cách import từ page khác ra sao?
   - `packages/storage/`, `packages/hmr/`, `packages/tailwind-config/`,
     `packages/tsconfig/` — mỗi package giải quyết vấn đề gì?

4. **Build system & Dev workflow:**
   - Vite config hoạt động thế nào cho extension? 
     (khác gì so với Vite cho web app thông thường?)
   - Turborepo orchestrate build/dev ra sao? 
     File `turbo.json` có gì đặc biệt?
   - HMR (Hot Module Replacement) hoạt động thế nào trong context 
     Chrome Extension? (đây là phần "ma thuật" — giải thích kỹ)
   - `pnpm` workspace config nằm đâu, cấu trúc ra sao?

5. **Data flow & Communication:**
   - Popup ↔ Background ↔ Content Script giao tiếp bằng cách nào?
     (chrome.runtime.sendMessage? Shared types?)
   - Storage API được wrap như thế nào trong `packages/storage`?
   - Có pattern nào cho type-safe messaging giữa các phần không?

6. **Điểm hay & Điểm cần lưu ý:**
   - 3 điểm kiến trúc "đỉnh" nhất mà junior nên học từ repo này.
   - 2-3 "gotchas" hoặc điểm dễ nhầm khi bắt đầu customize.
   - Repo này thiếu gì mà production-ready extension sẽ cần thêm?

Format output: dùng heading rõ ràng, code block khi cần, 
và giải thích mỗi concept bằng 1-2 câu đơn giản trước khi đi sâu.
Đừng liệt kê khô khan — hãy giải thích TẠI SAO mỗi thứ tồn tại.
```
