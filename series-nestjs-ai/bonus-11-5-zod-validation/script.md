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

Mọi request của User Management đều đi qua pipe dựa trên thư viện đó.

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

Mình yêu cầu AI chuyển đúng endpoint POST /tasks sang Zod. Pipe mới nằm trong common. Mọi endpoint khác giữ nguyên.

AI trả plan — và như thường lệ, nó phình to. Plan của AI muốn migrate toàn bộ DTO và xóa class-validator khỏi repo trong một sweep.

Nghe rất quyết đoán. Nhưng User Management đang chạy ổn, test đang xanh. Migrate mười mấy DTO chỉ để cảm giác gọn hơn là mua rủi ro không cần thiết.

Mình cắt plan về đúng một endpoint. Rồi approve.

Trong lúc AI xử lý, nói về pipe này.

Nó ngắn. Constructor nhận một Zod schema. `transform` gọi `schema.parse`.

Nếu parse fail, Zod ném ZodError. Mình tự gõ đoạn map từng issue thành path và lý do. Sau đó pipe ném BadRequestException.

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

Tập sau, request đi qua middleware, guard, interceptor và pipe. Không có bản đồ, debug chuỗi đó là địa ngục.

Link Git của nhánh này nằm trong description. Bạn có thể comment phần còn khó hiểu.

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
nestjs-base-with-ai validates DTOs with class-validator and a global ValidationPipe.
We already use Zod for env validation (src/config/env.validation.ts).
Plan a migration to Zod for the POST /tasks endpoint ONLY.
Write one reusable ZodValidationPipe in src/common/pipes.
Keep class-validator for every other endpoint. Do not remove any dependency.
Present the plan first. Do not modify code before approval.
```

**Điểm host phải bắt:** plan AI sẽ đề xuất migrate toàn bộ DTO và xóa class-validator. Host cắt scope về một endpoint — lý do: app đang ổn, test đang xanh, migrate hàng loạt là rủi ro không đổi lại giá trị gì.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of two dark IDE error panels facing each other on a developer monitor, the left panel dim and fragmented while the right panel shows a sharp structured validation path in neon green and cyan, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.`
2. `A cinematic photograph of a Vietnamese developer on the right studying one glowing Zod schema that branches into type, validation and error output, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.`
3. `A cinematic photograph of code reflected on developer eyeglasses while a dark IDE shows an old decorator stack fading beside a bright Zod schema, neon syntax highlighting, dark IDE theme, cinematic lighting, film grain, anamorphic lens flare, shallow depth of field, city bokeh, 8k, 16:9, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Zod hay class-validator cho dự án NestJS mới? — #11.5 | Lập trình là cuộc sống
2. Đừng viết Type và Validator hai lần — NestJS #11.5 | Lập trình là cuộc sống
3. class-validator còn đáng tin không? — NestJS #11.5 | Lập trình là cuộc sống
4. Một ZodValidationPipe thay đổi cách tôi viết DTO — #11.5 | Lập trình là cuộc sống
5. Một schema Zod làm ba việc — NestJS #11.5 | Lập trình là cuộc sống
6. Hai hệ validation trong một app là quá nhiều — #11.5 | Lập trình là cuộc sống
7. AI muốn migrate toàn bộ DTO, tôi chỉ đổi một endpoint — #11.5 | Lập trình là cuộc sống
8. Zod thắng ở đâu và thua ở đâu? — NestJS #11.5 | Lập trình là cuộc sống
9. Đừng migrate validation chỉ vì thư viện mới hơn — #11.5 | Lập trình là cuộc sống
10. TypeScript không tự validate request — NestJS #11.5 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1 (đúng intent search "zod vs class-validator"). A/B thêm Title 2 cho concept và Title 4 cho người muốn code ngay.

### 4b. SEO Description

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

### 4c. Keywords / Tags

```text
zod nestjs, zod vs class-validator, zodvalidationpipe, zod validation nestjs, nestjs validation, nestjs dto validation, zod infer typescript, class-validator nestjs, class-transformer, nestjs validation pipe custom, zod tiếng việt, nestjs #11.5, học nestjs bằng ai, nestjs-base-with-ai nestjs, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng

**Image prompt:** `A cinematic photograph, a Vietnamese developer silhouette on the right facing two oversized floating validation error panels, the old panel cracked and fading while the Zod panel glows sharply, dramatic neon lighting in green cyan and purple, code text floating and reflecting in the scene, dark moody background with city bokeh and rain, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

- `ZOD` — WHITE `#FFFFFF`
- `THẮNG?` — NEON GREEN `#00FF41`

### Option 2

**Image prompt:** `A cinematic photograph, a glowing Zod schema on the right splitting into three floating code layers for type validation and error output, dramatic neon lighting in green cyan and purple, exaggerated code reflections, dark moody background with fog and city bokeh, extreme contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

- `1 SCHEMA` — WHITE `#FFFFFF`
- `3 TRONG 1` — NEON GREEN `#00FF41`

### Option 3

**Image prompt:** `A cinematic photograph, a developer silhouette on the right watching an old validation package timestamp dissolve beside fresh neon Zod code, dramatic green cyan and purple lighting, floating code text, rain on the window, city bokeh, extreme contrast, deep shadows, empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

- `5 NĂM` — NEON GREEN `#00FF41`
- `KHÔNG UPDATE` — WHITE `#FFFFFF`

### Typography specs — áp dụng cả ba option

- Canvas 1280×720. Dùng Anton cho hook hoặc JetBrains Mono cho cảm giác code.
- Mỗi dòng cao khoảng 110–140px, line spacing 0.85; text chiếm khoảng một phần ba khung bên trái.
- Tạo neon glow bằng layer nhân bản, blur 8–12px, opacity 60–70%; thêm stroke đen 6–10px.
- Không đặt chữ lên mặt hoặc key visual. Thêm scan-line hoặc noise nhẹ trên background.
- Nên tạo ảnh sạch không chữ rồi typeset trong Canva để typography ổn định giữa các tập.
