# Content audit — 23/10/2026, cập nhật 27/10/2026

## Phạm vi

- EP01–EP04 đã quay/đăng: khóa lời thoại và workflow. Chỉ thêm correction note nếu một RC thay đổi API.
- EP05–EP07: đã audit để quay tiếp.
- EP08–EP19: đã audit metadata và baseline; một số `script.md` chưa merge đủ outcome theo `00-plan.md`, nên chưa được xem là recording-ready.

## Snapshot phải kiểm tra lại trước mỗi ngày quay

| Thành phần | Trạng thái ngày 23/10/2026 | Quyết định cho series |
|---|---|---|
| NestJS | `@nestjs/core` 12.2.0; CLI/schematics 12.0.10 hiện scaffold ESM, Jest 30 và TypeScript 6 | Giữ NestJS 12 và Vitest đã chọn từ EP01. Không tự đổi test runner hoặc nâng TypeScript chỉ để đuổi theo template mới. |
| Prisma ORM 8 | Vẫn là release candidate; `prisma` và `@prisma/orm-postgres` có thể khác số RC | Pin exact version riêng cho CLI/runtime. Không dùng `@latest` trong cảnh quay. Chạy `contract emit`, migration và test trước khi record. |
| AGENTS.md | Định dạng mở do Agentic AI Foundation thuộc Linux Foundation quản lý; hơn 60k repo OSS dùng | Nói “nhiều agent hỗ trợ”, không nói “mọi AI đều đọc”. Kiểm tra load order trên đúng client. |
| Agent Skills | Metadata `name` + `description` được dùng để route; instruction đầy đủ chỉ nạp khi skill được chọn | Giữ description ngắn, scope rõ; kiểm chứng trigger và non-trigger bằng hai prompt. |
| MCP | Chuẩn mở nối ứng dụng AI với data/tools/workflows | Antigravity hỗ trợ `.agents/mcp_config.json` ở workspace. Nói rõ đây là config của Antigravity, review quyền và chỉ bật tool cần dùng. |

## Sửa trực tiếp trong audit này

1. EP05: sửa code login để dummy bcrypt compare thật sự chạy khi email không tồn tại; dummy hash phải được precompute cùng cost.
2. EP05–EP19: đổi số tập theo cấu trúc 29 tập; không đổi metadata EP01–EP04 đã quay.
3. EP06: bỏ claim “mọi tool đều đọc”, bỏ `.cursorrules` cũ và bỏ `@import` không phù hợp khỏi bản cũ.
4. EP05–EP07: chuẩn hóa collection thành `code/taskflow.postman_collection.json`; EP07 thêm refresh/logout.
5. `00-plan.md`: ghi rõ Prisma 8 còn RC, CLI/runtime cần pin riêng; word-count estimate được đưa về 90–110 từ/phút.
6. Cập nhật 27/10: chuyển toàn bộ demo EP06 sang Antigravity; thêm mẫu MCP workspace bị disable mặc định, giới hạn `enabledTools`; sửa CLI scaffold hiện tại thành Jest 30.

## Recording gate

### Có thể quay tiếp

- EP05: ready sau khi code demo dùng dummy hash thật và collection mới.
- EP06: ready khi Antigravity Customizations hiển thị AGENTS.md và `nest-feature`; quay đủ plan → review → approve → implement → diff/test cho bộ file context.
- EP07: ready nếu refresh rotation được kiểm chứng bằng concurrent test và policy reuse/grace được nói rõ.

### Chưa quay từ `script.md` hiện tại

- EP08 thiếu nửa relation many-to-many đang nằm trong `merged-from-09/`.
- EP09 thiếu Tasks + ownership đang nằm trong `merged-from-11/`.
- EP11 thiếu phần common library/versioning.
- EP12 thiếu Docker deploy.
- EP13 thiếu REST vs GraphQL.
- EP15 thiếu tracing/observability.
- EP17 thiếu Project + Label.
- EP19 thiếu BullMQ/background jobs.

Các tập trên phải merge, cắt còn 900–1100 từ thoại và chạy lại technical gate trước khi quay.

## Nguồn chuẩn

- Prisma ORM 8 overview/status: https://www.prisma.io/docs/orm
- Prisma ORM 8 contract syntax: https://www.prisma.io/docs/orm/contract-authoring/psl-syntax
- Prisma ORM 8 transactions: https://www.prisma.io/docs/orm/fundamentals/transactions
- AGENTS.md: https://agents.md
- Antigravity Rules: https://www.antigravity.google/docs/rules/
- Antigravity Skills: https://www.antigravity.google/docs/skills?tab=ide
- Antigravity MCP: https://www.antigravity.google/docs/mcp/
- OpenAI Skills: https://developers.openai.com/plugins/concepts/skills
- OpenAI Codex AGENTS.md behavior: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
- MCP introduction: https://modelcontextprotocol.io/docs/getting-started/intro

