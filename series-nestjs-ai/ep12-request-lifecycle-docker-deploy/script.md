# NestJS #12 — Request Lifecycle và Docker Deploy

- **Series:** Học NestJS bằng AI — tập 12/29
- **Recording status:** READY
- **Target runtime:** 9–10 phút (~720 từ thoại + khoảng nghỉ terminal)
- **Outcome:** Đọc đúng request lifecycle, đóng gói API/PostgreSQL và deploy với migration gate cùng health check.
- **Pain mở EP13:** API đã public nhưng consumer chưa có contract để biết cách gọi.

---

## PART 1 — SCRIPT

Mình đặt breakpoint trong TasksController. Request trả 400, nhưng breakpoint không bao giờ dừng.

Controller không hề lỗi. Request đã bị chặn trước khi chạm tới nó.

User Management hiện có middleware, hai guard, interceptor, pipe và exception filter.

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

Dockerfile biến môi trường đó thành công thức lặp lại được. Image là gói build từ công thức. Container là process đang chạy.

Database không nằm chung container API. Compose chạy hai service và nối chúng qua network.

Mình yêu cầu AI giải thích từng layer trước khi viết Dockerfile.

Target `build` cài dependency và compile. Target `migrate` giữ Prisma CLI cùng migration history.

Target `runtime` chỉ nhận production dependency, `dist` và contract artifact cần lúc chạy.

Prisma 8 không sinh client package. `contract.json` phải nằm đúng chỗ `db.js` import sau compile.

`.dockerignore` loại `.env`, Git metadata và `node_modules` local.

Trong container API, hostname database là `db`, không phải `localhost`.

AI dùng `localhost`. Container khởi động rồi báo connection refused. Đây là lỗi mình giữ lại để giải thích network của Compose.

Release gate chạy migration check, xem plan, apply rồi `db verify`.

Migration lỗi thì deploy dừng. Không chạy code mới trên schema cũ.

Secret nằm trong dashboard của nền tảng, không truyền bằng Docker build argument.

Nest lắng nghe `0.0.0.0` trên port từ environment. `/health` cho nền tảng biết app đã sẵn sàng.

Build xanh. Migration xanh. Public URL trả health check.

Mình đăng ký user, login và tạo task. Ownership vẫn đúng ngoài localhost.

User Management đã public, nhưng consumer chưa biết endpoint nhận gì.

Tập sau, Swagger và GraphQL sẽ buộc API nói rõ contract mà không nhân đôi business rule.

Deploy không làm code trưởng thành hơn. Nó chỉ khiến mọi giả định môi trường lộ ra. Link Git của nhánh này nằm trong description. Bạn có thể comment phần còn khó hiểu.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Breakpoint controller không chạm; mở request lỗi | 30s |
| 2 | [DIAGRAM] | Middleware → guards → interceptor → pipe → handler → filter | 45s |
| 3 | [IDE] | Submit yêu cầu lifecycle; AI vẽ plan trong lúc voice-over | 40s |
| 4 | [IDE] | Middleware request ID, hai guard và pipe | 50s |
| 5 | [IDE] | Interceptor bao handler; filter thêm request ID | 45s |
| 6 | [BROWSER]+[TERM] | Ba request dừng ở ba layer; đối chiếu log | 50s |
| 7 | [DIAGRAM] | Dockerfile, image, container và Compose network | 40s |
| 8 | [IDE] | Review ba target build/migrate/runtime | 50s |
| 9 | [IDE] | Contract artifact, `.dockerignore`, secret boundary | 45s |
| 10 | [TERM] | Giữ lỗi `localhost`; sửa hostname thành `db` | 40s |
| 11 | [TERM] | Migration gate: check, show, apply, verify | 45s |
| 12 | [BROWSER] | Dashboard deploy, health xanh, public URL | 45s |
| 13 | [BROWSER] | Register/login/create task trên production | 40s |
| 14 | [B-ROLL] | Public API chưa có contract; teaser Swagger | 20s |

**Tổng: 585 giây = 9:45.** One Dark Pro, JetBrains Mono tối thiểu 18px; che secret và URL quản trị.

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

1. Request chưa tới Controller, Deploy đã lỗi — EP12 | Lập trình là cuộc sống
2. Từ Request Lifecycle tới Docker Production — EP12 | Lập trình là cuộc sống
3. Vì sao `localhost` làm Container crash? — EP12 | Lập trình là cuộc sống
4. Middleware, Guard, Pipe và Docker chạy thế nào? — EP12 | Lập trình là cuộc sống
5. Một Request đi qua NestJS rồi ra Internet — EP12 | Lập trình là cuộc sống
6. Dockerfile AI viết thiếu Migration Gate — EP12 | Lập trình là cuộc sống
7. Deploy xanh nhưng Schema vẫn có thể sai — EP12 | Lập trình là cuộc sống
8. Debug Request Lifecycle bằng Log thật — EP12 | Lập trình là cuộc sống
9. Ba Docker Target cho một NestJS API — EP12 | Lập trình là cuộc sống
10. Code chạy máy tôi chưa phải Production — EP12 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1; A/B với Title 3 cho hook Docker.

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
nestjs request lifecycle, middleware guard interceptor pipe order, nestjs interceptor, nestjs middleware, validation pipe nestjs, exception filter nestjs, request id nestjs, debug nestjs request, nestjs tiếng việt, nestjs tập 12, lập trình là cuộc sống
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
