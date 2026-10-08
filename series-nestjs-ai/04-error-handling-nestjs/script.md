# Một email trùng làm NestJS crash 500 — sửa đúng lỗi 409 | TaskFlow #4

- **Series:** Học NestJS bằng AI — tập 4/45
- **Target runtime:** 5:00–6:00 (khoảng 500 từ thoại)
- **Outcome:** Chuẩn hóa lỗi 400, 404, 409; che chi tiết nội bộ khỏi client; map trực tiếp sqlState 23505 trong repository.
- **Pain mở EP05:** API đã báo lỗi đẹp nhưng chưa có Auth, ai cũng gọi được.

---

## PART 1 — SCRIPT

Mình gửi lại đúng email vừa tạo trên Postman. NestJS lập tức trả 500 Internal Server Error như thể cả server vừa sập.

Nhìn vào log Docker, PostgreSQL chỉ đang báo một lỗi rất bình thường: unique constraint, tức là email này đã tồn tại. API lại biến một xung đột dữ liệu thành lỗi hệ thống nghiêm trọng.

Tệ hơn, nếu không cẩn thận, những lỗi 500 kiểu này có thể làm lộ nguyên một đoạn stack trace, query database và chi tiết hạ tầng ra ngoài client.

Nhiều người sẽ sửa nhanh bằng cách bọc `try/catch` rồi trả về `BadRequestException` cho xong chuyện. Nhưng không tìm thấy user, email trùng, và database mất kết nối không phải là cùng một loại lỗi.

Mình mở docs của NestJS. Bước ngoặt ở đây là phải hiểu và tách bạch ba lớp ngôn ngữ: Database nói ngôn ngữ kỹ thuật, Service nói ngôn ngữ nghiệp vụ, và HTTP phản hồi mã status cho client. Nó giống như phòng cấp cứu, cùng là đau nhưng mỗi ca cần một phác đồ phân loại khác nhau.

Thay vì tự sửa từng chỗ, mình yêu cầu AI audit toàn bộ request flow của Users. Nó phải liệt kê mọi điểm có thể fail trước khi chạm vào code.

AI vạch ra một danh sách rõ ràng: Dữ liệu sai định dạng từ payload, user không tồn tại, email trùng lặp, và PostgreSQL sập. 

Mình chốt plan chia làm hai lớp trách nhiệm. 

Đầu tiên, AI tạo một `HttpExceptionFilter` dùng chung. Filter này đóng vai trò như bảo vệ cổng. Bất cứ lỗi nghiệp vụ nào ném ra cũng được nó định dạng lại thành JSON chuẩn mực, và tuyệt đối chặn không cho stack trace lọt ra ngoài. Client chỉ nhận mã lỗi sạch, còn log chi tiết vẫn được giữ lại trên terminal của server.

Thứ hai, với Prisma 8, thay vì tạo thêm một filter phức tạp, mình bắt lỗi trực tiếp ngay trong repository. Postgres có một mã lỗi chuẩn cho việc trùng lặp dữ liệu là `23505`. Khi catch được mã `sqlState` này, mình chủ động ném ra `ConflictException`. 

Quy tắc rất đơn giản: Lỗi nào đã biết và kiểm soát được thì dịch sang 409 để báo cho client. Lỗi nào lạ, ngoài dự kiến, cứ để nó ném ra 500 để chúng ta vào debug.

Agent tự động chạy một loạt khói test xanh lét trên terminal. Mình kiểm chứng lại bằng request thật trên Postman.

Giờ đây, gửi email trùng, API trả 409 Conflict gọn gàng. Gửi email sai định dạng, nhận 400 Bad Request. Mọi thứ hoạt động hoàn hảo.

Một API chuyên nghiệp không phải là API không bao giờ lỗi. Nó là API nói đúng lỗi, đúng người, và đúng mức độ chi tiết.

Thế nhưng, API của chúng ta hiện tại vẫn đang mở toang. Mọi request nãy giờ đều đi qua trót lọt. Dù lỗi có đẹp đến đâu, ai biết URL cũng có thể kéo toàn bộ dữ liệu user về.

Tập sau, chúng ta sẽ nói về 401 Unauthorized và 403 Forbidden. Đã đến lúc hệ thống phải biết request này đến từ ai, trước khi cho phép họ làm bất cứ điều gì.

---

## PART 2 — SHOT LIST / CUE SHEET

Dưới đây là cue sheet khớp chính xác với video đã quay. Khi dựng, hãy đối chiếu narration với các nhịp hình này:

| # | Type | Nội dung hình ảnh (theo video) | Nhịp thoại tương ứng |
|---|---|---|---|
| 1 | [BROWSER] | Postman: POST trùng email, nhận lỗi 500. | *Mình gửi lại đúng email vừa tạo...* |
| 2 | [TERM] | VS Code: Mở Docker terminal xem log PostgreSQL báo lỗi `duplicate key value`. | *Nhìn vào log Docker, PostgreSQL...* |
| 3 | [BROWSER] | Đọc tài liệu NestJS về Exception Filters & Built-in HTTP exceptions. | *Mình mở docs của NestJS. Bước ngoặt...* |
| 4 | [IDE] | Viết prompt dài yêu cầu Cursor AI audit request flow. | *Thay vì tự sửa từng chỗ, mình yêu cầu AI...* |
| 5 | [IDE] | Cuộn đọc bản phân tích chi tiết của AI và các lớp xử lý. | *AI vạch ra một danh sách rõ ràng...* |
| 6 | [IDE] | AI tự động sinh file `http-exception.filter.ts` và tích hợp vào `main.ts`. | *Đầu tiên, AI tạo một HttpExceptionFilter...* |
| 7 | [IDE] | Trong `prisma-users.repository.ts`, AI thêm đoạn catch `sqlState === '23505'`. | *Thứ hai, với Prisma 8, thay vì tạo thêm...* |
| 8 | [TERM] | AI tự chạy Smoke Test trong terminal báo xanh (Passed). | *Agent tự động chạy một loạt khói test...* |
| 9 | [BROWSER] | Trở lại Postman: Test POST trùng email -> nhận 409. Test email sai -> nhận 400. | *Giờ đây, gửi email trùng, API trả 409...* |
| 10 | [BROWSER] | Tra Google mã HTTP 401 và 403 trên REST API Tutorial. | *Thế nhưng, API của chúng ta hiện tại...* |

**Ghi chú khi dựng:** Video gốc dài 9:36. Thoại dài khoảng 4 phút rưỡi. Hãy speed up hoặc cắt bớt những đoạn chờ AI gõ code và cuộn đọc để ép video xuống mức 5-6 phút. Giữ nguyên độ dài ở các điểm nhấn như lúc chạy Postman và kết quả smoke test.

### Response contract thực tế trong video

```json
{
  "statusCode": 409,
  "timestamp": "2026-10-02T06:40:00.000Z",
  "path": "/users",
  "message": "User with this email already exists"
}
```

### Prisma 8 error mapping (thực tế trong video)

```typescript
try {
  // Thực hiện query Prisma ở đây...
} catch (error) {
  // Prisma 8 surfaces native pg errors as SqlServerError
  // unique constraint violates returns Postgres SQLSTATE 23505
  if (error && typeof error === 'object' && 'sqlState' in error) {
    if ((error as any).sqlState === '23505') {
      throw new ConflictException('User with this email already exists');
    }
  }
  
  throw error;
}
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph matching the established TaskFlow NestJS thumbnail style, a Vietnamese developer with a tense expression on the right facing a dark monitor showing one large glowing HTTP 500 error caused by a duplicate email, deep black and navy room, dramatic NestJS red-pink #E0234E monitor light and rim light, simplified background, empty dark space on the left for bold typography, 16:9, 8k, photorealistic, like a high-end developer documentary, not a screenshot, not a tutorial, not cartoon, no text, no logos, no watermark.`
2. `A cinematic photograph matching the established TaskFlow NestJS thumbnail style, a Vietnamese developer on the right watching a red PostgreSQL unique-constraint warning transform into a clean 409 response on a dark code monitor, deep black and navy background, dramatic NestJS red-pink #E0234E lighting, one clear focal subject, empty dark space on the left for bold typography, 16:9, 8k, photorealistic, like a high-end tech commercial, not a screenshot, not a tutorial, not cartoon, no text, no watermark.`
3. `A cinematic photograph matching the established TaskFlow NestJS thumbnail style, a Vietnamese developer on the right with a dangerous stack trace locked behind a dark glass panel and a clean API error card visible on the monitor, deep shadows, black and navy palette with NestJS red-pink #E0234E highlights, simplified desk, empty dark space on the left for bold typography, 16:9, 8k, photorealistic, like a developer documentary, not a screenshot, not a tutorial, not cartoon, no text, no logos, no watermark.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Một email trùng làm NestJS crash 500 — sửa đúng lỗi 409 | TaskFlow #4
2. NestJS trả 500 chỉ vì trùng email — tôi sửa thành 409 thế nào?
3. Đừng biến mọi lỗi NestJS thành 400 | Error Handling #4
4. API của bạn đang làm lộ stack trace? | NestJS + Prisma 8
5. 400, 404, 409 hay 500? Cách API nói đúng lỗi | TaskFlow #4

**Khuyên dùng:** Đăng Title 1. Nếu impressions có nhưng CTR yếu sau khi đủ dữ liệu, thử Title 2. Title 5 là phương án thiên về search.

### 4b. SEO Description

```text
Mình gửi lại đúng email vừa tạo. NestJS trả 500 như thể cả server vừa sập.

PostgreSQL chỉ đang báo một email trùng. Tập này biến lỗi kỹ thuật đó thành response 409 đúng nghĩa, không làm lộ stack trace cho client.

✅ Phân biệt 400, 404, 409 và 500
✅ Đặt business exception trong service
✅ Chuẩn hóa response bằng ExceptionFilter
✅ Giữ lỗi Prisma gần database layer
✅ Không gửi stack trace cho client
✅ Hiểu vì sao kiểm tra trước không thay unique constraint
✅ Chạy error matrix bằng request thật

🔗 NestJS Exception Filters: https://docs.nestjs.com/exception-filters
🔗 Prisma 8 Error Reference: https://docs.prisma.io/docs/orm/v8/reference/error-reference

🤖 AI Prompt (Cursor/Claude Code):
"Audit the current Users request flow for every realistic failure point.
Before editing:
1. List failures and classify each as 400, 404, 409 or 500.
2. Decide which layer owns each mapping.
3. Keep generic HttpException formatting in src/common/filters.
4. Keep Prisma-specific error handling near src/database.
5. Never return stack traces or database details to clients.
6. Preserve server-side logs for unexpected errors.
7. Wait for approval before changing files."

⏱ 0:00 Email trùng nhưng API crash 500
⏱ 0:35 Cái bẫy try/catch mọi nơi
⏱ 1:20 Phân biệt 400, 404, 409 và 500
⏱ 2:10 Bắt AI audit mọi failure path
⏱ 3:10 Service exception và database constraint
⏱ 4:35 Hai filter, hai trách nhiệm
⏱ 5:50 Kiểm chứng 400, 404, 409 và 500
⏱ 7:05 Pain mới: API chưa biết ai đang gọi

#NestJS #ErrorHandling #ExceptionFilter #Prisma #RESTAPI #TypeScript #Backend #AICoding #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs error handling, nestjs exception filter, prisma 8 structured error, postgres sqlstate 23505, conflict exception nestjs, not found exception nestjs, http status code api, lỗi 500 nestjs, api error response, nestjs tiếng việt, học nestjs, nestjs tập 4, backend error handling, validationpipe exception, prisma unique constraint, typescript backend, backend fresher, ai coding mentor, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- Dòng chính: `CRASH 500` — `CRASH` WHITE `#FFFFFF`, `500` NEST RED `#E0234E`
- Badge nhỏ: `EMAIL TRÙNG` — WHITE trên nền NEST RED `#E0234E`
- Hình: response 500 lớn trên monitor; developer căng thẳng nhìn thẳng vào lỗi.

### Option 2
- Dòng 1: `500 CHỈ VÌ` — WHITE `#FFFFFF`
- Dòng 2: `TRÙNG EMAIL` — NEST RED `#E0234E`
- Hình: cảnh báo unique constraint biến thành response 409 sạch.

### Option 3
- Dòng 1: `ĐỪNG LỘ` — WHITE `#FFFFFF`
- Dòng 2: `STACK TRACE` — NEST RED `#E0234E`
- Hình: stack trace bị khóa sau lớp kính; client chỉ thấy response sạch.

**Typography chung:** Canvas 1280×720. Dùng Anton hoặc Helvetica Neue Condensed Black cho headline; JetBrains Mono chỉ dùng cho badge/code nhỏ. Mỗi dòng cao khoảng 110–140px, line spacing 0.85, block chữ chiếm khoảng một phần ba bên trái. Dùng stroke đen 8px và shadow gọn; không dùng neon glow dày. Giữ developer ở 35–40% bên phải và không để chữ đè lên mặt. Typeset trong Canva, kiểm tra cả bản 320×180 và giữ một bản nền không chữ.
