# NestJS #15 — Request Lifecycle: Middleware, Guard và Pipe chạy thế nào?

- **Series:** Học NestJS bằng AI — tập 15/45
- **Target runtime:** ~12 phút
- **Outcome:** Đọc đúng thứ tự middleware, guard, interceptor, pipe, handler và filter.
- **Pain mở EP16:** Ứng dụng rõ luồng nhưng vẫn chỉ chạy trên máy lập trình viên.

---

## PART 1 — SCRIPT

Mình đặt breakpoint trong TasksController. Request trả 400, nhưng breakpoint không bao giờ dừng.

Controller không hề lỗi. Request đã bị chặn trước khi chạm tới nó.

TaskFlow hiện có middleware, hai guard, interceptor, pipe và exception filter.

Không hiểu thứ tự, debug chỉ còn là đoán mò.

Ta sẽ gắn cùng một request ID và theo dấu nó từ cửa vào tới response.

Luồng vào cơ bản của NestJS như sau.

Request đi qua middleware, guard, interceptor phía trước, pipe, controller và service.

Response quay ngược qua interceptor. Nếu có exception, filter phù hợp sẽ tạo response lỗi.

Đây là bản đồ, không phải toàn bộ chi tiết scope.

Global, controller và route binding còn quyết định thứ tự trong từng nhóm.

Middleware chạy trước guard. Nó phù hợp để tạo request ID.

Middleware nhận `x-request-id` hoặc tạo UUID mới, gắn nó vào request và response.

Request ID không chứa business rule.

Nó giúp nối log từ nhiều lớp thành một câu chuyện.

Middleware không biết route này cần permission nào.

Authorization vẫn thuộc guard.

AuthGuard xác thực token và gắn `request.user`.

PermissionGuard chạy sau, đọc user cùng metadata của route.

Nếu AuthGuard ném 401, pipe và controller không chạy.

Nếu PermissionGuard ném 403, kết quả cũng tương tự.

Mình thêm log gồm request ID, layer và decision.

Log của `req-42` cho thấy AuthGuard cho qua, còn PermissionGuard từ chối.

Giờ ta biết request dừng chính xác ở đâu.

Interceptor chạy phần trước handler rồi nhận luồng response quay lại.

Nó phù hợp cho timing, logging và response mapping nhất quán.

Pipe xử lý argument trước khi controller nhận chúng.

ValidationPipe có thể biến string param thành number và loại payload lạ.

Vì vậy, breakpoint controller không chạy khi DTO sai.

AI ban đầu đặt validation trong interceptor. Mình yêu cầu trả nó về pipe.

Mỗi extension point nên giữ đúng trách nhiệm.

TaskService ném `ForbiddenException` vì sai owner.

Luồng bình thường dừng lại. Exception filter chuẩn hóa error response.

Response giữ status 403, message an toàn và `requestId` là `req-42`.

Filter không phải bước luôn chạy trên response thành công.

Nó được kích hoạt khi có exception phù hợp với phạm vi bắt lỗi.

Request ID giúp client và server cùng nói về một sự cố.

Mình gửi ba request.

Request thiếu token dừng tại AuthGuard.

Request có token nhưng payload sai vượt guard rồi dừng tại pipe.

Request hợp lệ đi tới service và quay qua interceptor.

Thứ tự log khớp với sequence diagram.

Interceptors phía response hoạt động theo thứ tự ngược chiều đi vào.

Từ giờ, ta không cần đặt log ngẫu nhiên khắp business code.

Nhưng toàn bộ hệ thống vẫn phụ thuộc máy mình có đúng Node và PostgreSQL.

Tập cuối Season 1, ta đóng gói TaskFlow bằng Docker và đưa lên internet.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Breakpoint controller không được chạm | 35s |
| 2 | [DIAGRAM] | Vẽ request lifecycle tổng quát | 75s |
| 3 | [IDE] | Middleware tạo request ID | 70s |
| 4 | [IDE] | AuthGuard rồi PermissionGuard | 70s |
| 5 | [TERMINAL] | Log request dừng tại permission | 50s |
| 6 | [DIAGRAM] | Interceptor bao quanh handler, pipe xử lý argument | 75s |
| 7 | [AI] | Sửa đề xuất validation trong interceptor | 50s |
| 8 | [IDE] | Exception filter thêm request ID | 65s |
| 9 | [BROWSER] | Gửi ba request và đối chiếu log | 100s |
| 10 | [DIAGRAM] | Response quay qua interceptor theo chiều ngược | 45s |
| 11 | [B-ROLL] | Từ localhost tới container | 25s |

**Tổng: 660 giây ≈ 11 phút.** Font tối thiểu 18px; dùng màu riêng cho từng lifecycle layer.

### Code cốt lõi

```ts
@Injectable()
export class RequestIdMiddleware implements NestMiddleware {
  use(req: RequestWithContext, res: Response, next: NextFunction) {
    req.requestId = req.header('x-request-id') ?? randomUUID();
    res.setHeader('x-request-id', req.requestId);
    next();
  }
}
```

```ts
intercept(context: ExecutionContext, next: CallHandler) {
  const startedAt = Date.now();
  return next.handle().pipe(
    finalize(() => this.logger.log({
      requestId: getRequestId(context),
      durationMs: Date.now() - startedAt,
    })),
  );
}
```

### Prompt cho AI

```text
Map the current NestJS request lifecycle using actual project bindings.
Include global, controller and route scopes.
Add a request ID middleware and structured timing interceptor.
Keep authentication and permission decisions inside guards.
Keep DTO transformation and validation inside pipes.
Add requestId to normalized exception responses.
Produce a sequence diagram, then verify it against logs from three requests.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic HTTP request traveling through glowing middleware guard interceptor pipe and controller gates, stopped at one red layer, dark server tunnel, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic developer searching for a lost request inside a dark NestJS pipeline maze, neon green trace line and red breakpoint, cinematic lighting, 16:9, photorealistic, no text.`
3. `A cinematic sequence of API security and validation checkpoints surrounding a controller, dark code environment, cyan and amber glow, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Request Lifecycle NestJS: Middleware, Guard và Pipe chạy thế nào? — EP15 | Lập trình là cuộc sống
2. Thứ tự Middleware, Guard, Interceptor và Pipe — EP15 | Lập trình là cuộc sống
3. Vì sao request chưa chạy vào Controller? — EP15 | Lập trình là cuộc sống
4. Theo dõi request bằng Request ID trong NestJS — EP15 | Lập trình là cuộc sống
5. Debug Request Lifecycle trong NestJS — EP15 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 3 cho tình huống debug.

### 4b. SEO Description

```text
Request trả lỗi trước khi vào controller? Hãy theo dõi đúng thứ tự lifecycle của NestJS.

✅ Middleware tạo request ID
✅ AuthGuard chạy trước PermissionGuard
✅ Interceptor bao quanh handler
✅ Pipe validate và transform argument
✅ Exception filter chuẩn hóa lỗi
✅ Đối chiếu sequence diagram với log thật

🔗 NestJS Request Lifecycle: https://docs.nestjs.com/faq/request-lifecycle

⏱ 0:00 Controller không được gọi
⏱ 1:10 Bản đồ lifecycle
⏱ 2:50 Middleware và request ID
⏱ 4:20 Hai guard
⏱ 6:00 Interceptor và pipe
⏱ 8:15 Exception filter
⏱ 9:45 Ba request, ba điểm dừng

#NestJS #RequestLifecycle #Middleware #Guards #Interceptors #Pipes #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs request lifecycle, middleware guard interceptor pipe order, nestjs interceptor, nestjs middleware, validation pipe nestjs, exception filter nestjs, request id nestjs, debug nestjs request, nestjs tiếng việt, nestjs tập 15, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `REQUEST` — WHITE
- `MẤT Ở ĐÂU?` — NEON GREEN `#00FF41`
### Option 2
- `GUARD → PIPE` — WHITE
- `RỒI TỚI GÌ?` — NEON GREEN `#00FF41`
### Option 3
- `CONTROLLER` — WHITE
- `KHÔNG HỀ CHẠY` — RED `#FF3B30`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
