# NestJS #06 — AGENTS.md, Skills và MCP: Dạy AI nhớ project

- **Series:** Học NestJS bằng AI — tập 6
- **Target runtime:** 10–12 phút (~900–1100 từ thoại)
- **Outcome:** Viewer hiểu 3 tầng context cho AI coding agent: project rules (AGENTS.md), on-demand workflow (Skills), tool connectivity (MCP). Áp dụng cho TaskFlow NestJS project.
- **Pain mở EP07:** Access token ngắn hạn an toàn nhưng buộc người dùng đăng nhập lại liên tục.

---

## PART 1 — SCRIPT

Cài Cơ-xờ, tạo `.cursorrules`. Cài Claude Code, tạo `CLAUDE.md`. Cài thêm Copilot, tạo `copilot-instructions.md`. Ba file. Cùng nội dung. Copy-paste qua lại. Đổi convention ở file A, quên cập nhật file B và C.

Thiếu convention thì còn tệ hơn. AI từ mỗi tool sinh code kiểu khác nhau. Cùng một project, hai folder cấu trúc hai kiểu.

Thử nhồi convention vào prompt. Mỗi lần paste lại một đoạn dài. Rồi prompt dài quá, AI chú ý đoạn đầu, quên rule ở giữa.

Vấn đề không phải AI lười. Mà convention chưa nằm đúng chỗ.

Giải pháp có ba tầng. Tầng một: dạy AI quy tắc project bằng một file mọi tool đều đọc. Tầng hai: đóng gói workflow lặp lại thành Skill. Tầng ba: kết nối AI với database, docs, API bằng MCP.

Bắt đầu từ tầng một. Năm hai nghìn hai mươi sáu, mỗi AI tool vẫn có file riêng. Claude Code đọc `CLAUDE.md`. Cơ-xờ đọc file `.mdc` trong `.cursor/rules/`. Copilot đọc `.github/copilot-instructions.md`. Kiro dùng file steering trong `.kiro/steering/`.

Nhưng có một chuẩn đang được mọi tool chấp nhận: `AGENTS.md`. File do Agentic AI Foundation quản lý — thuộc Linux Foundation. Sáu mươi nghìn repo đã dùng.

Quan trọng nhất cho series này: Claude Code từ bản hai chấm một chấm hai trăm bảy mươi bảy — tự đọc `AGENTS.md` nếu không có `CLAUDE.md`. Copilot cũng đọc AGENTS.md. Windsurf đọc AGENTS.md ở root như rule luôn bật. Kiro cũng đọc.

Vậy nên mình không tạo CLAUDE.md cho TaskFlow. Mình tạo `AGENTS.md`.

Giờ mình mở TaskFlow. Tạo `AGENTS.md` ở root. File này là "Hot Memory" — luôn được AI nạp vào context. Nên phải ngắn. Dưới một trăm năm mươi dòng.

Viết gì trong đó? Stack, build commands, coding boundaries. Những thứ AI cần biết mọi lúc.

Nhưng schema database, kiến trúc chi tiết, quyết định thiết kế — những thứ đó dài. Nếu nhồi hết vào AGENTS.md, context window bị ngập. Rule quan trọng bị AI bỏ quên vì kẹt giữa đống text.

Nên mình tách ra. Tạo folder `docs/` ngay trong source code. `docs/architecture.md` cho module map. `docs/database-schema.md` cho Prisma tám contract. AGENTS.md chỉ giữ rules cứng và trỏ tới docs: "See `docs/architecture.md` for module dependency direction."

Đây gọi là "Cold Memory". AI không đọc lúc khởi tạo. Chỉ đọc khi chạm vào phần liên quan.

Claude Code hỗ trợ cú pháp `@` để import. Viết `@docs/architecture.md` trong CLAUDE.md hoặc AGENTS.md, Claude Code inline nội dung đó vào context khi load. Giê-mi-ni, Antigravity cũng đọc thư mục docs nếu agent cần.

Mình demo trên màn hình. Mở Claude Code trong TaskFlow. Nó tự nhận AGENTS.md. Không cần tạo CLAUDE.md riêng. Convention giữ đúng với mọi tool.

Giờ qua tầng hai: Skill.

AGENTS.md giữ rules. Nhưng mỗi lần scaffold feature mới, mình lại paste cùng một danh sách bước. Thiếu một dòng, cấu trúc lệch.

Skill đóng gói bước đó thành workflow tái sử dụng. Tạo file `SKILL.md` trong `.agents/skills/nest-feature/`. Mình thích đặt trong `.agents/` vì theo chuẩn Agent Skills — chuẩn mở tại `agentskills.io`, Claude Code cũng hỗ trợ.

Skill dùng progressive disclosure. Ban đầu agent chỉ thấy tên và description. Khi prompt khớp, agent mới đọc toàn bộ instruction. Context không bị ngập bởi workflow không liên quan.

Description không phải lời quảng cáo. Nó là bộ định tuyến. Viết rõ: "Use for modules, controllers, services, DTOs. Do not use for one-line fixes."

Mình yêu cầu AI đọc Users và Auth, đề xuất phần nào đủ ổn định để đưa vào skill.

AI muốn ghi rule "register phải hash password". Rule đó chỉ thuộc Auth. Mình loại. Skill giữ file layout, dependency direction và workflow plan-first. Convention cụ thể từng domain giữ trong service.

Bây giờ kiểm chứng. Conversation mới. Yêu cầu scaffold Roles và Permissions theo convention TaskFlow.

Agent nhận đúng skill. Đọc cấu trúc repo. Chỉ đưa plan, không sửa file. Plan dùng contract Prisma tám, adapter riêng biệt. Không lặp snippet Prisma bảy từ mạng.

Thử prompt không liên quan: sửa typo README. Skill không kích hoạt. Đúng vậy — description scope rõ nên agent bỏ qua.

Tầng ba — MCP. Model Context Protocol.

MCP giống ổ cắm USB chuẩn. Cắm một đầu vào AI tool. Đầu kia vào database, docs, hoặc API. AI đọc và ghi trực tiếp, không cần bạn copy-paste.

Mọi tool lớn đều hỗ trợ: Claude Code, Cơ-xờ, Antigravity, Kiro. Chuẩn mở tại `modelcontextprotocol.io`.

Config nằm trong `.agents/mcp_config.json` hoặc tùy tool. Mình không demo cài MCP server ngay tập này — TaskFlow chưa đến mức cần. Nhưng bạn cần biết nó tồn tại. Khi project phức tạp hơn — cần đọc database, cần kéo docs từ API — MCP là cách kết nối.

Quay lại nhìn toàn bộ. AGENTS.md, `docs/`, Skill, MCP config. Tất cả nằm trong repo. Đổi tool vẫn giữ convention. AI biết kiến trúc trước khi viết dòng đầu tiên.

Convention tốt không phải để kiểm soát AI. Nó để AI và người cùng đọc được dự án sau sáu tháng.

Nhưng access token hiện hết hạn là phiên bị ngắt. Tập sau, ta thêm refresh token rotation và khả năng thu hồi session. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

> **Setup chung:** IDE One Dark Pro, font JetBrains Mono ≥18px, hide sidebar/minimap khi quay close-up. Che thông tin tài khoản.

| # | Type | Narration match | Nội dung quay | Thời lượng |
|---|---|---|---|---:|
| 1 | [IDE] | "Cài Cơ-xờ… ba file, cùng nội dung" | Mở 3 tab: `.cursorrules`, `CLAUDE.md`, `copilot-instructions.md` — highlight cùng convention copy-paste | 25s |
| 2 | [IDE] | "Thiếu convention… hai folder cấu trúc hai kiểu" | Split view 2 folder có structure khác nhau trong cùng project | 20s |
| 3 | [IDE] | "Vấn đề không phải AI lười" | Xóa 3 file, để blank — setup cho giải pháp | 10s |
| 4 | [DIAGRAM] | "Giải pháp có ba tầng" | Diagram: 3 layers — AGENTS.md (Hot) → docs/ (Cold) → Skills (On-demand) → MCP (Connectivity) | 20s |
| 5 | [IDE] | "Mỗi AI tool vẫn có file riêng" | Bảng so sánh trên màn hình (overlay hoặc markdown table): Claude/Cursor/Copilot/Windsurf/Kiro + file paths | 25s |
| 6 | [BROWSER] | "AGENTS.md. File do Agentic AI Foundation" | Mở trang `agents.md` — highlight "universal standard", 60K+ repos | 20s |
| 7 | [BROWSER] | "Claude Code từ bản…tự đọc AGENTS.md" | Mở Claude Code docs `code.claude.com/docs/en/memory.md` — highlight fallback behavior table | 25s |
| 8 | [IDE] | "Mình tạo AGENTS.md ở root" | Tạo file AGENTS.md, viết Stack + Commands + Boundaries (live typing hoặc fast-forward) | 40s |
| 9 | [IDE] | "Tạo folder docs/… Cold Memory" | Tạo `docs/architecture.md` + `docs/database-schema.md`. Show tree structure | 30s |
| 10 | [IDE] | "AGENTS.md chỉ giữ rules cứng… trỏ tới docs" | Viết "See docs/architecture.md" trong AGENTS.md | 15s |
| 11 | [IDE] | "Claude Code hỗ trợ cú pháp @" | Show `@docs/architecture.md` syntax trong CLAUDE.md (giải thích import) | 15s |
| 12 | [TERM] | "Mở Claude Code trong TaskFlow" | Chạy `claude` trong terminal TaskFlow. Show "AGENTS.md loaded" message | 25s |
| 13 | [IDE] | "Skill đóng gói bước đó thành workflow" | Tạo `.agents/skills/nest-feature/SKILL.md`. Show progressive disclosure concept | 35s |
| 14 | [IDE] | "Description không phải lời quảng cáo" | Zoom vào frontmatter: `name`, `description` với trigger + non-trigger | 20s |
| 15 | [IDE] | "AI muốn ghi rule hash password… mình loại" | AI suggest → host reject → keep only structural rules. Fast-forward AI response, voice-over explain | 40s |
| 16 | [IDE] | "Kiểm chứng. Conversation mới" | Prompt: scaffold Roles + Permissions. AI trả plan, không edit. Show plan output | 50s |
| 17 | [IDE] | "Thử prompt không liên quan: sửa typo" | Prompt: fix README typo. Skill không kích hoạt | 15s |
| 18 | [DIAGRAM] | "MCP giống ổ cắm USB" | Diagram: AI agent ↔ MCP protocol ↔ Database/API/Docs | 20s |
| 19 | [IDE] | "Config nằm trong .agents/mcp_config.json" | Show mcp_config.json file structure (example, không cài thật) | 15s |
| 20 | [IDE] | "Quay lại nhìn toàn bộ" | Tree view: AGENTS.md, docs/, .agents/skills/, .agents/mcp_config.json | 20s |
| 21 | [B-ROLL] | "Convention tốt… teaser refresh token" | Desk typing shot, monitor glow, cut to black | 15s |

**Tổng: 500s ≈ 8:20 quay + ~2 min buffer cho fast-forward AI = ~10:20 runtime**

### Cấu trúc project files cần tạo khi quay

```text
taskflow/
├── AGENTS.md                          # Hot Memory
├── docs/
│   ├── architecture.md                # Cold Memory — module map
│   └── database-schema.md             # Cold Memory — Prisma 8 contract
├── .agents/
│   ├── skills/
│   │   └── nest-feature/
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── architecture.md    # deep reference cho skill
│   └── mcp_config.json               # MCP config example
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

### Prompt kiểm chứng

```text
Use $nest-feature to plan Roles and Permissions inside the TaskFlow access-control domain.
Do not edit yet. Show the folders, dependency direction, business rules and verification commands.
```

### Nguồn chính thức — mở trên màn hình khi quay

| Topic | URL |
|---|---|
| AGENTS.md spec | `https://agents.md` |
| Claude Code Memory | `https://code.claude.com/docs/en/memory.md` |
| Agent Skills standard | `https://agentskills.io` |
| MCP Protocol | `https://modelcontextprotocol.io` |
| GitHub Copilot instructions | `https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot` |

### Bảng so sánh Agent Config — overlay khi quay

```text
┌─────────────────────┬───────────────────────────────────────┬──────────────┐
│ Tool                │ File / Folder                         │ AGENTS.md?   │
├─────────────────────┼───────────────────────────────────────┼──────────────┤
│ Claude Code         │ CLAUDE.md → AGENTS.md (fallback)      │ ✅ native    │
│ Gemini / Antigravity│ AGENTS.md + .agents/                  │ ✅ native    │
│ Cursor              │ .cursor/rules/*.mdc                   │ ✅ recognized│
│ GitHub Copilot      │ .github/copilot-instructions.md       │ ✅ supported │
│ Windsurf            │ .windsurf/rules/ or .devin/rules/     │ ✅ always-on │
│ Kiro                │ .kiro/steering/ + AGENTS.md            │ ✅ steering  │
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

1. AGENTS.md: Một file, mọi AI đều đọc — NestJS EP06 | Lập trình là cuộc sống
2. Dạy AI nhớ project bằng 3 tầng context — NestJS EP06 | Lập trình là cuộc sống
3. Đừng copy convention 3 lần cho 3 tool AI — NestJS EP06 | Lập trình là cuộc sống
4. AGENTS.md, Skills, MCP: Bộ ba context cho AI coding — EP06 | Lập trình là cuộc sống
5. Tại sao AI cùng project mà code kiểu khác nhau? — NestJS EP06 | Lập trình là cuộc sống
6. Hot Memory và Cold Memory: AI đọc đúng, nhớ đúng — EP06 | Lập trình là cuộc sống
7. Viết AGENTS.md cho NestJS: convention một lần, dùng mọi tool — EP06 | Lập trình là cuộc sống
8. 3 file convention, 3 tool AI, 0 nhất quán — NestJS EP06 | Lập trình là cuộc sống
9. Agent Skill + MCP: upgrade AI từ autocomplete thành teammate — EP06 | Lập trình là cuộc sống
10. Convention sống trong repo, không phải trong prompt — NestJS EP06 | Lập trình là cuộc sống

### 4b. SEO Description

```text
Mỗi AI tool đòi file convention riêng. Copy-paste qua lại giữa CLAUDE.md, .cursorrules, copilot-instructions — rồi quên cập nhật. EP06 giải quyết bằng 3 tầng context:

✅ AGENTS.md — chuẩn universal, mọi tool đều đọc (Claude Code, Cursor, Copilot, Windsurf, Kiro)
✅ docs/ — Cold Memory: schema, kiến trúc, ADR, AI chỉ đọc khi cần
✅ Agent Skill — đóng gói workflow scaffold feature thành SKILL.md
✅ MCP — Model Context Protocol, kết nối AI với database/API
✅ Progressive disclosure: AI chỉ nạp context cần thiết
✅ Demo: scaffold Roles/Permissions theo convention TaskFlow
✅ Kiểm chứng: skill không kích hoạt khi prompt không liên quan

🔗 AGENTS.md spec: https://agents.md
🔗 Claude Code Memory: https://code.claude.com/docs/en/memory.md
🔗 Agent Skills standard: https://agentskills.io
🔗 MCP Protocol: https://modelcontextprotocol.io

⏱ 0:00 3 file, cùng nội dung, copy-paste — pain
⏱ 0:55 AGENTS.md — universal standard
⏱ 2:15 Tạo AGENTS.md + docs/ (Hot vs Cold Memory)
⏱ 4:00 Agent Skill — progressive disclosure
⏱ 5:30 Viết SKILL.md cho TaskFlow
⏱ 7:00 Kiểm chứng: scaffold Roles/Permissions
⏱ 8:30 MCP — ổ cắm USB cho AI
⏱ 9:30 Toàn cảnh 3 tầng context

#AGENTS_md #AgentSkill #MCP #NestJS #AICoding #PromptEngineering #SoftwareArchitecture #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
AGENTS.md, agents md nestjs, agent skill, SKILL.md, MCP model context protocol, hot memory cold memory, ai coding convention, progressive disclosure ai, claude code agents md, cursor rules mdc, copilot instructions, windsurf rules, kiro steering, scaffold nestjs bằng ai, nestjs tập 6, ai context management, prompt engineering coding, ai coding workflow, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng

**Image prompt:**
`A cinematic photograph of a developer silhouette illuminated by dramatic neon green and cyan light from a massive monitor showing a glowing AGENTS.md file, code text floating and reflecting in the dark scene, deep shadows with city bokeh and rain outside window, high contrast, dramatic rim lighting, subject positioned on the right side leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

**Text spec:**
- Line 1: `MỘT FILE` — WHITE `#FFFFFF`
- Line 2: `MỌI AI` — NEON GREEN `#00FF41`
- Line 3: `ĐỀU ĐỌC` — NEON GREEN `#00FF41`

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
| Claude Code đọc AGENTS.md nếu không có CLAUDE.md (từ v2.1.277) | [memory.md](https://code.claude.com/docs/en/memory.md) — bảng "Your repository has / Claude reads" |
| Claude Code hỗ trợ `@path` import syntax trong CLAUDE.md/AGENTS.md | [memory.md](https://code.claude.com/docs/en/memory.md) — section "Import additional files" |
| Claude Code CLAUDE.md load order: managed → user → project → local | [memory.md](https://code.claude.com/docs/en/memory.md) — bảng "Choose where to put CLAUDE.md files" |
| Claude Code auto memory: user, feedback, project, reference types | [memory.md](https://code.claude.com/docs/en/memory.md) — section "Auto memory" |
| Claude Code skills follow Agent Skills open standard (agentskills.io) | [skills.md](https://code.claude.com/docs/en/skills.md) — paragraph 1 |
| Claude Code skill locations: enterprise, personal, project, nested, plugin | [skills.md](https://code.claude.com/docs/en/skills.md) — bảng "Where skills load" |
| Claude Code MCP = open standard at modelcontextprotocol.io | [mcp.md](https://code.claude.com/docs/en/mcp.md) — intro |
| GitHub Copilot đọc AGENTS.md (+ CLAUDE.md, GEMINI.md fallback) | [GitHub docs](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) — section "Agent instructions" |
| Copilot: repo-wide = `.github/copilot-instructions.md`, path-specific = `.github/instructions/*.instructions.md` | GitHub docs — section "Creating custom instructions" |
| Cursor: `.cursor/rules/*.mdc` với YAML frontmatter (description, globs, alwaysApply) | Cursor docs + web search confirmation |
| Cursor nhận AGENTS.md natively | Web search — confirmed by multiple sources |
| Windsurf: root AGENTS.md = always-on rule, subdirectory = directory-scoped | Web search — Windsurf documentation |
| Kiro: AGENTS.md trong steering system, `.kiro/steering/` + `.kiro/agents/` | Web search — Kiro documentation |
| AGENTS.md managed by Agentic AI Foundation (Linux Foundation) | agents.md website |
