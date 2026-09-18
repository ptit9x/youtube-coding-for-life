# BONUS 17.5 — Cùng một Service, hai API: REST và GraphQL

- **Series:** Học NestJS bằng AI — bonus sau tập 17
- **Target runtime:** khoảng 6 phút (500 từ thoại)
- **Outcome:** GraphQL code-first gọi lại use case hiện có; REST và GraphQL không nhân đôi business logic.

---

## PART 1 — SCRIPT

Dashboard cần user, task và permission trong cùng một màn hình.

REST client gọi ba endpoint, rồi tự ghép ba response.

Mình thêm GraphQL và AI lập tức copy logic từ controller sang resolver.

Hai API chạy được. Business rule bắt đầu có hai phiên bản.

Lần sau đổi ownership, một transport sẽ bị quên.

Bước ngoặt là hiểu REST và GraphQL chỉ là hai cửa vào cùng một use case.

Controller và resolver đều là transport boundary.

Chúng dịch input, gọi service, rồi định dạng output. Chúng không sở hữu policy.

GraphQL cho client chọn đúng field cần lấy trong một request.

Nó không tự làm query nhanh hơn, và cũng không thay thế thiết kế service tốt.

Mình chọn code-first vì project đã dùng TypeScript decorator.

GraphQL object type mô tả schema. Resolver nối query với application service.

Mình đưa AI controller, service và permission guard hiện tại.

AI phải chỉ ra code nào thuộc transport, code nào thuộc nghiệp vụ.

Sau khi review, mình approve một resolver rất mỏng.

REST `GET /tasks/:id` và GraphQL query `task(id)` cùng gọi `TasksService.getVisibleTask`.

Service nhận actor cùng task ID, rồi kiểm tra permission và ownership đúng một lần.

Resolver không query Prisma trực tiếp.

Nó cũng không copy exception mapping hay tự quyết định user được xem gì.

Authentication cần một thay đổi nhỏ.

HTTP guard đọc request trực tiếp từ execution context.

GraphQL có context riêng, nên adapter dùng `GqlExecutionContext` để lấy cùng request.

Sau bước đó, token parser và permission service được tái sử dụng.

Mình không giả vờ mọi thứ đều dùng chung hoàn toàn.

REST DTO và GraphQL object type phục vụ hai contract khác nhau.

Phần transport có thể khác. Business rule bên dưới phải là một.

Mình chạy hai ca kiểm chứng với cùng user.

REST trả task được phép xem. GraphQL trả đúng task đó cùng label đã chọn.

User khác nhận bốn-không-ba ở REST và GraphQL error tương ứng.

Sau đó mình mutation ownership rule trong service.

Cả hai transport cùng đỏ một test, rồi cùng xanh sau khi sửa.

Đây là bằng chứng reuse thật, không phải hai đoạn code trông giống nhau.

GraphQL vẫn có một cái bẫy khác.

Resolve field trong vòng lặp có thể tạo N cộng một query.

Mình đo query count, rồi dùng batch loader hoặc application query chuyên cho dashboard.

Không bật field-level guard hàng nghìn lần nếu top-level policy đã đủ.

GraphQL mạnh khi client cần shape linh hoạt. REST đơn giản khi resource và cache đã rõ.

Không có người thắng tuyệt đối. Có boundary phù hợp với từng consumer.

Thêm một API không nên tạo thêm một bộ sự thật.

Nếu service giữ nghiệp vụ, transport mới chỉ là thêm một ngôn ngữ giao tiếp.

Nếu bạn muốn học framework mà không khóa tư duy vào một protocol, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Dashboard tạo ba REST request trong Network tab | 30s |
| 2 | [IDE] | Resolver do AI copy business logic từ controller | 30s |
| 3 | [DIAGRAM] | REST Controller và GraphQL Resolver cùng trỏ vào một Service | 35s |
| 4 | [BROWSER] | Review plan, đánh dấu transport code và business code | 30s |
| 5 | [IDE] | Cấu hình GraphQL code-first và object types | 40s |
| 6 | [IDE] | REST controller và resolver cùng gọi `getVisibleTask` | 40s |
| 7 | [IDE] | Adapter lấy request bằng `GqlExecutionContext` | 35s |
| 8 | [TERM] | Chạy cùng auth/ownership test qua REST và GraphQL | 45s |
| 9 | [BROWSER] | Query một request lấy task, owner, labels và permissions | 35s |
| 10 | [TERM] | Đếm query, tái hiện N+1 rồi batch lại | 35s |
| 11 | [B-ROLL] | Hai cửa REST/GraphQL nhập vào một service | 15s |

**Tổng mục tiêu: 6 phút 10 giây.** One Dark Pro, JetBrains Mono 18–20px; tắt GraphiQL trên production nếu không dùng.

### Code cốt lõi

```ts
@Resolver(() => TaskType)
export class TasksResolver {
  constructor(private readonly tasksService: TasksService) {}

  @Query(() => TaskType)
  @RequirePermissions('tasks.read')
  task(@Args('id') id: string, @CurrentUser() actor: AuthUser) {
    return this.tasksService.getVisibleTask({ id, actor });
  }
}
```

```ts
const gql = GqlExecutionContext.create(context);
const request = context.getType<string>() === 'graphql'
  ? gql.getContext<{ req: Request }>().req
  : context.switchToHttp().getRequest<Request>();
```

### Prompt cho AI

```text
Plan a code-first GraphQL transport for the existing TaskFlow services.
- Treat resolvers as transport boundaries; do not copy business rules or query Prisma directly.
- Reuse the same TasksService use case used by REST.
- Adapt authentication and permission guards through GqlExecutionContext.
- Keep REST DTOs and GraphQL object types separate where their contracts differ.
- Add parity tests for auth, permission and ownership across both transports.
- Measure query count and prevent N+1 with batching or one application query.
- Keep GraphiQL disabled in production unless explicitly protected.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right facing two glowing doors labeled by visual REST brackets and a GraphQL node symbol, both leading into one shared service core, dark navy and black scene with NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no written text.`
2. `A cinematic photograph of a dark monitor showing three REST request streams merging into one precise GraphQL query, developer face reflected on the right, NestJS red-pink #E0234E rim light, empty left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of one glowing business service powering two different API interfaces on a dark developer desk, subject on the right, black and navy background with NestJS red-pink #E0234E highlights, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Cùng một Service, hai API: REST và GraphQL | Lập trình là cuộc sống
2. Đừng copy Business Logic sang Resolver | Lập trình là cuộc sống
3. GraphQL không thay thế Service tốt | Lập trình là cuộc sống
4. Thêm GraphQL mà không phá kiến trúc NestJS | Lập trình là cuộc sống
5. REST hay GraphQL? Boundary mới là câu trả lời | Lập trình là cuộc sống

**Khuyên dùng:** Title 1.

### 4b. SEO Description

```text
Thêm GraphQL không có nghĩa là thêm một bộ business logic. Bonus 17.5 dùng cùng TasksService cho REST controller và GraphQL resolver.

✅ Hiểu resolver là transport boundary
✅ Dùng GraphQL code-first trong NestJS
✅ Reuse service, auth và permission policy
✅ Adapt guard bằng GqlExecutionContext
✅ Test parity giữa REST và GraphQL
✅ Nhìn thấy và tránh N+1 query

🔗 NestJS GraphQL Quick Start: https://docs.nestjs.com/graphql/quick-start
🔗 GraphQL Guards và Context: https://docs.nestjs.com/graphql/other-features

⏱ 0:00 Ba REST request
⏱ 0:40 Copy logic sang resolver
⏱ 1:20 Hai transport, một use case
⏱ 2:15 GraphQL code-first
⏱ 3:05 Guard và execution context
⏱ 4:10 Test parity
⏱ 5:10 N+1 và quyết định chọn API

#NestJS #GraphQL #RESTAPI #TypeScript #Backend #SoftwareArchitecture #RBAC #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs graphql, rest vs graphql nestjs, graphql resolver service nestjs, gql execution context, graphql auth guard nestjs, graphql permission guard, nestjs code first graphql, avoid n+1 graphql, reuse business logic api, transport boundary nestjs, taskflow nestjs, học nestjs bằng ai, graphql tiếng việt, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `2 API` — WHITE `#FFFFFF`
- `1 SERVICE` — NEST RED `#E0234E`
- Badge nhỏ: `BONUS 17.5`

### Option 2
- `REST HAY` — WHITE `#FFFFFF`
- `GRAPHQL?` — NEST RED `#E0234E`
- Badge nhỏ: `CÙNG LOGIC`

### Option 3
- `ĐỪNG COPY` — WHITE `#FFFFFF`
- `BUSINESS LOGIC` — NEST RED `#E0234E`
- Badge nhỏ: `RESOLVER`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
