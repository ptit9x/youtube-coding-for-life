# NestJS #04 — Error Handling: Trả đúng lỗi 400, 404 và 409

- **Series:** Học NestJS bằng AI — tập 4/46
- **Target runtime:** ~11 phút
- **Outcome:** Chuẩn hóa lỗi 400, 404, 409 và che chi tiết nội bộ khỏi client.
- **Pain mở EP05:** API trả lỗi đẹp nhưng bất kỳ ai vẫn gọi được endpoint riêng tư.

---

## PART 1 — SCRIPT

Database nói email đã tồn tại. API lại trả 500 như thể cả server vừa bốc cháy.

Tệ hơn, stack trace có thể làm lộ tên file, query và chi tiết hạ tầng. Một lỗi nghiệp vụ nhỏ thành tín hiệu báo động giả.

Mình từng sửa kiểu nhanh: bọc mọi thứ trong `try/catch`, rồi trả `BadRequestException`. Code hết đỏ, nhưng mọi lỗi đều thành 400.

Không tìm thấy user, email trùng và database mất kết nối không phải cùng một chuyện.

Bước ngoặt là tách ba lớp ngôn ngữ. Database nói lỗi kỹ thuật, service nói nghiệp vụ, HTTP nói status cho client.

Nó giống phòng cấp cứu. Cùng là đau, nhưng bác sĩ phải phân loại trước khi điều trị.

400 nghĩa là request không hợp lệ. 404 nghĩa là resource không tồn tại. 409 nghĩa là request xung đột với trạng thái hiện tại.

500 được giữ cho lỗi ngoài dự kiến. Nếu biến mọi lỗi thành 400, ta đang che bug chứ không xử lý nó.

Mình yêu cầu AI audit toàn bộ Users flow. Nó phải liệt kê điểm có thể fail trước khi viết code.

Danh sách gồm UUID sai, user không tồn tại, email trùng, validation fail và PostgreSQL unavailable.

AI ban đầu đề xuất một filter bắt mọi exception rồi luôn trả status 500. Filter đó chỉ đổi hình thức, không đổi ý nghĩa.

Mình sửa plan thành hai trách nhiệm. Service chủ động ném HttpException cho rule đã biết, filter chuẩn hóa response cuối cùng.

Trong `findOne`, repository trả `null` thì service ném `NotFoundException`. Controller không tự đoán kết quả của database.

Trong `create`, service kiểm tra email và ném `ConflictException`. Đây là thông báo sớm, dễ đọc cho phần lớn request.

Nhưng hai request đồng thời vẫn có thể cùng vượt qua bước kiểm tra. Unique index trong PostgreSQL mới là hàng rào cuối.

Vì vậy Prisma adapter hoặc filter database vẫn phải map unique constraint thành 409. Kiểm tra trước không thay thế constraint.

Mình tạo `HttpExceptionFilter` trong `common/filters`. Nó chỉ hiểu Nest HttpException và format response nhất quán.

Response có `statusCode`, `error`, `message`, `path`, `timestamp` và `requestId` nếu request đã có.

Filter không gửi stack trace cho client. Stack vẫn được log ở server với context cần thiết.

Lỗi phụ thuộc Prisma không được nhét vào common. `PrismaExceptionFilter` nằm gần database vì nó biết mã lỗi của Prisma.

Đây là ranh giới đáng giữ. Common có thể mang sang dự án khác; mã `P2002` thì không.

Mình approve. Agent implement, rồi mình mở git diff từng filter.

Đến phần tự gõ, mình thêm case 409 cho unique constraint. Mình không so chuỗi message vì message có thể đổi.

Mình dùng type và code chính thức của Prisma. Mapping hẹp hơn, nhưng ít vỡ âm thầm hơn.

Giờ kiểm chứng bằng bốn request. Email sai nhận 400 từ ValidationPipe.

UUID hợp lệ nhưng không có user nhận 404. Email đã tồn tại nhận 409. Endpoint cố tình throw nhận 500 sạch.

Terminal vẫn giữ stack trace của lỗi bất ngờ. Client chỉ nhận câu trả lời cần thiết để xử lý.

Một API chuyên nghiệp không phải API không bao giờ lỗi. Nó là API nói đúng lỗi, đúng người và đúng mức chi tiết.

Nhưng lúc này ai biết URL cũng có thể đọc user. Cánh cửa đã lịch sự, chỉ là chưa có khóa.

Tập sau, JWT sẽ trả lời một câu hỏi rất cơ bản: request này đến từ ai.

Theo dõi series nếu bạn muốn thấy 401 xuất hiện đúng chỗ, không phải rải khắp controller. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER]+[TERM] | POST email trùng → 500; zoom log Prisma | 35s |
| 2 | [IDE] | Một `try/catch` biến mọi lỗi thành BadRequest | 35s |
| 3 | [DIAGRAM] | Database error → business exception → HTTP response | 50s |
| 4 | [DIAGRAM] | Bảng 400 / 404 / 409 / 500 với ví dụ Users | 50s |
| 5 | [IDE] | Gõ prompt audit failure points; AI trả danh sách | 60s |
| 6 | [IDE] | Review `findOne` và `create` trong UsersService | 60s |
| 7 | [IDE] | Tạo HttpExceptionFilter trong common | 65s |
| 8 | [IDE] | Tạo PrismaExceptionFilter gần database | 55s |
| 9 | [IDE] | Host tự gõ mapping unique constraint → 409 | 50s |
| 10 | [IDE] | Xem diff, kiểm tra không trả stack cho client | 40s |
| 11 | [BROWSER] | Chạy matrix: 400, 404, 409, 500 | 80s |
| 12 | [TERM] | So sánh client response với server log | 40s |
| 13 | [B-ROLL] | Khóa cửa trong ánh monitor, teaser JWT | 20s |

**Tổng: 645 giây ≈ 10:45.** Giữ IDE tối, font 18px và che connection string trong log.

### Response contract mục tiêu

```json
{
  "statusCode": 409,
  "error": "Conflict",
  "message": "Email đã được sử dụng",
  "path": "/users",
  "timestamp": "2026-09-12T10:00:00.000Z"
}
```

### Service rule cốt lõi

```typescript
async findOne(id: string): Promise<User> {
  const user = await this.usersRepository.findById(id);
  if (!user) {
    throw new NotFoundException('Không tìm thấy user');
  }
  return user;
}

async create(dto: CreateUserDto): Promise<User> {
  const existing = await this.usersRepository.findByEmail(dto.email);
  if (existing) {
    throw new ConflictException('Email đã được sử dụng');
  }
  return this.usersRepository.create(dto);
}
```

### Prompt cho Opus

```text
Audit the current Users request flow for every realistic failure point.

Before editing:
1. List failures and classify each as 400, 404, 409 or 500.
2. Decide which layer owns each mapping.
3. Keep generic HttpException formatting in src/common/filters.
4. Keep Prisma-specific error handling near src/database.
5. Never return stack traces or database details to clients.
6. Preserve server-side logs for unexpected errors.
7. Wait for approval before changing files.
```

### Matrix kiểm chứng

| Case | Expected |
|---|---:|
| Email sai định dạng | 400 |
| User ID không tồn tại | 404 |
| Email trùng | 409 |
| Database/nghiệp vụ lỗi bất ngờ | 500 |

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese developer facing a huge glowing red 500 error that fractures into clean 400, 404 and 409 cards, dark IDE background, neon green and cyan code, dramatic rim light, subject on the right with empty left space, 16:9, photorealistic, no text, no logos, no watermark.`
2. `A cinematic close-up of a database error entering a glowing filter and emerging as a clean JSON response, dark navy coding room, neon syntax reflected on glasses, high contrast, rain bokeh, empty left side for typography, 16:9, photorealistic, no text.`
3. `A cinematic developer desk with a dangerous stack trace locked behind glass while a clean API error card faces the viewer, red and cyan monitor glow, deep shadows, subject on the right, 16:9, photorealistic technology documentary, no text, no watermark.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Error Handling NestJS: Trả đúng lỗi 400, 404 và 409 — EP04 | Lập trình là cuộc sống
2. Xử lý email trùng trong NestJS bằng lỗi 409 — EP04 | Lập trình là cuộc sống
3. Tạo Exception Filter trong NestJS — EP04 | Lập trình là cuộc sống
4. Xử lý lỗi Prisma mà không lộ stack trace — EP04 | Lập trình là cuộc sống
5. Khi nào dùng lỗi 400, 404, 409 và 500? — EP04 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho tình huống cụ thể và Title 3 cho search.

### 4b. SEO Description

```text
Email trùng chỉ là xung đột dữ liệu, nhưng API lại trả 500 như server vừa sập. Tập này biến lỗi kỹ thuật thành response đúng nghĩa.

✅ Phân biệt 400, 404, 409 và 500
✅ Đặt business exception trong service
✅ Chuẩn hóa response bằng ExceptionFilter
✅ Giữ lỗi Prisma gần database layer
✅ Không gửi stack trace cho client
✅ Hiểu vì sao kiểm tra trước không thay unique constraint
✅ Chạy error matrix bằng request thật

🔗 NestJS Exception Filters: https://docs.nestjs.com/exception-filters
🔗 Prisma Error Reference: https://www.prisma.io/docs/orm/reference/error-reference

⏱ 0:00 Email trùng nhưng nhận 500
⏱ 1:10 Cái bẫy try/catch mọi nơi
⏱ 2:20 Bốn nhóm status cần phân biệt
⏱ 3:45 Audit failure points cùng AI
⏱ 5:10 Service exception và database constraint
⏱ 7:00 Hai filter, hai trách nhiệm
⏱ 8:40 Test 400, 404, 409, 500
⏱ 10:10 API cần một chiếc khóa

#NestJS #ErrorHandling #ExceptionFilter #Prisma #RESTAPI #TypeScript #Backend #AICoding #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs error handling, nestjs exception filter, prisma p2002 nestjs, conflict exception nestjs, not found exception nestjs, http status code api, lỗi 500 nestjs, api error response, nestjs tiếng việt, học nestjs, nestjs tập 4, backend error handling, validationpipe exception, prisma unique constraint, typescript backend, backend fresher, ai coding mentor, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `500 ≠` — WHITE
- `MỌI LỖI` — NEON GREEN `#00FF41`
- Hình: số 500 vỡ thành 400, 404, 409.

### Option 2
- `ĐỪNG TRẢ` — WHITE
- `STACK TRACE` — NEON GREEN `#00FF41`
- Hình: stack trace bị khóa sau lớp kính.

### Option 3
- `P2002` — WHITE
- `PHẢI LÀ 409` — NEON GREEN `#00FF41`
- Hình: mã Prisma đi qua filter thành response sạch.

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái chiếm một phần ba khung, stroke đen 8px, glow 10px. Typeset trong Canva và giữ bản nền không chữ.
