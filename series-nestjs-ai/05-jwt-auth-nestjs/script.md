# NestJS #05 — JWT Authentication: Register, Login và AuthGuard

- **Series:** Học NestJS bằng AI — tập 5/45
- **Target runtime:** 8–10 phút (650–800 từ thoại)
- **Outcome:** Register, login, hash password, phát JWT và bảo vệ `/users/me`.
- **Pain mở EP06:** Chuẩn bị thêm Role và Permission, nhưng convention phải nhắc lại cho AI mỗi lần.

---

## PART 1 — SCRIPT

API đã biết nói lỗi tử tế. Nhưng bất kỳ ai biết URL vẫn có thể đọc dữ liệu user.

Không có danh tính, request chỉ là một người lạ gõ cửa. Controller không biết nên mở cho ai.

Thêm một field `isLoggedIn` không giải quyết được gì. Client có thể tự gửi `true` nhanh hơn mình viết code.

Bước ngoặt là xác thực bằng bằng chứng server ký. Password chứng minh lúc đăng nhập, JWT chứng minh ở những request tiếp theo.

Mình gõ prompt cho agent luôn. Cài bcrypt, `@nestjs/jwt`, tạo AuthModule, register, login, hash password, AuthGuard toàn cục, mở rộng config boundary từ EP03. Lên threat model và plan trước, không code khi chưa duyệt.

Trong lúc agent phân tích, mình giải thích cho bạn.

JWT giống vòng tay của một sự kiện. Bảo vệ kiểm tra chữ ký, nhưng không cần hỏi lại quầy vé mỗi lần.

Database tuyệt đối không lưu plaintext password. Nếu database bị lộ, plaintext biến một sự cố thành hàng nghìn tài khoản bị chiếm.

Bcrypt tạo password hash — phép biến đổi một chiều. Salt làm hai password giống nhau có kết quả khác.

Project đang có user test từ tập trước. Migration thêm `passwordHash` bắt buộc sẽ không đi qua dữ liệu cũ.

Vì đây chỉ là database development, mình reset có chủ đích. Màn hình hiện cảnh báo dữ liệu sẽ bị xóa.

Lệnh này không bao giờ được dùng tùy tiện trên production. Một command đúng môi trường vẫn có thể là command phá hoại ở môi trường khác.

Secret không nằm trong source code. Prompt yêu cầu mở rộng config boundary đã tạo ở EP03 với `auth.config.ts`. `JWT_ACCESS_SECRET` bắt buộc tối thiểu 32 ký tự, không có fallback. Nếu thiếu, application từ chối khởi động.

Agent trả plan. Mình kiểm tra threat model: password leak, timing attack, token giả, user enumeration.

AuthModule phụ thuộc Users, còn Users không import ngược Auth. Dependency một chiều giúp hai module không kéo nhau thành vòng tròn.

AI đề xuất trả nguyên user sau register. Trong object đó có `passwordHash`. Đây là kiểu bug nhìn response vẫn chạy ngon. Mình yêu cầu mapper loại field nhạy cảm trước khi trả khỏi service boundary.

Mình approve plan. Agent implement, rồi mình mở diff theo đường request thay vì đọc ngẫu nhiên từng file.

Register nhận name, email và password. Validation kiểm tra độ dài, còn AuthService gọi bcrypt hash trước khi lưu.

Login tìm user theo email. Bcrypt compare kiểm tra password mà không giải mã hash. Nếu email không tồn tại, service vẫn chạy một lần compare với dummy hash để giảm chênh lệch timing dễ quan sát giữa "không có user" và "sai password".

Nếu sai email hoặc password, cả hai cùng nhận một thông báo 401 chung. Client không cần biết tài khoản nào tồn tại.

Khi đúng, JwtService ký payload chỉ có `sub`. Trong JWT, `sub` là subject, ở đây chính là user ID. Cấu hình ký và verify khóa cứng algorithm, issuer và audience; không chỉ kiểm tra mỗi secret và expiration.

Mình chưa nhét role hoặc permission vào token. Quyền thay đổi thường xuyên hơn danh tính, và token cũ không tự cập nhật.

AuthGuard lấy Bearer token từ header, verify chữ ký, algorithm, issuer, audience và expiration. Payload hợp lệ được gắn vào request.

Guard được đăng ký toàn cục bằng `APP_GUARD`: mặc định route phải xác thực. Chỉ register, login và health check được đánh dấu `@Public()`. Cách này tránh quên gắn guard khi thêm controller mới.

`@CurrentUser` chỉ giúp controller đọc user hiện tại gọn hơn. Decorator không tự xác thực và không thay guard.

Đường register là route `@Public()`, AuthService, UsersRepository rồi PostgreSQL. Đường `/users/me` tự động đi qua global AuthGuard trước controller.

Đến phần tự gõ, mình viết mapper `toPublicUser`. Type trả về không có `passwordHash`.

Đây là defense in depth. Kể cả controller return user, compiler cũng nhắc nếu mình làm rò field nhạy cảm.

Giờ kiểm chứng. Register trả 201 và không có hash. Login sai trả 401 với message chung.

Login đúng trả access token. Gọi `/users/me` không token nhận 401.

Gắn header `Authorization: Bearer ...`, endpoint trả đúng user đang đăng nhập.

Mình sửa một ký tự trong token. Chữ ký không còn khớp và guard chặn ngay.

JWT không phải mã hóa bí mật. Payload có thể được đọc; chữ ký chỉ giúp phát hiện nó bị sửa.

Cánh cửa đã biết người gõ là ai. Nhưng chuẩn bị xây Role và Permission, mình lại phải mô tả cùng convention cho AI.

Tập sau, ta biến convention đã kiểm chứng thành Agent Skill. AI sẽ nhớ cách scaffold, còn mình vẫn giữ quyền duyệt.

Đừng tin token chỉ vì nó trông dài và khó đọc. Theo dõi series để cùng kiểm tra từng lớp bảo vệ. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | GET user không auth vẫn thành công | 25s |
| 2 | [IDE] | Gõ prompt đầy đủ: install, auth, config, threat model | 50s |
| 3 | [DIAGRAM] | JWT = vòng tay sự kiện; password lúc login → JWT cho request sau | 45s |
| 4 | [DIAGRAM] | Plaintext vs salted hash; không minh họa giải mã | 40s |
| 5 | [IDE]+[TERM] | Migration passwordHash, reset dev DB có cảnh báo | 50s |
| 6 | [IDE] | Config boundary: auth.config.ts, JWT_ACCESS_SECRET schema | 35s |
| 7 | [IDE] | Agent trả plan + threat model, review dependency và response leak | 60s |
| 8 | [IDE] | Approve, agent implement, mở diff theo đường request | 55s |
| 9 | [IDE] | Diff: Register flow, bcrypt hash, public mapper | 60s |
| 10 | [IDE] | Diff: Login flow, compare, dummy hash, payload `{ sub }` | 60s |
| 11 | [IDE] | Diff: AuthGuard, APP_GUARD, @Public() | 55s |
| 12 | [IDE] | Host tự gõ `toPublicUser` và `@CurrentUser` | 50s |
| 13 | [BROWSER] | Register, login sai, login đúng | 60s |
| 14 | [BROWSER] | `/users/me`: thiếu, đúng và token bị sửa | 65s |
| 15 | [B-ROLL] | Code phản chiếu, teaser Agent Skill | 20s |

**Tổng: 730 giây ≈ 12:10.** Che token và JWT secret khi quay; font IDE tối thiểu 18px.

**Lưu ý flow mới:** Prompt được gõ ngay scene 2. Scenes 3–6 là giải thích khái niệm trong lúc agent lên plan — host nói voiceover, màn hình xen kẽ diagram và IDE hiện agent đang chạy. Scene 7 quay lại IDE khi agent trả kết quả.

### Command chuẩn bị

Agent sẽ tự chạy install và scaffold từ prompt. Host chỉ cần biết để verify diff:

```bash
# Agent chạy từ prompt:
npm install @nestjs/jwt bcrypt
npm install --save-dev @types/bcrypt
nest g module modules/auth
nest g controller modules/auth --no-spec
nest g service modules/auth --no-spec
```

Thêm `JWT_ACCESS_SECRET` vào `.env` local và chỉ thêm placeholder đủ dài vào `.env.example`. `auth.config.ts` là nơi duy nhất chuyển biến môi trường thô thành config của Auth.

```typescript
export default registerAs('auth', () => ({
  accessSecret: process.env.JWT_ACCESS_SECRET!,
  accessTtl: process.env.JWT_ACCESS_TTL ?? '15m',
  issuer: process.env.JWT_ISSUER!,
  audience: process.env.JWT_AUDIENCE!,
}));
```

Schema từ EP03 được mở rộng để app fail fast:

```typescript
JWT_ACCESS_SECRET: z.string().min(32),
JWT_ACCESS_TTL: z.string().default('15m'),
JWT_ISSUER: z.string().min(1),
JWT_AUDIENCE: z.string().min(1),
```

### Code cốt lõi

```typescript
const passwordHash = await bcrypt.hash(dto.password, 12);
const user = await this.usersService.createWithPassword(dto, passwordHash);
return toPublicUser(user);
```

```typescript
const valid = user && await bcrypt.compare(dto.password, user.passwordHash);
if (!valid) {
  throw new UnauthorizedException('Email hoặc mật khẩu không đúng');
}

return {
  accessToken: await this.jwtService.signAsync({ sub: user.id }),
};
```

```typescript
@Get('me')
findMe(@CurrentUser() actor: AuthenticatedUser) {
  return this.usersService.findPublicById(actor.id);
}
```

### Prompt cho Opus

```text
Plan JWT authentication for the existing NestJS Users API.

Setup:
- Install @nestjs/jwt and bcrypt (with @types/bcrypt as dev dependency).
- Generate AuthModule, AuthController and AuthService under modules/auth.

Requirements:
- Add register, login and GET /users/me.
- Hash passwords with bcrypt and never return passwordHash.
- Use @nestjs/jwt and a Bearer-token AuthGuard.
- Register AuthGuard globally with APP_GUARD; only explicit @Public routes bypass authentication.
- Pin the JWT algorithm and validate issuer, audience and expiration.
- JWT payload contains sub only for now.
- Use one generic 401 message for invalid email or password.
- Perform a dummy password-hash comparison when the email is absent to reduce timing differences.
- AuthModule may depend on UsersModule; UsersModule must not import AuthModule.
- Extend the ConfigModule boundary created in EP03 with a typed auth.config.ts.
- Add JWT_ACCESS_SECRET to startup validation; require at least 32 characters and never provide a secret fallback.
- Validate JWT_ISSUER and JWT_AUDIENCE at startup.
- Update .env.example with placeholders only; never commit or print the real secret.
- First produce a threat model, file plan and verification matrix.
- Do not edit before approval.
```

### Request matrix

| Request | Expected |
|---|---:|
| Register hợp lệ | 201, không có hash |
| Login sai | 401 |
| `/users/me` không token | 401 |
| Token hợp lệ | 200 |
| Token bị sửa | 401 |

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese developer holding a glowing JWT token like a digital wristband before a locked API doorway, dark code screens, neon green and cyan lighting, dramatic shadows, subject on the right with empty left space, 16:9, photorealistic, no text, no logos, no watermark.`
2. `A cinematic close-up of plaintext password dissolving into an irreversible bcrypt hash on a dark IDE monitor, code reflected in eyeglasses, neon green syntax and red warning light, empty space on the left, 16:9, photorealistic tech commercial, no text.`
3. `A cinematic developer workspace where a forged red JWT is stopped by a glowing cyan guard while a valid green token passes, rain bokeh, deep navy background, subject positioned right, 16:9, photorealistic, no text, no watermark.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. JWT Authentication NestJS: Register, Login và AuthGuard — EP05
2. Xây chức năng đăng nhập JWT trong NestJS — EP05
3. Hash mật khẩu với bcrypt trong NestJS — EP05
4. Bảo vệ API bằng AuthGuard và JWT — EP05
5. Tạo API /users/me trong NestJS — EP05

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 4 cho outcome bảo mật.

### 4b. SEO Description

```text
API trả lỗi đẹp nhưng vẫn mở cửa cho mọi người. Tập này thêm register, login, bcrypt, JWT và AuthGuard đúng boundary.

✅ Hash password bằng bcrypt
✅ Không trả passwordHash cho client
✅ Phát JWT với payload tối thiểu
✅ Verify Bearer token bằng AuthGuard
✅ Tạo decorator CurrentUser
✅ Phân biệt ký token với mã hóa payload
✅ Test token thiếu, sai và bị chỉnh sửa

🔗 NestJS Authentication: https://docs.nestjs.com/security/authentication
🔗 NestJS JWT: https://github.com/nestjs/jwt

⏱ 0:00 API chưa có khóa
⏱ 0:25 Gõ prompt cho agent
⏱ 1:15 JWT và password hash
⏱ 2:40 Migration passwordHash
⏱ 3:30 Config boundary
⏱ 4:05 Review threat model
⏱ 5:00 Agent implement
⏱ 5:55 Register, login, JWT payload
⏱ 8:00 AuthGuard và CurrentUser
⏱ 9:10 Kiểm chứng năm request
⏱ 11:15 Chuẩn bị đóng gói convention

#NestJS #JWT #Authentication #Bcrypt #TypeScript #Backend #AICoding #CyberSecurity #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs jwt auth, nestjs authentication, bcrypt nestjs, register login nestjs, auth guard nestjs, current user decorator, jwt bearer token, password hashing, jwt không mã hóa, nestjs tiếng việt, học nestjs, nestjs tập 5, backend security, typescript backend, users auth api, ai coding mentor, opus antigravity, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `JWT` — NEON GREEN `#00FF41`
- `KHÔNG MÃ HÓA` — WHITE
- Hình: payload JWT nhìn thấy được, chữ ký phát sáng.

### Option 2
- `PASSWORD` — WHITE
- `ĐỪNG LƯU THẲNG` — NEON GREEN `#00FF41`
- Hình: plaintext rơi vào máy nghiền bcrypt.

### Option 3
- `AI VIẾT AUTH` — WHITE
- `TÔI BẮT LỖI` — NEON GREEN `#00FF41`
- Hình: agent panel cạnh response rò passwordHash.

**Typography chung:** Canvas 1280×720, Anton cho hook và JetBrains Mono cho `NESTJS #05`. Chữ trái, hình phải, stroke 8px, glow 10px. Typeset trong Canva; giữ bản nền không chữ.
