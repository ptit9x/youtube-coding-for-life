# NestJS #19 — Structured Logging và Correlation ID

- **Series:** Học NestJS bằng AI — tập 19/45
- **Target runtime:** khoảng 6 phút (547 từ thoại)
- **Outcome:** Log JSON bằng Pino, một correlation ID xuyên request và dữ liệu nhạy cảm được redact.
- **Pain tập kế:** Log cho biết lỗi gì, nhưng chưa cho thấy Guard, Service hay database đang chậm.

---

## PART 1 — SCRIPT

Hai giờ sáng, TaskFlow báo năm-trăm giữa hàng nghìn dòng log.

Một dòng nói permission fail. Dòng khác nói database timeout.

Không ai biết chúng có thuộc cùng một request hay không.

Mình thử tìm theo user ID.

Một user có thể mở nhiều tab. Email còn xuất hiện trong những request chẳng liên quan.

Timestamp cũng không cứu được khi ba instance cùng ghi log.

Log có rất nhiều chữ. Nó lại thiếu đúng sợi dây nối các chữ đó với nhau.

Bước ngoặt là cho mỗi request một correlation ID ngay khi nó bước vào hệ thống.

Correlation ID là mã theo dõi, giống số vận đơn đi qua mọi chặng xử lý.

Structured logging biến log thành dữ liệu có field, không phải một câu văn để đoán.

Mình chọn Pino vì output JSON gọn và phù hợp cho production.

Mình đưa AI một đoạn log rối và yêu cầu lập plan trước.

AI tóm tắt rằng database là nguyên nhân.

Mình chưa tin. Bản tóm tắt không thể tạo ra bằng chứng chưa từng được ghi.

Plan mới phải tạo request ID, truyền nó tự động và kiểm tra redaction.

Client có thể gửi `x-request-id`. Server chỉ nhận khi giá trị hợp lệ.

Nếu không có, server tạo UUID mới.

ID được trả lại trong response để frontend đưa vào ticket hỗ trợ.

Pino tạo child logger cho request.

Mọi log bên trong request tự mang cùng `req.id`, method và path.

Service chỉ ghi sự kiện nghiệp vụ như `task.created` cùng `taskId`.

Nó không cần nối chuỗi dài chứa mọi context.

Mình dùng level có chủ đích.

`info` cho sự kiện bình thường. `warn` cho tình trạng bất thường còn phục hồi được.

`error` cần stack và context để điều tra. `debug` chỉ bật khi thực sự cần.

Rồi mình tìm thấy lỗi nguy hiểm hơn log rối.

AI đã log toàn bộ request body để “dễ debug”.

Login body chứa password. Header chứa bearer token. Cookie chứa refresh token.

Production không cần một vụ rò rỉ được đặt tên là observability.

Mình cấu hình redact cho authorization, cookie, password và set-cookie.

Sau đó mình viết test cố tình gửi chuỗi bí mật dễ nhận diện.

Test đọc output log và phải không tìm thấy chuỗi đó.

Bây giờ mình chạy lại sự cố với ba request song song.

Các dòng vẫn xen kẽ, nhưng mỗi dòng có request ID riêng.

Mình lọc một ID và thấy đường đi rõ ràng.

PermissionGuard đã pass. Query task timeout. ExceptionFilter trả năm-trăm cùng ID.

AI có thể tóm tắt nhóm log này. Mình kiểm tra lại từng kết luận bằng field thật.

Cuối cùng, mình gọi API và nhận `x-request-id` trong response.

Một lỗi production từ đây có thể được tìm lại bằng đúng một mã.

Log tốt không kể nhiều hơn. Nó giúp tìm đúng sự thật nhanh hơn.

Nhưng correlation chỉ nối sự kiện. Nó chưa đo thời gian nằm ở lớp nào.

Tập sau, mình sẽ nhìn request thành một trace waterfall bằng NestJS Observe.

Nếu bạn muốn debug bằng bằng chứng thay vì linh cảm, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERM] | Cuộn log xen kẽ từ ba request, dừng ở lỗi 500 | 30s |
| 2 | [DIAGRAM] | Minh họa request ID như số vận đơn qua Guard, Service, DB, Filter | 30s |
| 3 | [BROWSER] | Cho AI đọc log rối; highlight kết luận thiếu bằng chứng | 30s |
| 4 | [IDE] | Cấu hình `LoggerModule`, `genReqId` và response header | 40s |
| 5 | [IDE] | So sánh log nối chuỗi với log event + fields | 30s |
| 6 | [IDE] | Cấu hình level theo môi trường và `redact.paths` | 35s |
| 7 | [TERM] | Gửi login có password/token giả; kiểm tra log đã `[Redacted]` | 35s |
| 8 | [TERM] | Bắn ba request song song; dùng `jq` lọc theo `req.id` | 50s |
| 9 | [IDE] | Chạy test không rò password, authorization và cookie | 35s |
| 10 | [BROWSER] | Network tab cho thấy `x-request-id` trong response | 20s |
| 11 | [B-ROLL] | Một request ID sáng lên giữa màn hình log; chuyển sang trace waterfall | 15s |

**Tổng mục tiêu: 5 phút 50 giây.** One Dark Pro, JetBrains Mono 18–20px, format JSON qua `jq`, tuyệt đối không quay secret thật.

### Code cốt lõi

```ts
LoggerModule.forRoot({
  pinoHttp: {
    genReqId(req, res) {
      const incoming = req.headers['x-request-id'];
      const requestId = isSafeRequestId(incoming) ? incoming : randomUUID();
      res.setHeader('x-request-id', requestId);
      return requestId;
    },
    redact: {
      paths: [
        'req.headers.authorization',
        'req.headers.cookie',
        'req.body.password',
        'res.headers["set-cookie"]',
      ],
      censor: '[Redacted]',
    },
  },
});
```

```ts
const app = await NestFactory.create(AppModule, { bufferLogs: true });
app.useLogger(app.get(Logger)); // Logger từ nestjs-pino
```

```ts
this.logger.info({ event: 'task.created', taskId, ownerId }, 'Task created');
```

### Prompt cho AI

```text
Plan production structured logging for the current NestJS API.
- Use Pino through a Nest integration and preserve Nest application logs.
- Generate or validate one request id and return it as x-request-id.
- Define a small event naming and log-level convention.
- Redact authorization, cookies, refresh tokens, passwords and set-cookie.
- Never log complete request bodies or user records.
- Add tests that fail if sentinel secrets appear in captured logs.
- Produce three concurrent requests and show how to filter one request path.
- Analyze only evidence that exists in the structured fields.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right staring at thousands of dark terminal log lines while one correlation ID glows in NestJS red-pink #E0234E, deep black and navy background, empty left space for headline text, 16:9, photorealistic, high contrast, no text.`
2. `A cinematic photograph of several chaotic streams of JSON logs converging into one bright trace line on a dark monitor, developer face reflected in the screen on the right, NestJS red-pink #E0234E accents, empty left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer holding a support ticket with one glowing request identifier while dark server logs align behind it, subject on the right, deep shadows and NestJS red-pink #E0234E rim light, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Một ID cứu cả đêm debug production — EP19 | Lập trình là cuộc sống
2. Structured Logging và Correlation ID trong NestJS — EP19 | Lập trình là cuộc sống
3. Vì sao nghìn dòng log vẫn không đủ? — EP19 | Lập trình là cuộc sống
4. Đừng bao giờ log password và token — EP19 | Lập trình là cuộc sống
5. Truy một Request xuyên toàn bộ NestJS — EP19 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1. A/B test Title 2 cho search intent.

### 4b. SEO Description

```text
Hàng nghìn dòng log không có nghĩa là bạn truy được một request. Tập 19 thêm structured logging, correlation ID và redaction để debug production bằng bằng chứng.

✅ Dùng Pino cho log JSON
✅ Tạo và trả lại x-request-id
✅ Gắn context tự động cho từng request
✅ Chọn log level có chủ đích
✅ Không log password, token và cookie
✅ Test chống rò dữ liệu nhạy cảm
✅ Lọc một request giữa log từ nhiều instance

🔗 NestJS Logger: https://docs.nestjs.com/techniques/logger
🔗 nestjs-pino: https://github.com/iamolegga/nestjs-pino

⏱ 0:00 Lỗi 500 lúc hai giờ sáng
⏱ 0:35 Log rối thiếu điều gì
⏱ 1:05 Correlation ID
⏱ 1:35 Cấu hình Pino
⏱ 2:25 Event và log level
⏱ 3:15 Redact dữ liệu nhạy cảm
⏱ 4:10 Truy một request thật
⏱ 5:20 Từ log sang trace

#NestJS #StructuredLogging #Pino #CorrelationID #Production #Debugging #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs structured logging, nestjs pino, correlation id nestjs, request id nodejs, pino redact password, log json nestjs, x-request-id, production logging nodejs, debug production nestjs, redact authorization header, nestjs logger, logging best practices, taskflow nestjs, học nestjs bằng ai, nestjs tập 19, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `1 REQUEST` — WHITE `#FFFFFF`
- `1000 DÒNG LOG` — NEST RED `#E0234E`
- Badge nhỏ: `EP 19`

### Option 2
- `TÌM LỖI BẰNG` — WHITE `#FFFFFF`
- `1 CÁI ID` — NEST RED `#E0234E`
- Badge nhỏ: `PINO`

### Option 3
- `ĐỪNG LOG` — WHITE `#FFFFFF`
- `PASSWORD!` — NEST RED `#E0234E`
- Badge nhỏ: `REDACT`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
