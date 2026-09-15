# NestJS #03 — Kết nối PostgreSQL bằng Prisma 8

- **Series:** Học NestJS bằng AI — tập 3/46
- **Target runtime:** 12–14 phút
- **Outcome:** Dựng PostgreSQL local bằng Docker Compose; thay Users in-memory bằng PostgreSQL qua Prisma 8 và repository contract.
- **Technical baseline:** NestJS 12, Node.js 24.11+, TypeScript 5.9+, ESM, PostgreSQL, Prisma ORM 8.
- **Pain mở EP04:** Email trùng chạm unique constraint và biến thành lỗi 500 khó hiểu.
- **Source of truth:** [Prisma 8 với NestJS](https://www.prisma.io/docs/guides/frameworks/nestjs), [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status).

---

## PART 1 — SCRIPT

Một lần restart server, toàn bộ user vừa tạo biến mất.

API trả 201 rất đẹp. Nhưng trí nhớ của nó chỉ tồn tại cùng process Node.js.

Mảng trong UsersService nằm trong RAM. Process dừng, vùng nhớ được giải phóng, dữ liệu cũng đi theo.

Ta cần PostgreSQL. Nhưng thay database không có nghĩa UsersService phải biết mọi chi tiết của Prisma.

Bước ngoặt nằm ở một contract rất nhỏ.

UsersService chỉ biết nó cần lưu và tìm user. Prisma 8 đứng phía sau thực hiện những việc đó.

Repository giống quầy giao nhận. Nhân viên chỉ đưa yêu cầu, không cần biết kho vận hành bằng loại xe nào.

Trước tiên, mình cần một PostgreSQL chạy thật trên máy.

Không cài qua installer. Một file `docker-compose.postgres.yml` trong project là đủ.

Image `postgres:18-alpine` được khóa ngay trong file. Dữ liệu nằm trong Docker volume nên container tắt vẫn còn.

Một lệnh duy nhất: `docker compose -f docker-compose.postgres.yml up -d`.

Vài giây sau, healthcheck chuyển xanh. Port 5432 đã sẵn sàng trên máy.

Connection string ghi vào file `.env` với tên `DATABASE_URL`. File này không bao giờ lên git.

Server đã sống. Giờ mới đến lượt ORM.

Trước khi cài, mình kiểm tra Node, TypeScript, Nest và Prisma ngay trên màn hình.

Prisma 8 đang thay đổi nhanh. Video này không đoán phiên bản và cũng không âm thầm dùng latest.

Nếu bản stable đã phát hành, mình khóa đúng bản stable. Nếu chưa, mình khóa chính xác bản release candidate đã kiểm chứng.

Package lock được commit. Mọi tập sau dùng cùng baseline cho đến khi có một lần nâng cấp có chủ đích.

Prisma 8 không còn là Prisma Client quen thuộc trong nhiều tutorial cũ.

Không còn `schema.prisma`, `prisma generate` hay `prisma migrate dev` trong workflow mới.

Thay vào đó, mình khởi tạo Prisma 8 ngay trong Nest project đang có.

Project dùng ESM. Prisma tạo `contract.prisma`, `db.ts`, config và các file type được emit.

Contract là lời hứa giữa application và database.

Database schema là cấu trúc thật đang tồn tại trong PostgreSQL.

Hai khái niệm này gần nhau, nhưng không phải một.

Mình chỉ khai báo model User. ID là UUID, email unique, cùng thời điểm tạo và cập nhật. Với Prisma 8, timestamp cập nhật dùng `temporal.updatedAt()`.

Không có Role, Permission hay Task trong tập này. Một migration nhỏ luôn dễ review hơn một migration chứa cả tương lai.

Sau khi sửa contract, mình chạy `prisma contract emit`.

Lệnh này tạo `contract.json` cho runtime và `contract.d.ts` cho TypeScript.

Hai file đó được commit. Prisma 8 không cần generate client package trong lúc build hoặc deploy.

Tiếp theo, mình yêu cầu Prisma lập kế hoạch migration tên `create_users`.

Plan chỉ tạo file. Nó chưa chạm vào database.

Đây là khoảng dừng quan trọng cho con người.

Mình đọc `migration.ts`, `ops.json` và DDL preview trước khi apply.

Primary key có đúng UUID không. Unique constraint có nằm trên email không. Timestamp có đúng kiểu không.

ORM giúp ta viết query nhanh hơn. Nó không thay trách nhiệm hiểu database sắp thay đổi thế nào.

Giờ mình mở agent panel. AI chỉ được lên plan, chưa được sửa code.

Nó trả về một đoạn quen thuộc: tạo PrismaClient rồi inject thẳng vào UsersService.

Code đó có thể đúng với Prisma cũ. Nhưng trong project này, nó sai cả phiên bản lẫn boundary.

Mình yêu cầu AI đọc release status, Prisma 8 skill và contract vừa emit.

Plan mới có ba phần.

UsersRepository là contract. PrismaUsersRepository là adapter. Prisma database facade đi vào adapter qua DI token.

Contract chỉ có `create`, `findAll`, `findById` và `findByEmail`.

Nó diễn tả nhu cầu của Users. Nó không sao chép toàn bộ query API của Prisma.

Nếu repository lộ mọi filter và option của ORM, ta chỉ đổi tên dependency chứ chưa tạo boundary.

Sau khi approve, agent tạo DatabaseModule, Prisma provider và adapter.

Provider giữ một database facade dùng chung. Khi application shutdown, pool mới được đóng.

Không mở rồi đóng kết nối trong từng request. Làm vậy chỉ biến connection pool thành máy chạy bộ.

Trong adapter, câu lệnh tạo user bắt đầu bằng `db.orm.public.User.create`.

Prisma 8 không còn object `data` bọc bên ngoài như Prisma 7.

Tìm user dùng `.where(...).first()`. Lấy danh sách dùng `.all()`.

Trong UsersModule, token `USERS_REPOSITORY` nối contract với PrismaUsersRepository.

Nest container sẽ đưa adapter vào UsersService lúc runtime.

Mình mở git diff.

`db.orm` chỉ xuất hiện trong database adapter. Nó không xuất hiện trong UsersService hay controller.

Đây là bằng chứng cho dependency direction, không phải một sơ đồ đẹp để ngắm.

Mình chạy migration check, rồi apply migration vào PostgreSQL với `--advance-ref db` để lần plan tiếp theo bắt đầu từ đúng trạng thái vừa áp dụng.

Cuối cùng, `prisma db verify` xác nhận database thật đang khớp với contract đã emit.

Ứng dụng khởi động. Mình POST một user, GET danh sách, rồi dừng server.

Khoảnh khắc kiểm chứng thật sự đến sau khi server chạy lại.

GET `/users` vẫn trả đúng user vừa tạo.

RAM đã quên. PostgreSQL thì chưa.

Nhưng mình gửi lại đúng email đó.

PostgreSQL từ chối unique constraint. Prisma 8 trả một structured error, còn client nhận lỗi 500 lạnh lùng.

Database đang bảo vệ dữ liệu đúng. API chỉ chưa biết kể lỗi đó bằng ngôn ngữ của người gọi.

Tập sau, mình sẽ map lỗi kỹ thuật thành 400, 404 hoặc 409 rõ ràng.

Một boundary tốt không làm database biến mất. Nó chỉ ngăn quyết định hạ tầng lan vào nơi chứa nghiệp vụ.

Theo dõi series nếu bạn muốn nhìn lỗi 500 này được bóc tách đến tận nguyên nhân. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER]+[TERM] | Tạo user, restart Nest app, GET lại thành mảng rỗng | 35s |
| 2 | [DIAGRAM] | RAM nằm trong Node process; PostgreSQL nằm ngoài process | 35s |
| 3 | [TERM]+[IDE] | Tạo `docker-compose.postgres.yml`; `up -d`; đợi healthcheck xanh; `psql` ping được | 60s |
| 4 | [TERM] | Hiện Node, TypeScript, Nest, Prisma dist-tags và package tree | 50s |
| 5 | [BROWSER] | Mở Prisma 8 release status; highlight runtime và feature limitations | 40s |
| 6 | [TERM] | Pin exact Prisma 8 CLI/runtime; chạy `prisma orm init` trong Nest project | 65s |
| 7 | [IDE] | Review `contract.prisma`, `db.ts`, `prisma.config.ts` và package scripts | 55s |
| 8 | [IDE] | Viết model User; zoom UUID, unique email và timestamps | 50s |
| 9 | [TERM]+[IDE] | `contract emit`; mở `contract.json` và `contract.d.ts` | 45s |
| 10 | [TERM]+[IDE] | `migration plan`; review `migration.ts`, `ops.json`, DDL preview | 70s |
| 11 | [IDE] | Gõ Prompt 1 (ngây thơ); AI đề xuất PrismaClient và inject thẳng vào service | 45s |
| 12 | [DIAGRAM] | UsersService → UsersRepository ← PrismaUsersRepository → Prisma 8 db | 45s |
| 13 | [IDE] | Host bắt lỗi xong gõ Prompt 2 (đã dẫn nguồn); review contract, DI tokens và lifecycle provider trước khi approve | 70s |
| 14 | [IDE] | Agent implement adapter bằng `db.orm.public.User` | 70s |
| 15 | [IDE] | Host tự gõ `findByEmail`; kiểm tra git diff và import boundary | 55s |
| 16 | [TERM] | `migration check`, `db migrate --advance-ref db`, `db verify`, build và test | 65s |
| 17 | [BROWSER] | POST, GET, restart app, GET lại vẫn có dữ liệu | 60s |
| 18 | [BROWSER]+[TERM] | POST email trùng → 500 và Prisma 8 structured error | 40s |
| 19 | [B-ROLL] | Desk tối, freeze error code, teaser EP04 | 20s |

**Tổng: 980 giây ≈ 16:20.** Khi dựng, cắt các khoảng chờ cài package, pull image và migrate để đưa bản cuối về 12–14 phút.

Dùng One Dark Pro, JetBrains Mono tối thiểu 18px cho video ngang. Khi quay lại cảnh dọc cho Shorts, tăng lên 24px và giữ code trong safe zone giữa màn hình.

### Cổng kiểm tra phiên bản trước khi quay

```bash
node --version
npx tsc --version
nest --version
npm view prisma dist-tags
npm view @prisma/orm-postgres dist-tags
npm ls prisma @prisma/orm-postgres @prisma/client
docker --version
docker compose version
```

Điều kiện pass:

- Node.js `24.11+`.
- TypeScript `5.9+`.
- `package.json` có `"type": "module"`.
- Không có `@prisma/client`.
- Docker Engine + Compose v2 chạy được; port 5432 trên máy còn trống (`docker ps`, `ss -ltn | grep 5432`).
- CLI và PostgreSQL runtime được pin exact trong lockfile.
- Release status xác nhận các API dùng trong tập đã tồn tại.

### Command chuẩn bị

**Bước 0 — PostgreSQL local bằng Docker.** Tạo `docker-compose.postgres.yml` ở project root (file này tách riêng khỏi compose deploy của EP17 — nó chỉ phục vụ dev):

```yaml
services:
  postgres:
    image: postgres:18-alpine
    container_name: nestjs-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: nestjs
      POSTGRES_PASSWORD: nestjs
      POSTGRES_DB: nestjs_dev
    ports:
      - "5432:5432"
    volumes:
      - nestjs_pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U nestjs -d nestjs_dev"]
      interval: 5s
      timeout: 3s
      retries: 10

volumes:
  nestjs_pgdata:
```

Chạy và kiểm tra:

```bash
docker compose -f docker-compose.postgres.yml up -d
docker compose -f docker-compose.postgres.yml ps        # STATUS phải "healthy"
docker compose -f docker-compose.postgres.yml logs postgres | tail -5
docker exec -it nestjs-postgres psql -U nestjs -d nestjs_dev -c "SELECT version();"
# Hạ database khi cần: docker compose -f docker-compose.postgres.yml down
# Xóa sạch dữ liệu dev:  docker compose -f docker-compose.postgres.yml down -v
```

`.env` (đã có trong `.gitignore`; nếu chưa thì thêm ngay):

```text
DATABASE_URL="postgresql://nestjs:nestjs@localhost:5432/nestjs_dev"
```

**Bước 1 — Prisma 8.** Trong ngày quay, thay hai placeholder bằng exact versions hiển thị trên release status. Không giả định số RC của CLI và runtime giống nhau.

```bash
npx prisma@<PRISMA_CLI_VERSION> orm init --yes --target postgres --authoring psl
npm install --save-dev --save-exact prisma@<PRISMA_CLI_VERSION>
npm install --save-exact @prisma/orm-postgres@<POSTGRES_RUNTIME_VERSION>
npm install --save-exact temporal-polyfill
npx prisma skills sync
```

Sau khi điền `DATABASE_URL` và model User:

```bash
npx prisma contract emit
npx prisma migration plan --name create_users
npx prisma migration check
npx prisma db migrate --advance-ref db
npx prisma db verify
npm run build
npm run test
npm run start:dev
```

### Cấu trúc file sau EP03

```text
src/
├── prisma/
│   ├── contract.prisma
│   ├── contract.json
│   ├── contract.d.ts
│   └── db.ts
├── database/
│   ├── database.module.ts
│   ├── prisma.provider.ts
│   └── repositories/
│       └── prisma-users.repository.ts
└── modules/
    └── users/
        ├── domain/
        │   └── user.ts
        ├── repositories/
        │   └── users.repository.ts
        ├── users.controller.ts
        ├── users.module.ts
        └── users.service.ts
migrations/
└── app/
prisma.config.ts
docker-compose.postgres.yml
.env          # gitignored — DATABASE_URL
```

### Prisma 8 contract cốt lõi

`orm init` có thể đặt contract ở `src/prisma/contract.prisma`. Giữ nguyên đường dẫn mà config vừa sinh ra.

```prisma
types {
  Uuid = String @db.Uuid
}

model User {
  id        Uuid     @id @default(uuid())
  name      String
  email     String   @unique
  createdAt DateTime @default(now())
  updatedAt temporal.updatedAt()

  @@map("users")
}
```

Sau mỗi lần sửa contract, chạy `npx prisma contract emit` và review diff của cả `contract.json` lẫn `contract.d.ts`.

### Domain type và repository contract

```typescript
export type User = {
  id: string;
  name: string;
  email: string;
  createdAt: Temporal.Instant;
  updatedAt: Temporal.Instant;
};

export type CreateUserData = Pick<User, 'name' | 'email'>;
```

```typescript
export const USERS_REPOSITORY = Symbol('USERS_REPOSITORY');

export interface UsersRepository {
  create(data: CreateUserData): Promise<User>;
  findAll(): Promise<User[]>;
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
}
```

### Prisma provider và lifecycle

`src/prisma/db.ts` do Prisma 8 scaffold tạo. Vì baseline dùng Node 24, thêm polyfill theo hướng dẫn Prisma 8 ở đầu file này:

```typescript
import 'temporal-polyfill/full/global';
```

Nest chỉ bọc database facade bằng explicit token.

```typescript
import {
  Inject,
  Injectable,
  Module,
  OnApplicationShutdown,
} from '@nestjs/common';
import { db } from '../prisma/db.js';

export const PRISMA_DB = Symbol('PRISMA_DB');
export type PrismaDb = typeof db;

@Injectable()
class PrismaShutdown implements OnApplicationShutdown {
  constructor(@Inject(PRISMA_DB) private readonly database: PrismaDb) {}

  async onApplicationShutdown(): Promise<void> {
    await this.database.close();
  }
}

@Module({
  providers: [
    { provide: PRISMA_DB, useValue: db },
    PrismaShutdown,
  ],
  exports: [PRISMA_DB],
})
export class DatabaseModule {}
```

Trong `main.ts`, bật shutdown hooks để SIGTERM đi qua lifecycle của Nest:

```typescript
app.enableShutdownHooks();
```

### Prisma 8 adapter

```typescript
@Injectable()
export class PrismaUsersRepository implements UsersRepository {
  constructor(@Inject(PRISMA_DB) private readonly db: PrismaDb) {}

  create(data: CreateUserData): Promise<User> {
    return this.db.orm.public.User.create(data);
  }

  findAll(): Promise<User[]> {
    return this.db.orm.public.User
      .orderBy((user) => user.createdAt.asc())
      .all();
  }

  findById(id: string): Promise<User | null> {
    return this.db.orm.public.User.where({ id }).first();
  }

  findByEmail(email: string): Promise<User | null> {
    return this.db.orm.public.User.where({ email }).first();
  }
}
```

### UsersService không biết Prisma

```typescript
@Injectable()
export class UsersService {
  constructor(
    @Inject(USERS_REPOSITORY)
    private readonly usersRepository: UsersRepository,
  ) {}
}
```

### Provider binding trong UsersModule

```typescript
@Module({
  imports: [DatabaseModule],
  controllers: [UsersController],
  providers: [
    UsersService,
    PrismaUsersRepository,
    {
      provide: USERS_REPOSITORY,
      useExisting: PrismaUsersRepository,
    },
  ],
})
export class UsersModule {}
```

### Prompts cho Opus (2 bước)

Tập này cần HAI prompt — đó là chính cốt chuyện: prompt ngây thơ khiến AI rơi vào snippet Prisma 7, rồi prompt sửa lại sau khi host bắt lỗi.

**Prompt 1 — câu hỏi ngây thơ (cảnh 11).** Gõ nguyên văn, không thêm context phiên bản. AI sẽ trả plan kiểu Prisma 7: `PrismaClient`, `schema.prisma`, `prisma generate`, `migrate dev`, inject thẳng vào UsersService. Đó chính là chất liệu để host bắt lỗi.

```text
Read this NestJS project. Replace the in-memory Users store with PostgreSQL using Prisma.
Keep the current UsersService and controller behavior.
Show a plan first, do not edit any file until I approve.
```

**Prompt 2 — sau khi host bắt lỗi (đối chiếu release status + skill + contract vừa emit).**

```text
Read the current NestJS 12 ESM project and the installed Prisma 8 skill.
Plan replacing the in-memory Users store with PostgreSQL through Prisma ORM 8.

Constraints:
- Verify the installed Prisma CLI and @prisma/orm-postgres versions first.
- Use only Prisma 8 APIs and the current Prisma 8 release-status page.
- Keep the PSL source and emitted artifacts under src/prisma as scaffolded.
- Commit contract.json, contract.d.ts and migrations/app.
- Put Nest integration and adapters under src/database.
- UsersService must depend on a UsersRepository contract.
- PrismaUsersRepository receives the Prisma 8 db facade through an explicit DI token.
- Use db.orm.public.User, not PrismaClient or @prisma/client.
- Use contract emit, migration plan, migration check, db migrate --advance-ref db and db verify.
- Do not use schema.prisma, prisma generate, migrate dev, migrate deploy, P2002 or $transaction.
- Do not create Tasks, Roles or Permissions yet.
- Keep the existing DTO validation behavior.
- First show the file plan, dependency direction, contract, migration workflow and verification commands.
- Do not edit until I approve.
```

### Checklist review trước khi approve

- [ ] AI đã đọc Prisma 8 skill đúng version đang cài.
- [ ] Không có import từ `@prisma/client`.
- [ ] Không có `PrismaClient` hoặc query Prisma 7.
- [ ] UsersService chỉ import repository contract.
- [ ] Adapter là nơi duy nhất gọi `db.orm`.
- [ ] Migration plan chưa apply trước khi host review.
- [ ] `contract.json`, `contract.d.ts`, migration package và lockfile xuất hiện trong diff.
- [ ] Node 24 đã nạp `temporal-polyfill/full/global`; timestamp trong code là `Temporal.Instant`.
- [ ] Database URL không xuất hiện trong diff hoặc log công khai.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

Ba prompt tuân theo visual preset của series: NestJS red `#E0234E`, trắng, đen/navy; headline đặt riêng trong Canva.

1. `A cinematic photograph of a Vietnamese male developer on the right side watching user records disappear after a server restart, a dark code monitor behind him and a glowing PostgreSQL database cylinder remaining intact, dramatic deep black and navy environment, strong NestJS red-pink #E0234E rim light, white highlights, empty dark space on the left for bold typography, high contrast, photorealistic high-end developer documentary, 16:9, no text, no watermark.`
2. `A cinematic photograph of a Vietnamese male developer on the right reviewing a clean architecture flow from a NestJS service through a repository boundary into PostgreSQL, dark IDE monitor as a secondary element, dramatic NestJS red-pink #E0234E and white lighting over deep black navy, empty left side for headline, high contrast, photorealistic tech commercial, 16:9, no text, no watermark.`
3. `A cinematic close-up of a dark monitor showing a Prisma 8 contract and migration plan while a Vietnamese developer studies the diff from the right side of frame, deep black and navy background, bold NestJS red-pink #E0234E accent lighting, crisp white details, minimal desk elements, empty dark left area for typography, photorealistic, 16:9, no text, no watermark.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Kết nối NestJS với PostgreSQL bằng Prisma 8 — EP03 | Lập trình là cuộc sống
2. Prisma 8 ĐÃ KHÁC: Lưu User từ NestJS vào PostgreSQL — EP03
3. Repository Pattern với Prisma 8 trong NestJS — EP03
4. Từ RAM đến PostgreSQL: NestJS + Prisma 8 — EP03
5. Contract và Migration đầu tiên với Prisma 8 — EP03

**Khuyên dùng:** Title 1 cho search intent. A/B Title 2 cho curiosity và Title 3 cho architecture intent.

### 4b. SEO Description

```text
Restart NestJS một lần, toàn bộ user trong RAM biến mất. Ta sẽ đưa dữ liệu vào PostgreSQL bằng Prisma 8 mà không khóa UsersService vào ORM.

✅ Dựng PostgreSQL local bằng Docker Compose (không cài installer)
✅ Kiểm tra và khóa chính xác phiên bản Prisma 8
✅ Hiểu contract khác database schema thế nào
✅ Emit contract.json và contract.d.ts
✅ Plan, review, apply và verify migration
✅ Dùng db.orm.public.User thay cho Prisma Client cũ
✅ Tách UsersRepository contract khỏi Prisma adapter
✅ Restart server và xác nhận dữ liệu còn nguyên
✅ Mở pain unique constraint cho tập Error Handling

🔗 Prisma 8 + NestJS: https://www.prisma.io/docs/guides/frameworks/nestjs
🔗 Prisma 8 Release Status: https://www.prisma.io/docs/prisma-orm/release-status
🔗 Prisma 8 Data Contract: https://www.prisma.io/docs/orm/contract-authoring/the-data-contract
🔗 Prisma 8 Migrations: https://www.prisma.io/docs/orm/migrations/how-migrations-work
🔗 Prisma 8 Writing Data: https://www.prisma.io/docs/orm/fundamentals/writing-data

⏱ 0:00 Restart và mất sạch user
⏱ 1:10 PostgreSQL nằm ngoài process
⏱ 2:10 Dựng PostgreSQL local bằng Docker
⏱ 3:20 Khóa phiên bản Prisma 8
⏱ 4:30 Contract thay cho schema.prisma
⏱ 5:50 Emit và review migration plan
⏱ 7:25 AI dùng nhầm Prisma 7
⏱ 8:40 Repository boundary và DI token
⏱ 10:40 Query bằng db.orm.public.User
⏱ 12:10 Migrate, verify và restart
⏱ 13:40 Email trùng tạo lỗi 500

#NestJS #Prisma8 #PostgreSQL #RepositoryPattern #TypeScript #Backend #AICoding #Fresher #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs prisma 8, prisma 8 nestjs, prisma 8 postgresql, prisma contract, prisma 8 migration, db orm public user, repository pattern nestjs, nestjs database, prisma 8 tiếng việt, contract prisma, prisma migration plan, prisma db migrate, prisma db verify, users repository, postgresql tiếng việt, học nestjs, nestjs tập 3, nestjs architecture, dependency inversion typescript, esm nestjs, backend fresher, typescript backend, ai coding mentor, opus antigravity, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

Mọi option dùng ảnh tham chiếu `../01-hoc-nestjs-voi-ai/thumbnail-01-hoc-nestjs-cung-ai.png`: headline trái, host phải, monitor code là lớp phụ.

### Option 1 — khuyên dùng

- `NESTJS` — WHITE
- `KẾT NỐI DB` — NEST RED `#E0234E`
- Badge nhỏ: `EP03`
- Hình: host nhìn màn hình; monitor thể hiện NestJS kết nối PostgreSQL.

### Option 2

- `RESTART` — WHITE
- `DATA VẪN CÒN` — NEST RED `#E0234E`
- Badge nhỏ: `POSTGRES`
- Hình: server tắt, database vẫn sáng.

### Option 3

- `ĐỪNG INJECT` — WHITE
- `ORM TRỰC TIẾP` — NEST RED `#E0234E`
- Badge nhỏ: `BOUNDARY`
- Hình: sơ đồ service → repository → Prisma 8 trên monitor.

**Typography:** Canvas 1280×720. Anton hoặc Impact cho headline, JetBrains Mono cho badge. Stroke đen dày, shadow gọn, không dùng neon xanh/cyan. Kiểm tra full-size và preview 320×180; dấu tiếng Việt phải rõ.

---

## PART 6 — SOURCE / CLAIM MAP

| Claim trong video | Nguồn bắt buộc |
|---|---|
| Dựng PostgreSQL dev bằng Docker Compose tách riêng; healthcheck `pg_isready` | [Prisma 8 in Docker](https://www.prisma.io/docs/guides/deployment/docker) |
| Prisma 8 dùng được với NestJS; model access là `db.orm.public.User` | [Prisma 8 with NestJS](https://www.prisma.io/docs/guides/frameworks/nestjs) |
| Runtime tối thiểu, trạng thái RC/GA và feature chưa hỗ trợ | [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status) |
| `schema.prisma` → `contract.prisma`; `generate` → `contract emit`; migration command mới | [Coming from Prisma ORM 7](https://www.prisma.io/docs/orm/coming-from-prisma-orm-7) |
| Ý nghĩa contract, emitted JSON/types và database schema | [The Prisma 8 data contract](https://www.prisma.io/docs/orm/contract-authoring/the-data-contract), [contract artifacts](https://www.prisma.io/docs/orm/contract-authoring/the-contract-artifact) |
| Cú pháp PSL cho UUID, unique, default, `temporal.updatedAt()` và mapping table | [Prisma 8 PSL syntax](https://www.prisma.io/docs/orm/contract-authoring/psl-syntax), [Coming from Prisma ORM 7](https://www.prisma.io/docs/orm/coming-from-prisma-orm-7) |
| `.create`, `.where`, `.first`, `.all`, không có wrapper `data` | [Writing data](https://www.prisma.io/docs/orm/fundamentals/writing-data), [Reading data](https://www.prisma.io/docs/orm/fundamentals/reading-data) |
| Plan → review → `db migrate --advance-ref db` → `db verify` | [How migrations work](https://www.prisma.io/docs/orm/migrations/how-migrations-work), [Applying a migration](https://www.prisma.io/docs/orm/migrations/applying-a-migration) |
| Node 24 cần Temporal polyfill; `DateTime` trả về `Temporal.Instant` | [Coming from Prisma ORM 7](https://www.prisma.io/docs/orm/coming-from-prisma-orm-7) |
| Một database facade dùng lâu dài và chỉ close khi shutdown | [Transactions and runtime reference](https://www.prisma.io/docs/orm/reference/transactions-and-runtime) |
| Prisma 8 structured error thay cho `P2002`/`instanceof` cũ | [Prisma 8 error reference](https://www.prisma.io/docs/orm/reference/error-reference) |
| Nest provider, custom token và lifecycle hooks | [NestJS Custom Providers](https://docs.nestjs.com/fundamentals/custom-providers), [Lifecycle events](https://docs.nestjs.com/fundamentals/lifecycle-events) |

Trước ngày quay, mở lại toàn bộ link Prisma 8 trong bảng, ghi ngày kiểm tra vào production note và chạy code demo end-to-end. Nếu docs và script khác nhau, docs của exact package version đang khóa được ưu tiên; script phải sửa trước khi quay.
