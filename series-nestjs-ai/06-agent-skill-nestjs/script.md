# NestJS #06 — AGENTS.md, Skills và MCP: Dạy AI nhớ project

- **Series:** Học NestJS bằng AI — tập 6
- **Target runtime:** 9–11 phút (~810 từ thoại + khoảng nghỉ review/diff)
- **Outcome:** Viewer hiểu 3 tầng context cho AI coding agent: project rules (AGENTS.md), on-demand workflow (Skills), tool connectivity (MCP). Áp dụng cho TaskFlow NestJS project.
- **Pain mở EP07:** Access token ngắn hạn an toàn nhưng buộc người dùng đăng nhập lại liên tục.

---

## PART 1 — SCRIPT

AI vừa tạo hai module trong cùng một project. Một module theo convention. Module kia như code của đội khác.

Bạn nhắc lại rule trong prompt. Conversation mới, rule biến mất. Prompt dài hơn, nhưng code chưa chắc nhất quán hơn.

Vấn đề không phải AI lười. Convention của project đang nằm sai chỗ.

Cách sửa có ba tầng. AGENTS.md giữ rule luôn cần. Skill giữ workflow theo nhu cầu. MCP nối agent với tool bên ngoài.

Bắt đầu với AGENTS.md. Đây là định dạng mở dành cho coding agent. Hơn sáu mươi nghìn repo mã nguồn mở đã dùng.

Agentic AI Foundation thuộc Linux Foundation đang quản lý định dạng này. Antigravity, Codex, Cơ-xờ và nhiều agent khác đều hỗ trợ.

Nhưng hỗ trợ không có nghĩa mọi tool nạp giống nhau. Tập này mình kiểm chứng trên đúng công cụ đang dùng: Antigravity.

Mình tạo AGENTS.md ở root TaskFlow. Antigravity xem file này là rule luôn bật cho workspace.

Mình mở Customizations. AGENTS.md xuất hiện trong danh sách active rules. Đây mới là bằng chứng, không phải tên file.

File này chỉ giữ những điều bền vững. Stack, lệnh kiểm chứng và ranh giới kiến trúc.

Mình tự đặt giới hạn một trăm năm mươi dòng. Đây là convention của TaskFlow, không phải giới hạn của chuẩn.

Kiến trúc chi tiết thì dài. Nếu nhét hết vào rule, context bị tốn cho những thứ chưa cần.

Nên mình tạo docs architecture và database schema. AGENTS.md ghi rõ lúc nào agent phải đọc từng file.

Khi đổi boundary module, đọc architecture. Khi đổi model, đọc database schema. Một đường dẫn không có điều kiện chỉ là biển chỉ đường mơ hồ.

Mình gọi AGENTS.md là Hot Memory. Docs là Cold Memory. Đây là cách gọi trong TaskFlow, không phải thuật ngữ của chuẩn.

Giờ đến Skill. AGENTS.md nói điều luôn đúng. Skill mô tả một workflow chỉ dùng khi task phù hợp.

Mình yêu cầu agent đọc Users và Auth. Sau đó, nó đề xuất convention chung cho feature NestJS.

Agent muốn đưa rule hash password vào Skill. Mình từ chối. Đó là business rule của Auth, không phải kiến trúc chung.

Đây là bước review bằng mắt. AI đề xuất. Người hiểu project quyết định.

Sau khi duyệt plan, mình cho agent tạo AGENTS.md, docs và nest-feature Skill.

Antigravity dùng progressive disclosure. Ban đầu, agent chỉ thấy tên và description của Skill.

Khi task phù hợp, agent mới đọc toàn bộ instruction. Context không phải gánh mọi workflow trong mọi conversation.

Description là bộ định tuyến. Mình ghi rõ Skill dùng cho business feature. Sửa typo hoặc config nhỏ thì không dùng.

AI làm xong, mình không tin ngay. Mình mở git diff và đọc từng file.

Mình chạy git diff check, lint và test. Tất cả đều xanh. Chu trình sáu bước kết thúc ở đây.

Mình mở Customizations lần nữa. AGENTS.md và Skill đều xuất hiện. Bây giờ mới tới kiểm chứng routing.

Trong conversation mới, mình yêu cầu plan Roles và Permissions. Mình không gọi tên Skill.

Agent tự chọn đúng Skill. Nó đọc feature lân cận, trình file plan và dừng lại chờ approve.

Mình kiểm tra dependency direction. Controller gọi service. Service phụ thuộc contract. Adapter mới biết Prisma.

Skill không làm AI thông minh hơn. Nó biến kinh nghiệm đã kiểm chứng thành quy trình có thể lặp lại.

Mình mở conversation sạch khác và yêu cầu sửa typo README. Skill không kích hoạt. Scope đang hoạt động đúng.

Tầng cuối là MCP, viết tắt của Model Context Protocol. Đây là chuẩn mở để nối ứng dụng AI với hệ thống bên ngoài.

MCP giống cổng USB-C cho agent. Server có thể cung cấp database, docs, API hoặc tool chuyên biệt.

Antigravity hiện hỗ trợ MCP Store và workspace config. File của project nằm tại .agents, mcp_config.json.

Nhưng file này là cấu hình của Antigravity, không phải config chung cho mọi client. Đổi tool vẫn phải đọc docs của tool đó.

Mình mở MCP Store, chọn một server chỉ đọc và xem danh sách tool. Mình chỉ bật tool cần dùng.

Quyền truy cập cũng là code. Cấp thừa một tool hôm nay có thể thành sự cố ngày mai.

Giờ TaskFlow có ba tầng rõ ràng. Rule luôn bật. Workflow nạp theo nhu cầu. Kết nối ngoài được cấp quyền có chủ đích.

Convention tốt không khóa AI lại. Nó giúp người và AI cùng hiểu project sau sáu tháng.

Link Git của nhánh này nằm trong description. Bạn có thể comment convention khó giữ nhất trong project của mình.

Tập sau, ta thêm refresh token rotation và khả năng thu hồi session. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

> **Setup chung:** IDE One Dark Pro, font JetBrains Mono ≥18px, hide sidebar/minimap khi quay close-up. Che thông tin tài khoản.

| # | Type | Narration match | Nội dung quay | Thời lượng |
|---|---|---|---|---:|
| 1 | [IDE] | "AI vừa tạo hai module…" | Split view hai module cố ý khác convention; highlight dependency và folder lệch nhau | 20s |
| 2 | [DIAGRAM] | "Cách sửa có ba tầng" | Ba khối: AGENTS.md → Skill → MCP; docs nằm dưới AGENTS.md như nguồn đọc theo điều kiện | 20s |
| 3 | [BROWSER] | "Đây là định dạng mở…" | Mở `agents.md`; highlight 60K+ repo và Agentic AI Foundation | 20s |
| 4 | [BROWSER] | "Kiểm chứng trên Antigravity" | Mở Antigravity Rules docs; highlight `AGENTS.md` và directory scope | 25s |
| 5 | [IDE] | "Tạo AGENTS.md ở root" | Submit prompt tạo file; tua nhanh agent xử lý, voice-over giải thích Hot Memory | 40s |
| 6 | [IDE] | "Mở Customizations" | Agent side panel → Customizations → Rules; quay rõ AGENTS.md đang active | 25s |
| 7 | [IDE] | "Tạo docs architecture…" | Tạo `docs/architecture.md`, `docs/database-schema.md`; zoom hai rule có điều kiện đọc | 35s |
| 8 | [IDE] | "Yêu cầu agent đọc Users và Auth" | Submit prompt audit convention; tua nhanh processing, narration giải thích rule chung và riêng | 45s |
| 9 | [IDE] | "Agent muốn đưa hash password…" | Dừng tua; highlight đề xuất sai, host phản biện và yêu cầu bỏ business rule | 30s |
| 10 | [IDE] | "Cho agent tạo AGENTS.md, docs và Skill" | Host approve; agent tạo các file đã duyệt; quay processing ở fast-forward | 45s |
| 11 | [BROWSER] | "Antigravity dùng progressive disclosure" | Mở Antigravity Skills docs; highlight discovery → activation → execution | 20s |
| 12 | [IDE] | "Mở git diff và đọc từng file" | Review diff AGENTS.md, docs và Skill; zoom các rule quan trọng | 35s |
| 13 | [TERM] | "Git diff check, lint và test" | `git diff --check`, `git diff --stat`, `npm run lint`, `npm test`; giữ output xanh | 45s |
| 14 | [IDE] | "AGENTS.md và Skill đều xuất hiện" | Customizations → Rules/Skills; quay `AGENTS.md` và `nest-feature` đang active | 30s |
| 15 | [IDE] | "Conversation mới… Roles và Permissions" | Prompt tự nhiên, không gọi tên Skill; agent trả plan và dừng, tuyệt đối chưa edit | 45s |
| 16 | [IDE] | "Kiểm tra dependency direction" | Review plan; highlight controller → service → contract ← adapter | 30s |
| 17 | [IDE] | "Sửa typo README" | Conversation sạch; prompt typo, kiểm tra context để chứng minh Skill không được dùng | 20s |
| 18 | [DIAGRAM] | "MCP giống cổng USB-C" | Agent ↔ MCP ↔ database/docs/API; animation nhẹ từng kết nối | 20s |
| 19 | [IDE] | "Antigravity hỗ trợ MCP Store…" | Mở MCP Servers; quay Store, raw config và đường dẫn `.agents/mcp_config.json` | 35s |
| 20 | [IDE] | "Chỉ bật tool cần dùng" | Mở config mẫu; highlight `enabledTools`, không lộ token hoặc credential | 25s |
| 21 | [IDE] | "Ba tầng rõ ràng" | Tree view: AGENTS.md, docs/, `.agents/skills/`, `.agents/mcp_config.example.json` | 20s |
| 22 | [B-ROLL] | Closing | Desk shot, monitor glow, chuyển sang teaser refresh token rồi fade out | 20s |

**Tổng: 650s ≈ 10:50. Giữ scene 5, 8 và 10 ở fast-forward để không có dead time.**

### Cấu trúc project files cần tạo khi quay

```text
taskflow/
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
# AGENTS.md — TaskFlow

## Stack
NestJS 12, TypeScript 5.9+, Prisma 8, PostgreSQL, Node 24 ESM

## Commands
- Install: `npm install`
- Dev: `npm run start:dev`
- Test: `npm test`
- Lint: `npm run lint`
- E2E: `npm run test:e2e`

## Architecture
See `docs/architecture.md` for module dependency map and DI direction.

## Database
See `docs/database-schema.md` for Prisma 8 contract and relations.
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
description: Scaffold or extend a TaskFlow NestJS business feature. Use for modules, controllers, services, DTOs and repository boundaries. Do not use for one-line fixes or infrastructure-only changes.
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

### Prompt kiểm chứng auto-trigger

```text
Plan Roles and Permissions inside the TaskFlow access-control domain using
the existing project conventions.
Do not edit. Show the files, dependency direction, business rules and
verification commands.
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
2. Dạy AI nhớ project bằng 3 tầng context — NestJS EP06 | Lập trình là cuộc sống
3. Đừng copy convention 3 lần cho 3 tool AI — NestJS EP06 | Lập trình là cuộc sống
4. AGENTS.md, Skills, MCP: Bộ ba context cho AI coding — EP06 | Lập trình là cuộc sống
5. Tại sao AI cùng project mà code kiểu khác nhau? — NestJS EP06 | Lập trình là cuộc sống
6. Hot Memory và Cold Memory: AI đọc đúng, nhớ đúng — EP06 | Lập trình là cuộc sống
7. Viết AGENTS.md cho NestJS: convention một lần, dùng nhiều agent — EP06 | Lập trình là cuộc sống
8. 3 file convention, 3 tool AI, 0 nhất quán — NestJS EP06 | Lập trình là cuộc sống
9. Agent Skill + MCP: upgrade AI từ autocomplete thành teammate — EP06 | Lập trình là cuộc sống
10. Convention sống trong repo, không phải trong prompt — NestJS EP06 | Lập trình là cuộc sống

### 4b. SEO Description

```text
Nhiều AI tool có cơ chế convention riêng. Copy-paste qua lại giữa nhiều file rồi quên cập nhật. EP06 giải quyết bằng 3 tầng context:

✅ AGENTS.md — định dạng mở được nhiều coding agent hỗ trợ; cách nạp và ưu tiên tùy client
✅ docs/ — Cold Memory: schema, kiến trúc, ADR, AI chỉ đọc khi cần
✅ Agent Skill — đóng gói workflow scaffold feature thành SKILL.md
✅ MCP — Model Context Protocol, kết nối AI với database/API
✅ Progressive disclosure: AI chỉ nạp context cần thiết
✅ Demo: tạo AGENTS.md + Skill theo đủ workflow plan → review → approve → code → verify
✅ Kiểm chứng: skill không kích hoạt khi prompt không liên quan

🔗 AGENTS.md spec: https://agents.md
🔗 Antigravity Rules: https://www.antigravity.google/docs/rules/
🔗 Antigravity Skills: https://www.antigravity.google/docs/skills?tab=ide
🔗 Antigravity MCP: https://www.antigravity.google/docs/mcp/
🔗 Agent Skills standard: https://agentskills.io
🔗 MCP Protocol: https://modelcontextprotocol.io

⏱ 0:00 3 file, cùng nội dung, copy-paste — pain
⏱ 0:55 AGENTS.md — universal standard
⏱ 2:15 Tạo AGENTS.md + docs/ (Hot vs Cold Memory)
⏱ 4:00 Agent Skill — progressive disclosure
⏱ 5:30 Viết SKILL.md cho TaskFlow
⏱ 7:00 Kiểm chứng: diff/test + auto-route Skill
⏱ 8:45 MCP Store và quyền truy cập
⏱ 9:30 Toàn cảnh 3 tầng context

#AGENTS_md #AgentSkill #MCP #NestJS #AICoding #PromptEngineering #SoftwareArchitecture #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
AGENTS.md, agents md nestjs, Antigravity rules, Antigravity skills, agent skill, SKILL.md, MCP model context protocol, mcp_config.json, hot memory cold memory, ai coding convention, progressive disclosure ai, scaffold nestjs bằng ai, nestjs tập 6, ai context management, prompt engineering coding, ai coding workflow, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng

**Image prompt:**
`A cinematic photograph of a developer silhouette illuminated by dramatic neon green and cyan light from a massive monitor showing a glowing AGENTS.md file, code text floating and reflecting in the dark scene, deep shadows with city bokeh and rain outside window, high contrast, dramatic rim lighting, subject positioned on the right side leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

**Text spec:**
- Line 1: `MỘT FILE` — WHITE `#FFFFFF`
- Line 2: `NHIỀU AGENT` — NEON GREEN `#00FF41`
- Line 3: `CÙNG ĐỌC` — NEON GREEN `#00FF41`

### Option 2

**Image prompt:**
`A cinematic photograph of three scattered glowing configuration files converging into one bright central AGENTS.md file on a dark coding desk, extreme neon lighting in green and purple, code elements floating and exaggerated, deep moody shadows, fog and bokeh, subject area on right, large empty dark space on left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

**Text spec:**
- Line 1: `3 FILE` — NEON GREEN `#00FF41`
- Line 2: `CONVENTION` — WHITE `#FFFFFF`
- Line 3: `0 NHẤT QUÁN` — NEON GREEN `#00FF41`

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
| Antigravity nạp `AGENTS.md` như rule luôn bật theo directory scope | [Antigravity Rules](https://www.antigravity.google/docs/rules/) — “Directory-scoped rules” |
| Antigravity hiển thị rule và skill đang active trong Customizations | [Antigravity Rules](https://www.antigravity.google/docs/rules/) và [Skills](https://www.antigravity.google/docs/skills?tab=ide) |
| Antigravity discover workspace Skill tại `.agents/skills/<name>/SKILL.md` | [Antigravity Skills](https://www.antigravity.google/docs/skills?tab=ide) — “Antigravity IDE skill locations” |
| Antigravity Skill dùng progressive disclosure: discovery → activation → execution | [Antigravity Skills](https://www.antigravity.google/docs/skills?tab=ide) — “How the agent uses skills” |
| Antigravity workspace MCP config nằm tại `.agents/mcp_config.json`; có `enabledTools` và `disabledTools` | [Antigravity MCP](https://www.antigravity.google/docs/mcp/) |
| Codex tự tìm AGENTS.md theo cây thư mục, file gần hơn có độ ưu tiên cao hơn | [OpenAI Codex Prompting Guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) — section "Using agents.md" |
| GitHub Copilot đọc AGENTS.md (+ CLAUDE.md, GEMINI.md fallback) | [GitHub docs](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) — section "Agent instructions" |
| Copilot: repo-wide = `.github/copilot-instructions.md`, path-specific = `.github/instructions/*.instructions.md` | GitHub docs — section "Creating custom instructions" |
| Cursor: `.cursor/rules/*.mdc` với YAML frontmatter (description, globs, alwaysApply) | [Cursor Rules](https://cursor.com/docs/rules) |
| MCP là chuẩn mở kết nối ứng dụng AI với data, tools và workflows; config thuộc từng client | [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro) |
| AGENTS.md managed by Agentic AI Foundation (Linux Foundation) | agents.md website |
