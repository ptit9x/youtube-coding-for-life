# NestJS #02 — ValidationPipe: Chặn dữ liệu sai từ DTO

- **Series:** Học NestJS bằng AI — tập 2/46
- **Định dạng:** Host tự quay màn hình + tự thoại âm. Không AI voice, không AI footage.
- **AI tool:** Opus trong Antigravity IDE; giữ workflow Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng.
- **Technical baseline:** Tiếp tục project `nestjs-base-with-ai` từ EP01; Users API đang lưu dữ liệu trong RAM.
- **Target runtime:** ~11:55
- **Audience:** Dev mới vào nghề / Fresher đã xem EP01 hoặc biết controller/service cơ bản.
- **Outcome chính:** Mọi payload đi vào Users API được kiểm tra trước controller bằng global ValidationPipe.
- **Cấu trúc mới:** `src/common/pipes/app-validation.pipe.ts` — boundary toàn ứng dụng, không phụ thuộc business domain.
- **Pain mở tập 3:** Validation đã chắc nhưng restart server là toàn bộ user biến mất.

---

## PART 1 — SCRIPT

Cuối tập trước, DTO nói `email` phải là string. Nhưng mình gửi số 123, server vẫn trả 201. TypeScript nhìn thấy lỗi khi mình viết code. Người gọi API thì chẳng cần quan tâm TypeScript nghĩ gì.

Đây là một nhầm lẫn rất phổ biến. Type không phải validation. TypeScript chỉ bảo vệ lúc compile. Khi ứng dụng chạy, request từ internet chỉ là một object JavaScript. Nếu không có người kiểm tra ở cửa, dữ liệu nào cũng có thể đi vào service.

Mục tiêu tập này rất rõ: dữ liệu sai phải dừng trước controller. Controller không nên tự viết hàng loạt câu `if`. UsersService càng không nên đoán payload đã sạch hay chưa. Ta cần một boundary dùng chung cho toàn ứng dụng.

Mình vẫn bắt đầu bằng workflow sáu bước. Yêu cầu, plan, review, approve, thực hiện và kiểm chứng. Lần này phần kiểm chứng không chỉ có một payload đúng. Mình sẽ nhờ AI nghĩ như một người đang cố phá API.

Prompt của mình như sau:

“Users API hiện nhận `name` và `email`, nhưng chưa có runtime validation. Hãy lập plan dùng `class-validator`, `class-transformer` và global ValidationPipe. Pipe đặt trong `src/common/pipes`, không được import UsersModule. DTO vẫn nằm trong Users. Hãy đề xuất bảng payload có cả trường hợp hợp lệ và dữ liệu bậy. Phải gồm sai type, sai email, thiếu field, thừa field và chuỗi toàn dấu cách. Chưa sửa code trước khi tôi approve.”

AI trả về ba nhóm thay đổi. Một: cài hai package validation. Hai: tạo `AppValidationPipe` dùng cho toàn app. Ba: thêm rule vào `CreateUserDto`. Nó cũng đưa ra sáu payload để test. Mình kiểm tra chiều dependency: common chỉ import Nest, không biết Users là ai. Users được phép dùng decorator từ package validation. Không có import ngược từ common vào business module. Plan ổn, mình approve.

Terminal chạy `npm i class-validator class-transformer`. Hai package có hai nhiệm vụ khác nhau. `class-transformer` biến plain object thành instance phù hợp ở runtime. `class-validator` đọc decorator trên DTO rồi kiểm tra từng field.

Trong `src/common/pipes`, AI tạo `AppValidationPipe`. Bên trong có ba option. `transform` bật việc chuyển đổi payload. `whitelist` xác định field nào được phép đi tiếp. `forbidNonWhitelisted` biến field thừa thành lỗi 400, thay vì âm thầm bỏ qua.

Pipe nằm trong common vì đây là boundary áp dụng cho toàn ứng dụng, không thuộc riêng Users hay Auth. Nó không chứa business rule như “email công ty phải có domain nào”. Những rule đó vẫn phải ở module sở hữu nghiệp vụ.

Mở `main.ts`. Chỉ cần một dòng `app.useGlobalPipes(new AppValidationPipe())`. Từ lúc này, mọi HTTP endpoint đi qua chiếc cổng chung trước khi controller được gọi. Nếu payload sai, service thậm chí không biết request đó từng tồn tại.

Quay lại `CreateUserDto`. `name` có `IsString`, `IsNotEmpty` và giới hạn độ dài. `email` có `IsString` và `IsEmail`. Mỗi decorator có message tiếng Việt để client hiểu field nào sai. Đây vẫn là DTO của Users, vì cấu trúc dữ liệu đầu vào thuộc boundary của business module này.

Đến lúc kiểm chứng. Payload đầu tiên có name Richard và email hợp lệ. Server trả 201. Payload thứ hai đổi email thành số 123. Lần này response là 400, còn `UsersService.create` không hề chạy.

Payload thứ ba dùng chuỗi `richard-at-example.com`. Vẫn là string, nhưng không phải email. `IsEmail` chặn nó. Payload thứ tư bỏ hẳn name. `IsNotEmpty` trả lỗi rõ ràng. Type và format là hai lớp kiểm tra khác nhau; thiếu một lớp, dữ liệu bẩn vẫn lọt.

Payload thứ năm thêm `role: "admin"`. Nếu chỉ bật whitelist, field này sẽ bị bỏ đi. Nhưng mình đã bật `forbidNonWhitelisted`, nên API trả 400. Với dữ liệu nhạy cảm, từ chối rõ ràng thường dễ quan sát hơn âm thầm sửa request của client.

Còn payload cuối: name chỉ gồm ba dấu cách. AI dự đoán nó sẽ bị chặn. Thực tế server vẫn trả 201. `IsNotEmpty` thấy đây là một string có ba ký tự. Nó không hiểu ba ký tự đó chẳng tạo thành tên người.

Đây là lý do mình không dừng ở câu “AI đã viết xong”. Bộ fuzz test vừa tìm ra lỗ hổng trong chính plan của AI. Mình tự thêm `Transform` để trim name trước validation. Chạy lại payload cũ. Sau khi ba dấu cách trở thành chuỗi rỗng, `IsNotEmpty` mới chặn đúng.

Bây giờ xem git diff. Common có một pipe không phụ thuộc domain. Users DTO giữ rule của Users. `main.ts` chỉ đăng ký boundary toàn cục. Chạy build, rồi chạy lại toàn bộ sáu payload. Một payload hợp lệ trả 201. Năm payload sai đều trả 400.

Validation đã đóng được cửa trước. Nhưng còn một vấn đề khác. Tạo một user, restart server rồi GET `/users`. Danh sách lại rỗng. Dữ liệu vẫn nằm trong một mảng RAM, nên mỗi lần server khởi động là một lần mất trí nhớ.

Tập sau, ta sẽ đưa Users vào PostgreSQL bằng Prisma. Quan trọng hơn, business logic sẽ không phụ thuộc trực tiếp Prisma. Controller gọi service, service phụ thuộc repository contract, còn database chỉ là adapter được Nest nối vào.

AI có thể đề xuất rule. Chỉ dữ liệu thật và những test khó chịu mới cho biết rule đó có đứng vững hay không. AI viết, mình hiểu — và mình vẫn kiểm chứng.

Nếu bạn muốn thấy user sống sót sau một lần restart, gặp lại ở NestJS số ba. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Setup:** Tiếp tục đúng project và theme từ EP01. Font JetBrains Mono ≥18px. Agent panel bên phải, Postman hoặc REST client bên trái khi test. Quay 1920×1080, con trỏ có highlight.

| # | Type | Nội dung quay | Thoại khớp | Thời lượng |
|---|---|---|---|---|
| 1 | [BROWSER]+[IDE] | Replay POST từ EP01 với `email: 123` nhưng vẫn 201; đặt cạnh DTO `email!: string` | Cold open: type vẫn để payload sai lọt qua | 35s |
| 2 | [DIAGRAM] | Hai cột: compile time có TypeScript; runtime nhận plain JavaScript object | Type không phải validation | 45s |
| 3 | [DIAGRAM] | Request → Global Pipe → Controller → Service; dấu chặn đỏ trước controller | Mục tiêu boundary toàn app | 35s |
| 4 | [IDE] | Gõ prompt validation; agent chỉ trình plan và test matrix | Yêu cầu → Plan | 55s |
| 5 | [IDE] | Review plan, highlight dependency `common` không import `modules/users`; approve | Review → Approve | 55s |
| 6 | [TERM] | `npm i class-validator class-transformer`; mở package diff | Hai package, hai nhiệm vụ | 55s |
| 7 | [IDE] | Tạo `common/pipes/app-validation.pipe.ts`; highlight ba option | Global ValidationPipe | 55s |
| 8 | [IDE] | `main.ts` đăng ký pipe; diagram request bị chặn trước controller | Đăng ký boundary | 50s |
| 9 | [IDE] | `CreateUserDto`; highlight rule của name và email cùng message tiếng Việt | Rule nằm trong Users | 50s |
| 10 | [BROWSER] | POST hợp lệ → 201; `email: 123` → 400 | Test type | 45s |
| 11 | [BROWSER] | Email sai định dạng; thiếu name; đọc response message | Test format và field bắt buộc | 45s |
| 12 | [BROWSER] | Thêm `role: "admin"` → 400; đối chiếu `forbidNonWhitelisted` | Test field thừa | 45s |
| 13 | [BROWSER]+[IDE] | `name: "   "` bất ngờ trả 201; zoom `IsNotEmpty` | Fuzz test bắt blind spot | 40s |
| 14 | [IDE] | Host tự gõ `@Transform` trim name; watch mode reload; payload cũ → 400 | Tự sửa và kiểm chứng | 35s |
| 15 | [IDE]+[TERM] | `git diff`, `npm run build`; chạy lại test matrix, bảng 1 xanh + 5 đỏ | Verification | 40s |
| 16 | [TERM]+[BROWSER] | Tạo user → restart server → GET `/users` trả `[]`; end card EP03 Prisma | Pain mới + CTA | 30s |

**Tổng: 715 giây ≈ 11:55.** Sau khi thu voice, chỉnh timestamp theo waveform thật.

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

1. ValidationPipe NestJS: Chặn dữ liệu sai từ DTO — EP02 | Lập trình là cuộc sống
2. DTO và ValidationPipe khác nhau thế nào? — EP02 | Lập trình là cuộc sống
3. Kiểm tra email và payload trong NestJS — EP02 | Lập trình là cuộc sống
4. Cấu hình Global ValidationPipe trong NestJS — EP02 | Lập trình là cuộc sống
5. Vì sao TypeScript không chặn dữ liệu API sai? — EP02 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 4 cho search và Title 5 cho misconception.

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

⏱ Timestamps dự kiến:
0:00 DTO nói string, API vẫn nhận số
0:35 Type khác validation
1:20 Validation phải đứng trước controller
1:55 Prompt AI và test matrix
2:50 Review chiều dependency
3:45 Cài class-validator và class-transformer
4:40 AppValidationPipe trong common
5:35 Rule cho name và email
6:25 Test email là số
7:15 Test email sai và thiếu field
8:00 Chặn field role thừa
8:45 Ba dấu cách vẫn lọt
9:30 Tự thêm Transform để trim
10:10 Chạy lại toàn bộ test
10:45 Restart server — dữ liệu biến mất
11:25 Teaser Prisma + PostgreSQL

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
