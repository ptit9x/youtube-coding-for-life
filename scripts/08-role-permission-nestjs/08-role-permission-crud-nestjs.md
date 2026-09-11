# NestJS #08 — Role và Permission khác nhau thế nào?

- **Series:** Học NestJS bằng AI — tập 8/46
- **Target runtime:** ~13 phút
- **Outcome:** CRUD đầy đủ Role và Permission bằng service/repository explicit.
- **Pain mở EP09:** User, Role và Permission vẫn là các bảng rời, chưa có quan hệ N–N.

---

## PART 1 — SCRIPT

Hai user đều đăng nhập thành công. Một người là quản trị viên, người kia là thành viên, nhưng API chưa thấy khác biệt.

Ta cần Role và Permission. Cái bẫy xuất hiện ngay khi hai module cùng có create, find, update và delete.

Nhìn duplication, AI rất dễ tạo `CommonService<T>`. Số dòng giảm, nhưng ý nghĩa business cũng biến mất theo.

Bước ngoặt là chấp nhận code giống nhau cho tới khi biết chúng thay đổi vì cùng một lý do.

Role giống chức danh trong công ty. Permission là hành động cụ thể mà chức danh đó được phép làm.

`admin` và `member` là role. `users.read` hoặc `roles.assign` là permission.

Controller sau này nên yêu cầu hành động, không hỏi tên chức danh. Tổ chức đổi role vẫn không phải sửa route.

Mình dùng Agent Skill từ tập trước để scaffold `roles` và `permissions` trong `modules/access-control`.

Skill chỉ tạo khung. Nó không được tự quyết định rule tạo hoặc xóa dữ liệu.

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

Mình approve. Agent tạo controller mỏng, service rõ rule và adapter Prisma ở database layer.

Đến phần tự gõ, mình thêm `normalizeRoleName`. Nó trim, lowercase và thay khoảng trắng liên tiếp bằng dấu gạch ngang.

Mình không đưa function này vào common. Nó chỉ có một consumer và thể hiện policy đặt tên Role.

Tiếp theo, mình viết rule không xóa system permission. Đây là nơi CommonService bắt đầu lộ vấn đề.

Một method delete chung không biết tại sao `permissions.manage` cần được bảo vệ khác một role tự tạo.

Mình chạy migration `create_roles_permissions`, rồi mở SQL kiểm tra hai unique index.

Postman tạo role `Project Manager`, response trả name đã normalize. Tạo lại nhận 409.

Tạo permission `tasks.create` thành công. Update code của permission nhận 400 vì code là identity ổn định.

Xóa permission hệ thống nhận 409. Xóa permission thường thành công.

Hai API đều đủ CRUD, nhưng đường logic không còn giống nhau. Đó chính là lý do chúng cần service riêng.

Hiện tại User, Role và Permission vẫn đứng cạnh nhau như ba danh bạ chưa có số liên lạc.

Tập sau, ta nối chúng bằng explicit join table và giữ cả dữ liệu audit trên chính quan hệ.

Đừng abstract chỉ để AI gõ ít hơn. AI không ngại gõ; người maintain mới phải trả giá để hiểu. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Hai user login nhưng gọi API giống nhau | 30s |
| 2 | [DIAGRAM] | Role là chức danh; Permission là hành động | 45s |
| 3 | [IDE] | Dùng Agent Skill scaffold access-control folders | 55s |
| 4 | [IDE] | Model Role và Permission cạnh nhau | 55s |
| 5 | [DIAGRAM] | Permission naming: resource.action | 40s |
| 6 | [IDE] | Prompt AI lập bảng business rule | 55s |
| 7 | [IDE] | AI đề xuất BaseCrudService và hooks | 55s |
| 8 | [IDE] | Review hai service explicit | 70s |
| 9 | [IDE] | Review repository contracts theo domain | 55s |
| 10 | [IDE] | Host tự gõ normalize role và system delete rule | 65s |
| 11 | [TERM] | Migration, mở SQL, kiểm tra unique indexes | 55s |
| 12 | [BROWSER] | Role create/duplicate/update/delete | 60s |
| 13 | [BROWSER] | Permission create/immutable code/system delete | 65s |
| 14 | [B-ROLL]+[DIAGRAM] | Ba bảng rời, teaser join tables | 25s |

**Tổng: 730 giây ≈ 12:10.** Hiện hai service side-by-side; dùng IDE tối và font 18px.

### Schema cốt lõi

```prisma
model Role {
  id          String   @id @default(uuid())
  name        String   @unique
  description String?
  isSystem    Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

model Permission {
  id          String   @id @default(uuid())
  code        String   @unique
  description String?
  isSystem    Boolean  @default(false)
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
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

1. Role và Permission trong NestJS khác nhau thế nào? — EP08 | Lập trình là cuộc sống
2. Xây RolesModule và PermissionsModule trong NestJS — EP08 | Lập trình là cuộc sống
3. CRUD Role và Permission với Prisma — EP08 | Lập trình là cuộc sống
4. Vì sao không nên dùng BaseCrudService quá sớm? — EP08 | Lập trình là cuộc sống
5. Thiết kế mã quyền users.read và tasks.create — EP08 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 4 cho bài học kiến trúc.

### 4b. SEO Description

```text
Role và Permission đều có CRUD, nhưng create và delete không mang cùng business semantics. Tập này giữ code explicit để kiến trúc còn dễ hiểu.

✅ Tạo RolesModule và PermissionsModule
✅ Đặt permission code theo resource.action
✅ Unique role name và permission code
✅ Bảo vệ system role/permission
✅ Giữ controller mỏng và service explicit
✅ Không tạo CommonService hoặc BaseCrudService
✅ Dùng Agent Skill để scaffold, không quyết định business

🔗 NestJS Providers: https://docs.nestjs.com/providers
🔗 Prisma CRUD: https://www.prisma.io/docs/orm/prisma-client/queries/crud

⏱ 0:00 Hai user, một quyền
⏱ 1:10 Role và Permission
⏱ 2:30 Scaffold bằng Agent Skill
⏱ 4:10 Business rules khác nhau
⏱ 5:50 Cái bẫy BaseCrudService
⏱ 7:30 Service và repository explicit
⏱ 9:20 Migration và unique indexes
⏱ 10:30 Kiểm chứng CRUD
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
