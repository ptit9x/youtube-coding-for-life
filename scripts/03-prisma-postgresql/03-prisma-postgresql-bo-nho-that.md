# NestJS #03 — Kết nối PostgreSQL bằng Prisma 8

- **Series:** Học NestJS bằng AI — tập 3/45
- **Target runtime:** 14–16 phút
- **Outcome:** Dựng PostgreSQL local không hardcode Compose config; cấu hình ENV có validation; thay Users in-memory bằng PostgreSQL qua Prisma 8 và repository contract.
- **Technical baseline:** NestJS 12, Node.js 24.11+, TypeScript 5.9+, ESM, PostgreSQL, Prisma ORM 8.
- **Pain mở EP04:** Email trùng chạm unique constraint và biến thành lỗi 500 khó hiểu.
- **Source of truth:** [Prisma 8 với NestJS](https://www.prisma.io/docs/guides/frameworks/nestjs), [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status), [NestJS Configuration](https://docs.nestjs.com/techniques/configuration), [Docker Compose interpolation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/).

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

Image `postgres:18-alpine` được pin qua `POSTGRES_IMAGE`. Compose từ chối chạy nếu biến bắt buộc bị thiếu.

Dữ liệu nằm trong Docker volume nên container tắt vẫn còn.

Một lệnh duy nhất: `docker compose -f docker-compose.postgres.yml up -d`.

Vài giây sau, healthcheck chuyển xanh. Host port trong `POSTGRES_PORT` đã sẵn sàng trên máy.

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

Lúc này có một chi tiết dễ bỏ qua. Tạo `.env` chưa có nghĩa mọi process sẽ tự đọc nó.

Prisma CLI và Nest runtime dùng chung một giá trị, nhưng mỗi bên phải nạp nó rõ ràng.

Mình yêu cầu AI audit toàn bộ config trước khi sửa. Nó tìm cả giá trị đang hardcode trong Docker Compose.

Mình review danh sách biến, cách validate và `.env.example`, rồi mới approve.

Image PostgreSQL, user, password, database và host port được chuyển thành biến bắt buộc trong `.env`.

Compose dùng chúng để nội suy file YAML. Nest không validate các biến chỉ dành cho Compose.

`prisma.config.ts` nạp `.env` cho command Prisma. Nest dùng `ConfigModule` làm boundary của application.

Mình thêm `.env.example` chỉ chứa giá trị mẫu, rồi kiểm tra `.env` đã nằm trong `.gitignore`.

Trong `AppModule`, ConfigModule ép kiểu port và validate `DATABASE_URL` ngay khi startup.

Mình cố tình xóa biến đó. App dừng trước request đầu tiên và chỉ đúng field đang thiếu.

Không có fallback database URL bí mật. Config bắt buộc phải fail fast.

`src/prisma/db.ts` được đổi từ singleton đọc `process.env` thành factory nhận URL đã validate.

Database provider gọi factory qua DI. UsersService không biết `.env`, `ConfigService` hay connection string tồn tại.

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

Quay lại agent panel, mình đưa yêu cầu tích hợp Prisma. AI vẫn chỉ được lên plan, chưa được sửa code.

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
| 1 | [BROWSER]+[TERM] | Tạo user, restart Nest app, GET lại thành mảng rỗng | 30s |
| 2 | [DIAGRAM] | RAM nằm trong Node process; PostgreSQL nằm ngoài process | 25s |
| 3 | [TERM]+[IDE] | Tạo `docker-compose.postgres.yml`; `up -d`; đợi healthcheck xanh; `psql` ping được | 50s |
| 4 | [TERM] | Hiện Node, TypeScript, Nest, Prisma dist-tags và package tree | 40s |
| 5 | [BROWSER] | Mở Prisma 8 release status; highlight runtime và feature limitations | 30s |
| 6 | [TERM] | Pin exact Prisma 8 CLI/runtime; chạy `prisma orm init` trong Nest project | 50s |
| 7 | [IDE] | Review `contract.prisma`, `db.ts`, `prisma.config.ts` và package scripts | 40s |
| 8 | [AI]+[IDE]+[TERM] | Gõ Prompt 1 audit ENV; chuyển giá trị Compose sang biến bắt buộc; thêm ConfigModule, Zod và `.env.example` | 70s |
| 9 | [IDE] | Đổi `db.ts` thành factory nhận URL đã validate; review DI boundary | 40s |
| 10 | [IDE] | Viết model User; zoom UUID, unique email và timestamps | 40s |
| 11 | [TERM]+[IDE] | `contract emit`; mở `contract.json` và `contract.d.ts` | 35s |
| 12 | [TERM]+[IDE] | `migration plan`; review `migration.ts`, `ops.json`, DDL preview | 60s |
| 13 | [IDE] | Gõ Prompt 2 (ngây thơ); AI đề xuất PrismaClient và inject thẳng vào service | 35s |
| 14 | [DIAGRAM] | UsersService → UsersRepository ← PrismaUsersRepository → Prisma 8 db | 40s |
| 15 | [IDE] | Host bắt lỗi xong gõ Prompt 3; review config, contract, DI tokens và lifecycle provider trước khi approve | 60s |
| 16 | [IDE] | Agent implement adapter bằng `db.orm.public.User` | 55s |
| 17 | [IDE] | Host tự gõ `findByEmail`; kiểm tra git diff và import boundary | 40s |
| 18 | [TERM] | `migration check`, `db migrate --advance-ref db`, `db verify`, build và test | 55s |
| 19 | [BROWSER] | POST, GET, restart app, GET lại vẫn có dữ liệu | 50s |
| 20 | [BROWSER]+[TERM] | POST email trùng → 500 và Prisma 8 structured error | 35s |
| 21 | [B-ROLL] | Desk tối, freeze error code, teaser EP04 | 15s |

**Tổng: 895 giây ≈ 14:55.** Cắt toàn bộ thời gian chờ cài package, pull image và migrate.

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
- Docker Engine + Compose v2 chạy được; host port trong `POSTGRES_PORT` còn trống.
- CLI và PostgreSQL runtime được pin exact trong lockfile.
- Release status xác nhận các API dùng trong tập đã tồn tại.

### Command chuẩn bị

**Bước 0 — PostgreSQL local bằng Docker.** Tạo `docker-compose.postgres.yml` ở project root (file này tách riêng khỏi compose deploy của EP16 — nó chỉ phục vụ dev):

```yaml
services:
  postgres:
    image: "${POSTGRES_IMAGE:?POSTGRES_IMAGE is required}"
    restart: unless-stopped
    environment:
      POSTGRES_USER: "${POSTGRES_USER:?POSTGRES_USER is required}"
      POSTGRES_PASSWORD: "${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}"
      POSTGRES_DB: "${POSTGRES_DB:?POSTGRES_DB is required}"
    ports:
      - "${POSTGRES_PORT:?POSTGRES_PORT is required}:5432"
    volumes:
      - nestjs_pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}"]
      interval: 5s
      timeout: 3s
      retries: 10

volumes:
  nestjs_pgdata:
```

Chạy và kiểm tra:

```bash
docker compose -f docker-compose.postgres.yml config --quiet
docker compose -f docker-compose.postgres.yml up -d
docker compose -f docker-compose.postgres.yml ps        # STATUS phải "healthy"
docker compose -f docker-compose.postgres.yml logs postgres | tail -5
docker compose -f docker-compose.postgres.yml exec postgres sh -lc 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT version();"'
# Hạ database khi cần: docker compose -f docker-compose.postgres.yml down
# Xóa sạch dữ liệu dev:  docker compose -f docker-compose.postgres.yml down -v
```

`.env` thật nằm trong `.gitignore`:

```text
POSTGRES_IMAGE="postgres:18-alpine"
POSTGRES_USER="nestjs"
POSTGRES_PASSWORD="nestjs"
POSTGRES_DB="nestjs_dev"
POSTGRES_PORT=5432
DATABASE_URL="postgresql://nestjs:nestjs@localhost:5432/nestjs_dev"
PORT=3000
NODE_ENV="development"
```

`.env.example` được commit, nhưng chỉ chứa placeholder:

```text
POSTGRES_IMAGE="postgres:18-alpine"
POSTGRES_USER="YOUR_LOCAL_USER"
POSTGRES_PASSWORD="CHANGE_ME_LOCAL_ONLY"
POSTGRES_DB="YOUR_LOCAL_DATABASE"
POSTGRES_PORT=5432
DATABASE_URL="postgresql://YOUR_LOCAL_USER:CHANGE_ME_LOCAL_ONLY@localhost:5432/YOUR_LOCAL_DATABASE"
PORT=3000
NODE_ENV=development
```

`DATABASE_URL` được ghi tường minh vì Prisma CLI và Nest cùng cần URL hoàn chỉnh. Không dựa vào nested interpolation mà `dotenv` và Compose có thể xử lý khác nhau; khi đổi credential hoặc port local, phải cập nhật URL cùng lúc.

**Bước 1 — Prisma 8.** Trong ngày quay, thay hai placeholder bằng exact versions hiển thị trên release status. Không giả định số RC của CLI và runtime giống nhau.

```bash
npx prisma@<PRISMA_CLI_VERSION> orm init --yes --target postgres --authoring psl
npm install --save-dev --save-exact prisma@<PRISMA_CLI_VERSION>
npm install --save-exact @prisma/orm-postgres@<POSTGRES_RUNTIME_VERSION>
npm install --save-exact temporal-polyfill
npm install --save-exact @nestjs/config zod
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
├── config/
│   ├── app.config.ts
│   ├── database.config.ts
│   └── env.validation.ts
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
.env          # gitignored — local config và secret
.env.example  # committed — chỉ có placeholder
```

### Một `.env`, hai consumer rõ ràng

`prisma.config.ts` phục vụ Prisma CLI nên giữ `import 'dotenv/config'`. Nest runtime không import file CLI này; nó nạp cùng `.env` qua `ConfigModule`.

```typescript
// src/config/env.validation.ts
import { z } from 'zod';

export const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().int().min(1).max(65535).default(3000),
  DATABASE_URL: z.string().url(),
});

export type Env = z.infer<typeof envSchema>;
```

```typescript
// src/config/app.config.ts
import { registerAs } from '@nestjs/config';

export default registerAs('app', () => ({
  port: Number(process.env.PORT ?? 3000),
}));
```

```typescript
// src/config/database.config.ts
import { registerAs } from '@nestjs/config';

export default registerAs('database', () => ({
  url: process.env.DATABASE_URL!,
}));
```

```typescript
// app.module.ts
ConfigModule.forRoot({
  isGlobal: true,
  cache: true,
  load: [appConfig, databaseConfig],
  validationSchema: envSchema,
});
```

`main.ts` cũng lấy port từ config đã parse, không đọc lại `process.env`:

```typescript
import type { ConfigType } from '@nestjs/config';
import appConfig from './config/app.config.js';

const config = app.get<ConfigType<typeof appConfig>>(appConfig.KEY);
await app.listen(config.port);
```

Chỉ `src/config` và `prisma.config.ts` được chạm môi trường thô. Controller, service, repository adapter và Prisma runtime nhận dependency đã cấu hình.

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

`src/prisma/db.ts` do Prisma 8 scaffold tạo. Vì baseline dùng Node 24, thêm polyfill rồi đổi singleton thành factory nhận URL đã validate:

```typescript
import 'temporal-polyfill/full/global';
import postgres from '@prisma/orm-postgres/runtime';
import type { Contract } from './contract.d';
import contractJson from './contract.json' with { type: 'json' };

export const createDb = (url: string) =>
  postgres<Contract>({ contractJson, url });
```

Nest tạo database facade qua DI. `ConfigModule` validate trước; provider chỉ nhận giá trị bắt buộc.

```typescript
import {
  Inject,
  Injectable,
  Module,
  OnApplicationShutdown,
} from '@nestjs/common';
import type { ConfigType } from '@nestjs/config';
import databaseConfig from '../config/database.config.js';
import { createDb } from '../prisma/db.js';

export const PRISMA_DB = Symbol('PRISMA_DB');
export type PrismaDb = ReturnType<typeof createDb>;

@Injectable()
class PrismaShutdown implements OnApplicationShutdown {
  constructor(@Inject(PRISMA_DB) private readonly database: PrismaDb) {}

  async onApplicationShutdown(): Promise<void> {
    await this.database.close();
  }
}

@Module({
  providers: [
    {
      provide: PRISMA_DB,
      inject: [databaseConfig.KEY],
      useFactory: (config: ConfigType<typeof databaseConfig>) =>
        createDb(config.url),
    },
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

### Prompts cho Opus (3 bước)

Ba prompt vẫn nằm trong một sequence liên tục: chuẩn hóa ENV trước, đưa yêu cầu Prisma ngây thơ để lộ snippet cũ, rồi sửa plan trước khi approve.

**Prompt 1 — chuẩn hóa ENV và Docker Compose (cảnh 8).**

```text
Audit and standardize environment configuration for this NestJS 12, Prisma 8 and local Docker Compose project.

Before editing:
1. Inventory every process.env read and every environment-specific value hardcoded in docker-compose.postgres.yml.
2. Classify each variable as application runtime, Prisma CLI, or local Compose-only configuration.
3. Show the proposed .env keys, safe .env.example placeholders, affected files and verification commands.

Requirements:
- Use the project-root .env as the single local-development value source for Docker Compose interpolation, Prisma CLI and Nest runtime.
- Keep .env ignored. Commit .env.example with the same key names and no real secrets.
- Move the PostgreSQL image, user, password, database name and host port out of docker-compose.postgres.yml.
- Use required Compose interpolation (${VAR:?message}); do not silently substitute empty strings or secret defaults.
- Keep PostgreSQL's container port 5432 fixed; only the host port is configurable.
- Let Compose validate Compose-only variables. Nest startup validation should cover only application runtime variables such as NODE_ENV, PORT and DATABASE_URL.
- Keep DATABASE_URL explicit. Do not rely on nested .env interpolation; verify that it matches the local PostgreSQL credentials and host port.
- prisma.config.ts may load dotenv for Prisma CLI. Nest must load .env with ConfigModule and pass typed config into the database factory.
- Do not read process.env from controllers, business services or repository adapters.
- Validate the Compose model with `docker compose -f docker-compose.postgres.yml config --quiet` so secrets are not printed.
- Never print DATABASE_URL or POSTGRES_PASSWORD in the answer, terminal recording or logs.
- Show the audit and plan first. Do not edit until I approve.
```

**Prompt 2 — câu hỏi Prisma ngây thơ (cảnh 13).** Gõ nguyên văn, không thêm context phiên bản. AI sẽ trả plan kiểu Prisma 7: `PrismaClient`, `schema.prisma`, `prisma generate`, `migrate dev`, inject thẳng vào UsersService. Đó chính là chất liệu để host bắt lỗi.

```text
Read this NestJS project. Replace the in-memory Users store with PostgreSQL using Prisma.
Keep the current UsersService and controller behavior.
Show a plan first, do not edit any file until I approve.
```

**Prompt 3 — sau khi host bắt lỗi (đối chiếu release status + skill + contract vừa emit).**

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
- Preserve the approved ENV and Docker Compose boundary from Prompt 1.
- Change the Prisma runtime singleton into a factory that receives the validated URL through DI.
- Do not read process.env from controllers, business services or repository adapters.
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
- [ ] Xóa `DATABASE_URL` khiến Nest fail lúc startup trước khi nhận request.
- [ ] `.env` bị ignore; `.env.example` có đủ key, chỉ chứa placeholder và được commit.
- [ ] `docker-compose.postgres.yml` không hardcode image, user, password, database hoặc host port.
- [ ] `docker compose -f docker-compose.postgres.yml config --quiet` pass mà không in secret.
- [ ] `DATABASE_URL` khớp PostgreSQL credential và host port trong `.env`.
- [ ] UsersService và PrismaUsersRepository không đọc `process.env` hoặc inject `ConfigService`.
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
✅ Đưa image, credential, database và host port của Compose vào `.env`
✅ Dùng required interpolation để thiếu biến thì Compose dừng ngay
✅ Nạp cùng một `.env` cho Prisma CLI và Nest runtime
✅ Validate DATABASE_URL, PORT và NODE_ENV ngay lúc startup
✅ Giữ secret ngoài Git bằng `.gitignore` và `.env.example`
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
🔗 Docker Compose interpolation: https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/

⏱ 0:00 Restart và mất sạch user
⏱ 1:10 PostgreSQL nằm ngoài process
⏱ 2:10 Dựng PostgreSQL local bằng Docker
⏱ 3:20 ConfigModule và fail fast DATABASE_URL
⏱ 4:40 Khóa phiên bản Prisma 8
⏱ 5:50 Contract thay cho schema.prisma
⏱ 7:10 Emit và review migration plan
⏱ 8:45 AI dùng nhầm Prisma 7
⏱ 10:00 Repository boundary và DI token
⏱ 12:00 Query bằng db.orm.public.User
⏱ 13:30 Migrate, verify và restart
⏱ 14:35 Email trùng tạo lỗi 500

#NestJS #Prisma8 #PostgreSQL #ConfigModule #RepositoryPattern #TypeScript #Backend #AICoding #LapTrinhLaCuocSong
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
