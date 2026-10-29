# API của bạn đang bị lộ hết thông tin người dùng!

- **Series:** Học NestJS bằng AI — tập 5/29
- **Trạng thái:** ✅ Đã đăng
- **Ngày đăng:** 2026-10-26
- **Title đã đăng:** API của bạn đang bị lộ hết thông tin người dùng!
- **YouTube:** https://www.youtube.com/watch?v=HvVcAlgp7gU
- **Thumbnail đã đăng:** `assets/thumbnail-05-jwt-auth-v4-final.png`
- **Thời lượng thực tế:** 7:27
- **Technical baseline kiểm tra ngày 26/10/2026:** `@nestjs/core` `12.2.0`; `@nestjs/authentication` `0.1.1`, phải pin exact version theo lockfile.
- **Outcome:** Register, login, hash password bằng scrypt, phát JWT access token và bảo vệ `/users/me`.
- **Pain mở EP06:** Chuẩn bị thêm Role và Permission, nhưng convention phải nhắc lại cho AI mỗi lần.

---

## PART 1 — SCRIPT

Ok, ở tập trước mình đã làm một API biết nói lỗi tử tế. Nhưng bất kỳ ai biết URL vẫn có thể đọc dữ liệu user.

Chính vì thế, giờ mình sẽ sửa lại phần này. Mình có một prompt ngắn như sau.

Audit và plan authentication cho NestJS. Yêu cầu là tạo API đăng ký, login và lấy thông tin user qua `/users/me`. Password phải được hash.

Mình xem nó lên plan như thế nào.

Ok, kế hoạch đã xong. Bạn có thể thấy đây là plan nó đưa ra.

Đầu tiên, nó sẽ tạo bcrypt. Sau đó chỉnh UsersService và controller. Tiếp theo là AuthenticationModule và guard.

Nó đề xuất `@nestjs/jwt` và một AuthGuard tự viết.

Plan này từng rất quen. Nhưng bây giờ, quen không có nghĩa là còn mới nữa.

Mình mở docs NestJS cho bạn xem.

Bạn có thể thấy ngay ở dòng đầu tiên. Bây giờ docs không còn dùng bcrypt như plan vừa rồi. Nó dùng package `@nestjs/authentication`.

Tức là prompt của mình còn sơ sài.

Mình tiếp tục yêu cầu nó plan lại. Lần này, mình bắt nó đọc official docs của NestJS trước.

Mình phải xem xét plan trước khi duyệt. Bây giờ mình làm lại nhé.

Nó sẽ bỏ bcrypt và không dùng `@nestjs/jwt` theo plan cũ nữa. Nó chuyển sang package `@nestjs/authentication`.

Mình cho AI đọc `docs.nestjs.com`. Trong lúc agent phân tích, mình giải thích cho bạn.

JWT giống như vòng tay của một sự kiện. Bảo vệ kiểm tra chữ ký, nhưng không cần hỏi lại quầy vé mỗi lần.

Database tuyệt đối không lưu plaintext password. Nếu database bị lộ, plaintext biến một sự cố thành hàng nghìn tài khoản bị chiếm.

Vì thế, mình cần `PasswordHasher` để băm password được nhập vào.

Ok, plan mới đã có. Bạn có thể thấy package `@nestjs/authentication` phiên bản đầu tiên đã xuất hiện.

Database User cũng được chỉnh đúng theo những gì mình muốn.

Bây giờ mình sẽ approve để nó chạy.

Có một điểm khá thú vị. Plan ghi rõ phần out of scope là refresh token.

Phần refresh token mình sẽ giải thích kỹ ở video tiếp theo. Tập này chúng ta chỉ làm access token.

Trong kế hoạch có hai endpoint là register và login. Mình sẽ tạo chúng trong Postman.

Sau đó mình verify lại khi agent làm xong.

Không có token thì `/users/me` phải trả 401. Token chính xác thì endpoint trả 200.

Token sẽ dùng Bearer Authentication. Trong Postman, mình chọn Bearer Token và dán token vào đây.

Trong lúc chờ agent chạy, tài khoản Antigravity của mình bắt đầu bị giới hạn nhiều hơn.

Việc dùng AI như thế này sẽ tốn tiền hơn trước khá nhiều. Mình cũng không thích thay đổi này.

Mình sẽ cố gắng tìm cho bạn một tool mới, miễn phí hoặc rẻ nhất có thể. Trường phái của mình vẫn là trường phái tiết kiệm.

Ok, mọi thứ đã xong. Bây giờ mình quay lại kiểm thử.

Đầu tiên là register.

Tiếp theo mình login. Bạn có thể thấy API đã trả về một access token.

Access token này là gì, bạn có thể xem video ngắn mình đã làm về JWT.

JWT có ba phần. Phần đầu là header. Phần thứ hai là payload. Phần cuối cùng là signature.

Mình đăng nhập lại để lấy access token.

Tiếp theo là request User Profile. Mình đưa token vừa lấy vào phần Bearer Token.

Bạn có thể thấy endpoint trả 200 OK.

Bỏ token ra thì request trả 401. Như vậy, code đã thực hiện đúng yêu cầu.

Mình xem qua code một chút.

Users đã được bổ sung hai luồng là register và login. Register phục vụ đăng ký. Login phục vụ đăng nhập.

Trong AuthService có `TokenService` để tạo access token.

Trong UsersController có endpoint `/users/me`. Endpoint này sử dụng `@CurrentUser()` từ `@nestjs/authentication`.

Vậy là cánh cửa đã biết người gõ là ai. Nhưng package chính thức không thay mình quyết định ai được phép làm gì.

Tập sau, mình thêm refresh token rotation và khả năng thu hồi session.

Access token sẽ sống ngắn, nhưng người dùng không phải đăng nhập lại liên tục.

Mình sẽ để lại link Git của nhánh này trong description. Nếu có câu hỏi gì, hãy để lại comment nhé. Hẹn gặp ở video sau.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | GET user không auth vẫn thành công | 15s |
| 2 | [IDE] | Agent đưa plan cũ: bcrypt + @nestjs/jwt + custom guard | 30s |
| 3 | [BROWSER] | Mở docs NestJS 12 Authentication và Encryption/Hashing | 35s |
| 4 | [IDE] | Gõ prompt mới, yêu cầu audit docs rồi lập lại plan | 35s |
| 5 | [IDE]+[TERM] | Migration passwordHash, reset dev DB có cảnh báo | 35s |
| 6 | [IDE] | Config boundary: auth.config.ts, JWT_ACCESS_SECRET schema | 25s |
| 7 | [IDE] | Agent trả plan + threat model, review package 0.x, dependency và response leak | 40s |
| 8 | [IDE] | Approve, agent implement, mở diff theo đường request | 40s |
| 9 | [IDE] | Diff: Register, PasswordHasher scrypt, public mapper | 40s |
| 10 | [IDE] | Diff: Login, verify(undefined), TokenService và refreshToken: false | 45s |
| 11 | [IDE] | Diff: JwtBearerProvider, global guard, @Public() | 45s |
| 12 | [IDE] | Host tự gõ `toPublicUser` và `@CurrentUser` | 35s |
| 13 | [BROWSER] | Register, login sai, login đúng | 40s |
| 14 | [BROWSER] | `/users/me`: thiếu, đúng và token bị sửa | 45s |
| 15 | [BROWSER] | Postman: login tự lưu accessToken, chạy tiếp /users/me, export JSON | 35s |
| 16 | [B-ROLL] | Code phản chiếu, teaser Agent Skill, sign-off | 15s |

**Tổng: 555 giây ≈ 9:15, cộng nhịp nghỉ ngắn thành khoảng 9–10 phút.** Che token và JWT secret khi quay; dùng One Dark Pro, JetBrains Mono tối thiểu 18px, ẩn sidebar và minimap.

**Lưu ý flow mới:** Prompt được gõ ngay scene 2. Scenes 3–6 là giải thích khái niệm trong lúc agent lên plan — host nói voiceover, màn hình xen kẽ diagram và IDE hiện agent đang chạy. Scene 7 quay lại IDE khi agent trả kết quả.

### Command chuẩn bị

Trước khi quay, chạy và giữ nguyên exact version trong lockfile:

```bash
# Xem version thật, rồi pin đúng version đó; không quay với @latest
npm view @nestjs/core version
npm view @nestjs/authentication version
npm install --save-exact @nestjs/authentication@0.1.1
nest g module modules/auth
nest g controller modules/auth --no-spec
nest g service modules/auth --no-spec
```

Thêm `JWT_ACCESS_SECRET` vào `.env` local và chỉ thêm placeholder đủ dài vào `.env.example`. `auth.config.ts` là nơi duy nhất chuyển biến môi trường thô thành config của Auth.

```typescript
AuthenticationModule.forRootAsync({
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    accessToken: {
      key: config.getOrThrow<string>('auth.accessSecret'),
      ttl: config.getOrThrow<string>('auth.accessTtl'),
      issuer: config.getOrThrow<string>('auth.issuer'),
      audience: config.getOrThrow<string>('auth.audience'),
    },
    refreshToken: false,
  }),
});
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
const passwordHash = await this.passwordHasher.hash(dto.password);
const user = await this.usersService.createWithPassword(dto, passwordHash);
return toPublicUser(user);
```

```typescript
const credential = await this.usersRepository.findCredentials(dto.email);
const valid = await this.passwordHasher.verify(
  dto.password,
  credential?.passwordHash,
);
if (!credential || !valid) {
  throw new UnauthorizedException('Email hoặc mật khẩu không đúng');
}

return this.tokenService.issue(credential.user.id, {
  method: 'password',
  claims: { amr: ['pwd'] },
});
```

```typescript
export class JwtAuth extends JwtBearerProvider<PublicUser> {
  constructor(
    private readonly users: UsersRepository,
    registry: AuthenticationRegistry,
  ) {
    super({ realm: 'user-management' });
    registry.registerProvider(this);
  }

  validate({ sub }: JwtClaims) {
    return sub ? this.users.findPublicById(sub) : null;
  }
}
```

### Prompt cho Opus

```text
Audit and plan authentication for the existing NestJS 12 Users API.

Setup:
- Read the current official NestJS Authentication and Encryption/Hashing docs first.
- Use @nestjs/authentication and pin its exact 0.x version in package-lock.json.
- Generate AuthModule, AuthController and AuthService under modules/auth.

Requirements:
- Add register, login and GET /users/me.
- Hash passwords with PasswordHasher and never return passwordHash.
- Use AuthenticationModule, TokenService and JwtBearerProvider.
- Keep the package's global guard; only explicit @Public routes bypass authentication.
- Configure and validate key, issuer, audience and access-token TTL once.
- Set refreshToken: false in this episode; do not build refresh-token persistence yet.
- JwtBearerProvider.validate() must load the current public user and reject a deleted user.
- Use one generic 401 message for invalid email or password.
- Pass undefined to PasswordHasher.verify() when credentials are absent, so its built-in dummy verification runs.
- Rehash after successful login when PasswordHasher.needsRehash() is true.
- AuthModule may depend on UsersModule; UsersModule must not import AuthModule.
- Extend the ConfigModule boundary created in EP03 with a typed auth.config.ts.
- Add JWT_ACCESS_SECRET to startup validation; require at least 32 characters and never provide a secret fallback.
- Validate JWT_ISSUER and JWT_AUDIENCE at startup.
- Update .env.example with placeholders only; never commit or print the real secret.
- Do not add sessions, email verification, MFA or refresh tokens in this episode.
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

Không tự tạo `DUMMY_PASSWORD_HASH`. `PasswordHasher.verify(password, undefined)` đã thực hiện dummy verification cùng cost. Sau login thành công, dùng `needsRehash()` để nâng hash cũ khi cấu hình cost thay đổi.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a dark IDE monitor showing an old custom AuthGuard diff being replaced by the official NestJS 12 authentication package, dramatic Nest red and white monitor glow, neon syntax highlighting on a black background, shallow depth of field, rain bokeh through a window, film grain, anamorphic lens flare, 8k, photorealistic, like a high-end tech commercial or developer documentary, 16:9, text-free composition. Not a screenshot, not a tutorial, not cartoon.`
2. `A cinematic photograph of a password entering a glowing scrypt memory grid beside a dark IDE monitor, dramatic Nest red and white monitor glow, code visible with syntax highlighting on a black background, shallow depth of field, bokeh city lights through a window, film grain, 8k, photorealistic, like a high-end tech commercial or developer documentary, 16:9, text-free composition. Not a screenshot, not a tutorial, not cartoon.`
3. `A cinematic photograph of a forged red JWT stopped at a luminous API gate while one valid token passes toward a dark NestJS code monitor, dramatic Nest red and white monitor glow, syntax highlighting on a black background, shallow depth of field, rain bokeh through a window, 8k, photorealistic, like a high-end tech commercial or developer documentary, 16:9, text-free composition. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. NestJS 12 đổi cách làm Authentication như thế nào? — EP05 | Lập trình là cuộc sống
2. JWT Authentication NestJS 12: Register, Login và Bearer Token — EP05 | Lập trình là cuộc sống
3. Đừng tự viết AuthGuard trước khi xem package mới này — EP05 | Lập trình là cuộc sống
4. Một plan AI lỗi thời suýt làm Auth của tôi cũ ngay ngày đầu — EP05 | Lập trình là cuộc sống
5. Hash mật khẩu bằng scrypt trong NestJS 12 — EP05 | Lập trình là cuộc sống
6. NestJS đã có Authentication chính thức, bcrypt còn cần không? — EP05 | Lập trình là cuộc sống
7. Bảo vệ mọi route mặc định trong NestJS 12 — EP05 | Lập trình là cuộc sống
8. JWT không mã hóa dữ liệu: lỗi hiểu nhầm của nhiều Fresher — EP05 | Lập trình là cuộc sống
9. Tạo Register, Login và /users/me đúng kiểu NestJS 12 — EP05 | Lập trình là cuộc sống
10. Code Auth chạy được chưa chắc là Auth nên dùng — EP05 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1 để bắt thay đổi mới của NestJS 12. A/B test Title 2 cho search và Title 4 cho insight AI.

### 4b. SEO Description

```text
API trả lỗi đẹp nhưng vẫn mở cửa cho mọi người. Tập này dùng package authentication chính thức của NestJS 12 để thêm register, login, JWT bearer và global guard.

✅ Hash password bằng PasswordHasher dùng scrypt
✅ Không trả passwordHash cho client
✅ Phát JWT với payload tối thiểu
✅ Verify Bearer token bằng JwtBearerProvider
✅ Dùng global guard, Public và CurrentUser
✅ Phân biệt ký token với mã hóa payload
✅ Test token thiếu, sai và bị chỉnh sửa

🔗 NestJS Authentication: https://docs.nestjs.com/security/authentication
🔗 NestJS Encryption and Hashing: https://docs.nestjs.com/security/encryption-and-hashing

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
nestjs 12 authentication, nestjs authentication, passwordhasher nestjs, scrypt nestjs, register login nestjs, jwt bearer provider, current user decorator, jwt bearer token, password hashing, jwt không mã hóa, nestjs tiếng việt, học nestjs, nestjs tập 5, backend security, typescript backend, ai coding mentor, opus antigravity, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Thumbnail đã đăng

- **File:** `assets/thumbnail-05-jwt-auth-v4-final.png`
- **Hook:** `JWT / KHÔNG / MÃ HÓA`
- **Visual:** Không dùng nhân vật. Bên phải chỉ giữ mắt cảnh báo, payload JWT mở và khiên chữ ký; đã kiểm tra khả năng đọc ở kích thước 320×180.

### Option 1 — khuyên dùng
- **Image prompt:** `A cinematic photograph of a giant glowing NestJS shield replacing fragmented handwritten guard code on a dark IDE monitor, floating red authentication symbols, extreme Nest red and white contrast, dramatic rim lighting, deep shadows, subtle rain and code particles, visual elements positioned on the right leaving empty dark space on the left for text, 8k, 16:9, photorealistic, text-free, not cartoon or illustration.`
- Dòng 1: `NESTJS 12` — WHITE `#FFFFFF`
- Dòng 2: `AUTH ĐỔI RỒI` — `ĐỔI RỒI` NEST RED `#E0234E`, phần còn lại WHITE.
- Badge nhỏ: `EP05` — WHITE trên hộp `#1a1a2e`, viền NEST RED.
- Canvas 1280×720. Font Anton cho headline, JetBrains Mono cho badge. Mỗi dòng cao 110–140px, line spacing 0.85, block trái khoảng một phần ba khung. Stroke đen 8px, shadow/glow đỏ 8–12px ở 65%, không đè visual. Thêm noise/scan-line nhẹ.

### Option 2
- **Image prompt:** `A cinematic photograph of a plaintext password entering an exaggerated glowing scrypt memory grid beside a dark NestJS IDE, floating hash fragments and memory blocks, extreme Nest red and white lighting, dramatic rim light, deep black shadows and subtle fog, visual elements positioned on the right leaving empty dark space on the left for text, 8k, 16:9, photorealistic, text-free, not cartoon or illustration.`
- Dòng 1: `BCRYPT` — WHITE `#FFFFFF`
- Dòng 2: `KHÔNG CÒN MẶC ĐỊNH` — `KHÔNG CÒN` NEST RED `#E0234E`, phần còn lại WHITE.
- Badge nhỏ: `SCRYPT` — WHITE trên hộp `#1a1a2e`, viền NEST RED.
- Canvas 1280×720. Font Anton cho headline, JetBrains Mono cho badge. Mỗi dòng cao 110–140px, line spacing 0.85, block trái khoảng một phần ba khung. Stroke đen 8px, shadow/glow đỏ 8–12px ở 65%, không đè visual. Thêm noise/scan-line nhẹ.

### Option 3
- **Image prompt:** `A cinematic photograph of an AI coding panel proposing an old custom JWT guard while an official NestJS 12 authentication document glows red beside it, floating diff lines and a sharp warning marker, extreme red and white contrast, deep shadows and dramatic monitor light, visual elements positioned on the right leaving empty dark space on the left for text, 8k, 16:9, photorealistic, text-free, not cartoon or illustration.`
- Dòng 1: `AI ĐƯA CODE CŨ` — WHITE `#FFFFFF`
- Dòng 2: `DOCS CỨU TÔI` — `CỨU TÔI` NEST RED `#E0234E`, phần còn lại WHITE.
- Badge nhỏ: `NESTJS 12` — WHITE trên hộp `#1a1a2e`, viền NEST RED.
- Canvas 1280×720. Font Anton cho headline, JetBrains Mono cho badge. Mỗi dòng cao 110–140px, line spacing 0.85, block trái khoảng một phần ba khung. Stroke đen 8px, shadow/glow đỏ 8–12px ở 65%, không đè visual. Thêm noise/scan-line nhẹ.

Luôn typeset trong Canva thay vì để AI render chữ. Giữ bản nền sạch không chữ để tái sử dụng và A/B test.
