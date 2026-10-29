# NestJS #08 — Role, Permission và quan hệ many-to-many

- **Series:** Học NestJS bằng AI — tập 8/29
- **Recording status:** READY
- **Target runtime:** 9–10 phút (~875 từ thoại + khoảng nghỉ review)
- **Outcome:** Hoàn thiện Role, Permission, UserRole và RolePermission cùng audit metadata; chưa expose API quản trị trước PermissionGuard.
- **Pain mở EP09:** Database đã biểu diễn quyền, nhưng route chưa thực thi chính sách đó.

---

## PART 1 — SCRIPT

Hai user đều đăng nhập thành công. Một người là quản trị viên, người kia là thành viên, nhưng API chưa thấy khác biệt.

Ta cần Role và Permission. Cái bẫy xuất hiện ngay khi hai module cùng có create, find, update và delete.

Nhìn duplication, AI rất dễ tạo `CommonService<T>`. Số dòng giảm, nhưng ý nghĩa business cũng biến mất theo.

Bước ngoặt là chấp nhận code giống nhau cho tới khi biết chúng thay đổi vì cùng một lý do.

Role giống chức danh trong công ty. Permission là hành động cụ thể mà chức danh đó được phép làm.

`admin` và `member` là role. `users.read` hoặc `roles.assign` là permission.

Controller sau này nên yêu cầu hành động, không hỏi chức danh. Tổ chức đổi role vẫn không phải sửa route.

Controller quản trị chưa xuất hiện. Nếu expose CRUD trước PermissionGuard, user đăng nhập nào cũng có thể sửa chính sách quyền.

Mình dùng Agent Skill từ tập trước để scaffold `roles` và `permissions` trong `modules/access-control`.

Skill chỉ tạo model, repository contract/adapter, service nội bộ và seed. Nó không tạo controller hay route quản trị. Nó cũng không được tự quyết định rule tạo hoặc xóa dữ liệu.

Schema Role có name duy nhất, description và cờ `isSystem`. Permission có code duy nhất, description và cờ tương tự.

Code permission dùng dạng resource dot action. Ví dụ `users.read`, `roles.assign` và `tasks.create`.

Chuỗi này dễ đọc, dễ seed và không khóa controller vào một enum role cố định.

Mình yêu cầu AI lập bảng business rule trước khi implement. Role và Permission phải được so sánh cạnh nhau.

Role name được normalize về lowercase. Role hệ thống không được xóa. Permission code không đổi sau khi tạo.

Permission hệ thống đang dùng cũng không nên bị xóa tùy tiện. Sau khi có relations, rule này còn chặt hơn.

AI vẫn đề xuất BaseCrudService với hook `beforeDelete`. Đây là tín hiệu abstraction đang bắt đầu tự viết framework.

Mình từ chối. RolesService và PermissionsService giữ method riêng, dù mỗi file dài hơn vài chục dòng.

Code explicit giúp người mới nhìn thấy rule ngay nơi nó sống. Không cần nhảy qua ba lớp generic để hiểu một lệnh delete.

Repository contract cũng không sao chép mọi option Prisma. Roles cần `findByName`; Permissions cần `findByCode`.

Adapter có thể giống nhau ở mechanics, nhưng contract vẫn nói bằng ngôn ngữ của từng domain.

Mình approve. Agent tạo service rõ rule và adapter Prisma 8 ở database layer.

Seed và test nội bộ gọi các use case. HTTP boundary chỉ xuất hiện sau khi PermissionGuard tồn tại.

Đến phần tự gõ, mình thêm `normalizeRoleName`. Nó trim, lowercase và thay khoảng trắng liên tiếp bằng dấu gạch ngang.

Mình không đưa function này vào common. Nó chỉ có một consumer và thể hiện policy đặt tên Role.

Tiếp theo, mình viết rule không xóa system permission. Đây là nơi CommonService bắt đầu lộ vấn đề.

Một method delete chung không biết tại sao `permissions.manage` cần được bảo vệ khác một role tự tạo.

Mình emit lại contract, lập migration `create_roles_permissions`, rồi mở DDL kiểm tra hai unique index.

Integration test tạo role `Project Manager`, kết quả trả name đã normalize. Tạo lại nhận conflict ở service.

Seed tạo permission `tasks.create` thành công. Test đổi code của permission bị từ chối vì code là identity ổn định.

Test xóa permission hệ thống nhận conflict. Permission thường có thể bị xóa khi chưa có quan hệ sử dụng.

Hai service có thao tác gần giống CRUD, nhưng logic không giống nhau. Đó là lý do chúng cần service riêng.

Giờ tới quan hệ. `UserRole` nối user với role. `RolePermission` nối role với permission.

Mình không dùng implicit many-to-many. Quan hệ này cần `assignedAt` và `assignedById` để audit.

Mỗi join model dùng composite primary key. Cùng một cặp ID không thể được gán hai lần.

AI đề xuất nested write theo tutorial Prisma cũ. Mình dừng lại và đối chiếu tài liệu Prisma 8.

Assignment service nằm trong AccessControl, không nằm trong UsersService. User không nên sở hữu policy phân quyền.

Service kiểm tra hai đầu quan hệ tồn tại. Duplicate assignment được map thành conflict, không rơi xuống lỗi năm-trăm.

Use case `setPermissions` chạy trong transaction. Mọi query bên trong callback đi qua `tx.orm`.

Mình dùng `Set` để tính effective permission. Một permission đi qua hai role vẫn chỉ xuất hiện một lần.

Contract emit và migration đều xanh. DDL có đủ composite key cùng foreign key đã review.

Test gán hai role cho một user. Query relation trả đúng audit metadata và danh sách permission đã loại trùng.

Test cố tình lỗi giữa `setPermissions`. Toàn bộ thay đổi rollback.

Database bây giờ kể được chính sách truy cập. Nhưng controller vẫn chưa đọc câu chuyện đó.

Tập này không mở route assign hoặc revoke. Route quản trị chỉ xuất hiện sau khi PermissionGuard bảo vệ được nó.

Tập sau, `@RequirePermissions` biến dữ liệu này thành quyết định bốn-không-ba.

Đừng abstract chỉ để AI gõ ít hơn. Quan hệ có metadata cũng không còn là đường nối vô danh. Link Git của nhánh này nằm trong description. Bạn có thể comment phần còn khó hiểu.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [DIAGRAM] | Hai user login nhưng chưa có policy; Role khác Permission | 35s |
| 2 | [IDE] | Submit yêu cầu; AI plan Roles/Permissions bằng Skill, tua nhanh khi xử lý | 45s |
| 3 | [IDE] | Review và loại BaseCrudService; approve service explicit | 50s |
| 4 | [IDE] | Model Role/Permission, naming resource.action và system rule | 50s |
| 5 | [IDE] | Host tự gõ normalize role và immutable permission code | 40s |
| 6 | [DIAGRAM] | UserRole và RolePermission là entity có audit metadata | 40s |
| 7 | [IDE] | Review explicit junction, composite key và assignment service | 50s |
| 8 | [IDE] | Review transaction `setPermissions` và `tx.orm` | 45s |
| 9 | [TERM] | Contract emit, migration plan và DDL composite keys | 50s |
| 10 | [TERM] | Seed admin/member; test duplicate assignment và rollback | 50s |
| 11 | [IDE] | Tính effective permission bằng Set, loại quyền trùng | 40s |
| 12 | [DIAGRAM] | Database có policy nhưng route chưa thực thi; teaser PermissionGuard | 25s |

**Tổng: 520 giây ≈ 8:40; cộng khoảng nghỉ review thành 9–10 phút.** One Dark Pro, JetBrains Mono tối thiểu 18px; ẩn minimap.

### Schema cốt lõi

```prisma
model Role {
  id          Uuid     @id @default(uuid())
  name        String   @unique
  description String?
  isSystem    Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   temporal.updatedAt()
}

model Permission {
  id          Uuid     @id @default(uuid())
  code        String   @unique
  description String?
  isSystem    Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   temporal.updatedAt()
}
```

### Business rule mẫu

```typescript
async remove(id: string): Promise<void> {
  const permission = await this.findOne(id);
  if (permission.isSystem) {
    throw new ConflictException('Không thể xóa permission hệ thống');
  }
  await this.permissionsRepository.remove(id);
}
```

### Prompt cho Opus

```text
Use the project Agent Skill to plan Roles and Permissions under modules/access-control.

Before implementation, compare their business rules in a table.
- Role name is unique and normalized.
- Permission code is unique and immutable.
- System records cannot be deleted.
- Controllers stay thin.
- Each feature has its own explicit service and repository contract.
- Do not create BaseCrudService, CommonService or generic business hooks.
- Do not add relations yet.
- Do not create controllers or expose Role/Permission administration over HTTP yet.
- Use the Prisma 8 contract, emitted artifacts, database facade and migration workflow.
- Wait for approval before editing.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese developer comparing two glowing code panels labeled only by abstract role and key symbols, identical CRUD shapes splitting into different business paths, neon green and cyan, dark room, subject right, empty left space, 16:9, photorealistic, no readable text, no logos.`
2. `A cinematic close-up of a tempting generic code box swallowing distinct role and permission rules, red warning glow against green syntax, code reflected in glasses, deep shadows, empty left side, 16:9, photorealistic, no text.`
3. `A cinematic developer desk with three separate glowing database entities waiting to be connected, role badge, user silhouette and permission key, cyan and purple rim light, city bokeh, subject right, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Role và Permission chưa đủ nếu thiếu quan hệ — EP08 | Lập trình là cuộc sống
2. Join Table không chỉ để nối hai ID — EP08 | Lập trình là cuộc sống
3. Thiết kế RBAC bằng Prisma 8 — EP08 | Lập trình là cuộc sống
4. Vì sao BaseCrudService phá business rule? — EP08 | Lập trình là cuộc sống
5. Một Composite Key chặn quyền bị gán hai lần — EP08 | Lập trình là cuộc sống
6. UserRole và RolePermission nên là Entity thật — EP08 | Lập trình là cuộc sống
7. Permission `users.read` hoạt động thế nào? — EP08 | Lập trình là cuộc sống
8. AI chọn sai Many-to-Many, tôi dừng migration — EP08 | Lập trình là cuộc sống
9. RBAC không bắt đầu từ decorator — EP08 | Lập trình là cuộc sống
10. Database kể được ai có quyền gì — EP08 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1; A/B với Title 2 cho hook join table.

### 4b. SEO Description

```text
Role và Permission có các thao tác gần giống CRUD, nhưng create và delete không mang cùng business semantics. Tập này giữ code explicit và chưa expose API quản trị trước PermissionGuard.

✅ Tạo RolesModule và PermissionsModule nội bộ
✅ Đặt permission code theo resource.action
✅ Unique role name và permission code
✅ Bảo vệ system role/permission
✅ Giữ controller mỏng và service explicit
✅ Không tạo CommonService hoặc BaseCrudService
✅ Dùng Agent Skill để scaffold, không quyết định business
✅ Chưa mở route quản trị trước khi có PermissionGuard

🔗 NestJS Providers: https://docs.nestjs.com/providers
🔗 Prisma CRUD: https://www.prisma.io/docs/orm/prisma-client/queries/crud

⏱ 0:00 Hai user, một quyền
⏱ 1:10 Role và Permission
⏱ 2:30 Scaffold bằng Agent Skill
⏱ 4:10 Business rules khác nhau
⏱ 5:50 Cái bẫy BaseCrudService
⏱ 7:30 Service và repository explicit
⏱ 9:20 Migration và unique indexes
⏱ 10:30 Kiểm chứng service và seed
⏱ 11:50 Chuẩn bị nối N–N

#NestJS #RBAC #RolePermission #CleanArchitecture #Prisma #TypeScript #Backend #AICoding #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs role permission, rbac nestjs, role crud nestjs, permission crud nestjs, commonservice trap, base crud service, nestjs architecture, prisma role permission, permission resource action, explicit service pattern, agent skill nestjs, nestjs tiếng việt, học nestjs, nestjs tập 8, backend fresher, typescript backend, ai coding mentor, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `CRUD GIỐNG NHAU` — WHITE
- `LOGIC KHÁC NHAU` — NEON GREEN `#00FF41`
- Hình: hai code panel tách thành hai hướng.

### Option 2
- `COMMON SERVICE` — WHITE
- `CÁI BẪY` — NEON GREEN `#00FF41`
- Hình: generic box nuốt business rules.

### Option 3
- `AI MUỐN GOM` — WHITE
- `TÔI NÓI KHÔNG` — NEON GREEN `#00FF41`
- Hình: developer chặn proposal BaseCrudService.

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái một phần ba, stroke 8px, glow 10px. Typeset trong Canva và giữ nền không chữ.
