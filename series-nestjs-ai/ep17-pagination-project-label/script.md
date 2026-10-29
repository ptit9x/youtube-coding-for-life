# NestJS #17 — Pagination, Project, Label và migration không xóa lịch sử

- **Series:** Học NestJS bằng AI — tập 17/29
- **Recording status:** READY
- **Target runtime:** 9–10 phút (~775 từ thoại + khoảng nghỉ migration)
- **Outcome:** Pagination ổn định; Project, Label và TaskLabel được thêm bằng expand-backfill-contract an toàn.
- **Pain tập kế:** Create Task và attach Label vẫn là nhiều write có thể thành công một nửa.

---

## PART 1 — SCRIPT

GET `/tasks` từng trả về mười dòng trong chớp mắt.

Sau vài tháng, nó trả năm nghìn task cùng attachment metadata.

Response nặng. Client đứng hình. Database vẫn cố tỏ ra ổn.

Mình thêm `page` và `limit`, rồi dùng offset.

Trang đầu chạy đẹp. Trang thứ hai bắt đầu lặp task khi có dữ liệu mới chen vào.

Đi càng sâu, database càng phải bỏ qua nhiều dòng.

Phân trang không chỉ là cắt kết quả. Nó là lời hứa rằng trang kế tiếp tiếp tục đúng chỗ.

Bước ngoặt là dùng cursor trên một thứ tự ổn định.

Offset nói “bỏ qua hai mươi dòng”. Cursor nói “tiếp tục sau bản ghi này”.

Với màn hình quản trị nhỏ, offset vẫn hữu ích vì nhảy được tới trang cụ thể.

Với feed task thay đổi liên tục, cursor thường ổn định hơn.

Mình yêu cầu AI lập plan cho filter status, owner, deadline và sort ngày tạo.

AI chọn cursor chỉ có `createdAt`.

Mình dừng ở bước review. Hai task có thể được tạo cùng một thời điểm.

Cursor không duy nhất có thể bỏ sót hoặc lặp bản ghi ở ranh giới trang.

Plan mới sort theo `createdAt` rồi `id` làm tiebreaker.

Tiebreaker là khóa phụ để phân định khi khóa chính bằng nhau.

DTO query biến `limit` thành số, giới hạn từ một đến một trăm.

Status chỉ nhận enum hợp lệ. Sort field đi qua allowlist.

Không đưa tên cột tùy ý từ query string thẳng vào database.

Repository bắt đầu từ collection Task và ghép các điều kiện được phép.

Prisma 8 dùng `orderBy`, `cursor`, `take` và `all` trên collection.

Mình lấy dư một bản ghi so với limit.

Nếu có bản ghi dư, response đặt `hasNext` bằng true và loại nó khỏi items.

`nextCursor` mã hóa cả `createdAt` và `id` của item cuối cùng.

Cursor được ký hoặc kiểm tra schema trước khi dùng.

Client không cần hiểu cấu trúc bên trong, và server không tin chuỗi bất kỳ.

Filter cũng phải tôn trọng ownership.

Member chỉ query task trong scope của mình. Admin có scope rộng hơn theo permission.

Phân trang không được trở thành đường vòng đọc dữ liệu của người khác.

Mình tạo hai task có cùng `createdAt`, rồi chèn một task mới giữa hai lần gọi.

Offset trả một task trùng ở trang hai.

Cursor kép tiếp tục đúng sau cặp giá trị cuối, không lặp và không mất task cũ.

Mình chạy query lớn và xem trace.

Page đầu nhanh. Page sâu bằng cursor không phải đếm rồi bỏ hàng nghìn dòng như offset.

Response chỉ có `items`, `nextCursor` và `hasNext`.

Total count không được tính mặc định nếu UI không thật sự cần.

Một con số “tổng cộng” có thể là query đắt nhất chỉ để trang trí góc màn hình.

Pagination tốt không làm dữ liệu ít đi. Nó làm mỗi request có giới hạn rõ ràng.

Và một API có giới hạn rõ ràng thường sống lâu hơn API cố trả tất cả.

Task đã tải theo phần, nhưng vẫn nằm trong một danh sách phẳng.

Mình thêm `projectId` bắt buộc rồi chạy migration. PostgreSQL từ chối vì task cũ chưa có project.

Xóa database làm demo xanh, nhưng production không có nút quay lại tuổi thơ.

Bước ngoặt là xem migration như quá trình chuyển trạng thái.

Project và Task là một-nhiều. Task và Label là nhiều-nhiều qua `TaskLabel`.

Junction giữ `attachedAt` và `attachedBy`, nên nó là entity thật chứ không phải đường nối vô danh.

Composite key `taskId + labelId` ngăn cùng label bị gắn hai lần.

Label chỉ unique bên trong một Project. Service từ chối gắn Label của project khác.

Xóa Label có thể cascade junction. Xóa Project còn Task thì bị restrict.

AI không thể tự chọn delete policy. Đây là business rule.

Migration đi theo expand, backfill, contract.

Đầu tiên, mình thêm `projectId` nullable. Sau đó tạo Inbox cho từng owner và backfill task cũ.

Khi không còn dòng null, migration tiếp theo mới đặt cột thành bắt buộc.

Mình review foreign key, unique index và delete action trước khi apply.

Query list dùng `select` tối thiểu. Query detail chỉ `include` Project và Label khi màn hình cần.

Task cũ nằm trong Inbox. Task mới chọn Project và gắn Label an toàn.

Nhưng create Task và attach Label vẫn là nhiều write rời.

Tập sau, transaction sẽ biến nhiều write thành một lời hứa duy nhất.

Migration tốt không chỉ làm schema mới đúng. Nó còn đưa dữ liệu cũ sang tương lai nguyên vẹn.

Link Git của nhánh này nằm trong description. Bạn có thể comment phần còn khó hiểu.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | GET `/tasks` trả payload lớn | 25s |
| 2 | [DIAGRAM] | Offset so với cursor kép `createdAt + id` | 35s |
| 3 | [IDE] | Submit yêu cầu; AI plan pagination, host review allowlist | 40s |
| 4 | [IDE] | DTO, ownership filter, `limit + 1` và next cursor | 50s |
| 5 | [TERM] | Timestamp trùng và insert giữa hai page | 40s |
| 6 | [BROWSER] | Load-more ổn định, query page sâu | 35s |
| 7 | [TERM] | Migration fail khi thêm `projectId` bắt buộc | 35s |
| 8 | [DIAGRAM] | Project–Task và TaskLabel explicit junction | 40s |
| 9 | [IDE] | Review composite key, project-scoped label và delete policy | 45s |
| 10 | [DIAGRAM] | Expand → backfill Inbox → contract | 40s |
| 11 | [TERM] | Migration plan, DDL review, apply và verify | 50s |
| 12 | [BROWSER] | Task cũ trong Inbox; task mới có project/labels | 45s |
| 13 | [IDE] | `select` list và `include` detail để tránh N+1 | 35s |
| 14 | [B-ROLL] | Nhiều write rời; teaser transaction | 20s |

**Tổng: 535 giây ≈ 8:55; cộng khoảng nghỉ review thành 9–10 phút.** One Dark Pro, JetBrains Mono 18–20px.

### Code cốt lõi

```ts
const query = db.orm.public.Task
  .where((task) => task.ownerId.eq(scope.ownerId))
  .orderBy([
    (task) => task.createdAt.desc(),
    (task) => task.id.desc(),
  ]);

const page = await (cursor
  ? query.cursor({ createdAt: cursor.createdAt, id: cursor.id })
  : query
).take(limit + 1).all();
```

```ts
const hasNext = page.length > limit;
const items = hasNext ? page.slice(0, limit) : page;
const nextCursor = hasNext ? encodeCursor(items.at(-1)!) : null;
return { items, nextCursor, hasNext };
```

### Prompt cho AI

```text
Plan cursor pagination for the current Prisma 8 TasksRepository.
- Preserve permission and ownership scope before applying client filters.
- Support allowlisted status, owner, due-date and sort inputs.
- Cap limit at 100 and reject malformed cursors.
- Use a stable composite order: createdAt plus id as tiebreaker.
- Use Prisma 8 collection APIs, not Prisma 7 findMany syntax.
- Fetch limit + 1 and return items, nextCursor and hasNext.
- Demonstrate a same-timestamp tie and an insert between page requests.
- Compare offset and cursor behavior with tests and query timing.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right facing an endless dark list of tasks while one precise glowing cursor marks the next position, deep black and navy background, NestJS red-pink #E0234E highlights, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of two dark data timelines, one offset path repeating records and one cursor path continuing cleanly, developer silhouette on the right, NestJS red-pink #E0234E rim light, empty dark left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer watching five thousand task rows compress into small clean pages on a dark monitor, high contrast black and navy scene with NestJS red-pink #E0234E accents, subject right, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Một Migration suýt xóa lịch sử Task — EP17 | Lập trình là cuộc sống
2. Pagination đúng nhưng Schema mới vẫn có thể phá Data — EP17 | Lập trình là cuộc sống
3. Cursor kép và Migration ba bước với Prisma 8 — EP17 | Lập trình là cuộc sống
4. Đừng thêm Foreign Key bắt buộc trong một bước — EP17 | Lập trình là cuộc sống
5. Expand, Backfill, Contract cứu dữ liệu cũ — EP17 | Lập trình là cuộc sống
6. Join Table có lịch sử riêng — EP17 | Lập trình là cuộc sống
7. Vì sao Offset làm Task bị lặp? — EP17 | Lập trình là cuộc sống
8. Project, Label và năm nghìn Task — EP17 | Lập trình là cuộc sống
9. Delete Cascade hay Restrict? AI không thể tự chọn — EP17 | Lập trình là cuộc sống
10. Schema mới phải đưa Data cũ đi cùng — EP17 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1; A/B với Title 5 cho hook migration.

### 4b. SEO Description

```text
Offset nói “bỏ qua hai mươi dòng”. Cursor nói “tiếp tục sau bản ghi này”. Tập 17 xây pagination ổn định cho dữ liệu thay đổi liên tục.

✅ So sánh offset và cursor pagination
✅ Filter theo status, owner và deadline
✅ Allowlist sort field và giới hạn page size
✅ Dùng createdAt + id làm cursor kép
✅ Áp dụng API collection của Prisma 8
✅ Giữ nguyên RBAC và ownership scope
✅ Test insert giữa hai lần tải trang

🔗 Prisma 8 Reading Data: https://docs.prisma.io/docs/orm/fundamentals/reading-data
🔗 Prisma 8 ORM Client: https://docs.prisma.io/docs/orm/v8/reference/orm-client

⏱ 0:00 Năm nghìn task
⏱ 0:40 Offset bắt đầu lặp
⏱ 1:15 Cursor là gì
⏱ 1:50 Vì sao cần tiebreaker
⏱ 2:35 Query DTO và allowlist
⏱ 3:25 Prisma 8 cursor query
⏱ 4:20 Ownership và cursor validation
⏱ 5:15 Demo dữ liệu chèn liên tục

#NestJS #Prisma8 #Pagination #CursorPagination #PostgreSQL #TypeScript #Backend #APIDesign #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
prisma 8 pagination, cursor pagination nestjs, nestjs filtering sorting, offset vs cursor pagination, composite cursor createdAt id, prisma 8 orderBy cursor take, stable pagination postgres, api pagination best practices, list tasks nestjs, pagination ownership rbac, nestjs-base-with-ai nestjs, học nestjs bằng ai, nestjs tập 17, prisma tiếng việt, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `TASK BỊ LẶP` — WHITE `#FFFFFF`
- `VÌ OFFSET` — NEST RED `#E0234E`
- Badge nhỏ: `EP 22`

### Option 2
- `5000 TASK` — WHITE `#FFFFFF`
- `1 CURSOR` — NEST RED `#E0234E`
- Badge nhỏ: `PRISMA 8`

### Option 3
- `ĐỪNG SKIP` — WHITE `#FFFFFF`
- `HÃY CURSOR` — NEST RED `#E0234E`
- Badge nhỏ: `PAGINATION`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
