# EP02 — Muse AI Một Tuần Sau: Code Review, Schedule, Tiếng Việt, Ảnh & Video

- **Series:** AI Miễn Phí — EP02, tiếp nối EP01 đã phát hành ("Cách sử dụng VPN Free để lấy 1 TỶ Token Muse AI", https://youtu.be/hQzSDxDhX6s).
- **Target runtime:** ~7:50 (468s visuals, ~690 từ @ 100 wpm, fill ~88%).
- **Outcome:** Người xem biết Muse làm được gì ngoài chat: review code thật, đặt lịch agent tự chạy, TTS tiếng Việt (giới hạn giọng), gen ảnh, gen ảnh thành video — và tiêu token thế nào.
- **Nguyên tắc:** Thẳng thắn, không tô hồng — giới hạn thật được nói rõ (không diff view, TTS thiếu giọng Nam, media gen đốt token nhanh).

---

## PART 1 — SCRIPT

Video trước bạn đã có một tỷ token. Câu hỏi hôm nay: token đó làm được gì ngoài chat? Mình dùng Muse trên Mac một tuần, và thử năm việc: review code, đặt lịch, đọc tiếng Việt, vẽ ảnh, và biến ảnh thành video.

Việc đầu tiên, quen thuộc: review code. Mình chuẩn bị sẵn một prompt review bằng Chát-gi-pi-ti, yêu cầu Muse quét toàn bộ dự án React cộng Supabase: lỗi bảo mật, code smell, và plan fix. Dán vào, submit.

Và đây — Muse reaction tin nhắn của mình bằng emoji. Hàng Facebook có khác. Vừa hay vừa hơi rợn, y như video trước mình nói.

Khoan. Nó báo App chưa có quyền đọc ghi file. Vào Settings, bật quyền đọc ghi cho nó, rồi chat lại.

Chờ khá lâu — response của Muse chậm hơn mấy AI mình quen. Nhưng cứ chờ. Plan trả về: liệt kê rõ từng file, từng issue, mức độ nghiêm trọng. Đặc biệt một quả critical: lộ API key của Supabase khi gọi từ client. Cái này dev nào cũng từng dính.

Ra lệnh fix. Nó sửa xong — nhưng đây là điểm trừ lớn nhất: ở màn hình chat, bạn không review được diff. Không thấy nó sửa dòng nào, thay gì bằng gì. Claude hay Chát-gi-pi-ti đều xem được diff ngay trong giao diện. Muse thì chưa. Mình mở Antigravity review lại — kết quả ổn, commit.

Kiểm tra token: mất vài phần trăm. Với một tỷ, chưa đáng lo.

Tiếp, phần Connectors: kết nối app bên ngoài. Mình connect Gmail, rồi hỏi: hôm nay có email gì đặc biệt không. Kết quả về khá nhanh. Thử xóa thư rác — không được, nó bắt cấp thêm quyền ghi. Và đó là điều tốt. Với email, mình chỉ dám cấp quyền đọc thôi.

Giờ tới tính năng mình thích nhất: Schedule. Mình đặt lịch cho agent: mỗi sáng tám giờ, đọc tin công nghệ trong hai mươi tư giờ qua, chọn năm mục đáng đọc cho dev, gửi digest lại cho mình. Đặt xong, khởi động lại máy — job vẫn nằm đó. Nó chạy trên tài khoản, không phải trên máy bạn.

Sáng hôm sau, đúng tám giờ, tin nhắn tới. Không ai bấm nút. Đây là khác biệt giữa chatbot và agent: chatbot trả lời khi bạn hỏi — agent làm việc khi bạn không có mặt.

Thử tiếp phần đọc — text to speech. Mình nhờ Muse đọc một đoạn tiếng Việt. Nghe thử nhé. Nghe được: ngữ điệu rõ, không còn giọng robot hồi xưa. Nhưng nói thẳng: chọn giọng thì tiếng Việt hiện chưa có giọng miền Nam. Anh em miền Nam nghe sẽ thấy hơi bắc. Làm nội dung cần giọng Nam thì phải dùng tool khác — miễn phí không có nghĩa là đủ mọi thứ.

Giờ tới phần vẽ. Một prompt: bàn dev ban đêm, hai màn hình, ánh neon xanh. Khoảng một phút sau, ảnh trả về — đúng subject, composition ổn, làm thumbnail hay minh họa slide là dư sức. Lưu ý: gen media đốt token nhanh hơn chat text nhiều — vài ảnh là thấy hạn mức nhảy. Miễn phí có giá của nó.

Và chiêu cuối: biến chính ảnh vừa vẽ thành video. Upload lại ảnh, thêm một câu: camera chậm rãi zoom vào màn hình bên trái. Vài phút sau, Muse trả về một đoạn video ngắn có chuyển động. Chưa đủ làm quảng cáo, nhưng làm B-roll mở đầu video thì quá ổn. Từ text sang ảnh sang video, toàn bộ trong một app miễn phí — hai năm trước việc này phải ghép ba công cụ trả phí.

Nói nhanh ba cái tên cho ai mới vào: Muse là app mình đang dùng. Muse Spark là model — bộ não bên dưới. Muse Code là công cụ dòng lệnh cho dev.

Một tuần với Muse: code review được việc, schedule đáng tiền nhất, ảnh và video là bonus. Nếu bạn thấy hữu ích, dùng mã Ref của mình để có thêm một tỷ token — link ở phần mô tả.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: ~7:50 (468s visuals, ~690 từ @ 100 wpm ≈ 88% fill).**

**Cài đặt chung:** Dark mode toàn bộ; font ≥18px; ẩn bookmark bar; blur email/avatar cá nhân. App Muse for Mac cài sẵn. IDE theme Monokai/Dracula. Antigravity mở sẵn.

| # | Thời lượng | Loại | Narration tương ứng | Footage | Ghi chú |
|---|-----------|------|---------------------|---------|---------|
| 1 | 15s | **[BROWSER]** | "Video trước...ảnh thành video." | Flash thumbnail EP01 (1s) → App Muse Mac mở, dark mode; overlay 5 icon hiện dần: code / clock / speaker / image / film | Hook nhanh — liệt kê 5 việc tạo expectation |
| 2 | 25s | **[IDE]** | "Việc đầu tiên...dán vào, submit." | ChatGPT show Prompt 1 → copy → paste vào Muse chat → submit | Zoom prompt 2–3s cho viewer đọc kịp |
| 3 | 8s | **[BROWSER]** | "Và đây — Muse reaction...mình nói." | Emoji reaction hiện trên tin nhắn vừa gửi | Beat humor |
| 4 | 15s | **[BROWSER]** | "Khoan...chat lại." | Báo lỗi quyền → Settings → bật toggle Read/Write → quay lại chat | Quay rõ toggle |
| 5 | 35s | **[BROWSER]** | "Chờ khá lâu...dev nào cũng từng dính." | Loading giữ nguyên (timer nhỏ góc) → plan hiện → scroll → zoom critical Supabase API key | KHÔNG cắt thời gian chờ; khoanh đỏ critical |
| 6 | 15s | **[BROWSER]** | "Ra lệnh fix." | Gõ Prompt 2 → submit → reaction lại | Nhanh, gọn |
| 7 | 25s | **[BROWSER]** | "Nó sửa xong...Muse thì chưa." | Kết quả fix → scroll tìm diff → KHÔNG có → split screen screenshot diff view Claude/ChatGPT | Điểm trừ chính — beat thẳng thắn |
| 8 | 25s | **[IDE]** | "Mình mở Antigravity...commit." | Antigravity paste prompt review → kết quả → terminal `git add . && git commit` | Beat hứng khởi — AI review AI |
| 9 | 10s | **[BROWSER]** | "Kiểm tra token...chưa đáng lo." | Muse Settings → Token usage → highlight % đã dùng | Zoom số |
| 10 | 30s | **[BROWSER]** | "Tiếp, phần Connectors...quyền đọc thôi." | Sidebar Connectors → Connect Gmail → OAuth → prompt thống kê → kết quả; prompt xóa rác → báo cần quyền ghi → highlight | Quay liền mạch; blur email cá nhân |
| 11 | 50s | **[BROWSER]** | "Giờ tới tính năng...không phải trên máy bạn." | Tạo Schedule (Prompt 3): chọn 8:00, nhập yêu cầu → job tạo xong → restart app/Mac → job vẫn còn | Cảnh mới — quay theo UI thật; caption "CHẠY TRÊN TÀI KHOẢN, KHÔNG PHẢI TRÊN MÁY" |
| 12 | 40s | **[BROWSER + MOBILE]** | "Sáng hôm sau...không có mặt." | Đúng 8:00 tin nhắn digest tới (quay màn hình lock/Telegram); scroll digest 5 mục | Cảnh "tiền" — nếu không chờ qua đêm: đặt job +2 phút cho demo same-day + chèn screenshot digest sáng thật |
| 13 | 40s | **[BROWSER]** | "Thử tiếp phần đọc...đủ mọi thứ." | Muse TTS: dán đoạn văn tiếng Việt (Prompt 4) → chọn giọng → play; zoom danh sách giọng: có các giọng vi, KHÔNG có giọng Nam → overlay "GIỌNG MIỀN NAM: CHƯA CÓ" | Nghe thật ít nhất 1 câu; beat thẳng thắn |
| 14 | 45s | **[BROWSER]** | "Giờ tới phần vẽ...giá của nó." | Prompt 5 → chờ gen (timer góc, giữ thật ~15s rồi speed-up) → ảnh trả về → Settings token usage nhảy | Zoom ảnh kết quả; caption "MEDIA ĂN TOKEN NHANH HƠN TEXT" |
| 15 | 50s | **[BROWSER]** | "Và chiêu cuối...ba công cụ trả phí." | Upload lại ảnh vừa gen → Prompt 6 → chờ (speed-up phần dài) → video ngắn play loop 2 nhịp | Cảnh kết demo — video chạy loop 2 nhịp |
| 16 | 20s | **[DIAGRAM]** | "Nói nhanh ba cái tên...cho dev." | 3 hộp: MUSE (app) → MUSE SPARK (model) → MUSE CODE (CLI) | Fix định nghĩa — khớp EP01 + fact-sheet |
| 17 | 20s | **[B-ROLL]** | "Một tuần với Muse...phần mô tả." | Night desk: monitor glow, tách cà phê, bàn phím → fade to black + text Ref code | CTA nhẹ — không giục |

**Tổng: 468s visuals + breathing pauses ≈ 7:50.**

### Prompt trên màn hình (verbatim)

```text
Prompt 1 (review, soạn trong ChatGPT):
Review toàn bộ dự án React + Supabase này: quét lỗi bảo mật, code smell,
và đề xuất plan fix theo mức độ nghiêm trọng. Liệt kê rõ từng file và dòng.

Prompt 2 (fix critical):
Fix critical issue số 1: lộ Supabase API key khi gọi từ client.
Giải thích cách sửa trước khi sửa.

Prompt 3 (schedule):
Mỗi sáng 8:00, đọc tin công nghệ nổi bật trong 24 giờ qua, chọn 5 mục
đáng đọc nhất cho developer Việt, mỗi mục 1 câu + link, gửi digest cho tôi.

Prompt 4 (TTS tiếng Việt):
Đọc to đoạn sau bằng giọng tiếng Việt: "Lập trình là cuộc sống.
Hôm nay chúng ta thử một trợ lý AI mới, và nó nói tiếng Việt đấy."

Prompt 5 (gen ảnh):
Một bàn dev ban đêm, hai màn hình sáng, ánh neon xanh cyan,
phong cách cinematic, tỷ lệ 16:9.

Prompt 6 (ảnh thành video, kèm ảnh từ Prompt 5):
Camera chậm rãi zoom vào màn hình bên trái.
```

**Lưu ý quay:**
- Cảnh 2–10 đã có footage từ lần quay trước — dùng shot list sắp xếp lại khi edit, bổ sung split screen diff (cảnh 7) nếu thiếu.
- Cảnh 11–15 là cảnh MỚI: quay theo UI thật tại thời điểm quay; narration không đọc tên nút cứng nên vẫn đúng khi Meta đổi UI.
- Schedule demo: nếu không quay qua đêm, đặt job chạy sau 2 phút để có tin nhắn tới trong cùng session; khoe thêm screenshot digest 8:00 thật của buổi sáng hôm trước.
- TTS: verify danh sách giọng trước 30 phút quay — nếu Muse đã có giọng miền Nam, cập nhật narration và fact này.
- Giữ nguyên độ trễ response khi edit — đó là sự thật, cắt sẽ mất tính chân thực.
- Ref code để ở description + pinned comment; nhắc viewer mã hết hạn 48h.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

**Prompt 1 (code review — khớp assets sẵn `thumbnail-01-code-review.jpg`):**
A cinematic photograph of a developer's hands on a mechanical keyboard in a dark room, a large monitor showing the Muse AI chat interface with a glowing green emoji reaction floating above a code review message, dramatic neon green and cyan rim lighting, code syntax highlighting visible on a second monitor in the background, shallow depth of field, bokeh city lights through window, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.

**Prompt 2 (ảnh → video):**
A cinematic photograph of a developer's hand hovering over a trackpad in a dark room, a large monitor showing a single still photo of a neon-lit desk transforming into a video timeline with a subtle glowing play button, motion streaks flowing from the static image into moving light, dramatic low-key lighting with purple ambient glow, shallow depth of field, bokeh city lights through rain-streaked window, 8k, photorealistic, like a developer documentary. Not a screenshot, not cartoon.

**Prompt 3 (schedule — agent tự dậy):**
A cinematic photograph of a smartphone on a nightstand lighting up at dawn with a notification badge while the developer sleeps out of focus in the background, a subtle holographic clock floating above the phone showing 8:00, warm amber dawn light mixed with cyan glow from the screen, shallow depth of field, 8k, photorealistic, like a high-end tech commercial. Not a screenshot, not cartoon.

---

## PART 4 — TITLES (10)

1. Muse AI làm được gì ngoài chat? Review code, đặt lịch, đọc tiếng Việt, vẽ ảnh, dựng video | Lập trình là cuộc sống
2. AI tự dậy 8 giờ sáng gửi tin cho bạn — Muse Schedule | Lập trình là cuộc sống
3. 1 tỷ token Muse: một tuần sau, điều đáng tiền nhất không phải là code review | Lập trình là cuộc sống
4. Muse AI đọc tiếng Việt: nghe thử rồi quyết định — và giọng miền Nam thì chưa có | Lập trình là cuộc sống
5. Biến ảnh thành video ngay trong Muse AI — miễn phí | Lập trình là cuộc sống
6. Từ text sang ảnh sang video, tất cả trong 1 app miễn phí của Meta | Lập trình là cuộc sống
7. Muse AI review code React: lộ API key ngay lần đầu | Lập trình là cuộc sống
8. Trợ lý AI của Meta: review code, đọc Gmail, đặt lịch, vẽ ảnh — một app | Lập trình là cuộc sống
9. 5 việc bạn nên thử ngay khi có 1 tỷ token Muse | Lập trình là cuộc sống
10. Muse AI một tuần sau: điểm đáng tiền nhất và điểm trừ lớn nhất | Lập trình là cuộc sống

**Khuyên dùng:** Title 2 (schedule là hook khác biệt nhất so với mọi video Muse review khác) hoặc Title 6 (text→ảnh→video dễ viral). A/B test Title 1 cho người cần overview.

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

### Option 1 — "AI Tự Thức Dậy" (khuyên dùng — image Prompt 3)

**5b. Text spec:**
- Line 1: **8:00 SÁNG** — `#FFFFFF` white
- Line 2: **AI TỰ THỨC DẬY** — `#00FF41` neon green
- Line 3 (small badge): **KHÔNG AI BẤM NÚT** — `#00D4FF` cyan, nền badge `#1a1a2e` viền neon

### Option 2 — "Ảnh Thành Video" (image Prompt 2)

**5b. Text spec:**
- Line 1: **ẢNH** — `#FFFFFF` white
- Line 2: **THÀNH VIDEO** — `#00FF41` neon green
- Line 3 (small badge): **TRONG 1 APP** — `#00FF41` neon green, nền badge `#1a1a2e` viền neon

### Option 3 — "Code Review" (assets sẵn `thumbnail-01-code-review.jpg` / `thumbnail-03-critical-bug.jpg`)

**5b. Text spec:**
- Line 1: **MUSE AI** — `#FFFFFF` white
- Line 2: **REVIEW CODE** — `#00FF41` neon green
- Line 3 (small badge): **LỘ API KEY** — `#FF4444` neon red, nền badge `#1a1a2e` viền neon

**Typography chung (cả 3 option):** Canvas 1280×720. Font **Anton** cho line 1–2, **JetBrains Mono** cho badge. Mỗi line cao 110–140px. Line spacing 0.85. Text block bên trái ~1/3 khung. Neon glow: duplicate layer, blur 10–12px, opacity 60–70% màu trùng chữ. Black outline 8px. KHÔNG đè text lên subject. Scan-line overlay nhẹ. Giữ bản text-free.

---

## PART 6 — YOUTUBE SEO

### Description

```
1 tỷ token rồi làm gì? Mình dùng Muse AI của Meta một tuần: review code dự án thật, đặt lịch cho agent tự chạy mỗi sáng, đọc tiếng Việt, vẽ ảnh và biến ảnh thành video.

Video này cho bạn thấy:
⏩ 0:00 — Muse làm được gì ngoài chat?
⏩ 0:15 — Code review dự án React + Supabase thật
⏩ 1:53 — Điểm trừ lớn nhất: không có diff view
⏩ 2:53 — Connectors: đọc Gmail ngay trong AI chat
⏩ 3:23 — Schedule: AI tự dậy 8:00 sáng gửi digest
⏩ 4:53 — TTS tiếng Việt: nghe thử (chưa có giọng miền Nam)
⏩ 5:33 — Gen ảnh từ text
⏩ 6:18 — Biến ảnh thành video

━━━━━━━━━━━━━━━━━━━━━━
🎁 NHẬN 1 TỶ TOKEN MUSE MIỄN PHÍ
━━━━━━━━━━━━━━━━━━━━━━
👉 Code: 16NESL
👉 Đăng ký tại: https://muse.ai/join
⚠️ Bạn cần nhập mã trong vòng 48 giờ sau khi tạo tài khoản Muse!

━━━━━━━━━━━━━━━━━━━━━━
🔗 LINK HỮU ÍCH
━━━━━━━━━━━━━━━━━━━━━━
▸ Video trước — đăng ký Muse AI từ VN: https://youtu.be/hQzSDxDhX6s
▸ Muse AI: https://muse.ai

#MuseAI #Meta #AIAgent #Schedule #TTS #TextToImage #LapTrinhLaCuocSong #AIMienPhi
```

### Tags (paste vào YouTube Studio)

```
Muse AI, Meta Muse, Muse AI review, Muse AI schedule, AI tự động chạy, AI agent đặt lịch, Muse TTS tiếng Việt, muse text to speech việt nam, giọng đọc AI miền nam, Muse gen ảnh, Muse image generation, muse ảnh thành video, image to video AI, 1 tỷ token Muse, Muse referral code, Muse code review, AI review code React, Muse connectors, Muse Gmail, AI miễn phí cho dev, trợ lý AI Meta, lập trình là cuộc sống
```

### Hashtags (3 hiển thị trên tiêu đề)

```
#MuseAI #AIAgent #AIMienPhi
```

### Pinned Comment (ghim lên đầu)

```
📌 Mã giới thiệu Muse: 16NESL
👉 Đăng ký: https://muse.ai/join
⏰ Nhập mã trong Cài đặt → Quy đổi mã lời mời, trong vòng 48 giờ sau khi tạo tài khoản → cả hai cùng được 1 TỶ token!

Bạn đang dùng Muse làm gì? Comment chia sẻ — mình test trong video sau 👇
```
