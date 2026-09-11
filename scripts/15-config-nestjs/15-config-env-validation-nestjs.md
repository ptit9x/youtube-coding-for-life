# NestJS #15 — Config: Quản lý ENV an toàn cho mọi môi trường

- **Series:** Học NestJS bằng AI — tập 15/46
- **Target runtime:** ~12 phút
- **Outcome:** Config có type, validation lúc startup và secret không rò vào source.
- **Pain mở EP16:** Nhiều lớp cùng xử lý request khiến debug trở nên mơ hồ.

---

## PART 1 — SCRIPT

TaskFlow chạy tốt trên máy mình.

Đưa sang môi trường khác, ứng dụng khởi động rồi liên tục báo lỗi database.

Nguyên nhân là `DATABASE_URL` bị thiếu. `JWT_SECRET` còn dùng giá trị mặc định nguy hiểm.

Ứng dụng đã chấp nhận config sai và chết quá muộn.

App phải fail fast ngay khi startup, trước khi nhận request đầu tiên.

Mình tìm toàn bộ nơi đọc `process.env`.

Kết quả xuất hiện ở `main.ts`, `auth.module.ts`, `prisma.service.ts` và cả `users.service.ts`.

UsersService không nên biết biến môi trường tồn tại.

Business code chỉ cần dependency đã được cấu hình.

Ta dùng ConfigModule làm boundary giữa môi trường và ứng dụng.

ConfigModule trở thành global boundary. Nó nạp app, database, auth config và kiểm tra toàn bộ env schema.

Một file config khổng lồ sẽ sớm thành bãi chứa.

Mình chia theo app, database và auth.

Trong `src/config`, mỗi concern có một file riêng. `env.validation.ts` đứng ở cửa kiểm tra đầu vào.

Mỗi factory đổi string thô thành cấu trúc có nghĩa.

Port trở thành number. Thời gian token trở thành giá trị được kiểm tra.

Database URL chỉ được đọc tại config boundary.

Mình yêu cầu AI review repo như một pull request bảo mật.

AI tìm thấy `.env` trong vùng Git theo dõi.

Nó cũng thấy fallback `JWT_SECRET || 'secret'`.

Fallback đó tiện cho demo nhưng nguy hiểm ở production.

Secret bắt buộc không nên có default.

Mình giữ `.env.example` chỉ chứa tên biến và giá trị giả.

`.env` thật nằm trong gitignore và secret manager của nền tảng deploy.

`env.validation.ts` kiểm tra toàn bộ đầu vào môi trường.

Schema giới hạn `NODE_ENV`, kiểm tra port, bắt buộc database URL và hai JWT secret đủ dài.

Mình cố tình xóa `DATABASE_URL` rồi chạy app.

Process dừng ngay với message rõ ràng.

Fail fast tốt hơn nhận traffic rồi trả 500 ngẫu nhiên.

Ba môi trường dùng cùng code, nhưng khác giá trị config.

Development có log chi tiết và database local.

Test dùng database cô lập cùng token sống ngắn.

Production lấy secret từ nền tảng deploy và tắt stacktrace ngoài client.

Không dùng `if production` rải khắp service.

Config factory gom khác biệt thành dependency rõ ràng.

Test có thể override provider thay vì sửa biến toàn cục giữa chừng.

Mình đổi port, database và token duration mà không sửa business code.

Thiếu secret, ứng dụng từ chối khởi động.

Repo không còn key thật. `.env.example` giúp người mới biết cần cấu hình gì.

Config đã rõ, nhưng request vẫn đi qua nhiều lớp.

Middleware log một dòng. Guard log dòng khác. Pipe ném lỗi trước handler.

Khi request thất bại, chúng ta chưa biết nó dừng ở đâu.

Tập sau, ta soi toàn bộ request lifecycle bằng log và sequence diagram.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERMINAL] | App khởi động rồi lỗi database vì thiếu config | 40s |
| 2 | [IDE] | Tìm các chỗ đọc `process.env` | 60s |
| 3 | [DIAGRAM] | Environment → Config boundary → Application | 55s |
| 4 | [IDE] | Chia app, database và auth config | 75s |
| 5 | [AI] | Audit `.env`, secret và fallback nguy hiểm | 75s |
| 6 | [IDE] | Host viết validation schema | 90s |
| 7 | [TERMINAL] | Xóa biến bắt buộc và quan sát fail fast | 60s |
| 8 | [TABLE] | Dev, test và production khác giá trị | 70s |
| 9 | [TERMINAL] | Chạy lại với config hợp lệ | 50s |
| 10 | [B-ROLL] | Request đi qua nhiều lớp, teaser EP16 | 30s |

**Tổng: 605 giây ≈ 10:05.** Dành thêm hai phút giải thích secret management; che mọi secret thật.

### Code cốt lõi

```ts
export default registerAs('auth', () => ({
  accessSecret: process.env.JWT_ACCESS_SECRET,
  refreshSecret: process.env.JWT_REFRESH_SECRET,
  accessTtl: process.env.JWT_ACCESS_TTL ?? '15m',
}));
```

```ts
ConfigModule.forRoot({
  isGlobal: true,
  cache: true,
  load: [appConfig, databaseConfig, authConfig],
  validationSchema: envSchema,
});
```

### Prompt cho AI

```text
Audit the repository configuration as a security-focused pull request.
- Find direct process.env reads outside src/config.
- Find tracked secrets and unsafe fallback values.
- Group configuration by app, database and auth concerns.
- Validate all required values during startup.
- Keep .env ignored and update only .env.example.
- Do not import ConfigService into business services.
- Show the audit and migration plan before editing.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic NestJS server refusing to start beside a missing secret key warning, dark terminal, red alert and neon green configuration panel, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic developer moving scattered environment variables into one glowing secure configuration vault, dark IDE background, cyan rim light, 16:9, photorealistic, no text.`
3. `A cinematic application running across development test and production environments from one codebase, three illuminated server lanes, dark atmosphere, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Config NestJS: Quản lý ENV an toàn cho dev và production — EP15 | Lập trình là cuộc sống
2. Validation biến môi trường khi NestJS khởi động — EP15 | Lập trình là cuộc sống
3. Dọn process.env khỏi business logic — EP15 | Lập trình là cuộc sống
4. Bảo vệ JWT secret và DATABASE_URL trong NestJS — EP15 | Lập trình là cuộc sống
5. Cấu hình dev, test và production bằng ConfigModule — EP15 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho validation và Title 5 cho search.

### 4b. SEO Description

```text
Ứng dụng không nên nhận traffic khi DATABASE_URL hoặc JWT secret đang sai. Hãy fail fast từ lúc startup.

✅ Dọn process.env khỏi business code
✅ Chia app, database và auth config
✅ Validate biến môi trường khi startup
✅ Loại fallback JWT secret nguy hiểm
✅ Tách dev, test và production
✅ Giữ secret thật ngoài Git

🔗 NestJS Configuration: https://docs.nestjs.com/techniques/configuration

⏱ 0:00 Config sai chết quá muộn
⏱ 1:20 Dọn process.env
⏱ 3:00 Chia config theo concern
⏱ 4:35 Audit secret bằng AI
⏱ 6:20 Validation và fail fast
⏱ 8:20 Dev, test, production
⏱ 9:50 Payoff

#NestJS #ConfigModule #EnvironmentVariables #Security #TypeScript #Backend #DevOps #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs config module, env validation nestjs, environment variables nestjs, jwt secret security, process env typescript, configuration management, nestjs joi validation, fail fast configuration, nestjs tiếng việt, nestjs tập 15, backend configuration, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `THIẾU ENV?` — WHITE
- `DỪNG APP NGAY` — RED `#FF3B30`
### Option 2
- `ĐỪNG RẢI` — WHITE
- `PROCESS.ENV` — NEON GREEN `#00FF41`
### Option 3
- `SECRET MẶC ĐỊNH` — WHITE
- `RẤT NGUY HIỂM` — RED `#FF3B30`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
