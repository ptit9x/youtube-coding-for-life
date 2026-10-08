# EP02 — Trải Nghiệm Muse AI Trên Mac: Code Review, Connectors & Sự Thật

---

## PART 1 — SCRIPT

Video trước mình đã hướng dẫn bạn đăng ký Muse AI, nhận một tỷ token. Giờ câu hỏi thật: nó code được không? Mình vừa cài App Muse trên Mac, và thử luôn.

Cùng xem Muse code như thế nào nhé.

Đầu tiên, mình chuẩn bị sẵn một prompt review code bằng Chát-gi-pi-ti. Prompt yêu cầu Muse quét toàn bộ dự án React cộng Supabase, tìm lỗi bảo mật, code smell, và đề xuất plan fix. Dán prompt vào, submit.

Và đây — Muse reaction tin nhắn của mình bằng emoji. Hàng Facebook có khác. Cái này vừa hay vừa hơi rợn, y như video trước mình nói.

Nhưng khoan. Nó báo App không có quyền đọc ghi file. Vào Settings, bật quyền đọc ghi cho nó.

Xong. Chat lại để nó tiếp tục.

Chờ khá lâu. Nói thật, response của Muse chậm hơn mấy AI mình quen dùng. Nhưng cứ chờ.

OK, plan trả về rồi. Nhìn qua khá ổn. Nó liệt kê rõ từng file, từng issue, mức độ nghiêm trọng.

Đặc biệt có một quả critical: lộ API key của Supabase khi gọi từ client. Cái này dev nào cũng từng dính ít nhất một lần.

Giờ mình ra lệnh cho nó fix cái critical này.

Nó lại reaction tiếp. Khá thú vị.

Rồi, nó sửa xong. Nhưng đây là điểm trừ lớn nhất: ở màn hình chat này, bạn không review được diff — không thấy nó sửa dòng nào, thay gì bằng gì. Claude hay Chát-gi-pi-ti hiện tại đều cho xem diff ngay trong giao diện. Muse thì chưa.

Đương nhiên, nó mới. Mình tin bản cập nhật sẽ cải thiện sớm.

Giờ mình mở Antigravity lên, prompt nhanh để review lại chất lượng code mà Muse vừa sửa.

Kết quả trả về. Nhìn qua khá ổn. AI khác không chê gì luôn. Mình sẽ commit lên, chạy thử rồi báo anh em sau.

Kiểm tra token thì thấy mất khoảng vài phần trăm. Với một tỷ trong tay, chưa đáng lo.

Tiếp. Muse có phần Connectors — kết nối với app bên ngoài. Facebook, Gmail, Calendar... Giờ mình thử connect Gmail nhé.

Bấm Connect, cấp quyền cho app. Xong. Prompt thử: thống kê xem hôm nay có email gì đặc biệt không.

Kết quả trả về khá nhanh. Nhanh hơn mình nghĩ.

Giờ thử yêu cầu nó xóa thư rác. Không được — nó bắt cấp thêm quyền ghi. Và đó là điều tốt. Với email, mình chỉ dám cấp quyền đọc và thống kê hàng ngày thôi.

Connectors của Muse đủ để quản lý Gmail, Facebook cơ bản ngay trên một giao diện. Khá tiện cho ai muốn gom mọi thứ về một chỗ.

Một điều nói thẳng: tại thời điểm quay video, mình chưa thấy cách nào để kết nối Muse qua các AI Router như 9Router — nghĩa là chưa đưa được vào pipeline tự động hay IDE bên ngoài. Hi vọng Meta mở sớm.

À, còn một điều. Ngoài Muse — cái app mình vừa dùng — Meta còn có Muse Spark và Muse Code. Muse Spark là phiên bản nhẹ, chat nhanh, không cần cài app. Còn Muse Code là AI coding agent dành riêng cho developer — miễn phí, chạy trực tiếp trong IDE. Ba cái tên nghe giống nhau nhưng khác mục đích.

Nếu bạn đã trải nghiệm rồi thì comment cho mình biết nhé.

Vậy là mình đã dùng thử Muse trên Mac: code review thì được việc, connectors thì tiện, nhưng giao diện review code còn thiếu. Nếu bạn thấy hay, dùng mã Ref của mình để có thêm một tỷ token — link ở phần mô tả.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: ~5–6 phút (~500–550 từ @ ~100 wpm)**

**Cài đặt chung:** Dark mode toàn bộ; font ≥18px; ẩn bookmark bar; blur email/avatar cá nhân. Quay bằng App Muse for Mac (đã cài sẵn). IDE theme Monokai/Dracula. Antigravity mở sẵn.

| # | Thời lượng | Loại | Narration tương ứng | Footage | Ghi chú |
|---|-----------|------|---------------------|---------|----|
| 1 | 12s | **[BROWSER]** | "Video trước...thử luôn." | Flash lại thumbnail EP01 (1s) → App Muse trên Mac mở lên, dark mode | Hook nhanh — nhắc EP01 rồi vào luôn |
| 2 | 15s | **[IDE]** | "Đầu tiên, mình chuẩn bị...submit." | Mở ChatGPT → show prompt review code → copy → paste vào Muse chat → bấm submit | Zoom vào prompt cho viewer đọc kịp 2–3s |
| 3 | 8s | **[BROWSER]** | "Và đây — Muse reaction...mình nói." | Muse chat: emoji reaction hiện trên tin nhắn vừa gửi | Zoom vào emoji reaction — beat humor |
| 4 | 15s | **[BROWSER]** | "Nhưng khoan...tiếp tục." | Muse báo lỗi quyền đọc file → vào Settings → bật toggle Read/Write → quay lại chat gõ tiếp | Quay rõ toggle settings |
| 5 | 20s | **[BROWSER]** | "Chờ khá lâu...mức độ nghiêm trọng." | Màn hình Muse đang loading (giữ nguyên, timer nhỏ góc) → response hiện dần → scroll plan | KHÔNG cắt thời gian chờ — giữ thật |
| 6 | 12s | **[BROWSER]** | "Đặc biệt...ít nhất một lần." | Zoom vào critical issue: lộ Supabase API key | Highlight dòng critical bằng khoanh đỏ nhẹ khi edit |
| 7 | 15s | **[BROWSER]** | "Giờ mình ra lệnh...Khá thú vị." | Gõ prompt fix critical → submit → Muse reaction lại | Beat humor nhẹ |
| 8 | 20s | **[BROWSER]** | "Rồi, nó sửa xong...Muse thì chưa." | Muse trả về kết quả fix → scroll tìm diff → KHÔNG có diff view → split screen so sánh Claude/ChatGPT diff view (screenshot) | Điểm trừ chính — beat thẳng thắn |
| 9 | 8s | **[BROWSER]** | "Đương nhiên...cải thiện sớm." | Giữ nguyên màn Muse, text overlay "MỚI — SẼ CẢI THIỆN" fade in nhẹ | Tone cân bằng — không chê quá |
| 10 | 25s | **[IDE]** | "Giờ mình mở Antigravity...báo anh em sau." | Mở Antigravity → paste prompt review → submit → kết quả hiện → scroll nhanh → terminal: `git add . && git commit` | Beat hứng khởi — AI review AI |
| 11 | 10s | **[BROWSER]** | "Kiểm tra token...chưa đáng lo." | Muse Settings → Token usage → highlight % đã dùng | Zoom vào số |
| 12 | 25s | **[BROWSER]** | "Tiếp. Muse có phần Connectors...đặc biệt không." | Sidebar Connectors → danh sách apps (Facebook, Gmail...) → bấm Connect Gmail → OAuth consent → prompt thống kê email → kết quả | Quay liền mạch |
| 13 | 15s | **[BROWSER]** | "Kết quả trả về khá nhanh...về một chỗ." | Kết quả thống kê email → prompt xóa rác → Muse báo cần quyền ghi → highlight thông báo | Beat thẳng thắn + humor |
| 14 | 15s | **[BROWSER]** | "Một điều nói thẳng...Meta mở sớm." | Muse Connectors list → overlay text "9Router? ❌ CHƯA HỖ TRỢ" | Beat thẳng thắn |
| 15 | 15s | **[B-ROLL]** | "Vậy là mình đã dùng thử...phần mô tả." | Night desk: monitor glow Muse app, tách cà phê, bàn phím → fade to black với text Ref code | CTA nhẹ — không giục |

**Tổng: ~240–280s visuals + breathing pauses ≈ 5–6 phút**

**Lưu ý quay:**
- Bạn đã quay xong footage → dùng shot list này để sắp xếp clip khi edit. Nếu thiếu scene nào (vd split screen so sánh Claude), chụp screenshot bổ sung.
- Giữ nguyên thời gian chờ response của Muse — đó là sự thật, cắt sẽ mất tính chân thực.
- Blur email cá nhân trong phần Gmail Connectors.
- Font ≥18px toàn bộ. Dark mode.
- Ref code để ở description — nhắc viewer mã 48h nên check link mới nhất.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

**Prompt 1:**
A cinematic photograph of a developer's hands on a mechanical keyboard in a dark room, a large monitor showing the Muse AI chat interface with a glowing green emoji reaction floating above a code review message, dramatic neon green and cyan rim lighting, code syntax highlighting visible on a second monitor in the background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 2:**
A cinematic photograph of a MacBook in a dark moody room showing a chat interface connected to multiple app icons (email, social media) via glowing neon green connection lines radiating outward, dramatic low-key lighting with purple ambient glow, coffee cup with steam catching cyan light, shallow depth of field, city bokeh through rain-streaked window, 8k, photorealistic, like a developer documentary. Not a screenshot, not a tutorial, not cartoon.

**Prompt 3:**
A cinematic close-up photograph of a monitor in a dark room displaying a code diff view with green additions and red deletions glowing intensely, a large question mark made of neon particles floating beside the screen, dramatic contrast between bright code and deep shadows, mechanical keyboard in soft foreground blur, purple and cyan ambient glow, 8k, photorealistic, like a high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Muse AI review code dự án thật — kết quả bất ngờ | Lập trình là cuộc sống
2. 1 tỷ token Meta: mình thử code review và đây là sự thật | Lập trình là cuộc sống
3. Muse AI trên Mac: code tốt, nhưng thiếu 1 thứ quan trọng | Lập trình là cuộc sống
4. Thử Muse AI fix bug bảo mật — rồi nhờ AI khác chấm điểm | Lập trình là cuộc sống
5. Muse AI Connectors: quản lý Gmail ngay trong AI chat? | Lập trình là cuộc sống
6. Dùng thử 1 tỷ token Muse — mất bao nhiêu cho 1 code review? | Lập trình là cuộc sống
7. Muse AI của Meta code có giỏi không? Mình thử luôn | Lập trình là cuộc sống
8. AI của Facebook review code React: lộ API key ngay lập tức | Lập trình là cuộc sống
9. Muse AI thiếu diff view — điểm trừ lớn nhất mà dev cần biết | Lập trình là cuộc sống
10. Trải nghiệm Muse AI trên Mac: code review + Gmail trong 5 phút | Lập trình là cuộc sống

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

### Option 1 — "Code Review Bất Ngờ"

**5a. Image prompt:**
A cinematic photograph, a developer silhouette sitting at a dark desk facing a large monitor displaying a code review with glowing neon green checkmarks and one large red warning icon, dramatic neon green and purple lighting, dark moody background with city bokeh through window, extreme contrast between the glowing screen and deep black shadows, dramatic rim lighting on the silhouette, deep shadows, vivid saturated neon colors, silhouette positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **MUSE AI** — `#FFFFFF` white
- Line 2: **REVIEW CODE** — `#00FF41` neon green
- Line 3 (small badge): **KẾT QUẢ BẤT NGỜ** — `#00FF41` neon green, nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **Anton** (Google Fonts, free).
- Mỗi line cao 110–140px. Line spacing 0.85. Text block bên trái ~1/3 khung.
- Neon glow: duplicate layer, blur 10–12px, opacity 60–70% màu trùng chữ. Black outline 6–10px.
- KHÔNG đè text lên màn hình monitor. Scan-line/noise overlay nhẹ. Giữ bản text-free.

### Option 2 — "Lộ API Key"

**5a. Image prompt:**
A cinematic photograph, dramatic close-up of a monitor in a dark room showing code with a glowing red highlighted line containing an API key, neon warning particles emanating from the screen, dramatic low-key lighting with neon green and red contrast, dark moody background with deep shadows, high contrast, dramatic rim lighting, vivid saturated neon colors, monitor positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **LỘ API KEY** — `#FF4444` neon red
- Line 2: **MUSE TÌM RA** — `#00FF41` neon green
- Line 3 (small badge): **TRONG 30 GIÂY** — `#FFFFFF` white, nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **JetBrains Mono** cho line 1–2, **Anton** cho badge.
- Mỗi line cao 110–130px. Line spacing 0.85. Text block bên trái.
- Neon glow: duplicate layer, blur 8–12px, opacity 65%. Black outline 8px.
- Scan-line overlay. Giữ bản text-free.

### Option 3 — "Connectors Tiện Quá"

**5a. Image prompt:**
A cinematic photograph, over-the-shoulder view of a developer looking at a dark screen showing a chat interface with multiple connected app icons (email, social media, calendar) linked by glowing neon green connection lines forming a web, dramatic low-key lighting with cyan ambient glow, dark moody background with purple fog, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, developer positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**5b. Text spec:**
- Line 1: **GMAIL** — `#FFFFFF` white
- Line 2: **TRONG AI CHAT** — `#00FF41` neon green
- Line 3 (small badge): **CONNECTORS MUSE** — `#00FF41` neon green, nền badge `#1a1a2e` viền neon

**5c. Typography specs:**
- Canvas 1280×720. Font **Anton** (Google Fonts, free).
- Mỗi line cao 110–130px. Line spacing 0.85. Text block bên trái ~1/3 khung.
- Neon glow: duplicate layer, blur 10px, opacity 60–70%. Black outline 8px.
- KHÔNG đè text lên developer. Scan-line overlay. Giữ bản text-free.
