# NestJS #09 — PermissionGuard và Ownership: quyền chưa đủ

- **Series:** Học NestJS bằng AI — tập 9/29
- **Recording status:** READY
- **Target runtime:** 9–10 phút (~700 từ thoại + khoảng nghỉ demo)
- **Outcome:** PermissionGuard bảo vệ hành động; TasksService và repository giới hạn đúng resource theo owner.
- **Pain mở EP10:** Auth, permission và ownership có quá nhiều nhánh để tiếp tục thử tay.

---

## PART 1 — SCRIPT

Database nói Richard không có `permissions.manage`. Request vẫn xóa permission thành công vì controller chưa hề hỏi.

Authentication chỉ xác nhận danh tính. Authorization mới quyết định danh tính đó được làm gì.

Gắn `@Roles('admin')` lên mọi route có vẻ nhanh. Nhưng đổi tổ chức là phải sửa code rồi deploy lại.

Bước ngoặt là để controller yêu cầu hành động, còn role chỉ là cách cấp hành động đó.

`@RequirePermissions('permissions.manage')` giống biển yêu cầu vé trước cửa. Guard là người kiểm tra chiếc vé.

Decorator dùng metadata, không tự chạy logic. PermissionGuard dùng Reflector đọc metadata từ handler và controller.

Global AuthGuard từ EP05 chạy trước để gắn `request.user`. Chỉ route có `@Public()` mới bỏ qua xác thực. PermissionGuard dùng user ID đó truy vấn effective permissions.

JWT vẫn chỉ giữ `sub`. Nếu nhét toàn bộ quyền vào token, một quyền vừa revoke vẫn sống tới lúc token hết hạn.

Mình yêu cầu AI viết decision table trước. Không token là 401; token hợp lệ nhưng thiếu quyền là 403.

AI trả `false` cho cả hai trường hợp. Mình sửa plan để mỗi lớp chịu đúng lỗi của mình.

PermissionGuard lấy danh sách requirement bằng `getAllAndOverride`. Metadata ở method có thể ghi đè metadata controller.

Project chốt semantics mặc định là cần tất cả permission được khai báo. Tên `RequirePermissions` phải có ý nghĩa ổn định.

Nếu một route cần logic OR, ta tạo policy rõ ràng sau. Không lén đổi `every` thành `some` ở giữa dự án.

Guard gọi AccessControlService, không query Prisma trực tiếp. Cách tính DENY vẫn chỉ có một nguồn sự thật.

PermissionGuard nằm trong `modules/access-control/guards`. Nó phụ thuộc policy domain nên không thuộc `common`.

Đến phần tự gõ, mình thêm lỗi bốn-không-ba với message chung. Server log user ID và permission bị thiếu.

Response không liệt kê policy nội bộ cho client.

Mình protect endpoint tạo Permission. User member đăng nhập đúng vẫn nhận 403.

Gán `permissions.manage` qua role, request thành công. Revoke quyền, dùng lại access token cũ và request bị chặn ngay.

Đây là payoff của việc không nhét permission vào JWT.

Revoke role của user admin. Cùng token đó lập tức nhận 403 vì effective permission đã thay đổi.

Route không có permission metadata vẫn phải đi qua global AuthGuard. Chỉ `@Public()` mới thực sự public; route quản trị bắt buộc đi qua cả AuthGuard và PermissionGuard.

Đăng nhập không phải tấm vé VIP. Nó chỉ giúp hệ thống biết tên người đang đứng trước cửa.

Nhưng permission trên route vẫn chưa đủ. User A có `tasks.update` và vừa sửa được task của User B.

Permission trả lời hành động nào được phép. Ownership trả lời hành động đó áp dụng trên dữ liệu của ai.

Mình dùng Agent Skill để scaffold TasksModule. Controller mỏng, service giữ policy, repository tách khỏi Prisma.

AI đưa `ownerId` vào CreateTaskDto. Mình từ chối trước khi approve.

Client không được tự khai mình là chủ sở hữu. `ownerId` phải lấy từ access token.

Controller khai báo `tasks.update`. Guard kiểm tra hành động. Service kiểm tra resource cụ thể.

Bản đầu tìm task theo ID rồi update ngay. Task tồn tại, nhưng code không kiểm tra owner.

Mình sửa repository để tìm bằng cả `id` và `ownerId`.

Không có kết quả thì service trả bốn-không-bốn. Client không biết task vắng mặt hay nằm ngoài scope.

Danh sách task cũng luôn nhận `ownerId`. Ownership không chỉ áp dụng cho update và delete.

Admin muốn đọc mọi task phải có permission riêng như `tasks.read.any`. Không mở cửa bằng tên role bí mật.

Mình chạy lại bằng hai tài khoản. User A sửa task của mình thành công.

Sửa task của User B nhận bốn-không-bốn. Thiếu `tasks.update` nhận bốn-không-ba ngay tại guard.

Một status nói thiếu hành động. Status còn lại bảo vệ sự tồn tại của resource.

Nhưng ma trận này đã quá lớn để bấm Postman bằng trí nhớ.

Tập sau, Vitest và Supertest sẽ giữ auth, permission và ownership không trượt khỏi nhau.

Security không thể dựa vào trí nhớ của người test tay. Link Git của nhánh này nằm trong description. Bạn có thể comment phần còn khó hiểu.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | User thiếu quyền vẫn gọi route; dựng tension 401/403 | 30s |
| 2 | [DIAGRAM] | AuthGuard → PermissionGuard → Controller → Service ownership | 40s |
| 3 | [IDE] | Submit yêu cầu; AI plan decorator/guard, tua nhanh khi xử lý | 45s |
| 4 | [IDE] | Review bỏ `@Roles('admin')`; approve permission metadata | 45s |
| 5 | [IDE] | Reflector và AccessControlService, không gọi Prisma trực tiếp | 45s |
| 6 | [BROWSER] | Member 403; assign/revoke có hiệu lực với token cũ | 45s |
| 7 | [IDE] | Skill plan TasksModule; bắt lỗi `ownerId` trong DTO | 45s |
| 8 | [IDE] | Controller mỏng, service policy, repository contract | 45s |
| 9 | [BROWSER] | User A sửa task B thành công để lộ ownership bug | 35s |
| 10 | [IDE] | Sửa query bằng `id + ownerId`; giải thích 404 chống lộ resource | 50s |
| 11 | [IDE] | `findAllByOwner`; không dùng role name bí mật | 35s |
| 12 | [TERM]+[BROWSER] | Test 403, 404 và success bằng hai tài khoản | 50s |
| 13 | [B-ROLL] | Ma trận quá lớn để test tay; teaser Vitest/Supertest | 20s |

**Tổng: 530 giây ≈ 8:50; cộng khoảng nghỉ diff thành 9–10 phút.** Font 18px, che token và dữ liệu người dùng.

### Code cốt lõi

```typescript
export const PERMISSIONS_KEY = 'required_permissions';
export const RequirePermissions = (...codes: string[]) =>
  SetMetadata(PERMISSIONS_KEY, codes);
```

```typescript
const required = this.reflector.getAllAndOverride<string[]>(PERMISSIONS_KEY, [
  context.getHandler(),
  context.getClass(),
]);
if (!required?.length) return true;

const { user } = context.switchToHttp().getRequest<RequestWithUser>();
const effective = await this.accessControl.getEffectivePermissionCodes(user.id);
const missing = required.filter((code) => !effective.has(code));
if (missing.length) throw new ForbiddenException('Bạn không có quyền thực hiện thao tác này');
return true;
```

### Prompt cho Opus

```text
Plan claims-based authorization for the current AccessControlModule.
- Add @RequirePermissions metadata and PermissionGuard.
- Global AuthGuard must establish request.user first; only explicit @Public routes bypass it.
- PermissionGuard calls AccessControlService, never Prisma directly.
- Required permissions use AND semantics.
- No token returns 401; insufficient permission returns 403.
- Return a generic 403 message to clients; log missing permission codes only on the server.
- JWT remains identity-only so revocation applies immediately.
- Keep domain-specific guard and decorator inside access-control, not common.
- Produce a decision table and wait for approval.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of an authenticated developer stopped at a second glowing permission gate, green identity badge but red forbidden barrier, dark IDE code, cyan rim light, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A cinematic close-up of an old JWT remaining unchanged while a revoked permission disappears instantly from a live database panel, neon green and red contrast, code reflected in glasses, 16:9, photorealistic, no text.`
3. `A cinematic API doorway guarded by two layers, identity and permission, in a dark server room with neon syntax and city bokeh, developer silhouette right, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Có Permission vẫn sửa nhầm dữ liệu người khác — EP09 | Lập trình là cuộc sống
2. PermissionGuard chưa đủ nếu thiếu Ownership — EP09 | Lập trình là cuộc sống
3. 403 hay 404? Một quyết định bảo mật — EP09 | Lập trình là cuộc sống
4. Đừng cho client tự gửi `ownerId` — EP09 | Lập trình là cuộc sống
5. Authentication và Authorization khác nhau thế nào? — EP09 | Lập trình là cuộc sống
6. Vì sao không nên lưu permission trong JWT? — EP09 | Lập trình là cuộc sống
7. NestJS Guard bảo vệ hành động, Service bảo vệ dữ liệu — EP09 | Lập trình là cuộc sống
8. Một DTO suýt tạo lỗ hổng Ownership — EP09 | Lập trình là cuộc sống
9. User A sửa Task của User B như thế nào? — EP09 | Lập trình là cuộc sống
10. Authorization phải đi tới từng Resource — EP09 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1; A/B với Title 2 cho search intent.

### 4b. SEO Description

```text
Đăng nhập thành công chỉ chứng minh bạn là ai. PermissionGuard mới quyết định bạn được phép đi qua route nào.

✅ Phân biệt authentication và authorization
✅ Tạo @RequirePermissions bằng metadata
✅ Đọc metadata với Reflector
✅ Xếp AuthGuard trước PermissionGuard
✅ Trả 401 và 403 đúng nghĩa
✅ Không query Prisma trong guard
✅ Revoke quyền có hiệu lực với token cũ

🔗 NestJS Authorization: https://docs.nestjs.com/security/authorization

⏱ 0:00 Có token vẫn chưa đủ
⏱ 1:10 Role hay Permission?
⏱ 2:40 Decorator và metadata
⏱ 4:10 Hai guard, hai nhiệm vụ
⏱ 5:45 Review decision table
⏱ 7:00 Test assign, revoke và DENY
⏱ 8:35 Permission chưa giải quyết ownership

#NestJS #PermissionGuard #Authorization #RBAC #JWT #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs permission guard, require permissions nestjs, nestjs authorization, 401 vs 403, claims based authorization, rbac guard nestjs, reflector nestjs, permission metadata, jwt permissions, revoke permission, access control nestjs, nestjs tiếng việt, học nestjs, nestjs tập 9, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `ĐÃ LOGIN` — WHITE
- `VẪN 403` — NEON GREEN `#00FF41`
### Option 2
- `ĐỪNG NHÉT QUYỀN` — WHITE
- `VÀO JWT` — NEON GREEN `#00FF41`
### Option 3
- `401 ≠ 403` — NEON GREEN `#00FF41`
- `KHÁC GÌ NHAU?` — WHITE

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px. Typeset trong Canva; lưu nền không chữ.
