# So sánh Prisma vs TypeORM — Reference Table

| Tiêu chí | Prisma | TypeORM |
|---|---|---|
| **Schema definition** | File `.prisma` riêng (DSL) — schema là nguồn sự thật duy nhất | Class TypeScript + decorators — schema nằm trong code |
| **Type safety** | Emitted types từ contract — auto-generated, luôn đồng bộ schema | Dùng chính class entity — type đúng nhưng có thể lệch runtime nếu decorator sai |
| **Entity inheritance** | Không hỗ trợ class mixin. Variants/discriminator dành cho polymorphism cùng họ record | `extends` class tự nhiên — `AbstractEntity` giảm boilerplate timestamps |
| **Migration** | `prisma migrate dev` — auto-generate từ schema diff | `migration:generate` — cần review SQL trước khi chạy |
| **Query style** | Prisma Client — method chain, type-safe, cú pháp riêng | Repository pattern hoặc QueryBuilder — gần SQL hơn, linh hoạt hơn |
| **Relations** | Khai báo trong schema, Prisma tự tạo join table | Decorator `@ManyToMany`, `@JoinTable` hoặc explicit join entity |
| **Learning curve** | DSL mới + CLI workflow — curve ban đầu cao hơn | Decorator TypeScript quen thuộc — NestJS dev học nhanh hơn |
| **Raw SQL** | `$queryRaw` — escape hatch | `query()` hoặc QueryBuilder — gần SQL tự nhiên hơn |
| **Ecosystem NestJS** | `@nestjs/prisma` — tích hợp tốt nhưng cần adapter | `@nestjs/typeorm` — first-class integration, cùng decorator philosophy |
| **Khi nào chọn** | Team muốn schema tập trung, type safety tuyệt đối, ít viết SQL | Team quen decorator, cần fine-grained SQL control, dùng nhiều inheritance |
