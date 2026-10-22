# NestJS #11.5 — Zod vs class-validator: một nguồn sự thật cho validation

- **Series:** Học NestJS bằng AI — Bonus 11.5, xen giữa EP11 và EP12, không renumber.
- **Target runtime:** 7–8 phút (~650–700 từ thoại)
- **Outcome:** Quyết định có rationale: dự án mới chọn Zod (một nguồn sự thật, error chi tiết, thư viện đang sống); dự án đang chạy class-validator ngon thì không migrate. Có `ZodValidationPipe` dùng chung + demo POST `/tasks`.
- **Pain mở (kế thừa EP11):** common library tách xong nhưng validation pipe kéo `class-validator` + `class-transformer` vào package dùng chung — trong khi env đã validate bằng Zod từ EP03.
- **Không tạo pain mới:** EP12 vẫn mở đúng pain cũ của nó (debug request qua nhiều layer). Bonus off-chain.

---

## PART 1 — SCRIPT

Hai response này cùng chặn một payload sai.

Bên trái, class-validator: `title must be a string, received number`. Bên phải, Zod: path `title`, expected string, received number. Kèm luôn lý do và vị trí.

Cùng lúc đó, trong repo vừa tách xong common library, mình thấy một dependency khiến mình khó chịu.

class-transformer.

Lần publish cuối của nó là ngày hai-mươi-hai, tháng mười-một, năm hai-ngàn-không-trăm-hai-mươi-mốt. Tính đến hôm nay, gần năm năm.

Mọi request của TaskFlow đều đi qua pipe dựa trên thư viện đó.

Và điều buồn cười: từ tập ba, file `.env` của chính app này đã được validate bằng Zod.

Payload vào bằng class-validator. Cấu hình vào bằng Zod. Một app, hai hệ validation song song.

Tập này mình chốt một quyết định, không phải một trend.

Nhìn kỹ cách viết hiện tại.

Một interface TypeScript mô tả hình dạng dữ liệu. Một class DTO với decorator mô tả rule chạy được. Hai khai báo cho cùng một knowledge.

AI thêm field vào interface mà quên decorator, compiler vẫn im lặng. Type nói một đằng, runtime làm một nẻo. Lệch nhau lúc nào không hay.

Zod chỉ khai báo một lần. Schema là nguồn sự thật chạy được. `z.infer` suy ra type TypeScript từ chính schema đó.

Sửa schema, type đổi theo ngay lập tức. Không còn chỗ để lệch.

Thứ hai: error. class-validator muốn message rõ ràng thì tự viết từng field, từng message. Zod báo sẵn path, code, expected và received. Format mặc định đã máy đọc được, client map được.

Thứ ba, lý do nặng ký nhất: class-validator kéo theo class-transformer — thư viện gần năm năm không cập nhật. Zod đang publish đều tháng, kèm hệ sinh thái nestjs-zod và zod-openapi.

Mình đưa AI mục tiêu: chuyển đúng endpoint POST /tasks sang Zod, viết một ZodValidationPipe đặt trong common, mọi endpoint khác giữ nguyên. Plan trước, chưa sửa code.

AI trả plan — và như thường lệ, nó phình to. Plan của AI muốn migrate toàn bộ DTO và xóa class-validator khỏi repo trong một sweep.

Nghe rất quyết đoán. Nhưng TaskFlow đang chạy ổn, test đang xanh. Migrate mười mấy DTO chỉ để cảm giác gọn hơn là mua rủi ro không cần thiết.

Mình cắt plan về đúng một endpoint. Rồi approve.

Trong lúc AI xử lý, nói về pipe này.

Nó ngắn. Constructor nhận một Zod schema. `transform` gọi `schema.parse`.

Nếu parse fail, Zod ném ZodError. Đoạn map error này mình tự gõ: lấy từng issue, ghép path thành chuỗi, ném BadRequestException kèm danh sách field sai kèm lý do.

Không magic. Vài chục dòng, nằm trong tầm kiểm soát của mình.

Ở controller, pipe đứng ngay trong `@Body`, nhận schema làm tham số. Type của body lấy từ `z.infer` — một khai báo duy nhất cho cả runtime và compile-time.

Kiểm chứng.

Quay lại màn hình đầu video. Gửi payload sai cho endpoint mới — response chỉ đúng field sai, đúng lý do, đúng path.

Endpoint dùng class-validator vẫn chạy y xì trước đó. Toàn bộ test vẫn xanh.

Không migration. Không big-bang.

Zod có giá, phải nói thẳng.

class-validator là decorator, nên Nest tự sinh schema Swagger từ DTO. Chuyển sang Zod thì phải thêm nestjs-zod hoặc zod-openapi. Không khó, nhưng là một việc nữa — và tập mười-ba làm Swagger, mình sẽ ghé lại đúng điểm này.

Tài liệu chính thức của NestJS vẫn viết theo class-validator. Team toàn junior thì tra cứu theo tài liệu gốc sẽ nhanh hơn.

Chốt lại: dự án mới, mình chọn Zod — một nguồn sự thật, error tốt, thư viện đang sống. Dự án đang chạy class-validator ngon thì để yên. Đừng migrate chỉ vì trend.

Tập sau quay lại trục chính: request đi qua middleware, guard, interceptor, pipe — và khi nó lỗi ở đâu đó giữa chuỗi đó mà không có bản đồ, debug là địa ngục.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Cold open: hai response 400 cạnh nhau — class-validator vs Zod (path + expected/received) | 25s |
| 2 | [IDE] | `package.json` của library: class-transformer; tab npm: last publish 22/11/2021 | 30s |
| 3 | [IDE] | `env.validation.ts` (Zod, từ EP03) đặt cạnh `CreateTaskDto` (class-validator) | 30s |
| 4 | [DIAGRAM] | Một app hai hệ validation → sau này một schema cho type + runtime + error | 40s |
| 5 | [IDE] | DTO hiện tại: interface + class decorator (hai nguồn sự thật); demo `z.infer` suy type | 45s |
| 6 | [AI] | Prompt plan swap một endpoint; plan AI trả về migrate toàn bộ | 50s |
| 7 | [IDE] | Host cắt scope plan về một endpoint, approve | 20s |
| 8 | [IDE] | Viết `ZodValidationPipe`; host tự gõ đoạn map ZodError (fast-forward + voice-over) | 70s |
| 9 | [BROWSER] | POST `/tasks` payload sai → error Zod có path; endpoint cũ y xì; chạy test xanh | 45s |
| 10 | [IDE] | Màn hình npm: zod 4.6.7 (10/2026), nestjs-zod 5.5.0, zod-openapi 6.0.2 đối diện class-transformer (2021) | 25s |
| 11 | [B-ROLL] | Card chốt: dự án mới → Zod; đang chạy ngon → giữ nguyên | 20s |

**Tổng mục tiêu: 6 phút 40 giây + buffer ≈ 7–8 phút.** One Dark Pro, JetBrains Mono 18–20px, che token và URL production trước khi quay.

### Code cốt lõi

```ts
// src/common/pipes/zod-validation.pipe.ts
import { BadRequestException, Injectable, PipeTransform } from '@nestjs/common';
import { ZodError, type ZodType } from 'zod';

@Injectable()
export class ZodValidationPipe<T> implements PipeTransform<unknown, T> {
  constructor(private readonly schema: ZodType<T>) {}

  transform(value: unknown): T {
    try {
      return this.schema.parse(value);
    } catch (error) {
      if (error instanceof ZodError) {
        throw new BadRequestException({
          message: 'Validation failed',
          errors: error.issues.map((issue) => ({
            path: issue.path.join('.'),
            code: issue.code,
            message: issue.message,
          })),
        });
      }
      throw error;
    }
  }
}
```

```ts
// src/modules/tasks/create-task.schema.ts
import { z } from 'zod';

export const CreateTaskSchema = z.object({
  title: z.string().trim().min(1, 'Tiêu đề không được rỗng').max(200),
  dueDate: z.iso.datetime().optional(),
});

export type CreateTaskDto = z.infer<typeof CreateTaskSchema>;
```

```ts
// src/modules/tasks/tasks.controller.ts (chỉ endpoint này đổi)
@Post()
@RequirePermissions('tasks.create')
create(
  @Body(new ZodValidationPipe(CreateTaskSchema)) body: CreateTaskDto,
) {
  return this.tasksService.create(body);
}
```

### Prompt cho AI

```text
TaskFlow validates DTOs with class-validator and a global ValidationPipe.
We already use Zod for env validation (src/config/env.validation.ts).
Plan a migration to Zod for the POST /tasks endpoint ONLY.
Write one reusable ZodValidationPipe in src/common/pipes.
Keep class-validator for every other endpoint. Do not remove any dependency.
Present the plan first. Do not modify code before approval.
```

**Điểm host phải bắt:** plan AI sẽ đề xuất migrate toàn bộ DTO và xóa class-validator. Host cắt scope về một endpoint — lý do: app đang ổn, test đang xanh, migrate hàng loạt là rủi ro không đổi lại giá trị gì.

---

## PART 3 — TITLES, SEO DESCRIPTION & KEYWORDS

### 3a. Titles

1. NestJS #11.5: Zod vs class-validator — Chọn gì cho dự án mới?
2. NestJS #11.5: Đừng viết Type và Validator hai lần
3. NestJS #11.5: class-validator còn đáng tin không?
4. NestJS #11.5: ZodValidationPipe — vài chục dòng thay cả thư viện
5. NestJS #11.5: Một schema Zod = Schema + Type + Error

**Khuyên dùng:** Title 1 (đúng intent search "zod vs class-validator"). A/B thêm Title 2 cho concept và Title 4 cho người muốn code ngay.

### 3b. SEO Description

```text
class-transformer gần 5 năm không update, trong khi .env của chính app đã validate bằng Zod từ EP03. Một app, hai hệ validation — tập này chốt: chọn gì cho dự án mới?

✅ Một nguồn sự thật: schema Zod → z.infer ra type TS
✅ Error có path + expected/received, không cần custom message từng field
✅ Tự viết ZodValidationPipe, không magic
✅ AI đòi migrate toàn bộ — và lý do mình từ chối
✅ Giá phải trả: Swagger và nestjs-zod / zod-openapi
✅ Đang chạy class-validator ngon thì đừng migrate

⏱ 0:00 Hai error, hai thế giới
⏱ 1:00 Hai hệ validation trong một app
⏱ 2:00 Ba lý do nghiêng về Zod
⏱ 3:30 AI plan phình to — cắt scope
⏱ 4:30 Viết ZodValidationPipe
⏱ 6:00 Kiểm chứng + giá phải trả

#NestJS #Zod #class-validator #TypeScript #Validation #Backend #LapTrinhLaCuocSong
```

### 3c. Keywords / Tags

```text
zod nestjs, zod vs class-validator, zodvalidationpipe, zod validation nestjs, nestjs validation, nestjs dto validation, zod infer typescript, class-validator nestjs, class-transformer, nestjs validation pipe custom, zod tiếng việt, nestjs #11.5, học nestjs bằng ai, taskflow nestjs, lập trình là cuộc sống
```

---

## PART 4 — THUMBNAIL PACKAGE (code-centric, theo visual grammar series)

- Canvas 1280×720, nền đen/navy đậm, NEST RED `#E0234E` + WHITE, không nhân vật.
- Bố cục: headline lớn bên trái (~1/3 frame), bên phải là monitor hai JSON error cạnh nhau — trái mờ xám (class-validator, badge đỏ `2021`), phải sáng rõ (Zod, badge `#path`). Badge số tập `#11.5` nhỏ.
- Font condensed đậm (Anton + JetBrains Mono cho JSON), stroke đen, shadow gọn, không neon glow.
- Kiểm tra dấu tiếng Việt ở bản thu nhỏ 320×180 trước khi chốt.

### Option 1 — khuyên dùng
- `ZOD` — WHITE
- `THẮNG?` — NEST RED `#E0234E`

### Option 2
- `1 SCHEMA` — WHITE
- `3 TRONG 1` — NEST RED `#E0234E`

### Option 3
- `5 NĂM` — WHITE
- `KHÔNG UPDATE` — NEST RED `#E0234E`
