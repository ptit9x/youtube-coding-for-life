# NestJS #09 — Quan hệ User, Role và Permission với Prisma

- **Series:** Học NestJS bằng AI — tập 9/46
- **Target runtime:** ~11 phút
- **Outcome:** Explicit join models, seed và API assign/revoke đầy đủ.
- **Pain mở EP10:** Database đã có chính sách, nhưng route chưa thực thi permission.

---

## PART 1 — SCRIPT

Richard nhận `permissions.manage` từ role admin. Một direct DENY lại cấm đúng quyền đó.

Nếu precedence mơ hồ, cùng một request có thể được phép hoặc bị chặn tùy cách code.

User, Role và Permission phải được nối bằng những quan hệ chứa đủ ý nghĩa business.

Bước ngoặt là coi join table như entity thật. Nó không chỉ nối hai ID; nó ghi lại quyền được cấp thế nào.

Mô hình chuẩn có `UserRole` và `RolePermission`. Permission của user được suy ra qua những role đang sở hữu.

TaskFlow còn cần ngoại lệ theo từng user. Vì vậy mình thêm `UserPermission` với `ALLOW` hoặc `DENY` rõ ràng.

Nếu dự án không cần ngoại lệ, hãy bỏ bảng này. Đừng tạo quan hệ thứ ba chỉ để sơ đồ trông cân đối.

Mỗi join model dùng composite primary key. Cùng một cặp ID không thể được gán hai lần.

`assignedAt` và `assignedById` giúp audit. Đây là lý do implicit many-to-many không còn phù hợp.

Mình yêu cầu AI thiết kế schema và bảng precedence trước khi migrate. Nó phải trả lời direct DENY thắng hay thua role.

AI ban đầu cộng mọi permission lại. Khi đó direct DENY tồn tại nhưng không có tác dụng.

Mình chốt công thức: quyền qua role, cộng direct ALLOW, rồi loại direct DENY. Deny trực tiếp có ưu tiên cuối.

Service assignment nằm trong AccessControl, không nằm trong UsersService. Users không nên sở hữu policy phân quyền.

API gán và gỡ role kiểm tra cả user lẫn role tồn tại. Duplicate assignment trả 409, không rơi xuống lỗi 500.

RolePermission cũng có attach và detach. Một endpoint `setPermissions` dùng transaction để thay cả tập quyền nguyên tử.

Đến phần tự gõ, mình viết hàm tính effective permission bằng `Set`. Permission trùng qua hai role chỉ xuất hiện một lần.

Sau đó direct ALLOW được thêm, direct DENY bị xóa. Thứ tự vài dòng này chính là business policy.

Mình chạy migration, đọc SQL và kiểm tra composite keys. Tiếp theo, seed role `admin`, `member` cùng permission mẫu.

Postman gán hai role cho một user. Endpoint effective permissions trả danh sách đã loại trùng.

Mình direct deny `tasks.delete`. Permission biến mất dù role admin đang cấp nó.

Gỡ deny, quyền trở lại. Gán lại cùng role nhận 409 thay vì tạo record rác.

Database bây giờ kể được toàn bộ chính sách. Nhưng controller vẫn chưa đọc câu chuyện đó.

Tập sau, `@RequirePermissions` và PermissionGuard sẽ biến dữ liệu thành quyết định 403.

Quan hệ chỉ nên là implicit khi nó thực sự chỉ là quan hệ. Có metadata và rule, nó đã trở thành domain concept.

Theo dõi series để xem permission rời database và đứng ngay trước cửa controller. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [DIAGRAM] | Ba bảng rời, rồi nối bằng ba join models | 45s |
| 2 | [DIAGRAM] | Standard RBAC và nhánh direct override | 55s |
| 3 | [IDE] | Schema UserRole, RolePermission, UserPermission | 75s |
| 4 | [IDE] | Prompt AI về precedence; bắt lỗi DENY vô dụng | 65s |
| 5 | [DIAGRAM] | Role grants + ALLOW − DENY | 45s |
| 6 | [IDE] | AssignmentService và transaction `setPermissions` | 75s |
| 7 | [IDE] | Host tự gõ effective permission bằng Set | 65s |
| 8 | [TERM] | Migration, SQL composite keys và seed | 65s |
| 9 | [BROWSER] | Assign/revoke role và permission | 75s |
| 10 | [BROWSER] | Duplicate 409; direct DENY thắng role | 70s |
| 11 | [B-ROLL] | Permission đi tới cánh cửa controller | 25s |

**Tổng: 660 giây ≈ 11 phút.** Giữ sơ đồ tối, ba màu nhất quán cho User, Role và Permission.

### Schema rút gọn

```prisma
enum PermissionEffect { ALLOW DENY }

model UserRole {
  userId String
  roleId String
  assignedAt DateTime @default(now())
  assignedById String?
  user User @relation(fields: [userId], references: [id], onDelete: Cascade)
  role Role @relation(fields: [roleId], references: [id], onDelete: Cascade)
  @@id([userId, roleId])
}

model RolePermission {
  roleId String
  permissionId String
  role Role @relation(fields: [roleId], references: [id], onDelete: Cascade)
  permission Permission @relation(fields: [permissionId], references: [id], onDelete: Cascade)
  @@id([roleId, permissionId])
}

model UserPermission {
  userId String
  permissionId String
  effect PermissionEffect
  user User @relation(fields: [userId], references: [id], onDelete: Cascade)
  permission Permission @relation(fields: [permissionId], references: [id], onDelete: Cascade)
  @@id([userId, permissionId])
}
```

### Prompt cho Opus

```text
Plan explicit many-to-many access-control relations.
- Add UserRole, RolePermission and UserPermission.
- UserPermission must have ALLOW or DENY semantics.
- Store assignedAt and assignedById where assignments need audit.
- Define precedence before writing queries.
- Add assign/revoke APIs and a transactional setPermissions use case.
- Reject duplicate assignments with 409.
- Keep assignment business logic inside AccessControlModule.
- Show migration SQL risks and wait for approval.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of three glowing entities represented by a user silhouette, role badge and permission key connected through explicit junction nodes, dark developer room, neon green cyan and purple, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A cinematic close-up of a red DENY token cutting through multiple green role permissions on a dark code screen, dramatic reflections on eyeglasses, deep shadows, empty left space, 16:9, photorealistic, no text.`
3. `A cinematic database diagram with explicit join tables glowing like bridges and audit timestamps floating subtly, late-night monitor light, developer on the right, city bokeh, 16:9, photorealistic, no readable text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Quan hệ User, Role và Permission với Prisma — EP09 | Lập trình là cuộc sống
2. Thiết kế RBAC nhiều-nhiều trong NestJS — EP09 | Lập trình là cuộc sống
3. Tạo UserRole và RolePermission bằng Prisma — EP09 | Lập trình là cuộc sống
4. Khi nào cần UserPermission trực tiếp? — EP09 | Lập trình là cuộc sống
5. Cách tính quyền ALLOW và DENY trong RBAC — EP09 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho khái niệm RBAC và Title 3 cho search Prisma.

### 4b. SEO Description

```text
Richard vừa có quyền từ role, vừa nhận direct DENY. Tập này chốt precedence và biến join table thành business entity có audit.

✅ UserRole, RolePermission và UserPermission
✅ Composite primary key chống duplicate
✅ Audit assignedAt và assignedById
✅ Direct ALLOW/DENY có precedence rõ
✅ Assign, revoke và transaction set permissions
✅ Seed admin/member cùng permission mẫu
✅ Tính effective permissions không trùng

🔗 Prisma Relations: https://www.prisma.io/docs/orm/prisma-schema/data-model/relations

⏱ 0:00 Ba bảng chưa nói chuyện
⏱ 1:20 Standard RBAC và direct override
⏱ 3:00 Explicit join models
⏱ 5:00 Precedence ALLOW/DENY
⏱ 6:45 Assignment service
⏱ 8:35 Migration và seed
⏱ 10:00 Kiểm chứng effective permissions

#NestJS #RBAC #Prisma #ManyToMany #Authorization #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
user role permission nestjs, many to many prisma, explicit join table prisma, rbac database design, userrole rolepermission, userpermission allow deny, effective permissions, composite key prisma, nestjs access control, permission assignment api, nestjs tiếng việt, học nestjs, nestjs tập 9, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `3 QUAN HỆ N–N` — WHITE
- `ĐỪNG MƠ HỒ` — NEON GREEN `#00FF41`
### Option 2
- `DIRECT DENY` — NEON GREEN `#00FF41`
- `THẮNG ROLE` — WHITE
### Option 3
- `JOIN TABLE` — WHITE
- `LÀ BUSINESS` — NEON GREEN `#00FF41`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px. Typeset trong Canva; lưu nền không chữ.
