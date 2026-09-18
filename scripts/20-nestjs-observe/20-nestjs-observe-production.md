# NestJS #20 — Observe: nhìn xuyên request production

- **Series:** Học NestJS bằng AI — tập 20/45
- **Target runtime:** khoảng 6 phút 35 giây (595 từ thoại)
- **Outcome:** NestJS Observe ghi request, error và trace; xác định span chậm bằng telemetry thật.
- **Pain tập kế:** User báo lỗi task nhưng chưa thể đính kèm ảnh hoặc file.

---

## PART 1 — SCRIPT

Correlation ID cho biết những log nào thuộc cùng một request.

Nó vẫn không nói ba giây đã biến mất ở Guard, Service hay database.

Mình đọc code và đoán query chậm. Một lần nữa, production không quan tâm linh cảm.

Mình thêm timer thủ công quanh từng method.

Log nhiều hơn, nhưng các khoảng thời gian vẫn rời rạc.

Một request gọi sang service khác thì bức tranh lại vỡ.

Bước ngoặt là ngừng hỏi code nào trông chậm, và đo request thật đang chậm ở đâu.

Trace là hành trình của một request. Span là từng chặng bên trong hành trình đó.

Waterfall đặt các span trên cùng trục thời gian, nên khoảng chờ không còn vô hình.

NestJS Observe là nền tảng observability chính thức, hiểu lifecycle riêng của Nest.

Nó nhìn thấy controller, provider, resolver và queue consumer bằng đúng tên trong code.

Trước khi cài, mình kiểm tra phiên bản.

SDK cần Nest core từ mười-một chấm một chấm bốn.

Mình cũng quyết định dữ liệu nào được phép rời khỏi hệ thống.

API key, app secret và source context đều là quyết định production, không phải checkbox vô hại.

Mình đưa AI tài liệu chính thức cùng mục tiêu tạo một endpoint chậm có kiểm soát.

AI lập plan. Mình review credential, redaction, sampling và release ID rồi mới approve.

`createObserveModule` trả về module và instrument hook cùng một cấu hình.

Module nhận service ID, version deploy và credential từ environment đã validate.

Hook phải được truyền vào `NestFactory.create` trước khi ứng dụng nhận request.

Đặt nó sai vị trí có thể làm dashboard im lặng mà app vẫn chạy bình thường.

Mình bật trace cho HTTP và giữ log forwarding ở phạm vi demo.

Production thật cần redact token, cookie và field nhạy cảm trước khi gửi telemetry.

Mình tạo endpoint báo cáo task cố tình chậm.

Service chờ một truy vấn tổng hợp, rồi gọi một provider giả lập bên ngoài.

Request mất gần ba giây.

Nhìn từ log, hai bước đều “đã hoàn tất”.

Nhìn trên waterfall, provider bên ngoài chiếm hơn hai giây.

P-chín-mươi-lăm là mốc mà chín mươi lăm phần trăm request nhanh hơn hoặc bằng.

Một request chậm có thể ngẫu nhiên. P-chín-mươi-lăm tăng sau release mới là tín hiệu đáng điều tra.

Observe gắn service version vào telemetry.

Mình so release hiện tại với commit trước và thấy latency tăng đúng sau deploy.

AI nhận trace đã chọn, rồi đề xuất tối ưu query database.

Mình từ chối. Span database chỉ mất tám mươi mili giây.

Span external provider mới là bằng chứng.

Mình thêm timeout và fallback tại đúng boundary đó.

Chạy lại cùng kịch bản, request còn dưới một giây.

Waterfall mới xác nhận span chậm đã biến mất. Test vẫn xanh.

Observability không sửa lỗi thay mình. Nó thu hẹp nơi cần suy nghĩ.

MCP đọc dữ liệu có thể tiện cho AI, nhưng không phải điều kiện của flow này.

Copy một trace đã redact cũng đủ để phân tích. Con người vẫn xác minh trên dashboard.

Log cho ta lời kể. Trace cho ta thời gian. Code cho ta nguyên nhân.

Khi ba thứ khớp nhau, mình mới sửa production.

Tập sau, TaskFlow sẽ nhận file mà không tin tên file người dùng gửi lên.

Nếu bạn muốn quan sát hệ thống trước khi tối ưu nó, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERM] | Một request có correlation ID nhưng chỉ thấy tổng thời gian ba giây | 25s |
| 2 | [DIAGRAM] | Vẽ trace và các span Guard → Service → DB → external provider | 30s |
| 3 | [BROWSER] | Mở docs Observe chính thức, highlight yêu cầu phiên bản và dữ liệu thu thập | 25s |
| 4 | [BROWSER] | Review plan về credential, redaction, sampling và serviceVersion | 30s |
| 5 | [IDE] | Tạo `observe.ts`, `forRootAsync` và env validation | 40s |
| 6 | [IDE] | Truyền `instrument: ObserveInstrument` trong bootstrap | 25s |
| 7 | [IDE] | Tạo endpoint chậm có hai dependency; gọi bằng `curl` | 40s |
| 8 | [BROWSER] | Mở waterfall, self-time và error context | 45s |
| 9 | [DIAGRAM] | Giải thích p95 bằng 100 chấm request, đánh dấu 95 | 25s |
| 10 | [BROWSER] | So sánh release theo `GIT_SHA`; chọn trace regression | 30s |
| 11 | [BROWSER] | Đưa trace đã redact cho AI; bác đề xuất tối ưu sai span | 30s |
| 12 | [IDE] | Thêm timeout/fallback, chạy lại và xác nhận waterfall mới | 35s |
| 13 | [B-ROLL] | Trace chuyển xanh; cut sang form upload attachment | 15s |

**Tổng mục tiêu: 6 phút 35 giây.** One Dark Pro, font 18–20px. Che app key, app secret, user data và URL nội bộ trên dashboard.

### Code cốt lõi

```ts
// observe.ts
export const { ObserveModule, ObserveInstrument } = createObserveModule({
  sourceContext: false,
  attachTraceIdToLogs: true,
});
```

```ts
ObserveModule.forRootAsync({
  imports: [ConfigModule],
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    appKey: config.getOrThrow('OBSERVE_APP_KEY'),
    appSecret: config.getOrThrow('OBSERVE_APP_SECRET'),
    serviceId: 'taskflow-api',
    serviceVersion: config.getOrThrow('GIT_SHA'),
    forwardLogs: true,
  }),
});
```

```ts
const app = await NestFactory.create(AppModule, {
  instrument: ObserveInstrument,
});
```

### Prompt cho AI

```text
Plan a minimal NestJS Observe integration for TaskFlow using only current official docs.
- Verify the installed @nestjs/core version is compatible before editing.
- Load app key, app secret and release version from validated environment config.
- Decide source context, log forwarding, redaction and trace sampling explicitly.
- Pass the instrument hook at bootstrap and add a verification request.
- Create one controlled slow path with a database span and an external-provider span.
- Analyze the captured waterfall and self-time; do not infer from code appearance.
- Compare the current serviceVersion with the previous release.
- Keep MCP optional and read-only; the primary flow must work from the dashboard.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right watching a luminous request trace waterfall cut through a dark monitor, one long red span standing out, deep black and navy background with NestJS red-pink #E0234E highlights, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of a dark NestJS application visualized as transparent layers from guard to service to database, developer face on the right seeing through every layer, NestJS red-pink #E0234E rim light, empty dark left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer comparing two release timelines on a dark observability dashboard, the newer release has one dramatic red latency spike, subject right, NestJS red-pink #E0234E accents, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. NestJS Observe: Nhìn xuyên Request Production — EP20 | Lập trình là cuộc sống
2. Ba giây của API đã biến mất ở đâu? — EP20 | Lập trình là cuộc sống
3. Đừng tối ưu code trước khi nhìn Trace — EP20 | Lập trình là cuộc sống
4. Tìm đúng Method làm NestJS chậm — EP20 | Lập trình là cuộc sống
5. Log chưa đủ: Production cần Trace — EP20 | Lập trình là cuộc sống

**Khuyên dùng:** Title 2. A/B test Title 1 cho chủ đề mới NestJS Observe.

### 4b. SEO Description

```text
Correlation ID nối được log, nhưng chưa nói ba giây nằm ở Guard, Service hay database. Tập 20 dùng NestJS Observe để chẩn đoán bằng trace thật.

✅ Hiểu trace, span và waterfall
✅ Tích hợp @nestjs/observe đúng bootstrap
✅ Gắn release bằng GIT_SHA
✅ Quyết định redaction, source context và sampling
✅ Đọc p95 và self-time
✅ Bác đề xuất AI không khớp telemetry
✅ Xác minh cải thiện bằng trace mới

🔗 NestJS Observe overview: https://docs.nestjs.com/observability/overview
🔗 Observe SDK: https://docs.nestjs.com/observability/sdk

⏱ 0:00 Ba giây biến mất
⏱ 0:35 Trace và span
⏱ 1:05 Observe hiểu gì về NestJS
⏱ 1:35 Review dữ liệu telemetry
⏱ 2:20 Tích hợp SDK
⏱ 3:15 Tạo endpoint chậm
⏱ 4:05 Đọc waterfall và p95
⏱ 5:10 AI đoán sai span
⏱ 6:00 Sửa và xác minh

#NestJS #NestJSObserve #Observability #Tracing #APM #Production #Performance #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs observe, @nestjs/observe, nestjs observability, distributed tracing nestjs, trace waterfall nodejs, nestjs p95 latency, debug slow api nestjs, nestjs production monitoring, nestjs instrument hook, observe serviceVersion, api performance tracing, nestjs telemetry, học nestjs bằng ai, nestjs tập 20, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `3 GIÂY` — WHITE `#FFFFFF`
- `MẤT Ở ĐÂU?` — NEST RED `#E0234E`
- Badge nhỏ: `EP 20`

### Option 2
- `NHÌN XUYÊN` — WHITE `#FFFFFF`
- `REQUEST` — NEST RED `#E0234E`
- Badge nhỏ: `OBSERVE`

### Option 3
- `ĐỪNG ĐOÁN` — WHITE `#FFFFFF`
- `HÃY TRACE` — NEST RED `#E0234E`
- Badge nhỏ: `P95`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
