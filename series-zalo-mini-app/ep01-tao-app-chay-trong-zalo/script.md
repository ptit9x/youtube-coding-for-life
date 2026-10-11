# EP01 — Một chiều ra app chạy trong Zalo | Zalo Mini App #1

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~8–9 phút (premiere, đã được chấp nhận dài hơn tập thường)
- **Word count PART 1:** [điền sau khi check]
- **Repo app:** `/home/vmo/vibe-coding/gap-them` (tạo trong tập này)
- **CLI probe thật (10/2026):** Node v26.7.0, `create-zalo-mini-app` 1.0.4 → cài `zmp-cli` 4.0.3; prompt đầu tiên của CLI là `Mini App ID:`

## Gap table (research 10/2026)

| Nguồn | Hình thức | Lỗ hổng series khai thác |
|---|---|---|
| miniapp.vn, wifim.vn, cnv.vn | Marketing agency | Không có code, không dạy |
| GitHub zaui-shop / mini-zalo-demo | Template + README | Có code, không có hành trình; fork 2023–2025 |
| Docs Zalo (mini.zalo.me) | Text tiếng Việt | Không phải video, không AI workflow, không có cảnh duyệt/publish thật |
| YouTube VN | — | Không tìm thấy series vibe-code Mini App từ số 0 đến live (re-verify khi đăng) |

Khác biệt của tập này: mở màn bằng app chạy trong Zalo THẬT trên điện thoại thật; fact mới 2026 (xác thực chủ sở hữu, prompt CLI hỏi Mini App ID); AI là mentor theo 6 bước.

---

## PART 1 — SCRIPT

Quán cơm nhà mình vừa có app riêng. Khách mở Zalo, quét mã, đặt bàn trong ba mươi giây. Không cần App Store. Không cần Google Play. Chi phí nền tảng: không đồng.

Chào bạn, đây là Lập trình là cuộc sống, và đây là tập đầu của một mùa mới. Mùa này mình làm một thứ rất Việt Nam: Mini App chạy ngay trong Zalo, cho quán ăn nhà mình. Làm thật, sai thật, và quay lại toàn bộ.

Nếu bạn search hướng dẫn làm Mini App, bạn gặp hai thứ. Trang bán dịch vụ của agency. Hoặc tài liệu tiếng Anh dài của Zalo. Mà tài liệu đó vừa đổi. Từ tháng Mười năm ngoái, mọi app phải xác thực chủ sở hữu trước khi phát hành. Tutorial cũ không còn đúng. Nên mình làm series này.

Một điều nói trước. Mình không code một mình, mình đi cùng AI. Nhưng AI không làm hộ. Mình yêu cầu, AI lên kế hoạch, mình đọc từng dòng, duyệt, rồi mới cho code. Không giải thích lại được, coi như chưa hiểu.

Ba mươi giây lý thuyết trước khi bấm. Mini App Zalo bản chất là trang web, gói dưới mười megabyte, chạy trong Zalo. Nó giống gian hàng trong trung tâm thương mại. Bạn không xây tòa nhà, không lo bảo vệ, không lo tiền điện. Trung tâm lo hết, và khách ai cũng đi ngang. Cái giá là nội luật. Zalo duyệt mọi app trước khi lên kệ. Và chủ shop phải khai danh tính. Cá nhân thì Zalo đã định danh eKYC là xong ngay, như mình. Doanh nghiệp hoặc hộ kinh doanh thì nộp giấy phép, chờ ba đến năm ngày làm việc. Quán nhà mình chưa có hộ kinh doanh, nên mùa này đi đường cá nhân. Khi làm thanh toán trong app thì buộc phải lên hộ kinh doanh. Bảng so sánh mình để trên màn hình, bạn pause chụp lại.

Giờ là tay chân. Việc đầu tiên không phải code, mà là giấy tờ. mini.zalo.me, đăng nhập bằng Zalo đã định danh, bấm tạo Mini App. Tên: Gắp Thêm. Danh mục: Ẩm thực. Icon: đôi đũa. Dashboard trả lại một dãy số, Mini App ID. Đây là giấy khai sinh của app, giữ kỹ.

Vì sao giữ kỹ? Mở terminal ra là biết. Node hai mươi sáu, một lệnh duy nhất: npx create-zalo-mini-app. CLI tự cài. Và prompt đầu tiên không hỏi tên project. Nó hỏi Mini App ID. Không có ID từ dashboard, bạn đứng chết ngay ở dòng này. Dán ID vào, chọn template có sẵn giỏ hàng, TypeScript, Tailwind. Đoạn cài dependencies mình cắt nhé, không ai cần xem thanh tải ba phút. Xong: npm start. Trình duyệt mở localhost ba nghìn. Nhưng đó mới là web. Hôm nay cần mở trong Zalo. CLI đưa mã QR, điện thoại quét một cái. Và đây: quán Gắp Thêm, chạy trong Zalo thật, trên điện thoại thật. Buổi chiều đầu tiên, đếm bằng phút.

Giờ đến mentor. Mình mở Antigravity, một IDE miễn phí, agent Opus nằm bên phải. Mình prompt tiếng Việt cho bạn dễ theo dõi. Làm thật thì prompt tiếng Anh rẻ hơn. Mình gửi spec quán: menu, đặt bàn, gọi món trước, voucher, blog. Kèm luật: trình plan trước, chờ mình duyệt, chưa đụng file. Opus trả lại bản plan rất hoành tráng. Thanh toán, giao hàng, tích điểm, đầy đủ hết. Đọc kỹ thì hợp lý, cho một nhà hàng. Nhưng quán mẹ mình có ba cái bàn. Thanh toán mùa sau. Giao hàng mùa sau. Tích điểm, nữa nữa. Mình cắt, và duyệt phần còn lại.

Nhìn lại màn hình, mình vừa chạy quy trình chuẩn của cả series. Một: yêu cầu kèm context. Hai: AI lên plan. Ba: mình review. Bốn: duyệt. Năm: AI code. Sáu: kiểm chứng bằng git diff và chạy app. Sáu bước này lặp lại trong mọi tập. AI không bao giờ tự ý sửa code của mình.

Kết tập một. Trên tay: app thật trên dashboard, mở được trong Zalo qua QR, và một plan đã duyệt. Chi phí: không đồng. Thời gian: một buổi chiều. Nhưng menu đang nằm trong file json cứng của template. Sửa một cái giá, phải build lại app. Tập hai mình dọn menu vào database thật. Sửa giá trên điện thoại, menu tự đổi. Làm theo cùng mình thì lưu kênh, hẹn tập sau.

---

## PART 2 — SHOT LIST

Tiêu chí cắt ghép của series: KHÔNG quay trực tiếp thời gian chờ (install, gen code) — time-lapse 3–5s. Giữ nguyên thời lượng thật của: prompt gõ, plan review, git diff, moment app chạy. IDE dark theme, font ≥18px.

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | Màn hình điện thoại thật: mở Zalo → vào "Gắp Thêm" → đặt bàn 30 giây, kết ở màn hình xác nhận | Beat 0 (4 câu đầu) | 45 |
| 2 | [B-ROLL] | Bàn làm việc đêm, cà phê, gõ phím; overlay logo kênh + "MÙA MỚI" | Chào kênh + giới thiệu mùa | 25 |
| 3 | [BROWSER] | Tab search Google "hướng dẫn làm zalo mini app": kết quả agency + docs Zalo; scroll nhanh | Gap (tutorial cũ/không có) | 30 |
| 4 | [DIAGRAM] | Sơ đồ Excalidraw: web 10MB → webview trong Zalo → CDN; metaphor gian hàng trong TTTM; 3 nút: kiểm duyệt / permission / xác thực chủ sở hữu | 30 giây lý thuyết (phần 1) | 35 |
| 5 | [DIAGRAM] | Bảng so sánh Cá nhân vs DN/HKD (xác thực, thời gian chờ, khi nào bắt buộc HKD) — hiện 6–7 giây, không đọc hết | "Bảng so sánh mình để trên màn hình..." | 20 |
| 6 | [BROWSER] | mini.zalo.me: đăng nhập → tạo app → điền tên "Gắp Thêm" + danh mục Ẩm thực + upload icon → xong; ZOOM vào Mini App ID | "Giờ là tay chân... giữ kỹ" | 50 |
| 7 | [TERM] | Terminal: gõ `npx create-zalo-mini-app gap-them`; prompt đầu hiện `? Mini App ID:` — hover/zoom dòng này; dán ID; chọn template e-commerce, TS, Tailwind | "Vì sao giữ kỹ?..." | 40 |
| 8 | [TERM] | TIME-LAPSE 3–5s install + `npm start`; trình duyệt tự mở localhost:3000 hiện quán demo | "Đoạn cài dependencies mình cắt..." | 15 |
| 9 | [PHONE] | Quét QR preview bằng Zalo → app "Gắp Thêm" mở trong Zalo thật; lướt menu demo | "Và đây: quán Gắp Thêm..." | 25 |
| 10 | [IDE] | Antigravity mở repo: agent panel Opus bên phải; host DÁN prompt spec (Prompt 1, xem code/prompt-spec-quan.md); bấm gửi | "Giờ đến mentor... chưa đụng file" | 40 |
| 11 | [IDE] | Plan của Opus hiện ra; host scroll, highlight mục thanh toán/giao hàng/tích điểm; gõ thêm yêu cầu cắt scope; status đổi "approved" | "Opus trả lại bản plan hoành tráng..." | 55 |
| 12 | [DIAGRAM] | Graphic 6 bước workflow (số 1→6, vòng lặp) — làm 1 lần dùng lại cả series | "Nhìn lại màn hình..." | 45 |
| 13 | [IDE] | Terminal repo: `git log --oneline` (commit scaffold + plan); mở file plan đã duyệt | "Kết tập một. Trên tay..." | 20 |
| 14 | [BROWSER] | Mở file `mock/products.json` của template — scroll giá món; freeze frame + mũi tên đỏ vào một cái giá | "Menu đang nằm trong file json cứng..." | 15 |
| 15 | [B-ROLL] | Closings: điện thoại đặt bàn + laptop; overlay "TẬP 2: MENU THẬT" | Teaser + CTA lưu kênh | 20 |

**Tổng: 425 giây ≈ 7,1 phút hình.** Thoại ~800 từ @ ~95–100 wpm ≈ 8–8,5 phút — phần dư là khoảng thở của scene 1, 9, 12 (visual carries). Tổng runtime thực tế dự kiến **8–9 phút**.

**Batch-record gợi ý:** scene 3+6 một phiên browser; scene 7+8+13 một phiên terminal; scene 1+9 một phiên phone (quay lại sau khi scaffold xong thật); scene 10+11 một phiên IDE.

---

## Prompt cho Opus (Prompt 1 — scene 10–11, gõ verbatim)

Lưu tại `code/prompt-spec-quan.md`:

```
Bối cảnh: mình đang làm Zalo Mini App cho quán cơm gia đình nhỏ (tên Gắp Thêm),
quay series YouTube. Project vừa scaffold từ template e-commerce của zmp-cli
(React + TypeScript + Tailwind + ZaUI), chưa sửa gì. Backend dự kiến Supabase.

Nhiệm vụ: lên plan sản phẩm cho v1 gồm: xem menu, đặt bàn, gọi món trước
(pre-order), voucher, blog, tab admin ẩn cho chủ quán.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file. Plan phải nêu:
scope từng mảng, bảng dữ liệu cần, rủi ro, thứ tự triển khai đề xuất.
Cuối cùng gợi ý phần nào nên cắt khỏi v1 cho một quán 3 bàn.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS (Flow / Nano Banana 2)

1. `A cinematic photograph of a young Vietnamese developer at a dark desk at night holding a smartphone that shows a food ordering app, dramatic Zalo blue neon lighting, a second monitor with code in blue and cyan syntax highlighting on dark background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of a hand holding a phone scanning a glowing blue QR code floating above a mechanical keyboard, dark moody room lit by monitor glow, food app interface faintly reflecting on glasses nearby, vivid saturated blue and cyan accents on deep navy background, high contrast, 8k, photorealistic, developer documentary style. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic close-up photograph of a dark IDE screen showing a React component with neon blue syntax highlighting, a bowl of rice and chopsticks beside the keyboard illuminated by monitor glow, night coding session mood, shallow depth of field, subtle film grain, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #1: Một buổi chiều ra app cho quán nhà mình | Lập trình là cuộc sống`
2. `Zalo Mini App #1: App chạy trong Zalo, 0 đồng nền tảng | Lập trình là cuộc sống`
3. `Zalo Mini App #1: Không cần App Store, quán cơm có app riêng | Lập trình là cuộc sống`
4. `Zalo Mini App #1: Từ số 0 đến app mở trong Zalo thật | Lập trình là cuộc sống`
5. `Zalo Mini App #1: Vibe coding app thật cho quán ăn | Lập trình là cuộc sống`

### 4b. SEO Description

```
Quán cơm nhà mình vừa có app riêng — chạy ngay trong Zalo, không cần App Store, 0 đồng chi phí nền tảng. Tập 1 của series "Vibe Zalo Mini App": mình làm app thật cho quán ăn nhà mình và quay lại toàn bộ.

✅ Mini App Zalo là gì: web app < 10MB chạy trong webview Zalo
✅ Tạo app trên mini.zalo.me đúng quy trình mới 2026 (xác thực chủ sở hữu: cá nhân = eKYC xong ngay)
✅ Scaffold bằng zmp-cli: vì sao prompt đầu tiên hỏi Mini App ID
✅ Preview app trong Zalo THẬT bằng QR
✅ AI lên plan sản phẩm, host review và cắt scope v1
✅ Quy trình 6 bước: Yêu cầu → Plan → Review → Approve → Code → Kiểm chứng

Links:
- Zalo Mini App docs: https://mini.zalo.me/docs
- Template zaui-shop: https://github.com/Zalo-MiniApp/zaui-shop
- IDE trong series: Antigravity (miễn phí)

Timestamps:
00:00 Quán nhà mình có app riêng
00:45 Mùa mới: Mini App cho quán ăn
01:15 Tutorial cũ đã lỗi thời
01:45 AI là mentor, không phải người làm hộ
02:05 Mini App là gì (30 giây)
03:05 Tạo app + Mini App ID
04:10 zmp-cli: prompt đầu tiên hỏi gì
05:00 Lần đầu mở app trong Zalo thật
05:25 AI lên plan + cắt scope
06:50 Quy trình 6 bước của series
07:35 Kết tập 1 + teaser tập 2

#ZaloMiniApp #Zalo #MiniApp #vibecoding #laptrinh #AI #React #TypeScript #LapTrinhLaCuocSong #zmpcli #Supabase #indiedev
```

### 4c. Keywords

```
zalo mini app, huong dan zalo mini app, lam app tren zalo, vibe coding, vibe coding tieng viet, zalo mini app tutorial, zmp-cli, zaui, lap trinh zalo mini app, tao mini app zalo, app dat mon zalo, app dat ban nha hang, mini app quán ăn, react typescript, ai coding agent, ai lam app, antigravity ide, opus ai, supabase, hoc lap trinh voi ai, lap trinh la cuoc song, developer viet nam, app khong can cai dat, zalo developer, mini app la gi
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity series: Zalo blue `#0068FF` + trắng `#FFFFFF` + đen/navy. Bố cục: chữ lớn trái, dev/phải 35–40%, màn hình code nền phụ. Badge `#01` góc trên phải — góc cố định cả series.

### Option 1 — "QUÁN NHÀ MÌNH / CÓ APP / RIÊNG"
- Image: Prompt 1 (Part 3).
- Text: `QUÁN NHÀ MÌNH` (trắng) / `CÓ APP RIÊNG` (Zalo blue `#0068FF`, chữ "APP" là shock word) + badge nhỏ `#01` nền `#1a1a2e` viền blue.

### Option 2 — "KHÔNG CẦN / APP STORE"
- Image: Prompt 2 (Part 3).
- Text: `KHÔNG CẦN` (trắng) / `APP STORE` (blue `#0068FF`) + badge `0 ĐỒNG` nhỏ dưới, nền tối viền blue.

### Option 3 — "MỘT CHIỀU / RA APP"
- Image: Prompt 3 (Part 3).
- Text: `MỘT CHIỀU` (trắng) / `RA APP` (blue `#0068FF`) + badge `#01`.

### Typography specs (mọi option, Canva)
- Canvas 1280×720; font **Anton** (hoặc JetBrains Mono cho badge); dấu tiếng Việt chuẩn.
- Mỗi dòng 15–20% chiều cao khung (~110–140px), line spacing 0,85, khối chữ chiếm ~1/3 khung bên trái.
- Stroke đen 6–10px mỗi chữ; glow: nhân đôi layer chữ, blur 8–12px màu blue, opacity 60–70%.
- Không đè chữ lên mặt người/chi tiết chính; overlay scan-line mỏng cho chất tech.
- Kiểm tra bản thu nhỏ 320×180 trước khi chốt.
