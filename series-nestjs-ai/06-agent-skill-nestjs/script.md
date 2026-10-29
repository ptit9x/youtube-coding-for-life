# NestJS #06 — AGENTS.md, Skills và MCP: Dạy AI nhớ project

- **Series:** Học NestJS bằng AI — tập 6/19
- **Target runtime:** 10–12 phút (~1000 từ thoại + khoảng nghỉ review/diff)
- **Outcome:** Viewer hiểu 3 tầng context cho AI coding agent: project rules (AGENTS.md), on-demand workflow (Skills), tool connectivity (MCP). Áp dụng cho nestjs-base-with-ai NestJS project.
- **Pain mở EP07:** Access token hết hạn, user phải đăng nhập lại. Chưa có refresh token.

---

## PART 1 — SCRIPT

> **Ghi chú prompt:** Các prompt được xen kẽ đúng vị trí trong kịch bản.
> Host paste từng prompt vào agent panel Antigravity, review kết quả, rồi mới chuyển sang prompt tiếp theo.

AI đọc code rất tốt. Nó nhìn Users module, thấy repository contract, thấy Prisma adapter, rồi bắt chước cho module tiếp theo.

Nhưng convention không phải code. Cái gì bị cấm, workflow chạy thứ tự nào, khi nào đọc file nào — những thứ này nằm trong đầu bạn, không nằm trong source code.

Mình hỏi agent ngay bây giờ: Prisma pattern nào bị cấm trong project này? Nó chỉ nói cái đang dùng. Cái bị cấm, nó không biết, vì code không chứa thông tin đó.

> ---
>
> ### 🎬 PROMPT 1 — Hỏi banned patterns TRƯỚC khi có AGENTS.md
>
> **Mục đích:** Cold open. Chứng minh AI chỉ biết cái đang dùng, không biết
> cái bị cấm — vì code không chứa thông tin đó.
>
> ⚠️ **Reliable 100%:** Không phụ thuộc AI "sai" hay "đúng". Chỉ cần nó
> không liệt kê được banned patterns (vì AGENTS.md chưa tồn tại).
>
> **Conversation:** Conversation đầu tiên. AGENTS.md chưa tồn tại.
>
> ```text
> What Prisma patterns are BANNED in this project?
> List specific imports, commands, and file names that must NOT be used.
> ```
>
> **Kết quả mong đợi:** Agent nói cái project đang dùng
> (`@prisma/orm-postgres`, `contract.prisma`), nhưng **không liệt kê
> cái bị cấm** (`@prisma/client`, `PrismaClient`, `schema.prisma`,
> `migrate dev`) vì không có nguồn nào ghi thông tin đó.
>
> ---

Vấn đề không phải AI kém. Convention đang nằm sai chỗ.

Cách sửa có ba tầng. AGENTS.md giữ rule luôn cần. Skill giữ workflow theo nhu cầu. MCP nối agent với tool bên ngoài.

Bắt đầu với AGENTS.md. Đây là định dạng mở dành cho coding agent. Hơn sáu mươi nghìn repo mã nguồn mở đã dùng.

Agentic AI Foundation thuộc Linux Foundation đang quản lý định dạng này. Antigravity, Codex, Cơ-xờ và nhiều agent khác đều hỗ trợ.

Nhưng hỗ trợ không có nghĩa mọi tool nạp giống nhau. Tập này mình kiểm chứng trên đúng công cụ đang dùng: Antigravity.

Kiến trúc chi tiết thì dài. Nếu nhét hết vào rule, context bị tốn cho những thứ chưa cần.

Nên mình tạo docs architecture và database schema. AGENTS.md ghi rõ lúc nào agent phải đọc từng file.

Khi đổi boundary module, đọc architecture. Khi đổi model, đọc database schema. Một đường dẫn không có điều kiện chỉ là biển chỉ đường mơ hồ.

Mình gọi AGENTS.md là Hot Memory. Docs là Cold Memory. Đây là cách gọi trong project này, không phải thuật ngữ của chuẩn.

Project này còn nhỏ. AI đọc toàn bộ cũng chưa tốn bao nhiêu. Nhưng khi repo lớn, vài trăm file, context window không chứa nổi. Lúc đó đổ hết code vào prompt là cách chắc chắn thất bại.

AGENTS.md không chứa chi tiết. Nó chỉ đường. Khi đổi model, đọc file này. Khi đổi module, đọc file kia. Agent chỉ nạp đúng thứ cần cho task hiện tại.

Context window có giới hạn. Cách dùng nó mới quan trọng hơn kích thước của nó.

Giờ đến Skill. AGENTS.md nói điều luôn đúng. Skill mô tả một workflow chỉ dùng khi task phù hợp.

Mình yêu cầu agent đọc toàn bộ code. Sau đó, nó đề xuất convention chung giữa các feature.

> ---
>
> ### 🎬 PROMPT 2 — Audit convention từ code đã hoàn thiện
>
> **Mục đích:** Cho AI đọc toàn bộ code — rút ra convention chung
> giữa các feature đã stable.
>
> **Conversation:** Conversation MỚI.
>
> ```text
> Read all code base.
>
> List the SHARED conventions that BOTH features follow — file layout,
> dependency direction, database workflow, verification steps.
>
> Exclude feature-specific rules (password hashing, JWT logic). Those are
> business rules, not architecture templates.
>
> Output as bullet list grouped by category. Max 2 sentences per item.
> ```
>
> ---

Agent muốn đưa rule hash password vào Skill. Mình từ chối. Đó là business rule của Auth, không phải kiến trúc chung.

Đây là bước review bằng mắt. AI đề xuất. Người hiểu project quyết định.

Sau khi duyệt plan, mình cho agent tạo AGENTS.md, docs và nest-feature Skill.

> ---
>
> ### 🎬 PROMPT 3 — Tạo AGENTS.md + docs/ + Skill từ convention đã duyệt
>
> **Mục đích:** Sau khi host review output prompt 2 và loại bỏ business rule
> (ví dụ: hash password), prompt này yêu cầu AI tạo toàn bộ convention files
> trong 1 lần: AGENTS.md (Hot Memory), docs/ (Cold Memory) và nest-feature Skill.
>
> **Conversation:** Cùng conversation với Prompt 2.
>
> ```text
> Based on the shared conventions I just approved, read the current project
> structure and create these 5 files:
>
> 1. `AGENTS.md` (repo root) — Hot Memory, always loaded.
>    Project overview, directory layout, dependency rules, database
>    conventions (Prisma 8, banned Prisma 7 patterns), conditional reading
>    rules for docs/, env/config, testing commands, agent workflow.
>    Target under 150 lines.
>
> 2. `docs/architecture.md` — Cold Memory, read when changing module
>    boundaries. Detailed src/ tree, dependency diagram, responsibility
>    table per layer (what each DOES and what is FORBIDDEN), module
>    dependency map. Based on actual code only.
>
> 3. `docs/database-schema.md` — Cold Memory, read when changing models.
>    Current models from contract.prisma, migration workflow with concrete
>    commands, patterns in use, banned Prisma 7 patterns with WRONG vs
>    CORRECT examples. Based on actual code only.
>
> 4. `.agents/skills/nest-feature/SKILL.md` — Skill for scaffolding NestJS
>    business features.
>    Frontmatter: name `nest-feature`, description as router (when to use,
>    when NOT to use).
>    Instructions as numbered rules: read references first, present plan
>    before coding, thin controllers, explicit business rules per feature,
>    no generic CRUD, repository contracts without Prisma imports, Prisma 8
>    only (ban @prisma/client, PrismaClient, schema.prisma, migrate dev),
>    verification after every change.
>
> 5. `.agents/skills/nest-feature/references/architecture.md` — Reference
>    loaded on demand. Directory tree, dependency diagram, layer explanation.
> ```
>
> ---

Antigravity dùng progressive disclosure. Ban đầu, agent chỉ thấy tên và description của Skill.

Khi task phù hợp, agent mới đọc toàn bộ instruction. Context không phải gánh mọi workflow trong mọi conversation.

Description là bộ định tuyến. Mình ghi rõ Skill dùng cho business feature. Sửa typo hoặc config nhỏ thì không dùng.

AI làm xong, mình không tin ngay. Mình mở git diff và đọc từng file.

Mình chạy git diff check, lint và test. Tất cả đều xanh. Chu trình sáu bước kết thúc ở đây.

Mình mở Customizations. AGENTS.md và Skill đều xuất hiện. Bây giờ mới tới kiểm chứng.

Mình hỏi lại cùng câu lúc đầu. Prisma pattern nào bị cấm? Lần này agent trả danh sách rõ ràng: cấm dùng prisma client import, cấm PrismaClient, cấm schema.prisma, cấm migrate dev. Nó quote thẳng từ AGENTS.md.

> ---
>
> ### 🎬 PROMPT 4 — Hỏi banned patterns SAU khi có AGENTS.md (conversation MỚI)
>
> **Mục đích:** Cùng câu hỏi như Prompt 1. Lần này AGENTS.md đã tồn tại →
> agent trả danh sách banned patterns rõ ràng, quote từ AGENTS.md.
> Contrast reliable 100%.
>
> **Conversation:** Conversation MỚI (AGENTS.md đã tồn tại).
>
> ```text
> What Prisma patterns are BANNED in this project?
> List specific imports, commands, and file names that must NOT be used.
> ```
>
> **Kết quả mong đợi:** Agent quote AGENTS.md, liệt kê: cấm `@prisma/client`,
> `PrismaClient`, `schema.prisma`, `migrate dev`, `migrate deploy`,
> `client generation`. Rõ ràng hơn Prompt 1.
>
> ---

Cùng một AI, cùng câu hỏi. Khác biệt duy nhất là AGENTS.md tồn tại.

AGENTS.md không làm AI thông minh hơn. Nó biến kinh nghiệm trong đầu người thành rule mà AI đọc được mỗi conversation.

Nhưng có một điều dễ bỏ qua. Mỗi conversation là stateless. Agent không nhớ conversation trước đã code kiểu gì.

Conversation đầu, code đúng convention. Conversation thứ mười, nó bắt đầu trôi. Đổi naming, bỏ pattern, dùng lại thứ đã cấm. Hiện tượng này gọi là convention drift. AI không sai vì kém. Nó sai vì quên — và nó quên sau mỗi conversation.

AGENTS.md là neo. Mỗi conversation đều bắt đầu từ cùng một bộ rule. Không có neo, năm mươi conversation là năm mươi cách code khác nhau trong cùng một project.

Và còn một cái giá nữa. Không có AGENTS.md, mỗi conversation bạn phải nhắc lại: dùng pattern này, cấm cái kia, structure theo kiểu này. Năm mươi conversation là năm mươi lần gõ cùng instruction. Đó là thuế thời gian bạn đang trả mà không nhận ra. AGENTS.md trả một lần, dùng mãi.

Mình mở conversation sạch khác và yêu cầu sửa typo README. Skill không kích hoạt. Scope đang hoạt động đúng.

> ---
>
> ### 🎬 PROMPT 5 — Test negative: skill KHÔNG nên kích hoạt
>
> **Mục đích:** Prompt không liên quan → skill không được dùng.
>
> **Conversation:** Conversation MỚI.
>
> ```text
> Fix the typo in README.md line 3: change "Tsak" to "Task".
> ```
>
> ---

Tầng cuối là MCP, viết tắt của Model Context Protocol. Đây là chuẩn mở để nối ứng dụng AI với hệ thống bên ngoài.

MCP giống cổng USB-C cho agent. Server có thể cung cấp database, docs, API hoặc tool chuyên biệt.

Mình thử ngay trong một workspace đã tắt terminal và chưa cấp database tool. Mình hỏi agent có bao nhiêu user trong database. Nó không có bằng chứng để trả lời.

> ---
>
> ### 🎬 PROMPT 6a — MCP demo: TRƯỚC khi bật MCP
>
> **Mục đích:** Chứng minh agent không được đoán khi chưa có database tool.
>
> **Điều kiện:** Docker PostgreSQL đang chạy, đã có ít nhất 1 user. Tắt terminal
> cho workspace demo để loại bỏ đường truy cập khác ngoài MCP.
>
> **Chuẩn bị MCP demo:**
> - `docker compose -f docker-compose.postgres.yml up -d`
> - Register ít nhất 1 user qua POST `/auth/register`
> - Che credential khi quay
>
> ```text
> How many users are currently in the database? Query the actual PostgreSQL
> database and tell me the exact count.
> ```
>
> **Kết quả mong đợi:** Agent nói chưa có bằng chứng thay vì đoán số lượng.
>
> ---

Antigravity hỗ trợ MCP Store và workspace config. File của project nằm tại .agents, mcp_config.json.

Mình mở MCP Store, chọn database server và cấu hình bằng PostgreSQL role chỉ có quyền SELECT. Trong config, mình chỉ expose tool query.

Mình hỏi lại cùng câu. Lần này agent dùng MCP tool, chạy SELECT count và trả kết quả thật từ database.

> ---
>
> ### 🎬 PROMPT 6b — MCP demo: SAU khi bật database MCP (cùng conversation)
>
> **Mục đích:** Sau khi cấu hình MCP bằng PostgreSQL role chỉ có `SELECT`, hỏi
> lại cùng câu. `enabledTools` chỉ giới hạn tool lộ cho agent; quyền read-only
> phải được enforce ở PostgreSQL.
>
> **Conversation:** Cùng conversation với Prompt 6a.
>
> **Giữa 6a và 6b:** MCP Store → database server → PostgreSQL role chỉ có
> `SELECT` → chỉ expose query tool.
>
> ```text
> How many users are currently in the database? Query the actual PostgreSQL
> database and tell me the exact count.
> ```
>
> **Kết quả mong đợi:** Agent dùng MCP tool, chạy SELECT count, trả kết quả thật.
>
> ---

MCP không phải cách duy nhất để chạm database. Giá trị của nó là một giao diện tool rõ ràng, có schema và quyền được giới hạn chủ đích.

File cấu hình này là của Antigravity, không phải config chung cho mọi client. Đổi tool vẫn phải đọc docs của tool đó.

Giờ nestjs-base-with-ai có ba tầng rõ ràng. Rule luôn bật. Workflow nạp theo nhu cầu. Kết nối ngoài được cấp quyền có chủ đích.

Trước khi đóng, ba điều đáng nhớ.

Một. AGENTS.md không phải README. README viết cho người đọc — onboarding, business context. AGENTS.md viết cho máy thực thi — command, boundary, banned pattern. Copy README vào AGENTS.md nghĩa là agent đọc cả đoạn giới thiệu sản phẩm vô nghĩa rồi bỏ sót rule quan trọng.

Hai. Khi repo lớn, AI không đọc nổi toàn bộ mỗi conversation. Đổ hết code vào prompt thì gặp hiện tượng Lost in the Middle — LLM chú ý mạnh nhất ở đầu và cuối context, phần giữa bị mờ. AGENTS.md với conditional reading chống lại điều này. Context ngắn, tập trung, không có phần giữa bị bỏ qua.

Ba. AGENTS.md lỗi thời không vô hại. Nó chủ động inject thông tin sai vào mọi conversation. Agent tin tuyệt đối vì đó là rule. Ghi sai command, ghi pattern đã đổi — agent sẽ lặp lại cái sai đó trong mọi file nó tạo. Treat AGENTS.md lỗi thời như bug. Cập nhật nó cùng pull request.

Convention tốt không khóa AI lại. Nó giúp người và AI cùng hiểu project sau sáu tháng.

Project này mới viết, convention còn sạch. Nhưng nếu bạn đang maintain legacy code — project năm bảy năm, pattern cũ nằm lẫn pattern mới — AGENTS.md còn quan trọng hơn. AI đọc code cũ, thấy pattern sai xuất hiện nhiều hơn pattern đúng, rồi bắt chước cái sai. AGENTS.md là chỗ duy nhất nói rõ cái nào bị cấm dù code vẫn còn.

Link Git của nhánh này nằm trong description. Bạn có thể comment convention khó giữ nhất trong project của mình.

Tập sau, access token hết hạn là user phải đăng nhập lại. Ta thêm refresh token rotation để giữ session mượt mà. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

> **Setup chung:** IDE One Dark Pro, font JetBrains Mono ≥18px, hide sidebar/minimap khi quay close-up. Che thông tin tài khoản.

| # | Type | Narration match | Nội dung quay | Thời lượng |
|---|---|---|---|---:|
| 1 | [IDE] | "AI đọc code rất tốt" | Split view Users module: repository contract → adapter → service; highlight pattern AI copy | 15s |
| 2 | [IDE] | "Prisma pattern nào bị cấm?" | Conversation mới, hỏi banned patterns; agent chỉ nói cái đang dùng, không liệt kê cái bị cấm | 30s |
| 3 | [DIAGRAM] | "Cách sửa có ba tầng" | Ba khối: AGENTS.md → Skill → MCP; docs nằm dưới AGENTS.md | 20s |
| 4 | [BROWSER] | "Đây là định dạng mở…" | Mở `agents.md`; highlight 60K+ repo và Agentic AI Foundation | 20s |
| 5 | [BROWSER] | "Kiểm chứng trên Antigravity" | Mở Antigravity Rules docs; highlight `AGENTS.md` và directory scope | 25s |
| 6 | [IDE] | "Tạo docs architecture…" | Voice-over giải thích Hot Memory vs Cold Memory; zoom conditional reading rules | 30s |
| 6b | [DIAGRAM] | "Context window không chứa nổi" | Overlay: repo lớn (nhiều file) vs context window (giới hạn); AGENTS.md chỉ đường đến đúng file | 20s |
| 7 | [IDE] | "Yêu cầu agent đọc toàn bộ code" | Submit prompt audit convention; tua nhanh processing, narration giải thích | 40s |
| 8 | [IDE] | "Agent muốn đưa hash password…" | Dừng tua; highlight đề xuất sai, host phản biện | 25s |
| 9 | [IDE] | "Cho agent tạo AGENTS.md, docs và Skill" | Host approve; agent tạo files; fast-forward | 40s |
| 10 | [BROWSER] | "Antigravity dùng progressive disclosure" | Mở Antigravity Skills docs; highlight discovery → activation → execution | 20s |
| 11 | [IDE] | "Mở git diff và đọc từng file" | Review diff AGENTS.md, docs và Skill; zoom banned patterns section | 30s |
| 12 | [TERM] | "Git diff check, lint và test" | `git diff --check`, `npm run lint`, `npm test`; output xanh | 35s |
| 13 | [IDE] | "Customizations: AGENTS.md và Skill" | Customizations → Rules/Skills; quay cả hai đang active | 20s |
| 14 | [IDE] | "Hỏi lại cùng câu lúc đầu" | Conversation mới; cùng câu banned patterns; agent quote danh sách cấm từ AGENTS.md | 30s |
| 14b | [DIAGRAM] | "Convention drift — AI trôi qua nhiều conversation" | Overlay: 10 conversations không AGENTS.md → code trôi dần; có AGENTS.md → neo giữ | 25s |
| 14c | [DIAGRAM] | "Prompt repetition tax" | Overlay: 50 conversations × cùng instructions = thuế thời gian; AGENTS.md = trả 1 lần | 15s |
| 15 | [IDE] | "Sửa typo README" | Conversation sạch; prompt typo, Skill không kích hoạt | 15s |
| 16 | [DIAGRAM] | "MCP giống cổng USB-C" | Agent ↔ MCP ↔ database/docs/API | 15s |
| 17 | [IDE] | "Workspace đã tắt terminal" | Hỏi count users; agent nói không có bằng chứng | 25s |
| 18 | [IDE] | "Mở MCP Store" | MCP Store → database server → PostgreSQL role SELECT only | 35s |
| 19 | [IDE] | "Hỏi lại cùng câu" | Agent dùng MCP tool, `SELECT count(*)`, trả kết quả thật | 25s |
| 20 | [IDE] | "File cấu hình của Antigravity" | Mở `.agents/mcp_config.json`; highlight `enabledTools` | 20s |
| 21 | [IDE] | "Ba tầng rõ ràng" | Tree view: AGENTS.md, docs/, `.agents/skills/`, `.agents/mcp_config.json` | 15s |
| 21b | [DIAGRAM] | "Ba điều đáng nhớ" | Overlay 3 bullets: (1) AGENTS.md ≠ README (2) Lost in the Middle (3) Stale = bug | 30s |
| 21c | [IDE] | "Legacy code — pattern sai nhiều hơn pattern đúng" | Voice-over trên tree view; nhấn mạnh legacy càng cần AGENTS.md | 15s |
| 22 | [B-ROLL] | Closing | Desk shot, monitor glow, teaser refresh token, fade out | 15s |

**Tổng: 675s ≈ 11:15. Scene 7 và 9 ở fast-forward. 2 cặp contrast: scene 2↔14 (banned patterns) và 17↔19 (MCP). Scene 14b–14c, 21b–21c là voice-over/overlay, không cần quay footage mới — dùng diagram hoặc text overlay trong edit.**

### Diagram assets (đã sinh sẵn, mở Chrome fullscreen rồi record)

| Scene | File |
|---|---|
| 3 — Ba tầng context | `assets/diagrams/scene-03-three-layers.html` |
| 6b — Context window | `assets/diagrams/scene-06b-context-window.html` |
| 14b — Convention drift | `assets/diagrams/scene-14b-convention-drift.html` |
| 14c — Prompt repetition tax | `assets/diagrams/scene-14c-prompt-repetition-tax.html` |
| 16 — MCP USB-C | `assets/diagrams/scene-16-mcp-usbc.html` |
| 21b — Ba điều đáng nhớ | `assets/diagrams/scene-21b-three-takeaways.html` |

### Cấu trúc project files cần tạo khi quay

```text
nestjs-base-with-ai/
├── AGENTS.md                          # Hot Memory
├── docs/
│   ├── architecture.md                # Cold Memory — module map
│   └── database-schema.md             # Cold Memory — Prisma 8 contract
├── .agents/
│   ├── mcp_config.example.json        # mẫu Antigravity, không chứa secret
│   ├── skills/
│   │   └── nest-feature/
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── architecture.md    # deep reference cho skill
└── src/
    └── ...
```

### AGENTS.md mẫu để quay

```markdown
# AGENTS.md — nestjs-base-with-ai

## Stack
NestJS 12, TypeScript 6, Prisma 8, PostgreSQL, Node 24 ESM

## Commands
- Install: `npm install`
- Dev: `npm run start:dev`
- Test: `npm test`
- Lint: `npm run lint`
- E2E: `npm run test:e2e`

## Architecture
When changing module boundaries or dependency direction, read `docs/architecture.md`.

## Database
When changing models, relations or migrations, read `docs/database-schema.md`.
Never use @prisma/client, PrismaClient, or Prisma 7 commands.

## Boundaries
- Controller: thin, no business logic
- Service: explicit business rules, no generic CRUD base
- Repository: contract interface, Prisma adapter separate
- common/: only cross-cutting code with 2+ consumers
```

### SKILL.md mẫu để quay

```markdown
---
name: nest-feature
description: Scaffold or extend a nestjs-base-with-ai NestJS business feature. Use for modules, controllers, services, DTOs and repository boundaries. Do not use for one-line fixes or infrastructure-only changes.
---

Before editing, read `references/architecture.md` and the nearest completed feature.

1. Present the file plan and dependency direction.
2. Wait for approval.
3. Keep controllers thin.
4. Keep business rules explicit in services or use cases.
5. Keep repository contracts independent from Prisma.
6. Never create a generic business CRUD service.
7. For database work, read the Prisma 8 release status and current Prisma 8 docs first.
8. Use contract.prisma, emitted contract artifacts, the Prisma 8 database facade and the Prisma 8 migration workflow.
9. Never use @prisma/client, PrismaClient, client generation, schema.prisma, migrate dev or migrate deploy.
10. Run contract emit and migration check when the contract changes; then run lint, tests and show the diff summary.
```

### Nguồn chính thức — mở trên màn hình khi quay

| Topic | URL |
|---|---|
| AGENTS.md spec | `https://agents.md` |
| Antigravity Rules | `https://www.antigravity.google/docs/rules/` |
| Antigravity Skills | `https://www.antigravity.google/docs/skills?tab=ide` |
| Antigravity MCP | `https://www.antigravity.google/docs/mcp/` |
| Agent Skills standard | `https://agentskills.io` |
| MCP Protocol | `https://modelcontextprotocol.io` |

### Bảng so sánh Agent Config — overlay khi quay

```text
┌─────────────────────┬───────────────────────────────────────┬──────────────┐
│ Tool                │ File / Folder                         │ AGENTS.md?   │
├─────────────────────┼───────────────────────────────────────┼──────────────┤
│ Antigravity         │ AGENTS.md + .agents/rules/*.md         │ ✅ native    │
│ Codex               │ AGENTS.md, hỗ trợ nested files         │ ✅ native    │
│ Cursor              │ .cursor/rules/*.mdc + AGENTS.md        │ ✅ recognized│
│ GitHub Copilot      │ .github/copilot-instructions.md        │ ✅ coding agent│
│ Claude Code         │ CLAUDE.md hoặc AGENTS.md               │ ✅ supported │
└─────────────────────┴───────────────────────────────────────┴──────────────┘
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese developer sitting in a dark room, neon monitor glow reflecting on their face, the screen shows a glowing file tree with AGENTS.md highlighted in green, code syntax in cyan on dark background, city bokeh through window, shallow depth of field, subject on right leaving empty dark space on left, 16:9, 8k, photorealistic like a high-end tech documentary. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic close-up of a dark IDE monitor showing three scattered configuration files merging into one glowing AGENTS.md file, neon green and cyan syntax highlighting on dark background, dramatic rim lighting in purple, code reflecting on developer glasses in foreground, empty left side for text, 16:9, 8k, photorealistic developer documentary style. Not a tutorial screenshot, not cartoon.`

3. `A cinematic late-night coding desk photograph with a developer reviewing a luminous architecture diagram on screen, three connected glowing nodes labeled with abstract code symbols, dark moody background with neon green and cyan accents, mechanical keyboard in foreground, city lights bokeh, subject positioned right, 16:9, 8k, photorealistic tech commercial feel. Not a screenshot, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (10)

1. AGENTS.md: Một file, nhiều coding agent cùng đọc — NestJS EP06 | Lập trình là cuộc sống
2. Dạy AI nhớ convention bằng 3 tầng context — NestJS EP06 | Lập trình là cuộc sống
3. Code nói cái đang dùng, AGENTS.md nói cái bị cấm — NestJS EP06 | Lập trình là cuộc sống
4. AGENTS.md, Skills, MCP: Bộ ba context cho AI coding — EP06 | Lập trình là cuộc sống
5. Tại sao AI cùng project mà code kiểu khác nhau? — NestJS EP06 | Lập trình là cuộc sống
6. Hot Memory và Cold Memory: AI đọc đúng, nhớ đúng — EP06 | Lập trình là cuộc sống
7. Viết AGENTS.md cho NestJS: convention một lần, dùng nhiều agent — EP06 | Lập trình là cuộc sống
8. Convention sống trong repo, không phải trong prompt — NestJS EP06 | Lập trình là cuộc sống
9. Agent Skill + MCP: upgrade AI từ autocomplete thành teammate — EP06 | Lập trình là cuộc sống
10. AI biết cái đang có, nhưng không biết cái bị cấm — NestJS EP06 | Lập trình là cuộc sống

### 4b. SEO Description

```text
AI đọc code rất giỏi. Nhưng convention không phải code. Cái gì bị cấm, workflow chạy thứ tự nào — những thứ này nằm trong đầu bạn, không nằm trong source code. EP06 biến kinh nghiệm đó thành file AI đọc được.

✅ AGENTS.md — định dạng mở được nhiều coding agent hỗ trợ
✅ docs/ — Cold Memory: schema, kiến trúc, AI chỉ đọc khi cần
✅ Agent Skill — đóng gói workflow scaffold feature thành SKILL.md
✅ MCP — Model Context Protocol, kết nối AI với database/API
✅ Demo: banned patterns contrast — trước và sau AGENTS.md
✅ Demo: MCP trước và sau — agent query database thật

🔗 AGENTS.md spec: https://agents.md
🔗 Antigravity Rules: https://www.antigravity.google/docs/rules/
🔗 Antigravity Skills: https://www.antigravity.google/docs/skills?tab=ide
🔗 Antigravity MCP: https://www.antigravity.google/docs/mcp/
🔗 Agent Skills standard: https://agentskills.io
🔗 MCP Protocol: https://modelcontextprotocol.io

⏱ 0:00 AI đọc code tốt, nhưng convention ≠ code
⏱ 0:30 Hỏi banned patterns — AI không biết
⏱ 1:30 AGENTS.md — universal standard
⏱ 2:45 Tạo AGENTS.md + docs/ (Hot vs Cold Memory)
⏱ 4:30 Agent Skill — progressive disclosure
⏱ 5:30 Viết SKILL.md cho nestjs-base-with-ai
⏱ 7:00 Kiểm chứng: banned patterns + scope test
⏱ 8:00 MCP Store và trước/sau
⏱ 9:00 Toàn cảnh 3 tầng context

#AGENTS_md #AgentSkill #MCP #NestJS #AICoding #PromptEngineering #SoftwareArchitecture #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
AGENTS.md, agents md nestjs, Antigravity rules, Antigravity skills, agent skill, SKILL.md, MCP model context protocol, mcp_config.json, hot memory cold memory, ai coding convention, progressive disclosure ai, scaffold nestjs bằng ai, nestjs tập 6, ai context management, prompt engineering coding, ai coding workflow, banned patterns ai, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng

**Image prompt:**
`A cinematic photograph of a developer silhouette illuminated by dramatic neon green and cyan light from a massive monitor showing a glowing AGENTS.md file, code text floating and reflecting in the dark scene, deep shadows with city bokeh and rain outside window, high contrast, dramatic rim lighting, subject positioned on the right side leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

**Text spec:**
- Line 1: `CODE NÓI` — WHITE `#FFFFFF`
- Line 2: `CÁI ĐANG CÓ` — WHITE `#FFFFFF`
- Line 3: `AGENTS.MD NÓI` — NEON GREEN `#00FF41`
- Line 4: `CÁI BỊ CẤM` — NEON GREEN `#00FF41`

### Option 2

**Image prompt:**
`A cinematic photograph of three scattered glowing configuration files converging into one bright central AGENTS.md file on a dark coding desk, extreme neon lighting in green and purple, code elements floating and exaggerated, deep moody shadows, fog and bokeh, subject area on right, large empty dark space on left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

**Text spec:**
- Line 1: `MỘT FILE` — WHITE `#FFFFFF`
- Line 2: `NHIỀU AGENT` — NEON GREEN `#00FF41`
- Line 3: `CÙNG ĐỌC` — NEON GREEN `#00FF41`

### Option 3

**Image prompt:**
`A cinematic photograph of a Vietnamese developer in dramatic rim lighting reviewing a luminous three-layer architecture diagram floating above their dark desk, neon green cyan and purple glow, code syntax reflected on their glasses, city lights through rain-streaked window, subject right side, empty dark left space, 8k, 16:9. Photorealistic, not cartoon or illustration.`

**Text spec:**
- Line 1: `DẠY AI` — WHITE `#FFFFFF`
- Line 2: `NHỚ PROJECT` — NEON GREEN `#00FF41`
- Badge: `3 TẦNG CONTEXT` — small, dark badge `#1a1a2e` with neon border

### Typography specs (áp dụng cả 3 options)

- Canvas 1280×720
- Font: **Anton** (impact) cho hook lines, **JetBrains Mono** (code feel) cho badge/technical terms
- Text block height: mỗi dòng 15–20% frame height (~110–140px trên 1280×720)
- Line spacing 0.85
- Text block: ~1/3 frame width, left side
- Neon glow: duplicate text layer, blur 10px, matching neon color, opacity 65%
- Black outline/stroke 8px trên mọi chữ
- KHÔNG overlap text lên face
- Scan-line noise texture overlay nhẹ trên background
- **Typeset trong Canva.** Giữ bản nền không chữ để dùng lại.

---

## Facts & Sources — Đã kiểm chứng Oct 2026

> [!IMPORTANT]
> Mọi fact dưới đây đã kiểm chứng từ primary source documentation, không từ search summary.

| Fact | Source |
|---|---|
| Antigravity nạp `AGENTS.md` như rule luôn bật theo directory scope | [Antigravity Rules](https://www.antigravity.google/docs/rules/) — "Directory-scoped rules" |
| Antigravity hiển thị rule và skill đang active trong Customizations | [Antigravity Rules](https://www.antigravity.google/docs/rules/) và [Skills](https://www.antigravity.google/docs/skills?tab=ide) |
| Antigravity discover workspace Skill tại `.agents/skills/<name>/SKILL.md` | [Antigravity Skills](https://www.antigravity.google/docs/skills?tab=ide) — "Antigravity IDE skill locations" |
| Antigravity Skill dùng progressive disclosure: discovery → activation → execution | [Antigravity Skills](https://www.antigravity.google/docs/skills?tab=ide) — "How the agent uses skills" |
| Antigravity workspace MCP config nằm tại `.agents/mcp_config.json`; có `enabledTools` và `disabledTools` | [Antigravity MCP](https://www.antigravity.google/docs/mcp/) |
| Codex tự tìm AGENTS.md theo cây thư mục, file gần hơn có độ ưu tiên cao hơn | [OpenAI Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) — section "Using agents.md" |
| GitHub Copilot đọc AGENTS.md (+ CLAUDE.md, GEMINI.md fallback) | [GitHub docs](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) — section "Agent instructions" |
| Copilot: repo-wide = `.github/copilot-instructions.md`, path-specific = `.github/instructions/*.instructions.md` | GitHub docs — section "Creating custom instructions" |
| Cursor: `.cursor/rules/*.mdc` với YAML frontmatter (description, globs, alwaysApply) | [Cursor Rules](https://cursor.com/docs/rules) |
| MCP là chuẩn mở kết nối ứng dụng AI với data, tools và workflows; config thuộc từng client | [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro) |
| AGENTS.md managed by Agentic AI Foundation (Linux Foundation) | agents.md website |
| Convention drift: AI output trôi dần khi không có rule file cố định qua nhiều conversation stateless | [Reddit — r/ClaudeAI discussion](https://www.reddit.com/r/ClaudeAI/) · [amattn.com — context compaction drift](https://amattn.com) |
| Lost in the Middle: LLM chú ý mạnh nhất ở đầu và cuối context, phần giữa bị giảm attention | [Liu et al. 2023 — "Lost in the Middle"](https://arxiv.org/abs/2307.03172) · [Anthropic — Claude Code best practices](https://docs.anthropic.com/en/docs/claude-code) |
| AGENTS.md ≠ README.md: README cho người đọc (onboarding), AGENTS.md cho máy thực thi (commands, boundaries) | [AAIF best practices](https://aaif.io) · [Packmind analysis](https://packmind.com) |
| Stale AGENTS.md = injected hallucination: rule lỗi thời chủ động inject thông tin sai vào mọi conversation | [Promptessor — AGENTS.md maintenance](https://promptessor.com) · [AI Hero — instruction budget](https://aihero.dev) |
| Prompt repetition tax: không có rule file → developer lặp cùng instruction mỗi conversation | Derived from convention drift pattern; community consensus across r/ClaudeAI, r/cursor |
