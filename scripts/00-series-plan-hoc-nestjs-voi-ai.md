# Series Plan — "Học NestJS bằng AI" (46 tập chính + bonus, lane: Học lập trình bằng LLM)

- **Format:** 38 tập xây modular monolith, 8 tập Microservices và các tập bonus rẽ sang stack khác. Host tự quay màn hình + tự thoại âm.
- **Thời lượng:** Phần lớn 10–15 phút. Tập concept 8–11 phút; tập implementation phức tạp 14–18 phút. Không kéo dài chỉ để chạm mốc thời lượng.
- **Nguyên tắc tách tập:** Mỗi tập có một outcome chính và một pain nối sang tập sau. Nếu cần quá 18 phút để hoàn thành hai outcome độc lập, tách thành hai tập.
- **Technical baseline mở màn:** NestJS 12, Node.js `24.11+`, TypeScript `5.9+`, npm, ESM (`"type": "module"`) và PostgreSQL. Data layer dùng **Prisma ORM 8** với PSL contract; Node 24 nạp `temporal-polyfill/full/global` vì timestamp Prisma 8 là `Temporal.Instant`. Khi setup, luôn hiện phiên bản thực tế trên màn hình.
- **AI tool:** **Opus trong IDE Antigravity** (agent panel đọc codebase thật). Pattern: hỏi – đọc – chất vấn – verify.
- **Spine:** build MỘT project thật từ đầu đến cuối — **TaskFlow**, task manager API — từ folder rỗng đến modular monolith production, rồi tách sang Microservices có chủ đích. Phần nền tảng hoàn thiện User–Role–Permission trước khi đưa Tasks vào làm business feature đầu tiên.
- **Chain rule:** tập sau mở bằng NỖI ĐAU tập trước tạo ra (không phải "hôm nay ta học X"). Dưới đây mỗi tập ghi rõ "← pain" kế thừa.
- **Differentiator:** mỗi tập đúng MỘT AI sequence liền mạch — theo **AI-Driven Development Workflow 6 bước: Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng**. Không bao giờ copy-blind.

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

Lộ trình hình thành skeleton: EP01 tạo `modules/users`; EP02 bắt đầu boundary validation; EP03 thêm `src/prisma/`, `src/database/`, `migrations/` và `prisma.config.ts`; EP04 thêm filter; EP05 thêm `modules/auth`; EP06 đóng gói convention thành Agent Skill; EP08–10 hoàn thiện `modules/access-control`; EP11 tạo `modules/tasks`; EP14 nâng phần portable khỏi `common`; EP15 hoàn thiện `config/`; EP16 thêm interceptor/pipe cross-cutting.

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

### Backlog bắt buộc trước khi quay các script đã viết

Đổi plan không tự làm các script cũ tương thích. Các file dưới đây chưa được coi là sẵn sàng quay cho đến khi hoàn thành migration:

| Mức | Script | Việc phải đổi |
|---|---|---|
| Hoàn tất | `03-prisma-postgresql/03-prisma-postgresql-bo-nho-that.md` | Đã viết lại setup, contract, query API, DI provider, migration workflow và source map cho Prisma 8 |
| Blocker | `04-error-handling-nestjs/04-error-handling-nestjs.md` | Bỏ `P2002`; dùng Prisma 8 structured error code và `isStructuredError` |
| Blocker | `12-testing-rbac-nestjs/12-testing-ma-tran-rbac-ownership.md` | Đổi direct `prisma.task...` sang Prisma 8 facade hoặc test repository contract |
| Blocker | `17-docker-deploy-nestjs/17-docker-deploy-taskflow.md` | Bỏ `generate`/`migrate deploy`; đóng gói emitted contract và chạy migration gate Prisma 8 |
| Cần viết lại demo | `09-user-role-permission-nestjs/09-user-role-permission-many-to-many.md` | Dùng explicit junction, `.include(...)`, direct junction writes và `db.transaction(...)` |
| Cần cập nhật convention | `06-agent-skill-nestjs/06-agent-skill-nestjs.md` | Skill phải cấm Prisma 7 snippet và buộc đọc release status/Prisma 8 skill |
| Cần cập nhật so sánh | `bonus-13-5-typeorm-nestjs/bonus-13-5-prisma-vs-typeorm-inheritance.md` | So TypeORM entity với Prisma 8 contract/query facade, không so với Prisma Client cũ |
| Audit thuật ngữ | EP02, EP07, EP08, EP10, EP11, EP15 | Thay các mô tả chung gây hiểu nhầm về schema/client/migration Prisma 7 nếu có |

Definition of done cho từng script migrated:

1. `rg` không còn API Prisma 7 ngoài đoạn cố ý minh họa “AI làm sai”.
2. Mọi đoạn “AI làm sai” phải được gắn nhãn và sửa ngay trong cùng Short/tập.
3. Demo chạy trên PostgreSQL thật với exact package versions đã khóa.
4. `contract emit`, `migration check`, `db verify`, unit test và e2e test đều pass.
5. Source link của tập trỏ đến Prisma 8 docs, không trỏ mặc định vào docs Prisma 6/7.

## SEASON 1 — NỀN TẢNG (EP 01–17): từ số 0 đến API có xác thực và phân quyền

### Quy ước đóng gói để tăng click và giữ retention

- Tiêu đề mặc định nói rõ công nghệ và kết quả để người mới hiểu ngay nội dung sẽ học.
- Mỗi script có ba hướng A/B rõ ràng: keyword/search, outcome thực tế và insight/curiosity dễ hiểu.
- Số EP và branding đứng cuối để không che mất chủ đề trên màn hình nhỏ.
- Thumbnail chỉ dùng 2–4 từ lớn và bổ sung cho tiêu đề, không chép lại toàn bộ tiêu đề.
- 30 giây đầu phải chiếu đúng bằng chứng đã hứa: response sai, test xanh giả, dữ liệu mất hoặc deploy thất bại.
- Nhịp nội dung ưu tiên: lỗi thật → AI đề xuất → host bắt lỗi → sửa → kiểm chứng bằng request/test/diff.
- Không kéo video tới 15–20 phút bằng lý thuyết. Chỉ giữ cảnh giúp hiểu quyết định hoặc chứng minh code hoạt động.

### Visual identity thumbnail của series NestJS

- Ảnh chuẩn tham chiếu: `01-hoc-nestjs-voi-ai/thumbnail-01-hoc-nestjs-cung-ai.png`.
- Bố cục cố định: headline lớn bên trái, developer chiếm khoảng 35–40% bên phải, monitor code là lớp nền phụ.
- Màu chủ đạo: NEST RED `#E0234E`, WHITE `#FFFFFF`, đen và navy đậm. Không dùng xanh lá hoặc cyan cho headline và ánh sáng chính.
- Headline chính chỉ 3–5 từ; số EP và badge phụ phải nhỏ hơn rõ rệt.
- Font condensed đậm, stroke đen và shadow gọn; không dùng neon glow dày.
- Mỗi EP chỉ thay nội dung headline, biểu cảm nhẹ và chi tiết trên monitor. Không thay visual grammar của cả series.
- Trước khi chốt, kiểm tra ảnh full-size và bản thu nhỏ `320×180`; dấu tiếng Việt phải chính xác.

### EP 01 — Học NestJS với AI: Xây Users API đầu tiên ✅ đã quay — prompt demo đã có
- ← pain: repo công ty lạ hoắc, tutorial 3h lỗi thời.
- Học: Nest CLI, luồng `main.ts → module → controller → service`, decorator, DI cơ bản và nguyên tắc module theo business domain.
- Cấu trúc đầu tiên: tạo `src/modules/users` bằng `nest g resource modules/users`; chưa tạo sẵn `common/`, `config/`, `database/` khi chưa có code thật.
- AI sequence: yêu cầu Users API in-memory → AI trình plan → host review/chất vấn → approve → AI thực hiện → host kiểm tra diff và chạy app.
- Host tự gõ: endpoint `GET /users/count`, đặt trước route động `GET /users/:id`.
- Thành quả: `POST /users` trả 201, `GET /users` thấy dữ liệu, `GET /users/count` trả đúng số lượng.
- → **pain mới:** gửi `{ "name": "Richard", "email": 123 }` vẫn được chấp nhận vì DTO chưa có validation runtime.
- File: `01-hoc-nestjs-voi-ai/01-nestjs-tu-0-cung-ai.md`

### EP 02 — ValidationPipe: Chặn dữ liệu sai từ DTO ✅ đã quay — prompt demo đã có
- ← pain: EP01 nhận payload gì cũng được — `email` là số hoặc sai định dạng vẫn thành user.
- Học: compile-time type khác runtime validation; class-validator, ValidationPipe toàn cục (`whitelist`, `forbidNonWhitelisted`, `transform`), `@IsString`, `@IsNotEmpty`, `@IsEmail`, custom message tiếng Việt.
- Cấu trúc mới: thêm `src/common/pipes/app-validation.pipe.ts`; pipe chỉ phụ thuộc Nest/class-validator, không import Users hay business domain.
- AI sequence: AI đề xuất rule + bộ payload fuzz → host review/approve → chạy từng payload → phát hiện chuỗi toàn dấu cách vẫn lọt → host tự thêm bước trim rồi kiểm chứng lại.
- Thành quả: POST bậy → 400 rõ ràng. → **pain: dù sao data vẫn nằm trong RAM.**
- File: `02-validation-nestjs/02-dto-validationpipe-nestjs.md`

### EP 03 — Kết nối PostgreSQL bằng Prisma 8 ✅ đã rewrite — prompt demo đã có (2 prompt)
- ← pain: EP02 xong, restart server, dữ liệu bốc hơi.
- Học: khởi tạo Prisma 8 trong Nest app bằng `prisma orm init --target postgres --authoring psl`; phân biệt contract với database schema; emit contract; plan/review/apply migration; tạo `DatabaseModule`, Prisma provider, repository contract và Prisma adapter. Chỉ persist User, chưa tạo Tasks hay Access Control trong tập này.
- File sinh ra: `src/prisma/contract.prisma`, `contract.json`, `contract.d.ts`, `db.ts`, `prisma.config.ts` và `migrations/app/`. Commit emitted contract artifacts và migration package.
- Dependency đích: `UsersController → UsersService/use-case → UsersRepository contract ← PrismaUsersRepository → Prisma 8 db facade`; business module không import `db.orm`, không phụ thuộc `@prisma/orm-postgres`.
- Query demo dùng API Prisma 8: `db.orm.public.User.create(...)`, `.where(...).first()` và `.all()`; không dùng `prisma.user.findMany()` của Prisma 7.
- Cấu hình tối thiểu: `DATABASE_URL` đi qua biến môi trường và không commit secret. Phần tổ chức config đầy đủ được xử lý ở EP15.
- AI moment: AI lấy nhầm snippet Prisma 7 (`schema.prisma`, `PrismaClient`, `migrate dev`) → host dùng release status và docs Prisma 8 bắt lỗi, sửa plan trước khi code.
- Kiểm chứng bắt buộc: `contract emit` → `migration plan --name init` → review DDL → `db migrate --advance-ref db` → `db verify` → restart Nest app → user vẫn còn.
- Thành quả: restart, data còn nguyên. → **pain: trùng email → crash 500 xấu xí.**
- File: `03-prisma-postgresql/03-prisma-postgresql-bo-nho-that.md`

### EP 04 — Error Handling: Trả đúng lỗi 400, 404 và 409 ⚠️ script cần rewrite
- ← pain: EP03 unique constraint vi phạm → 500 stacktrace bắn ra client.
- Học: HttpException, NotFoundException/BadRequestException/ConflictException, 404 vs 400 vs 409, custom ExceptionFilter và structured error envelope của Prisma 8.
- Prisma 8 mapping: nhận diện bằng `isStructuredError`, match `error.code` dạng namespace/subcode và không dùng `instanceof PrismaClientKnownRequestError` hay mã `P2002` của Prisma 7.
- AI moment: bảo AI liệt kê MỌI chỗ service có thể fail → học tư duy defensive.
- Thành quả: mọi lỗi trả JSON sạch, đúng status. → **pain: API ai gọi cũng được, không có cửa.**
- File: `04-error-handling-nestjs/04-error-handling-nestjs.md`

### EP 05 — JWT Authentication: Register, Login và AuthGuard ✅
- ← pain: EP04 xong nhưng bất kỳ ai cũng đọc và sửa dữ liệu user.
- Học: register/login, bcrypt hash (tại sao không plaintext), JwtModule, AuthGuard, @CurrentUser, bảo vệ `/users/me`.
- AI moment: tranh luận với AI "tại sao không lưu JWT trong localStorage?" — security thinking.
- Thành quả: không token → 401; có token → đọc đúng hồ sơ của mình. → **pain: sắp tạo thêm Role và Permission, nhưng mỗi lần lại phải nhắc AI cùng convention.**
- File: `05-jwt-auth-nestjs/05-jwt-auth-nestjs.md`

### EP 06 — Agent Skill: Giúp AI làm đúng cấu trúc dự án ⚠️ script cần cập nhật Prisma 8
- ← pain: chuẩn bị tạo thêm Role và Permission, nhưng mỗi feature lại phải nhắc AI cùng một cấu trúc module/controller/service/repository/DTO.
- Học: cấu trúc `.agents/skills/<name>/SKILL.md`, YAML frontmatter, project-scoped skill và progressive disclosure.
- AI sequence: AI đọc Users/Auth đã hoàn thiện → đề xuất convention scaffold → host loại business rule khỏi template → approve tạo skill.
- Kiểm chứng: mở conversation mới, yêu cầu scaffold Role và Permission; skill phải trình plan trước, chờ approve, sinh đúng folder và chạy lint/test.
- Thành quả: AI chịu phần boilerplate; service vẫn explicit để người maintain nhìn thấy business semantics. → **pain: access token ngắn hạn làm phiên đăng nhập liên tục bị ngắt.**
- File: `06-agent-skill-nestjs/06-agent-skill-nestjs.md`

### EP 07 — Refresh Token: Gia hạn đăng nhập và thu hồi phiên ✅
- ← pain: access token ngắn hạn an toàn hơn, nhưng người dùng bị yêu cầu đăng nhập lại liên tục.
- Học: access/refresh flow, hash refresh token, rotation, reuse detection, revoke session và logout.
- AI moment: AI đề xuất lưu refresh token nguyên văn → host threat-model database leak rồi sửa thiết kế trước khi code.
- Thành quả: phiên có thể gia hạn, xoay vòng và thu hồi. → **pain: xác thực đã hoàn chỉnh nhưng mọi user vẫn có quyền như nhau.**
- File: `07-refresh-token-nestjs/07-refresh-token-rotation-nestjs.md`

### EP 08 — Role và Permission khác nhau thế nào? ✅
- ← pain: EP07 xác định được người gọi và phiên, nhưng chưa mô tả được họ được phép làm gì.
- Học: tạo `RolesModule` và `PermissionsModule`, DTO, repository contract/adapter, CRUD đầy đủ; `Role.name` và `Permission.code` là duy nhất.
- Permission code theo resource/action: `users.read`, `roles.assign`, `permissions.manage`, `tasks.create`.
- AI moment: dùng Agent Skill scaffold hai feature → AI đề xuất `CommonService<T>` → host từ chối sau khi so sánh business rule create/delete của Role và Permission.
- Thành quả: quản lý được danh mục Role và Permission. → **pain: chúng vẫn là ba bảng rời, chưa ai được gán quyền.**
- File: `08-role-permission-nestjs/08-role-permission-crud-nestjs.md`

### EP 09 — Quan hệ User, Role và Permission với Prisma 8 ⚠️ script cần rewrite demo
- ← pain: Role và Permission đã tồn tại nhưng chưa gắn được cho user hay cho nhau.
- Học: Prisma 8 explicit many-to-many với `UserRole` và `RolePermission`; composite key; `assignedAt`, `assignedBy`; seed `admin`, `member` và permission mẫu. Query relation bằng `.include(...)`; đọc junction metadata bằng model junction trực tiếp.
- API: assign/revoke role cho user; attach/detach permission cho role; dùng `db.transaction(async tx => ...)` và chỉ query qua `tx.orm` khi cập nhật nhiều quan hệ.
- Quyết định thiết kế: mặc định permission của user được suy ra qua Role. Chỉ thêm `UserPermission` khi cần cấp quyền ngoại lệ trực tiếp.
- Nếu có `UserPermission`: bắt buộc có `effect: ALLOW | DENY`; quyền hiệu lực = quyền qua Role + direct ALLOW − direct DENY.
- AI moment: AI đề xuất implicit many-to-many hoặc nested write chưa được Prisma 8 hỗ trợ đầy đủ → host kiểm tra trang relation limitations, chuyển sang explicit junction và transaction trước khi migrate.
- Thành quả: database biểu diễn được toàn bộ chính sách truy cập. → **pain: có dữ liệu quyền nhưng API vẫn chưa thực thi nó.**
- File: `09-user-role-permission-nestjs/09-user-role-permission-many-to-many.md`

### EP 10 — PermissionGuard: Phân biệt lỗi 401 và 403 ✅
- ← pain: EP09 có chính sách trong database nhưng route nào cũng chỉ kiểm tra đăng nhập.
- Học: authentication khác authorization; `@RequirePermissions()`; `PermissionGuard`; tính effective permissions theo user.
- JWT chỉ giữ `sub` và thông tin phiên cơ bản. Không nhét toàn bộ permission vào token vì quyền bị thu hồi sẽ không có hiệu lực tới khi token hết hạn.
- `PermissionGuard` và decorator nằm trong `modules/access-control`, không nằm trong `common/`.
- AI moment: AI dùng `@Roles('admin')` trực tiếp trên mọi route → host đổi sang permission claim để role có thể thay đổi mà không sửa controller.
- Thành quả: thiếu quyền → 403; có đúng permission → request đi tiếp. → **pain: kiến trúc đã có quyền nhưng chưa có business feature thật để chứng minh nó dùng lại được.**
- File: `10-permission-guard-nestjs/10-permission-guard-nestjs.md`

### EP 11 — RBAC và Ownership: Không cho sửa task người khác ✅
- ← pain: Access Control chạy được trên endpoint quản trị, nhưng chưa chứng minh được trên nghiệp vụ TaskFlow.
- Học: tạo TasksModule theo convention; task có owner; controller mỏng; service giữ business rule; repository tách Prisma.
- Áp dụng permission `tasks.create`, `tasks.read`, `tasks.update`, `tasks.delete`; phân biệt có permission với có quyền trên đúng resource của mình.
- AI moment: AI chỉ kiểm tra `tasks.update` rồi cho sửa mọi task → host bổ sung ownership rule và test thủ công bằng hai user.
- Thành quả: user chỉ thao tác task được phép và thuộc phạm vi của mình. → **pain: nhiều nhánh auth/permission/ownership quá, thử tay không còn đáng tin.**
- File: `11-tasksmodule-nestjs/11-tasksmodule-rbac-ownership.md`

### EP 12 — Testing phân quyền bằng Vitest và Supertest ⚠️ script cần cập nhật Prisma 8 + đổi Jest sang Vitest
- ← pain: EP11 thay guard hoặc ownership rule là phải thử tay hàng loạt tài khoản và route.
- Học: Vitest unit test service/guard với mock (Nest CLI 12 scaffold sẵn vitest 4, `globals: true` — API tương thích Jest), e2e Supertest, database test riêng, đỏ→xanh; coverage là gì và không phải là gì.
- Ma trận bắt buộc: user không role; nhiều role; permission trùng qua hai role; revoke role; revoke permission; thiếu permission; ownership sai; direct ALLOW/DENY nếu bật override.
- AI moment: AI sinh test chỉ assert status chung chung → host mutation nhỏ vào guard để chứng minh test vẫn xanh, rồi viết lại assertion có giá trị.
- Thành quả: `test` và `test:e2e` bảo vệ luồng auth/RBAC/ownership. → **pain: duplication giữa ba feature bắt đầu rõ, rất dễ refactor quá tay.**
- File: `12-testing-rbac-nestjs/12-testing-ma-tran-rbac-ownership.md`

### EP 13 — DRY: Khi nào không nên dùng BaseCrudService ✅
- ← pain: UsersService, RolesService và PermissionsService có nhiều method cùng tên, nhìn rất muốn gom thành `CommonService<T>`.
- Học: duplicate code khác duplicate knowledge; YAGNI; abstraction boundary; khi nào repository generic nhẹ có ích và khi nào nó che business semantics.
- AI sequence: yêu cầu AI giảm tối đa code duplicate → AI tạo BaseCrudService → host dùng test chứng minh `register user`, `create role` và `delete system permission` thay đổi vì lý do khác nhau.
- Kết luận: không tạo generic business service; chỉ abstract persistence mechanics khi duplication đã ổn định và abstraction làm code dễ hiểu hơn.
- File: `13-dry-abstraction-nestjs/13-generic-crud-abstraction-trap.md`

### BONUS 13.5 — Prisma 8 và TypeORM: Có nên dùng BaseEntity? ⚠️ script cần cập nhật
- ← pain: Prisma 8 contract phải lặp `id`, `createdAt`, `updatedAt`, nhưng tạo table inheritance chỉ để né ba dòng là quá nặng.
- Học: Prisma 8 PSL contract + emitted types + query facade so với TypeORM class/decorator; TypeORM `AbstractEntity`; concrete table inheritance; phân biệt entity reuse với service inheritance.
- Demo lại User, Role, Permission và explicit join entities bằng TypeORM; `AbstractEntity` nằm ở infrastructure/database, không đặt trong `common/` portable.
- AI moment: entity inheritance chạy đẹp nên AI tiếp tục tạo CrudService inheritance → host dùng business rule để chỉ ra abstraction không phù hợp.
- Thành quả: chọn abstraction theo programming model của tool, không theo số dòng code.
- File: `bonus-13-5-typeorm-nestjs/bonus-13-5-prisma-vs-typeorm-inheritance.md`

### EP 14 — Tách common thành thư viện dùng cho nhiều dự án ✅
- ← pain: EP13 giữ được business service explicit, nhưng copy nguyên `common/` sang repo khác sẽ tạo nhiều bản lệch nhau.
- Học: project-local common khác reusable library; chọn public API, peer dependencies, semantic versioning và migration note.
- AI sequence: AI audit `common/` → lọc phần không phụ thuộc domain/config/database → host duyệt public exports → tách workspace library hoặc private package.
- Kiểm chứng: dùng library trong TaskFlow và một Nest app sạch; consumer build được, không import ngược vào TaskFlow.
- Thành quả: cross-cutting code ổn định có phiên bản; business policy vẫn thuộc project. → **pain: library dùng được nhưng config từng môi trường vẫn rải rác.**
- File: `14-common-library-nestjs/14-tach-common-thanh-library.md`

### EP 15 — Config: Quản lý ENV an toàn cho mọi môi trường ✅
- ← pain: EP14 có hai consumer, nhưng DB test, JWT secret và port của mỗi môi trường vẫn cấu hình một kiểu.
- Học: `.env`, ConfigModule, config factory, env validation, dev/test/prod, gitignore secrets.
- AI moment: nhờ AI audit repo như senior review PR — scan secret, tìm config đọc trực tiếp từ `process.env`, review giá trị bắt buộc.
- Thành quả: đổi PORT/DATABASE_URL/JWT config không sửa business code; repo sạch key. → **pain: auth + pipe + guard + interceptor cùng chạy, request lỗi không biết lớp nào chặn.**
- File: `15-config-nestjs/15-config-env-validation-nestjs.md`

### EP 16 — Request Lifecycle: Middleware, Guard và Pipe chạy thế nào? ✅
- ← pain: EP15 đã có auth, validation và config nhưng debug request vẫn như lần trong mê cung.
- Học: thứ tự middleware → guard → interceptor → pipe → handler, logging interceptor, transform response.
- AI moment: AI vẽ sequence diagram lifecycle → host đối chiếu từng bước với log từ code thật.
- Thành quả: nhìn log biết request dừng ở đâu. → **pain: "máy tôi chạy được" — giờ cần người khác chạy được.**
- File: `16-request-lifecycle-nestjs/16-request-lifecycle-nestjs.md`

### EP 17 — Docker và Deploy NestJS lên Production ⚠️ script cần rewrite Prisma 8
- ← pain: cả 16 tập chạy localhost — máy thiếu Node/PostgreSQL là không chạy được.
- Học: Dockerfile Node 24, docker-compose kèm PostgreSQL, commit `contract.json`/`contract.d.ts` và `migrations/`, chạy `prisma migration check` + `prisma db migrate --show` + `prisma db migrate --advance-ref db` trước khi start app, env production, deploy Render/Railway.
- Prisma 8 không có native query engine và không có bước `prisma generate` trong image. Không dùng `prisma migrate deploy` của Prisma 7.
- AI moment: AI dùng Dockerfile Prisma cũ rồi cài OpenSSL/query-engine không cần thiết → host đối chiếu guide Prisma 8, review từng layer và migration gate. Recap Season 1.
- Thành quả: public URL. → **pain: API công khai mà không có tài liệu — ai biết gọi thế nào.**
- File: `17-docker-deploy-nestjs/17-docker-deploy-taskflow.md`

## SEASON 2 — CỨNG CÁP (EP 18–27): production thật sự

### EP 18 — Swagger docs: API tự viết hồ sơ
- ← pain: EP17 public xong, người dùng cứ hỏi endpoint nhận gì và cần permission nào.
- Học: `@nestjs/swagger`, `@ApiTags`, `@ApiOperation`, bearer auth, response/error schema, annotate DTO.
- AI moment: nhờ AI annotate toàn bộ controller → host rà annotation nào nói khác code và permission nào bị bỏ sót.
- Thành quả: `/docs` mô tả được cả auth và RBAC. → **pain: REST client phải gọi nhiều endpoint để ghép một màn hình.**

### BONUS 18.5 — Cùng một Service, hai API: REST vs GraphQL
- ← pain: dashboard cần user, tasks và permissions; REST client phải tự ghép nhiều response.
- Học: `@nestjs/graphql` code-first, resolver là transport boundary, reuse Users/Tasks/AccessControl service; guard với GraphQL execution context.
- AI moment: AI copy business logic sang resolver → host kéo logic về service và chứng minh REST/GraphQL dùng chung một use case.
- Thành quả: hiểu GraphQL mà không biến series thành một course GraphQL khác.

### EP 19 — Rate limiting & Helmet: dạy API tự vệ
- ← pain: docs công khai trở thành bản đồ cho bot spam login và API quản trị.
- Học: `@nestjs/throttler`, giới hạn theo IP/user/route, Helmet, bảo vệ login khác endpoint thường.
- AI moment: AI viết script spam chính API → host quan sát 429 rồi chất vấn cách attacker đổi IP hoặc tài khoản.
- Thành quả: spam bị giới hạn, security headers bật đủ. → **pain: bị spam nhưng log rời rạc, không truy nổi một request.**

### EP 20 — Structured logging + Correlation ID
- ← pain: EP19 xảy ra lỗi lúc 2h sáng — hàng nghìn dòng log không biết dòng nào cùng request.
- Học: pino structured logging, correlation ID đi suốt request, log level, redaction; tuyệt đối không log password/token.
- AI moment: cho AI đọc log rối và tóm tắt sự cố → host kiểm tra lại theo correlation ID thay vì tin bản tóm tắt.
- Thành quả: một request có một dấu vết đầu cuối. → **pain: log cho biết có lỗi nhưng không chỉ ra method nào đang chậm.**

### EP 21 — NestJS Observe: nhìn xuyên request production
- ← pain: EP20 có log nhưng vẫn phải đoán request chậm ở Guard, Service, Prisma hay queue.
- Học: `@nestjs/observe`, auto-instrument request/job/error/trace, trace waterfall, latency p95, release và error context.
- AI moment: tạo một endpoint chậm → đưa telemetry thật cho AI phân tích → host verify span gây chậm trước khi sửa.
- Không biến MCP thành điều kiện bắt buộc: flow chính dùng dashboard/copy agent prompt; MCP read-only chỉ là nhánh tùy gói dịch vụ.
- Thành quả: chẩn đoán dựa trên telemetry, không đoán từ code. → **pain: user báo lỗi task nhưng không gắn được ảnh minh họa.**

### BONUS 21.5 — Observe vs Sentry/OpenTelemetry: chọn công cụ theo nhu cầu
- So sánh Nest-aware instrumentation, error tracking, open standard, self-hosting, chi phí và vendor lock-in.
- Không cài ba stack vào cùng project; dùng decision matrix và một trace/error giống nhau để so sánh.

### EP 22 — File upload: avatar và attachment cho task
- ← pain: EP21 thấy lỗi rõ rồi, nhưng task vẫn không đính kèm được ảnh hoặc file.
- Học: Multer, `@UploadedFile`, validate loại/dung lượng, local vs object storage, serve file an toàn.
- AI moment: hỏi AI nếu file giả danh `.jpg` thì sao → học magic bytes, không tin extension.
- Thành quả: task có attachment hợp lệ. → **pain: dữ liệu và file tăng, GET `/tasks` trả hàng nghìn dòng.**

### EP 23 — Pagination, filtering, sorting
- ← pain: EP22 xong, task 5 nghìn dòng làm response lớn và client treo.
- Học: offset vs cursor, query filter, sort, metadata page; Prisma 8 chain `.orderBy(...).skip(...).take(...).all()` và cursor ổn định có `id` làm tiebreaker.
- AI moment: chất vấn offset pagination khi dữ liệu chèn liên tục → hiểu vì sao cursor.
- Thành quả: danh sách task tải theo phần. → **pain: task vẫn là danh sách phẳng, chưa nhóm theo dự án.**

### EP 24 — Quan hệ dữ liệu: Project, Label và many-to-many
- ← pain: EP23 xong nhưng task chưa thuộc project và chưa có label.
- Học: quan hệ 1–N, N–N trong Prisma 8, migration khi đã có data, `.include(...)` vs `.select(...)`, explicit junction khi cần metadata, module Project/Label.
- AI moment: AI thiết kế schema → host chất vấn cascade hay restrict trước khi migrate.
- Thành quả: task thuộc project và gắn nhiều label. → **pain: tạo task kèm label hỏng giữa chừng làm data lệch.**

### EP 25 — Transactions: làm trọn vẹn hoặc không làm
- ← pain: EP24 tạo task xong nhưng attach label fail, hệ thống còn nửa trạng thái.
- Học: Prisma 8 `db.transaction(async tx => ...)`, query qua `tx.orm`, rollback khi callback throw, transaction boundary, race condition, khi nào không nên giữ transaction lâu. Không dạy `$transaction` của Prisma 7.
- Giới hạn phiên bản: không trình bày transaction isolation level như một API đã ổn định nếu release status vẫn ghi chưa hỗ trợ.
- AI moment: AI dựng hai request chạy đồng thời → host chạy demo và quan sát dữ liệu lệch trước khi sửa.
- Thành quả: hoặc toàn bộ thành công, hoặc quay về như chưa có gì. → **pain: dashboard join nhiều bảng, gọi liên tục làm DB nặng.**

### EP 26 — Caching với Redis: học cách quên
- ← pain: EP25 đúng dữ liệu nhưng dashboard query nặng và lặp lại.
- Học: cache-aside, key design, invalidate khi data/quyền đổi, TTL và stale data.
- AI moment: hỏi AI khi nào cache là kẻ thù → cố tình tạo bug quyền cũ còn trong cache rồi sửa invalidation.
- Thành quả: dashboard nhanh hơn mà revoke permission vẫn có hiệu lực. → **pain: gửi mail nhắc deadline ngay trong request làm user chờ.**

### EP 27 — Background jobs với BullMQ: việc nặng để sau
- ← pain: EP26 xong, gửi mail trong request vẫn bị phụ thuộc mail server.
- Học: BullMQ + Redis, retry/backoff, failed job, dead-letter strategy, idempotent job cơ bản.
- AI moment: host tắt mail server giữa chừng → quan sát retry rồi quyết định khi nào bỏ cuộc.
- Thành quả: response về ngay, mail chạy nền. Recap Season 2. → **pain: queue có worker nhưng chưa ai tạo job nhắc việc mỗi sáng.**

## SEASON 3 — CHUYÊN SÂU (EP 28–38): modular monolith thực thụ

### EP 28 — Cron job: robot làm ca đêm
- ← pain: EP27 queue chỉ chạy khi có producer; nhắc deadline cần quét mỗi sáng.
- Học: `@nestjs/schedule`, `@Cron`, job định kỳ, chống chạy trùng nhiều instance.
- AI moment: hỏi AI nếu ba server cùng chạy cron → học distributed lock ở mức ứng dụng.
- Thành quả: lịch nhắc việc tự tạo job. → **pain: teammate thêm task nhưng màn hình phải F5.**

### EP 29 — Realtime WebSocket: dữ liệu tự đi đến
- ← pain: EP28 server đã tự động nhưng trình duyệt vẫn phải refresh để thấy task mới.
- Học: Socket.IO gateway, `@WebSocketServer`, emit event, client subscribe, ACK và reconnect cơ bản.
- AI moment: AI sinh gateway → host chất vấn client mất mạng ngay sau emit thì sao.
- Thành quả: task mới hiện trên tab khác. → **pain: socket nào cũng nhận mọi sự kiện.**

### EP 30 — Socket auth & rooms: phòng riêng cho mỗi người
- ← pain: EP29 mọi client nhận mọi notification, làm lộ dữ liệu.
- Học: JWT handshake, reuse auth service, room per user/project, permission khi join room, emit có chủ đích.
- AI moment: kết nối bằng token hết hạn và user thiếu permission → AI review flow, host tìm đường bypass.
- Thành quả: mỗi user chỉ nhận event được phép. → **pain: chạy nhiều server thì room nằm rải rác trong từng process.**

### EP 31 — WebSocket nhiều server: Redis Adapter và sticky session
- ← pain: user nối API1 nhưng event phát từ API3 không tới đúng room.
- Học: Socket.IO Redis adapter, pub/sub giữa instance, sticky session, reconnect và giới hạn delivery guarantee.
- Redis đã xuất hiện ở EP26 nên tập này tập trung vào scaling, không dạy lại cache.

### EP 32 — Soft delete & Audit log: không có gì xóa vĩnh viễn
- ← pain: socket đã đúng người nhưng user lỡ xóa task thì mất trắng, không truy được ai làm.
- Học: `deletedAt`, filter mặc định, restore, audit actor/action/time, request context và privacy.
- AI moment: AI đề xuất log mọi field → host cắt dữ liệu nhạy cảm và chỉ giữ bằng chứng cần thiết.
- Thành quả: khôi phục được và có dấu vết. → **pain: thêm field mới làm client cũ vỡ contract.**

### EP 33 — API versioning & backward compatibility
- ← pain: EP32 đổi response shape làm app cũ parse lỗi.
- Học: URI versioning, deprecation, compatibility window, changelog và contract test.
- AI moment: AI đề xuất v2 → host duyệt từng breaking change như review PR.
- Thành quả: v1 và v2 sống chung. → **pain: dữ liệu lớn dần, endpoint chậm nhưng chưa biết vì sao.**

### EP 34 — Performance: N+1, index và đo trước khi sửa
- ← pain: EP33 xong, một số endpoint chậm dần và mọi người sửa theo cảm giác.
- Học: query log/trace, N+1, index, `EXPLAIN` cơ bản, đo before/after.
- AI moment: AI nhìn telemetry đoán bottleneck → host verify bằng query plan và số liệu thật.
- Thành quả: endpoint chậm nhất cải thiện có số đo. → **pain: GraphQL bonus cũng có thể tạo N+1 tinh vi.**

### BONUS 34.5 — GraphQL N+1: DataLoader giải quyết thế nào?
- Dùng query users → tasks → labels để tạo N+1 thật.
- So sánh naive field resolver, batching/caching theo request và DataLoader; verify bằng số query.

### EP 35 — CI/CD GitHub Actions: robot nhận việc deploy
- ← pain: code nhanh hơn nhưng mỗi lần push vẫn test, build và deploy bằng tay.
- Học: workflow YAML, test matrix, build image, deploy khi merge, branch protection và PR checks.
- AI moment: AI viết workflow → host đọc từng step và xóa phần thừa.
- Thành quả: push → test → deploy. → **pain: rollout đang có traffic làm request bị đứt.**

### EP 36 — Health check & graceful shutdown: thay lốp xe đang chạy
- ← pain: EP35 deploy tự động nhưng rollout vẫn tạo vài giây 502.
- Học: liveness/readiness, dependency health, SIGTERM, connection draining và graceful shutdown.
- AI moment: AI kể timeline shutdown → host đối chiếu bằng log và request đang chạy.
- Thành quả: deploy không làm rơi request. → **pain: thêm listener mail/notification vẫn phải sửa service trung tâm.**

### EP 37 — Event-driven: module nói chuyện qua sự kiện
- ← pain: TasksService trở thành file nóng vì mail, audit, notification cùng bám vào nó.
- Học: domain event trong monolith, `TaskCompleted`, listener, eventual side effect và failure boundary.
- AI moment: thêm tính năng điểm thưởng bằng listener mà không sửa use case hoàn thành task.
- Thành quả: module giao tiếp qua event có chủ đích. → **pain: boundary đã rõ, câu hỏi tiếp theo là khi nào nên tách process.**

### EP 38 — Recap modular monolith: từ folder rỗng đến hệ thống thật
- ← pain: 37 tập nhiều khái niệm, người học cần một bản đồ và tiêu chí trước khi bước sang distributed system.
- Học: vẽ lại TaskFlow, dependency direction, auth/RBAC, production stack, 15 câu phỏng vấn và cách kể project theo STAR.
- AI moment: AI đóng vai interviewer → host trả lời bằng quyết định và trade-off đã thực sự implement.
- Thành quả: modular monolith hoàn chỉnh, có lý do rõ ràng nếu muốn tách service. → **pain: notification workload bắt đầu ảnh hưởng API chính.**

## SEASON 4 — MICROSERVICES (EP 39–46): chỉ tách khi monolith có lý do để tách

### EP 39 — Monolith → Microservices: khi nào nên tách?
- ← pain: notification workload ảnh hưởng API nhưng không muốn chia service theo cảm tính.
- Học: service boundary, ownership dữ liệu, operational cost, modular monolith vs distributed system.
- AI moment: AI đề xuất tách mọi module → host dùng coupling và failure data để chỉ chọn Notification Service.
- Thành quả: có boundary và lý do đo được. → **pain: hai service cần giao tiếp nhưng chưa biết dùng message hay event.**

### EP 40 — MessagePattern vs EventPattern: hỏi đáp hay phát sự kiện?
- ← pain: API cần gửi lệnh và nhận kết quả, trong khi TaskCompleted chỉ cần thông báo.
- Học: request-response, event-based messaging, timeout, contract và transport abstraction của Nest.
- AI moment: AI dùng event cho câu hỏi cần response → host dựng failure để lộ thiết kế sai.
- Thành quả: chọn đúng communication style. → **pain: consumer chết giữa chừng thì message xử lý tới đâu?**

### EP 41 — RabbitMQ: ACK, retry và dead-letter queue
- ← pain: message đã gửi nhưng worker crash trước khi hoàn tất.
- Học: broker, durable message, manual ACK/NACK, retry/backoff, DLQ và poison message.
- AI moment: kill consumer đúng giữa xử lý → quan sát redelivery thay vì suy đoán.
- Thành quả: message không im lặng biến mất. → **pain: retry có thể chạy business action hai lần.**

### EP 42 — Idempotency: message chạy hai lần thì sao?
- ← pain: RabbitMQ redelivery làm email hoặc side effect bị lặp.
- Học: idempotency key, inbox/deduplication record, unique constraint và retry-safe handler.
- AI moment: phát cùng message hai lần → host chứng minh chỉ một side effect xảy ra.
- Thành quả: at-least-once delivery không phá business data. → **pain: database commit nhưng publish event có thể fail.**

### EP 43 — Distributed transaction và Outbox Pattern
- ← pain: task đã hoàn thành trong DB nhưng event không tới Notification Service.
- Học: dual-write problem, ghi business state và outbox record trong cùng Prisma 8 `db.transaction(...)`, relay worker, retry và cleanup.
- AI moment: ngắt broker giữa DB commit và publish → tái hiện mất event rồi verify outbox phục hồi.
- Thành quả: state và event không lệch nhau. → **pain: không phải giao tiếp service nào cũng phù hợp asynchronous event.**

### EP 44 — gRPC: synchronous service-to-service
- ← pain: API cần dữ liệu đồng bộ từ service khác với contract chặt và latency thấp.
- Học: protobuf, unary call, deadline, error mapping, schema evolution cơ bản.
- AI moment: AI thay REST bằng gRPC mọi nơi → host đo trade-off và giữ event cho workflow bất đồng bộ.
- Thành quả: có thêm lựa chọn synchronous rõ ràng. → **pain: một request đi qua HTTP, gRPC và RabbitMQ thì log từng service không đủ.**

### EP 45 — NestJS Observe Distributed Tracing
- ← pain: request chạy qua nhiều service, trace ID bị đứt ở transport boundary.
- Học: propagation qua HTTP/gRPC/microservice transport, trace waterfall, slow span và error chain.
- AI moment: AI đọc trace thật để khoanh vùng service chậm → host verify bằng span và metric.
- Thành quả: nhìn được hành trình xuyên service. → **pain: hệ thống đã phân tán nhưng còn thiếu kiểm chứng production toàn diện.**

### EP 46 — Microservices production capstone
- ← pain: từng pattern chạy riêng, chưa biết hệ thống chịu deploy, retry và service failure đồng thời ra sao.
- Học: health/readiness, deploy order, backward-compatible contract, failure drill, runbook và cost review.
- AI moment: AI đóng vai incident commander trên một sự cố dựng sẵn → host yêu cầu evidence trước mỗi hành động.
- Thành quả: TaskFlow distributed chạy end-to-end và người học hiểu cả giá phải trả của Microservices.

## Nguyên tắc xuyên suốt series

1. Mỗi ep mở bằng NỖI ĐAU của ep trước (chain rule) — không bao giờ mở bằng "hôm nay ta học X".
2. Mỗi ep có đúng MỘT AI sequence liền mạch — có thể gồm vài lượt hỏi–đáp nhưng chỉ phục vụ một outcome, không biến thành màn trình diễn nhiều tính năng AI.
3. **AI-Driven Development Workflow (quy trình chuẩn 6 bước, xuyên suốt mọi ep):** (1) Yêu cầu — mô tả mục tiêu + context → (2) AI lên Plan → (3) host Review bằng mắt → (4) host Approve → (5) AI Thực hiện code → (6) Kiểm chứng (git diff / test / chạy app). AI không bao giờ tự ý sửa.
4. Host luôn TỰ GÕ lại ít nhất một đoạn code AI sinh trong mỗi ep — điều kiện để gọi là "mình hiểu".
5. Kết mỗi ep teaser 1 câu cho ep sau (retention loop + minh bạch chain).
6. Tool AI: **Opus trong IDE Antigravity**. Đổi tool thì giữ nguyên pattern hỏi–đọc–chất vấn.
7. Mỗi season có điểm tổng kết rõ: EP17 recap nền tảng, EP27 recap production, EP38 tổng kết modular monolith và EP46 là microservices capstone.
8. Title mọi tập đánh số series: `NestJS #NN: <hook> | Lập trình là cuộc sống`.
