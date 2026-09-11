# NestJS #11 — RBAC và Ownership: Không cho sửa task người khác

- **Series:** Học NestJS bằng AI — tập 11/46
- **Target runtime:** ~12 phút
- **Outcome:** TasksModule hoàn chỉnh, permission theo route và ownership theo resource.
- **Pain mở EP12:** Số nhánh bảo mật đã vượt khả năng kiểm tra thủ công.

---

## PART 1 — SCRIPT

User A có permission `tasks.update`. User B cũng có permission đó.

User A gửi request sửa task của User B. API trả về 200.

PermissionGuard hoạt động đúng, nhưng dữ liệu vẫn bị xâm phạm.

Permission trả lời bạn được làm hành động nào. Ownership trả lời bạn được làm trên dữ liệu của ai.

TasksModule sẽ nối permission ở cửa với ownership trên từng bản ghi.

Task có `id`, `title`, `completed` và `ownerId`.

Mỗi task chỉ thuộc một user. Quan hệ này nằm trong database, không nằm trong trí nhớ controller.

TasksController nhận request và gọi service. TasksService giữ business rule.

TasksRepository là contract. PrismaTasksRepository là adapter truy cập dữ liệu.

Toàn bộ feature nằm trong `src/modules/tasks`. DTO, controller, service và repository đứng cạnh domain mà chúng phục vụ.

Mình không tạo thêm use-case folder. Độ phức tạp hiện tại chưa cần nó.

Mình gọi Agent Skill từ EP06.

Prompt yêu cầu scaffold TasksModule, giữ controller mỏng và repository contract không phụ thuộc Prisma. AI phải trình plan rồi chờ duyệt.

AI đề xuất `ownerId` trong CreateTaskDto. Nhìn hợp lý, nhưng đây là lỗi bảo mật.

Client không được tự tuyên bố chủ sở hữu. `ownerId` phải lấy từ access token.

Mình yêu cầu bỏ trường đó khỏi DTO trước khi approve.

Đây là giá trị thật của bước review plan. Lỗi bị chặn trước khi thành code.

Bốn hành động dùng bốn permission rõ ràng.

Chúng là `tasks.create`, `tasks.read`, `tasks.update` và `tasks.delete`.

Controller khai báo permission, nhưng không tự tính quyền.

Route POST khai báo `tasks.create`. Controller lấy user hiện tại rồi chuyển user ID cùng DTO vào service.

Guard kiểm tra hành động. Service kiểm tra resource cụ thể.

Hai lớp này bổ sung cho nhau, không thay thế nhau.

Bản đầu của update khá quen thuộc.

Nó tìm task theo ID rồi update ngay.

Code kiểm tra task tồn tại, nhưng không kiểm tra chủ sở hữu.

Mình đăng nhập bằng User A rồi sửa task của User B. Request vẫn thành công.

Đây là khoảnh khắc quan trọng nhất của tập.

AI không thiếu cú pháp. Prompt của chúng ta thiếu chính sách ownership.

Mình bổ sung rule tại service.

Nếu `task.ownerId` khác `actorId`, service ném `ForbiddenException`.

Service là nơi phù hợp vì rule phụ thuộc task cụ thể.

Guard không nên tải mọi resource chỉ để đoán ownership.

Sửa một task đã an toàn. Nhưng `GET /tasks` vẫn trả toàn bộ database.

Ownership không chỉ áp dụng cho update và delete. Nó còn giới hạn phạm vi truy vấn.

Repository nhận `ownerId` từ service.

Method `findAllByOwner` luôn đưa `ownerId` vào điều kiện truy vấn Prisma.

User thường chỉ thấy task của mình. Admin cần hành vi khác phải có policy rõ ràng.

Ta chưa thêm `tasks.read.any`. Đừng mở cửa bằng một điều kiện tên role bí mật.

Khi requirement xuất hiện, ta sẽ thêm permission tương ứng.

Mình chạy lại bằng hai tài khoản.

User A tạo task, đọc danh sách và sửa task của mình thành công.

User A sửa task của User B và nhận 403.

User thiếu `tasks.update` cũng nhận 403, nhưng bị chặn ngay tại guard.

Cùng status, hai nguyên nhân nằm ở hai tầng khác nhau.

Controller vẫn mỏng. Business rule vẫn nhìn thấy được trong service.

Repository chỉ lo truy vấn. Không có `CommonService` thần kỳ nào xuất hiện.

Nhưng bây giờ chúng ta có quá nhiều nhánh để thử bằng tay.

Tập sau, ta xây ma trận test cho auth, permission và ownership.

Security không thể dựa vào trí nhớ của người bấm Postman. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | User A sửa task của User B và nhận 200 | 35s |
| 2 | [DIAGRAM] | Permission và ownership trả lời hai câu hỏi khác nhau | 50s |
| 3 | [IDE] | Cấu trúc TasksModule và Prisma model | 70s |
| 4 | [AI] | Gọi Agent Skill, review plan và loại `ownerId` khỏi DTO | 80s |
| 5 | [IDE] | Gắn bốn permission lên controller | 70s |
| 6 | [BROWSER] | Tái hiện bug update chéo user | 60s |
| 7 | [IDE] | Host tự gõ ownership rule trong service | 80s |
| 8 | [IDE] | Scope `findAllByOwner` tại repository | 65s |
| 9 | [BROWSER] | Test hai user, thiếu permission và sai owner | 90s |
| 10 | [DIAGRAM] | Guard kiểm tra action, service kiểm tra resource | 55s |
| 11 | [B-ROLL] | Ma trận test mở ra teaser EP12 | 25s |

**Tổng: 680 giây ≈ 11:20.** Font IDE tối thiểu 18px; che token và dữ liệu cá nhân.

### Code cốt lõi

```prisma
model Task {
  id        Int      @id @default(autoincrement())
  title     String
  completed Boolean  @default(false)
  ownerId   Int
  owner     User     @relation(fields: [ownerId], references: [id])
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([ownerId])
}
```

```ts
async update(actorId: number, id: number, dto: UpdateTaskDto) {
  const task = await this.getById(id);
  if (task.ownerId !== actorId) {
    throw new ForbiddenException('Bạn không thể sửa task này');
  }
  return this.tasksRepository.update(id, dto);
}
```

### Prompt cho AI

```text
Use the project Agent Skill to plan a TasksModule.
- Task belongs to one User through ownerId.
- Client never supplies ownerId; derive it from request.user.
- Controller declares tasks.create/read/update/delete.
- Guard checks permission; service checks resource ownership.
- Repository contract must not import Prisma types.
- List queries must be scoped by owner.
- Show the plan and wait for approval.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic developer holding a valid green permission badge while blocked from another user's red locked task card, dark IDE background, cyan rim light, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic split-screen of two user profiles and one task record, a glowing ownership line protecting the correct user, dark server room, neon green and red accents, 16:9, photorealistic, no text.`
3. `A cinematic API security checkpoint with two gates labeled visually by icons for action and ownership, developer silhouette, dark blue code environment, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. RBAC và Ownership: Không cho sửa task người khác — EP11 | Lập trình là cuộc sống
2. Xây TasksModule hoàn chỉnh trong NestJS — EP11 | Lập trình là cuộc sống
3. Permission và Ownership khác nhau thế nào? — EP11 | Lập trình là cuộc sống
4. Lấy ownerId từ JWT thay vì payload — EP11 | Lập trình là cuộc sống
5. Giới hạn User chỉ xem task của mình — EP11 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho search và Title 3 cho người mới.

### 4b. SEO Description

```text
PermissionGuard chạy đúng nhưng user vẫn sửa được task của người khác. Vấn đề nằm ở ownership.

✅ Scaffold TasksModule bằng Agent Skill
✅ Giữ controller mỏng và repository tách Prisma
✅ Không nhận ownerId từ client
✅ Phân biệt permission với resource ownership
✅ Scope danh sách task theo user
✅ Test thủ công bằng hai tài khoản

⏱ 0:00 Có permission vẫn sai
⏱ 1:15 Thiết kế TasksModule
⏱ 2:40 Review plan của AI
⏱ 4:20 Gắn permission lên route
⏱ 6:00 Phát hiện bug ownership
⏱ 8:15 Scope dữ liệu theo owner
⏱ 10:15 Test hai tài khoản

#NestJS #Authorization #RBAC #Ownership #Prisma #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs tasks module, nestjs ownership, permission vs ownership, rbac nestjs, prisma repository nestjs, current user decorator, resource authorization, nestjs forbidden exception, nestjs tiếng việt, học nestjs, nestjs tập 11, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `CÓ PERMISSION` — WHITE
- `VẪN SAI?` — NEON GREEN `#00FF41`
### Option 2
- `TASK CỦA AI?` — WHITE
- `ĐỪNG ĐỤNG!` — RED `#FF3B30`
### Option 3
- `GUARD ĐÚNG` — WHITE
- `DATA VẪN LỘ` — NEON GREEN `#00FF41`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
