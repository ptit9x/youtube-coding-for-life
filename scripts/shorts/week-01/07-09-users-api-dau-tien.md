# Kịch bản Shorts tuần 1 — EP01 Users API đầu tiên

- **Series:** Học NestJS bằng AI
- **Gồm:** Short 07, 08 và 09
- **Khung hình:** 9:16, 1080×1920, 30fps
- **Thời lượng mục tiêu:** 42–52 giây/Short
- **Project quay:** `nestjs-base-with-ai` sau EP01, Users API dùng mảng in-memory
- **Visual:** One Dark Pro, JetBrains Mono 24–28px, NestJS red `#E0234E`
- **Thông điệp:** AI viết, mình hiểu; AI đề xuất, mình kiểm chứng.

## Lịch đăng đề xuất

| Thời điểm | Short | Vai trò |
|---|---|---|
| T+1 sau EP01 | 07 — Module, Controller, Service | Giải thích mental model từ video dài |
| T+3 sau EP01 | 08 — Nest CLI tiết kiệm gì? | Demo công cụ và thói quen audit code sinh ra |
| T−2 trước EP02 | 09 — API nhận mọi rác | Tạo pain để kéo sang ValidationPipe |

Không dùng intro hoặc logo animation. Frame đầu phải là code, command hoặc response thật.

---

# SHORT 07 — Module, Controller, Service: đừng học thuộc

## 1. Mục tiêu

- **Format:** Một request đi đâu?
- **Thời lượng:** 45–48 giây
- **Insight duy nhất:** Module nối dependency khi bootstrap; request được controller nhận và giao xuống service.
- **Related video:** EP01 — Users API đầu tiên

## 2. Lời thoại sẵn để thu

> Đây là một request `POST /users`.
>
> Nếu bạn đang cố học thuộc Module, Controller, Service, dừng lại.
>
> `UsersModule` không xử lý từng request. Khi app khởi động, nó khai báo `UsersController` và `UsersService` để Nest dựng dependency graph.
>
> Khi request tới, router chọn `UsersController`. Controller lấy body rồi giao việc cho `UsersService`. Service tạo user trong mảng và trả kết quả ngược lại.
>
> Module là bảng điện. Controller là quầy tiếp nhận. Service là nơi làm việc.
>
> Nhớ một chiều này: bootstrap nối dây; request vào controller, xuống service, rồi trở về response.
>
> Mình trace toàn bộ luồng bằng code thật trong EP01 của TaskFlow.

## 3. Timeline và cảnh quay

| Thời gian | Hình ảnh | Caption lớn | Thao tác dựng |
|---|---|---|---|
| 0–2s | REST Client gửi `POST /users` | `REQUEST ĐI ĐÂU?` | Freeze ngay lúc bấm Send; sound click mạnh |
| 2–7s | Ba file xuất hiện nhanh | `ĐỪNG HỌC THUỘC` | Xếp dọc Module / Controller / Service |
| 7–16s | Zoom `users.module.ts` | `MODULE NỐI DÂY` | Highlight `controllers` rồi `providers` |
| 16–27s | Chuyển sang controller | `CONTROLLER NHẬN REQUEST` | Vẽ mũi tên body → `create()` |
| 27–37s | Chuyển sang service | `SERVICE XỬ LÝ` | Highlight `this.users.push(user)` |
| 37–43s | Response 201 cạnh sơ đồ | `RỒI TRẢ RESPONSE` | Mũi tên chạy ngược về client |
| 43–48s | End frame EP01 | `XEM LUỒNG ĐẦY ĐỦ: EP01` | Gắn Related video đến EP01 |

### Sơ đồ overlay chính xác

```text
BOOTSTRAP
AppModule → UsersModule → đăng ký UsersController + UsersService

RUNTIME
POST /users → UsersController.create() → UsersService.create() → 201 response
```

Không vẽ request “chạy xuyên qua UsersModule”. Module cung cấp metadata để Nest dựng application graph lúc bootstrap; controller mới là lớp nhận HTTP request.

## 4. Code quay cận cảnh

```typescript
@Module({
  controllers: [UsersController],
  providers: [UsersService],
})
export class UsersModule {}
```

```typescript
@Post()
create(@Body() dto: CreateUserDto) {
  return this.usersService.create(dto);
}
```

```typescript
create(dto: CreateUserDto): User {
  const user = {
    id: this.nextId++,
    name: dto.name,
    email: dto.email,
  };
  this.users.push(user);
  return user;
}
```

## 5. Title, caption và hashtag

**Title khuyên dùng:** Module, Controller, Service trong NestJS hoạt động thế nào?

**Caption đăng:**

```text
Đừng học thuộc ba khái niệm rời rạc. Hãy trace đúng một request: Module nối dependency khi app khởi động, Controller nhận HTTP request, Service xử lý công việc.

Xem luồng đầy đủ trong EP01 của TaskFlow.
```

**Hashtag:** `#NestJS #TypeScript #Backend #NodeJS #LapTrinhLaCuocSong`

## 6. Nguồn và claim

| Claim | Nguồn |
|---|---|
| Module cung cấp metadata để Nest tổ chức application graph, controllers và providers | [NestJS Modules](https://docs.nestjs.com/modules) |
| Controller chịu trách nhiệm xử lý request và trả response | [NestJS Controllers](https://docs.nestjs.com/controllers) |
| Controller nên giao tác vụ phức tạp cho provider/service | [NestJS Providers](https://docs.nestjs.com/providers) |

---

# SHORT 08 — Lệnh Nest CLI tiết kiệm gì cho bạn?

## 1. Mục tiêu

- **Format:** AI viết được, nhưng… / tool audit
- **Thời lượng:** 45–50 giây
- **Insight duy nhất:** Generator tiết kiệm boilerplate; developer vẫn phải quyết định và review code.
- **Related video:** EP01 — Users API đầu tiên

## 2. Lời thoại sẵn để thu

> Một lệnh này tạo gần như toàn bộ khung Users API.
>
> `nest g resource modules/users --no-spec`.
>
> Chọn REST API, CLI sinh module, controller, service, hai DTO, entity và các CRUD entry point. Nhanh thật, nhưng đây mới chỉ là boilerplate.
>
> CLI không biết bạn cần route nào, business rule nằm ở đâu, hay `/count` có thể bị `/:id` nuốt mất.
>
> Vì vậy lệnh tiếp theo của mình là `git diff --stat`. Mở từng file, bỏ code thừa, kiểm tra module registration và chạy build.
>
> Generator tạo điểm xuất phát. Review của bạn mới quyết định code nào được ở lại.
>
> Mình audit toàn bộ phần CLI tạo trong EP01.

## 3. Timeline và cảnh quay

| Thời gian | Hình ảnh | Caption lớn | Thao tác dựng |
|---|---|---|---|
| 0–3s | Terminal có command generator | `1 LỆNH, 6 FILE CHÍNH` | Gõ command nhanh, không chiếu thời gian chờ |
| 3–11s | Chọn `REST API` và CRUD | `CLI TẠO BOILERPLATE` | Speed ramp phần prompt |
| 11–21s | Cây file Users mở rộng | `MODULE · CONTROLLER · SERVICE` | Tick lần lượt sáu file chính |
| 21–31s | Controller placeholder | `NHƯNG CLI KHÔNG BIẾT...` | Highlight các route chưa được review |
| 31–38s | `count` và `:id` đặt cạnh nhau | `ROUTE NÀO THẬT SỰ CẦN?` | Cảnh báo đỏ ở route order |
| 38–45s | `git diff --stat`, rồi diff file | `GENERATE → REVIEW` | Sound terminal + swipe sang diff |
| 45–50s | End frame | `AUDIT ĐẦY ĐỦ: EP01` | Gắn Related video EP01 |

## 4. Command và checklist quay

```bash
nest g resource modules/users --no-spec
# Chọn REST API
# Chọn tạo CRUD entry points
git diff --stat
git diff -- src/modules/users
npm run build
```

Sáu file chính dự kiến khi dùng `--no-spec`:

```text
src/modules/users/
├── dto/create-user.dto.ts
├── dto/update-user.dto.ts
├── entities/user.entity.ts
├── users.controller.ts
├── users.module.ts
└── users.service.ts
```

CLI có thể cập nhật module cha để đăng ký `UsersModule`. Khi quay, dùng `git diff` của đúng phiên bản Nest CLI đang cài làm bằng chứng; không đọc cứng số file nếu output thực tế khác.

Checklist audit trên màn hình:

1. Có file hoặc endpoint nào chưa cần trong EP01 không?
2. `UsersModule` đã được nối vào application graph chưa?
3. Controller có chứa business logic không?
4. Route tĩnh như `/users/count` có đứng trước `/:id` không?
5. Build có pass sau khi chỉnh generator output không?

## 5. Title, caption và hashtag

**Title khuyên dùng:** `nest g resource` tạo được gì trong 5 giây?

**Caption đăng:**

```text
Nest CLI tạo module, controller, service, DTO và entity rất nhanh. Nhưng generator không hiểu business rule của project. Generate xong vẫn phải đọc diff, bỏ code thừa và chạy build.
```

**Hashtag:** `#NestJS #NestCLI #AICoding #Backend #TypeScript`

## 6. Nguồn và claim

| Claim | Nguồn |
|---|---|
| `nest g resource` sinh module, service, controller, entity, DTO và có thể sinh test | [NestJS CRUD generator](https://docs.nestjs.com/recipes/crud-generator) |
| Các generator/schematic có nhiệm vụ sinh cấu trúc boilerplate | [Nest CLI usage](https://docs.nestjs.com/cli/usages) |
| Controller nhận request; logic phức tạp nên được giao cho provider | [NestJS Controllers](https://docs.nestjs.com/controllers), [NestJS Providers](https://docs.nestjs.com/providers) |

---

# SHORT 09 — Users API chạy rồi, nhưng nhận mọi rác

## 1. Mục tiêu

- **Format:** Bug trong 30 giây
- **Thời lượng:** 48–52 giây
- **Insight duy nhất:** TypeScript type không tự kiểm tra payload HTTP ở runtime.
- **Related video:** EP02 — ValidationPipe, hoặc EP01 nếu EP02 chưa public
- **Video prototype:** [Xem bản dựng 45 giây](../../../videos/shorts/week-01/short-09-preview/short-09-preview.mp4)

## 2. Lời thoại sẵn để thu

> DTO này nói `email` phải là string. Trông an toàn, đúng không?
>
> Giờ mình gửi `email` bằng số 123. API vẫn trả 201.
>
> Bỏ hẳn `name`. Vẫn 201.
>
> Gửi một chuỗi chẳng phải email. Vẫn 201 và dữ liệu còn được đẩy vào mảng.
>
> TypeScript không bị lỗi. Type chỉ kiểm tra code khi phát triển, rồi bị xóa khỏi JavaScript chạy thật. Request từ internet vẫn là dữ liệu runtime.
>
> Dấu chấm than sau `email` cũng không phải validation. Nó chỉ là lời khẳng định field sẽ được gán.
>
> Muốn dữ liệu sai dừng trước controller, ta cần rule runtime và `ValidationPipe`.
>
> EP02 bắt đầu từ chính ba response 201 sai này.

## 3. Timeline và cảnh quay

| Thời gian | Hình ảnh | Caption lớn | Thao tác dựng |
|---|---|---|---|
| 0–3s | DTO cạnh response 201 | `EMAIL LÀ SỐ → 201` | Zoom `email!: string` rồi snap sang response |
| 3–10s | Payload `email: 123` | `TYPE KHÔNG CHẶN REQUEST` | Highlight số `123` màu đỏ |
| 10–17s | Payload thiếu `name` | `THIẾU NAME → 201` | Counter `Sai 2/3` |
| 17–24s | Email sai định dạng | `EMAIL RÁC → 201` | GET list để chứng minh đã lưu |
| 24–35s | Build TypeScript → JavaScript | `TYPE BỊ XÓA KHI COMPILE` | DTO type mờ dần khỏi JS output |
| 35–43s | Zoom dấu `!` | `! KHÔNG PHẢI VALIDATION` | Cross đỏ trên chữ “validation” |
| 43–48s | Overlay Pipe trước Controller | `CẦN RUNTIME VALIDATION` | Request đập vào barrier đỏ |
| 48–52s | End frame EP02 | `SỬA TRỌN LUỒNG: EP02` | Gắn Related video phù hợp |

## 4. Code và payload quay thật

DTO chưa có validation ở EP01:

```typescript
export class CreateUserDto {
  name!: string;
  email!: string;
}
```

Payload 1 — sai type:

```json
{ "name": "Richard", "email": 123 }
```

Payload 2 — thiếu field:

```json
{ "email": "richard@example.com" }
```

Payload 3 — đúng type nhưng sai format:

```json
{ "name": "Richard", "email": "khong-phai-email" }
```

Lệnh quay bằng `curl` nếu không dùng REST Client:

```bash
curl -i -X POST http://localhost:3000/users \
  -H 'Content-Type: application/json' \
  -d '{"name":"Richard","email":123}'

curl -i -X POST http://localhost:3000/users \
  -H 'Content-Type: application/json' \
  -d '{"email":"richard@example.com"}'

curl -i -X POST http://localhost:3000/users \
  -H 'Content-Type: application/json' \
  -d '{"name":"Richard","email":"khong-phai-email"}'

curl -s http://localhost:3000/users
```

Điều kiện quay đạt:

- Cả ba POST đều trả 201 trước khi cài ValidationPipe.
- GET `/users` chứng minh dữ liệu sai đã chạm vào service/mảng, không chỉ bị controller bỏ qua.
- Không bật validation sớm chỉ để tạo cảnh demo.
- Sau cảnh cuối mới preview sơ đồ `Request → ValidationPipe → Controller` của EP02.

## 5. Title, caption và hashtag

**Title khuyên dùng:** TypeScript không bảo vệ API NestJS của bạn

**Caption đăng:**

```text
`email!: string` chỉ giúp TypeScript kiểm tra code khi phát triển. Payload HTTP vẫn là dữ liệu runtime và cần được kiểm tra bằng rule thật.

EP02 sẽ chặn cả ba request trước khi chúng chạm vào controller.
```

**Hashtag:** `#TypeScript #NestJS #ValidationPipe #Backend #APIDevelopment`

## 6. Nguồn và claim

| Claim | Nguồn |
|---|---|
| TypeScript xóa type sau khi compile và không thay đổi runtime behavior của JavaScript | [TypeScript for the New Programmer — Erased Types](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch#erased-types) |
| Payload qua network là plain object; ValidationPipe áp dụng rule runtime từ DTO class | [NestJS Validation](https://docs.nestjs.com/techniques/validation) |
| Definite assignment assertion `!` chỉ tác động type checking | [TypeScript 2.7 — Strict Class Initialization](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-7.html#strict-class-initialization) |

---

## Prompt chung nếu dùng AI sinh video từ kịch bản

```text
Tạo một YouTube Short dọc 9:16 từ đúng một mục SHORT trong file này.

Yêu cầu:
- Giữ nguyên claim kỹ thuật và chỉ dùng các nguồn trong mục Nguồn và claim.
- Voice tiếng Việt tự nhiên, tốc độ rõ ràng; không thêm lời chào hoặc intro.
- Frame 0–2 giây phải hiện bằng chứng thật: command, code hoặc HTTP response.
- Caption tối đa 5–7 từ mỗi dòng, dùng NestJS red #E0234E để highlight.
- Code dùng One Dark Pro, JetBrains Mono tối thiểu 24px và nằm trong safe zone giữa khung hình.
- Không bịa terminal output, package version, benchmark hoặc tính năng NestJS.
- Không biến UsersModule thành một runtime middleware; module chỉ wiring application graph.
- Kết thúc bằng đúng CTA và Related video đã ghi trong kịch bản.
- Trước khi render, xuất storyboard có timestamp để con người review.
```

## Checklist xuất bản tuần 1

- [ ] Mỗi Short chỉ truyền một insight.
- [ ] Code và response được quay từ cùng commit EP01.
- [ ] Font đọc được ở preview 320×568.
- [ ] Caption không che terminal output hoặc code chính.
- [ ] Không có secret, token, email thật hoặc notification cá nhân trên màn hình.
- [ ] Nguồn trong file vẫn mở được vào ngày sinh video.
- [ ] Related video trỏ đúng EP01/EP02.
- [ ] Title không vượt quá ý nghĩa đã chứng minh trên màn hình.
