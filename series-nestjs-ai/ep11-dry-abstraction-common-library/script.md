# NestJS #11 — DRY: Khi nào không nên dùng BaseCrudService

- **Series:** Học NestJS bằng AI — tập 11/29
- **Recording status:** READY
- **Target runtime:** 9–10 phút (~800 từ thoại + khoảng nghỉ review)
- **Outcome:** Tránh generic business service và tách phần cross-cutting ổn định thành library có public API, version cùng consumer test.
- **Pain mở EP12:** `common/` ổn định nhưng request đi qua quá nhiều layer, debug không còn trực quan.

---

## PART 1 — SCRIPT

AI giúp mình xóa gần sáu mươi dòng bằng `BaseCrudService`.

Ba business rule sau, mình xóa luôn abstraction đó.

Code dài hơn, nhưng đường đi của logic lại ngắn hơn.

UsersService, RolesService và PermissionsService đều có `create`, `findAll`, `findOne`, `update`, `remove`.

AI nhìn thấy những method giống nhau và đề nghị cho cả ba service kế thừa một base class.

Nhưng ít dòng hơn không đồng nghĩa thiết kế tốt hơn.

Mình sẽ dùng business rule thật để thử phá abstraction hấp dẫn đó.

Hai đoạn code giống hình dạng chưa chắc đại diện cùng một kiến thức.

Tạo user phải hash password và chuẩn hóa email.

Tạo role phải bảo vệ tên hệ thống và audit người tạo.

Tạo permission phải kiểm tra format `resource.action`.

Ba method cùng tên, nhưng thay đổi vì ba lý do khác nhau.

Đó là duplicate code, chưa phải duplicate knowledge.

Một abstraction tốt gom những thứ luôn thay đổi cùng nhau.

Mình cố tình đưa prompt nguy hiểm.

Prompt yêu cầu giảm tối đa code CRUD trùng lặp bằng inheritance và generic type.

AI tạo `BaseCrudService<TEntity, CreateDto, UpdateDto>`.

Nó còn thêm hook `beforeCreate`, `beforeUpdate` và `beforeDelete`.

Mỗi service override vài hook. Sau đó, hook lại nhận nhiều generic parameter.

Boilerplate biến mất ở service, nhưng complexity chuyển vào base class.

Người đọc phải nhảy qua nhiều file để hiểu một thao tác create.

Bộ test EP10 cho phép mình thử refactor an toàn.

Mình thêm ba rule mới.

System role không được xóa. System permission cũng không được đổi code.

User bị khóa vẫn có thể được xem, nhưng không thể tự cập nhật hồ sơ.

Base service bắt đầu cần thêm flag.

Constructor bắt đầu nhận cờ `canDelete`, danh sách `immutableFields` và lựa chọn `audit`.

Config đang biến business rule thành một ngôn ngữ lập trình nhỏ.

Đây là tín hiệu abstraction đã vượt quá giá trị của nó.

Mình xóa base service và trả logic về từng module.

RolesService nói rõ system role không được xóa.

PermissionsService nói rõ code bất biến sau khi được sử dụng.

UsersService nói rõ email và password được xử lý thế nào.

Code dài hơn một chút, nhưng mỗi rule nằm đúng nơi cần đọc.

Explicit không có nghĩa là copy thiếu suy nghĩ.

Nó nghĩa là ưu tiên semantic trước số dòng.

Persistence mechanics có thể ổn định hơn business logic.

Ví dụ, phân trang dùng `skip`, `take`, cursor và metadata giống nhau ở nhiều repository.

Một helper tạo pagination result có thể đáng dùng chung.

Validation pipe và exception filter cũng là cross-cutting boundary.

Chúng không biết User, Role, Permission hay Task là gì.

Đó là tiêu chí quan trọng cho `common/`.

Chỉ abstract sau khi có ít nhất hai consumer thật và test bảo vệ.

Sau refactor, toàn bộ test vẫn xanh.

Business service không kế thừa class tổng quát nào.

Repository vẫn có thể dùng helper nhỏ cho pagination và transaction mapping.

Dependency tiếp tục đi một chiều. Domain không import infrastructure.

DRY không phải xóa mọi dòng giống nhau.

DRY là tránh nhiều nguồn sự thật cho cùng một kiến thức.

Nhưng những helper ổn định trong `common/` đang được copy sang dự án khác. Mỗi bản copy bắt đầu sửa theo một hướng.

Phần thật sự portable cần một library có phiên bản và public API rõ ràng.

Mình yêu cầu AI lập bảng dependency. Pagination helper chỉ cần TypeScript.

Validation pipe và exception filter phụ thuộc NestJS. Permission decorator lại phụ thuộc AccessControl của User Management.

Tên folder `common` không tự biến code thành reusable. Dependency mới là bằng chứng.

Mình tạo package `@coding-for-life/nest-common` với filters, pipes và pagination.

File `index.ts` là cửa public duy nhất. Consumer không import đường dẫn nội bộ.

NestJS được khai báo peer dependency để app và library dùng cùng runtime.

Library không được import User, Task hoặc AccessControl. Mũi tên chỉ đi từ ứng dụng tới library.

Mình chuyển pagination trước, rồi validation pipe và exception filter.

User Management đổi import sang package mới và chạy toàn bộ test.

Tiếp theo, mình tạo một Nest app sạch làm consumer thứ hai.

Hai consumer build được mới chứng minh package thật sự portable.

Fix tương thích là patch. Thêm export là minor. Xóa public symbol là breaking change cần major version.

PermissionGuard vẫn ở AccessControl. CurrentUser vẫn ở Auth vì chúng mang policy của ứng dụng.

Ta tái sử dụng mechanics, không phát tán business rule.

Nhưng request giờ đi qua middleware, guard, pipe, interceptor và filter.

Tập sau, ta theo dấu toàn bộ lifecycle rồi đóng gói cùng ứng dụng bằng Docker.

Code dùng chung tốt không có nghĩa là code xuất hiện ở nhiều nơi. Nó có nghĩa là thay đổi vì cùng một lý do. Link Git của nhánh này nằm trong description. Bạn có thể comment phần còn khó hiểu.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Ba service có method cùng tên | 35s |
| 2 | [IDE] | Submit prompt giảm duplication; tua nhanh AI xử lý | 40s |
| 3 | [IDE] | Review BaseCrudService phình theo business rule | 55s |
| 4 | [DIAGRAM] | Duplicate code khác duplicate knowledge | 45s |
| 5 | [TERM] | Mutation business rule làm generic test thất bại | 45s |
| 6 | [IDE] | Trả policy về từng service; giữ helper persistence nhỏ | 45s |
| 7 | [IDE] | Audit dependency từng file trong `common/` | 45s |
| 8 | [DIAGRAM] | App → `nest-common`; library không import app | 40s |
| 9 | [IDE] | Public `index.ts`, peer dependency và ba vùng package | 45s |
| 10 | [TERM] | Build User Management và Nest app sạch | 50s |
| 11 | [DIAGRAM] | Semver patch/minor/major và migration note | 35s |
| 12 | [IDE] | PermissionGuard/CurrentUser ở lại domain module | 35s |
| 13 | [B-ROLL] | Lifecycle nhiều lớp, teaser tập kế | 20s |

**Tổng: 535 giây ≈ 8:55; cộng khoảng nghỉ review thành 9–10 phút.** One Dark Pro, font tối thiểu 18px.

### Code cốt lõi

```ts
async remove(id: number) {
  const role = await this.getById(id);
  if (role.isSystem) {
    throw new ConflictException('Không thể xóa system role');
  }
  return this.rolesRepository.remove(id);
}
```

```ts
export type Page<T> = {
  items: T[];
  total: number;
  page: number;
  pageSize: number;
};
```

### Prompt cho AI

```text
Audit duplication across Users, Roles and Permissions.
Classify each duplicate as business knowledge or persistence mechanics.
Try a generic BaseCrudService on a temporary diff.
Run the existing tests against three new business rules.
Prefer explicit services when rules change for different reasons.
Only extract helpers with at least two real consumers.
Do not create abstractions solely to reduce line count.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic developer trapped inside a giant tangled generic type declaration, dark IDE, glowing angle brackets, red warning light, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic clean business service facing a towering abstract base class with many hooks, neon green versus red lighting, dark code studio, 16:9, photorealistic, no text.`
3. `A cinematic pair of identical code blocks splitting into different business paths, dark background, glowing arrows and test shields, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. DRY quá tay biến code thành mê cung — EP11 | Lập trình là cuộc sống
2. BaseCrudService có thật sự giúp code tốt hơn? — EP11 | Lập trình là cuộc sống
3. Duplicate Code khác Duplicate Knowledge — EP11 | Lập trình là cuộc sống
4. Folder `common` không có nghĩa là dùng chung — EP11 | Lập trình là cuộc sống
5. Khi nào code nên trở thành Library? — EP11 | Lập trình là cuộc sống
6. Hai Consumer mới chứng minh code Reusable — EP11 | Lập trình là cuộc sống
7. Tách NestJS Common Library mà không kéo Business Rule — EP11 | Lập trình là cuộc sống
8. Một Public API nhỏ cứu cả Package — EP11 | Lập trình là cuộc sống
9. AI muốn xóa Duplication, tôi giữ lại — EP11 | Lập trình là cuộc sống
10. Reuse Mechanics, đừng phát tán Policy — EP11 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1; A/B với Title 4 cho góc nhìn `common`.

### 4b. SEO Description

```text
AI xóa gần sáu mươi dòng bằng BaseCrudService. Ba business rule sau, mình xóa abstraction đó dù code dài hơn.

✅ Phân biệt duplicate code và duplicate knowledge
✅ Thử BaseCrudService bằng test thật
✅ Nhận diện hook và config phình to
✅ Giữ business service explicit
✅ Chỉ abstract persistence mechanics ổn định
✅ Áp dụng YAGNI và dependency một chiều

⏱ 0:00 BaseCrudService rất hấp dẫn
⏱ 1:20 Duplicate knowledge là gì?
⏱ 3:00 Cho AI tối ưu cực đoan
⏱ 5:00 Dùng test phá abstraction
⏱ 7:30 Trả business rule về service
⏱ 9:30 Phần nào thật sự tái sử dụng?

#NestJS #DRY #Refactoring #CleanArchitecture #TypeScript #Backend #YAGNI #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs generic crud, base crud service nestjs, abstraction trap, dry principle, duplicate knowledge, yagni nestjs, refactor nestjs, clean architecture nestjs, repository pattern, typescript generics, nestjs tiếng việt, nestjs tập 11, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `GENERIC CRUD` — WHITE
- `LÀ CÁI BẪY?` — RED `#FF3B30`
### Option 2
- `ÍT CODE HƠN` — WHITE
- `KHÓ HIỂU HƠN` — NEON GREEN `#00FF41`
### Option 3
- `DRY ≠ GOM HẾT` — NEON GREEN `#00FF41`
- `VÀO BASE CLASS` — WHITE

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
