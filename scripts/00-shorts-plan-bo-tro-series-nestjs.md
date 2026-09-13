# Kế hoạch YouTube Shorts bổ trợ series “Học NestJS bằng AI”

## 1. Vai trò của Shorts trong toàn bộ series

Shorts không tóm tắt lại video dài. Mỗi Short phải làm đúng một việc:

1. **Kéo người mới bằng JavaScript/TypeScript:** bắt đầu từ lỗi quen thuộc để mở rộng tệp ngoài người đã biết NestJS.
2. **Bắc cầu sang NestJS:** cho thấy một vấn đề JavaScript/backend được NestJS tổ chức lại thế nào.
3. **Chuyển sang tập dài:** kết thúc tại đúng điểm người xem cần video đầy đủ để hiểu hoặc làm tiếp.

Tỉ lệ nội dung đề xuất:

- Trước khi series ra mắt: **40% JavaScript/TypeScript, 40% NestJS, 20% AI workflow**.
- Sau khi series ra mắt: **20% JavaScript/TypeScript, 60% NestJS, 20% AI workflow**.

Thông điệp xuyên suốt: **AI viết, mình hiểu; AI đề xuất, mình kiểm chứng.**

## 2. Format chung

- Khung hình: `9:16`, code ở giữa safe zone, font IDE tối thiểu `22–26px`.
- Thời lượng chủ lực: **30–55 giây**. Chỉ dùng `60–90 giây` khi cần chứng minh bằng request hoặc test.
- Không intro, không logo animation, không chào hỏi.
- Mỗi Short chỉ có **một lỗi, một insight, một bằng chứng**.
- Caption lớn, mỗi dòng tối đa 5–7 từ; highlight bằng NestJS red `#E0234E`.
- Dùng âm thanh bàn phím, terminal và response thật; nhạc chỉ làm nền.

YouTube hiện nhận video dọc hoặc vuông dài tối đa ba phút là Shorts, nhưng series này vẫn ưu tiên dưới một phút để giữ mật độ cao. Sau khi đăng, luôn gắn **Related video** đến tập dài tương ứng; không trông chờ URL trong mô tả hoặc bình luận Shorts vì chúng không phải link bấm được.

## 3. Công thức kịch bản 45 giây

| Thời gian | Nội dung | Hình ảnh |
|---|---|---|
| 0–2s | Bằng chứng gây sốc hoặc lỗi thật | Response sai, test xanh giả, dữ liệu biến mất |
| 2–8s | Nêu pain bằng một câu | Zoom đúng dòng code gây lỗi |
| 8–32s | Demo hoặc giải thích một concept | Gõ/chạy code, không dùng slide dài |
| 32–42s | Kết quả trước và sau | Split-screen hoặc test đỏ → xanh |
| 42–48s | Một câu kết + cầu sang tập dài | “Luồng đầy đủ nằm ở EP…” |

Ba mẫu CTA nên luân phiên:

- “Mình xử lý trọn luồng này trong EP02 của TaskFlow.”
- “Bản đầy đủ có cả đoạn AI đề xuất sai và cách mình bắt lỗi.”
- “Tập tiếp theo bắt đầu từ chính response lỗi này.”

## 4. Bốn format có thể sản xuất lặp lại

### A. “Bug trong 30 giây”

Mở bằng lỗi thật, sửa đúng một dòng hoặc một quyết định. Phù hợp với route order, validation, status code, JWT và Prisma constraint.

### B. “JavaScript đứng sau NestJS”

Giải thích cơ chế gốc như class runtime, decorator, async/await, DI và event loop; sau đó chỉ ra NestJS sử dụng nó ở đâu.

### C. “AI viết được, nhưng…”

Cho AI đưa ra giải pháp có vẻ hợp lý, host chỉ ra một lỗi kiến trúc hoặc bảo mật, rồi kiểm chứng bằng diff/test. Đây là format nhận diện riêng của series.

### D. “Một request đi đâu?”

Visual hóa request chạy qua module, controller, service, guard, pipe, interceptor hoặc repository. Dùng code thật của TaskFlow để nối các tập với nhau.

## 5. Nhịp đăng đề xuất

Một video dài mỗi tuần đi cùng ba Shorts:

- **T−2 ngày — Pain Short:** đưa ra lỗi mà tập dài sẽ giải quyết.
- **T+1 ngày — Concept Short:** giải thích một mảnh kiến thức có thể đứng độc lập.
- **T+3 ngày — AI Review Short:** cho thấy AI sai hoặc bị host chất vấn ở đâu.

Nếu chỉ đủ sức làm hai Shorts mỗi tuần, giữ **Pain Short** và **AI Review Short**. Không cắt ba đoạn ngẫu nhiên từ video dài; quay dọc riêng để chữ và code đọc được trên điện thoại.

## 6. Lịch 10 tuần đầu — 30 Shorts

### Tuần −2 — Mở tệp bằng JavaScript/TypeScript

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 01 | **TypeScript không bảo vệ API của bạn** | Gửi `email: 123`, app vẫn nhận ở runtime | Teaser EP02 |
| 02 | **Decorator `@Get()` thật sự làm gì?** | Route metadata → handler được gọi | Teaser EP01 |
| 03 | **AI viết đúng code, sai kiến trúc** | Service gọi thẳng Prisma; highlight dependency sai | Lời hứa của series |

### Tuần −1 — Làm quen với TaskFlow

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 04 | **Một request đi qua NestJS thế nào?** | `main.ts → module → controller → service` | EP01 |
| 05 | **Route `/count` bỗng thành một user ID** | Đặt `/:id` trước `/count`, response sai | EP01 |
| 06 | **Dependency Injection khác `new Service()` ở đâu?** | Đổi fake repository mà controller không đổi | EP01/EP03 |

### Tuần 1 — EP01: Users API đầu tiên

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 07 | **Module, Controller, Service: đừng học thuộc** | Trace một request duy nhất qua ba file | EP01 |
| 08 | **Lệnh Nest CLI tiết kiệm gì cho bạn?** | `nest g resource modules/users` rồi audit file sinh ra | EP01 |
| 09 | **Users API chạy rồi, nhưng nhận mọi rác** | `POST /users` với ba payload sai vẫn trả 201 | EP02 |

### Tuần 2 — EP02: ValidationPipe

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 10 | **`interface` biến mất khi code chạy** | So sánh interface và DTO class trong JavaScript build | EP02 |
| 11 | **`whitelist` và `forbidNonWhitelisted` khác gì?** | Cùng một payload thừa field, hai response khác nhau | EP02 |
| 12 | **`@IsNotEmpty()` vẫn cho dấu cách đi qua** | Tên chỉ gồm space lọt validation; trim rồi test lại | EP02/EP03 |

### Tuần 3 — EP03: PostgreSQL và Prisma 8

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 13 | **Restart server, user biến mất** | In-memory trước/sau restart | EP03 |
| 14 | **Vì sao UsersService không nên gọi Prisma 8 trực tiếp?** | Đổi adapter in-memory ↔ Prisma 8 qua repository contract | EP03 |
| 15 | **Một email trùng làm API crash 500** | Prisma 8 structured constraint error chưa được map | EP04 |

### Tuần 4 — EP04: Error Handling

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 16 | **400, 404 hay 409?** | Ba request, ba status, một câu phân biệt mỗi loại | EP04 |
| 17 | **Đừng gửi stack trace cho client** | Before/after response qua ExceptionFilter | EP04 |
| 18 | **AI tìm lỗi tốt hơn khi bạn hỏi đúng** | Prompt “liệt kê mọi failure path” rồi host verify từng điểm | EP04/EP05 |

### Tuần 5 — EP05: JWT Authentication

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 19 | **Hash password không phải mã hóa password** | Hash cùng password với salt khác nhau | EP05 |
| 20 | **JWT đọc được, sao vẫn an toàn?** | Decode payload; chỉ ra chữ ký, không gọi JWT là encryption | EP05 |
| 21 | **401 và 403 không giống nhau** | Không token → 401; có token thiếu quyền → 403 | EP05/EP10 |

### Tuần 6 — EP06: Agent Skill và AI workflow

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 22 | **Đừng để AI sửa code ngay** | Workflow: yêu cầu → plan → review → approve → code → verify | EP06 |
| 23 | **Một file giúp AI nhớ convention của repo** | Conversation mới scaffold đúng cấu trúc nhờ Skill | EP06 |
| 24 | **Template không được chứa business rule** | Loại rule User khỏi scaffold Role/Permission | EP06/EP08 |

### Tuần 7 — EP07: Refresh Token

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 25 | **Access token và refresh token khác việc** | Timeline token ngắn hạn và phiên dài hạn | EP07 |
| 26 | **Đừng lưu refresh token nguyên văn** | Database leak giả lập: raw token vs hash | EP07 |
| 27 | **Token cũ bị dùng lại thì sao?** | Rotation + reuse detection thu hồi session | EP07 |

### Tuần 8 — EP08: Role và Permission

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 28 | **Role là nhóm, Permission mới là quyền** | `admin` chứa các code `users.read`, `roles.assign` | EP08 |
| 29 | **Đặt tên permission để khỏi sửa controller** | So sánh `@Roles('admin')` và `@RequirePermissions()` | EP08/EP10 |
| 30 | **Ba service giống nhau chưa chắc nên gom** | AI tạo `CommonService<T>`; business rule phá abstraction | EP08/EP13 |

## 7. Content bank mở rộng — 25 Shorts

Nhóm này được chèn vào giữa các tập chính, dùng trong tuần nghỉ hoặc phát triển thành mini-series riêng. Không đăng năm video cùng một nhóm liên tục; nên luân phiên một chủ đề rộng với một chủ đề NestJS sát series.

### A. REST APIs — nền móng trước khi học framework

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 31 | **REST không phải là “API trả JSON”** | Cùng JSON nhưng một thiết kế dùng resource/status đúng, một thiết kế chỉ RPC qua HTTP | EP01/EP18 |
| 32 | **Đừng đặt route là `/getAllUsers`** | So sánh `GET /getAllUsers` với `GET /users` | EP01 |
| 33 | **PUT và PATCH khác nhau ở đâu?** | Replace toàn bộ user với update riêng trường `name` | EP01/EP33 |
| 34 | **Stateless không có nghĩa là không dùng database** | Mỗi request tự mang auth context; dữ liệu vẫn nằm trong PostgreSQL | EP03/EP05 |
| 35 | **Bấm hai lần, API có tạo hai đơn hàng?** | Gửi cùng request hai lần; giới thiệu idempotency key | EP25/EP42 |

Góc triển khai: dùng TaskFlow làm ví dụ xuyên suốt. Tránh biến nhóm này thành danh sách “REST constraint” học thuộc lòng; luôn bắt đầu bằng một API thiết kế sai nhưng vẫn chạy.

### B. Git — lớp an toàn cho AI-driven development

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 36 | **Commit không phải nút Save** | Một commit chỉ chứa một thay đổi có chủ đích; so với commit lẫn refactor và feature | EP06 |
| 37 | **AI sửa 20 file: nhìn đâu trước?** | `git diff --stat` → diff theo file → test | EP06 |
| 38 | **Merge, squash hay rebase?** | Vẽ ba history graph và kết quả sau khi nhập PR | EP06/EP35 |
| 39 | **Reset và revert: chỉ một cái viết lại lịch sử** | Revert tạo commit đảo ngược; reset di chuyển branch pointer | EP35 |
| 40 | **Xóa nhầm commit vẫn còn đường về** | `git reflog` tìm lại HEAD cũ trên repo demo | EP35 |

Góc triển khai: Git không đứng ngoài series. Nó là bằng chứng cho workflow **Review → Approve → Thực hiện → Kiểm chứng**, đặc biệt khi AI thay đổi nhiều file.

### C. Angular đi lên backend và lịch sử NestJS

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 41 | **NestJS có phải Angular cho backend?** | Đặt Angular component/service/module cạnh Nest controller/provider/module | EP01 |
| 42 | **Vì sao NestJS nhìn rất giống Angular?** | Decorator, module và DI ở hai codebase; kết luận “lấy cảm hứng kiến trúc”, không phải bê Angular lên server | EP01 |
| 43 | **Trước NestJS, Node.js thiếu điều gì?** | Express route vẫn chạy tốt nhưng không áp đặt cấu trúc project | EP01/EP38 |
| 44 | **NestJS ra đời từ một nỗi đau kiến trúc** | Timeline 2017, Kamil Myśliwiec, mục tiêu app dễ test và maintain | Video lịch sử độc lập/EP01 |
| 45 | **NestJS không thay thế Express** | Chuyển adapter Express/Fastify; Nest giữ lớp kiến trúc phía trên | EP01/EP34 |

Guardrail nội dung: chỉ nói NestJS **được truyền cảm hứng mạnh từ Angular**. Không nói NestJS là Angular chạy trên backend hoặc dùng Angular bên trong. Trang chính thức ghi framework được phát hành từ năm 2017 và do Kamil Myśliwiec tạo ra.

### D. REST APIs và GraphQL

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 46 | **Một màn hình cần ba REST request hay một GraphQL query?** | Dashboard lấy user, tasks và permissions theo hai cách | Bonus 18.5 |
| 47 | **GraphQL chọn field, REST luôn trả thừa?** | Chỉ yêu cầu `id`, `title`; so với response contract cố định của API demo | Bonus 18.5 |
| 48 | **GraphQL không tự nhiên nhanh hơn REST** | Một query đẹp nhưng resolver tạo N+1 query database | Bonus 18.5/Bonus 34.5 |
| 49 | **Một endpoint GraphQL có thay thế mọi REST route?** | `/graphql` nhận nhiều operation nhưng schema/resolver vẫn có boundary | Bonus 18.5 |
| 50 | **Cùng một Service, hai lớp API** | REST controller và GraphQL resolver gọi cùng `TasksService` | Bonus 18.5 |

Kết luận xuyên suốt: không chọn công nghệ bằng khẩu hiệu “GraphQL hiện đại hơn”. REST phù hợp với API đơn giản, HTTP semantics và caching rõ ràng; GraphQL hữu ích khi client cần ghép dữ liệu linh hoạt. Quyết định dựa trên shape của sản phẩm và chi phí vận hành.

### E. Prisma và TypeORM

| # | Hook/tiêu đề Short | Bằng chứng trên màn hình | Dẫn đến |
|---|---|---|---|
| 51 | **Cùng model User: Prisma 8 viết gì, TypeORM viết gì?** | `contract.prisma` + emitted types cạnh class `@Entity()` | EP03/Bonus 13.5 |
| 52 | **Vì sao Prisma 8 đáng chú ý?** | Contract dễ đọc/diff → typed query → migration graph → AI review | EP03 |
| 53 | **TypeORM có hai tính cách** | Cùng truy vấn bằng Active Record và Data Mapper | Bonus 13.5 |
| 54 | **Prisma 8 type-safe là hết lỗi database?** | Sai field bị compiler bắt; constraint và race condition vẫn lỗi runtime | EP03/EP04 |
| 55 | **Prisma 8 hay TypeORM cho NestJS mới?** | Decision matrix: contract/query API, query control, legacy schema, team experience | Bonus 13.5 |

Không khẳng định Prisma “phổ biến hơn TypeORM” nếu chưa chốt thước đo và thời gian đo. Cách đóng gói chính xác hơn là: **“Vì sao Prisma 8 đáng chú ý?”** Những lý do có thể kiểm chứng gồm contract có thể inspect/diff, typed query API, migration graph và thiết kế thân thiện với coding agent. TypeORM vẫn có lợi thế khi team thích entity/decorator, Data Mapper hoặc Active Record, và cần phong cách ORM truyền thống.

### Lịch chen 25 Shorts mở rộng

- REST và Angular/NestJS: ưu tiên trước hoặc trong EP01–EP04.
- Git: rải quanh EP06, testing và EP35 CI/CD.
- Prisma vs TypeORM: đăng quanh EP03, EP13 và Bonus 13.5.
- REST vs GraphQL: giữ ba Short đầu để “gieo vấn đề” từ EP18; đăng trọn nhóm quanh Bonus 18.5.
- Idempotency và N+1: dùng làm callback sớm, rồi dẫn lại khi EP34/EP42 ra mắt.

## 8. Source map để AI viết Short

Khi giao cho AI viết kịch bản, luôn gửi **ID Short + link nguồn đúng hàng**. Yêu cầu AI tách ba phần: fact lấy từ nguồn, demo của TaskFlow và nhận định của host. Không cho AI biến nhận định thành số liệu.

Quy tắc phiên bản:

1. Với Prisma, chỉ dùng tài liệu có nhãn Prisma 8 hoặc trang current trỏ đến Prisma 8. Không dùng snippet `PrismaClient`, `@prisma/client`, `schema.prisma`, `P2002`, `$transaction` hay `migrate dev` của Prisma 6/7.
2. Prisma 8 đang là release candidate tại thời điểm lập kế hoạch. Trước khi sinh script, đọc lại trang release status, ghi ngày kiểm tra và phiên bản sẽ xuất hiện trên màn hình.
3. Với REST/HTTP/OAuth/JWT, ưu tiên RFC hoặc tài liệu gốc. Với NestJS, Angular, Prisma và TypeORM, ưu tiên docs chính thức.
4. Link thứ hai dùng để bổ sung hoặc phản biện, không được trộn API giữa hai phiên bản.

### Nguồn cho Shorts 01–30

| Short ID | Nguồn chính | Claim được phép dùng |
|---|---|---|
| 01, 09, 10 | [TypeScript: Erased Types](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch#erased-types), [NestJS Validation](https://docs.nestjs.com/techniques/validation) | Type bị xóa sau compile; API cần validation runtime |
| 02 | [NestJS Controllers](https://docs.nestjs.com/controllers), [Custom decorators](https://docs.nestjs.com/custom-decorators) | Decorator gắn metadata/khai báo route trong Nest |
| 03, 14 | [Prisma 8 với NestJS](https://www.prisma.io/docs/guides/frameworks/nestjs), [NestJS Custom Providers](https://docs.nestjs.com/fundamentals/custom-providers) | Prisma 8 tích hợp Nest qua provider; business service có thể đứng sau repository contract |
| 04, 07 | [NestJS First steps](https://docs.nestjs.com/first-steps), [Modules](https://docs.nestjs.com/modules), [Providers](https://docs.nestjs.com/providers) | Luồng controller/provider/module và DI cơ bản |
| 05 | [NestJS Controllers](https://docs.nestjs.com/controllers), [script EP01](./01-hoc-nestjs-voi-ai/01-nestjs-tu-0-cung-ai.md) | Route tĩnh/động phải được kiểm chứng trên đúng code TaskFlow |
| 06 | [NestJS Providers](https://docs.nestjs.com/providers), [Custom Providers](https://docs.nestjs.com/fundamentals/custom-providers) | DI cho phép thay implementation qua token/provider |
| 08 | [Nest CLI usage](https://docs.nestjs.com/cli/usages) | Generator tạo boilerplate; output vẫn phải được review |
| 11 | [NestJS Validation](https://docs.nestjs.com/techniques/validation) | Ý nghĩa `whitelist`, `forbidNonWhitelisted`, `transform` |
| 12 | [class-validator decorators](https://github.com/typestack/class-validator#validation-decorators), [issue về whitespace](https://github.com/typestack/class-validator/issues/794) | `IsNotEmpty` loại `''`, `null`, `undefined` nhưng không tự trim chuỗi chỉ có space |
| 13 | [Prisma 8/NestJS guide](https://www.prisma.io/docs/guides/frameworks/nestjs) | Persistence giữ dữ liệu sau khi process restart |
| 15, 16, 17 | [Prisma 8 Error Reference](https://www.prisma.io/docs/orm/reference/error-reference), [NestJS Exception Filters](https://docs.nestjs.com/exception-filters), [RFC 9110 status codes](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) | Map structured database error sang HTTP response; không dùng `P2002` của Prisma 7 |
| 18 | [NestJS Exception Filters](https://docs.nestjs.com/exception-filters), [OWASP Error Handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) | Liệt kê failure path và không lộ chi tiết nội bộ |
| 19 | [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) | Password phải hash, không encrypt/plaintext; Argon2id được ưu tiên cho hệ thống mới |
| 20 | [RFC 7519: JWT](https://www.rfc-editor.org/rfc/rfc7519.html), [OWASP JWT for Java](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) | JWT payload có thể decode; chữ ký không phải encryption |
| 21 | [RFC 9110: 401](https://www.rfc-editor.org/rfc/rfc9110.html#name-401-unauthorized), [RFC 9110: 403](https://www.rfc-editor.org/rfc/rfc9110.html#name-403-forbidden), [NestJS Guards](https://docs.nestjs.com/guards) | 401 liên quan credentials; 403 là server hiểu nhưng từ chối thực hiện |
| 22, 37 | [Git diff](https://git-scm.com/docs/git-diff), [series AI workflow](./00-series-plan-hoc-nestjs-voi-ai.md) | Review diff trước khi chấp nhận thay đổi của AI |
| 23, 24 | [Agent Skills specification](https://agentskills.io/specification), [script EP06](./06-agent-skill-nestjs/06-agent-skill-nestjs.md) | Cấu trúc `SKILL.md`, progressive disclosure và convention của repo |
| 25, 26, 27 | [RFC 9700: Refresh Token Protection](https://www.rfc-editor.org/rfc/rfc9700.html#name-refresh-token-protection) | Rotation, replay detection, binding và thu hồi refresh token |
| 28, 29 | [NestJS Authorization](https://docs.nestjs.com/security/authorization) | Role là một cách gom policy; permission/claim phù hợp kiểm soát chi tiết hơn |
| 30 | [script EP13](./13-dry-abstraction-nestjs/13-generic-crud-abstraction-trap.md), [TypeORM Active Record vs Data Mapper](https://typeorm.io/docs/guides/active-record-data-mapper/) | Trùng method không đồng nghĩa trùng business knowledge |

### Nguồn cho Shorts 31–55

| Short ID | Nguồn chính | Claim được phép dùng |
|---|---|---|
| 31 | [Roy Fielding — REST chapter](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm), [REST overview](https://restfulapi.net/) | REST là architectural style xoay quanh resource/representation, không đồng nghĩa JSON qua HTTP |
| 32 | [Microsoft REST API design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design), [Google AIP-122](https://google.aip.dev/122) | URI thường đặt theo resource/noun; HTTP method đã mang ý nghĩa hành động |
| 33 | [MDN HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods), [RFC 9110 PUT](https://www.rfc-editor.org/rfc/rfc9110.html#name-put) | PUT thay thế representation; PATCH sửa một phần; semantics và idempotency khác nhau |
| 34 | [Fielding — Stateless](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm#sec_5_1_3) | Mỗi request chứa đủ context; stateless không có nghĩa server không lưu business data |
| 35 | [RFC 9110 — Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods), [Stripe Idempotent Requests](https://docs.stripe.com/api/idempotent_requests) | Retry cùng operation không được tạo side effect lần hai; idempotency key là một implementation pattern |
| 36 | [Git commit](https://git-scm.com/docs/git-commit) | Commit ghi một snapshot/thay đổi có chủ đích, không phải thao tác lưu file |
| 38 | [GitHub Pull Request Merges](https://docs.github.com/en/pull-requests/reference/pull-request-merges) | Merge commit, squash và rebase tạo lịch sử khác nhau |
| 39 | [Git reset](https://git-scm.com/docs/git-reset), [Git revert](https://git-scm.com/docs/git-revert) | Reset di chuyển ref/có thể đổi index/worktree; revert tạo commit đảo thay đổi |
| 40 | [Git reflog](https://git-scm.com/docs/git-reflog) | Reflog ghi các lần ref/HEAD thay đổi và có thể giúp tìm lại commit cũ |
| 41, 42 | [NestJS Philosophy](https://docs.nestjs.com/), [Angular Dependency Injection](https://angular.dev/guide/di) | NestJS được truyền cảm hứng mạnh từ Angular về kiến trúc, decorator và DI; không chạy Angular trên server |
| 43 | [NestJS Philosophy](https://docs.nestjs.com/), [Express starter](https://expressjs.com/en/starter/basic-routing.html) | Nest giải quyết bài toán structure/architecture phía trên nền Node HTTP adapter |
| 44 | [NestJS homepage](https://nestjs.com/), [NestJS v4 docs](https://docs.nestjs.com/v4/) | NestJS do Kamil Myśliwiec tạo; mốc bản quyền/phát hành bắt đầu năm 2017 |
| 45 | [NestJS HTTP adapter](https://docs.nestjs.com/faq/http-adapter), [NestJS Performance/Fastify](https://docs.nestjs.com/techniques/performance) | Nest có thể chạy trên Express hoặc Fastify adapter; Nest không phải bản thay thế trực tiếp cho transport library |
| 46, 47 | [GraphQL Queries](https://graphql.org/learn/queries/), [NestJS GraphQL quick start](https://docs.nestjs.com/graphql/quick-start) | Client chọn field và có thể lấy dữ liệu liên quan trong một request |
| 48 | [GraphQL Performance](https://graphql.org/learn/performance/), [NestJS GraphQL resolvers](https://docs.nestjs.com/graphql/resolvers) | GraphQL không mặc nhiên nhanh hơn; resolver thiếu batching có thể tạo N+1 |
| 49 | [GraphQL over HTTP](https://graphql.org/learn/serving-over-http/), [NestJS GraphQL quick start](https://docs.nestjs.com/graphql/quick-start) | Một HTTP endpoint có thể nhận nhiều operation; schema và resolver vẫn là contract/boundary |
| 50 | [NestJS Controllers](https://docs.nestjs.com/controllers), [NestJS GraphQL Resolvers](https://docs.nestjs.com/graphql/resolvers), [series Bonus 18.5](./00-series-plan-hoc-nestjs-voi-ai.md) | Controller và resolver là transport boundary; reuse service là quyết định kiến trúc của TaskFlow |
| 51 | [Prisma 8 data contract](https://www.prisma.io/docs/orm/core-concepts), [TypeORM Entities](https://typeorm.io/docs/entity/entities/) | Prisma 8 author contract + emit types; TypeORM author class có decorator |
| 52 | [Prisma 8 overview](https://www.prisma.io/docs/orm), [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status) | Contract, typed query API, migration graph và trạng thái phát hành hiện tại |
| 53 | [TypeORM Active Record vs Data Mapper](https://typeorm.io/docs/guides/active-record-data-mapper/) | TypeORM hỗ trợ cả hai pattern; mỗi pattern có trade-off maintainability/simplicity |
| 54 | [Prisma 8 Error Reference](https://www.prisma.io/docs/orm/reference/error-reference), [Prisma 8 transactions](https://www.prisma.io/docs/orm/fundamentals/transactions) | Type-safe query không loại bỏ constraint, concurrency hay runtime error |
| 55 | [Prisma 8 từ góc nhìn Prisma 7](https://www.prisma.io/docs/orm/coming-from-prisma-orm-7), [TypeORM docs](https://typeorm.io/docs/) | So sánh programming model và workflow; không kết luận “tool A thắng mọi dự án” |

Prompt nguồn tối thiểu cho AI:

```text
Viết Short ID <ID> dựa trên đúng các nguồn bên dưới.
Không dùng kiến thức nhớ sẵn nếu khác nguồn.
Mở từng link và ghi phiên bản/ngày kiểm tra cho nội dung thay đổi nhanh.
Tách rõ: fact từ tài liệu, demo TaskFlow, nhận định của host.
Không khẳng định benchmark, mức độ phổ biến hoặc bảo mật tuyệt đối nếu nguồn không cung cấp số liệu.
Với Prisma chỉ dùng Prisma 8 API; loại mọi snippet Prisma 6/7.
```

## 9. Quy trình batch-production mỗi tuần

1. Khi viết tập dài, đánh dấu ba khoảnh khắc: **failure**, **aha**, **AI sai**.
2. Viết ba hook riêng; không bê nguyên lời thoại của video dài.
3. Quay một session dọc khoảng 30 phút, font lớn, chỉ mở file cần thiết.
4. Mỗi Short dùng tối đa ba góc: terminal, IDE, response/browser.
5. Dựng theo cùng preset caption và màu NestJS để nhận diện series.
6. Đăng Pain Short trước; sau khi video dài public, gắn nó làm Related video cho cả ba Shorts.
7. Sau 48–72 giờ, ghi kết quả vào bảng theo dõi và chọn hook thắng để tái sử dụng.

## 10. Cách đo sau mỗi 10 Shorts

Không tối ưu theo view thô duy nhất. Theo dõi:

- **Chose to view / viewed vs swiped away:** hook hai giây đầu có giữ người không.
- **Average view duration và audience retention:** đoạn giải thích có quá dài không.
- **Subscriber change:** format nào tạo đúng tệp người xem muốn học tiếp.
- **Traffic sang Related video:** Short có hoàn thành vai trò kéo sang tập dài không.
- **Comment chất lượng:** người xem hỏi tiếp về concept hay chỉ tranh luận ngoài chủ đề.

Quy tắc quyết định:

- Hook tốt, retention thấp: giữ chủ đề, rút phần giải thích.
- Hook yếu, retention tốt: quay lại cùng nội dung với frame đầu mạnh hơn.
- View cao nhưng không có người sang tập dài: giảm nội dung JavaScript quá rộng, tăng cầu nối sang NestJS.
- Một format thắng ba lần: biến nó thành mini-series có tên cố định.

Lưu ý từ ngày 24/08/2026, YouTube thay đổi cách đếm view: video bắt đầu phát đã có thể được tính view, trong khi kiếm tiền và điều kiện YPP vẫn dựa trên các biến thể engaged/qualified. Vì vậy khi so sánh hiệu quả, ưu tiên **engaged views, chose to view, retention và chuyển đổi sang video dài**.

## 11. Tên mini-series và hashtag

Tên nên dùng cố định trên caption hoặc playlist, không cần nhét hết vào title:

- **NestJS 45 Giây**
- **JavaScript Đứng Sau NestJS**
- **AI Viết Được, Nhưng…**
- **Bug TaskFlow**
- **REST Không Khó**
- **Git Cứu Một Bàn Thua**
- **Hai Phút Lịch Sử Backend**
- **Chọn Tool, Đừng Chọn Phe**

Hashtag lõi: `#nestjs #javascript #typescript #nodejs #backend #laptrinh #coding #taskflow`

## 12. Nguồn tham chiếu vận hành

- YouTube Help — Shorts tối đa ba phút: https://support.google.com/youtube/answer/15424877
- YouTube Help — gắn Related video: https://support.google.com/youtube/answer/14075157
- YouTube Help — Shorts Analytics: https://support.google.com/youtube/answer/12942217
- YouTube Help — link trong mô tả/bình luận Shorts: https://support.google.com/youtube/answer/13748639
- NestJS Docs — Request lifecycle: https://docs.nestjs.com/faq/request-lifecycle
- NestJS Docs — Validation: https://docs.nestjs.com/techniques/validation
- NestJS Docs — Guards: https://docs.nestjs.com/guards
- NestJS Docs — kiến trúc được truyền cảm hứng từ Angular: https://docs.nestjs.com/
- NestJS — lịch sử phát hành và tác giả: https://nestjs.com/
- NestJS Docs — GraphQL với TypeScript: https://docs.nestjs.com/graphql/quick-start
- GraphQL Foundation — query đúng field cần dùng và dữ liệu liên quan trong một request: https://graphql.org/learn/queries/
- REST API Tutorial — REST là architectural style, không phải protocol: https://restfulapi.net/
- Prisma 8 Docs — contract, typed query và migration graph: https://www.prisma.io/docs/orm
- Prisma 8 release status — runtime tối thiểu và feature chưa có: https://www.prisma.io/docs/prisma-orm/release-status
- TypeORM Docs — Active Record và Data Mapper: https://typeorm.io/docs/guides/active-record-data-mapper/
- Git Docs — reflog: https://git-scm.com/docs/git-reflog
- GitHub Docs — merge, squash và rebase: https://docs.github.com/en/pull-requests/reference/pull-request-merges
