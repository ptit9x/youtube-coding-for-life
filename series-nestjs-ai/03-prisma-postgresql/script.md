# NestJS + Prisma 8: Lưu User vào PostgreSQL | #3

- **Series:** Học NestJS bằng AI — tập 3/45
- **Trạng thái:** ✅ Đã đăng
- **Title đã đăng:** NestJS + Prisma 8: Lưu User vào PostgreSQL | #3
- **YouTube:** https://www.youtube.com/watch?v=kUXmQxjecNE
- **Ngày đăng:** 2026-09-20
- **Thời lượng thực tế:** 14:19
- **Target runtime:** 14:19 (thời lượng video đã đăng)
- **Outcome:** Dựng PostgreSQL local không hardcode Compose config; cấu hình ENV có validation; thay Users in-memory bằng PostgreSQL qua Prisma 8 và repository contract.
- **Technical baseline:** NestJS 12, Node.js 24.11+, TypeScript 5.9+, ESM, PostgreSQL, Prisma ORM 8.
- **Pain mở EP04:** Email trùng chạm unique constraint và biến thành lỗi 500 khó hiểu.
- **Source of truth:** [Prisma 8 với NestJS](https://www.prisma.io/docs/guides/frameworks/nestjs), [Prisma 8 release status](https://www.prisma.io/docs/prisma-orm/release-status), [NestJS Configuration](https://docs.nestjs.com/techniques/configuration), [Docker Compose interpolation](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/).

---

## PART 1 — TRANSCRIPT VIDEO ĐÃ ĐĂNG (LÀM SẠCH)

### 0:00 — Restart server làm mất toàn bộ user

Chào mọi người. Ở video trước, mỗi lần restart server thì toàn bộ user vừa tạo đều biến mất. API trả 201 rất đẹp nhưng khi gọi lại danh sách thì mảng đã rỗng.

Mảng trong `UsersService` nằm trong RAM nên vùng nhớ được giải phóng khi application khởi động lại. Chính vì thế, chúng ta cần PostgreSQL hoặc một database khác để lưu dữ liệu. Trong video hôm nay, mình sẽ chia sẻ cách kết nối NestJS với PostgreSQL.

### 0:43 — Yêu cầu AI tạo Docker Compose cho PostgreSQL

Mình yêu cầu AI viết một file Docker để chạy PostgreSQL ngay trong thư mục source code. Sau khi file được tạo, chúng ta chạy lệnh `docker compose up`. Để dùng được lệnh này, máy cần cài Docker trước; các bạn có thể tải tại docker.com.

### 1:15 — Đọc cấu hình container PostgreSQL

Trong file vừa tạo, Docker sẽ pull một PostgreSQL image từ Docker Hub. Có thể hiểu đơn giản image là bộ cài đã được đóng gói; Docker chạy image đó thành một container chứa database.

File cấu hình trên màn hình cũng chứa các thông tin dùng để kết nối database gồm username, password, tên database và port `5432`.

### 1:59 — Tách file Docker cho môi trường development

`docker-compose.yml` mặc định sau này còn được dùng để đóng gói và deploy application. Vì file hiện tại chỉ chạy PostgreSQL cho development, mình đổi tên thành `docker-compose.postgres.yml` và cập nhật README với lệnh khởi động tương ứng.

Khi development, chúng ta dùng file PostgreSQL riêng này. Đến lúc triển khai production hoặc môi trường test, mình sẽ tạo file Docker Compose phù hợp sau.

### 2:39 — PostgreSQL đã chạy trên máy

Sau khi chạy lệnh, container PostgreSQL đã được khởi động trên máy. Như vậy phần database local đã sẵn sàng.

### 2:52 — Prompt chuẩn hóa biến môi trường

Username, password và tên database đều là cấu hình nhạy cảm nên không nên hardcode. Mình dùng một prompt đã chuẩn bị sẵn, yêu cầu AI tìm toàn bộ biến môi trường và giá trị hardcode trong project, sau đó chuyển chúng sang file môi trường.

### 3:31 — Review kế hoạch cấu hình của AI

AI audit trạng thái hiện tại và nhận ra project mới chỉ đọc một biến môi trường trong `main.ts`, chưa có `ConfigModule`, `ConfigService` hay thư viện `@nestjs/config`. Kế hoạch cũng bổ sung các biến database và file `.env.example`.

Thứ tự thực hiện khá hợp lý: cài phần cấu hình cho NestJS trước rồi mới chuyển các giá trị sang biến môi trường.

### 4:35 — Chỉnh lại vị trí thư mục config

Trong plan ban đầu, AI muốn đặt config dưới `src/common`. Mình không đồng ý vì `common` chỉ nên chứa những thành phần thật sự dùng chung. Có project dùng PostgreSQL, nhưng cũng có project dùng MySQL hoặc MongoDB; database config không phù hợp để nhét vào `common`.

Mình yêu cầu tạo `src/config` ngang cấp với `src/common`, đồng thời tách rõ biến nào thuộc application và biến nào thuộc database. Sau khi AI cập nhật plan, cấu trúc gồm phần validation, application config và database config đã hợp lý hơn.

### 5:42 — Approve plan và tạo các file config

Mình approve để AI thực hiện. Các file config và môi trường mới được tạo theo đúng cấu trúc vừa thống nhất.

### 6:09 — Cách review code khi AI viết ngày càng nhanh

Với tốc độ phát triển của AI, việc đọc kỹ từng dòng code mà agent sinh ra ngày càng khó trong công việc thực tế. Mình thường kiểm tra cấu trúc tổng thể, review các file quan trọng và đặt ra những quy tắc rõ ràng để AI tiếp tục sửa code đúng hướng.

### 6:33 — Prompt thay in-memory store bằng Prisma

Đây là phần quan trọng nhất của video. Mình yêu cầu AI đọc project và thay in-memory Users store bằng PostgreSQL sử dụng Prisma. Trước tiên, mình cố tình dùng một prompt khá ngắn để xem AI sẽ xử lý như thế nào.

### 6:59 — Kế hoạch Prisma ban đầu

AI tìm thấy User entity, DTO, controller, module và cấu hình database hiện có. Kế hoạch của nó là tạo Prisma schema, cài các thư viện cần thiết và chạy migration. Nhìn tổng thể plan có vẻ ổn nên mình cho chạy thử.

### 7:52 — AI bắt đầu với Prisma 7 rồi phát hiện Prisma 8

Trong package, Prisma Client đang ở phiên bản 7.10 trở lên. Sau đó AI phát hiện Prisma có thêm phiên bản 8, tạo tài liệu riêng cho V8 và hỏi có nên xóa phần Prisma cũ hay không. Khả năng tự phát hiện thay đổi phiên bản này khá ấn tượng.

### 9:12 — Kiểm tra release status của Prisma

Mình mở tài liệu phiên bản hiện tại của Prisma để kiểm tra. Trang release status cho thấy ORM 7 đang được support đầy đủ, còn ORM 8 mới ở trạng thái candidate.

Prisma 7 hoàn toàn có thể dùng trong production. Vấn đề ở đây là prompt của mình chưa chỉ định rõ phiên bản, khiến AI cài V7, phát hiện V8, xóa rồi tạo lại. Workflow đó tạo ra rework không cần thiết, nên mình reject và làm lại.

### 10:33 — Viết lại prompt rõ ràng cho Prisma 8

Prompt mới yêu cầu AI đọc codebase hiện tại và sử dụng Prisma ORM 8. Mình vẫn giữ nguyên quy tắc: trước khi chỉnh sửa file, AI phải đưa ra plan để mình review.

Prompt càng rõ thì càng tiết kiệm token, chi phí và thời gian. Nếu yêu cầu mơ hồ, một tác vụ có thể phải làm lại nhiều lần và phần rework còn đắt hơn việc chuẩn bị đúng ngay từ đầu.

### 11:25 — Review kế hoạch Prisma 8

Trong plan mới, AI chuyển dependency từ V7 sang V8 và dùng package PostgreSQL runtime thay cho Prisma Client cũ. Nó cũng vẽ lại architecture và cho thấy các thay đổi về thư viện cũng như cú pháp. Sau khi review, mình cho AI tiếp tục.

### 12:02 — Áp dụng Prisma 8 và repository pattern

Package đã được đổi từ Prisma Client sang PostgreSQL runtime của Prisma ORM 8. Prisma cũng tạo một Users repository.

Có thể hiểu repository giống như một quầy giao nhận. `UsersService` cần tìm kiếm hoặc lưu dữ liệu user thì Prisma đứng phía sau thực hiện công việc đó thông qua repository. Service không cần làm việc trực tiếp với chi tiết database.

### 12:39 — Tự kiểm tra API bằng Postman

AI bắt đầu chạy test nhưng mình dừng lại để tự kiểm tra. Khi gọi API bằng Postman, dữ liệu user mà AI vừa tạo đã xuất hiện và ID tiếp tục tăng, cho thấy dữ liệu đang được lưu trong PostgreSQL thay vì mảng RAM.

### 13:13 — Email trùng trả lỗi 500

Khi gửi lại request với cùng email, API trả lỗi 500. Prisma định nghĩa model User tương ứng với các cột trong database và email có unique constraint, vì vậy database từ chối bản ghi bị trùng.

Database đang bảo vệ dữ liệu đúng, nhưng API chưa biết diễn giải lỗi kỹ thuật đó cho client.

### 14:02 — Teaser Error Handling

Trong tập sau, mình sẽ map lỗi kỹ thuật thành các status 400, 404 hoặc 409 rõ ràng. Theo dõi series nếu bạn muốn thấy lỗi 500 này được bóc tách đến tận nguyên nhân. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — TIMELINE VIDEO ĐÃ ĐĂNG

| Timestamp | Nội dung thực tế |
|---|---|
| 0:00 | Restart server làm mất toàn bộ user |
| 0:43 | Yêu cầu AI tạo Docker Compose cho PostgreSQL |
| 1:15 | Đọc cấu hình container PostgreSQL |
| 1:59 | Tách file Docker cho môi trường development |
| 2:39 | PostgreSQL đã chạy trên máy |
| 2:52 | Prompt chuẩn hóa biến môi trường |
| 3:31 | Review kế hoạch cấu hình của AI |
| 4:35 | Chỉnh lại vị trí thư mục config |
| 5:42 | Approve plan và tạo các file config |
| 6:09 | Cách review code khi AI viết ngày càng nhanh |
| 6:33 | Prompt thay in-memory store bằng Prisma |
| 6:59 | Kế hoạch Prisma ban đầu |
| 7:52 | AI bắt đầu với Prisma 7 rồi phát hiện Prisma 8 |
| 9:12 | Kiểm tra release status của Prisma |
| 10:33 | Viết lại prompt rõ ràng cho Prisma 8 |
| 11:25 | Review kế hoạch Prisma 8 |
| 12:02 | Áp dụng Prisma 8 và repository pattern |
| 12:39 | Tự kiểm tra API bằng Postman |
| 13:13 | Email trùng trả lỗi 500 |
| 14:02 | Teaser Error Handling |

**Thời lượng thực tế:** 14:19.

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

1. NestJS + Prisma 8: Lưu User vào PostgreSQL | #3
2. Prisma 8 ĐÃ KHÁC: Lưu User từ NestJS vào PostgreSQL — EP03
3. Repository Pattern với Prisma 8 trong NestJS — EP03
4. Từ RAM đến PostgreSQL: NestJS + Prisma 8 — EP03
5. Contract và Migration đầu tiên với Prisma 8 — EP03

**Title 1 là title đã đăng.** Các title còn lại được giữ làm tư liệu tham khảo.

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

⏱ Timestamps thực tế:
0:00 Restart server làm mất toàn bộ user
0:43 Tạo Docker Compose cho PostgreSQL
1:15 Đọc cấu hình container PostgreSQL
1:59 Tách file Docker cho development
2:39 PostgreSQL đã chạy trên máy
2:52 Prompt chuẩn hóa biến môi trường
3:31 Review kế hoạch cấu hình của AI
4:35 Chỉnh lại vị trí thư mục config
5:42 Approve plan và tạo các file config
6:09 Cách review code do AI tạo
6:33 Prompt thay in-memory store bằng Prisma
6:59 Kế hoạch Prisma ban đầu
7:52 AI bắt đầu với Prisma 7 rồi phát hiện Prisma 8
9:12 Kiểm tra release status của Prisma
10:33 Viết lại prompt rõ ràng cho Prisma 8
11:25 Review kế hoạch Prisma 8
12:02 Áp dụng Prisma 8 và repository pattern
12:39 Tự kiểm tra API bằng Postman
13:13 Email trùng trả lỗi 500
14:02 Teaser Error Handling

📋 PROMPT DÙNG TRONG VIDEO (copy thoải mái):

▶ Prompt 1 — Chuẩn hóa ENV và Docker Compose:
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

▶ Prompt 2 — Câu hỏi Prisma ngây thơ (để xem AI trả lời sai thế nào):
Read this NestJS project. Replace the in-memory Users store with PostgreSQL using Prisma.
Keep the current UsersService and controller behavior.
Show a plan first, do not edit any file until I approve.

▶ Prompt 3 — Sửa lại đúng Prisma 8:
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
