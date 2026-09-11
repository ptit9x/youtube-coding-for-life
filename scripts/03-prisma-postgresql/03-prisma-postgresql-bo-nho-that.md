# NestJS #03 — Kết nối PostgreSQL bằng Prisma

- **Series:** Học NestJS bằng AI — tập 3/46
- **Target runtime:** ~12 phút
- **Outcome:** Thay Users in-memory bằng PostgreSQL qua Prisma và repository contract.
- **Pain mở EP04:** Email trùng chạm unique constraint và biến thành lỗi 500 khó hiểu.

---

## PART 1 — SCRIPT

Một lần restart server, toàn bộ user vừa tạo biến mất. API trả 201 rất đẹp, nhưng trí nhớ của nó ngắn hơn cá vàng.

Mảng trong UsersService chỉ sống trong RAM. Process dừng, vùng nhớ bị giải phóng, dữ liệu cũng đi theo.

Ta cần PostgreSQL. Nhưng nếu UsersService gọi Prisma trực tiếp, business logic sẽ bị khóa vào một công cụ database.

Bước ngoặt nằm ở một lớp rất mỏng. Service chỉ biết hợp đồng repository, còn Prisma đứng phía sau thực hiện hợp đồng đó.

Repository giống quầy giao nhận của một cửa hàng. Nhân viên bán hàng chỉ đưa phiếu, không cần biết kho dùng xe nâng nào.

Trước khi cài, mình kiểm tra Node, Nest và Prisma trên màn hình. Prisma thay đổi khá nhanh, nên video không đoán phiên bản.

Project đang dùng CommonJS. Generator Prisma hỗ trợ `moduleFormat` là `cjs`, nên mình khai báo rõ thay vì dựa vào suy luận.

Mình cài Prisma, Prisma Client, PostgreSQL driver và adapter tương ứng. Sau đó khởi tạo thư mục `prisma` ở project root.

Schema bắt đầu bằng một model User. ID dùng UUID, email là duy nhất, còn thời gian tạo và sửa được database quản lý.

`schema.prisma` là bản thiết kế. Migration là lịch sử những lần bản thiết kế đó thay đổi.

Mình không tạo Role, Permission hay Task ngay lúc này. Một migration nhỏ dễ đọc hơn một migration chứa cả tương lai.

Tiếp theo, mình mở agent panel và đưa yêu cầu. AI chỉ được lên plan, chưa được sửa file.

Nó đề xuất cho UsersService inject PrismaService trực tiếp. Code ngắn thật, nhưng chiều dependency đã sai mục tiêu series.

Mình yêu cầu sửa plan thành ba phần. UsersRepository là contract, PrismaUsersRepository là adapter, UsersService chỉ thấy contract.

Contract có `create`, `findAll`, `findById` và `findByEmail`. Nó diễn tả nhu cầu của Users, không sao chép toàn bộ Prisma Client.

Đây là chi tiết quan trọng. Repository không phải áo khoác mới mặc lên mọi method database.

Nếu contract chứa cả trăm option của Prisma, ta chỉ đổi tên dependency chứ chưa tạo được boundary.

Sau khi approve, agent tạo `DatabaseModule` và `PrismaService`. Service này sở hữu kết nối và đóng kết nối đúng lifecycle.

`PrismaUsersRepository` nhận PrismaService. Method `create` gọi `prisma.user.create`, rồi trả về dữ liệu mà Users cần.

Trong UsersModule, một injection token nối contract với adapter. Nest container sẽ đưa adapter vào UsersService lúc runtime.

Mình mở git diff. Import Prisma chỉ xuất hiện trong database adapter, không xuất hiện trong UsersService hay controller.

Giờ đến phần mình tự gõ. Mình thêm `findByEmail` vào contract và adapter.

Method này chưa dùng để chặn email trùng. Nó sẽ trở thành dữ kiện cho tập error handling tiếp theo.

Mình chạy migration với tên `create_users`. Terminal tạo SQL, cập nhật database và generate client.

Đừng lướt qua file SQL. Mình mở nó, kiểm tra primary key, unique index và kiểu timestamp.

ORM giúp viết query thuận tiện. Nó không thay trách nhiệm hiểu database đã thay đổi thế nào.

Ứng dụng khởi động. Mình POST một user, GET danh sách, rồi dừng server.

Khoảnh khắc kiểm chứng thật sự đến sau khi server chạy lại. GET `/users` vẫn trả đúng user vừa tạo.

RAM đã quên, PostgreSQL thì chưa.

Nhưng mình gửi lại cùng email. Terminal đỏ lên với unique constraint, còn client nhận lỗi 500 lạnh lùng.

Database đã bảo vệ dữ liệu đúng. API chỉ chưa biết kể lỗi đó bằng ngôn ngữ của người gọi.

Tập sau, mình sẽ biến lỗi kỹ thuật thành 400, 404 hoặc 409 rõ ràng.

Một boundary tốt không làm database biến mất. Nó chỉ ngăn quyết định hạ tầng lan vào nơi chứa nghiệp vụ.

Theo dõi series nếu bạn muốn nhìn lỗi 500 này được bóc tách đến tận nguyên nhân. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER]+[TERM] | Tạo user, restart app, GET lại thành mảng rỗng | 35s |
| 2 | [DIAGRAM] | RAM process biến mất; PostgreSQL nằm ngoài process | 35s |
| 3 | [TERM] | Hiện `node -v`, `nest --version`, `npx prisma -v` | 35s |
| 4 | [TERM] | Cài Prisma packages và chạy `prisma init` | 45s |
| 5 | [IDE] | Viết model User, zoom UUID, unique email và timestamps | 55s |
| 6 | [TERM]+[IDE] | Chạy migration, mở file SQL vừa sinh | 55s |
| 7 | [IDE] | Gõ prompt; AI đề xuất inject Prisma thẳng vào service | 55s |
| 8 | [DIAGRAM] | UsersService → UsersRepository ← PrismaUsersRepository | 55s |
| 9 | [IDE] | Review contract, token và adapter trước khi approve | 60s |
| 10 | [IDE] | Agent implement DatabaseModule, PrismaService và adapter | 65s |
| 11 | [IDE] | Host tự gõ `findByEmail`; xem git diff | 50s |
| 12 | [TERM] | Build, start app, không có lỗi kết nối | 40s |
| 13 | [BROWSER] | POST, GET, restart, GET lại vẫn có dữ liệu | 55s |
| 14 | [BROWSER]+[TERM] | POST email trùng → 500 và log unique constraint | 35s |
| 15 | [B-ROLL] | Desk tối, freeze terminal đỏ, teaser EP04 | 20s |

**Tổng: 750 giây ≈ 12:30.** Dùng One Dark Pro, JetBrains Mono 18px, ẩn minimap và sidebar thừa.

### Command chuẩn bị

```bash
npm install @prisma/client @prisma/adapter-pg pg
npm install --save-dev prisma
npx prisma init --output ../src/generated/prisma
npx prisma migrate dev --name create_users
npm run build
npm run start:dev
```

### Schema cốt lõi

```prisma
generator client {
  provider     = "prisma-client"
  output       = "../src/generated/prisma"
  moduleFormat = "cjs"
}

datasource db {
  provider = "postgresql"
}

model User {
  id        String   @id @default(uuid())
  name      String
  email     String   @unique
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

### Boundary cần quay rõ

```typescript
export const USERS_REPOSITORY = Symbol('USERS_REPOSITORY');

export interface UsersRepository {
  create(data: { name: string; email: string }): Promise<User>;
  findAll(): Promise<User[]>;
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
}
```

```typescript
@Injectable()
export class UsersService {
  constructor(
    @Inject(USERS_REPOSITORY)
    private readonly usersRepository: UsersRepository,
  ) {}
}
```

### Prompt cho Opus

```text
Read the current NestJS project and plan replacing the in-memory Users store with PostgreSQL through Prisma.

Constraints:
- Keep prisma/schema.prisma and migrations at the project root.
- Put runtime integration under src/database.
- UsersService must depend on a UsersRepository contract, not PrismaService.
- PrismaUsersRepository implements that contract.
- Do not create Tasks, Roles or Permissions yet.
- Keep the existing DTO validation behavior.
- First show files, dependency direction, schema and verification commands.
- Do not edit until I approve.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese developer watching user records vanish from a dark NestJS terminal after restart, red empty database grid on one monitor and glowing PostgreSQL cylinder on another, neon cyan and green lighting, subject on the right, empty dark space on the left, 16:9, photorealistic developer documentary, no text, no logos, no watermark.`
2. `A cinematic close-up of glowing data flowing from a NestJS service through a repository boundary into PostgreSQL, dark IDE code reflected in eyeglasses, cyan arrows and neon green syntax, dramatic low-key lighting, clean left space for typography, 16:9, photorealistic, no text, no watermark.`
3. `A cinematic late-night coding scene with a green PostgreSQL database surviving while a red server process shuts down, dramatic monitor glow, rain and city bokeh, developer silhouette on the right, empty left side, 16:9, photorealistic, no text, no logos.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Kết nối NestJS với PostgreSQL bằng Prisma — EP03 | Lập trình là cuộc sống
2. Lưu User vào PostgreSQL với NestJS và Prisma — EP03 | Lập trình là cuộc sống
3. Tạo Repository Pattern với Prisma trong NestJS — EP03 | Lập trình là cuộc sống
4. Chuyển Users API từ RAM sang PostgreSQL — EP03 | Lập trình là cuộc sống
5. Migration Prisma đầu tiên trong NestJS — EP03 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho outcome và Title 3 cho architecture.

### 4b. SEO Description

```text
Restart NestJS một lần, toàn bộ user trong RAM biến mất. Ta sẽ đưa dữ liệu vào PostgreSQL mà không khóa UsersService vào Prisma.

✅ Cài Prisma và PostgreSQL driver theo phiên bản thực tế
✅ Tạo model User và migration đầu tiên
✅ Hiểu schema, migration và generated client
✅ Tách UsersRepository contract khỏi Prisma adapter
✅ Kiểm tra SQL thay vì tin ORM mù quáng
✅ Restart server và xác nhận dữ liệu còn nguyên
✅ Mở pain email trùng cho tập Error Handling

🔗 NestJS Database: https://docs.nestjs.com/techniques/database
🔗 Prisma + NestJS: https://www.prisma.io/docs/guides/frameworks/nestjs

⏱ 0:00 Restart và mất sạch user
⏱ 1:10 PostgreSQL nằm ngoài process
⏱ 2:20 Kiểm tra phiên bản và cài Prisma
⏱ 3:30 Model User và migration
⏱ 5:00 Repository boundary
⏱ 7:10 AI plan và review dependency
⏱ 9:10 Implement, build và kiểm tra SQL
⏱ 10:35 Restart vẫn còn dữ liệu
⏱ 11:45 Email trùng tạo lỗi 500

#NestJS #Prisma #PostgreSQL #RepositoryPattern #TypeScript #Backend #AICoding #Fresher #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs prisma, prisma postgresql nestjs, repository pattern nestjs, nestjs database, prisma migration, users repository, prisma service nestjs, postgresql tiếng việt, học nestjs, nestjs tập 3, nestjs architecture, dependency inversion typescript, prisma commonjs, backend fresher, typescript backend, ai coding mentor, opus antigravity, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `RESTART` — WHITE
- `DATA VẪN CÒN` — NEON GREEN `#00FF41`
- Hình: server đỏ tắt, database xanh vẫn sáng.

### Option 2
- `ĐỪNG INJECT` — WHITE
- `PRISMA TRỰC TIẾP` — NEON GREEN `#00FF41`
- Hình: service và Prisma bị chặn bởi repository boundary.

### Option 3
- `API MẤT TRÍ NHỚ` — WHITE
- `POSTGRES CỨU` — NEON GREEN `#00FF41`
- Hình: bảng user rỗng đối diện PostgreSQL sáng xanh.

**Typography chung:** Canvas 1280×720, Anton cho hook, JetBrains Mono cho `NESTJS #03`. Chữ bên trái, subject bên phải, stroke đen 8px và glow 10px. Typeset trong Canva; lưu thêm nền không chữ.
