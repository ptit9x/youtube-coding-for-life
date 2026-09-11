# NestJS #01 — Từ số 0 đến CRUD đầu tiên cùng Opus (LLM mentor series)

- **Series:** Học NestJS bằng AI (lane 6) — tập 1/30
- **Định dạng:** Host tự quay màn hình + tự thoại âm. Không AI voice, không AI footage.
- **AI tool:** **Opus trong IDE Antigravity** (agent panel đọc + sửa codebase thật)
- **Target runtime:** ~11:10
- **Audience:** Dev mới vào nghề / Fresher — lần đầu chạm backend framework

## Phân tích đối thủ (research 09/2026)

| Đối thủ | Format | Điểm yếu ta khai thác |
|---|---|---|
| freeCodeCamp (2.8M views, 6 năm tuổi) | Marathon 3 giờ, tiếng Anh | Lỗi thời, không ai xem hết |
| Net Ninja Crash Course | Series ngắn 10 phút/ep | Giảng một chiều, copy-follow, không giải thích "why" |
| The Techzeen (50 video) | Toàn tập Hindi/Urdu | Không phục vụ người Việt |
| Code with Vlad, Michael Guay | REST API + TypeORM/Prisma | Giả định viewer đã biết Express + OOP, Fresher dễ tụt |
| Content tiếng Việt | Rất mỏng, chủ yếu blog | Không có series NestJS tiếng Việt chất lượng trên YouTube |

**Khoảng trống:** series tiếng Việt cho Fresher + học CÙNG AI agent (Opus + Antigravity, AI scaffold theo feature-based) + format 8–10 phút + "AI viết — mình hiểu" thay vì copy theo tutorial.

---

## PART 1 — SCRIPT

Chào mọi người đến với Lập trình là cuộc sống — dạo gần đây mình thấy các khóa học NestJS trên mạng khá cũ, và chưa có tutorial nào thật sự dùng AI để học một framework mới. Vì vậy mình làm series này theo một tinh thần khác: không bắt AI làm hộ, mà biến AI thành mentor cho mình.

Hiện tại có rất nhiều IDE hỗ trợ lập trình bằng AI. Mình chọn Antigravity vì nó free — model Opus chạy ngay trong agent panel, đọc được codebase thật. Series này mình cũng cố gắng hướng dẫn áp dụng AI với chi phí thấp nhất. Cách học của mình: hỏi nhiều hơn gõ. Hai buổi tối, mình vào được NestJS.

Nói nhanh NestJS là gì, cho đúng bản chất. Nó là framework backend chạy trên Node. Bên trong vẫn là Express — Nest không thay Express. Nó đóng thêm một lớp kiến trúc lên trên. Express giao cho bạn dây và gỗ. Nest giao bạn ngôi nhà có phòng: ai làm gì, nằm ở đâu, rõ ràng. Đó là lý do công ty dùng nó — không phải vì nhanh, mà vì mười người code chung không giẫm chân nhau.

Làm thật. Terminal: node -v — Nest cần Node hai mươi trở lên. npm i -g @nestjs/cli, rồi nest new task-app, chọn npm. Chạy ngay: npm run start:dev — watch mode, lưu file là server tự restart. Browser mở localhost cổng ba nghìn: Hello World. Chưa có gì hay.

App chạy rồi — dừng lại một nhịp. Toàn bộ series này, mình làm việc với AI theo đúng một quy trình chuẩn sáu bước — AI-Driven Development Workflow. Một: yêu cầu — mô tả mục tiêu kèm context. Hai: AI lên plan. Ba: mình review plan bằng mắt. Bốn: mình approve. Năm: AI mới được thực hiện code. Sáu: kiểm chứng — git diff, test, chạy lại app. AI không bao giờ tự ý sửa. Ghi nhớ sáu bước này — lát nữa mình dùng nó thật. Giờ xem app vừa sinh ra đi từ đâu.

Trước khi trace, hỏi câu chất vấn hơn: vì sao Nest sinh ra đúng những file này? Vì nó ra đời để lấp một khoảng trống. Năm hai nghìn không trăm mười bảy, một dev người Ba Lan tên Ca-min nhìn thấy Node đã có vô số library, mà không ai giải bài toán kiến trúc. Anh đem tinh thần Angular — framework của Google — sang backend, mang theo ba thứ: TypeScript, để kiểu dữ liệu rõ ràng cho cả team; class với decorator, để framework đọc được code của bạn; và dependency injection, để test từng mảnh rời nhau. Mỗi file sinh ra đều có lý do. main.ts tách riêng, vì việc khởi động khác việc lắp ráp. File spec nằm sẵn cạnh service, vì ở Nest test là văn hóa mặc định — không phải tính năng cộng thêm. Hiểu lý do sinh ra, bạn không cần học thuộc cấu trúc nữa.

Trace một request, từng chặng. Chặng một: main.ts. Toàn bộ app bắt đầu từ NestFactory dot create, truyền vào AppModule — module gốc khởi động toàn bộ app. Rồi app dot listen cổng ba nghìn. File này chạy đúng một lần, sinh ra toàn bộ ứng dụng.

Chặng hai: AppModule. Module là hộp đựng — mỗi tính năng một hộp, tự khai báo bên trong có controller nào, service nào, cần hộp nào khác. App thật là cây module: gốc là AppModule, cành là từng feature. Nest quét cây này lúc khởi động để biết mọi thứ nằm ở đâu.

Nhưng để ý: nest new xếp code theo LOẠI — controller một kệ, service một kệ, như tủ quần áo. Dự án nhỏ thì ổn; mười feature thì sửa một tính năng phải mở năm folder. Công ty làm theo feature, code cũng nên thế: mỗi folder một tính năng tự trọn — module, controller, service, dto nằm cạnh nhau. Mở một folder là đủ cả bộ. Tên gọi: feature-based. Lát nữa nhờ AI xếp lại cho.

Chặng ba — điểm hay nhất: Nest đọc cây đó bằng cách nào? Bằng chữ @ đó — decorator. @Controller không phải magic. Khi TypeScript dịch code, decorator gắn một tấm nhãn metadata lên class. Nest khởi động, đọc hết nhãn bằng reflect-metadata, tự dựng bảng routing: GET slash tasks trỏ về method nào, POST trỏ về method nào. Decorator chính là giấy tờ tùy thân của class trong mắt framework. Hiểu tới đây, nửa sự ma thuật của Nest tan biến.

Chặng bốn: request vào controller. Nhiệm vụ controller đúng một: nhận đơn, kiểm tra, giao việc. Nó không chứa logic — như lễ tân không xuống sửa xe. Việc nặng nằm trong service — class gắn @Injectable, chứa business logic thật. Tách hai lớp vậy vì một lý do: test. Service test được không cần HTTP, controller mỏng đến mức gần như không bao giờ bug.

Câu hỏi hay nhất của người mới: service đến với controller bằng cách nào? Nhìn constructor: private readonly tasksService. Bạn không bao giờ gõ new TasksService — không ai gõ. Nest tạo sẵn object, giữ trong IoC container, ai cần thì tiêm nấy. Tiêm — inject. Service mặc định là singleton: một bản duy nhất cho cả app. Không phải chi tiết phụ — đây là lý do tồn tại của framework, và là câu phỏng vấn kinh điển.

Giờ mới tới phần vui. Mở Antigravity, chọn model Opus. Prompt đầu tiên của mình luôn là: giải thích cấu trúc src cho một fresher — dùng code thật của project tao, đừng lấy ví dụ generic. Nó đọc đúng file mình có, chỉ đúng dòng mình thấy. Hỏi tiếp Dependency Injection là gì — nó vẽ ra flow Nest tạo, container giữ, constructor nhận. Đúng cái mình vừa học. Kiến thức đóng đinh.

Prompt thứ hai — việc mà làm tay mất nguyên một buổi: xếp lại project theo feature-based, hết lỗi compile là được. Và đây là lúc quy trình sáu bước lên sân. Opus không chạy ngay — nó trình bản plan: move file nào, tạo folder nào, sửa dòng import nào. Mình đọc từng dòng như review pull request, thấy chỗ lạ thì hỏi, nó giải thích. Hết ý kiến, bấm duyệt. Nó là agent — nó sửa file thật, không chỉ miệng nói. Vài giây, cây thư mục đảo nhà. Kiểm chứng: git diff đối chiếu với plan nó cam kết, chạy lại app — vẫn xanh. Đó là vòng làm việc với AI khi đi làm thật — và cũng là vòng senior làm với bạn.

Prompt thứ ba: nest g resource tasks làm gì. Opus giải thích rồi chạy luôn: mười giây, sinh controller, service, module, thư mục dto — vào đúng folder feature. DTO — Data Transfer Object — hợp đồng dữ liệu vào ra: khách đặt món qua form chuẩn, không nhảy thẳng vào bếp. Hỏi ngược tiếp: bỏ DTO đi thì sao? Nó trả lời thẳng: payload bậy tràn vào service, dữ liệu bẩn chảy xuống database. Tự hỏi một câu, nhớ lâu hơn đọc mười trang docs — đó là ranh giới giữa học và copy.

Và một prompt nữa — prompt mình tâm đắc nhất. Đây là chỗ AI khác hẳn tutorial: nó không chỉ giúp bạn làm, nó giúp bạn làm NHANH LẦN SAU. Mình bảo Opus: viết cho tao một SKILL — một file hướng dẫn đóng gói quy trình — để từ giờ mỗi lần cần thêm feature mới, nó làm đúng chuẩn: trình plan trước, chờ tao approve, rồi mới sinh folder feature-based với module, controller, service, dto, đăng ký vào AppModule, luôn luôn kèm validation. Opus trình plan cấu trúc skill — mình duyệt — approve — nó viết file tạo-feature.md: nguyên quy trình, cấu trúc file mẫu, checklist hoàn thành. Từ giờ muốn thêm feature labels hay comments, mình chỉ nói một câu — và vẫn được duyệt plan như thường. Lần sau không cần nhớ các bước — chỉ cần nhớ là CÓ skill. Kiến thức của bạn nằm lại trong project, không nằm trong đầu bạn.

Nguyên tắc của mình: AI sinh code, mình phải tự tay gõ lại ít nhất một lần. Mình thêm endpoint đếm số task — không copy, gõ từ đầu: một Get decorator, một method trong service. Gõ xong, watch mode tự reload. Chạy được.

Khoảnh khắc đền đáp. Postman: POST một task lên slash tasks — response hai nghìn một, created. GET lại danh sách — data nằm đó. Không màu mè. Nhưng lần đầu tiên, mình hiểu từng chặng request đi qua vì sao nó chạy. Cái hiểu đó, tutorial ba tiếng không mua được.

NestJS không khó. Học một mình mới khó. AI không tự làm bạn giỏi hơn — cách bạn dùng AI mới làm bạn giỏi. Đọc từng đoạn nó viết. Chất vấn nó. Và bắt buộc: giải thích lại được cho người khác. Kỹ năng đọc code AI là kỹ năng sống còn của dev mới mười năm tới. AI viết, mình hiểu. Đó là cách.

Series ba mươi tập này đi từ số 0 tới production thật: validation, database, auth, Docker, deploy — mỗi tập một mảnh của cùng một project. Subscribe để không lỡ tập hai. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Setup reminder:** Antigravity IDE dark theme (dùng mãi một theme), font JetBrains Mono ≥18px, ẩn sidebar + minimap, agent panel Opus đặt bên phải màn hình. Quay 1920×1080, highlight con trỏ chuột.

| # | Type | Nội dung quay | Thoại khớp | Thời lượng |
|---|---|---|---|---|
| 1 | [B-ROLL] | Title card series "NestJS #01 — Học framework cùng AI mentor" trên nền màn hình tối; lướt nhanh 2-3 thumbnail khóa học NestJS cũ trên YouTube | Lời chào + lý do series | 20s |
| 2 | [TERM] | `node -v` → `npm i -g @nestjs/cli` → `nest new task-app` (chọn npm) | "Làm thật" | 40s |
| 3 | [TERM] | `npm run start:dev` → [BROWSER] localhost:3000 Hello World | "Chạy trước đã" | 25s |
| 4 | [DIAGRAM] | Excalidraw: quy trình 6 bước AI-Driven Development Workflow — Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng (vòng tròn khép kín) | "Quy trình chuẩn 6 bước" | 25s |
| 5 | [IDE] | Cây file nest new sinh: main.ts, app.module, app.controller, app.service, **file .spec** (zoom), tsconfig — mỗi file hiện caption lý do ngắn góc màn hình | "Vì sao sinh ra như vậy — gốc Angular" | 35s |
| 6 | [IDE] | main.ts — highlight `NestFactory.create(AppModule)` + `listen(3000)` | Chặng 1: điểm khởi động | 35s |
| 7 | [IDE] | app.module.ts — mở `imports`, `controllers`, `providers`; [DIAGRAM] cây module AppModule gốc → cành feature | Chặng 2: hộp đựng + cây module | 45s |
| 8 | [DIAGRAM] | 2 ô so sánh: xếp theo LOẠI (tủ quần áo) vs theo FEATURE (folder tự trọn) — cây thư mục type-based của nest new bên trái | "Tủ quần áo vs folder tự trọn" | 35s |
| 9 | [IDE] | tasks.controller.ts — highlight @Controller, @Get, @Post; vẽ nhanh bảng routing `GET /tasks → findAll()` | Chặng 3: decorator = nhãn metadata, Nest dựng bảng routing | 55s |
| 10 | [IDE] | Split controller vs service — controller gõ mỏng, service chứa logic; highlight @Injectable | Chặng 4: lễ tân vs thợ | 35s |
| 11 | [IDE] | Constructor `private readonly tasksService` — zoom; [DIAGRAM] IoC container: Nest tạo → bảng chứa → tiêm constructor; nhãn singleton | "Câu hỏi hay nhất" — DI | 45s |
| 12 | [IDE] | Antigravity agent panel (Opus): prompt 1 "giải thích cấu trúc src cho fresher, dùng code thật" → trả lời trỏ đúng file; hỏi "DI là gì?" — flow khớp hình vừa học | "Prompt đầu tiên — kiến thức đóng đinh" | 40s |
| 13 | [IDE] | Agent prompt 2 — chạy đủ 6 bước trên màn hình: (1) gõ yêu cầu → (2) Opus trình **PLAN** → (3) host đọc plan từng dòng, hỏi 1 chỗ lạ → (4) bấm **APPROVE** → (5) cây thư mục đảo nhà → (6) [TERM] `git diff --stat` đối chiếu plan + `npm run start:dev` vẫn xanh | "Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng" | 55s |
| 14 | [TERM]+[IDE] | `nest g resource tasks` (chọn REST API) → sinh vào đúng folder feature + dto/; agent giải thích DTO; hỏi "bỏ DTO thì sao?" | "Hợp đồng dữ liệu + chất vấn" | 40s |
| 15 | [IDE] | Agent prompt 4: "viết SKILL tạo-feature — nói tên feature là sinh chuẩn project này" → file `tao-feature.md` hiện ra, scroll nhanh nội dung (quy trình + cấu trúc mẫu + checklist); demo 1 câu "thêm feature labels" → folder labels sinh ra | "Kiến thức nằm lại trong project" | 40s |
| 16 | [IDE] | Host gõ tay endpoint `getTaskCount()` (không copy), save, watch reload | "Ranh giới học và copy" | 30s |
| 17 | [TERM]+[BROWSER] | Postman: POST /tasks → 201 → GET /tasks thấy JSON | "Khoảnh khắc đền đáp" | 35s |
| 18 | [B-ROLL] | Cà phê, màn hình soi nhẹ; end card subscribe neon + "NestJS #02" teaser | "AI viết, mình hiểu" + CTA | 35s |

**Tổng: ~670s ≈ 11:10.** Batch: cảnh 1+18 quay chung buổi B-roll; cảnh 2+3 idempotent (xóa folder chạy lại được); cảnh 12–15 là agent panel — quay thật, giữ nguyên câu hỏi lẫn câu trả lời, đừng edit đẹp.

**Code chuẩn bị trước:**
```bash
node -v                      # ≥ 20
npm i -g @nestjs/cli
nest new task-app            # chọn npm
cd task-app
npm run start:dev            # localhost:3000 → Hello World!
nest g resource tasks        # REST API, CRUD entry points: Yes
```
Prompt 2 cho Opus (restructure — chuẩn bị sẵn):
```
Restructure this NestJS project to feature-based architecture:
- Each feature gets its own folder under src/ (module, controller, service, dto together)
- Move app.controller/app.service into a feature folder or remove leftovers
- Keep the app compiling and running with zero errors
RULE: Do NOT edit any file yet. First present a PLAN (which files to move,
which folders to create, which imports to fix). Wait for my approval. Only
after I approve, execute the plan. Show me what you moved when done.
```
Prompt 4 cho Opus (tạo SKILL — chuẩn bị sẵn):
```
Write a SKILL file (tao-feature.md) for this project — a reusable playbook so that
whenever I ask for a new feature, you scaffold it consistently:
- RULE: always present a PLAN first and wait for my approval before writing any code
- Input: just the feature name
- Output: feature-based folder (module, controller, service, dto) under src/
- Always register the new module in AppModule
- Always include DTO validation rules
- Include a completion checklist (compiles, app boots, CRUD responds)
Save it in the project so future sessions can reuse it.
```
Endpoint tự gõ (cảnh 16):
```typescript
// tasks.controller.ts
@Get('count')
getTaskCount(): number {
  return this.tasksService.countAll();
}
// tasks.service.ts
countAll(): number {
  return this.tasks.length; // mảng in-memory — ep3 thay bằng DB
}
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS (Nano Banana 2 / Imagen in Flow)

1. `A cinematic photograph of a young developer at night leaning toward his monitor while an AI agent chat panel glows on the right half of the screen and a NestJS file tree glows on the left half, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of a developer's hand pointing at a glowing diagram of boxes and arrows representing modules controllers and services on a dark screen, while an AI chat panel explains beside it, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of two coffee cups on a dark desk in front of one glowing monitor — one cup before the keyboard for the developer and one beside an AI agent panel on screen, symbolizing a mentor sitting beside you, dark moody lighting, monitor glow illuminating the scene, code visible on screen with syntax highlighting in green and cyan on dark background, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial or developer documentary. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5) — đánh số series

1. NestJS #01: Từ số 0 đến CRUD đầu tiên cùng Opus | Lập trình là cuộc sống
2. NestJS #01: Học framework bằng AI mentor — không phải AI làm hộ | Lập trình là cuộc sống
3. NestJS #01: Module, Controller, Service, DI — trace 1 request từng chặng | Lập trình là cuộc sống
4. NestJS #01: Nhờ AI xếp codebase theo feature-based trong 10 giây | Lập trình là cuộc sống
5. NestJS #01: Decorator là gì? Bóc trần "ma thuật" của NestJS cho Fresher | Lập trình là cuộc sống

### 4b. SEO Description

```
Các khóa học NestJS trên mạng khá cũ — và chưa có tutorial nào thật sự dùng AI để học một framework mới. Series này mình làm khác: không bắt AI làm hộ, mà biến AI thành mentor (Opus trong Antigravity) — hỏi, đọc, chất vấn, tự gõ lại.

✅ NestJS là gì THẬT SỰ: lớp kiến trúc trên Express
✅ Trace 1 request từng chặng: main.ts → AppModule → Controller → Service
✅ Decorator = nhãn metadata — Nest đọc nhãn, tự dựng bảng routing
✅ Dependency Injection + IoC container + singleton — câu phỏng vấn kinh điển
✅ Nhờ Opus restructure codebase theo feature-based — rồi git diff kiểm chứng
✅ nest g resource: sinh CRUD + DTO trong 10 giây
✅ Hỏi ngược AI "bỏ DTO thì sao?" — nhớ lâu hơn 10 trang docs
✅ Nguyên tắc: AI viết, mình hiểu — tự gõ lại mới là của mình

🔗 Links:
NestJS docs: https://docs.nestjs.com/
Series plan 30 tập: https://github.com/ptit9x/youtube-coding-for-life

⏱ Timestamps:
0:00 Lời chào + lý do làm series — AI mentor, không phải AI làm hộ
0:35 NestJS là gì — lớp kiến trúc trên Express
1:15 Cài NestJS CLI + nest new + Hello World
1:45 AI-Driven Development Workflow — quy trình 6 bước
2:15 Vì sao nest new sinh ra đúng những file này
2:50 Chặng 1: main.ts — điểm khởi động app
3:25 Chặng 2: AppModule — cây module + feature-based là gì
4:35 Chặng 3: Decorator — bóc trần ma thuật
5:35 Chặng 4: Controller vs Service — lễ tân và thợ
6:10 Dependency Injection + IoC container
6:55 Prompt 1: Opus giải thích project thật
7:35 Prompt 2: restructure feature-based — 6 bước thật + git diff
8:30 Prompt 3: nest g resource + DTO + chất vấn
9:10 Prompt 4: SKILL tạo-feature — kiến thức nằm lại trong project
9:50 Tự gõ endpoint + Postman 201
10:20 AI viết, mình hiểu + series 30 tập

#NestJS #HocNestJS #Opus #Antigravity #AIMentor #FeatureBased #Fresher #Backend #TypeScript #NodeJS #DependencyInjection #LapTrinhLaCuocSong #DevVietNam
```

### 4c. Keywords / Tags

```
nestjs, học nestjs, nestjs cho người mới bắt đầu, nestjs tiếng việt, nestjs series, nestjs tập 1, opus, antigravity, ai mentor, học lập trình bằng ai, ai viết code, claude opus, google antigravity, feature based architecture, cấu trúc project nestjs, nestjs fresher, backend fresher, nestjs module controller service, nestjs dependency injection, decorator là gì, ioc container, nest g resource, typescript backend, node js framework, lập trình là cuộc sống, dev việt nam, fresher developer việt nam
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

### Option 1 — "AI mentor" (khuyên dùng cho tập 1)

*Image prompt (x4 resolution):*
`A cinematic photograph, a young developer seen from behind at a dark desk with a glowing dual-pane screen showing an AI agent chat panel on one side and NestJS code on the other, a second empty chair beside him subtly lit by monitor glow as if a mentor is present, dramatic neon lighting in cyan and green, code text floating and reflecting on the desk surface, dark moody background with city bokeh through window, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

*Text spec:*
- Dòng 1: `NESTJS #01` — WHITE (font JetBrains Mono, nhỏ hơn)
- Dòng 2: `HỌC CÙNG` — WHITE
- Dòng 3: `OPUS` — NEON GREEN `#00FF41`

### Option 2 — "AI đảo nhà codebase"

*Image prompt (x4 resolution):*
`A cinematic photograph, glowing holographic file folders with code symbols flying through the air and rearranging themselves into neat labeled stacks above a developer's desk while the developer watches with arms crossed, an AI agent panel glowing on the monitor, dramatic neon lighting in green and cyan, code text floating and reflecting in the scene, dark moody background with fog and city bokeh, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

*Text spec:*
- Dòng 1: `NESTJS #01` — WHITE (JetBrains Mono)
- Dòng 2: `AI XẾP` — WHITE
- Dòng 3: `CODEBASE` — NEON GREEN `#00FF41`
- Badge nhỏ: `10 GIÂY` — WHITE trên box `#1a1a2e` viền neon

### Option 3 — "Bóc trần ma thuật"

*Image prompt (x4 resolution):*
`A cinematic photograph, a developer silhouette pointing at a floating neon diagram of connected boxes labeled with at-symbols like a constellation map while an AI hologram hand reveals the hidden wiring behind it, dramatic neon lighting in green and cyan, code text floating and reflecting in the scene, dark moody background with fog and city bokeh, high contrast, dramatic rim lighting, deep shadows, vivid saturated neon colors, subject positioned on the right side of the frame leaving empty dark space on the left for text, 8k, 16:9. Photorealistic, not cartoon or illustration.`

*Text spec:*
- Dòng 1: `NESTJS #01` — WHITE (JetBrains Mono)
- Dòng 2: `BÓC TRẦN` — WHITE
- Dòng 3: `MA THUẬT` — NEON GREEN `#00FF41`

*Typography specs (chung — typeset trong Canva):*
- Canvas 1280×720. Font **Anton** cho text chính, **JetBrains Mono** cho số tập + badge.
- Số tập `#01` đặt góc trên khối text, nhỏ hơn dòng chính ~40% — vị trí cố định mọi tập (brand anchor).
- Mỗi dòng 15–20% chiều cao frame, line spacing 0.85, khối text ~1/3 bề ngang, căn trái.
- Neon glow: duplicate layer, blur 8–12px, opacity 60–70%, stroke đen 6–10px.
- Không đè chữ lên mặt người. Overlay scan-line/noise nhẹ. Giữ bản sạch không chữ.
