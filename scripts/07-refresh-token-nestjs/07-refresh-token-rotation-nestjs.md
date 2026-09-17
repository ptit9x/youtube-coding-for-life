# NestJS #07 — Refresh Token: Gia hạn đăng nhập và thu hồi phiên

- **Series:** Học NestJS bằng AI — tập 7/45
- **Target runtime:** 8–10 phút (650–800 từ thoại)
- **Outcome:** Tạo session, refresh rotation, reuse detection và logout có thu hồi.
- **Pain mở EP08:** Xác thực đã hoàn chỉnh nhưng mọi user vẫn có quyền như nhau.

---

## PART 1 — SCRIPT

Người dùng bấm logout. Access token cũ vẫn mở được API cho tới khi hết hạn.

Cho token sống lâu hơn thì tiện, nhưng token bị lộ cũng sống lâu hơn.

Đây không phải bài toán chọn tiện hoặc an toàn. Ta cần hai chiếc chìa khóa với hai nhiệm vụ khác nhau.

Access token sống ngắn và mở API. Refresh token sống dài, chỉ dùng để xin một access token mới.

Config boundary từ EP03 được mở rộng thêm `REFRESH_TOKEN_TTL_DAYS`. Refresh token là chuỗi ngẫu nhiên, nên không tạo thêm một JWT secret giả tạo.

Nhưng lưu refresh token nguyên văn trong database lại tạo thêm một password mới. Database lộ là session của user cũng lộ.

Bước ngoặt là dùng token ngẫu nhiên, chỉ lưu hash, rồi xoay token sau mỗi lần refresh.

Nó giống vé gửi xe bị bấm lỗ sau khi dùng. Vé cũ xuất hiện lần nữa là dấu hiệu có bản sao.

Mình không dùng bcrypt cho refresh token. Token có entropy cao, còn server cần hash xác định để lookup nhanh.

SHA-256 phù hợp cho mục đích này. Password yếu do con người chọn mới cần thuật toán chậm như bcrypt.

Schema thêm `AuthSession`. Mỗi session có user ID, token hash, family ID, expiration và thời điểm revoke.

Family ID nối các lần rotation. Khi token cũ bị reuse, server có thể thu hồi toàn bộ nhánh session đó.

Theo OAuth Security Best Current Practice, public client cần rotation hoặc sender-constrained refresh token.

Project này chọn rotation vì dễ nhìn thấy bằng request thật. Đây là một lựa chọn thiết kế, không phải phép màu của JWT.

Mình yêu cầu AI threat-model refresh flow trước. Nó phải mô tả token theft, replay, logout và hai request chạy đồng thời.

AI đề xuất update cùng một row bằng hash mới. Cách đó xóa mất dấu vết token cũ và không phát hiện reuse đáng tin.

Mình sửa plan: row cũ được revoke, row mới được tạo cùng family. Dấu vết phải còn để nhận diện replay.

Login bây giờ phát access token và refresh token ngẫu nhiên. Database chỉ giữ SHA-256 của refresh token.

Với browser, refresh token đi trong cookie `HttpOnly`. JavaScript phía client không đọc được cookie này.

Cookie bật `Secure` ở production, `HttpOnly`, scope `Path` chỉ dành cho refresh/logout và chọn `SameSite` theo kiến trúc frontend. Nếu buộc dùng cross-site cookie, phải có CSRF protection riêng; cookie không tự giải quyết toàn bộ CSRF.

Endpoint refresh đọc cookie, hash giá trị và tìm session. Session hợp lệ phải được consume theo kiểu atomic compare-and-set trong cùng transaction: chỉ row chưa revoke mới được cập nhật. Unique index trên token hash bảo đảm không có hai row cùng đại diện một token.

Sau đó server tạo session thay thế, phát refresh token mới và trả access token mới. Nếu hai request refresh dùng cùng token đến gần như đồng thời, chỉ một request thắng; request còn lại không được tạo thêm session kế nhiệm.

Nếu token đã revoke xuất hiện lại, server xem đó là reuse. Toàn bộ family bị thu hồi.

Đây là chi tiết AI hay bỏ qua. Rotation không có reuse detection chỉ là thay token, chưa phải cơ chế phát hiện đánh cắp. Tuy nhiên request đồng thời do browser retry không tự động chứng minh token đã bị đánh cắp; client nên single-flight refresh và server cần policy grace/reuse được threat-model rõ để tránh tự revoke phiên hợp lệ.

Logout cũng revoke session hiện tại và clear cookie. Xóa cookie phía client thôi chưa đủ vì bản sao token vẫn dùng được.

Đến phần mình tự gõ, mình viết `hashToken` bằng `createHash('sha256')`. Function này nằm trong Auth, không đưa vào common.

Nó phục vụ một policy bảo mật cụ thể. Có hai nơi gọi chưa có nghĩa nó trở thành utility của mọi domain.

Mình approve, xem diff, rồi chạy test theo timeline.

Login tạo session A. Refresh bằng token A trả session B và token A bị revoke.

Dùng token B tiếp tục thành công. Dùng lại token A, server trả 401 và revoke cả family.

Bây giờ token B cũng bị từ chối. Reuse detection đã biến một dấu hiệu bất thường thành hành động bảo vệ.

Login lại, rồi logout. Cookie biến mất và session trong database có `revokedAt`.

Security không nằm ở việc token dài bao nhiêu ký tự. Nó nằm ở lifecycle khi token được tạo, dùng, xoay và thu hồi.

Phiên đăng nhập đã ổn. Nhưng authenticated không đồng nghĩa authorized.

Tập sau, ta tạo Role và Permission.

Ta cũng xem vì sao ba CRUD giống nhau vẫn không nên dùng một CommonService.

Theo dõi series nếu bạn muốn security được kiểm chứng bằng timeline, không bằng niềm tin. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Access token hết hạn; request đang làm nhận 401 | 35s |
| 2 | [DIAGRAM] | Access token ngắn và refresh token dài | 45s |
| 3 | [DIAGRAM] | Vé cũ bị bấm lỗ; reuse báo động | 45s |
| 4 | [IDE] | Thêm refresh TTL vào config đã validate; model AuthSession và các field lifecycle | 60s |
| 5 | [BROWSER] | Mở RFC 9700 đúng đoạn refresh rotation | 35s |
| 6 | [IDE] | Prompt AI threat model bốn tình huống | 60s |
| 7 | [IDE] | Review lỗi update cùng row, chuyển thành token family | 60s |
| 8 | [IDE] | Login tạo opaque token, lưu SHA-256 hash | 70s |
| 9 | [IDE] | Set HttpOnly cookie, production flags | 55s |
| 10 | [IDE] | Transaction revoke cũ và tạo session mới | 75s |
| 11 | [IDE] | Reuse detection và revoke family | 65s |
| 12 | [IDE] | Host tự gõ `hashToken` và logout revoke | 55s |
| 13 | [BROWSER]+[TERM] | Timeline A → B → reuse A → B bị chặn | 80s |
| 14 | [BROWSER] | Login mới, logout, kiểm tra cookie và DB | 50s |
| 15 | [B-ROLL] | Hai chìa khóa trên bàn tối, teaser Role/Permission | 25s |

**Tổng mục tiêu: 8–10 phút.** Khi quay, làm mờ token/cookie thật và chỉ dùng database development.

### Model cốt lõi

```prisma
model AuthSession {
  id               String    @id @default(uuid())
  userId           String
  familyId         String
  refreshTokenHash String    @unique
  expiresAt        DateTime
  revokedAt        DateTime?
  replacedById     String?
  createdAt        DateTime  @default(now())
  user             User      @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@index([userId])
  @@index([familyId])
}
```

### Token helpers

`auth.config.ts` và env schema được mở rộng, không tạo config song song trong AuthService:

```typescript
REFRESH_TOKEN_TTL_DAYS: z.coerce.number().int().min(1).max(90).default(30),
```

```typescript
import { createHash, randomBytes } from 'node:crypto';

const createRefreshToken = () => randomBytes(32).toString('base64url');
const hashToken = (token: string) =>
  createHash('sha256').update(token).digest('hex');
```

### Prompt cho Opus

```text
Threat-model and plan refresh-token rotation for the current NestJS AuthModule.

Requirements:
- Access tokens remain short-lived JWTs.
- Refresh tokens are random opaque values.
- Extend the validated auth config with REFRESH_TOKEN_TTL_DAYS; do not introduce a refresh JWT secret.
- Store only a deterministic cryptographic hash.
- Add a unique constraint/index for the refresh-token hash.
- Rotate on every successful refresh.
- Consume the current session atomically and create its replacement in one transaction.
- Keep revoked rows to detect reuse and revoke the whole token family.
- Logout must revoke server-side state and clear the client cookie.
- Use an HttpOnly cookie for the browser demo.
- Define Secure, SameSite, Path and CSRF policy for the browser demo.
- Discuss concurrent refresh requests, browser retry and client-side single-flight before implementation.
- Do not treat every concurrent loser as theft without documenting the reuse/grace policy.
- Do not edit until I approve the threat model and transaction boundary.
```

### Timeline kiểm chứng

```text
login → refresh A
refresh A → revoke A + issue B
refresh B → revoke B + issue C
reuse A → 401 + revoke family
refresh C → 401
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of two glowing digital keys on a dark developer desk, one short-lived green access key and one rotating cyan refresh key, a copied red key triggering an alarm, dramatic monitor glow, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A cinematic close-up of refresh token A transforming into token B while the old token receives a red revoked stamp, dark IDE with neon syntax, code reflected in eyeglasses, high contrast, left text space, 16:9, photorealistic, no text.`
3. `A cinematic developer confronting a stolen red token while an entire glowing session family shuts down across the monitor, deep navy shadows, rain bokeh, cyan rim light, subject on the right, 16:9, photorealistic, no text, no watermark.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Refresh Token NestJS: Gia hạn đăng nhập và thu hồi phiên — EP07 | Lập trình là cuộc sống
2. Access Token và Refresh Token khác nhau thế nào? — EP07 | Lập trình là cuộc sống
3. Refresh Token Rotation trong NestJS — EP07 | Lập trình là cuộc sống
4. Logout và thu hồi phiên đăng nhập trong NestJS — EP07 | Lập trình là cuộc sống
5. Phát hiện Refresh Token bị sử dụng lại — EP07 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho người mới và Title 3 cho search.

### 4b. SEO Description

```text
Người dùng đã logout nhưng access token cũ vẫn gọi được API. Refresh token rotation tạo lifecycle phiên có thể phát hiện reuse và thu hồi.

✅ Phân biệt access token và refresh token
✅ Tạo opaque token có entropy cao
✅ Chỉ lưu SHA-256 hash trong database
✅ Rotate token sau mỗi lần refresh
✅ Phát hiện reuse và revoke cả token family
✅ Logout thu hồi server-side session
✅ Dùng HttpOnly cookie cho browser demo

🔗 OAuth 2.0 Security BCP: https://www.rfc-editor.org/rfc/rfc9700.html
🔗 NestJS Authentication: https://docs.nestjs.com/security/authentication

⏱ 0:00 Token sống ngắn hay dài?
⏱ 1:20 Hai chiếc chìa khóa
⏱ 2:45 AuthSession và token family
⏱ 4:20 Threat model cùng AI
⏱ 6:00 Hash và HttpOnly cookie
⏱ 7:50 Rotation transaction
⏱ 9:45 Reuse detection
⏱ 11:20 Test timeline A, B, C
⏱ 13:00 Authenticated chưa phải authorized

#NestJS #RefreshToken #JWT #OAuthSecurity #Authentication #CyberSecurity #Backend #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs refresh token, refresh token rotation, refresh token reuse detection, jwt nestjs, auth session database, opaque refresh token, hash refresh token, httpOnly cookie nestjs, logout revoke token, oauth security bcp, rfc 9700, nestjs tiếng việt, học nestjs, nestjs tập 7, backend security, typescript backend, ai coding mentor, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `TOKEN CŨ` — WHITE
- `BÁO ĐỘNG` — NEON GREEN `#00FF41`
- Hình: token A đỏ quay lại khi token B đang sáng.

### Option 2
- `REFRESH TOKEN` — WHITE
- `ĐỪNG LƯU THẲNG` — NEON GREEN `#00FF41`
- Hình: token bị băm trước khi vào database.

### Option 3
- `LOGOUT RỒI` — WHITE
- `VẪN VÀO ĐƯỢC?` — NEON GREEN `#00FF41`
- Hình: cookie bị xóa nhưng bản sao token còn sáng.

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, text trái, subject phải, stroke đen 8px, glow 10px. Typeset trong Canva; giữ nền không chữ.
