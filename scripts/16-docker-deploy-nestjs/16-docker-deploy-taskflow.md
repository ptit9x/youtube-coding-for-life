# NestJS #16 — Docker và Deploy NestJS lên Production

- **Series:** Học NestJS bằng AI — tập 16/45, kết Season 1
- **Target runtime:** ~15 phút
- **Outcome:** Container production, PostgreSQL local, migration deploy và public health check.
- **Pain mở Season 2:** API đã public nhưng chưa có tài liệu cho người sử dụng.

---

## PART 1 — SCRIPT

TaskFlow đã có auth, RBAC, ownership, test và config.

Mình gửi repo cho một người khác. Họ thiếu đúng phiên bản Node và PostgreSQL.

Ứng dụng không khởi động.

Mười lăm tập code vẫn chỉ hoạt động trên máy mình.

Tập cuối Season 1 phải biến repo này thành một cách chạy lặp lại được.

API sẽ được đóng gói bằng Docker và chạy từ một public URL.

Dockerfile là công thức. Image là gói bất biến được build từ công thức đó.

Container là một process đang chạy từ image.

Database không nên nằm chung container với API.

Compose giúp chạy hai service và nối chúng bằng network.

Named volume giữ dữ liệu PostgreSQL khi container database được tạo lại.

Hiểu ba khái niệm này trước khi copy Dockerfile từ AI.

Mình yêu cầu AI giải thích từng layer trước khi viết.

Build stage cài dependency, generate Prisma Client và compile TypeScript.

Runtime stage chỉ nhận artifact cùng dependency cần thiết.

Dockerfile có hai stage. Build stage cài dependency, generate Prisma Client và compile TypeScript.

Runtime stage chỉ nhận `node_modules` đã prune, thư mục `dist`, Prisma schema và package metadata.

Multi-stage tách công cụ build khỏi runtime image.

`.dockerignore` loại `.env`, Git metadata và `node_modules` local.

Development cần một lệnh để chạy cả API và database.

Compose định nghĩa service API và PostgreSQL. API chỉ khởi động sau khi healthcheck database thành công.

Hostname database là `db`, không phải `localhost` bên trong API container.

Đây là lỗi demo rất đáng giữ lại trong video.

Schema production phải đi theo migration history đã commit.

Với phiên bản Prisma đã pin trong series, release chạy migration command tương ứng.

Release chạy `npx prisma migrate deploy`.

Không chạy `migrate dev` trong production.

Không dùng `db push` như quy trình deploy chính thức.

Migration nên chạy trong release job hoặc pipeline trước khi mở phiên bản mới.

Nếu migration lỗi, deploy phải dừng thay vì chạy code trên schema cũ.

Mình chọn Render cho demo, nhưng quy trình áp dụng được cho Railway.

Nền tảng build từ Dockerfile và cấp PostgreSQL riêng.

Mình cấu hình `DATABASE_URL`, JWT access secret, access TTL, refresh TTL và `NODE_ENV` trên dashboard.

Không truyền secret bằng Docker build argument.

Nest phải lắng nghe `0.0.0.0` và port do môi trường cung cấp.

Nest lắng nghe `0.0.0.0` trên port do môi trường cung cấp.

Endpoint `/health` giúp nền tảng biết ứng dụng đã sẵn sàng.

Build hoàn tất. Migration chạy thành công. Health check chuyển sang màu xanh.

Mình gọi public URL và đăng ký một user mới.

Login trả token. User tạo task và chỉ đọc task của mình.

Chúng ta bắt đầu Season 1 bằng một mảng dữ liệu trong RAM.

Bây giờ, TaskFlow có PostgreSQL, auth, refresh rotation, RBAC và ownership.

AI đã scaffold, review và gợi ý. Con người vẫn quyết định boundary cùng business rule.

API đã public, nhưng người khác chưa biết endpoint nhận gì.

Season 2 sẽ bắt đầu bằng Swagger và một API tự mô tả.

Nếu bạn đã đi đến đây, hãy thử deploy bằng chính domain của mình.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERMINAL] | Máy khác thiếu Node và PostgreSQL | 40s |
| 2 | [DIAGRAM] | Dockerfile, image và container | 60s |
| 3 | [AI] | Yêu cầu giải thích từng Docker layer | 55s |
| 4 | [IDE] | Viết Dockerfile multi-stage và `.dockerignore` | 110s |
| 5 | [TERMINAL] | Build image và kiểm tra runtime | 75s |
| 6 | [IDE] | Compose API cùng PostgreSQL health check | 100s |
| 7 | [TERMINAL] | Sửa lỗi dùng localhost trong container | 60s |
| 8 | [DIAGRAM] | Migration trong release pipeline | 65s |
| 9 | [BROWSER] | Cấu hình service, database và environment | 90s |
| 10 | [BROWSER] | Health check và public API thành công | 80s |
| 11 | [MONTAGE] | Recap EP01 tới EP16 | 70s |
| 12 | [B-ROLL] | Swagger mở Season 2 | 25s |

**Tổng: 830 giây ≈ 13:50.** Che URL database và secret; font terminal tối thiểu 18px.

### Code cốt lõi

```dockerfile
FROM node:22-bookworm-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npx prisma generate && npm run build && npm prune --omit=dev

FROM node:22-bookworm-slim AS runtime
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY --from=build /app/prisma ./prisma
USER node
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

```dockerignore
node_modules
dist
.git
.env
.env.*
!.env.example
coverage
```

### Prompt cho AI

```text
Plan a production Docker deployment for the current NestJS and Prisma project.
- Explain every Dockerfile layer before writing it.
- Use a multi-stage build and a non-root runtime user.
- Never copy .env or secrets into the image.
- Add Compose with PostgreSQL and health checks for local verification.
- Use committed migrations through the pinned Prisma production command.
- Bind Nest to 0.0.0.0 and the environment PORT.
- Add a health endpoint and a rollback checklist.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic Docker container launching a glowing NestJS API from a laptop into a cloud data center, PostgreSQL cylinder beside it, dark blue atmosphere, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic developer watching a deployment health check turn green above a public API endpoint, dark terminal reflections, neon green light, 16:9, photorealistic, no text.`
3. `A cinematic journey from localhost on the left to production cloud servers on the right, connected by a glowing container, dark code environment, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Docker và Deploy NestJS lên Production — EP16 | Lập trình là cuộc sống
2. Viết Dockerfile multi-stage cho NestJS và Prisma — EP16 | Lập trình là cuộc sống
3. Chạy NestJS và PostgreSQL bằng Docker Compose — EP16 | Lập trình là cuộc sống
4. Chạy Prisma Migration khi deploy production — EP16 | Lập trình là cuộc sống
5. Đưa API NestJS từ localhost lên public URL — EP16 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho Dockerfile và Title 5 cho outcome deploy.

### 4b. SEO Description

```text
Mười lăm tập code vẫn chỉ chạy trên máy mình. Tập kết Season 1 đóng gói TaskFlow bằng Docker và đưa API lên public URL.

✅ Phân biệt Dockerfile, image và container
✅ Viết Dockerfile multi-stage
✅ Chạy API cùng PostgreSQL bằng Compose
✅ Không đưa secret vào image
✅ Chạy production migration an toàn
✅ Cấu hình port, health check và public service
✅ Recap toàn bộ kiến trúc Season 1

🔗 Docker multi-stage builds: https://docs.docker.com/build/building/multi-stage/
🔗 Prisma production migrations: https://docs.prisma.io/docs/cli/migrate/deploy
🔗 Render Docker deployment: https://render.com/docs/docker

⏱ 0:00 Máy tôi chạy được
⏱ 1:10 Image và container
⏱ 2:45 Dockerfile multi-stage
⏱ 5:20 Compose với PostgreSQL
⏱ 7:50 Migration production
⏱ 9:45 Deploy lên cloud
⏱ 12:00 Public URL
⏱ 13:10 Recap Season 1

#NestJS #Docker #Prisma #PostgreSQL #Deployment #DevOps #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs docker, deploy nestjs, dockerfile nestjs prisma, docker compose postgresql, prisma migrate deploy, nestjs render deploy, railway nestjs deploy, multi stage docker nodejs, production nestjs, nestjs tiếng việt, nestjs tập 16, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `TỪ LOCALHOST` — WHITE
- `LÊN PRODUCTION` — NEON GREEN `#00FF41`
### Option 2
- `MÁY TÔI CHẠY` — WHITE
- `CHƯA ĐỦ!` — RED `#FF3B30`
### Option 3
- `NESTJS + DOCKER` — NEON GREEN `#00FF41`
- `DEPLOY THẬT` — WHITE

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
