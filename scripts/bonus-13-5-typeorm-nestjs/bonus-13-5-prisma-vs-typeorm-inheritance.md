# BONUS 13.5 — Prisma và TypeORM: Có nên dùng BaseEntity?

- **Series:** Học NestJS bằng AI — Bonus sau tập 13
- **Target runtime:** ~12 phút
- **Vai trò:** Nhánh so sánh ORM, không thay đổi stack Prisma của series chính.
- **Outcome:** Hiểu entity inheritance không đồng nghĩa business service inheritance.

---

## PART 1 — SCRIPT

Mỗi model Prisma đều lặp `id`, `createdAt` và `updatedAt`.

Sau EP13, nhiều bạn sẽ hỏi tại sao không tạo `BaseEntity`.

Prisma schema không dùng class inheritance theo cách TypeORM sử dụng.

TypeORM giải quyết phần lặp này bằng class inheritance.

Đây là tập Bonus vì chúng ta tạm rẽ khỏi stack chính.

TaskFlow vẫn dùng Prisma sau video này.

Prisma schema là một DSL mô tả model và quan hệ.

TypeORM dùng class TypeScript cùng decorator để ánh xạ entity.

Vì là class, TypeORM có thể dùng inheritance tự nhiên hơn.

`AbstractEntity` gom ID cùng thời gian tạo và sửa bằng decorator của TypeORM.

User, Role và Permission có thể extends class này.

`AbstractEntity` phụ thuộc decorator của TypeORM.

Nó không phải utility portable cho mọi dự án.

Vì vậy, mình đặt nó trong infrastructure database.

Vì vậy, nó nằm trong `src/database/typeorm/entities`, không nằm trong package common độc lập.

Không đặt nó trong package `common` độc lập với framework.

Vị trí file phải phản ánh dependency thật, không phản ánh mong muốn tái sử dụng.

Ta demo lại User, Role và Permission.

Join table vẫn là entity thật vì cần audit metadata.

`UserRole` extends base entity, nhưng vẫn khai báo `userId`, `roleId` và `assignedBy` của chính nó.

Inheritance giảm phần metadata kỹ thuật lặp lại.

Nó không xóa nhu cầu thiết kế quan hệ explicit.

Thấy entity inheritance chạy đẹp, AI đề nghị thêm `CrudService<TEntity>`.

Đây chính là chiếc bẫy từ EP13 quay lại.

Entity chia sẻ lifecycle database. Service chia sẻ hay không còn phụ thuộc business semantics.

Hai quyết định này độc lập.

User register, role create và permission create vẫn có rule khác nhau.

Một base entity hợp lý không chứng minh base service cũng hợp lý.

TypeORM cho cảm giác gần TypeScript và decorator của NestJS.

Prisma cho schema tập trung, generated client và query API rõ ràng.

TypeORM inheritance giảm vài trường lặp. Prisma giữ model tường minh trong schema.

Không lựa chọn nào thắng chỉ bằng số dòng.

Hãy xét migration, type safety, query style và kinh nghiệm của đội.

Đừng đổi ORM giữa dự án chỉ để tránh ba field lặp.

Demo TypeORM build và migration thành công.

UserRole và RolePermission vẫn chứa metadata riêng.

Business service vẫn explicit, không kế thừa generic CRUD.

Ta đã tái sử dụng đúng phần thay đổi cùng nhau.

Sau Bonus này, series trở lại Prisma tại EP14.

Mục tiêu tiếp theo là tách code portable ra khỏi một project cụ thể.

Công cụ khác nhau cho phép abstraction khác nhau. Nguyên tắc thiết kế vẫn không đổi.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [IDE] | Ba field lặp trong Prisma schema | 35s |
| 2 | [DIAGRAM] | Prisma DSL và TypeORM class model | 60s |
| 3 | [IDE] | Tạo AbstractEntity bằng decorator | 80s |
| 4 | [IDE] | Vị trí base entity trong database infrastructure | 45s |
| 5 | [IDE] | UserRole explicit với audit metadata | 80s |
| 6 | [AI] | AI đề nghị CrudService inheritance | 55s |
| 7 | [DIAGRAM] | Entity reuse khác service reuse | 60s |
| 8 | [TERMINAL] | Chạy migration và build demo | 70s |
| 9 | [TABLE] | So sánh trade-off Prisma và TypeORM | 75s |
| 10 | [B-ROLL] | Quay lại nhánh Prisma của series | 25s |

**Tổng: 585 giây ≈ 9:45.** Dành thêm hai phút cho bảng so sánh; font tối thiểu 18px.

### Code cốt lõi

```ts
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
@Entity('roles')
export class Role extends AbstractEntity {
  @Column({ unique: true })
  name: string;

  @Column({ default: false })
  isSystem: boolean;
}
```

### Prompt cho AI

```text
Create a separate TypeORM comparison demo without changing TaskFlow's Prisma stack.
- Add AbstractEntity for id and timestamps.
- Keep UserRole and RolePermission as explicit entities.
- Place TypeORM-specific base classes inside database infrastructure.
- Do not add a generic business CrudService.
- Compare trade-offs without declaring a universal winner.
- Show the migration plan before implementing.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic split-screen duel between a declarative database schema and TypeScript entity classes, dark IDE, neon blue and green lighting, developer centered, 16:9, photorealistic, no text, no logos.`
2. `A dramatic abstract entity blueprint projecting id and timestamp fields into three database entities, dark server room, cyan holograms, 16:9, photorealistic, no text.`
3. `A cinematic developer choosing between two ORM pathways, one schema-based and one decorator-based, dark atmosphere, neon signs without words, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Prisma và TypeORM: Có nên dùng BaseEntity? — Bonus 13.5 | Lập trình là cuộc sống
2. BaseEntity trong TypeORM hoạt động thế nào? — Bonus 13.5 | Lập trình là cuộc sống
3. Vì sao Prisma schema không dùng BaseEntity? — Bonus 13.5 | Lập trình là cuộc sống
4. So sánh Entity Inheritance trong Prisma và TypeORM | Lập trình là cuộc sống
5. Có nên đổi ORM chỉ để giảm code lặp? — Bonus 13.5 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho TypeORM và Title 3 cho người dùng Prisma.

### 4b. SEO Description

```text
Prisma schema không extends BaseEntity như TypeORM. Điều đó có đáng để đổi ORM không?

✅ So sánh schema DSL và class entity
✅ Tạo TypeORM AbstractEntity
✅ Đặt ORM-specific code đúng tầng infrastructure
✅ Giữ explicit join entities cho audit metadata
✅ Phân biệt entity inheritance với service inheritance
✅ So sánh trade-off thay vì chọn theo số dòng

⏱ 0:00 Ba field lặp trong Prisma
⏱ 1:10 Hai programming model
⏱ 3:00 AbstractEntity đúng chỗ
⏱ 4:45 Explicit many-to-many
⏱ 6:30 Generic CRUD quay lại
⏱ 8:10 Prisma hay TypeORM?

#NestJS #Prisma #TypeORM #ORM #Database #TypeScript #CleanArchitecture #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
prisma vs typeorm, typeorm abstract entity, prisma inheritance, base entity nestjs, typeorm many to many, explicit join entity, generic crud trap, nestjs orm comparison, typeorm tiếng việt, prisma tiếng việt, nestjs bonus, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `PRISMA KHÔNG EXTENDS` — WHITE
- `TYPEORM THÌ SAO?` — NEON GREEN `#00FF41`
### Option 2
- `BASE ENTITY` — NEON GREEN `#00FF41`
- `CÓ ĐÁNG KHÔNG?` — WHITE
### Option 3
- `3 DÒNG LẶP` — WHITE
- `ĐỔI CẢ ORM?` — RED `#FF3B30`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
