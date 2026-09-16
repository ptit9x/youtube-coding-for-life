# NestJS #10 — PermissionGuard: Phân biệt lỗi 401 và 403

- **Series:** Học NestJS bằng AI — tập 10/45
- **Target runtime:** ~9–10 phút
- **Outcome:** `@RequirePermissions`, PermissionGuard và response 401/403 đúng nghĩa.
- **Pain mở EP11:** Cần một business feature thật để kiểm chứng permission và ownership.

---

## PART 1 — SCRIPT

Database nói Richard không có `permissions.manage`. Request vẫn xóa permission thành công vì controller chưa hề hỏi.

Authentication chỉ xác nhận danh tính. Authorization mới quyết định danh tính đó được làm gì.

Gắn `@Roles('admin')` lên mọi route có vẻ nhanh. Nhưng đổi tổ chức là phải sửa code rồi deploy lại.

Bước ngoặt là để controller yêu cầu hành động, còn role chỉ là cách cấp hành động đó.

`@RequirePermissions('permissions.manage')` giống biển yêu cầu vé trước cửa. Guard là người kiểm tra chiếc vé.

Decorator dùng metadata, không tự chạy logic. PermissionGuard dùng Reflector đọc metadata từ handler và controller.

AuthGuard phải chạy trước để gắn `request.user`. PermissionGuard dùng user ID đó truy vấn effective permissions.

JWT vẫn chỉ giữ `sub`. Nếu nhét toàn bộ quyền vào token, một quyền vừa revoke vẫn sống tới lúc token hết hạn.

Mình yêu cầu AI viết decision table trước. Không token là 401; token hợp lệ nhưng thiếu quyền là 403.

AI trả `false` cho cả hai trường hợp. Mình sửa plan để mỗi lớp chịu đúng lỗi của mình.

PermissionGuard lấy danh sách requirement bằng `getAllAndOverride`. Metadata ở method có thể ghi đè metadata controller.

Project chốt semantics mặc định là cần tất cả permission được khai báo. Tên `RequirePermissions` phải có ý nghĩa ổn định.

Nếu một route cần logic OR, ta tạo policy rõ ràng sau. Không lén đổi `every` thành `some` ở giữa dự án.

Guard gọi AccessControlService, không query Prisma trực tiếp. Cách tính DENY vẫn chỉ có một nguồn sự thật.

PermissionGuard nằm trong `modules/access-control/guards`. Nó phụ thuộc policy domain nên không thuộc `common`.

Đến phần tự gõ, mình thêm lỗi 403 có message và permission bị thiếu. Server log user ID, nhưng không lộ dữ liệu thừa.

Mình protect endpoint tạo Permission. User member đăng nhập đúng vẫn nhận 403.

Gán `permissions.manage` qua role, request thành công. Revoke quyền, dùng lại access token cũ và request bị chặn ngay.

Đây là payoff của việc không nhét permission vào JWT.

Direct DENY được thêm cho user admin. Cùng token đó lập tức nhận 403 vì effective permission đã thay đổi.

Một route public không có metadata vẫn đi qua theo policy đã chốt. Route protected bắt buộc đi qua cả hai guard.

Đăng nhập không phải tấm vé VIP. Nó chỉ giúp hệ thống biết tên người đang đứng trước cửa.

Tập sau, ta tạo TasksModule. Khi đó permission trên route vẫn chưa đủ vì user có thể sửa task của người khác.

Theo dõi series để thấy authorization đi từ route xuống đúng resource, không dừng ở một decorator đẹp mắt. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | User thiếu quyền vẫn xóa Permission | 30s |
| 2 | [DIAGRAM] | Authentication: ai; Authorization: được làm gì | 45s |
| 3 | [IDE] | `@Roles('admin')` rải rác rồi thay bằng permission | 50s |
| 4 | [IDE] | Decorator metadata và Reflector | 55s |
| 5 | [DIAGRAM] | AuthGuard → PermissionGuard → Controller | 45s |
| 6 | [IDE] | AI decision table; sửa 401 và 403 | 55s |
| 7 | [IDE] | Guard gọi AccessControlService, không gọi Prisma | 60s |
| 8 | [IDE] | Host tự gõ missing-permission error | 45s |
| 9 | [BROWSER] | Member 403, assign role rồi 201 | 65s |
| 10 | [BROWSER] | Revoke và direct DENY có hiệu lực với token cũ | 70s |
| 11 | [B-ROLL] | Cửa API có hai lớp bảo vệ, teaser Tasks | 20s |

**Tổng: 545 giây ≈ 9:05.** Font 18px, zoom decorator và guard; che token trong Postman.

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
- AuthGuard must establish request.user first.
- PermissionGuard calls AccessControlService, never Prisma directly.
- Required permissions use AND semantics.
- No token returns 401; insufficient permission returns 403.
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

1. PermissionGuard NestJS: Phân biệt lỗi 401 và 403 — EP10 | Lập trình là cuộc sống
2. Tạo decorator RequirePermissions trong NestJS — EP10 | Lập trình là cuộc sống
3. Kiểm tra quyền truy cập API bằng PermissionGuard — EP10 | Lập trình là cuộc sống
4. Authentication và Authorization khác nhau thế nào? — EP10 | Lập trình là cuộc sống
5. Vì sao không nên lưu permission trong JWT? — EP10 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 3 cho search và Title 4 cho người mới.

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
nestjs permission guard, require permissions nestjs, nestjs authorization, 401 vs 403, claims based authorization, rbac guard nestjs, reflector nestjs, permission metadata, jwt permissions, revoke permission, access control nestjs, nestjs tiếng việt, học nestjs, nestjs tập 10, typescript backend, lập trình là cuộc sống
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
