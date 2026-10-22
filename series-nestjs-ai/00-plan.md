# Series Plan — "Học NestJS bằng AI" (29 tập + bonus, lane: Học lập trình bằng LLM)

- **Format:** 23 tập xây modular monolith, 6 tập Microservices, cộng các bonus xen giữa season khi một quyết định kỹ thuật xứng đáng có riêng một tập. Host tự quay màn hình + tự thoại âm.
- **Thời lượng:** EP01–EP04 giữ thời lượng thực tế đã quay. Các video chưa quay hướng tới 8–12 phút với khoảng 800–1100 từ thoại; chỉ dài hơn khi outcome không thể tách hợp lý.
- **Nguyên tắc tách tập:** Mỗi tập có một outcome chính và một pain nối sang tập sau. Nếu cần quá 18 phút để hoàn thành hai outcome độc lập, tách thành hai tập.
- **Technical baseline mở màn:** NestJS 12, Node.js `24.11+`, TypeScript `5.9+`, npm, ESM (`"type": "module"`) và PostgreSQL. Data layer dùng **Prisma ORM 8** với PSL contract; Node 24 nạp `temporal-polyfill/full/global` vì timestamp Prisma 8 là `Temporal.Instant`. Khi setup, luôn hiện phiên bản thực tế trên màn hình.
- **AI tool:** **Opus trong IDE Antigravity** (agent panel đọc codebase thật). Pattern: hỏi – đọc – chất vấn – verify.
- **Spine:** build MỘT project thật từ đầu đến cuối — **TaskFlow**, task manager API — từ folder rỗng đến modular monolith production, rồi tách sang Microservices có chủ đích. Phần nền tảng hoàn thiện User–Role–Permission trước khi đưa Tasks vào làm business feature đầu tiên.
- **Chain rule:** tập sau mở bằng NỖI ĐAU tập trước tạo ra (không phải "hôm nay ta học X"). Dưới đây mỗi tập ghi rõ "← pain" kế thừa.
- **Differentiator:** mỗi tập đúng MỘT AI sequence liền mạch — theo **AI-Driven Development Workflow 6 bước: Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng**. Không bao giờ copy-blind.

## Kỹ thuật sản xuất: "Narrate over the fast-forward"

> [!IMPORTANT]
> Thay đổi quan trọng nhất — **giải thích TRONG LÚC AI đang xử lý**, không giải thích TRƯỚC rồi mới prompt.

### Flow sản xuất chuẩn
```
Submit prompt → ĐỒNG THỜI giải thích concept (voice-over trên fast-forward) → Code trả về → Review diff
= Tối ưu thời lượng, không có dead time
```

### Nguyên tắc sắp xếp ý cho mỗi AI sequence

1. **Mở:** Nêu vấn đề + mô tả prompt sẽ gửi (1–2 câu)
2. **Submit prompt** → màn hình bắt đầu tua nhanh AI processing
3. **Voice-over trên fast-forward:** Giải thích concept/lý thuyết liên quan. Viewer thấy AI đang làm + nghe giải thích = hai kênh thông tin song song
4. **AI trả code** → dừng tua, review diff chi tiết
5. **Kiểm chứng:** chạy app/test, highlight kết quả

> [!TIP]
> Kỹ thuật này biến "thời gian chết" thành "thời gian học". Viewer không bao giờ thấy màn hình đứng yên.

## Mapping EP cũ → EP mới (49 → 29)

| EP mới | EP cũ gộp | Tên |
|---|---|---|
| 01 | 01 | NestJS từ con số 0 ✅ |
| 02 | 02 | Validation ✅ |
| 03 | 03 | Prisma 8 + PostgreSQL ✅ |
| 04 | 04 | Error Handling ✅ |
| 05 | 05 | JWT Auth: Register, Login, Guard |
| **06** | **06 (mở rộng)** | **AGENTS.md, Skills và MCP: Dạy AI nhớ project** |
| **07** | **07** | **Refresh Token: Gia hạn phiên, thu hồi session** |
| 08 | 08 + 09 | Role, Permission và quan hệ many-to-many |
| 09 | 10 + 11 | PermissionGuard + Ownership |
| 10 | 12 | Testing RBAC bằng Vitest |
| 11 | 13 + B13.5 + 14 | DRY, Abstraction và Common Library |
| B11.5 | mới | Bonus: Zod vs class-validator |
| 12 | 15 + 16 | Request Lifecycle + Docker Deploy |
| 13 | 17 + B17.5 | Swagger + REST vs GraphQL |
| 14 | 18 | Rate Limiting & Helmet |
| 15 | 19 + 20 + B20.5 | Logging, Tracing và Observability |
| 16 | 21 | File Upload |
| 17 | 22 + 23 | Pagination, Project và Label |
| 18 | 24 | Transactions |
| 19 | 25 + 26 | Redis Cache + Background Jobs |
| 20 | 27 + 28 + 29 | Cron + WebSocket + Socket Auth |
| 21 | 30 + 31 | WebSocket Scale + Soft Delete |
| 22 | 32 + 33 + B33.5 | API Versioning + Performance |
| 23 | 34 + 35 | CI/CD + Graceful Shutdown |
| 24 | 36 + 37 | Event-Driven + Monolith Recap |
| 25 | 38 | Monolith → Microservices |
| 26 | 39 + 40 | Message/Event + RabbitMQ |
| 27 | 41 + 42 | Idempotency + Outbox |
| 28 | 43 + 44 | gRPC + Distributed Tracing |
| 29 | 45 | Microservices Capstone |

### So sánh tổng thể

| | Gốc | Mới | Giảm |
|---|---|---|---|
| **Season 1** | 17 (16+1 bonus) | **11** | -6 |
| **Season 2** | 12 (10+2 bonus) | **8** | -4 |
| **Season 3** | 12 (11+1 bonus) | **5** | -7 |
| **Season 4** | 8 | **5** | -3 |
| **Tổng** | **49** | **29** | **-20 (-41%)** |

## Kiến trúc đích và luật dependency

Series xây một modular monolith theo business domain. `modules/` chứa nghiệp vụ; `common/`, `config/` và `database/` chứa các năng lực cross-cutting có thể tái sử dụng. Không tạo folder rỗng từ EP01: mỗi nhánh chỉ xuất hiện khi series thật sự cần đến nó.

```text
src/
├── main.ts
├── app.module.ts
├── prisma/
│   ├── contract.prisma
│   ├── contract.json
│   ├── contract.d.ts
│   └── db.ts
├── common/
│   ├── decorators/
│   ├── filters/
│   ├── guards/
│   ├── interceptors/
│   ├── pipes/
│   ├── constants/
│   └── utils/
├── config/
│   ├── app.config.ts
│   ├── database.config.ts
│   └── env.validation.ts
├── database/
│   ├── database.module.ts
│   ├── prisma.provider.ts
│   └── repositories/
└── modules/
    ├── users/
    ├── auth/
    ├── access-control/
    │   ├── roles/
    │   ├── permissions/
    │   ├── assignments/
    │   ├── decorators/
    │   ├── guards/
    │   └── types/
    └── tasks/
migrations/
└── app/
prisma.config.ts
```

Với Prisma 8, PSL source nằm ở `src/prisma/contract.prisma`; `contract.json` và `contract.d.ts` được emit, review và commit cùng code. `src/prisma/db.ts` tạo database facade. Nest provider và repository adapter nằm trong `src/database/`. Migration history nằm trong `migrations/app/`; config CLI nằm ở `prisma.config.ts`. Không dùng `schema.prisma`, `@prisma/client`, `prisma generate`, `prisma migrate dev`, `prisma migrate deploy` hay `PrismaClient` của Prisma 7.

Luật bắt buộc:

1. Chia module theo business domain, không chia toàn project theo loại file.
2. Dependency đi một chiều: controller → service/use-case → repository contract; database adapter implement contract, nhận Prisma 8 database facade qua DI token và được nối trong module.
3. Controller chỉ xử lý transport; business rule nằm ở service/use-case hoặc domain object.
4. `common/` không được import từ `modules/`, `config/` hay implementation database. Code thuộc riêng Auth, Users, Access Control hoặc Tasks phải ở lại module đó.
5. Chỉ đưa code vào `common/` khi nó có từ hai consumer trở lên, hoặc là boundary áp dụng cho toàn app như global pipe/filter/interceptor. Code phải độc lập với business domain. Khi cần dùng qua nhiều repo, nâng phần ổn định thành workspace library hoặc package riêng thay vì copy thủ công vô hạn.
6. `PermissionGuard`, `@RequirePermissions()` và cách tính quyền hiệu lực nằm trong `modules/access-control`, không đặt trong `common/`. Chúng là business policy, không phải utility dùng chung cho mọi dự án.
7. Business service của User, Role và Permission luôn explicit. Không tạo `CommonService<T>` chỉ vì các method CRUD có tên giống nhau; chỉ cân nhắc abstraction nhẹ ở persistence layer sau khi có duplication thật và test bảo vệ.

Lộ trình hình thành skeleton: EP01 tạo `modules/users`; EP02 bắt đầu boundary validation; EP03 thêm `src/config/`, `src/prisma/`, `src/database/`, `migrations/` và `prisma.config.ts`; EP04 thêm filter; EP05 thêm `modules/auth`; EP06 đóng gói convention thành AGENTS.md + Agent Skill + MCP; EP08 hoàn thiện `modules/access-control`; EP09 tạo `modules/tasks` với PermissionGuard + ownership; EP11 nâng phần portable khỏi `common`; EP12 thêm interceptor/pipe cross-cutting + Docker deploy.

## Baseline Prisma 8 và cổng kiểm tra trước khi quay

Series chọn Prisma 8 vì thời gian sản xuất kéo dài qua thời điểm GA dự kiến. Trong giai đoạn release candidate, khóa **exact version** của `prisma` và `@prisma/orm-postgres` trong `package.json`/lockfile; không ghi `@latest` vào script quay. Khi Prisma 8 stable, nâng có chủ đích trong một PR riêng và chạy lại toàn bộ integration/e2e test.

Trước mỗi tập có chạm database, host phải quay hoặc lưu lại kết quả:

```bash
node --version
npx tsc --version
npm view prisma dist-tags
npm ls prisma @prisma/orm-postgres @prisma/client
npx prisma --version
```

Điều kiện pass:

1. Node.js tối thiểu `22.18`; nếu dùng Node 24 thì tối thiểu `24.11`. Series chuẩn hóa Node `24.11+` để tránh lệch môi trường.
2. TypeScript tối thiểu `5.9`, project chạy ESM.
3. Trên Node 24, cài `temporal-polyfill` và import `temporal-polyfill/full/global` ở đầu `src/prisma/db.ts`; field cập nhật dùng `temporal.updatedAt()`, type runtime là `Temporal.Instant`.
4. Không có `@prisma/client` trong dependency tree của TaskFlow.
5. Mọi feature dùng trong tập phải có trong [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status). Không nhờ AI đoán API còn thiếu.
6. Query và command phải đối chiếu [Prisma 8 docs](https://www.prisma.io/docs/orm), không lấy snippet Prisma 6/7 từ search result.

Workflow database chuẩn của series:

```text
Sửa contract
→ prisma contract emit
→ prisma migration plan --name <ten>
→ host review migration.ts + ops.json + DDL preview
→ prisma db migrate --advance-ref db
→ prisma db verify
→ chạy integration/e2e test
```

Nguồn chuẩn: [Prisma 8 với NestJS](https://www.prisma.io/docs/guides/frameworks/nestjs), [chuyển từ Prisma 7 sang Prisma 8](https://www.prisma.io/docs/orm/coming-from-prisma-orm-7), [migration workflow](https://www.prisma.io/docs/orm/migrations/how-migrations-work) và [Prisma 8 trong Docker](https://www.prisma.io/docs/guides/deployment/docker).

---

## SEASON 1 — NỀN TẢNG (EP 01–11): từ số 0 đến API có xác thực, phân quyền và code organization

### Quy ước đóng gói để tăng click và giữ retention

- Tiêu đề mặc định nói rõ công nghệ và kết quả để người mới hiểu ngay nội dung sẽ học.
- Mỗi script có ba hướng A/B rõ ràng: keyword/search, outcome thực tế và insight/curiosity dễ hiểu.
- Số EP và branding đứng cuối để không che mất chủ đề trên màn hình nhỏ.
- Thumbnail chỉ dùng 2–4 từ lớn và bổ sung cho tiêu đề, không chép lại toàn bộ tiêu đề.
- 30 giây đầu phải chiếu đúng bằng chứng đã hứa: response sai, test xanh giả, dữ liệu mất hoặc deploy thất bại.
- Nhịp nội dung ưu tiên: lỗi thật → AI đề xuất → host bắt lỗi → sửa → kiểm chứng bằng request/test/diff.
- Không kéo video tới 15–20 phút bằng lý thuyết. Chỉ giữ cảnh giúp hiểu quyết định hoặc chứng minh code hoạt động.

### Visual identity thumbnail của series NestJS

**Chuyển đổi phong cách (từ EP04):** Thumbnail KHÔNG dùng nhân vật AI-generated. Phong cách code-centric: monitor/code/icons/badges trên nền dark, text lớn dễ đọc ở kích thước nhỏ 320×180. Lý do: thumbnail EP04 (code-only) có contrast mạnh hơn, text đọc được ở kích thước nhỏ, không bị "uncanny valley" của AI face. EP01–03 đã có bản v2 code-only trong assets để thay thế trên YouTube.

- Ảnh chuẩn tham chiếu mới: `04-error-handling-nestjs/assets/thumbnail-04-500-khong-phai-moi-loi.webp`.
- Bố cục: headline lớn bên trái (chiếm ~1/3 frame), visual elements (monitor, code, icons, status badges) chiếm phần còn lại. KHÔNG có nhân vật người.
- Màu chủ đạo: NEST RED `#E0234E`, WHITE `#FFFFFF`, đen và navy đậm. Không dùng xanh lá hoặc cyan cho headline và ánh sáng chính.
- Headline chính chỉ 2–4 từ lớn; số EP và badge phụ phải nhỏ hơn rõ rệt.
- Font condensed đậm, stroke đen và shadow gọn; không dùng neon glow dày.
- Mỗi EP chỉ thay nội dung headline và visual element trên monitor. Không thay visual grammar của cả series.
- Trước khi chốt, kiểm tra ảnh full-size và bản thu nhỏ `320×180`; dấu tiếng Việt phải chính xác.
- **Thumbnail v1 (có nhân vật) vẫn giữ lại trong assets để so sánh A/B nếu cần.**

### EP 01 — NestJS từ con số 0: Thực chiến cùng AI Mentor — ✅ Đã đăng (lần 2)
- **YouTube:** https://www.youtube.com/watch?v=p3LYkjwdlqg
- **Link cũ (đã xóa):** ~~https://www.youtube.com/watch?v=7lRvCk_CHLs~~
- **Ngày đăng:** 2026-09-24
- **Thời lượng thực tế:** 10:38
- ← pain: repo công ty lạ hoắc, tutorial 3h lỗi thời.
- Học: Nest CLI, luồng `main.ts → module → controller → service`, decorator, DI cơ bản và nguyên tắc module theo business domain.
- Cấu trúc đầu tiên: tạo `src/modules/users` bằng `nest g resource modules/users`; chưa tạo sẵn `common/`, `config/`, `database/` khi chưa có code thật.
- AI sequence: yêu cầu Users API in-memory → AI trình plan → host review/chất vấn → approve → AI thực hiện → host kiểm tra diff và chạy app.
- Host tự gõ: endpoint `GET /users/count`, đặt trước route động `GET /users/:id`.
- Thành quả: `POST /users` trả 201, `GET /users` thấy dữ liệu, `GET /users/count` trả đúng số lượng.
- → **pain mới:** gửi `{ "name": "Richard", "email": 123 }` vẫn được chấp nhận vì DTO chưa có validation runtime.
- File: `01-hoc-nestjs-voi-ai/01-nestjs-tu-0-cung-ai.md`

### EP 02 — Kiểm tra email và payload trong NestJS — ✅ Đã đăng (lần 2)
- **YouTube:** https://www.youtube.com/watch?v=k3vi2u-Xabw
- **Link cũ (đã xóa):** ~~https://www.youtube.com/watch?v=GCWSSb6-qhk~~
- **Ngày đăng:** 2026-09-25
- **Thời lượng thực tế:** 6:45
- ← pain: EP01 nhận payload gì cũng được — `email` là số hoặc sai định dạng vẫn thành user.
- Học: compile-time type khác runtime validation; class-validator, ValidationPipe toàn cục (`whitelist`, `forbidNonWhitelisted`, `transform`), `@IsString`, `@IsNotEmpty`, `@IsEmail`, custom message tiếng Việt.
- Cấu trúc mới: thêm `src/common/pipes/app-validation.pipe.ts`; pipe chỉ phụ thuộc Nest/class-validator, không import Users hay business domain.
- AI sequence: AI đề xuất rule + bộ payload fuzz → host review/approve → chạy từng payload → phát hiện chuỗi toàn dấu cách vẫn lọt → host tự thêm bước trim rồi kiểm chứng lại.
- Thành quả: POST bậy → 400 rõ ràng. → **pain: dù sao data vẫn nằm trong RAM.**
- File: `02-validation-nestjs/02-dto-validationpipe-nestjs.md`

### EP 03 — NestJS + Prisma 8: Lưu User vào PostgreSQL — ✅ Đã đăng
- **YouTube:** https://www.youtube.com/watch?v=kUXmQxjecNE
- **Ngày đăng:** 2026-09-19
- **Thời lượng thực tế:** 14:19
- ← pain: EP02 xong, restart server, dữ liệu bốc hơi.
- Học: khởi tạo Prisma 8 trong Nest app bằng `prisma orm init --target postgres --authoring psl`; phân biệt contract với database schema; emit contract; plan/review/apply migration; tạo `DatabaseModule`, Prisma provider, repository contract và Prisma adapter. Đồng thời dựng ConfigModule, Zod env validation và `.env.example` để cả Prisma CLI lẫn Nest runtime dùng một nguồn `DATABASE_URL` an toàn. Chỉ persist User, chưa tạo Tasks hay Access Control trong tập này.
- File sinh ra: `src/prisma/contract.prisma`, `contract.json`, `contract.d.ts`, `db.ts`, `prisma.config.ts` và `migrations/app/`; đồng thời thêm `src/config/app.config.ts`, `database.config.ts`, `env.validation.ts` và `.env.example`. Commit emitted contract artifacts và migration package.
- Dependency đích: `UsersController → UsersService/use-case → UsersRepository contract ← PrismaUsersRepository → Prisma 8 db facade`; business module không import `db.orm`, không phụ thuộc `@prisma/orm-postgres`.
- Query demo dùng API Prisma 8: `db.orm.public.User.create(...)`, `.where(...).first()` và `.all()`; không dùng `prisma.user.findMany()` của Prisma 7.
- Config chuẩn ngay từ đầu: `.env` bị ignore; `.env.example` chỉ có placeholder; Docker Compose lấy image/credential/database/host port qua required interpolation; Prisma CLI nạp env qua `prisma.config.ts`; Nest runtime nạp và validate qua ConfigModule; database factory nhận URL đã validate bằng DI. Các tập sau mở rộng cùng boundary cho JWT, Redis và dịch vụ ngoài.
- AI sequence: prompt 1 audit ENV và hardcode trong Docker Compose; prompt 2 cố ý thiếu context làm AI lấy nhầm snippet Prisma 7; prompt 3 dùng release status và docs Prisma 8 sửa plan trước khi code.
- Kiểm chứng bắt buộc: `contract emit` → `migration plan --name init` → review DDL → `db migrate --advance-ref db` → `db verify` → restart Nest app → user vẫn còn.
- Thành quả: restart, data còn nguyên. → **pain: trùng email → crash 500 xấu xí.**
- File: `03-prisma-postgresql/03-prisma-postgresql-bo-nho-that.md`

### EP 04 — Đừng biến mọi lỗi NestJS thành 500 | Error Handling — ✅ Đã đăng
- **YouTube:** https://www.youtube.com/watch?v=KwQ7Sr8727Y
- **Ngày đăng:** 2026-10-06
- **Thời lượng thực tế:** 7:58
- ← pain: EP03 unique constraint vi phạm → 500 stacktrace bắn ra client.
- Học: HttpException, NotFoundException/BadRequestException/ConflictException, 404 vs 400 vs 409, custom ExceptionFilter và structured error envelope của Prisma 8.
- Prisma 8 mapping: nhận diện error envelope bằng `isStructuredError` và `error.code` dạng namespace/subcode; unique violation của PostgreSQL được map bằng `sqlState` `23505`, không dùng error class/mã client cũ.
- AI moment: bảo AI liệt kê MỌI chỗ service có thể fail → học tư duy defensive.
- Thành quả: mọi lỗi trả JSON sạch, đúng status. → **pain: API ai gọi cũng được, không có cửa.**
- File: `04-error-handling-nestjs/04-error-handling-nestjs.md`

### EP 05 — JWT Authentication: Register, Login và AuthGuard
- ← pain: EP04 xong nhưng bất kỳ ai cũng đọc và sửa dữ liệu user.
- Học: register/login, bcrypt hash (tại sao không plaintext), JwtModule, AuthGuard, @CurrentUser, bảo vệ `/users/me`; mở rộng config boundary với JWT access secret/TTL có startup validation.
- AI moment: tranh luận với AI "tại sao không lưu JWT trong localStorage?" — security thinking.
- Thành quả: không token → 401; có token → đọc đúng hồ sơ của mình. → **pain: sắp tạo thêm Role và Permission, nhưng mỗi lần lại phải nhắc AI cùng convention. Cài mỗi tool AI tạo một file convention riêng.**
- File: `05-jwt-auth-nestjs/05-jwt-auth-nestjs.md`

### EP 06 — AGENTS.md, Skills và MCP: Dạy AI nhớ project ✅ script mới
- ← pain: mỗi tool AI đòi file convention riêng (CLAUDE.md, .cursorrules, copilot-instructions.md). Copy-paste qua lại, đổi convention file A quên cập nhật file B và C.
- Học 3 tầng context cho AI coding agent:
  - **Tầng 1 — AGENTS.md (Hot Memory):** file universal, mọi tool đều đọc. Chuẩn do Agentic AI Foundation (Linux Foundation) quản lý. Claude Code (v2.1.277+) fallback đọc AGENTS.md nếu không có CLAUDE.md. Cursor, Copilot, Windsurf, Kiro đều nhận.
  - **Tầng 2 — docs/ (Cold Memory):** architecture.md, database-schema.md — AI chỉ đọc khi chạm phần liên quan. Giữ AGENTS.md ngắn gọn (<150 dòng), tiết kiệm context window.
  - **Tầng 3 — Skills (On-demand workflow):** `.agents/skills/nest-feature/SKILL.md` đóng gói scaffold convention. Progressive disclosure — agent chỉ nạp instruction khi prompt khớp.
  - **MCP (Tool connectivity):** giới thiệu Model Context Protocol — "USB cho AI" kết nối database/API. Chỉ giới thiệu concept, chưa demo cài server.
- Bảng so sánh Agent Config trên màn hình: Claude Code, Cursor, Copilot, Windsurf, Kiro + file paths + AGENTS.md support status.
- AI sequence: tạo AGENTS.md + docs/ cho TaskFlow → tạo nest-feature skill → scaffold Roles/Permissions → verify skill chỉ kích hoạt đúng lúc.
- Kiểm chứng: prompt không liên quan (fix README typo) → skill không kích hoạt.
- Thành quả: convention sống trong repo, đổi tool vẫn giữ. AI biết kiến trúc trước khi viết dòng đầu tiên. → **pain: access token ngắn hạn làm phiên đăng nhập liên tục bị ngắt.**
- File: `06-agent-skill-nestjs/script.md`

### EP 07 — Refresh Token: Gia hạn đăng nhập và thu hồi phiên
- ← pain: access token ngắn hạn an toàn hơn, nhưng người dùng bị yêu cầu đăng nhập lại liên tục.
- Học: access/refresh flow, hash refresh token, rotation, reuse detection, revoke session và logout; thêm refresh TTL vào config đã validate, không tạo refresh JWT secret vì refresh token là opaque random value.
- AI moment: AI đề xuất lưu refresh token nguyên văn → host threat-model database leak rồi sửa thiết kế trước khi code.
- Thành quả: phiên có thể gia hạn, xoay vòng và thu hồi. → **pain: xác thực đã hoàn chỉnh nhưng mọi user vẫn có quyền như nhau.**
- File: `07-refresh-token-nestjs/07-refresh-token-rotation-nestjs.md`

### EP 08 — Role, Permission và quan hệ many-to-many *(gộp EP cũ 08+09)*
- ← pain: EP07 xác định được người gọi và phiên, nhưng chưa mô tả được họ được phép làm gì. Role và Permission tồn tại nhưng chưa gắn cho user hay cho nhau.
- Học: tạo `RolesModule` và `PermissionsModule`, repository contract/adapter, service nội bộ; `Role.name` và `Permission.code` duy nhất. Prisma 8 explicit many-to-many `UserRole` và `RolePermission`; composite key; `assignedAt`, `assignedBy`; seed `admin`, `member` và permission mẫu. Query relation bằng `.include(...)`.
- Permission code theo resource/action: `users.read`, `roles.assign`, `permissions.manage`, `tasks.create`.
- AI moment 1: dùng Agent Skill scaffold hai feature → AI đề xuất `CommonService<T>` → host từ chối. AI moment 2: AI đề xuất implicit many-to-many → host kiểm tra Prisma 8 relation limitations → chuyển sang explicit junction + transaction.
- Chưa expose controller quản trị trước PermissionGuard.
- Thành quả: database biểu diễn toàn bộ chính sách truy cập. Service nội bộ quản lý danh mục Role/Permission. → **pain: có dữ liệu quyền nhưng API vẫn chưa thực thi nó.**
- Ước lượng: ~2500 từ → 9–11 min
- Files gốc: `08-role-permission-nestjs/`, `09-user-role-permission-nestjs/`

### EP 09 — PermissionGuard + Ownership: Ai được làm gì trên dữ liệu nào? *(gộp EP cũ 10+11)*
- ← pain: EP08 có chính sách trong database nhưng route nào cũng chỉ kiểm tra đăng nhập. Và chưa có business feature thật để chứng minh RBAC dùng lại được.
- Học: authentication khác authorization; `@RequirePermissions()`; `PermissionGuard`; tính effective permissions. JWT chỉ giữ `sub`, không nhét permission. Tạo TasksModule theo convention; task có owner; controller mỏng; service giữ business rule; repository tách Prisma. Áp dụng `tasks.*` permissions; phân biệt có permission với có quyền trên đúng resource.
- `PermissionGuard` và decorator nằm trong `modules/access-control`, không trong `common/`.
- AI moment 1: AI dùng `@Roles('admin')` → host đổi sang permission claim. AI moment 2: AI chỉ kiểm tra `tasks.update` rồi cho sửa mọi task → host bổ sung ownership rule.
- Thành quả: thiếu quyền → 403; user chỉ thao tác task được phép và thuộc phạm vi của mình. → **pain: nhiều nhánh auth/permission/ownership quá, thử tay không còn đáng tin.**
- Ước lượng: ~2400 từ → 9–10 min
- Files gốc: `10-permission-guard-nestjs/`, `11-tasksmodule-nestjs/`

### EP 10 — Testing phân quyền bằng Vitest và Supertest
- ← pain: EP09 thay guard hoặc ownership rule là phải thử tay hàng loạt tài khoản và route.
- Học: Vitest unit test service/guard với mock (Nest CLI 12 scaffold sẵn vitest 4, `globals: true` — API tương thích Jest), e2e Supertest, database test riêng, đỏ→xanh; coverage là gì và không phải là gì.
- Ma trận bắt buộc: user không role; nhiều role; permission trùng qua hai role; revoke role; revoke permission; thiếu permission; ownership sai; direct ALLOW/DENY nếu bật override.
- AI moment: AI sinh test chỉ assert status chung chung → host mutation nhỏ vào guard để chứng minh test vẫn xanh, rồi viết lại assertion có giá trị.
- Thành quả: `test` và `test:e2e` bảo vệ luồng auth/RBAC/ownership. → **pain: duplication giữa ba feature bắt đầu rõ, rất dễ refactor quá tay.**
- File gốc: `12-testing-rbac-nestjs/`

### EP 11 — DRY, Abstraction và khi nào tách Common Library *(gộp EP cũ 13+B13.5+14)*
- ← pain: UsersService, RolesService và PermissionsService có nhiều method cùng tên, nhìn rất muốn gom thành `CommonService<T>`. Copy nguyên `common/` sang repo khác sẽ tạo nhiều bản lệch nhau.
- Học: duplicate code khác duplicate knowledge; YAGNI; abstraction boundary; khi nào repository generic nhẹ có ích. So sánh nhanh TypeORM entity với Prisma 8 contract (~2 min). Tách phần portable thành workspace library hoặc private package.
- AI sequence: AI giảm duplicate → tạo BaseCrudService → host dùng test chứng minh business rule khác nhau → loại bỏ. AI audit `common/` → lọc phần không phụ thuộc domain → host duyệt → tách library.
- Kiểm chứng: dùng library trong TaskFlow và một Nest app sạch; consumer build được.
- Thành quả: cross-cutting code ổn định có phiên bản; business policy vẫn thuộc project. → **pain: middleware, guard, pipe, filter và interceptor đã nhiều đến mức request lỗi không biết dừng ở lớp nào.**
- Ước lượng: ~2600 từ → 10–11 min
- Files gốc: `13-dry-abstraction-nestjs/`, `bonus-13-5-typeorm-nestjs/`, `14-common-library-nestjs/`

> [!NOTE]
> **Tổng Season 1:** 11 tập + bonus. Mỗi tập 8–12 min, đặc hơn.

### Bonus 11.5 — Zod vs class-validator: một nguồn sự thật cho validation
- **Vị trí:** xen giữa EP11 và EP12. Không renumber; tiêu đề đánh `NestJS #11.5:`. Pain mở phải khớp pain-đóng của EP11 (library tách ra nhưng validation pipe kéo theo dependency cũ) và pain-đóng phải nối sang pain mở EP12 (debug request qua nhiều layer) — bonus không phá chain 29 tập.
- ← pain: EP11 tách common library xong, phát hiện validation pipe kéo `class-validator` + `class-transformer` vào package dùng chung — mà `class-transformer` lần publish cuối là 22/11/2021 (verify trên npm registry 23/10/2026). Cùng lúc, env của app lại được validate bằng Zod từ EP03 (`env.validation.ts`) — TaskFlow đang có hai hệ validation song song.
- Học: một nguồn sự thật (schema Zod → `z.infer` ra type TS luôn, không viết interface + decorator riêng); error chi tiết có path + expected/received (`age: Expected number, received string`) so với custom message thủ công từng field; maintenance status hai library (có số npm trên màn hình); viết `ZodValidationPipe` (~vài chục dòng: `schema.parse` + map `ZodError` → `BadRequestException`); demo swap đúng MỘT endpoint (POST /tasks) — phần còn lại giữ class-validator.
- AI moment: nhờ AI plan swap Zod cho một endpoint → AI đề xuất rewrite toàn bộ DTO trong một sweep → host từ chối: dự án đang chạy ngon thì không migrate cho mệt, YAGNI, incremental. Đúng format "host bắt AI quá tay".
- Giá phải trả (nói thẳng trong video): mất Swagger auto-gen từ decorator → cần `nestjs-zod` hoặc `zod-openapi` (và phải đợi tới EP13 mới thấy trên màn hình, tập đó vẫn dùng class-validator — không retrofit). Tài liệu NestJS chính thống viết theo class-validator → team toàn junior thì tra cứu nhanh hơn với class-validator.
- Kiểm chứng 30s đầu: gửi payload sai, đặt error Zod và error class-validator cạnh nhau trên màn hình.
- Thành quả: endpoint demo có schema + type từ một khai báo; quyết định "mới thì Zod, cũ đang ngon thì giữ" có rationale. → pain-đóng không tạo pain mới cho EP12 (bonus off-chain).
- Ước lượng: ~1500 từ → 6–8 min
- File: `bonus-11-5-zod-validation/script.md`

---

## SEASON 2 — PRODUCTION (EP 12–19): deploy và vận hành

### EP 12 — Request Lifecycle + Docker Deploy *(gộp EP cũ 15+16)*
- ← pain: EP11 đã có nhiều cross-cutting layer nhưng debug request vẫn như lần trong mê cung. Và 11 tập trước vẫn chỉ chạy localhost.
- Học: thứ tự middleware → guard → interceptor → pipe → handler, logging interceptor, transform response. Dockerfile Node 24, docker-compose kèm PostgreSQL, commit contract artifacts + migrations, migration gate Prisma 8.
- AI moment 1: AI vẽ sequence diagram lifecycle → host đối chiếu với log thật. AI moment 2: AI dùng Dockerfile Prisma cũ → host đối chiếu guide Prisma 8. Season 1 recap.
- Thành quả: public URL, nhìn log biết request dừng ở đâu. → **pain: API công khai mà không có tài liệu — ai biết gọi thế nào.**
- Ước lượng: ~2200 từ → 9–10 min
- Files gốc: `15-request-lifecycle-nestjs/`, `16-docker-deploy-nestjs/`

### EP 13 — Swagger + REST vs GraphQL: API tự viết hồ sơ *(gộp EP cũ 17+B17.5)*
- ← pain: EP12 public xong, người dùng cứ hỏi endpoint nhận gì và cần permission nào. REST client phải gọi nhiều endpoint để ghép một màn hình.
- Học: `@nestjs/swagger`, `@ApiTags`, bearer auth, annotate DTO. `@nestjs/graphql` code-first, resolver là transport boundary, reuse service; guard với GraphQL execution context.
- AI moment: AI annotate controller → host rà annotation nào khác code. AI copy logic sang resolver → host kéo về service.
- Thành quả: `/docs` mô tả API + hiểu GraphQL mà không biến series thành course GraphQL khác. → **pain: docs công khai trở thành bản đồ cho bot spam.**
- Ước lượng: ~2400 từ → 9–10 min
- Files gốc: `17-swagger-openapi-nestjs/`, `bonus-17-5-rest-vs-graphql-nestjs/`

### EP 14 — Rate Limiting & Helmet: dạy API tự vệ
- ← pain: docs công khai trở thành bản đồ cho bot spam login và API quản trị.
- Học: `@nestjs/throttler`, giới hạn theo IP/user/route, Helmet, bảo vệ login khác endpoint thường.
- AI moment: AI viết script spam chính API → host quan sát 429 rồi chất vấn cách attacker đổi IP.
- Thành quả: spam bị giới hạn, security headers bật đủ. → **pain: bị spam nhưng log rời rạc, không truy nổi một request.**
- File gốc: `18-rate-limiting-helmet-nestjs/`

### EP 15 — Logging, Tracing và Observability *(gộp EP cũ 19+20+B20.5)*
- ← pain: EP14 xảy ra lỗi lúc 2h sáng — hàng nghìn dòng log không biết dòng nào cùng request. Log cho biết có lỗi nhưng không chỉ ra method nào đang chậm.
- Học: pino structured logging, correlation ID, redaction; `@nestjs/observe`, auto-instrument, trace waterfall, latency p95; so sánh nhanh Sentry/OTel (decision matrix, không cài ba stack).
- AI moment: cho AI đọc log rối → host kiểm tra theo correlation ID. Tạo endpoint chậm → AI phân tích telemetry → host verify span.
- Thành quả: chẩn đoán dựa trên telemetry, một request có một dấu vết đầu cuối. → **pain: user báo lỗi task nhưng không gắn được ảnh minh họa.**
- Ước lượng: ~3000 từ → 11–13 min (video dài nhất season, packed)
- Files gốc: `19-structured-logging-correlation-id/`, `20-nestjs-observe/`, `bonus-20-5-observability-tools/`

### EP 16 — File upload: avatar và attachment cho task
- ← pain: EP15 thấy lỗi rõ rồi, nhưng task vẫn không đính kèm được ảnh hoặc file.
- Học: Multer, `@UploadedFile`, validate loại/dung lượng, local vs object storage, serve file an toàn.
- AI moment: hỏi AI nếu file giả danh `.jpg` thì sao → học magic bytes, không tin extension.
- Thành quả: task có attachment hợp lệ. → **pain: dữ liệu và file tăng, GET `/tasks` trả hàng nghìn dòng.**
- File gốc: `21-file-upload-nestjs/`

### EP 17 — Pagination, Project và Label *(gộp EP cũ 22+23)*
- ← pain: task 5 nghìn dòng làm response lớn và client treo. Task vẫn là danh sách phẳng, chưa nhóm theo dự án.
- Học: offset vs cursor, query filter, sort, metadata page; Prisma 8 cursor ổn định. Quan hệ 1–N, N–N, migration khi đã có data, module Project/Label.
- AI moment: chất vấn offset pagination khi data chèn liên tục → hiểu cursor. AI thiết kế schema → host chất vấn cascade hay restrict.
- Thành quả: task thuộc project, gắn nhiều label, tải theo phần. → **pain: tạo task kèm label hỏng giữa chừng làm data lệch.**
- Ước lượng: ~2600 từ → 10–11 min
- Files gốc: `22-pagination-filtering-sorting/`, `23-project-label-relations/`

### EP 18 — Transactions: làm trọn vẹn hoặc không làm
- ← pain: EP17 tạo task xong nhưng attach label fail, hệ thống còn nửa trạng thái.
- Học: Prisma 8 `db.transaction(async tx => ...)`, query qua `tx.orm`, rollback khi callback throw, transaction boundary, race condition. Không dạy `$transaction` của Prisma 7.
- AI moment: AI dựng hai request chạy đồng thời → host chạy demo và quan sát dữ liệu lệch trước khi sửa.
- Thành quả: hoặc toàn bộ thành công, hoặc quay về như chưa có gì. → **pain: dashboard join nhiều bảng, gọi liên tục làm DB nặng.**
- File gốc: `24-transactions-prisma8/`

### EP 19 — Redis Cache + Background Jobs *(gộp EP cũ 25+26)*
- ← pain: EP18 đúng dữ liệu nhưng dashboard query nặng lặp lại. Gửi mail trong request bị phụ thuộc mail server.
- Học: cache-aside, key design, invalidation khi data/quyền đổi, TTL. BullMQ + Redis, retry/backoff, failed job, dead-letter strategy, idempotent job cơ bản.
- AI moment 1: tạo bug quyền cũ còn trong cache → sửa invalidation. AI moment 2: tắt mail server → quan sát retry.
- Thành quả: dashboard nhanh hơn, response về ngay, mail chạy nền. Recap Season 2. → **pain: queue có worker nhưng chưa ai tạo job nhắc việc mỗi sáng.**
- Ước lượng: ~2600 từ → 10–11 min
- Files gốc: `25-redis-cache-nestjs/`, `26-bullmq-background-jobs/`

> [!NOTE]
> **Tổng Season 2:** 8 tập. Mỗi tập 8–13 min.

---

## SEASON 3 — CHUYÊN SÂU (EP 20–24): modular monolith thực thụ

### EP 20 — Cron + WebSocket + Socket Auth *(gộp EP cũ 27+28+29)*
- ← pain: EP19 queue chỉ chạy khi có producer; nhắc deadline cần quét mỗi sáng. Trình duyệt vẫn phải refresh. Socket mở nhưng lộ dữ liệu.
- Học: `@nestjs/schedule`, `@Cron`, distributed lock cơ bản. Socket.IO gateway, emit event, reconnect. JWT handshake, reuse auth service, room per user/project, permission khi join room.
- AI moment: AI sinh gateway → host chất vấn client mất mạng. Kết nối bằng token hết hạn → AI review flow.
- Thành quả: lịch tự tạo job, task mới hiện realtime, mỗi user chỉ nhận event được phép. → **pain: chạy nhiều server thì room nằm rải rác. User lỡ xóa task thì mất trắng.**
- Ước lượng: ~2800 từ → 10–12 min

### EP 21 — WebSocket Scale + Soft Delete *(gộp EP cũ 30+31)*
- ← pain: multi-instance room bị rời. User xóa task mất trắng, không truy được ai làm.
- Học: Socket.IO Redis adapter, pub/sub giữa instance, sticky session. Soft delete `deletedAt`, filter mặc định, restore, audit actor/action/time.
- AI moment: AI đề xuất log mọi field → host cắt dữ liệu nhạy cảm.
- Thành quả: không mất kết nối, không mất dữ liệu, có dấu vết. → **pain: thêm field mới làm client cũ vỡ contract. Endpoint chậm.**
- Ước lượng: ~2400 từ → 9–10 min

### EP 22 — API Versioning + Performance *(gộp EP cũ 32+33+B33.5)*
- ← pain: EP21 đổi response shape làm app cũ parse lỗi. Một số endpoint chậm dần.
- Học: URI versioning, deprecation, compatibility window, contract test. Query log/trace, N+1, index, `EXPLAIN`, đo before/after. GraphQL N+1 + DataLoader (~2 min).
- AI moment: AI đề xuất v2 → host duyệt breaking change. AI nhìn telemetry đoán bottleneck → host verify bằng query plan.
- Thành quả: v1 v2 sống chung, endpoint chậm nhất cải thiện có số đo. → **pain: push vẫn test build deploy bằng tay.**
- Ước lượng: ~2600 từ → 10–11 min

### EP 23 — CI/CD + Graceful Shutdown *(gộp EP cũ 34+35)*
- ← pain: code nhanh hơn nhưng push vẫn manual test/build/deploy. Rollout đang có traffic làm request đứt.
- Học: GitHub Actions workflow YAML, test matrix, build image, deploy khi merge, branch protection. Liveness/readiness, SIGTERM, connection draining, graceful shutdown.
- AI moment: AI viết workflow → host đọc step xóa thừa. AI kể timeline shutdown → host đối chiếu log.
- Thành quả: push → test → deploy, deploy không rơi request. → **pain: thêm listener mail/notification vẫn phải sửa service trung tâm.**
- Ước lượng: ~2400 từ → 9–10 min

### EP 24 — Event-Driven + Modular Monolith Recap *(gộp EP cũ 36+37)*
- ← pain: TasksService trở thành file nóng vì mail, audit, notification cùng bám vào nó. 24 tập nhiều khái niệm, cần bản đồ.
- Học: domain event trong monolith, `TaskCompleted`, listener, eventual side effect, failure boundary. Vẽ lại TaskFlow, dependency direction, auth/RBAC, production stack, câu hỏi phỏng vấn.
- AI moment: thêm tính năng điểm thưởng bằng listener không sửa use case. AI đóng vai interviewer → host trả lời bằng trade-off đã implement.
- Thành quả: modular monolith hoàn chỉnh, có lý do rõ ràng nếu muốn tách service. → **pain: notification workload ảnh hưởng API chính.**
- Ước lượng: ~2600 từ → 10–11 min

> [!NOTE]
> **Tổng Season 3:** 5 tập. Mỗi tập 9–12 min.

---

## SEASON 4 — MICROSERVICES (EP 25–29): chỉ tách khi monolith có lý do để tách

### EP 25 — Monolith → Microservices: khi nào nên tách?
- ← pain: notification workload ảnh hưởng API nhưng không muốn chia service theo cảm tính.
- Học: service boundary, ownership dữ liệu, operational cost, modular monolith vs distributed system.
- AI moment: AI đề xuất tách mọi module → host dùng coupling và failure data để chỉ chọn Notification Service.
- Thành quả: có boundary và lý do đo được. → **pain: hai service cần giao tiếp nhưng chưa biết dùng message hay event.**

### EP 26 — Message/Event + RabbitMQ *(gộp EP cũ 39+40)*
- ← pain: API cần gửi lệnh và nhận kết quả, trong khi TaskCompleted chỉ cần thông báo. Message đã gửi nhưng worker crash.
- Học: request-response vs event-based, timeout, transport abstraction. Broker, durable message, manual ACK/NACK, retry/backoff, DLQ, poison message.
- AI moment: AI dùng event cho câu hỏi cần response → host dựng failure. Kill consumer giữa xử lý → quan sát redelivery.
- Thành quả: chọn đúng communication style, message không biến mất. → **pain: retry có thể chạy business action hai lần.**
- Ước lượng: ~2600 từ → 10–11 min

### EP 27 — Idempotency + Outbox Pattern *(gộp EP cũ 41+42)*
- ← pain: RabbitMQ redelivery làm email lặp. Task commit DB nhưng event có thể fail.
- Học: idempotency key, inbox/deduplication record, unique constraint. Dual-write problem, outbox record trong cùng transaction, relay worker.
- AI moment: phát message hai lần → chỉ một side effect. Ngắt broker giữa commit → verify outbox phục hồi.
- Thành quả: at-least-once delivery không phá data; state và event không lệch. → **pain: không phải mọi giao tiếp service phù hợp asynchronous.**
- Ước lượng: ~2400 từ → 9–10 min

### EP 28 — gRPC + Distributed Tracing *(gộp EP cũ 43+44)*
- ← pain: API cần dữ liệu đồng bộ từ service khác với contract chặt và latency thấp. Request đi qua nhiều service, trace ID bị đứt.
- Học: protobuf, unary call, deadline, error mapping, schema evolution. Propagation qua HTTP/gRPC/microservice transport, trace waterfall, slow span.
- AI moment: AI thay REST bằng gRPC mọi nơi → host đo trade-off. AI đọc trace khoanh vùng service chậm → host verify bằng span.
- Thành quả: synchronous rõ ràng + nhìn hành trình xuyên service. → **pain: hệ thống phân tán nhưng thiếu kiểm chứng production toàn diện.**
- Ước lượng: ~2600 từ → 10–11 min

### EP 29 — Microservices Production Capstone
- ← pain: từng pattern chạy riêng, chưa biết hệ thống chịu deploy, retry và service failure đồng thời ra sao.
- Học: health/readiness, deploy order, backward-compatible contract, failure drill, runbook và cost review.
- AI moment: AI đóng vai incident commander trên sự cố dựng sẵn → host yêu cầu evidence trước mỗi hành động.
- Thành quả: TaskFlow distributed chạy end-to-end và người học hiểu cả giá phải trả của Microservices.

> [!NOTE]
> **Tổng Season 4:** 5 tập.

---

## Nguyên tắc xuyên suốt series

1. Mỗi ep mở bằng NỖI ĐAU của ep trước (chain rule) — không bao giờ mở bằng "hôm nay ta học X".
2. Mỗi ep có đúng MỘT AI sequence liền mạch — có thể gồm vài lượt hỏi–đáp nhưng chỉ phục vụ một outcome, không biến thành màn trình diễn nhiều tính năng AI.
3. **AI-Driven Development Workflow (quy trình chuẩn 6 bước, xuyên suốt mọi ep):** (1) Yêu cầu — mô tả mục tiêu + context → (2) AI lên Plan → (3) host Review bằng mắt → (4) host Approve → (5) AI Thực hiện code → (6) Kiểm chứng (git diff / test / chạy app). AI không bao giờ tự ý sửa.
4. Host luôn TỰ GÕ lại ít nhất một đoạn code AI sinh trong mỗi ep — điều kiện để gọi là "mình hiểu".
5. Kết mỗi ep teaser 1 câu cho ep sau (retention loop + minh bạch chain).
6. Tool AI: **Opus trong IDE Antigravity**. Đổi tool thì giữ nguyên pattern hỏi–đọc–chất vấn.
7. Mỗi season có điểm tổng kết rõ: EP12 recap nền tảng + deploy, EP19 recap production, EP24 tổng kết modular monolith và EP29 là microservices capstone.
8. Title mọi tập đánh số series: `NestJS #NN: <hook>`.
9. **Narrate over the fast-forward:** mọi script phải sắp xếp giải thích concept TRONG LÚC AI đang xử lý, không có dead time trên màn hình.
