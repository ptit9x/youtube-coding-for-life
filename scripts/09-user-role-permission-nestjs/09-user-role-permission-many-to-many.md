# NestJS #09 — Quan hệ User, Role và Permission với Prisma 8

- **Series:** Học NestJS bằng AI — tập 9/45
- **Target runtime:** 8–10 phút (650–800 từ thoại)
- **Outcome:** Prisma 8 explicit junction models, seed và assignment service chạy trong transaction; chưa expose API quản trị trước PermissionGuard.
- **Pain mở EP10:** Database đã có chính sách, nhưng route chưa thực thi permission.

---

## PART 1 — SCRIPT

Richard có role admin, nhưng database hiện chưa biểu diễn được admin gồm những permission nào.

User, Role và Permission phải được nối bằng những quan hệ chứa đủ ý nghĩa business.

Bước ngoặt là coi join table như entity thật. Nó không chỉ nối hai ID; nó ghi lại quyền được cấp thế nào.

Mô hình chuẩn có `UserRole` và `RolePermission`. Permission của user được suy ra qua những role đang sở hữu.

TaskFlow bắt đầu với RBAC chuẩn: permission của user được suy ra qua Role. `UserPermission` trực tiếp chưa được thêm chỉ để sơ đồ trông cân đối. Nếu sau này nghiệp vụ thật cần ngoại lệ, model đó phải có `ALLOW` hoặc `DENY` và precedence được chốt trước khi migrate.

Mỗi join model dùng composite primary key. Cùng một cặp ID không thể được gán hai lần.

`assignedAt` và `assignedById` giúp audit. Đây là lý do implicit many-to-many không còn phù hợp.

Mình yêu cầu AI thiết kế contract Prisma 8 và chỉ ra giới hạn relation hiện tại trước khi migrate. AI đề xuất nested write như các tutorial Prisma cũ. Mình dừng lại, đối chiếu tài liệu Prisma 8 rồi chuyển sang explicit junction write.

Service assignment nằm trong AccessControl, không nằm trong UsersService. Users không nên sở hữu policy phân quyền.

Assignment service gán và gỡ role phải kiểm tra cả user lẫn role tồn tại. Duplicate assignment được map thành conflict, không rơi xuống lỗi 500.

RolePermission cũng có attach và detach. Use case `setPermissions` dùng `db.transaction(async tx => ...)` để thay cả tập quyền nguyên tử. Mọi query bên trong callback đi qua `tx.orm`; không trộn query từ facade bên ngoài transaction.

Đến phần tự gõ, mình viết hàm tính effective permission bằng `Set`. Permission trùng qua hai role chỉ xuất hiện một lần.

Nếu dự án bật direct override ở tương lai, công thức phải được test rõ: quyền qua role cộng direct ALLOW rồi trừ direct DENY. Nhưng tập này không thêm model chưa có nhu cầu.

Mình chạy contract emit, lập migration, đọc DDL và kiểm tra composite keys. Tiếp theo, seed role `admin`, `member` cùng permission mẫu.

Integration test gán hai role cho một user. Query Prisma 8 dùng `.include(...)` để đọc relation, còn metadata của assignment được đọc trực tiếp từ collection junction. Danh sách permission hiệu lực đã loại trùng.

Test `setPermissions` cố tình lỗi ở giữa transaction. Toàn bộ thay đổi rollback. Gán lại cùng role nhận conflict thay vì tạo record rác.

Database bây giờ kể được toàn bộ chính sách. Nhưng controller vẫn chưa đọc câu chuyện đó. Tập này không mở endpoint assign/revoke ra HTTP; route quản trị chỉ xuất hiện sau khi PermissionGuard có thể bảo vệ nó.

Tập sau, `@RequirePermissions` và PermissionGuard sẽ biến dữ liệu thành quyết định 403.

Quan hệ chỉ nên là implicit khi nó thực sự chỉ là quan hệ. Có metadata và rule, nó đã trở thành domain concept.

Theo dõi series để xem permission rời database và đứng ngay trước cửa controller. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [DIAGRAM] | Ba bảng rời, rồi nối bằng hai junction models | 40s |
| 2 | [DIAGRAM] | RBAC chuẩn và nhánh direct override chỉ khi có nhu cầu | 40s |
| 3 | [IDE] | Prisma 8 contract: UserRole và RolePermission | 60s |
| 4 | [IDE] | AI đề xuất nested write cũ; host đối chiếu relation limitations | 50s |
| 5 | [DIAGRAM] | Luồng explicit junction write | 35s |
| 6 | [IDE] | AssignmentService và transaction `setPermissions` | 75s |
| 7 | [IDE] | Host tự gõ effective permission bằng Set | 65s |
| 8 | [TERM] | Contract emit, migration, composite keys và seed | 55s |
| 9 | [IDE]+[TERM] | Integration test assign/revoke qua junction collection | 55s |
| 10 | [IDE]+[TERM] | Duplicate conflict và transaction rollback | 55s |
| 11 | [B-ROLL] | Permission đi tới cánh cửa controller | 25s |

**Tổng mục tiêu: 8–10 phút.** Giữ sơ đồ tối, ba màu nhất quán cho User, Role và Permission.

### Schema rút gọn

```prisma
model UserRole {
  userId Uuid
  roleId Uuid
  assignedAt DateTime @default(now())
  assignedById Uuid?
  user User @relation(fields: [userId], references: [id], onDelete: Cascade)
  role Role @relation(fields: [roleId], references: [id], onDelete: Cascade)
  @@id([userId, roleId])
}

model RolePermission {
  roleId Uuid
  permissionId Uuid
  role Role @relation(fields: [roleId], references: [id], onDelete: Cascade)
  permission Permission @relation(fields: [permissionId], references: [id], onDelete: Cascade)
  @@id([roleId, permissionId])
}

```

Nếu có requirement direct override ở tập sau, mới bổ sung `UserPermission` với `effect: ALLOW | DENY` và test precedence.

### Transaction Prisma 8 cốt lõi

```typescript
await db.transaction(async (tx) => {
  await tx.orm.public.RolePermission
    .where({ roleId })
    .deleteAll();

  await tx.orm.public.RolePermission.createAll(
    permissionIds.map((permissionId) => ({ roleId, permissionId })),
  );
});
```

Tên method chính xác phải được đối chiếu với facade type đã emit ở phiên bản Prisma 8 được pin trước khi quay.

### Prompt cho Opus

```text
Plan explicit many-to-many access-control relations.
- Add UserRole and RolePermission as explicit junction models.
- Do not add UserPermission unless a real direct-override requirement exists.
- Store assignedAt and assignedById where assignments need audit.
- Define precedence before writing queries.
- Add internal assign/revoke use cases and transactional setPermissions with db.transaction; query only through tx.orm inside the callback.
- Reject duplicate assignments with 409.
- Keep assignment business logic inside AccessControlModule.
- Do not create HTTP management endpoints before PermissionGuard exists.
- Use Prisma 8 contract emit, explicit junction collections, .include(...) and direct junction writes.
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

1. Quan hệ User, Role và Permission với Prisma 8 — EP09 | Lập trình là cuộc sống
2. Thiết kế RBAC nhiều-nhiều trong NestJS — EP09 | Lập trình là cuộc sống
3. Tạo UserRole và RolePermission bằng Prisma — EP09 | Lập trình là cuộc sống
4. Khi nào cần UserPermission trực tiếp? — EP09 | Lập trình là cuộc sống
5. Cách tính quyền ALLOW và DENY trong RBAC — EP09 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho khái niệm RBAC và Title 3 cho search Prisma.

### 4b. SEO Description

```text
User, Role và Permission đang là ba bảng rời. Tập này dùng Prisma 8 explicit junction models để biến quan hệ thành business entity có audit.

✅ UserRole và RolePermission explicit
✅ Composite primary key chống duplicate
✅ Audit assignedAt và assignedById
✅ Chỉ thêm direct ALLOW/DENY khi có requirement thật
✅ Assign, revoke và transaction set permissions bằng Prisma 8
✅ Seed admin/member cùng permission mẫu
✅ Tính effective permissions không trùng
✅ Chưa expose API quản trị trước PermissionGuard

🔗 Prisma Relations: https://www.prisma.io/docs/orm/prisma-schema/data-model/relations

⏱ 0:00 Ba bảng chưa nói chuyện
⏱ 1:20 Standard RBAC và direct override
⏱ 3:00 Explicit join models
⏱ 5:00 Explicit junction writes
⏱ 6:45 Assignment service
⏱ 8:35 Migration và seed
⏱ 10:00 Kiểm chứng effective permissions

#NestJS #RBAC #Prisma #ManyToMany #Authorization #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
user role permission nestjs, many to many prisma 8, explicit junction prisma 8, rbac database design, userrole rolepermission, prisma 8 transaction, effective permissions, composite key prisma, nestjs access control, permission assignment service, nestjs tiếng việt, học nestjs, nestjs tập 9, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `2 JUNCTION` — WHITE
- `ĐỪNG MƠ HỒ` — NEON GREEN `#00FF41`
### Option 2
- `PRISMA 8` — NEON GREEN `#00FF41`
- `TRANSACTION` — WHITE
### Option 3
- `JOIN TABLE` — WHITE
- `LÀ BUSINESS` — NEON GREEN `#00FF41`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px. Typeset trong Canva; lưu nền không chữ.
