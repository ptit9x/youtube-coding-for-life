# NestJS #14 — Tách common thành thư viện dùng cho nhiều dự án

- **Series:** Học NestJS bằng AI — tập 14/45
- **Target runtime:** 8–10 phút (650–800 từ thoại)
- **Outcome:** Một package cross-cutting có public API, version và hai consumer thật.
- **Pain mở EP15:** Quá nhiều cross-cutting layer khiến request lỗi trước controller mà không rõ bị chặn ở đâu.

---

## PART 1 — SCRIPT

TaskFlow đã có validation pipe, exception filter và pagination helper ổn định.

Một dự án NestJS mới cũng cần những thứ đó.

Cách nhanh nhất là copy cả folder `common/` sang repo mới.

Hai tuần sau, một filter được sửa ở dự án A nhưng không sửa ở dự án B.

Chúng ta có hai nguồn sự thật và không biết bản nào đúng.

Phần thật sự portable phải trở thành library có phiên bản và một public API rõ ràng.

Không phải mọi file trong `common/` đều thật sự dùng chung.

Mình yêu cầu AI lập bảng dependency cho từng file.

Validation pipe phụ thuộc Nest và class-validator. Exception filter phụ thuộc Nest, còn pagination helper chỉ cần TypeScript.

Permission decorator gắn AccessControl policy. CurrentUser decorator lại dựa vào Auth contract của TaskFlow.

Ba file đầu có khả năng portable. Hai file cuối vẫn gắn business domain.

Tên folder `common` không tự biến code thành reusable.

Dependency mới là bằng chứng.

Library không nên export mọi file đang có.

Mình tạo package `@coding-for-life/nest-common` trong workspace.

Package mới có ba vùng: filters, pipes và pagination. File `index.ts` là cửa chính của package.

Consumer chỉ import những symbol được hỗ trợ từ cửa này.

Không import đường dẫn nội bộ như `src/filters/private-helper`.

Public API nhỏ giúp phiên bản sau dễ thay đổi hơn.

Package dùng decorator và exception của NestJS.

NestJS nên là peer dependency để consumer dùng cùng một runtime.

Library không được import module User, Task hoặc AccessControl.

TaskFlow và một Nest app sạch cùng phụ thuộc `@coding-for-life/nest-common`.

Mũi tên chỉ đi từ ứng dụng tới library.

Nếu library phải import TaskFlow, ranh giới đã bị đảo ngược.

Mình chuyển pagination helper trước vì nó ít dependency nhất.

Sau đó, mình export validation pipe và exception filter.

TaskFlow đổi import sang package mới rồi chạy toàn bộ test.

Tiếp theo, mình tạo một Nest app sạch làm consumer thứ hai.

App này đăng ký pipe và filter mà không biết TaskFlow tồn tại.

Hai consumer build được mới chứng minh library thật sự portable.

Một file nằm trong package chưa đủ để gọi là reusable.

Đổi message nội bộ có thể là patch.

Thêm export tương thích ngược thường là minor.

Xóa symbol public hoặc đổi response contract là breaking change.

Khi đó, package cần major version và migration note.

Version không chỉ dành cho package public trên npm.

Private package cũng cần cách thông báo thay đổi cho các team.

Không chỉnh package âm thầm rồi hy vọng mọi repo vẫn build.

TaskFlow và app sạch cùng dùng một validation pipe.

Fix một lỗi trong library, nâng version và cập nhật hai consumer.

PermissionGuard vẫn nằm trong AccessControlModule.

CurrentUser vẫn nằm trong AuthModule vì nó dựa vào contract của ứng dụng.

Chúng ta tái sử dụng cross-cutting mechanics, không phát tán business policy.

Nhưng TaskFlow giờ đã có middleware, guard, pipe, interceptor và filter.

Một request trả lỗi trước controller. Breakpoint trong handler không bao giờ dừng.

Tập sau, ta theo dấu một request qua toàn bộ lifecycle để biết chính xác nó dừng ở lớp nào.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Hai bản `common/` đã lệch nhau | 45s |
| 2 | [AI] | Audit dependency từng file | 75s |
| 3 | [TABLE] | Portable, domain-specific và chưa chắc chắn | 60s |
| 4 | [IDE] | Tạo package và public `index.ts` | 85s |
| 5 | [DIAGRAM] | Hai consumer phụ thuộc một chiều vào library | 55s |
| 6 | [IDE] | Chuyển helper, pipe và filter | 90s |
| 7 | [TERMINAL] | Build TaskFlow và Nest app sạch | 85s |
| 8 | [DIAGRAM] | Patch, minor, major và migration note | 65s |
| 9 | [IDE] | Giữ PermissionGuard ngoài package | 55s |
| 10 | [B-ROLL] | Một request chạy qua middleware, guard, pipe, interceptor và filter | 30s |

**Tổng: 645 giây ≈ 10:45.** Dành thêm ba phút giải thích package boundary; font tối thiểu 18px.

### Code cốt lõi

```ts
// packages/nest-common/src/index.ts
export * from './filters/http-exception.filter';
export * from './pipes/app-validation.pipe';
export * from './pagination/page';
```

```json
{
  "name": "@coding-for-life/nest-common",
  "version": "1.0.0",
  "peerDependencies": {
    "@nestjs/common": "^12.0.0"
  }
}
```

### Prompt cho AI

```text
Audit src/common for extraction into a reusable NestJS package.
For every file, list framework, config, database and domain dependencies.
Exclude Auth and AccessControl policies.
Design the smallest supported public API through src/index.ts.
Use peer dependencies for the Nest runtime.
Migrate one file at a time and run both consumers.
Produce a semantic-versioning and migration-note proposal before editing.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic glowing code package feeding two separate NestJS applications, dark studio, clean one-way arrows, neon green accents, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic pile of duplicated common folders transforming into one versioned package, dark IDE background, cyan holographic boxes, 16:9, photorealistic, no text.`
3. `A cinematic developer separating portable tools from locked business policy modules, dark server room, green and amber lighting, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Tách common thành thư viện dùng cho nhiều dự án — EP14 | Lập trình là cuộc sống
2. Biến common thành package dùng lại trong NestJS — EP14 | Lập trình là cuộc sống
3. Code nào nên giữ trong common? — EP14 | Lập trình là cuộc sống
4. Tạo public API và version cho thư viện NestJS — EP14 | Lập trình là cuộc sống
5. Dùng chung pipe, filter và pagination giữa nhiều dự án — EP14 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 3 cho nguyên tắc thiết kế.

### 4b. SEO Description

```text
Copy folder common sang nhiều repo rất nhanh. Sau đó, mỗi bản copy trở thành một nguồn sự thật khác nhau.

✅ Audit dependency trước khi extract
✅ Tách portable code khỏi business policy
✅ Thiết kế public API nhỏ
✅ Dùng peer dependency cho NestJS
✅ Kiểm chứng bằng hai consumer thật
✅ Áp dụng semantic versioning và migration note

⏱ 0:00 Copy nhanh, trả giá chậm
⏱ 1:20 Audit common
⏱ 3:10 Public API của package
⏱ 5:00 Dependency một chiều
⏱ 6:45 Di chuyển từng phần
⏱ 8:50 Version và breaking change
⏱ 10:30 Hai consumer cùng chạy

#NestJS #Monorepo #Library #CleanArchitecture #TypeScript #SemanticVersioning #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs common library, reusable nestjs package, nestjs monorepo, shared library typescript, peer dependencies nestjs, semantic versioning, public api package, dependency direction, clean architecture nestjs, nestjs tiếng việt, nestjs tập 14, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `ĐỪNG COPY` — RED `#FF3B30`
- `FOLDER COMMON` — WHITE
### Option 2
- `1 LIBRARY` — NEON GREEN `#00FF41`
- `NHIỀU DỰ ÁN` — WHITE
### Option 3
- `COMMON ≠ REUSABLE` — WHITE
- `NẾU CÒN IMPORT DOMAIN` — NEON GREEN `#00FF41`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
