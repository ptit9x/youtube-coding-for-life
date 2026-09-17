# NestJS ValidationPipe: Chặn data bẩn trước Controller | NestJS + AI #2

- **Series:** Học NestJS bằng AI — tập 2/45
- **Trạng thái:** ✅ Đã đăng
- **Title đã đăng:** NestJS ValidationPipe: Chặn data bẩn trước Controller | NestJS + AI #2
- **YouTube:** https://www.youtube.com/watch?v=GCWSSb6-qhk
- **Ngày đăng:** 2026-09-16
- **Thời lượng thực tế:** 6:45
- **Định dạng:** Host tự quay màn hình + tự thoại âm. Không AI voice, không AI footage.
- **AI tool:** Opus trong Antigravity IDE; giữ workflow Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng.
- **Technical baseline:** Tiếp tục project `nestjs-base-with-ai` từ EP01; Users API đang lưu dữ liệu trong RAM.
- **Target runtime:** 6:45 (thời lượng video đã đăng)
- **Audience:** Dev mới vào nghề / Fresher đã xem EP01 hoặc biết controller/service cơ bản.
- **Outcome chính:** Mọi payload đi vào Users API được kiểm tra trước controller bằng global ValidationPipe.
- **Cấu trúc mới:** `src/common/pipes/app-validation.pipe.ts` — boundary toàn ứng dụng, không phụ thuộc business domain.
- **Pain mở tập 3:** Validation đã chắc nhưng restart server là toàn bộ user biến mất.

---

## PART 1 — TRANSCRIPT VIDEO ĐÃ ĐĂNG (LÀM SẠCH)

### 0:00 — DTO khai báo string nhưng API vẫn nhận `123`

Ở tập trước, trong DTO mình đã khai báo `email` là string. Nhưng khi gửi request với giá trị 123, API vẫn nhận và tạo user bình thường. TypeScript có thể báo lỗi khi chúng ta viết code, nhưng người gọi API từ bên ngoài không quan tâm kiểu dữ liệu trong source code của mình.

### 0:28 — TypeScript type khác runtime validation

Type không phải là validation. TypeScript chỉ kiểm tra ở compile time. Khi ứng dụng chạy, request gửi lên chỉ là một plain JavaScript object. Nếu không có runtime validation thì dữ liệu sai vẫn có thể đi vào ứng dụng.

### 0:42 — Mục tiêu chặn dữ liệu trước controller

Mục tiêu của tập này là chặn dữ liệu sai trước khi nó đi vào controller. Mình không muốn viết nhiều câu `if/else` trong controller hay service. Thay vào đó, chúng ta sẽ tạo một lớp kiểm tra dùng chung.

### 0:57 — Workflow sáu bước và prompt

Mình tiếp tục sử dụng workflow sáu bước: yêu cầu, plan, review, approve, thực hiện và kiểm chứng.

Prompt lần này nói rõ Users API đang có `name` và `email` nhưng chưa có runtime validation. AI cần lập kế hoạch dùng `class-validator`, `class-transformer` và global `ValidationPipe`; pipe đặt trong `src/common`, không import `UsersModule`, còn DTO vẫn nằm trong module Users. Trước tiên chỉ đưa ra plan, chưa sửa code.

### 2:10 — Review kế hoạch

AI đề xuất cài `class-validator` và `class-transformer`, tạo một validation pipe dùng chung, thêm decorator validation vào DTO rồi đăng ký pipe toàn cục trong `main.ts`. Mình review lại kế hoạch trước khi cho AI thực hiện. Global pipe sẽ áp dụng cho tất cả module chứ không chỉ riêng Users.

### 2:51 — Duyệt command AI

Khi AI muốn chạy command, công cụ yêu cầu mình duyệt. Các bạn nên đọc command trước khi bấm Yes để biết AI sắp cài package hay thay đổi điều gì trong project.

### 3:20 — Decorator validation trong DTO

Trong `CreateUserDto`, AI thêm các decorator validation cho `name` và `email`. `IsString` kiểm tra đúng kiểu chuỗi, `IsEmail` kiểm tra định dạng email, còn `IsNotEmpty` bảo đảm giá trị không bị bỏ trống.

### 3:36 — Ba option của ValidationPipe

ValidationPipe có ba option chính. `transform` hỗ trợ chuyển đổi dữ liệu đầu vào. `whitelist` chỉ giữ lại những field đã được khai báo. `forbidNonWhitelisted` sẽ trả lỗi nếu request gửi thêm field không được phép.

### 3:57 — Chặn field thừa

Ví dụ nếu người dùng gửi thêm một field khác ngoài `name` và `email`, API sẽ chặn request đó thay vì âm thầm cho dữ liệu đi tiếp.

### 4:07 — Đăng ký pipe trong `main.ts`

Trong `main.ts`, chúng ta đăng ký pipe bằng `app.useGlobalPipes(new AppValidationPipe())`. Từ đây, mọi request HTTP đều phải đi qua bước validation trước khi tới controller.

### 4:20 — Trim khoảng trắng

Bây giờ mình kiểm tra trường hợp người dùng nhập khoảng trắng ở đầu hoặc cuối. Giá trị này ban đầu vẫn đi qua, nên mình yêu cầu xử lý `trim` cho `name` và `email`. Sau khi sửa, dữ liệu gửi lên được loại bỏ khoảng trắng trước khi kiểm tra và lưu lại.

### 4:56 — Message lỗi tiếng Việt

Tiếp theo mình muốn thông báo lỗi dễ hiểu hơn. Mình yêu cầu AI thêm message tiếng Việt vào các decorator, chẳng hạn `IsNotEmpty`. Khi gửi dữ liệu không hợp lệ, response trả về đúng message tiếng Việt để client biết field nào có vấn đề.

### 5:41 — Kiểm tra độ dài

Mình kiểm tra thêm giới hạn độ dài. Nếu chuỗi vượt quá 100 ký tự thì validation sẽ trả lỗi. Như vậy ngoài type và format, DTO còn kiểm soát được độ dài dữ liệu đầu vào.

### 6:09 — Restart làm mất dữ liệu

Sau khi tạo user thành công, mình restart server rồi gọi lại danh sách. Dữ liệu đã biến mất vì hiện tại user chỉ được lưu trong một mảng ở RAM.

### 6:25 — Teaser PostgreSQL và Prisma

Ở tập tiếp theo, chúng ta sẽ kết nối PostgreSQL và dùng Prisma để lưu dữ liệu thật vào database. Khi server restart, user vẫn còn. Cảm ơn các bạn đã xem video và hẹn gặp lại ở tập tiếp theo.

---

## PART 2 — TIMELINE VIDEO ĐÃ ĐĂNG

| Timestamp | Nội dung thực tế |
|---|---|
| 0:00 | DTO khai báo string nhưng API vẫn nhận `123` |
| 0:28 | TypeScript type khác runtime validation |
| 0:42 | Mục tiêu chặn dữ liệu trước controller |
| 0:57 | Workflow sáu bước và prompt |
| 2:10 | Review kế hoạch |
| 2:51 | Duyệt command AI |
| 3:20 | Decorator validation trong DTO |
| 3:36 | Ba option của ValidationPipe |
| 3:57 | Chặn field thừa |
| 4:07 | Đăng ký pipe trong `main.ts` |
| 4:20 | Trim khoảng trắng |
| 4:56 | Message lỗi tiếng Việt |
| 5:41 | Kiểm tra độ dài |
| 6:09 | Restart làm mất dữ liệu |
| 6:25 | Teaser PostgreSQL và Prisma |

**Thời lượng thực tế:** 6:45.

### Command chuẩn bị

```bash
cd nestjs-base-with-ai
npm i class-validator class-transformer
npm run start:dev
npm run build
```

### Prompt cho Opus

```text
The in-memory Users API accepts invalid runtime payloads. Create a validation plan.

Requirements:
- Use class-validator and class-transformer.
- Create a reusable global pipe at src/common/pipes/app-validation.pipe.ts.
- Enable transform, whitelist and forbidNonWhitelisted.
- Validate CreateUserDto.name and CreateUserDto.email with Vietnamese messages.
- Keep Users-specific rules inside src/modules/users.
- common must not import UsersModule or any business-domain code.
- Propose a fuzz-test matrix covering: valid input, wrong type, malformed email,
  missing field, extra field and whitespace-only name.

Workflow:
1. Do not edit files yet.
2. Show the plan and expected behavior for every test payload.
3. Wait for my approval.
4. After approval, implement the plan.
5. Run the build and report the exact files changed.
```

### Code đích để đối chiếu khi quay

```typescript
// src/common/pipes/app-validation.pipe.ts
import { ValidationPipe } from '@nestjs/common';

export class AppValidationPipe extends ValidationPipe {
  constructor() {
    super({
      transform: true,
      whitelist: true,
      forbidNonWhitelisted: true,
    });
  }
}
```

```typescript
// src/main.ts
import { AppValidationPipe } from './common/pipes/app-validation.pipe';

app.useGlobalPipes(new AppValidationPipe());
```

```typescript
// src/modules/users/dto/create-user.dto.ts
import { Transform } from 'class-transformer';
import {
  IsEmail,
  IsNotEmpty,
  IsString,
  MaxLength,
} from 'class-validator';

export class CreateUserDto {
  @Transform(({ value }) =>
    typeof value === 'string' ? value.trim() : value,
  )
  @IsString({ message: 'Tên phải là chuỗi' })
  @IsNotEmpty({ message: 'Tên không được để trống' })
  @MaxLength(80, { message: 'Tên không được vượt quá 80 ký tự' })
  name!: string;

  @IsString({ message: 'Email phải là chuỗi' })
  @IsEmail({}, { message: 'Email không đúng định dạng' })
  email!: string;
}
```

### Fuzz-test matrix

| # | Payload | Kết quả mong đợi |
|---|---|---|
| 1 | `{ "name": "Richard", "email": "richard@example.com" }` | 201 |
| 2 | `{ "name": "Richard", "email": 123 }` | 400 — sai type |
| 3 | `{ "name": "Richard", "email": "richard-at-example.com" }` | 400 — sai format |
| 4 | `{ "email": "richard@example.com" }` | 400 — thiếu name |
| 5 | `{ "name": "Richard", "email": "richard@example.com", "role": "admin" }` | 400 — field thừa |
| 6 | `{ "name": "   ", "email": "richard@example.com" }` | 201 trước khi trim; 400 sau khi thêm Transform |

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

Ảnh tham chiếu của series: `../01-hoc-nestjs-voi-ai/thumbnail-01-hoc-nestjs-cung-ai.png`. Giữ cùng host, bố cục, ánh sáng đỏ và typography; chỉ đổi badge thành `EP02`, headline thành `CHẶN / DATA BẨN`, và màn hình thành request `POST /users` với `"email": 123` bị trả `400 Bad Request`. Badge `CÙNG AI` giữ nguyên.

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. NestJS ValidationPipe: Chặn data bẩn trước Controller | NestJS + AI #2
2. DTO và ValidationPipe khác nhau thế nào? — EP02 | Lập trình là cuộc sống
3. Kiểm tra email và payload trong NestJS — EP02 | Lập trình là cuộc sống
4. Cấu hình Global ValidationPipe trong NestJS — EP02 | Lập trình là cuộc sống
5. Vì sao TypeScript không chặn dữ liệu API sai? — EP02 | Lập trình là cuộc sống

**Title 1 là title đã đăng.** Các title còn lại được giữ làm tư liệu tham khảo.

### 4b. SEO Description

```text
DTO nói email phải là string, nhưng Users API vẫn nhận số 123. TypeScript chỉ bảo vệ lúc compile — dữ liệu từ internet cần một lớp validation thật ở runtime.

✅ Phân biệt TypeScript type và runtime validation
✅ Cài class-validator và class-transformer
✅ Tạo AppValidationPipe dùng chung trong src/common/pipes
✅ Hiểu transform, whitelist và forbidNonWhitelisted
✅ Validate name và email với message tiếng Việt
✅ Dùng AI tạo fuzz-test matrix thay vì chỉ test happy path
✅ Bắt lỗi chuỗi toàn dấu cách mà IsNotEmpty vẫn cho qua
✅ Restart server để mở pain PostgreSQL cho tập 3

🔗 Links:
NestJS Validation: https://docs.nestjs.com/techniques/validation
class-validator: https://github.com/typestack/class-validator
Source series: https://github.com/ptit9x/youtube-coding-for-life

⏱ Timestamps thực tế:
0:00 DTO khai báo string nhưng API vẫn nhận 123
0:28 TypeScript type khác runtime validation
0:42 Chặn dữ liệu trước controller
0:57 Workflow sáu bước và prompt
2:10 Review kế hoạch
2:51 Duyệt command AI
3:20 Decorator validation trong DTO
3:36 Ba option của ValidationPipe
3:57 Chặn field thừa
4:07 Đăng ký pipe trong main.ts
4:20 Trim khoảng trắng
4:56 Message lỗi tiếng Việt
5:41 Kiểm tra độ dài
6:09 Restart làm mất dữ liệu
6:25 Teaser PostgreSQL và Prisma

#NestJS #ValidationPipe #ClassValidator #TypeScript #Backend #AICoding #Opus #Antigravity #Fresher #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs validation, nestjs validationpipe, nestjs dto validation, class validator nestjs, class transformer nestjs, dto có type vẫn sai, runtime validation typescript, nestjs tiếng việt, học nestjs, nestjs tập 2, users api nestjs, forbid non whitelisted, whitelist validationpipe, transform validationpipe, custom validation message, fuzz test api, opus coding, antigravity ide, ai coding mentor, backend fresher, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Thumbnail đã tạo

![Thumbnail NestJS EP02 — Chặn data bẩn](./thumbnail-02-chan-data-ban.png)

**Typography chung của series:** Canvas 1672×941. Headline condensed đậm bên trái, host bên phải, monitor là lớp phụ. Chỉ dùng WHITE `#FFFFFF`, NEST RED `#E0234E`, đen và navy đậm; stroke đen và shadow gọn. Kiểm tra dấu tiếng Việt và độ đọc ở bản thu nhỏ 320×180 trước khi đăng.
