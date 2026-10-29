# EP03 — Vibe Coding Với Muse Spark: AI Viết, Mình Vẫn Phải Hiểu

---

## PART 1 — SCRIPT

Vibe coding rất dễ ở năm phút đầu. Bạn mô tả một app, AI tạo cả đống file, rồi màn hình sáng lên như phép màu.

Đến phút thứ sáu, một nút không chạy. Không ai biết state nằm ở đâu. Kể cả người vừa bấm approve.

Mình muốn thử Muse Spark theo cách khác. AI được viết code, nhưng chưa được sửa gì trước khi mình hiểu plan.

Project hôm nay là một status dashboard cho developer. Nó hiển thị API, database và worker đang khỏe hay lỗi.

Không backend, không đăng nhập, không database thật. Scope nhỏ để mình đánh giá workflow, không đánh giá khả năng dựng scaffold.

Mình mở một repo React và gửi context trước.

### 🎬 PROMPT 1 — Yêu cầu và context

> **Mục đích:** Mô tả outcome, stack và giới hạn trước khi AI lên plan.  
> **Conversation:** Mới trong Muse Code hoặc Muse app có quyền đọc repo.  
> **Prompt:**
> ```text
> Đây là project React + TypeScript dùng Vite.
> Hãy xây một developer status dashboard bằng dữ liệu mock.
> Dashboard có 3 service: API, PostgreSQL và background worker.
> Mỗi service có trạng thái, latency và thời điểm kiểm tra cuối.
> Có nút “Run health check” để giả lập cập nhật trạng thái.
> Dùng CSS hiện có, không cài UI library và không thêm backend.
> Trước tiên chỉ phân tích repo và lập plan theo từng file. Chưa sửa code.
> ```
> **Kết quả mong đợi:** Muse trả plan, danh sách file và tiêu chí kiểm chứng.

Muse đọc repo rồi đề xuất component, type, mock data và state ở trang chính.

Plan nhìn hợp lý, nhưng nó định tạo quá nhiều component cho một màn hình nhỏ. Đây là lúc kinh nghiệm giúp tiết kiệm code.

Mình yêu cầu giữ một component `ServiceCard`, một file type và một trang `App`. Chưa cần abstraction cho thứ chỉ dùng một lần.

### 🎬 PROMPT 2 — Thu gọn plan

> **Mục đích:** Review và giảm abstraction trước khi code được tạo.  
> **Conversation:** Tiếp tục conversation hiện tại.  
> **Prompt:**
> ```text
> Thu gọn plan.
> Chỉ tạo ServiceCard.tsx và types.ts; giữ mock data cùng state trong App.tsx.
> Không tạo hook riêng, context hoặc utility chưa cần thiết.
> Bổ sung tiêu chí hoàn thành và cách test.
> Chưa sửa file.
> ```
> **Kết quả mong đợi:** Plan ngắn hơn, có tiêu chí hoàn thành rõ ràng.

Đây là phần nhiều video vibe coding bỏ qua. Code tốt không bắt đầu bằng việc AI gõ nhanh. Nó bắt đầu bằng việc cả hai đồng ý sẽ không xây thừa.

Mình approve plan. Muse bắt đầu sửa file.

### 🎬 PROMPT 3 — Thực hiện theo plan đã duyệt

> **Mục đích:** Cho phép AI code trong phạm vi đã review.  
> **Conversation:** Tiếp tục conversation hiện tại.  
> **Prompt:**
> ```text
> Tôi approve plan vừa chốt.
> Hãy thực hiện đúng phạm vi đó.
> Không cài package mới và không sửa file ngoài danh sách.
> Sau khi xong, chạy typecheck và test hiện có.
> Trả lại danh sách file đã đổi và các lệnh đã chạy.
> ```
> **Kết quả mong đợi:** Muse sửa đúng file, chạy kiểm tra và báo kết quả.

Trong lúc Muse xử lý, mình giải thích state. State là dữ liệu có thể thay đổi và làm giao diện render lại. Ví dụ, service từ xanh chuyển đỏ sau một lần health check.

TypeScript type là hợp đồng của dữ liệu. `status` chỉ được là healthy, degraded hoặc down. Một typo không nên đợi tới browser mới lộ ra.

Muse hoàn tất. Nhưng mình chưa mở app ngay. Mình mở git diff trước.

Diff là phần thay đổi giữa code cũ và mới. Nó giống bản kê trước khi merge: file nào đổi, dòng nào thêm, dòng nào biến mất.

Mình kiểm tra bốn thứ. Không có package lạ. Không có file ngoài plan. State vẫn nằm trong App. Và nút health check không dùng timer vô hạn.

Một chi tiết chưa ổn: Muse dùng index làm key khi render service. Với danh sách cố định, nó chạy. Nhưng `id` đã có sẵn, nên dùng `id` rõ nghĩa hơn.

### 🎬 PROMPT 4 — Sửa một issue từ diff

> **Mục đích:** Sửa đúng phát hiện của host, không mở rộng scope.  
> **Conversation:** Tiếp tục conversation hiện tại.  
> **Prompt:**
> ```text
> Trong ServiceCard list, thay React key đang dùng index bằng service.id.
> Không thay đổi phần khác.
> Sau đó chạy lại typecheck và cho tôi xem diff mới.
> ```
> **Kết quả mong đợi:** Một thay đổi nhỏ, typecheck xanh và diff sạch.

Đây là khoảnh khắc quan trọng. AI không thất bại vì viết một dòng chưa tối ưu. Workflow thất bại nếu mình không đọc được dòng đó.

Mình chạy app. Ba service xuất hiện, latency rõ ràng và màu trạng thái đủ tương phản.

Mình bấm health check. Số liệu đổi, thời gian cập nhật và không có lỗi trong console.

Nhưng test bằng mắt chưa đủ. Mình yêu cầu thêm test cho hành vi chính.

### 🎬 PROMPT 5 — Thêm test sau khi hành vi đã rõ

> **Mục đích:** Khóa hành vi quan trọng bằng test nhỏ.  
> **Conversation:** Tiếp tục conversation hiện tại.  
> **Prompt:**
> ```text
> Lập plan cho đúng 2 test:
> 1. Render đủ 3 service.
> 2. Bấm “Run health check” làm thay đổi thời điểm kiểm tra.
> Nếu project thiếu test runner, hãy đề xuất trước và chờ tôi duyệt.
> Chưa sửa code.
> ```
> **Kết quả mong đợi:** Muse kiểm tra setup test và dừng trước khi cài dependency.

Muse phát hiện repo chưa có test runner. Nó đề xuất Vitest và Testing Library.

Đây là thay đổi dependency, nên mình review rồi mới approve. Sau đó, Muse thêm đúng hai test và chạy lại toàn bộ.

### 🎬 PROMPT 6 — Approve test setup và kiểm chứng

> **Mục đích:** Cài đúng dependency đã duyệt và chạy kiểm chứng cuối.  
> **Conversation:** Tiếp tục conversation hiện tại.  
> **Prompt:**
> ```text
> Tôi approve Vitest, jsdom và Testing Library cho devDependencies.
> Thêm đúng 2 test đã chốt, không mở rộng coverage.
> Chạy test, typecheck và build.
> Nếu tất cả xanh, tóm tắt git diff theo từng file.
> ```
> **Kết quả mong đợi:** Test, typecheck và build đều thành công.

Ba lệnh đều xanh. App không lớn, nhưng workflow đã hoàn chỉnh: yêu cầu, plan, review, approve, code và kiểm chứng.

Vibe coding không có nghĩa là ngừng suy nghĩ. Nó chỉ chuyển phần gõ phím cho AI, để mình dành thời gian cho scope, kiến trúc và bằng chứng.

Code mẫu và prompt nằm trong phần mô tả. Comment phần diff bạn thường bỏ qua khi dùng coding agent.

Tập sau, mình tổng hợp những gì Muse làm tốt, làm chậm và chưa nên tin. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Tổng thời lượng mục tiêu: 8:53 (533 giây).**

| # | Thời lượng | Loại | Narration | Footage cụ thể |
|---|---:|---|---|---|
| 1 | 20s | **[IDE]** | “Vibe coding rất dễ…” | AI tạo file nhanh → app lỗi → console đỏ. |
| 2 | 18s | **[B-ROLL]** | “Đến phút thứ sáu…” | Host nhìn code, con trỏ đứng trước nút hỏng. |
| 3 | 24s | **[BROWSER + IDE]** | “Project hôm nay…” | Preview wireframe dashboard và repo Vite sạch. |
| 4 | 32s | **[IDE]** | Prompt 1 | Paste prompt, Muse scan repo; processing tua 8x. |
| 5 | 35s | **[IDE]** | “Muse đọc repo…” | Scroll plan, highlight số component thừa. |
| 6 | 28s | **[IDE]** | Prompt 2 | Thu gọn plan; before/after tree cạnh nhau. |
| 7 | 25s | **[DIAGRAM]** | “Code tốt không bắt đầu…” | Scope → plan → approve → implementation. |
| 8 | 38s | **[IDE]** | Prompt 3 | Approve; Muse sửa file; narration-over-fast-forward. |
| 9 | 35s | **[DIAGRAM + IDE]** | Giải thích state và type | Service status đổi màu; type union hiện bên cạnh. |
| 10 | 42s | **[IDE]** | “Mình mở git diff…” | `git diff --stat`, rồi diff từng file. |
| 11 | 28s | **[IDE]** | Issue React key | Highlight `key={index}` và `service.id`. |
| 12 | 25s | **[IDE]** | Prompt 4 | Muse sửa đúng một dòng, typecheck xanh. |
| 13 | 38s | **[BROWSER]** | “Mình chạy app…” | Dashboard, responsive width, bấm health check. |
| 14 | 25s | **[BROWSER + TERM]** | “Test bằng mắt…” | Console sạch, mở terminal test setup. |
| 15 | 32s | **[IDE]** | Prompt 5 | Muse đề xuất dependencies và dừng chờ duyệt. |
| 16 | 38s | **[IDE + TERM]** | Prompt 6 | Approve, thêm test; processing tua 8x. |
| 17 | 30s | **[TERM]** | “Ba lệnh đều xanh…” | `npm test`, `npm run typecheck`, `npm run build`. |
| 18 | 20s | **[B-ROLL]** | Kết luận | Dashboard trên monitor, diff sạch, fade logo. |

**Tổng: 533 giây = 8:53.**

**Lưu ý quay:** One Dark Pro, JetBrains Mono 18px, ẩn minimap và sidebar khi review diff. Chỉ giữ processing thật hai đến ba giây rồi tua 6–10x. Không quay secret hoặc đường dẫn cá nhân. File tree, diff, test và app chạy phải là cùng một repo.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. A cinematic photograph of a Vietnamese developer reviewing a massive glowing git diff generated by an AI coding agent, dark moody lighting, monitor glow illuminating the face, neon syntax highlighting in green and cyan on a dark IDE, reflection of code on eyeglasses, shallow depth of field, city bokeh through window, 8k, 16:9, photorealistic, like a high-end developer documentary. Not a screenshot, not a tutorial, not cartoon.
2. A cinematic photograph of an AI agent rapidly generating code on one monitor while a developer holds a glowing approval switch on another, dark moody lighting, neon syntax highlighting in green and cyan, shallow depth of field, rain and city bokeh, film grain, anamorphic lens flare, 8k, 16:9, photorealistic, like a tech commercial. Not a screenshot, not a tutorial, not cartoon.
3. A cinematic photograph of a dark developer desk with a green test suite, a clean git diff and a glowing service status dashboard across three monitors, monitor glow illuminating the scene, neon green and cyan code accents, shallow depth of field, bokeh city lights, 8k, 16:9, photorealistic, like a high-end developer documentary. Not a screenshot, not a tutorial, not cartoon.

---

## PART 4 — TITLES (10)

1. Vibe coding không có nghĩa là ngừng suy nghĩ | Lập trình là cuộc sống
2. Tôi để Muse Spark viết app — nhưng không cho nó tự sửa | Lập trình là cuộc sống
3. AI viết code, tôi chỉ làm 3 việc này | Lập trình là cuộc sống
4. Muse Spark build React app từ một prompt đến đâu? | Lập trình là cuộc sống
5. Đừng chạy app trước khi đọc git diff | Lập trình là cuộc sống
6. Một dòng code cho thấy AI vẫn cần code review | Lập trình là cuộc sống
7. Vibe coding đúng cách: Plan, Diff, Test | Lập trình là cuộc sống
8. Muse Spark viết rất nhanh — workflow mới quyết định chất lượng | Lập trình là cuộc sống
9. Tôi build status dashboard cùng Muse Spark | Lập trình là cuộc sống
10. AI viết, mình hiểu: cách dùng coding agent không copy mù | Lập trình là cuộc sống

**Khuyên dùng:** Title 2.

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — AI VIẾT / TÔI DUYỆT

**Image prompt:** A cinematic photograph, a developer silhouette on the right reviewing a huge floating git diff generated by an AI agent, dramatic neon green and cyan lighting, exaggerated code lines and approval switch, dark rainy city bokeh, extreme contrast, empty dark space on the left, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `AI VIẾT` trắng / `TÔI DUYỆT` xanh `#00FF41`.

### Option 2 — ĐỪNG COPY MÙ

**Image prompt:** A cinematic photograph, an AI hand offering glowing code while a developer stops it with a review gesture, dramatic neon green and purple rim lighting, floating diff markers and test checks, deep shadows, empty dark text space on the left, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `ĐỪNG` trắng / `COPY MÙ` xanh `#00FF41`.

### Option 3 — PLAN / DIFF / TEST

**Image prompt:** A cinematic photograph, three giant luminous panels labeled by visual symbols for plan, git diff and green tests above a dark coding desk, dramatic neon green and cyan lighting, code reflections, extreme contrast, key visual on the right leaving empty space on the left, 8k, 16:9. Photorealistic, not cartoon or illustration.

**Text:** `PLAN` trắng / `DIFF` trắng / `TEST` xanh `#00FF41`.

**Typography chung:** Canvas 1280×720. Anton cho hook, JetBrains Mono cho badge. Mỗi line cao 110–140px, spacing 0.85. Text bên trái khoảng một phần ba khung. Neon blur 10px, opacity 65%, black stroke 8px. Typeset trong Canva và lưu bản sạch.

---

## PART 6 — YOUTUBE SEO

### Description

```text
Mình dùng Muse Spark build một React status dashboard, nhưng AI không được tự sửa trước khi mình review plan. Sau đó mình kiểm tra git diff, sửa một issue và chạy test, typecheck, build.

⏩ 0:00 — Vibe coding hỏng ở phút thứ sáu
⏩ 0:38 — Chốt scope cho status dashboard
⏩ 1:34 — Muse lên plan, mình cắt abstraction thừa
⏩ 2:49 — Approve và để Muse code
⏩ 3:52 — State và TypeScript type thực sự làm gì
⏩ 4:27 — Review git diff trước khi chạy app
⏩ 5:37 — Một issue nhỏ AI bỏ qua
⏩ 6:30 — Chạy app và health check
⏩ 7:13 — Thêm test, typecheck và build

#MuseSpark #VibeCoding #React
```

### Tags

`Muse Spark, Muse Code, vibe coding, AI coding agent, React TypeScript, git diff, code review AI, AI viết code, Vitest, status dashboard, lập trình bằng AI, lập trình là cuộc sống`

### Pinned Comment

```text
Workflow của tập này: yêu cầu → plan → review → approve → code → git diff + test.

Khi dùng coding agent, bạn thường bỏ qua plan, diff hay test? 👇
```
