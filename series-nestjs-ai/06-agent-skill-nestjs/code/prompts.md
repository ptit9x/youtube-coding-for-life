# Prompt dùng trong EP06 — Agent Skill: Giúp AI làm đúng cấu trúc dự án

> Các prompt dưới đây dùng tuần tự trong video.
> Host paste từng prompt vào agent panel Antigravity,
> review kết quả, chỉnh sửa, rồi mới chuyển sang prompt tiếp theo.

---

## PROMPT 1 — Hỏi banned patterns TRƯỚC khi có AGENTS.md

> **Mục đích:** Cold open. Chứng minh AI chỉ biết cái đang dùng, không biết
> cái bị cấm — vì code không chứa thông tin đó.
>
> ⚠️ **Reliable 100%:** Không phụ thuộc AI "sai" hay "đúng". Chỉ cần nó
> không liệt kê được banned patterns (vì AGENTS.md chưa tồn tại).

```text
What Prisma patterns are BANNED in this project?
List specific imports, commands, and file names that must NOT be used.
```

> **Kết quả mong đợi:** Agent nói cái project đang dùng
> (`@prisma/orm-postgres`, `contract.prisma`), nhưng **không liệt kê
> cái bị cấm** (`@prisma/client`, `PrismaClient`, `schema.prisma`,
> `migrate dev`) vì không có nguồn nào ghi thông tin đó.

---

## PROMPT 2 — Audit convention từ code đã hoàn thiện

> **Mục đích:** Cho AI đọc toàn bộ code — rút ra convention chung
> giữa các feature đã stable.

```text
Read all code base.

List the SHARED conventions that BOTH features follow — file layout,
dependency direction, database workflow, verification steps.

Exclude feature-specific rules (password hashing, JWT logic). Those are
business rules, not architecture templates.

Output as bullet list grouped by category. Max 2 sentences per item.
```

---

## PROMPT 3 — Tạo AGENTS.md + docs/ + Skill từ convention đã duyệt

> **Mục đích:** Sau khi host review output prompt 2 và loại bỏ business rule
> (ví dụ: hash password), prompt này yêu cầu AI tạo toàn bộ convention files
> trong 1 lần: AGENTS.md (Hot Memory), docs/ (Cold Memory) và nest-feature
> Skill.

```text
Based on the shared conventions I just approved, read the current project
structure and create these 5 files:

1. `AGENTS.md` (repo root) — Hot Memory, always loaded.
   Project overview, directory layout, dependency rules, database
   conventions (Prisma 8, banned Prisma 7 patterns), conditional reading
   rules for docs/, env/config, testing commands, agent workflow.
   Target under 150 lines.

2. `docs/architecture.md` — Cold Memory, read when changing module
   boundaries. Detailed src/ tree, dependency diagram, responsibility
   table per layer (what each DOES and what is FORBIDDEN), module
   dependency map. Based on actual code only.

3. `docs/database-schema.md` — Cold Memory, read when changing models.
   Current models from contract.prisma, migration workflow with concrete
   commands, patterns in use, banned Prisma 7 patterns with WRONG vs
   CORRECT examples. Based on actual code only.

4. `.agents/skills/nest-feature/SKILL.md` — Skill for scaffolding NestJS
   business features.
   Frontmatter: name `nest-feature`, description as router (when to use,
   when NOT to use).
   Instructions as numbered rules: read references first, present plan
   before coding, thin controllers, explicit business rules per feature,
   no generic CRUD, repository contracts without Prisma imports, Prisma 8
   only (ban @prisma/client, PrismaClient, schema.prisma, migrate dev),
   verification after every change.

5. `.agents/skills/nest-feature/references/architecture.md` — Reference
   loaded on demand. Directory tree, dependency diagram, layer explanation.
```

---

## PROMPT 4 — Hỏi banned patterns SAU khi có AGENTS.md (conversation MỚI)

> **Mục đích:** Cùng câu hỏi như Prompt 1. Lần này AGENTS.md đã tồn tại →
> agent trả danh sách banned patterns rõ ràng, quote từ AGENTS.md.
> Contrast reliable 100%.

```text
What Prisma patterns are BANNED in this project?
List specific imports, commands, and file names that must NOT be used.
```

> **Kết quả mong đợi:** Agent quote AGENTS.md, liệt kê: cấm `@prisma/client`,
> `PrismaClient`, `schema.prisma`, `migrate dev`, `migrate deploy`,
> `client generation`. Rõ ràng hơn Prompt 1.

---

## PROMPT 5 — Test negative: skill KHÔNG nên kích hoạt

> **Mục đích:** Prompt không liên quan → skill không được dùng.

```text
Fix the typo in README.md line 3: change "Tsak" to "Task".
```

---

## PROMPT 6a — MCP demo: TRƯỚC khi bật MCP

> **Mục đích:** Chứng minh agent không được đoán khi chưa có database tool.
> **Điều kiện:** Docker PostgreSQL đang chạy, đã có ít nhất 1 user. Tắt terminal
> cho workspace demo để loại bỏ đường truy cập khác ngoài MCP.

```text
How many users are currently in the database? Query the actual PostgreSQL
database and tell me the exact count.
```

> **Kết quả mong đợi:** Agent nói chưa có bằng chứng thay vì đoán số lượng.

---

## PROMPT 6b — MCP demo: SAU khi bật database MCP (cùng conversation)

> **Mục đích:** Sau khi cấu hình MCP bằng PostgreSQL role chỉ có `SELECT`, hỏi
> lại cùng câu. `enabledTools` chỉ giới hạn tool lộ cho agent; quyền read-only
> phải được enforce ở PostgreSQL.

```text
How many users are currently in the database? Query the actual PostgreSQL
database and tell me the exact count.
```

> **Kết quả mong đợi:** Agent dùng MCP tool, chạy SELECT count, trả kết quả
> thật.

---

## Ghi chú quay video

- **Prompt 1:** Conversation đầu tiên. Hỏi banned patterns khi chưa có
  AGENTS.md (chưa tồn tại → không cần ẩn gì).
- **Prompt 2–3:** Conversation MỚI. Review prompt 2, loại business
  rule, rồi prompt 3 tạo tất cả files.
- **Prompt 4:** Conversation MỚI (AGENTS.md đã tồn tại). Cùng câu hỏi
  như Prompt 1 → so sánh contrast.
- **Prompt 5:** Conversation MỚI, test negative (typo).
- **Prompt 6a:** Chưa bật MCP và đã tắt terminal. Agent không được đoán.
- **Giữa 6a và 6b:** MCP Store → database server → PostgreSQL role chỉ có
  `SELECT` → chỉ expose query tool.
- **Prompt 6b:** Cùng conversation với 6a. Agent query thành công.
- Mở **Customizations → Skills** trước prompt 4 để quay Skill đang active.
- **Chuẩn bị MCP demo:**
  - `docker compose -f docker-compose.postgres.yml up -d`
  - Register ít nhất 1 user qua POST `/auth/register`
  - Che credential khi quay
- IDE theme: One Dark Pro, font ≥18px, ẩn sidebar/minimap khi chiếu terminal.
