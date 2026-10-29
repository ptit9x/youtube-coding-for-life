# EP02 — Điều Khiển Muse Từ Điện Thoại: Giao Việc Ở Đâu, Theo Dõi Ở Đó

---

## PART 1 — SCRIPT

AI agent mất ý nghĩa nếu nó chỉ làm việc khi bạn ngồi trước laptop.

Mình từng giao một task trên Mac, rời bàn, rồi quay lại chỉ để xem nó đang chờ một nút Allow. Agent chạy nền, còn mình vẫn bị buộc vào cái ghế.

Bước ngoặt của Muse không phải thêm một model. Đó là cùng một conversation đi theo mình qua điện thoại, Mac và WhatsApp.

Mình bắt đầu trên điện thoại. Task rất thực tế: theo dõi một chủ đề, tóm tắt nguồn và chuẩn bị draft. Chưa gửi cho ai.

### 🎬 PROMPT 1 — Giao task từ điện thoại

> **Mục đích:** Tạo một task có đầu ra rõ ràng và không có hành động công khai.  
> **Conversation:** Mới trên Muse mobile.  
> **Prompt:**
> ```text
> Theo dõi tin mới về Muse Spark trong hôm nay.
> Ưu tiên nguồn chính thức của Meta.
> Lập plan trước, chưa bắt đầu tìm.
> Kết quả cuối gồm 5 ý chính, link nguồn và một draft Facebook.
> Không publish hoặc gửi draft cho bất kỳ ai.
> ```
> **Kết quả mong đợi:** Muse trả plan và chờ duyệt.

Plan có ba bước: tìm nguồn, lọc thay đổi đáng chú ý, rồi viết draft. Mình kiểm tra lại phạm vi và nhấn approve.

Đây là khác biệt giữa giao việc và ném một câu prompt. Mục tiêu rõ, nguồn rõ, đầu ra rõ, quyền cũng rõ.

Muse bắt đầu chạy. Mình khóa điện thoại và rời app.

Task không chạy trên chiếc điện thoại trong túi. Muse dùng môi trường của nó và giữ conversation trên tài khoản.

Vì vậy, tắt màn hình không làm mất task. Nhưng mất mạng, hết quyền hoặc gặp bước cần xác nhận vẫn có thể khiến nó dừng.

Mình mở cùng conversation trên Mac. Trạng thái và kết quả đang chờ ở đó, không cần copy prompt qua lại.

### 🎬 PROMPT 2 — Tiếp tục task trên Mac

> **Mục đích:** Kiểm tra context có được giữ giữa hai thiết bị.  
> **Conversation:** Mở đúng conversation vừa tạo trên điện thoại.  
> **Prompt:**
> ```text
> Tóm tắt tiến độ hiện tại trong 3 dòng.
> Nêu rõ phần đã làm, phần chưa làm và hành động nào đang chờ tôi duyệt.
> Không thực hiện thêm hành động.
> ```
> **Kết quả mong đợi:** Muse mô tả đúng task và trạng thái hiện tại.

Nó nhớ chủ đề, nguồn và giới hạn publish. Đây mới là remote đúng nghĩa: tiếp tục cùng một công việc, không phải mở một chatbot khác.

Nhưng mình thử khó hơn. Mình đóng Mac rồi nhắn Muse qua WhatsApp.

### 🎬 PROMPT 3 — Kiểm tra task qua WhatsApp

> **Mục đích:** Theo dõi và điều chỉnh task bằng một kênh nhắn tin quen thuộc.  
> **Conversation:** Chat với đúng Muse account đã liên kết.  
> **Prompt:**
> ```text
> Cho tôi trạng thái task Muse Spark đang chạy.
> Nếu draft đã xong, gửi phần mở đầu và danh sách nguồn để tôi review.
> Không publish.
> ```
> **Kết quả mong đợi:** Muse trả đúng tiến độ và cùng nội dung đang thấy trên Mac.

WhatsApp tiện, nhưng màn hình nhỏ không phù hợp để review mọi thứ. Một link sai trông vẫn rất ngoan khi nằm giữa sáu dòng chữ.

Mình chỉ dùng điện thoại để theo dõi, nudge và duyệt hành động nhỏ. Review nguồn dài vẫn quay về màn hình lớn.

Draft đã xong. Muse dùng nguồn chính thức, nhưng một ý diễn giải rộng hơn nội dung gốc.

Mình yêu cầu sửa đúng phần đó. Không viết lại toàn bộ bài.

### 🎬 PROMPT 4 — Sửa có phạm vi

> **Mục đích:** Chứng minh context được giữ và giới hạn thay đổi.  
> **Conversation:** Tiếp tục cùng conversation trên điện thoại hoặc WhatsApp.  
> **Prompt:**
> ```text
> Sửa riêng ý thứ 3 để bám sát nguồn chính thức.
> Không thay tiêu đề, các ý còn lại hoặc CTA.
> Trả lại đoạn trước và sau khi sửa để tôi so sánh.
> ```
> **Kết quả mong đợi:** Muse chỉ thay đúng đoạn được yêu cầu.

Đây là bước dễ bị bỏ qua khi làm việc bằng điện thoại. Approve nhanh rất tiện. Approve nhầm còn nhanh hơn.

Mình mở lại Mac, đối chiếu bản sửa với nguồn, rồi lưu draft. Không có publish trong tập này.

Điều đáng giá nhất không phải điều khiển AI từ xa. Đó là giữ được một workflow liên tục khi mình đổi thiết bị.

Điện thoại dùng để giao việc và theo dõi. Màn hình lớn dùng để review. Quyền cuối cùng vẫn thuộc về mình.

Prompt nằm trong phần mô tả. Comment task bạn muốn giao cho Muse khi rời bàn.

Tập sau, mình dùng Muse Spark build một app nhỏ và kiểm tra xem “vibe coding” có thật sự tiết kiệm thời gian. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: 7:20 (440 giây).**

| # | Thời lượng | Loại | Narration | Footage cụ thể |
|---|---:|---|---|---|
| 1 | 18s | **[MOBILE + B-ROLL]** | “AI agent mất ý nghĩa…” | Mac hiện nút Allow, host rời bàn, điện thoại rung. |
| 2 | 20s | **[DIAGRAM]** | “Cùng một conversation…” | Phone ↔ Muse account ↔ Mac ↔ WhatsApp. |
| 3 | 28s | **[MOBILE]** | “Mình bắt đầu…” | Mở Muse, tạo conversation, paste Prompt 1. |
| 4 | 35s | **[MOBILE]** | “Plan có ba bước…” | Scroll plan, highlight scope và nút approve. |
| 5 | 30s | **[MOBILE + B-ROLL]** | “Muse bắt đầu chạy…” | Khóa màn hình, bỏ điện thoại vào túi; processing tua 8x. |
| 6 | 24s | **[DIAGRAM]** | “Task không chạy…” | Phone chỉ là remote; task chạy trên Muse environment. |
| 7 | 34s | **[BROWSER]** | “Mình mở cùng conversation…” | Mac mở đúng thread, nhập Prompt 2, thấy đúng trạng thái. |
| 8 | 25s | **[B-ROLL]** | “Nó nhớ chủ đề…” | Split screen phone và Mac cùng tên conversation. |
| 9 | 32s | **[MOBILE]** | “Mình đóng Mac…” | WhatsApp, Prompt 3, trạng thái task trả về. |
| 10 | 24s | **[MOBILE]** | “WhatsApp tiện…” | Zoom link nguồn trên màn hình nhỏ; overlay “TRACK ≠ REVIEW”. |
| 11 | 38s | **[BROWSER]** | “Draft đã xong…” | Mac mở nguồn chính thức cạnh draft, highlight chỗ diễn giải rộng. |
| 12 | 28s | **[MOBILE]** | “Mình yêu cầu sửa…” | Paste Prompt 4, Muse trả before/after. |
| 13 | 30s | **[DIAGRAM]** | “Approve nhanh…” | Permission nhỏ → tác động lớn; human checkpoint. |
| 14 | 35s | **[BROWSER]** | “Mình mở lại Mac…” | Đối chiếu nguồn, lưu draft, xác nhận không publish. |
| 15 | 25s | **[B-ROLL]** | “Điều đáng giá nhất…” | Đi bộ với điện thoại, Mac ở bàn, task hoàn tất. |
| 16 | 14s | **[BROWSER]** | Outro | Preview EP03: terminal, Muse Spark plan và app chạy. |

**Tổng: 440 giây = 7:20.**

**Lưu ý quay:** Dùng cùng một account trên mobile, Mac và WhatsApp. Che số điện thoại, email, avatar và notification riêng. Giữ thời gian chờ thật tối đa ba giây rồi tua 6–10x. Nếu tính năng cross-device chưa có trên account, không giả lập; quay màn hình trạng thái thật và nói rõ giới hạn rollout.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. A cinematic photograph of a Vietnamese developer walking away from a glowing laptop while controlling the same AI task from a smartphone, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, 16:9, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.
2. A cinematic photograph of a smartphone in the foreground showing a glowing AI task while a laptop continues working in the dark background, dark moody lighting, monitor glow illuminating the scene, code visible with neon syntax highlighting in green and cyan, shallow depth of field, rain and city bokeh, film grain, 8k, 16:9, photorealistic, like a developer documentary. Not a screenshot, not a tutorial, not cartoon.
3. A cinematic photograph of one luminous conversation thread flowing between a smartphone, WhatsApp and a Mac on a developer desk, dark moody lighting, monitor glow illuminating the scene, code visible on screen with green and cyan syntax highlighting, shallow depth of field, bokeh city lights, 8k, 16:9, photorealistic, like a high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Tôi rời laptop, Muse vẫn tiếp tục làm việc | Lập trình là cuộc sống
2. Điều khiển Muse từ điện thoại có thật sự hữu ích? | Lập trình là cuộc sống
3. Giao việc trên điện thoại, review trên Mac | Lập trình là cuộc sống
4. Muse chạy nền khi bạn đã đóng app thế nào? | Lập trình là cuộc sống
5. Một conversation đi từ điện thoại sang laptop | Lập trình là cuộc sống
6. Tôi thử quản lý AI agent qua WhatsApp | Lập trình là cuộc sống
7. AI chạy từ xa — nhưng nút duyệt vẫn theo bạn | Lập trình là cuộc sống
8. Remote Muse mà không approve mù | Lập trình là cuộc sống
9. Điện thoại không phải nơi review code | Lập trình là cuộc sống
10. Muse biến điện thoại thành remote cho AI agent | Lập trình là cuộc sống

**Khuyên dùng:** Title 1.

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — RỜI MÁY / AI VẪN CHẠY

**Image prompt:** A cinematic photograph, a developer silhouette leaving a glowing laptop while holding a smartphone that controls a floating AI task, dramatic neon green and cyan lighting, exaggerated code and progress elements, dark rainy city bokeh, extreme contrast, subject on the right leaving dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `RỜI MÁY` trắng / `AI VẪN CHẠY` xanh `#00FF41`.

### Option 2 — MUSE TRONG TÚI

**Image prompt:** A cinematic photograph, a hand holding a smartphone with a glowing Muse agent while a laptop works unattended in the background, dramatic neon green and purple rim lighting, floating task cards and code, deep shadows, empty dark space on the left, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `MUSE` trắng / `TRONG TÚI` xanh `#00FF41`.

### Option 3 — PHONE → MAC

**Image prompt:** A cinematic photograph, one luminous AI conversation flowing from a smartphone to a Mac across a dark developer desk, dramatic neon green and cyan lighting, floating message and code elements, extreme contrast, key visuals on the right leaving text space on the left, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `PHONE` trắng / `→ MAC` xanh `#00FF41` / badge `KHÔNG MẤT CONTEXT` trắng.

**Typography chung:** Canvas 1280×720. Anton cho hook, JetBrains Mono cho badge. Mỗi line cao 110–140px, spacing 0.85. Text chiếm một phần ba bên trái. Neon blur 10px, opacity 65%, black stroke 8px. Typeset bằng Canva và lưu bản sạch không chữ.

---

## PART 6 — YOUTUBE SEO

### Description

```text
Mình thử giao task cho Muse trên điện thoại, theo dõi qua WhatsApp và review kết quả trên Mac. Điểm quan trọng: đổi thiết bị không có nghĩa được bỏ bước review.

⏩ 0:00 — Vì sao agent vẫn trói bạn vào laptop
⏩ 0:38 — Giao task từ Muse mobile
⏩ 1:35 — Task chạy khi màn hình đã khóa
⏩ 2:29 — Tiếp tục cùng conversation trên Mac
⏩ 3:28 — Theo dõi task qua WhatsApp
⏩ 4:24 — Vì sao không nên review trên màn hình nhỏ
⏩ 5:26 — Sửa đúng một đoạn, không viết lại tất cả
⏩ 6:24 — Kiểm chứng trên Mac

#MuseAI #AIAgent #RemoteWork
```

### Tags

`Muse AI mobile, Muse remote phone, Muse WhatsApp, AI agent chạy nền, điều khiển AI từ điện thoại, Muse Mac, cross device AI, AI workflow, lập trình là cuộc sống`

### Pinned Comment

```text
Điện thoại để giao việc và theo dõi. Màn hình lớn để review. Quyền cuối cùng vẫn thuộc về người dùng.

Bạn muốn giao task nào cho Muse khi rời bàn? 👇
```
