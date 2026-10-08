# Prompt dùng trong EP06 — Agent Skill: Giúp AI làm đúng cấu trúc dự án

> Các prompt dưới đây dùng tuần tự trong video.
> Host paste từng prompt vào agent panel (Antigravity / Cursor / Codex),
> review kết quả, chỉnh sửa, rồi mới chuyển sang prompt tiếp theo.

---

## PROMPT 1 — Audit convention từ code đã hoàn thiện

> **Mục đích:** Cho AI đọc Users và Auth module — hai feature đã stable — rồi
> rút ra convention chung đủ ổn định để đưa vào agent skill.

```text
Đọc toàn bộ code trong `src/modules/users/` và `src/modules/auth/`.
Đọc thêm `src/prisma/`, `src/database/`, `src/common/` và `src/config/`.

Liệt kê những convention chung mà CẢ HAI feature đều tuân thủ:
- Cấu trúc file/folder bên trong module
- Hướng dependency (controller → service → repository contract → adapter)
- Cách tách repository contract khỏi Prisma adapter
- Cách đăng ký module, provider và export
- Cách dùng DTO, validation pipe
- Cách tương tác với Prisma 8 database facade (`db.ts`)
- Lệnh verify sau khi thay đổi code (lint, test, contract emit, migration)

Phân biệt rõ hai loại:
1. Convention CHUNG — áp dụng được cho BẤT KỲ feature mới nào (file layout,
   dependency direction, workflow)
2. Convention RIÊNG — chỉ thuộc Users hoặc Auth (hash password, JWT, guard
   logic cụ thể)

Chỉ đề xuất loại 1 để đưa vào agent skill.
KHÔNG đề xuất loại 2 — đó là business rule của feature đó, không phải template.

Output dạng danh sách bullet, chia nhóm: File Layout, Dependency Direction,
Database Workflow, Verification Steps. Mỗi mục tối đa 2 câu.
```

---

## PROMPT 2 — Tạo SKILL.md từ convention đã duyệt

> **Mục đích:** Sau khi host review output prompt 1, loại bỏ business rule
> (ví dụ: hash password), thì dùng prompt này để AI sinh SKILL.md.

```text
Dựa trên convention chung tôi vừa duyệt, tạo file:
`.agents/skills/nest-feature/SKILL.md`

Yêu cầu:

### Frontmatter YAML
- `name`: `nest-feature` (ngắn, ổn định, không đổi)
- `description`: mô tả KHI NÀO dùng (scaffold hoặc mở rộng business feature
  NestJS trong TaskFlow) VÀ KHI NÀO KHÔNG dùng (one-line fix, infrastructure
  change, config-only change). Description là bộ routing — không phải quảng cáo.

### Instruction (phần markdown sau frontmatter)
Viết dưới dạng numbered list, mỗi rule 1–2 câu. Bao gồm:

1. Trước khi edit, đọc `references/architecture.md` và feature lân cận
   đã hoàn thiện gần nhất.
2. Trình file plan và dependency direction trước. Chờ approve rồi mới code.
3. Controller mỏng — chỉ xử lý transport (parse request, trả response).
4. Business rule nằm trong service hoặc use case, explicit cho từng feature.
5. KHÔNG tạo `BaseCrudService`, `CommonService<T>` hay bất kỳ generic
   business CRUD nào chỉ vì method CRUD trùng tên.
6. Repository contract không import Prisma — contract là interface thuần.
7. Prisma adapter implement contract, nhận database facade qua DI token.
8. Code thuộc riêng một domain KHÔNG đưa vào `common/`.
9. Với mọi thay đổi database:
   - Đọc Prisma 8 release status trước.
   - Đọc tài liệu Prisma 8 docs, KHÔNG dùng snippet Prisma 6/7.
   - Dùng `contract.prisma`, emitted contract và database facade.
   - KHÔNG dùng `@prisma/client`, `PrismaClient`, `prisma generate`,
     `schema.prisma`, `migrate dev`, `migrate deploy`.
10. Verification sau mỗi thay đổi:
    - `prisma contract emit` và `prisma migration check` khi contract thay đổi
    - Lint, test, diff summary theo phạm vi thay đổi

### Tạo thêm file reference
Tạo `.agents/skills/nest-feature/references/architecture.md` chứa:
- Cây thư mục đích của `src/` (dựa trên cấu trúc hiện tại)
- Dependency diagram dạng text (controller → service → contract ← adapter → db)
- Giải thích ngắn từng layer (1–2 câu mỗi layer)

Tách reference ra khỏi SKILL.md để agent chỉ nạp khi thật sự cần —
progressive disclosure giúp tiết kiệm context.
```

---

## PROMPT 3 — Tạo AGENTS.md cho project TaskFlow

> **Mục đích:** AGENTS.md là project-level instruction file mà mọi agent đọc
> ngay khi mở repo. Nó khác SKILL (chỉ kích hoạt khi khớp) — AGENTS.md luôn
> có hiệu lực.

```text
Đọc toàn bộ cấu trúc project hiện tại: `src/`, `package.json`,
`prisma.config.ts`, `tsconfig.json`, `.env.example` và `docker-compose.yml`.

Tạo file `AGENTS.md` ở root repo với nội dung:

### 1. Project Overview (3–5 câu)
- Tên project: TaskFlow
- Loại: Task management REST API
- Stack: NestJS 12, TypeScript 5.9+, Prisma 8, PostgreSQL, Node 24 ESM
- Kiến trúc: modular monolith, module theo business domain
- Auth: JWT access token + refresh token rotation

### 2. Directory Layout
- Cây thư mục `src/` ở mức folder chính (không liệt kê từng file)
- Giải thích mục đích mỗi folder top-level: `modules/`, `common/`,
  `config/`, `prisma/`, `database/`

### 3. Dependency Rules (luật bắt buộc)
Tóm tắt các luật kiến trúc quan trọng nhất:
- Hướng dependency
- Controller thin, service/use-case giữ business logic
- Repository contract tách khỏi Prisma adapter
- `common/` không import từ `modules/`
- Không tạo generic business CRUD service

### 4. Database Conventions (Prisma 8)
- Contract file: `src/prisma/contract.prisma`
- Emitted artifacts: `contract.json`, `contract.d.ts`
- Database facade: `src/prisma/db.ts`
- Migration: `migrations/app/`
- Workflow: edit contract → emit → plan → review → apply → verify
- CẤM: `@prisma/client`, `PrismaClient`, `prisma generate`,
  `schema.prisma`, `migrate dev/deploy` (Prisma 7)

### 5. Environment & Config
- `.env` bị gitignore; `.env.example` chỉ có placeholder
- ConfigModule + Zod validation cho mọi biến môi trường
- Docker Compose dùng required interpolation

### 6. Testing
- Framework: Vitest 4 (Nest CLI 12 scaffold sẵn, globals: true)
- Unit test: mock repository contract
- E2E test: Supertest + database thật (test container hoặc test DB)
- Chạy: `npm test`, `npm run test:e2e`

### 7. Workflow cho Agent
- Luôn trình plan trước, chờ approve rồi mới sửa code
- Đọc feature lân cận trước khi tạo feature mới
- Chạy verification đầy đủ sau mỗi thay đổi
- Đối chiếu Prisma 8 docs, không dùng snippet từ search result

Giữ AGENTS.md ngắn gọn (dưới 150 dòng). Đây là bản đồ tổng quan —
chi tiết nằm trong skill và reference.
```

---

## PROMPT 4 — Kiểm chứng Skill (dùng trong conversation MỚI)

> **Mục đích:** Mở conversation mới (context sạch) để xem agent có tự nhận
> skill và tuân thủ convention không.

```text
Use $nest-feature to plan Roles and Permissions inside the TaskFlow
access-control domain.

Do not edit yet. Show:
1. Folder structure for `src/modules/access-control/roles/` and
   `src/modules/access-control/permissions/`
2. Dependency direction for each layer
3. Repository contract interface (no Prisma imports)
4. Which Prisma 8 docs/release-status pages to check before migration
5. Verification commands to run after implementation
```

---

## PROMPT 5 — Test negative: skill KHÔNG nên kích hoạt

> **Mục đích:** Chứng minh description scope hoạt động — prompt không liên quan
> thì skill không được dùng.

```text
Fix the typo in README.md line 3: change "Tsak" to "Task".
```

---

## PROMPT 6 — Test ranh giới: cố ép AI tạo generic CRUD

> **Mục đích:** Chứng minh skill cấm generic business service ngay cả khi
> prompt yêu cầu giảm duplicate.

```text
I want to minimize code duplication across Roles, Permissions and Users
services. Create a BaseCrudService<T> that all three can extend.
```

> **Kết quả mong đợi:** Agent từ chối tạo `BaseCrudService` vì skill cấm,
> giải thích rằng business logic của mỗi feature khác nhau dù method name
> trùng.

---

## Ghi chú quay video

- **Prompt 1–3:** Chạy trong cùng conversation để AI có context liên tục.
  Host review output từng prompt, loại bỏ business rule trước khi approve.
- **Prompt 4–6:** Mở conversation MỚI (context sạch) để kiểm chứng skill
  hoạt động độc lập.
- Quay cả lúc host đọc output, suy nghĩ và loại bỏ — đây là điểm khác biệt
  "AI viết, mình hiểu" của series.
- IDE theme: One Dark Pro, font ≥18px, ẩn sidebar/minimap khi chiếu terminal.
