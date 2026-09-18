# BONUS 20.5 — Observe, Sentry hay OpenTelemetry?

- **Series:** Học NestJS bằng AI — bonus sau tập 20
- **Target runtime:** khoảng 6 phút (540–580 từ thoại)
- **Outcome:** Chọn một hướng observability bằng decision matrix, không cài ba stack vào cùng project.

---

## PART 1 — SCRIPT

Sau tập Observe, câu hỏi xuất hiện ngay: vậy Sentry và OpenTelemetry thì sao?

Mình từng trả lời bằng cách cài cả ba vào một project thử nghiệm.

Kết quả là ba SDK, ba cách đặt tên span và một hóa đơn khó giải thích.

Nhiều telemetry hơn không tự động tạo ra nhiều hiểu biết hơn.

Bước ngoặt là chọn công cụ từ câu hỏi cần trả lời, không từ danh sách tính năng dài nhất.

Mình dùng cùng một lỗi và cùng một request chậm để so sánh.

NestJS Observe đi từ framework ra ngoài.

Nó hiểu controller, provider, resolver và queue consumer bằng tên NestJS.

Điểm mạnh là setup ít và trace đọc giống call graph của project.

Đổi lại, mình phải đánh giá nơi dữ liệu đi tới và chi phí hiện tại.

Mức phụ thuộc nền tảng cũng cần được ghi rõ.

Sentry đi rất mạnh từ lỗi về ngữ cảnh.

Error grouping, stack trace, release và breadcrumb giúp trả lời lỗi nào đang ảnh hưởng user.

Tracing có thể mở rộng bức tranh, nhưng trải nghiệm cốt lõi vẫn rất hợp với error tracking.

OpenTelemetry lại không phải một dashboard cụ thể.

Nó là chuẩn mở cùng SDK, semantic convention và giao thức xuất telemetry.

Mình có thể gửi OTLP tới nhiều backend hoặc collector do mình vận hành.

Sự linh hoạt đó đi kèm nhiều quyết định hơn về instrumentation, collector, storage và dashboard.

Mình đưa AI requirement của TaskFlow, không đưa tên công cụ yêu thích.

Requirement gồm một service NestJS, team nhỏ và lỗi production cần điều tra nhanh.

AI lập decision matrix theo sáu tiêu chí.

Thời gian setup. Độ sâu NestJS. Error workflow. Tính portable. Vận hành. Chi phí thực tế.

Mình không cho AI chấm điểm bằng cảm giác.

Mỗi ô phải gắn với một bằng chứng từ docs và một thử nghiệm giống nhau.

Test đầu tiên là exception trong `TasksService`.

Test thứ hai là external call chậm hai giây.

Test thứ ba là job BullMQ fail sau retry.

Observe cho trace Nest-aware rất nhanh.

Sentry làm luồng triage error và release regression rõ ràng.

OpenTelemetry cho quyền chọn exporter cùng backend, nhưng mình phải ráp nhiều mảnh hơn.

Nếu team chỉ cần sửa lỗi NestJS nhanh với ít vận hành, Observe là ứng viên tự nhiên.

Nếu workflow xoay quanh crash, issue ownership và frontend-backend error, Sentry đáng thử.

Nếu tổ chức nhiều ngôn ngữ cần chuẩn chung và kiểm soát backend, OpenTelemetry có lợi thế.

Đây không phải bảng xếp hạng chung.

Một startup năm người và một platform team trăm service không có cùng bài toán.

Mình cũng kiểm tra pricing và data retention tại ngày ra quyết định.

Những con số đó thay đổi. Không đóng băng chúng trong kiến trúc bằng trí nhớ cũ.

Cuối cùng, mình chọn một stack cho TaskFlow và ghi lại lý do trong ADR.

ADR là bản ghi quyết định kiến trúc, gồm bối cảnh, lựa chọn và tradeoff đã chấp nhận.

Không cài ba agent cùng lúc chỉ để cảm thấy an toàn.

Observability tốt là nhìn rõ hệ thống, không phải nhìn thấy nhiều logo.

Nếu bạn muốn chọn tool bằng workload thật thay vì hype, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [DIAGRAM] | Ba SDK chồng lên một app rồi tạo ba luồng telemetry | 30s |
| 2 | [DIAGRAM] | Một câu hỏi → một tiêu chí lựa chọn | 25s |
| 3 | [BROWSER] | Observe dashboard: controller/provider trace | 35s |
| 4 | [BROWSER] | Sentry demo/docs: grouped error, release và breadcrumb | 35s |
| 5 | [DIAGRAM] | App → OpenTelemetry SDK → Collector → backend tùy chọn | 40s |
| 6 | [BROWSER] | AI dựng matrix sáu tiêu chí; host yêu cầu nguồn cho từng ô | 35s |
| 7 | [TERM] | Chạy cùng exception, slow call và failed job | 45s |
| 8 | [DIAGRAM] | Matrix kết quả theo team nhỏ, error-first, multi-language platform | 50s |
| 9 | [BROWSER] | Kiểm tra pricing/retention hiện hành thay vì ghi số cố định | 25s |
| 10 | [IDE] | Viết ADR ngắn: context, decision, tradeoffs | 35s |
| 11 | [B-ROLL] | Giữ lại một logo/tool, hai logo còn lại mờ đi | 15s |

**Tổng mục tiêu: 6 phút 10 giây.** Dùng cùng dataset và cùng failure scenario; che project ID, token và dữ liệu telemetry thật.

### Decision matrix dùng khi quay

| Nhu cầu chính | Điểm khởi đầu phù hợp |
|---|---|
| Một app NestJS, cần trace theo controller/provider với ít setup | Đánh giá NestJS Observe trước |
| Error triage, issue workflow, release và frontend-backend context | Đánh giá Sentry trước |
| Nhiều ngôn ngữ, OTLP, backend linh hoạt hoặc collector tự quản | Đánh giá OpenTelemetry trước |

### Prompt cho AI

```text
Build an evidence-backed decision matrix for NestJS Observe, Sentry and OpenTelemetry.
- Use the current official docs for every factual claim.
- Compare setup time, NestJS-level visibility, error workflow, portability, operations and current cost model.
- Run the same three scenarios: service exception, slow external call and failed BullMQ job.
- Treat OpenTelemetry as a telemetry standard and SDK ecosystem, not a dashboard product.
- Do not install all three agents in TaskFlow.
- Do not freeze pricing or retention numbers; link the current pages and date the decision.
- Recommend one starting point for this project's actual team and requirements.
- Produce a short ADR with context, decision, alternatives and tradeoffs.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right choosing between three abstract observability paths represented by a Nest trace, an error stack and an open telemetry pipeline, dark black and navy environment with NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no brand text.`
2. `A cinematic photograph of one slow request trace displayed identically across three dark monitoring screens while a developer compares them on the right, deep shadows, NestJS red-pink #E0234E rim light, empty left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer removing two overlapping monitoring agents from a dark NestJS server and keeping one clean telemetry path, black and navy scene, NestJS red-pink #E0234E highlights, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Observe, Sentry hay OpenTelemetry? | Lập trình là cuộc sống
2. Đừng cài ba Stack Observability cùng lúc | Lập trình là cuộc sống
3. Chọn APM theo lỗi thật, không theo hype | Lập trình là cuộc sống
4. NestJS Production nên dùng công cụ nào? | Lập trình là cuộc sống
5. Một Trace, ba công cụ, một quyết định | Lập trình là cuộc sống

**Khuyên dùng:** Title 1.

### 4b. SEO Description

```text
Ba công cụ không tạo ra ba lần hiểu biết. Bonus 20.5 dùng cùng một lỗi và một request chậm để chọn observability stack cho TaskFlow.

✅ So sánh NestJS Observe, Sentry và OpenTelemetry
✅ Phân biệt APM platform với telemetry standard
✅ Dùng sáu tiêu chí có bằng chứng
✅ Chạy cùng failure scenario trên từng lựa chọn
✅ Cân nhắc portability, vận hành và chi phí hiện hành
✅ Ghi quyết định bằng ADR

🔗 NestJS Observe: https://docs.nestjs.com/observability/overview
🔗 Sentry for NestJS: https://docs.sentry.io/platforms/javascript/guides/nestjs/
🔗 OpenTelemetry JavaScript: https://opentelemetry.io/docs/languages/js/

⏱ 0:00 Ba SDK, một mớ rối
⏱ 0:40 Chọn từ câu hỏi cần trả lời
⏱ 1:15 NestJS Observe
⏱ 2:00 Sentry
⏱ 2:45 OpenTelemetry
⏱ 3:40 Cùng một failure scenario
⏱ 4:40 Decision matrix
⏱ 5:35 ADR và kết luận

#NestJS #Observability #Sentry #OpenTelemetry #APM #Tracing #Production #SoftwareArchitecture #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs observe vs sentry, nestjs opentelemetry, observability tools comparison, sentry nestjs, open telemetry nodejs, nestjs apm, distributed tracing nestjs, error monitoring nestjs, otlp collector, vendor lock in observability, self hosted telemetry, architecture decision record, học nestjs bằng ai, production monitoring, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `OBSERVE` — WHITE `#FFFFFF`
- `SENTRY HAY OTEL?` — NEST RED `#E0234E`
- Badge nhỏ: `BONUS 20.5`

### Option 2
- `3 CÔNG CỤ` — WHITE `#FFFFFF`
- `CHỌN 1` — NEST RED `#E0234E`
- Badge nhỏ: `APM`

### Option 3
- `ĐỪNG CHỌN` — WHITE `#FFFFFF`
- `THEO HYPE` — NEST RED `#E0234E`
- Badge nhỏ: `TRACE`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
