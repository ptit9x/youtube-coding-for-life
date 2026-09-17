# NestJS #06 — Agent Skill: Giúp AI làm đúng cấu trúc dự án

- **Series:** Học NestJS bằng AI — tập 6/45
- **Target runtime:** 8–10 phút (650–800 từ thoại)
- **Outcome:** Tạo repo-scoped Agent Skill để scaffold feature đúng kiến trúc, không generic hóa business logic.
- **Pain mở EP07:** Access token ngắn hạn an toàn nhưng buộc người dùng đăng nhập lại liên tục.

---

## PART 1 — SCRIPT

Mỗi lần nhờ AI tạo feature, mình lại dán cùng một đoạn yêu cầu dài. Thiếu một dòng, structure lập tức trôi sang kiểu khác.

AI không quên vì nó lười. Convention của project chưa được biến thành context bền vững.

Copy prompt vào file text chỉ đỡ gõ. Agent vẫn không biết khi nào cần đọc và tài nguyên nào đi kèm.

Bước ngoặt là Agent Skill. Nó đóng gói instruction, reference và script thành một workflow có thể tái sử dụng.

Skill giống onboarding note cho một teammate mới. Nó nói khi nào áp dụng, phải làm gì và ranh giới nào không được vượt.

Theo tài liệu OpenAI, một skill là một thư mục có `SKILL.md`. Nó có thể kèm `scripts`, `references`, `assets` và metadata giao diện.

Codex dùng progressive disclosure. Ban đầu agent chỉ thấy tên và description; khi skill khớp, nó mới đọc toàn bộ hướng dẫn.

Vì vậy description không phải lời quảng cáo. Nó là bộ định tuyến quyết định lúc nào skill được kích hoạt.

Mình tạo `.agents/skills/nest-feature/SKILL.md` trong repo. Đây là repo-scoped skill, phù hợp convention riêng của TaskFlow.

Skill cá nhân có thể dùng ở nhiều repo. Nhưng convention chứa UsersRepository và Prisma adapter không nên áp dụng bừa cho mọi project.

Mình yêu cầu AI đọc Users và Auth, rồi đề xuất phần nào đủ ổn định để đưa vào skill.

AI muốn ghi cả rule `register phải hash password`. Rule đó chỉ thuộc Users/Auth, không thuộc mọi feature.

Mình loại nó. Skill chỉ giữ file layout, dependency direction, workflow plan-first và lệnh verify. Vì TaskFlow dùng Prisma 8, skill còn phải buộc agent đọc release status cùng tài liệu Prisma 8 trước mọi thay đổi database.

Nó được phép scaffold module, controller, service, DTO, repository contract và adapter. Nó không được tự tạo BaseCrudService. Nó cũng không được dùng `@prisma/client`, `PrismaClient`, client generation hay migration command của Prisma 7.

Một Skill tốt giảm công sức lặp lại. Nó không biến quyết định business thành template cứng.

Trong frontmatter, `name` ngắn và ổn định. `description` nói rõ trigger và cả trường hợp không nên dùng.

Phần instruction yêu cầu agent đọc feature lân cận trước. Sau đó nó phải trình plan và chờ approve.

Mình thêm reference về cấu trúc đích. Nội dung dài được tách khỏi SKILL.md để chỉ nạp khi thật sự cần.

Không cần nhồi mọi kiến thức vào một file. Progressive disclosure tốt còn giúp context không bị ngập.

Đến phần tự gõ, mình viết rule quan trọng nhất: controller mỏng, business rule nằm trong service hoặc use case.

Rule thứ hai: code phụ thuộc domain không được đưa vào common. Rule thứ ba: database code phải dùng contract, facade và migration workflow Prisma 8. Rule thứ tư: luôn chạy contract emit, migration check, lint, test và xem diff theo đúng phạm vi thay đổi.

Giờ kiểm chứng trong conversation mới. Mình yêu cầu scaffold Roles và Permissions theo convention TaskFlow.

Agent nhận đúng skill, đọc cấu trúc repo và chỉ đưa plan. Nó không sửa file trước khi mình approve.

Plan đúng folder `modules/access-control`. Repository contract không import Prisma, còn adapter nằm gần database. Plan dùng `contract.prisma`, emitted contract và database facade; không lặp lại snippet Prisma 7 phổ biến trên search result.

Mình thử một prompt không liên quan: sửa typo trong README. Skill không được kích hoạt.

Đó là lý do description cần scope rõ. Skill luôn bật cho mọi việc sẽ trở thành một bộ luật gây nhiễu.

Mình cũng cố yêu cầu “giảm tối đa code duplicate”. Agent vẫn giữ service explicit vì skill cấm generic business CRUD.

Skill không thay code review. Nó chỉ chuyển những quyết định đã review thành điểm bắt đầu nhất quán hơn.

Convention tốt giúp AI viết nhanh. Ranh giới tốt giúp con người còn hiểu thứ AI vừa viết.

Nhưng access token hiện hết hạn là phiên bị ngắt. Tập sau, ta thêm refresh token rotation và khả năng thu hồi session.

Theo dõi series nếu bạn muốn dùng AI như teammate có onboarding, không phải máy autocomplete khổng lồ. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Ba prompt scaffold giống nhau, structure khác nhau | 35s |
| 2 | [DIAGRAM] | Prompt rời rạc → Skill → workflow ổn định | 35s |
| 3 | [BROWSER] | Mở OpenAI Docs phần Build skills | 40s |
| 4 | [DIAGRAM] | Name/description được thấy trước; SKILL.md nạp sau | 45s |
| 5 | [IDE] | Tạo `.agents/skills/nest-feature/SKILL.md` | 45s |
| 6 | [IDE] | AI audit Users/Auth và đề xuất convention | 55s |
| 7 | [IDE] | Host loại rule hash password khỏi generic skill | 45s |
| 8 | [IDE] | Viết frontmatter, trigger và non-trigger | 55s |
| 9 | [IDE] | Tách architecture reference khỏi SKILL.md | 45s |
| 10 | [IDE] | Host tự gõ ba dependency rules | 50s |
| 11 | [IDE] | Conversation mới: scaffold Roles/Permissions | 65s |
| 12 | [IDE] | Verify skill chỉ plan, chưa edit | 45s |
| 13 | [IDE] | Test prompt README và prompt generic CRUD | 50s |
| 14 | [B-ROLL] | Teammate onboarding, teaser refresh token | 20s |

**Tổng: 630 giây ≈ 10:30.** Quay sidebar Skills, IDE One Dark Pro và font 18px; che thông tin tài khoản.

### Cấu trúc skill

```text
.agents/skills/nest-feature/
├── SKILL.md
└── references/
    └── architecture.md
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

### Nguồn kiểm tra khi quay

- OpenAI Docs — Build skills: `https://developers.openai.com/codex/skills`

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese developer handing a glowing digital playbook labeled only with abstract code symbols to an AI agent on a dark monitor, neon green and cyan light, dramatic shadows, subject on the right and clean left space, 16:9, photorealistic, no readable text, no logos, no watermark.`
2. `A cinematic close-up of a dark IDE where repeated chaotic folder trees become one clean consistent architecture through a glowing skill file, code reflected in glasses, purple and cyan rim light, empty left side, 16:9, photorealistic tech documentary, no text.`
3. `A cinematic late-night coding desk with an AI assistant following a luminous checklist while the developer reviews a diff, neon green approvals, deep navy shadows, city bokeh, subject right, 16:9, photorealistic, no text, no logos.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Agent Skill: Giúp AI làm đúng cấu trúc dự án NestJS — EP06 | Lập trình là cuộc sống
2. Tạo Agent Skill cho dự án NestJS — EP06 | Lập trình là cuộc sống
3. Lưu convention của dự án để AI không làm sai — EP06 | Lập trình là cuộc sống
4. Dùng AI scaffold module NestJS đúng kiến trúc — EP06 | Lập trình là cuộc sống
5. Không phải viết lại prompt khi dùng AI coding — EP06 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 5 cho nỗi đau lặp prompt.

### 4b. SEO Description

```text
Mỗi lần nhờ AI tạo feature, structure lại trôi sang một kiểu. Agent Skill biến convention đã kiểm chứng thành workflow dùng lại trong chính repository.

✅ Hiểu Agent Skill và progressive disclosure
✅ Tạo repo-scoped `.agents/skills`
✅ Viết name và description đúng scope
✅ Tách reference để tiết kiệm context
✅ Bắt AI plan trước, chờ approve rồi mới code
✅ Scaffold boilerplate nhưng giữ business service explicit
✅ Chặn snippet Prisma 7 và buộc đối chiếu release status Prisma 8
✅ Test cả trường hợp skill không nên kích hoạt

🔗 OpenAI Docs — Build skills: https://developers.openai.com/codex/skills

⏱ 0:00 Prompt lặp nhưng code vẫn lệch
⏱ 1:05 Agent Skill là gì?
⏱ 2:10 Progressive disclosure
⏱ 3:20 Repo-scoped skill
⏱ 4:30 Audit convention cùng AI
⏱ 6:00 Viết SKILL.md
⏱ 7:40 Test trong conversation mới
⏱ 9:15 Skill không thay code review

#AgentSkill #Codex #NestJS #AICoding #PromptEngineering #SoftwareArchitecture #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
agent skill codex, codex skills, SKILL.md, repo scoped skill, nestjs agent skill, ai coding convention, progressive disclosure ai, scaffold nestjs bằng ai, codex tiếng việt, học nestjs, nestjs tập 6, prompt engineering coding, ai coding workflow, software architecture, common service trap, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `DẠY AI` — WHITE
- `NHỚ PROJECT` — NEON GREEN `#00FF41`
- Hình: developer đưa playbook sáng cho AI.

### Option 2
- `ĐỪNG COPY` — WHITE
- `PROMPT NỮA` — NEON GREEN `#00FF41`
- Hình: nhiều prompt rối hợp thành một SKILL.md.

### Option 3
- `AI VIẾT NHANH` — WHITE
- `CODE VẪN RÕ` — NEON GREEN `#00FF41`
- Hình: cây thư mục sạch cạnh agent panel.

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, text trái một phần ba khung, stroke 8px, glow 10px. Typeset trong Canva; lưu nền không chữ.
