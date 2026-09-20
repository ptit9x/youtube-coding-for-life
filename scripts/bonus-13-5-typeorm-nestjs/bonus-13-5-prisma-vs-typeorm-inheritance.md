# BONUS 13.5 — Prisma vs TypeORM: Cùng RBAC, hai cách nghĩ khác nhau

- **Series:** Học NestJS bằng AI — Bonus sau tập 13
- **Target runtime:** 10–12 phút (900–1100 từ thoại)
- **Vai trò:** Nhánh so sánh ORM, không thay đổi stack Prisma của series chính.
- **Outcome:** Viewer thấy cùng hệ thống RBAC được xây bằng hai ORM, hiểu trade-off thật thay vì chọn theo trend.

---

## PART 1 — SCRIPT

Từ tập 3 đến giờ, TaskFlow dùng Prisma.

Schema nằm trong file riêng, contract được emit, adapter gọi qua facade.

Nhưng có một câu hỏi cứ xuất hiện: nếu dùng TypeORM thì sao?

Hôm nay mình build lại hệ thống RBAC từ EP08 và EP09, nhưng bằng TypeORM.

Không phải để chứng minh cái nào tốt hơn.

Mà để bạn thấy rõ hai cách tư duy khác nhau khi thiết kế entity.

Prisma bắt đầu từ schema.

Bạn mở file `.prisma`, khai báo model, field, relation.

Schema là nguồn sự thật duy nhất.

Chạy `prisma migrate dev`, Prisma đọc schema, tạo SQL migration tự động.

TypeORM bắt đầu từ class TypeScript.

Mỗi entity là một class với decorator `@Entity`, `@Column`, `@PrimaryGeneratedColumn`.

Class chính là schema.

Chạy `migration:generate`, TypeORM so sánh entity với database rồi tạo migration.

Hai hướng đi, cùng đích đến.

Điểm khác biệt đầu tiên xuất hiện ở phần metadata lặp lại.

Prisma, mỗi model bạn viết lại `id`, `createdAt`, `updatedAt`.

Ba field, lặp ở mười model, ba mươi dòng.

Prisma không có class, nên không có inheritance.

Variant và discriminator giải quyết bài toán polymorphism, không phải bài toán timestamp mixin.

TypeORM khác.

Vì entity là class TypeScript, bạn tạo `AbstractEntity`, đặt ba field vào đó.

User, Role, Permission extends class này.

Ba mươi dòng lặp biến mất.

Nhưng `AbstractEntity` phụ thuộc decorator của TypeORM.

Nó không phải utility portable.

Vì vậy mình đặt nó trong `src/database/entities`, không phải `common/`.

Vị trí file phải phản ánh dependency thật, không phản ánh mong muốn tái sử dụng.

Giờ mình mở demo TypeORM.

User entity extends `AbstractEntity`, thêm `email`, `password`, `name`.

Role entity extends base, thêm `name` unique, `description`, và cờ `isSystem`.

Permission entity tương tự, thêm `code` unique dạng `resource.action`.

Đến join table.

Với Prisma, mình khai báo model `UserRole` trong schema, nó là entity thật có `assignedBy` và `assignedAt`.

Với TypeORM, `UserRole` cũng là class entity, extends `AbstractEntity`, khai báo `@ManyToOne` tới User và Role.

Cả hai ORM đều cho phép explicit join table.

Khác nhau là cách khai báo.

Prisma dùng DSL, relation được validate ở schema level.

TypeORM dùng decorator, relation được validate ở runtime khi DataSource khởi tạo.

Mình chạy migration bên TypeORM.

`npm run migration:generate -- -n CreateRbacTables`.

TypeORM đọc entity, so với database trống, tạo file migration.

Mở file ra, mình thấy SQL tạo bảng, foreign key, unique index.

Đây là điểm quan trọng.

Prisma auto-generate migration và bạn trust nó.

TypeORM generate migration và bạn review SQL trước khi chạy.

Cả hai đều hợp lý, tùy team muốn kiểm soát ở mức nào.

`npm run migration:run`.

Bảng được tạo.

Mình seed data.

Bên service, mình giữ nguyên triết lý EP13.

Mỗi service viết logic riêng.

UsersService hash password, normalize email.

RolesService bảo vệ system role, normalize tên.

PermissionsService kiểm tra format `resource.action`, không cho đổi code.

Không có `BaseCrudService`.

Entity inheritance giảm metadata lặp.

Nó không chứng minh business service cũng nên kế thừa.

Hai quyết định này độc lập.

Giờ mình đặt hai codebase cạnh nhau.

Schema definition: Prisma dùng DSL tập trung, TypeORM dùng class phân tán.

Type safety: Prisma emit type từ contract, luôn đồng bộ. TypeORM dùng class entity, type chính là code nhưng có thể lệch runtime nếu decorator sai.

Migration: Prisma auto diff, TypeORM generate rồi review.

Query: Prisma Client cú pháp riêng, type-safe. TypeORM Repository hoặc QueryBuilder, gần SQL hơn.

Learning curve: Prisma cần học DSL mới. TypeORM quen với decorator TypeScript, NestJS dev tiếp cận nhanh hơn.

Không ORM nào thắng ở mọi tiêu chí.

Prisma mạnh khi team muốn schema là nguồn sự thật duy nhất, type safety tuyệt đối, và ít viết SQL.

TypeORM mạnh khi team quen decorator, cần fine-grained SQL control, và muốn entity inheritance tự nhiên.

Đừng đổi ORM giữa dự án chỉ vì thấy code lặp ba field.

Hãy chọn trước khi bắt đầu, dựa trên kinh nghiệm team và yêu cầu dự án.

Demo build thành công.

Migration chạy đúng.

Service vẫn explicit, không kế thừa generic CRUD.

Sau Bonus này, series trở lại Prisma tại EP14.

Công cụ khác nhau cho phép abstraction khác nhau.

Nguyên tắc thiết kế vẫn không đổi.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Ba field `id`, `createdAt`, `updatedAt` lặp trong Prisma schema | 30s |
| 2 | [DIAGRAM] | Hai hướng: Prisma schema DSL ↔ TypeORM class decorator | 50s |
| 3 | [IDE] | Tạo `AbstractEntity` bằng decorator TypeORM | 60s |
| 4 | [IDE] | Vị trí `AbstractEntity` trong `src/database/entities` | 30s |
| 5 | [IDE] | User, Role, Permission entity extends base | 70s |
| 6 | [IDE] | `UserRole` và `RolePermission` explicit join entities | 60s |
| 7 | [IDE] | So sánh Prisma schema UserRole vs TypeORM class UserRole | 50s |
| 8 | [TERMINAL] | `npm run migration:generate`, mở file SQL review | 60s |
| 9 | [TERMINAL] | `npm run migration:run`, seed data | 40s |
| 10 | [IDE] | Service explicit: Users hash password, Roles bảo vệ system, Permissions validate code | 80s |
| 11 | [DIAGRAM] | Entity inheritance ≠ service inheritance (callback EP13) | 45s |
| 12 | [TABLE] | Bảng so sánh 5 chiều: schema, type safety, migration, query, learning curve | 60s |
| 13 | [IDE] | Prisma Client query vs TypeORM Repository query side-by-side | 50s |
| 14 | [B-ROLL] | Quay lại nhánh Prisma của series — teaser EP14 | 20s |

**Tổng mục tiêu: 10–12 phút (705 giây ≈ 11:45).** Bảng so sánh dùng font tối thiểu 18px. IDE dark theme (Monokai/Dracula).

### Code cốt lõi — TypeORM

```ts
// src/database/entities/abstract.entity.ts
import {
  PrimaryGeneratedColumn,
  CreateDateColumn,
  UpdateDateColumn,
} from 'typeorm';

export abstract class AbstractEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @CreateDateColumn()
  createdAt: Date;

  @UpdateDateColumn()
  updatedAt: Date;
}
```

```ts
// src/roles/entities/role.entity.ts
import { Entity, Column, OneToMany } from 'typeorm';
import { AbstractEntity } from '../../database/entities/abstract.entity';

@Entity('roles')
export class Role extends AbstractEntity {
  @Column({ unique: true })
  name: string;

  @Column({ nullable: true })
  description: string;

  @Column({ default: false })
  isSystem: boolean;
}
```

```ts
// src/roles/entities/user-role.entity.ts
import { Entity, Column, ManyToOne, JoinColumn } from 'typeorm';
import { AbstractEntity } from '../../database/entities/abstract.entity';
import { User } from '../../users/entities/user.entity';
import { Role } from './role.entity';

@Entity('user_roles')
export class UserRole extends AbstractEntity {
  @Column()
  userId: number;

  @Column()
  roleId: number;

  @Column()
  assignedBy: number;

  @ManyToOne(() => User)
  @JoinColumn({ name: 'userId' })
  user: User;

  @ManyToOne(() => Role)
  @JoinColumn({ name: 'roleId' })
  role: Role;
}
```

### Code tương đương — Prisma (để so sánh)

```prisma
model Role {
  id          Int        @id @default(autoincrement())
  name        String     @unique
  description String?
  isSystem    Boolean    @default(false)
  createdAt   DateTime   @default(now())
  updatedAt   DateTime   @updatedAt
  userRoles   UserRole[]
}

model UserRole {
  id         Int      @id @default(autoincrement())
  userId     Int
  roleId     Int
  assignedBy Int
  createdAt  DateTime @default(now())
  updatedAt  DateTime @updatedAt
  user       User     @relation(fields: [userId], references: [id])
  role       Role     @relation(fields: [roleId], references: [id])

  @@unique([userId, roleId])
}
```

### Prompt cho AI

```text
Build the same RBAC system (User, Role, Permission, UserRole, RolePermission) using NestJS + TypeORM + PostgreSQL.
- Create AbstractEntity for id, createdAt, updatedAt in src/database/entities/.
- User, Role, Permission extend AbstractEntity.
- UserRole and RolePermission are explicit join entities with assignedBy metadata.
- Each service has its own business logic — no BaseCrudService, no generic CRUD inheritance.
- UsersService: hash password, normalize email.
- RolesService: protect system roles, normalize name.
- PermissionsService: validate resource.action format, immutable code.
- Generate TypeORM migration and review SQL before running.
- Show the migration plan before implementing.
- Compare with the Prisma equivalent at each step.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic split-screen of two developer monitors, one showing a schema DSL file and the other showing TypeScript decorator classes, dark room, neon blue on left screen and neon green on right screen, code reflections on desk surface, 16:9, photorealistic, no text, no logos.`
2. `A dramatic developer standing at a crossroads with two glowing ORM pathways, one schema-based with blue neon and one decorator-based with green neon, dark foggy atmosphere, city bokeh background, subject right side, 16:9, photorealistic, no text.`
3. `A cinematic close-up of a TypeScript class entity glowing with green decorator annotations inheriting from a base class, dark IDE background, shallow depth of field, code reflecting in eyeglasses, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Prisma vs TypeORM: Cùng RBAC, hai cách nghĩ khác nhau — Bonus 13.5 | Lập trình là cuộc sống
2. Xây RBAC bằng TypeORM thì khác Prisma chỗ nào? — Bonus 13.5 | Lập trình là cuộc sống
3. TypeORM có thật sự dễ hơn Prisma cho NestJS? — Bonus 13.5 | Lập trình là cuộc sống
4. So sánh Prisma và TypeORM bằng code thật — Bonus 13.5 | Lập trình là cuộc sống
5. BaseEntity trong TypeORM giải quyết được gì mà Prisma không? — Bonus 13.5 | Lập trình là cuộc sống
6. Prisma hay TypeORM? Đừng chọn theo số sao GitHub — Bonus 13.5 | Lập trình là cuộc sống
7. Entity Inheritance trong TypeORM và cái giá phải trả — Bonus 13.5 | Lập trình là cuộc sống
8. TypeORM RBAC từ đầu: AbstractEntity, Migration, Explicit Service — Bonus 13.5 | Lập trình là cuộc sống
9. Nếu TaskFlow dùng TypeORM thì code trông thế nào? — Bonus 13.5 | Lập trình là cuộc sống
10. Đổi ORM chỉ vì ba field lặp? Nghĩ lại đi — Bonus 13.5 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 3 cho curiosity gap và Title 6 cho controversy.

### 4b. SEO Description

```text
Series chính dùng Prisma. Bonus này build lại RBAC bằng TypeORM để so sánh trực tiếp — không chọn winner, chỉ cho bạn thấy trade-off thật.

✅ So sánh schema DSL (Prisma) và class decorator (TypeORM)
✅ Tạo AbstractEntity — inheritance tự nhiên trong TypeORM
✅ Đặt base entity đúng tầng infrastructure
✅ Explicit join entities: UserRole, RolePermission với audit metadata
✅ Migration auto-diff vs generate-and-review
✅ Service explicit — không kế thừa generic CRUD
✅ Bảng so sánh 5 chiều: schema, type safety, migration, query, learning curve
✅ Khi nào chọn Prisma, khi nào chọn TypeORM

⏱ 0:00 Ba field lặp trong Prisma schema
⏱ 0:50 Hai hướng: schema DSL vs class decorator
⏱ 2:00 AbstractEntity và vị trí đúng
⏱ 3:30 Entity RBAC: User, Role, Permission
⏱ 5:00 Explicit join tables với metadata
⏱ 6:30 Migration workflow so sánh
⏱ 8:00 Service explicit — entity ≠ service inheritance
⏱ 9:30 Bảng trade-off 5 chiều
⏱ 11:00 Chọn ORM trước khi bắt đầu

#NestJS #Prisma #TypeORM #ORM #RBAC #Database #TypeScript #CleanArchitecture #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
prisma vs typeorm, typeorm nestjs, prisma nestjs, typeorm abstract entity, base entity typeorm, typeorm migration, prisma migration, typeorm rbac, nestjs orm comparison, explicit join entity, typeorm decorator, prisma schema, typeorm repository, generic crud trap, nestjs bonus, typeorm tiếng việt, prisma tiếng việt, so sánh orm, nestjs orm, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `PRISMA` — NEON GREEN `#00FF41`
- `vs TYPEORM` — WHITE
- `AI CHỌN AI?` — NEON GREEN `#00FF41`
- Hình: split-screen hai monitor, một schema DSL một decorator class.

### Option 2
- `CÙNG RBAC` — WHITE
- `HAI CÁCH NGHĨ` — NEON GREEN `#00FF41`
- Hình: developer đứng giữa hai con đường ORM.

### Option 3
- `3 DÒNG LẶP` — WHITE
- `ĐỔI CẢ ORM?` — RED `#FF3B30`
- Hình: code timestamps bị highlight đỏ, TypeORM class phát sáng xanh.

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px. Typeset trong Canva và giữ bản nền không chữ.
