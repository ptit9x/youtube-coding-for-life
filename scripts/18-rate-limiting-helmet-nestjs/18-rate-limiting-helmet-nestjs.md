# NestJS #18 — Rate Limiting và Helmet: dạy API tự vệ

- **Series:** Học NestJS bằng AI — tập 18/45
- **Target runtime:** khoảng 6 phút 30 giây (592 từ thoại)
- **Outcome:** Login có rate limit riêng, API có security headers và hoạt động đúng sau reverse proxy.
- **Pain tập kế:** Khi bị spam, log rời rạc khiến một request không thể truy vết.

---

## PART 1 — SCRIPT

Swagger vừa công khai toàn bộ cửa ra vào của TaskFlow.

Một bot không cần đọc source. Nó chỉ cần bấm login nhanh hơn người thật.

Trong vài giây, endpoint auth nhận hàng trăm mật khẩu đoán thử.

Mình từng nghĩ JWT và validation đã đủ bảo vệ API.

Chúng kiểm tra request có hợp lệ. Chúng không kiểm tra request đến quá nhiều.

Chặn toàn bộ ở cùng một mức cũng không ổn.

Ba lần login một phút có thể đáng ngờ. Ba lần tải task thì hoàn toàn bình thường.

Bước ngoặt là rate limit phải phản ánh rủi ro của từng route.

Rate limiting là chiếc van giới hạn số request trong một khoảng thời gian.

Nó giảm brute force và spam. Nó không biến API thành pháo đài bất khả xâm phạm.

Mình yêu cầu AI lập threat model cho login, refresh token, docs và task endpoint.

AI đề xuất một con số toàn cục rồi bắt đầu sửa code.

Mình dừng ở bước review. Một chính sách cho mọi route là quá thô.

Mình approve plan mới với nhiều throttler theo cửa sổ ngắn và dài.

`ThrottlerModule` giữ cấu hình mặc định cho API thông thường.

`ThrottlerGuard` chạy toàn cục, nên route mới không vô tình mở hoàn toàn.

Riêng login dùng `Throttle` chặt hơn.

Tracker ban đầu là IP. Sau khi xác thực, tracker có thể ghép user ID với route.

Nhưng production của mình đứng sau reverse proxy.

Nếu đọc sai địa chỉ, mọi người dùng có thể trông như cùng một IP.

Mình cấu hình `trust proxy` đúng hạ tầng, rồi kiểm tra `req.ip` bằng request thật.

Không tin mù quáng header `X-Forwarded-For` từ Internet.

Một instance dùng bộ nhớ có thể đủ cho local.

Nhiều instance cần storage dùng chung, nếu không mỗi máy đếm một kiểu.

Rate limit chỉ là một lớp. Helmet xử lý lớp header của trình duyệt.

Helmet thêm các security header để giảm một số kiểu tấn công web phổ biến.

Nó phải được gắn trước route và các middleware cần được bảo vệ.

Swagger UI dùng script và style riêng, nên Content Security Policy có thể chặn giao diện.

Mình không tắt toàn bộ CSP cho tiện.

Mình chỉ cho phép đúng nguồn Swagger cần, hoặc đóng docs trên production.

Giờ tới phần vui nhất: để AI viết script spam chính API của mình.

Năm request đầu đi qua. Request tiếp theo trả bốn-hai-chín.

Header cho biết client nên chậm lại.

Sau đó mình đổi IP giả bằng header tùy ý.

Nếu proxy chưa được cấu hình đúng, cách né này dễ đến mức hơi xúc phạm.

Mình sửa trust boundary, chạy lại test và thử bằng hai tài khoản.

Login bị giới hạn riêng. GET task vẫn hoạt động trong mức bình thường.

Response có security headers. Swagger vẫn mở được cho đúng môi trường.

Rate limit không chỉ là một con số. Nó là quyết định ai được làm gì, nhanh tới đâu.

Khi API biết tự nói chậm lại, production bớt mong manh hơn một chút.

Nhưng lúc bốn-hai-chín xuất hiện giữa hàng nghìn request, mình vẫn chưa truy được dấu vết.

Tập sau, mỗi request sẽ có một correlation ID đi xuyên toàn bộ log.

Nếu bạn muốn học những lỗi chỉ xuất hiện sau khi deploy, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Swagger mở auth routes; terminal bên cạnh tăng request login | 25s |
| 2 | [DIAGRAM] | So sánh validation với chiếc van rate limit | 25s |
| 3 | [BROWSER] | Threat-model bốn nhóm route; highlight đề xuất limit toàn cục quá thô | 30s |
| 4 | [IDE] | Cấu hình named throttlers và global `APP_GUARD` | 40s |
| 5 | [IDE] | Gắn `@Throttle()` riêng lên login; minh họa tracker IP/user | 35s |
| 6 | [DIAGRAM] | Reverse proxy, `trust proxy`, `req.ip`, storage dùng chung | 40s |
| 7 | [IDE] | Gắn Helmet trước route; cấu hình CSP vừa đủ cho Swagger | 35s |
| 8 | [TERM] | Chạy script spam; quay 200 chuyển thành 429 | 45s |
| 9 | [TERM] | Thử giả `X-Forwarded-For`, sửa cấu hình rồi chạy lại | 35s |
| 10 | [BROWSER] | Kiểm tra security headers và Swagger UI | 30s |
| 11 | [TERM] | Chạy test e2e cho login limit và task route | 25s |
| 12 | [B-ROLL] | Log 429 chạy nhanh, zoom vào việc thiếu dấu vết request | 20s |

**Tổng mục tiêu: 6 phút 25 giây.** Dùng One Dark Pro, font 18–20px, giữ terminal sạch và che IP/domain thật nếu cần.

### Code cốt lõi

```ts
ThrottlerModule.forRoot([
  { name: 'burst', ttl: 1_000, limit: 5 },
  { name: 'default', ttl: 60_000, limit: 100 },
]);

@Throttle({ burst: { limit: 3, ttl: 60_000 } })
@Post('login')
login(@Body() dto: LoginDto) {
  return this.authService.login(dto);
}
```

```ts
const app = await NestFactory.create(AppModule);
app.set('trust proxy', 'loopback'); // Phải khớp topology deploy thật.
app.use(helmet()); // Gắn trước các route/setup phụ thuộc middleware.
```

### Prompt cho AI

```text
Threat-model rate abuse for the current TaskFlow API before changing code.
- Separate login, refresh, public docs, authenticated reads and admin mutations.
- Propose named @nestjs/throttler policies with reasons, not one global number.
- Explain tracker choice before and after authentication.
- Account for the real reverse proxy topology and shared storage across replicas.
- Add Helmet before routes and keep Swagger CSP narrowly functional.
- Write an abuse script and e2e tests for 429 behavior and normal traffic.
- Do not claim rate limiting prevents distributed attacks.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right facing a dark monitor flooded by red login requests, a single glowing rate-limit barrier stopping them, deep black and navy background, NestJS red-pink #E0234E lighting, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of a dark API gateway represented as a metal valve controlling a stream of glowing request packets, developer silhouette on the right, NestJS red-pink #E0234E highlights, empty dark left side, high contrast, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer watching a terminal response change from green success lines to a bold red 429 signal, monitor-lit face on the right, black and dark navy setup, NestJS red-pink #E0234E rim light, empty left side, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Rate Limiting và Helmet: Dạy API tự vệ — EP18 | Lập trình là cuộc sống
2. JWT không chặn được bot spam login — EP18 | Lập trình là cuộc sống
3. Vì sao một Rate Limit cho mọi route là sai? — EP18 | Lập trình là cuộc sống
4. Chặn Brute Force trong NestJS đúng cách — EP18 | Lập trình là cuộc sống
5. API trả 429 trước khi production gục — EP18 | Lập trình là cuộc sống

**Khuyên dùng:** Title 2. A/B test Title 1 cho intent tìm kiếm.

### 4b. SEO Description

```text
JWT kiểm tra ai đang gọi. Nó không kiểm tra người đó gọi nhanh tới đâu. Tập 18 thêm rate limiting, Helmet và một trust boundary đúng cho production.

✅ Phân loại rủi ro theo từng route
✅ Cấu hình @nestjs/throttler với nhiều cửa sổ
✅ Siết login mà không bóp nghẹt GET task
✅ Xử lý IP thật sau reverse proxy
✅ Hiểu giới hạn của in-memory storage
✅ Bật Helmet và CSP vừa đủ cho Swagger
✅ Dùng script spam để kiểm chứng 429

🔗 NestJS Rate Limiting: https://docs.nestjs.com/security/rate-limiting
🔗 NestJS Helmet: https://docs.nestjs.com/security/helmet

⏱ 0:00 Swagger trở thành bản đồ cho bot
⏱ 0:40 Validation không giới hạn tần suất
⏱ 1:10 Threat model từng route
⏱ 1:45 ThrottlerModule và ThrottlerGuard
⏱ 2:35 IP, user và reverse proxy
⏱ 3:30 Helmet và CSP
⏱ 4:30 Spam test tới 429
⏱ 5:45 Giới hạn thật của rate limiting

#NestJS #RateLimiting #Helmet #APISecurity #BruteForce #TypeScript #Backend #Production #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs rate limiting, nestjs throttler, helmet nestjs, chống spam login nestjs, brute force protection api, 429 too many requests, throttle login nestjs, reverse proxy ip nestjs, trust proxy express, api security headers, swagger csp helmet, rate limit redis nestjs, nestjs production security, học nestjs bằng ai, nestjs tập 18, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `JWT VẪN` — WHITE `#FFFFFF`
- `CHƯA ĐỦ!` — NEST RED `#E0234E`
- Badge nhỏ: `EP 18`

### Option 2
- `BOT SPAM` — WHITE `#FFFFFF`
- `API TỰ CHẶN` — NEST RED `#E0234E`
- Badge nhỏ: `429`

### Option 3
- `DẠY API` — WHITE `#FFFFFF`
- `TỰ VỆ` — NEST RED `#E0234E`
- Badge nhỏ: `HELMET`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ một bản ảnh sạch không chữ và kiểm tra preview 320×180.
