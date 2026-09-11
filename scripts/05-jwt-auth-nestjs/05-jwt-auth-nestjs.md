# NestJS #05 — JWT Authentication: Register, Login và AuthGuard

- **Series:** Học NestJS bằng AI — tập 5/46
- **Target runtime:** ~13 phút
- **Outcome:** Register, login, hash password, phát JWT và bảo vệ `/users/me`.
- **Pain mở EP06:** Chuẩn bị thêm Role và Permission, nhưng convention phải nhắc lại cho AI mỗi lần.

---

## PART 1 — SCRIPT

API đã biết nói lỗi tử tế. Nhưng bất kỳ ai biết URL vẫn có thể đọc dữ liệu user.

Không có danh tính, request chỉ là một người lạ gõ cửa. Controller không biết nên mở cho ai.

Thêm một field `isLoggedIn` không giải quyết được gì. Client có thể tự gửi `true` nhanh hơn mình viết code.

Bước ngoặt là xác thực bằng bằng chứng server ký. Password chứng minh lúc đăng nhập, JWT chứng minh ở những request tiếp theo.

JWT giống vòng tay của một sự kiện. Bảo vệ kiểm tra chữ ký, nhưng không cần hỏi lại quầy vé mỗi lần.

Mình bắt đầu từ password. Database tuyệt đối không lưu plaintext.

Nếu database bị lộ, plaintext biến một sự cố thành hàng nghìn tài khoản bị chiếm.

Mình dùng bcrypt để tạo password hash. Hash là phép biến đổi một chiều, còn salt làm hai password giống nhau có kết quả khác.

Project đang có user test từ tập trước. Migration mới thêm `passwordHash` bắt buộc sẽ không thể đi qua dữ liệu cũ.

Vì đây chỉ là database development, mình reset có chủ đích. Màn hình hiện cảnh báo dữ liệu sẽ bị xóa.

Lệnh này không bao giờ được dùng tùy tiện trên production. Một command đúng môi trường vẫn có thể là command phá hoại ở môi trường khác.

Tiếp theo, mình tạo AuthModule với register và login. Auth phụ thuộc Users, còn Users không import ngược Auth.

Dependency một chiều giúp hai module không kéo nhau thành vòng tròn.

Mình yêu cầu AI lập threat model trước khi code. Nó phải liệt kê password leak, timing, token giả và user enumeration.

AI đề xuất trả nguyên user sau register. Trong object đó có `passwordHash`.

Đây là kiểu bug nhìn response vẫn chạy ngon. Mình yêu cầu mapper loại field nhạy cảm trước khi trả khỏi service boundary.

Register nhận name, email và password. Validation kiểm tra độ dài, còn AuthService gọi bcrypt hash trước khi lưu.

Login tìm user theo email. Bcrypt compare kiểm tra password mà không giải mã hash.

Nếu sai email hoặc password, cả hai cùng nhận một thông báo 401 chung. Client không cần biết tài khoản nào tồn tại.

Khi đúng, JwtService ký payload chỉ có `sub`. Trong JWT, `sub` là subject, ở đây chính là user ID.

Mình chưa nhét role hoặc permission vào token. Quyền thay đổi thường xuyên hơn danh tính, và token cũ không tự cập nhật.

Secret không nằm trong source code. Tập Config sẽ tổ chức nó đầy đủ; hiện tại terminal export biến môi trường trước khi chạy.

AuthGuard lấy Bearer token từ header, verify chữ ký và expiration. Payload hợp lệ được gắn vào request.

`@CurrentUser` chỉ giúp controller đọc user hiện tại gọn hơn. Decorator không tự xác thực và không thay guard.

Mình approve plan. Agent implement, rồi mình mở diff theo đường request thay vì đọc ngẫu nhiên từng file.

Đường register là controller, AuthService, UsersRepository rồi PostgreSQL. Đường `/users/me` đi qua AuthGuard trước controller.

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
| 1 | [BROWSER] | GET user không auth vẫn thành công | 30s |
| 2 | [DIAGRAM] | Password lúc login → JWT cho request sau | 45s |
| 3 | [DIAGRAM] | Plaintext vs salted hash; không minh họa giải mã hash | 45s |
| 4 | [IDE]+[TERM] | Thêm passwordHash, migration/reset dev có cảnh báo | 55s |
| 5 | [TERM] | Cài bcrypt và `@nestjs/jwt`; export JWT_SECRET | 40s |
| 6 | [IDE] | Gõ prompt threat model và plan | 60s |
| 7 | [IDE] | Review dependency Auth → Users và response leak | 55s |
| 8 | [IDE] | Register flow, bcrypt hash, public mapper | 70s |
| 9 | [IDE] | Login flow, compare và payload `{ sub }` | 70s |
| 10 | [IDE] | AuthGuard verify Bearer token | 65s |
| 11 | [IDE] | Host tự gõ `toPublicUser` và `@CurrentUser` | 55s |
| 12 | [BROWSER] | Register, login sai, login đúng | 65s |
| 13 | [BROWSER] | `/users/me`: thiếu, đúng và token bị sửa | 70s |
| 14 | [B-ROLL] | Vòng tay sự kiện, code phản chiếu, teaser skill | 25s |

**Tổng: 750 giây ≈ 12:40.** Che token và JWT secret khi quay; font IDE tối thiểu 18px.

### Command chuẩn bị

```bash
npm install @nestjs/jwt bcrypt
npm install --save-dev @types/bcrypt
nest g module modules/auth
nest g controller modules/auth --no-spec
nest g service modules/auth --no-spec
export JWT_SECRET="dev-only-change-me"
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
@UseGuards(AuthGuard)
@Get('me')
findMe(@CurrentUser() actor: AuthenticatedUser) {
  return this.usersService.findPublicById(actor.id);
}
```

### Prompt cho Opus

```text
Plan JWT authentication for the existing NestJS Users API.

Requirements:
- Add register, login and GET /users/me.
- Hash passwords with bcrypt and never return passwordHash.
- Use @nestjs/jwt and a Bearer-token AuthGuard.
- JWT payload contains sub only for now.
- Use one generic 401 message for invalid email or password.
- AuthModule may depend on UsersModule; UsersModule must not import AuthModule.
- Read JWT_SECRET from the environment and fail at startup if missing.
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

1. JWT Authentication NestJS: Register, Login và AuthGuard — EP05 | Lập trình là cuộc sống
2. Xây chức năng đăng nhập JWT trong NestJS — EP05 | Lập trình là cuộc sống
3. Hash mật khẩu với bcrypt trong NestJS — EP05 | Lập trình là cuộc sống
4. Bảo vệ API bằng AuthGuard và JWT — EP05 | Lập trình là cuộc sống
5. Tạo API /users/me trong NestJS — EP05 | Lập trình là cuộc sống

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
⏱ 1:15 Password hash và salt
⏱ 2:40 Migration passwordHash
⏱ 4:00 Threat model cùng AI
⏱ 5:30 Register và public mapper
⏱ 7:15 Login và JWT payload
⏱ 9:00 AuthGuard và CurrentUser
⏱ 10:35 Kiểm chứng năm request
⏱ 12:10 Chuẩn bị đóng gói convention

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
