# NestJS #01 — Học NestJS với AI: Xây Users API đầu tiên

- **Series:** Học NestJS bằng AI — tập 1/46
- **Định dạng:** Host tự quay màn hình + tự thoại âm. Không AI voice, không AI footage.
- **AI tool:** Opus trong Antigravity IDE; có thể thay bằng coding agent khác nhưng giữ nguyên workflow.
- **Technical baseline:** NestJS 12, Node.js 24 Active LTS, npm, ESM (Nest CLI 12 sinh sẵn `"type": "module"`).
- **Target runtime:** ~11:15 (khung phù hợp: 10–12 phút)
- **Audience:** Dev mới vào nghề / Fresher — lần đầu chạm backend framework.
- **Outcome chính:** Hiểu đường đi của một request và chạy được Users API trong `src/modules/users` bằng mảng in-memory.
- **Pain mở tập 2:** DTO khai báo `email` là string nhưng payload số vẫn lọt qua vì chưa có validation runtime.

---

## PART 1 — SCRIPT

AI dựng Users API trong vài giây. Nhưng khi API lỗi, bạn không biết request đã đi qua file nào. Code chạy mà không hiểu vẫn giống tháo dây điện trong phòng tối.

Mình từng học framework bằng cách mở tutorial rồi gõ theo. Code chạy thì vui. Nhưng khi đổi tên một file, mọi thứ vỡ và mình không biết vì sao. Lần này ta làm khác. AI có thể viết, nhưng trước đó mình phải hiểu đường đi của code.

NestJS là framework backend chạy trên Node.js. Mặc định, nó dùng Express ở bên dưới; bạn cũng có thể đổi sang Fastify. Phần Nest thêm vào là kiến trúc: module gom tính năng, controller nhận request, còn service xử lý logic. Nó giống một bản sơ đồ điện được dán sẵn lên căn nhà. Khi nhiều người cùng sửa, ai cũng biết dây nào đi về đâu.

Bắt đầu từ terminal. Gõ `node -v`. Với Nest CLI hiện tại, cách an toàn nhất là dùng bản Node Active LTS mới nhất. Máy mình đang dùng phiên bản hiện trên màn hình. Tiếp theo, cài CLI bằng `npm i -g @nestjs/cli`, rồi chạy `nest new taskflow-api`.

CLI hỏi package manager. Nest CLI 12 sinh sẵn ESM, `"type": "module"`, không cần chọn gì thêm. Hai lựa chọn này không thay đổi những khái niệm Nest mà ta sắp học. Cài xong, vào thư mục project và chạy `npm run start:dev`. Browser mở `localhost:3000`. Dòng Hello World xuất hiện.

Trước khi thêm code, đây là workflow dùng AI xuyên suốt series. Mình đưa yêu cầu và context. AI chỉ trình plan, chưa được sửa file. Mình đọc, chất vấn và approve. Sau đó AI mới thực hiện. Cuối cùng, mình xem git diff, chạy test và gọi API thật. Sáu bước: yêu cầu, plan, review, approve, thực hiện, kiểm chứng.

Giờ trace request Hello World đang chạy. Điểm bắt đầu là `main.ts`. `NestFactory.create` nhận `AppModule` và dựng ứng dụng. `app.listen` mở cổng để chờ request. File này là công tắc tổng: bật hệ thống lên, nhưng không chứa nghiệp vụ.

Từ `main.ts`, Nest đi vào `AppModule`. Module là ranh giới của một nhóm tính năng. Nó khai báo controller nào nhận request và provider nào cung cấp logic. App lớn sẽ có một cây module. `AppModule` là gốc; Users, Auth hay Tasks sẽ là các nhánh.

Series này dùng bốn khu vực chính. `modules` chứa business domain. `common` chứa code cross-cutting đã thật sự được dùng lại. `config` quản lý cấu hình, còn `database` nối ứng dụng với hạ tầng dữ liệu. Ta không tạo hàng loạt folder rỗng ngay hôm nay. Cấu trúc sẽ lớn lên cùng nhu cầu thật của project.

Dependency cũng phải đi một chiều. Controller gọi service hoặc use-case. Lớp nghiệp vụ phụ thuộc vào repository contract, không phụ thuộc trực tiếp database cụ thể. Infrastructure sẽ implement contract đó và module chịu trách nhiệm nối hai phía. Tập đầu chưa có database, nên ta bắt đầu bằng một module Users đơn giản.

Tiếp theo là `AppController`. Decorator `@Controller` gắn metadata lên class. Decorator `@Get` nói rằng method bên dưới xử lý request GET. Khi khởi động, Nest đọc metadata này và dựng bảng routing. Chữ @ không phải phép thuật; nó là nhãn để framework hiểu code của mình.

Controller nhận request rồi giao việc cho `AppService`. Logic nằm trong service để nó có thể được dùng lại và test mà không cần khởi động HTTP. Controller càng mỏng, đường đi của request càng dễ đọc.

Service đến controller bằng dependency injection. Nhìn vào constructor: `private readonly appService`. Ta không hề gọi `new AppService`. Nest tạo provider, giữ nó trong IoC container rồi tiêm vào nơi cần dùng. Provider mặc định dùng một instance chung trong ứng dụng. Nest cũng hỗ trợ các scope khác khi thật sự cần.

Bây giờ mới giao việc cho AI. Mình mở agent panel và đưa một yêu cầu có giới hạn rõ ràng:

“Đọc project NestJS hiện tại. Tôi cần một Users API dùng mảng in-memory trong `src/modules/users`. Hãy dùng `nest g resource modules/users`, hoàn thiện create, find all và count. DTO chỉ khai báo type, chưa thêm validation. Trước tiên chỉ trình plan: file nào thay đổi, request đi qua đâu và kiểm chứng bằng lệnh nào. Không sửa file trước khi tôi approve.”

AI trả về plan. Nó sẽ tạo `src/modules/users`, gồm module, controller, service, DTO và entity. `UsersModule` được đăng ký vào `AppModule`. Service giữ một mảng trong RAM. Controller chuyển request xuống service. Mình kiểm tra lại: không database, không ValidationPipe, không tạo sẵn `common` chỉ để cây thư mục trông đẹp.

Có một chi tiết cần kiểm tra: vị trí route `GET /users/count`. Nếu đặt dưới `GET /users/:id` khi dùng Express, chữ `count` có thể bị hiểu thành một id. Plan phải đặt route tĩnh trước route động. AI sửa plan. Bây giờ mình mới approve.

Agent chạy generator và hoàn thiện code. Mình không nhìn animation rồi tin luôn. Mở git diff. `CreateUserDto` có `name` và `email`. `UsersService` có mảng `users`, một biến tăng id, cùng các method create và findAll. Không có database bí mật nào xuất hiện. Chạy build; terminal xanh. Chạy app; Hello World vẫn còn.

Nguyên tắc của mình là AI sinh code thì mình phải tự gõ lại ít nhất một phần. Mình thêm `countAll` trong service. Sau đó thêm `@Get('count')` trong controller và đặt nó trước `@Get(':id')`. Watch mode reload, không báo lỗi. Đoạn code ngắn, nhưng mình biết nó nằm ở đó vì sao.

Đến lúc kiểm chứng. Trong Postman, gửi POST `/users` với tên Richard và một email hợp lệ. Server trả 201 cùng user có id. Gửi GET `/users`, user vừa tạo nằm trong mảng. Gửi GET `/users/count`, kết quả là một. Request đã đi đúng con đường mình vừa trace: controller, service rồi quay về response.

Nhưng thử đổi payload thành `{ "name": "Richard", "email": 123 }`. TypeScript nói email phải là string, vậy mà server vẫn nhận. Không phải Nest bị lỗi. Type của TypeScript biến mất khi code chạy, còn DTO hiện chưa có luật kiểm tra runtime.

Đó là vết nứt đầu tiên của API này. Tập sau, mình sẽ dùng ValidationPipe để biến hợp đồng DTO thành một cánh cửa thật. Dữ liệu sai phải dừng trước khi chạm vào service.

AI không tự làm bạn giỏi hơn. Quy trình đọc, chất vấn và kiểm chứng code của nó mới làm được điều đó. AI viết, mình hiểu. Đó là cách series này sẽ đi tiếp.

Nếu bạn muốn thấy payload bậy bị chặn ngay từ cửa, gặp lại ở NestJS số hai. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

**Setup:** Antigravity IDE dark theme, JetBrains Mono ≥18px, ẩn minimap và panel thừa. Agent panel đặt bên phải. Quay 1920×1080, con trỏ có highlight. Không dùng footage AI trong video.

| # | Type | Nội dung quay | Thoại khớp | Thời lượng |
|---|---|---|---|---|
| 1 | [B-ROLL]+[IDE] | Repo NestJS thật; mở nhanh cây `src`, dừng ở các decorator và constructor | Cold open: repo chạy nhưng không biết request đi đâu | 30s |
| 2 | [DIAGRAM] | Một lớp Nest nằm trên Express/Fastify; bên phải là Module → Controller → Service | NestJS là gì và giá trị kiến trúc | 35s |
| 3 | [TERM] | `node -v`, cài CLI, `nest new taskflow-api`; chọn npm; từ chối observability nếu CLI hỏi | Setup bằng phiên bản hiện hành | 40s |
| 4 | [TERM]+[BROWSER] | `npm run start:dev` → `localhost:3000` → Hello World | Chạy trước khi sửa | 25s |
| 5 | [DIAGRAM] | Vòng sáu bước: Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng | Workflow AI của series | 40s |
| 6 | [IDE] | `main.ts`; highlight `NestFactory.create(AppModule)` và `listen` | Chặng 1: bootstrap | 45s |
| 7 | [IDE]+[DIAGRAM] | `app.module.ts`; nối AppModule tới `modules/users`; hiện sơ đồ đích `common/config/database/modules` | Chặng 2: business module và chiều dependency | 65s |
| 8 | [IDE] | `app.controller.ts` và `app.service.ts` đặt cạnh nhau; highlight `@Controller`, `@Get`, lời gọi service | Chặng 3: controller và service | 45s |
| 9 | [IDE]+[DIAGRAM] | Zoom constructor; vẽ IoC container tạo và tiêm AppService | Decorator và dependency injection | 55s |
| 10 | [IDE] | Gõ nguyên prompt Users API; agent chỉ trả plan, chưa sửa code | Yêu cầu → plan → review | 60s |
| 11 | [IDE] | Host hỏi về `/count` và `/:id`; agent cập nhật plan; host approve | Chất vấn route order | 50s |
| 12 | [TERM]+[IDE] | `nest g resource modules/users`; cây `src/modules/users`; agent hoàn thiện in-memory service | Thực hiện | 40s |
| 13 | [IDE]+[TERM] | Xem `git diff`; mở DTO, service, AppModule; chạy build | Kiểm chứng thay đổi | 45s |
| 14 | [IDE] | Host tự gõ `countAll` và `@Get('count')` trước `@Get(':id')` | Tự gõ để hiểu | 40s |
| 15 | [BROWSER] | Postman: POST user hợp lệ → 201; GET list; GET count → `{ "count": 1 }` | Thành quả | 35s |
| 16 | [BROWSER]+[B-ROLL] | POST với `email: 123` vẫn 201; freeze frame payload sai; end card EP02 Validation | Pain mới + CTA | 25s |

**Tổng: 675 giây ≈ 11:15.** Timestamps ở Part 4 bám trực tiếp tổng thời lượng này; sau khi thu voice thật, cập nhật lại theo waveform.

### Command chuẩn bị

```bash
node -v
npm i -g @nestjs/cli
nest new taskflow-api
# Chọn npm. CLI 12 không hỏi module type — sinh sẵn ESM "type": "module".
# Nếu CLI hỏi observability (@nestjs/observe), chọn No để giữ project tối giản.
cd taskflow-api
npm run start:dev
nest g resource modules/users --no-spec
# Chọn REST API, CRUD entry points: Yes
```

### Prompt cho Opus

```text
Read this NestJS project. I need an in-memory Users API under `src/modules/users`.

Requirements:
- Use `nest g resource modules/users --no-spec`.
- Implement create, find all, find one, update and remove with an in-memory array.
- Add a count method and expose GET /users/count.
- Keep GET /users/count before GET /users/:id so Express does not shadow it.
- CreateUserDto has `name` and `email` TypeScript fields only.
- Do not install class-validator and do not enable ValidationPipe yet.
- Do not add a database or unrelated dependencies.
- Do not create empty common, config or database folders yet.

Workflow:
1. Do not edit files yet.
2. First show a plan listing every file to create or change.
3. Explain the request flow and verification commands.
4. Wait for my approval.
5. After approval, implement the plan.
6. Finish with a concise change summary and verification results.
```

### Code đích để đối chiếu khi quay

```typescript
// modules/users/dto/create-user.dto.ts
export class CreateUserDto {
  name!: string;
  email!: string;
}

// modules/users/entities/user.entity.ts
export class User {
  id!: number;
  name!: string;
  email!: string;
}
```

```typescript
// modules/users/users.service.ts — các phần cốt lõi
private readonly users: User[] = [];
private nextId = 1;

create(createUserDto: CreateUserDto): User {
  const user: User = {
    id: this.nextId++,
    name: createUserDto.name,
    email: createUserDto.email,
  };
  this.users.push(user);
  return user;
}

findAll(): User[] {
  return this.users;
}

countAll(): number {
  return this.users.length;
}
```

```typescript
// modules/users/users.controller.ts — đặt route tĩnh trước route động
@Get('count')
count() {
  return { count: this.usersService.countAll() };
}

@Get(':id')
findOne(@Param('id') id: string) {
  return this.usersService.findOne(+id);
}
```

### Payload kiểm chứng

```json
{ "name": "Richard", "email": "richard@example.com" }
```

```json
{ "name": "Richard", "email": 123 }
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a young Vietnamese developer at a dark desk, positioned on the right, studying a widescreen monitor split between a NestJS TypeScript editor and a subtle AI agent panel, official NestJS red-pink #E0234E monitor light on his face, deep black and navy shadows, high contrast, subtle film grain, generous clean dark space on the left for typography, 16:9, photorealistic high-end technology documentary, no green or cyan accents, no text, no logos, no watermark.`

2. `A cinematic photograph of a Vietnamese developer tracing a glowing request path across a dark monitor, with connected code panels suggesting Module, Controller and Service, NestJS red-pink #E0234E arrows and white code reflections, focused expression, dramatic red rim lighting, dark city bokeh and subtle fog, subject on the right with empty dark space on the left for typography, 16:9, photorealistic, no green or cyan accents, no text, no logos, no watermark.`

3. `A cinematic close-up of a developer staring at an API payload where the email field contains the number 123 while white TypeScript code expects a string, a subtle AI panel beside the editor, tension from official NestJS red-pink #E0234E light against deep black shadows, dark late-night workspace, subject on the right and clean negative space on the left, 16:9, photorealistic technology documentary, no green or cyan accents, no text, no logos, no watermark.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Học NestJS với AI: Xây Users API đầu tiên — EP01 | Lập trình là cuộc sống
2. NestJS cho người mới: Module, Controller và Service — EP01 | Lập trình là cuộc sống
3. Luồng request trong NestJS hoạt động thế nào? — EP01 | Lập trình là cuộc sống
4. Tạo REST API đầu tiên bằng NestJS — EP01 | Lập trình là cuộc sống
5. Dùng AI học NestJS mà không copy code — EP01 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 5 cho góc học bằng AI.

### 4b. SEO Description

```text
Mở một repo NestJS, API vẫn chạy nhưng request đi qua đâu thì không biết. Tập đầu của series sẽ trace đường đi đó và dựng một Users API thật cùng AI — theo quy trình plan, review, approve và kiểm chứng.

✅ Tạo project NestJS 12 bằng CLI
✅ Hiểu main.ts, AppModule, Controller và Service
✅ Decorator và Dependency Injection giải thích cho Fresher
✅ Dùng Opus trong Antigravity như mentor, không copy mù
✅ Users API in-memory trong src/modules/users
✅ Skeleton phát triển dần với common, config, database và modules
✅ Kiểm tra git diff, build và gọi API thật bằng Postman
✅ Thấy tận mắt vì sao DTO có type vẫn chưa chặn được payload sai

🔗 Links:
NestJS docs: https://docs.nestjs.com/
NestJS CLI: https://docs.nestjs.com/cli/overview
Source series: https://github.com/ptit9x/youtube-coding-for-life

⏱ Timestamps dự kiến:
0:00 Repo chạy nhưng không biết request đi đâu
0:30 NestJS là gì?
1:05 Cài CLI và tạo project
1:45 Hello World
2:10 Workflow AI sáu bước
2:50 main.ts — công tắc tổng
3:35 AppModule — business module và chiều dependency
4:40 Controller và Service
5:25 Decorator và Dependency Injection
6:20 Yêu cầu AI trình plan
7:20 Chất vấn route /count
8:10 AI thực hiện, mình xem diff
8:50 Tự gõ endpoint đếm user
9:35 Postman: POST, GET và count
10:15 Email là số vẫn lọt qua
10:50 Teaser ValidationPipe

#NestJS #HocNestJS #AICoding #Opus #Antigravity #Backend #TypeScript #NodeJS #Fresher #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs, học nestjs, nestjs tiếng việt, nestjs cho người mới, nestjs tập 1, nestjs 12, users api nestjs, nestjs modular architecture, nestjs common folder, nestjs controller service module, nestjs dependency injection, decorator là gì, nest g resource, dto nestjs, validationpipe nestjs, opus coding, antigravity ide, ai coding mentor, học backend cùng ai, typescript backend, nodejs backend, backend fresher, lập trình là cuộc sống, dev việt nam
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — “NestJS từ số 0” — khuyên dùng

- Badge nhỏ: `EP01` — WHITE, nền tối và viền NEST RED `#E0234E`
- Dòng 1: `NESTJS` — WHITE `#FFFFFF`
- Dòng 2: `TỪ SỐ 0` — NEST RED `#E0234E`
- Badge phụ: `CÙNG AI` — WHITE, nền tối và viền NEST RED `#E0234E`
- Hình: crop gần developer ở nửa phải; code trên monitor là lớp nền phụ; nửa trái tối và sạch.

### Option 2 — “Request đi đâu?”

- Dòng nhỏ: `NESTJS #01` — WHITE
- Dòng 1: `REQUEST` — WHITE
- Dòng 2: `ĐI ĐÂU?` — NEST RED `#E0234E`
- Hình: đường sáng đỏ hồng chạy qua ba node Module → Controller → Service.

### Option 3 — “DTO chưa đủ”

- Dòng nhỏ: `NESTJS #01` — WHITE
- Dòng 1: `DTO CÓ TYPE` — WHITE
- Dòng 2: `VẪN LỌT?` — NEST RED `#E0234E`
- Hình: payload `email: 123` màu đỏ đối diện code `email: string` màu trắng.

**Typography chung:** Canvas 1672×941. Anton cho headline, JetBrains Mono cho số tập. Mỗi dòng cao khoảng 150–185px, line spacing 0.85, stroke đen 8–12px và shadow gọn. Chỉ dùng WHITE `#FFFFFF` và NEST RED `#E0234E` cho typography; không dùng xanh lá hoặc cyan. Giữ nhân vật và monitor không bị chữ che. Nếu tạo bản nền không chữ, typeset lại trong Canva để duy trì typography xuyên suốt series.

### Thumbnail đã tạo

![Thumbnail NestJS EP01 — NestJS từ số 0 cùng AI](./thumbnail-01-hoc-nestjs-cung-ai.png)
