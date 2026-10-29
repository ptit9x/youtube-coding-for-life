# EP01 — Quản Lý Facebook Page Và YouTube Với Muse: AI Làm, Người Duyệt

---

## PART 1 — SCRIPT

Quản lý hai kênh không khó. Khó là lặp lại cùng một việc trên hai dashboard mỗi ngày.

Bạn kiểm tra số liệu, tìm chủ đề, viết bài, làm ảnh, đăng video, rồi đọc comment. Cuối ngày, nội dung chưa chắc tốt hơn. Chỉ có số tab tăng lên.

Mình từng dùng một tool cho mỗi việc. Cách đó chạy được, nhưng mình trở thành người chuyển dữ liệu giữa các tool.

Điểm đổi hướng là thế này. AI không cần thay mình quản lý kênh. Nó cần gom workflow về một chỗ, rồi dừng trước quyết định quan trọng.

Mình bắt đầu với Facebook. Muse báo tài khoản đã kết nối, nhưng Page vẫn cần quyền riêng.

### 🎬 PROMPT 1 — Kết nối và đọc Facebook Page

> **Mục đích:** Chọn đúng Page và chỉ đọc dữ liệu.  
> **Conversation:** Mới. Chuẩn bị tài khoản Meta đang quản trị Page.  
> **Prompt:**
> ```text
> Kết nối Facebook Page “Lập trình là cuộc sống”.
> Chỉ cấp quyền cho Page này, không chọn toàn bộ Page trong tài khoản.
> Phân tích hiệu suất 28 ngày gần nhất. Chỉ đọc dữ liệu, chưa đăng nội dung.
> ```
> **Kết quả mong đợi:** Muse kết nối đúng Page và trả báo cáo.

Meta hiện bốn Page mình đang quản lý. Mình chỉ chọn “Lập trình là cuộc sống”.

Đây là nguyên tắc quyền tối thiểu. Tool chỉ nhận đúng quyền cần để làm việc. Tài khoản database cũng không nên có quyền xóa production.

Muse đọc dữ liệu hai mươi tám ngày. Nó tổng hợp lượt xem, người xem riêng, tương tác và follower mới.

Con số đáng chú ý nhất lại là số không. Page có hơn mười ngàn follower, nhưng kỳ này không có follower mới.

AI không cứu được một chiến lược nội dung yếu. Nhưng nó giúp mình nhìn thẳng vào dữ liệu, thay vì tự an ủi bằng follower cũ.

Mình chuyển sang bước tạo nội dung. Yêu cầu phải có chủ đề, nguồn và giới hạn hành động.

### 🎬 PROMPT 2 — Tìm tin và tạo draft Facebook

> **Mục đích:** Tìm tin phù hợp và chuẩn bị bài nháp có nguồn.  
> **Conversation:** Tiếp tục conversation Facebook hiện tại.  
> **Prompt:**
> ```text
> Tìm một tin công nghệ nổi bật trong 24 giờ gần nhất, phù hợp với developer Việt.
> Ưu tiên nguồn chính thức. Ghi link nguồn, ngày đăng và dữ kiện cần kiểm tra.
> Soạn một bài ngắn theo giọng Page. Chỉ tạo draft, chưa publish.
> ```
> **Kết quả mong đợi:** Muse trả chủ đề, nguồn và draft để review.

Trong lúc Muse xử lý, mình review theo sáu bước. Yêu cầu, plan, đọc lại, approve, thực hiện, rồi kiểm chứng.

Muse chọn một cảnh báo bảo mật PHP. Nó viết tiêu đề, phiên bản bị ảnh hưởng, nguồn và lời kêu gọi cập nhật.

Nghe rất thuyết phục. Đó cũng là lúc cần nghi ngờ nhất.

Với tin bảo mật, sai một phiên bản có thể khiến người đọc hiểu sai rủi ro. AI viết nhanh không đồng nghĩa AI được miễn review.

Mình kiểm tra nguồn, ngày và từng con số. Sau đó, mình yêu cầu thêm ảnh và link YouTube Shorts liên quan.

### 🎬 PROMPT 3 — Hoàn thiện và publish sau khi duyệt

> **Mục đích:** Bổ sung media, nhưng giữ quyền publish cho người quản trị.  
> **Conversation:** Tiếp tục conversation Facebook hiện tại.  
> **Prompt:**
> ```text
> Bổ sung một ảnh minh họa và link YouTube Shorts cùng chủ đề.
> Giữ nguyên các nguồn đã kiểm chứng. Cho tôi xem bản hoàn chỉnh trước.
> Chỉ publish sau khi tôi xác nhận.
> ```
> **Kết quả mong đợi:** Muse cập nhật draft và dừng ở bước xin phép đăng.

Muse tạo ảnh, gắn link, rồi dừng lại ở màn hình xin quyền. Đây là đoạn đáng giữ nguyên tốc độ.

Quyền đọc số liệu và quyền xuất bản là hai chuyện khác nhau. Một nút Allow có thể đưa nội dung tới hơn mười ngàn người.

Mình duyệt. Muse đăng bài và trả lại đường dẫn Facebook.

Nhưng thông báo “đã đăng” chưa phải bằng chứng. Mình mở link, kiểm tra ảnh, nội dung và link Shorts trên Page thật.

Sau đó, mình tạo một tác vụ hằng ngày. Tác vụ hẹn giờ giống cron job trên server, nhưng kết quả chỉ dừng ở draft.

### 🎬 PROMPT 4 — Tạo draft Facebook hằng ngày

> **Mục đích:** Tự động hóa phần chuẩn bị, không tự động hóa quyết định đăng.  
> **Conversation:** Tiếp tục conversation Facebook hiện tại.  
> **Prompt:**
> ```text
> Tạo job chạy mỗi ngày lúc 8:30.
> Tìm tin công nghệ trong 24 giờ gần nhất và kiểm tra ít nhất hai nguồn.
> Soạn bài cho Page “Lập trình là cuộc sống” và chỉ lưu draft.
> Không tự publish. Báo lại để tôi review.
> ```
> **Kết quả mong đợi:** Muse tạo lịch chạy và ghi rõ đầu ra là draft.

Mỗi sáng, AI đặt một bản nháp lên bàn. Quyết định sửa, đăng hay xóa vẫn thuộc về mình.

Facebook đã ổn. Mình chuyển sang YouTube trong một conversation mới để context không bị trộn.

### 🎬 PROMPT 5 — Kết nối và phân tích YouTube

> **Mục đích:** Kết nối kênh và lấy bối cảnh trước khi hành động.  
> **Conversation:** Mới. Chuẩn bị tài khoản Google quản lý đúng kênh.  
> **Prompt:**
> ```text
> Kết nối kênh YouTube “Lập trình là cuộc sống”.
> Tóm tắt thông tin kênh và các video Shorts gần đây.
> Chỉ đọc dữ liệu. Chưa upload, sửa hoặc bình luận.
> ```
> **Kết quả mong đợi:** Muse xác thực Google và trả tóm tắt kênh.

Muse mở đăng nhập Google và lưu kết nối bảo mật. Phần này cần thiết, nhưng không cần xem từng giây.

Sau khi kết nối, Muse đọc thông tin kênh và danh sách Shorts. Mình dùng dữ liệu đó để chọn nội dung tiếp theo.

Mình giao một file video có sẵn. Muse không tạo footage thay mình. Nó chỉ mở YouTube Studio và đi qua quy trình upload.

### 🎬 PROMPT 6 — Upload một YouTube Short

> **Mục đích:** Upload đúng file và cho phép review trước khi công khai.  
> **Conversation:** Tiếp tục conversation YouTube. Chuẩn bị sẵn file video dọc.  
> **Prompt:**
> ```text
> Upload file video dọc tôi đã chọn dưới dạng Short.
> Đề xuất tiêu đề và mô tả ngắn dựa trên nội dung file.
> Điền metadata, chọn đúng đối tượng người xem và dừng để tôi review.
> Không tự chọn file khác. Không tự publish.
> ```
> **Kết quả mong đợi:** Muse upload đúng file và dừng trước bước hiển thị.

Trong lúc file upload, mình kiểm tra ba thứ. Đúng file, đúng kênh và đúng chế độ hiển thị.

Muse điền tiêu đề, mô tả, đối tượng người xem và chế độ hiển thị. Những màn hình này trông dài, nhưng ý nghĩa chỉ có vậy.

Mình review rồi cho phép tiếp tục. Short xuất hiện trong YouTube Studio.

Cuối cùng, mình thử một hành động nhỏ nhưng công khai: đăng comment lên video vừa chọn.

### 🎬 PROMPT 7 — Đăng comment và kiểm chứng

> **Mục đích:** Thao tác trên video thật và xác minh kết quả.  
> **Conversation:** Tiếp tục conversation YouTube.  
> **Prompt:**
> ```text
> Mở video YouTube gần nhất mà chúng ta vừa chọn.
> Soạn một comment ngắn, đúng ngữ cảnh và cho tôi review.
> Sau khi tôi xác nhận, đăng comment rồi mở lại video để kiểm chứng.
> ```
> **Kết quả mong đợi:** Comment xuất hiện trên video thật.

Muse mở video, điền comment và đăng. Mình kiểm tra lại ở YouTube, không chỉ tin vào phản hồi trong chat.

Nói thẳng, Muse chưa thay người quản lý nội dung. Nó vẫn có thể chọn sai nguồn, sai file hoặc viết một câu rất tự tin nhưng vô duyên.

Giá trị thật nằm ở chỗ khác. Một agent có thể nối Facebook và YouTube thành một workflow có kiểm soát.

AI làm phần lặp lại. Mình giữ context, quyền duyệt và trách nhiệm cuối cùng.

Mình để toàn bộ prompt trong phần mô tả. Comment workflow bạn muốn Muse làm tiếp theo.

Tập sau, mình rời bàn làm việc và điều khiển Muse từ điện thoại. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: ~8:40 (520 giây).** Footage gốc dài khoảng 18:15. Chỉ giữ thao tác có giá trị chứng minh. Mốc dưới đây là mốc dựng gần đúng; chốt theo frame trên timeline.

**Thứ tự clip:** Facebook 1 → Facebook 2 → YouTube 1 → YouTube 2 → YouTube 3.

| # | Thành phẩm | Loại | Nguồn | Nội dung giữ | Cách dựng |
|---|---:|---|---|---|---|
| 1 | 15s | **[BROWSER]** | FB1 `00:00–00:25` + YT1 `00:00–00:08` | Muse, Facebook, YouTube | Ba cut nhanh; bỏ con trỏ đứng yên. |
| 2 | 15s | **[DIAGRAM]** | Bổ sung | Hai dashboard → agent → người duyệt | Một sơ đồ duy nhất. |
| 3 | 30s | **[BROWSER]** | FB1 `00:20–01:20` | Kiểm tra kết nối, chọn đúng Page | Tua tải trang; tốc độ thật lúc chọn Page. |
| 4 | 35s | **[BROWSER]** | FB1 `01:25–02:50` | Báo cáo 28 ngày | Jump cut giữa chỉ số; zoom follower mới. |
| 5 | 20s | **[BROWSER]** | FB1 `02:55–03:20` | Prompt tìm tin và tạo draft | Overlay prompt; không giữ toàn bộ thao tác gõ. |
| 6 | 42s | **[BROWSER + DIAGRAM]** | FB1 `03:20–04:20` | Tìm nguồn, draft PHP | Tua 6–8x; overlay workflow sáu bước. |
| 7 | 30s | **[BROWSER]** | FB1 `04:20–05:05` | Review, mở Short, thêm link | Short chỉ xuất hiện 3–4 giây. |
| 8 | 38s | **[BROWSER]** | FB1 `05:05–06:10` | Thêm ảnh, xin quyền, publish | Tốc độ thật ở Allow; jump cut tới kết quả. |
| 9 | 25s | **[BROWSER]** | FB1 `06:10–06:40` | Kiểm tra bài trên Facebook | Crop sidebar; giữ ảnh, chữ và link. |
| 10 | 25s | **[BROWSER]** | FB1 `06:40–08:25` | Draft tiếp theo và prompt tạo job | Chỉ giữ prompt, kết quả và chữ “draft”. |
| 11 | 18s | **[BROWSER]** | FB1 `08:25–10:23` | Tạo job và lịch | Cắt mạnh; task cuối giữ 5 giây. |
| 12 | 10s | **[BROWSER]** | FB2 `00:00–00:31` | Bằng chứng Facebook bổ sung | Montage tối đa 10 giây. |
| 13 | 32s | **[BROWSER]** | YT1 `00:00–01:10` | Google OAuth, secure credentials | Tua 5–8x; che email và dữ liệu nhạy cảm. |
| 14 | 30s | **[BROWSER]** | YT1 `01:10–02:10` | Tóm tắt kênh, danh sách Shorts | Giữ một màn hình Studio rõ nhất. |
| 15 | 30s | **[BROWSER]** | YT1 `02:10–03:30` | Chọn file và plan upload | Nén chat thành: file → metadata → review. |
| 16 | 24s | **[BROWSER]** | YT1 `03:30–04:55` | Browser session mở Studio | Tua 8x; dừng ở nút upload. |
| 17 | 30s | **[BROWSER]** | YT2 `00:00–00:55` | File, tiêu đề, audience | Jump cut từng quyết định; bỏ chờ upload. |
| 18 | 25s | **[BROWSER]** | YT3 `00:00–00:35` | Visibility, hoàn tất upload | Giữ popup xác nhận và danh sách Content. |
| 19 | 30s | **[BROWSER]** | YT3 `00:35–01:20` | Đăng và kiểm tra comment | Chỉ giữ một lần comment xuất hiện. |
| 20 | 16s | **[BROWSER + B-ROLL]** | YT3 `01:20–01:30` | Short chạy trên kênh thật | Fade sang logo; outro ngắn. |

**Tổng: 520 giây ≈ 8:40.**

### Những đoạn nên cắt hoặc rút ngắn

- **FB1:** Tua 4–8x mọi đoạn Muse chờ. Không scroll đọc cùng một draft nhiều lần.
- **FB1 `08:25–10:23`:** Workflow tạo job dài gần hai phút. Chỉ giữ prompt, lịch và task cuối.
- **FB2:** Chỉ là bằng chứng bổ sung. Dùng tối đa 15 giây, không kể lại quy trình.
- **YT1 `01:35–02:00`:** Đoạn mở Google Chat không phục vụ câu chuyện. Cắt hoàn toàn.
- **YT1:** OAuth và secure credentials lặp lại chỉ giữ xác nhận cuối. Che email, token và tài khoản.
- **YT1 `03:30–04:55`:** Browser session tải lâu. Tua 8x hoặc jump cut tới Studio.
- **YT2:** Mỗi quyết định trong wizard chỉ cần một shot: file, metadata, audience, visibility.
- **YT3:** Các frame comment giống nhau. Giữ thao tác đăng và một frame xác nhận.
- Nếu narration kết thúc trước footage, cắt footage ngay. Không giữ cảnh chờ để đủ thời lượng.

**Cài đặt:** Crop giao diện đủ lớn để đọc trên điện thoại, zoom 125–150%. Nếu quay bổ sung, dùng One Dark Pro, JetBrains Mono tối thiểu 18px, ẩn sidebar và minimap. Giữ ánh sáng cyan/tím và monitor glow.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. A cinematic photograph of a Vietnamese developer controlling Facebook and YouTube dashboards from one AI agent interface, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, reflection of approval buttons on eyeglasses, shallow depth of field, bokeh city lights through window, 8k, 16:9, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

2. A cinematic photograph of a human hand hovering over a glowing approval switch between floating Facebook and YouTube panels, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, film grain, anamorphic lens flare, 8k, 16:9, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

3. A cinematic photograph of a developer desk at 3 AM with an AI agent preparing a Facebook draft on one monitor and uploading a YouTube Short on another, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, 16:9, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Tôi giao Facebook và YouTube cho AI — nhưng giữ lại một quyền | Lập trình là cuộc sống
2. Muse quản lý cả Facebook Page lẫn YouTube thế nào? | Lập trình là cuộc sống
3. Một AI, hai kênh, và nút Đăng vẫn thuộc về tôi | Lập trình là cuộc sống
4. AI đăng Facebook, upload Shorts và comment được đến đâu? | Lập trình là cuộc sống
5. Đừng để AI tự quản lý kênh của bạn | Lập trình là cuộc sống
6. Từ Facebook draft đến YouTube Short trong một workflow | Lập trình là cuộc sống
7. Muse có thể thay người quản lý nội dung không? | Lập trình là cuộc sống
8. Tôi thử dùng Muse quản lý hai kênh cùng lúc | Lập trình là cuộc sống
9. AI làm nội dung rất nhanh — và sai cũng rất nhanh | Lập trình là cuộc sống
10. Quản lý Facebook và YouTube bằng AI, không mất quyền kiểm soát | Lập trình là cuộc sống

**Khuyên dùng:** Title 1.

---

## PART 5 — THUMBNAIL PACKAGE (3 OPTIONS)

### Option 1 — AI QUẢN 2 KÊNH

**Image prompt:** A cinematic photograph, a Vietnamese developer silhouette on the right controlling two giant floating Facebook and YouTube panels through one luminous AI interface, dramatic neon green and cyan lighting, exaggerated floating code elements and approval icons, dark moody background with rainy city bokeh, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `AI QUẢN` trắng / `2 KÊNH` xanh `#00FF41` / badge `TÔI GIỮ QUYỀN ĐĂNG` trắng, nền `#1a1a2e`, viền xanh.

### Option 2 — ĐỪNG TRAO NÚT ĐĂNG

**Image prompt:** A cinematic photograph, a human hand on the right holding a glowing physical publish key while an AI silhouette operates floating Facebook posts and YouTube Shorts behind it, dramatic neon green, cyan, and purple lighting, exaggerated floating code text, dark moody background with rain and city bokeh, extreme contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, key visual positioned on the right leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `ĐỪNG TRAO` trắng / `NÚT ĐĂNG` xanh `#00FF41` / badge `CHO AI` trắng, nền `#1a1a2e`, viền xanh.

### Option 3 — 1 AI, 2 DASHBOARD

**Image prompt:** A cinematic photograph, a developer watching one AI agent bridge a glowing Facebook dashboard and YouTube Studio dashboard, dramatic neon green and purple lighting, floating draft cards, video upload bars, comments, and code elements, dark moody background with fog and city bokeh, extreme contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `1 AI` xanh `#00FF41` / `2 DASHBOARD` trắng / badge `CÓ KIỂM SOÁT` trắng, nền `#1a1a2e`, viền xanh.

**Typography cho cả ba:** Canvas 1280×720. Font Anton cho hook, JetBrains Mono cho badge. Mỗi line cao 110–140px, line spacing 0.85. Text block chiếm một phần ba bên trái. Neon blur 8–12px, opacity 60–70%, black stroke 6–10px. Không đè chữ lên mặt hoặc key visual. Thêm noise nhẹ. Typeset trong Canva và giữ bản sạch không chữ.

---

## PART 6 — YOUTUBE SEO

### Description

```text
Mình thử dùng Muse quản lý cả Facebook Page và YouTube: đọc số liệu, tìm tin, tạo draft, làm ảnh, đăng bài, upload Short và comment.

Điểm quan trọng không phải AI bấm được bao nhiêu nút. Đó là nơi workflow buộc AI dừng lại để người quản trị review, approve và kiểm chứng.

⏩ 0:00 — Hai dashboard và một đống việc lặp lại
⏩ 0:45 — Kết nối đúng một Facebook Page
⏩ 1:20 — Muse đọc số liệu 28 ngày
⏩ 2:05 — Tìm tin và tạo draft có nguồn
⏩ 3:20 — Review, thêm ảnh và link Shorts
⏩ 4:15 — Duyệt đăng và kiểm chứng Facebook
⏩ 5:00 — Tạo job hằng ngày, chỉ lưu draft
⏩ 5:40 — Kết nối kênh YouTube
⏩ 6:30 — Upload Short trong YouTube Studio
⏩ 7:45 — Review metadata và visibility
⏩ 8:25 — Đăng comment và kiểm chứng

#MuseAI #FacebookPage #YouTubeStudio #AIAgent
```

### Tags

`Muse AI, quản lý Facebook Page bằng AI, quản lý YouTube bằng AI, AI upload YouTube Shorts, AI đăng bài Facebook, AI comment YouTube, Facebook Page automation, YouTube Studio automation, AI agent social media, Meta Business Manager, lập trình là cuộc sống`

### Pinned Comment

```text
Workflow mình dùng: AI chuẩn bị → mình kiểm tra nguồn và file → review quyền → approve → mở nền tảng thật để kiểm chứng.

Bạn muốn mình thử sâu hơn phần Facebook draft hay workflow upload YouTube Shorts? 👇
```
