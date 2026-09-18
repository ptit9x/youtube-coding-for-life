# NestJS #17 — Swagger: API tự viết hồ sơ

- **Series:** Học NestJS bằng AI — tập 17/45, mở Season 2
- **Target runtime:** khoảng 6 phút (535 từ thoại)
- **Outcome:** `/docs` và OpenAPI JSON mô tả đúng request, response, lỗi, bearer auth và permission.
- **Pain tập kế:** Dashboard phải gọi nhiều REST endpoint để ghép một màn hình.

---

## PART 1 — SCRIPT

TaskFlow đã chạy trên production, nhưng người dùng không biết phải gọi nó thế nào.

Mỗi câu hỏi đều giống nhau. Endpoint ở đâu, body gồm gì, và token đặt chỗ nào.

API đã online. Hợp đồng của nó vẫn nằm rải rác trong code và trong đầu mình.

Mình từng giải quyết bằng một file README rất dài.

Hai tuần sau, code đổi nhưng ví dụ trong README không đổi.

Tài liệu sai nguy hiểm hơn không có tài liệu. Nó khiến người khác tự tin làm sai.

Bước ngoặt là để tài liệu đứng gần code nhất có thể.

Swagger không đọc được ý định. Nó biến metadata của NestJS thành tài liệu OpenAPI có thể kiểm tra.

OpenAPI là một hợp đồng máy đọc được về endpoint, dữ liệu và cách xác thực.

Mình đưa AI mục tiêu cùng controller, DTO và error envelope hiện tại.

AI phải lập plan trước. Mình kiểm tra phạm vi, rồi mới approve phần annotation.

Trong `main.ts`, `DocumentBuilder` khai báo tên API, phiên bản và bearer auth.

`SwaggerModule` sinh tài liệu tại `/docs` và bản JSON tại `/docs-json`.

Bearer auth chỉ mô tả cách gửi JWT. Nó không thay thế `AuthGuard` đang bảo vệ route.

Trong `TasksController`, `ApiTags` gom endpoint theo nghiệp vụ.

`ApiOperation` nói endpoint làm gì. `ApiResponse` nói từng kết quả có hình dạng nào.

DTO dùng `ApiProperty` để mô tả field, ví dụ và giá trị hợp lệ.

Đây là nơi AI làm rất nhanh, và cũng dễ nói dối rất nhanh.

AI ghi `dueDate` là bắt buộc. Code thật lại cho phép bỏ trống.

AI ghi update trả hai-trăm. Controller thật trả hai-không-bốn.

Tệ hơn, endpoint xóa task cần `tasks.delete`, nhưng tài liệu không nhắc tới permission.

Mình không sửa từng lỗi bằng trí nhớ.

Mình đối chiếu annotation với DTO, decorator quyền và test e2e đang chạy.

Permission không phải chuẩn có sẵn của OpenAPI.

Mình tạo decorator ghép `RequirePermissions` với extension `x-permissions`.

Một khai báo vừa chạy trong app, vừa xuất hiện trong tài liệu.

Lúc này, policy và docs không còn hai nguồn sự thật riêng biệt.

Mình thêm schema chung cho lỗi bốn-trăm, bốn-không-một, bốn-không-ba và bốn-không-chín.

Người dùng API thấy cả status, message, code và correlation ID.

Sau đó mình mở Swagger UI, bấm Authorize và dán access token.

POST `/tasks` với payload hợp lệ trả hai-không-một.

Payload thiếu title trả bốn-trăm đúng như schema.

Token thiếu permission trả bốn-không-ba, không phải lỗi bí ẩn trong console.

Cuối cùng, mình tải `/docs-json` và chạy kiểm tra trong CI.

Nếu endpoint đổi ngoài hợp đồng, pull request phải báo đỏ.

Swagger không làm API tốt hơn. Nó khiến lời hứa của API nhìn thấy được.

Và lời hứa đã nhìn thấy thì khó bị sửa lén hơn.

Nhưng một tài liệu đẹp không làm REST bớt nhiều request.

Tập sau, mình sẽ dùng cùng service cho REST và GraphQL, không nhân đôi business logic.

Nếu bạn muốn theo TaskFlow tới production thật, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Mở public API trả JSON rồi cắt sang README đã lỗi thời | 25s |
| 2 | [DIAGRAM] | Vẽ `Controller + DTO + metadata → OpenAPI JSON → Swagger UI/client` | 30s |
| 3 | [BROWSER] | Prompt AI lập plan annotate controller; dừng ở bước review | 30s |
| 4 | [IDE] | Cài `@nestjs/swagger`; cấu hình `DocumentBuilder` và `/docs-json` trong `main.ts` | 40s |
| 5 | [IDE] | Annotate `CreateTaskDto` và `TasksController` | 40s |
| 6 | [IDE] | Zoom ba annotation sai của AI rồi đối chiếu code/test | 35s |
| 7 | [IDE] | Tạo `ApiRequirePermissions()` bằng `applyDecorators` và `ApiExtension` | 40s |
| 8 | [IDE] | Mở `ApiErrorResponseDto`; annotate 400/401/403/409 | 30s |
| 9 | [BROWSER] | Authorize trong Swagger; thử POST thành công, validation fail và thiếu quyền | 45s |
| 10 | [TERM] | Tải `/docs-json`; chạy test kiểm tra operation và `x-permissions` | 30s |
| 11 | [B-ROLL] | Giữ khung Swagger cạnh màn hình code; chuyển sang dashboard nhiều request | 20s |

**Tổng mục tiêu: 6 phút 05 giây.** Dùng One Dark Pro, JetBrains Mono 18–20px, ẩn minimap và che token trước khi quay.

### Code cốt lõi

```ts
const config = new DocumentBuilder()
  .setTitle('TaskFlow API')
  .setVersion('2.0')
  .addBearerAuth()
  .build();

const documentFactory = () => SwaggerModule.createDocument(app, config);
SwaggerModule.setup('docs', app, documentFactory, {
  jsonDocumentUrl: 'docs-json',
});
```

```ts
export function ApiRequirePermissions(...permissions: string[]) {
  return applyDecorators(
    RequirePermissions(...permissions),
    ApiBearerAuth(),
    ApiExtension('x-permissions', permissions),
    ApiForbiddenResponse({ type: ApiErrorResponseDto }),
  );
}
```

### Prompt cho AI

```text
Audit the current NestJS REST API and propose an OpenAPI documentation plan.
- Read every controller, DTO, auth guard, permission decorator and error envelope first.
- Cover operation summaries, request schemas, success responses and 400/401/403/404/409 errors.
- Add bearer auth without changing runtime authentication.
- Expose required permissions as an x-permissions OpenAPI extension.
- Reuse one composed decorator so runtime policy and docs share one declaration.
- Add a test for the generated OpenAPI document.
- List any mismatch between code and proposed documentation.
- Wait for approval before editing files.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right studying a dark monitor that shows a clean API documentation interface and one glowing contract page, deep black and dark navy background, NestJS red-pink #E0234E rim light, empty dark space on the left for headline text, high contrast, 16:9, photorealistic, high-end developer documentary, no text.`
2. `A cinematic photograph of a dark code monitor on the right transforming controller code into a structured API document, one developer face lit by NestJS red-pink #E0234E monitor glow, deep shadows, empty left side for headline text, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer holding an old faded README while a precise glowing API contract appears on the monitor behind him, subject on the right, black and dark navy scene with NestJS red-pink #E0234E accents, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Swagger cho NestJS: API tự viết hồ sơ — EP17 | Lập trình là cuộc sống
2. Tài liệu API sai còn nguy hiểm hơn không có — EP17 | Lập trình là cuộc sống
3. Biến Controller NestJS thành OpenAPI chuẩn — EP17 | Lập trình là cuộc sống
4. Document Auth và RBAC trong Swagger — EP17 | Lập trình là cuộc sống
5. Đừng để README nói khác code — EP17 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1. A/B test Title 2 để tăng curiosity.

### 4b. SEO Description

```text
API đã lên production, nhưng endpoint, payload và permission vẫn nằm rải rác trong code. Tập 17 biến metadata NestJS thành một hợp đồng OpenAPI có thể kiểm tra.

✅ Cấu hình Swagger UI và OpenAPI JSON
✅ Document DTO, response và error envelope
✅ Thêm bearer auth mà không thay AuthGuard
✅ Hiển thị permission bằng x-permissions
✅ Bắt lỗi annotation do AI suy đoán
✅ Kiểm tra OpenAPI contract trong CI

🔗 NestJS OpenAPI: https://docs.nestjs.com/openapi/introduction
🔗 OpenAPI security: https://docs.nestjs.com/openapi/security

⏱ 0:00 API online nhưng không ai biết gọi
⏱ 0:40 Tại sao README bị lệch
⏱ 1:10 OpenAPI là gì
⏱ 1:40 Plan và review annotation của AI
⏱ 2:25 Swagger trong main.ts
⏱ 3:20 Auth, permission và error schema
⏱ 4:45 Kiểm chứng trên Swagger UI
⏱ 5:35 Contract trong CI

#NestJS #Swagger #OpenAPI #RESTAPI #TypeScript #Backend #RBAC #APIDocumentation #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs swagger, nestjs openapi, swagger nestjs tiếng việt, document api nestjs, api bearer auth swagger, nestjs api response, api permissions openapi, x-permissions openapi, taskflow nestjs, nestjs production, rest api documentation, dto api property, openapi contract test, học nestjs bằng ai, nestjs tập 17, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `API TỰ VIẾT` — WHITE `#FFFFFF`
- `HỒ SƠ` — NEST RED `#E0234E`
- Badge nhỏ: `EP 17`

### Option 2
- `README` — WHITE `#FFFFFF`
- `ĐÃ NÓI DỐI` — NEST RED `#E0234E`
- Badge nhỏ: `SWAGGER`

### Option 3
- `CODE ĐỔI` — WHITE `#FFFFFF`
- `DOCS ĐỔI` — NEST RED `#E0234E`
- Badge nhỏ: `OPENAPI`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ một bản ảnh sạch không chữ và kiểm tra preview 320×180.
