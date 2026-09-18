# NestJS #22 — Pagination, Filtering và Sorting với Prisma 8

- **Series:** Học NestJS bằng AI — tập 22/45
- **Target runtime:** khoảng 6 phút 20 giây (581 từ thoại)
- **Outcome:** GET `/tasks` có filter, sort allowlist và cursor ổn định với `createdAt + id`.
- **Pain tập kế:** Task vẫn là danh sách phẳng, chưa thuộc project hay có label.

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

Tập sau, mình sẽ thêm Project, Label và migration an toàn cho dữ liệu đang tồn tại.

Nếu bạn muốn hiểu query thay vì copy pagination snippet, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | GET `/tasks` trả payload lớn; DevTools cho thấy kích thước và thời gian | 30s |
| 2 | [DIAGRAM] | Offset “bỏ N dòng” so với cursor “sau bản ghi X” | 30s |
| 3 | [BROWSER] | Highlight cursor chỉ có `createdAt`; tạo phản ví dụ timestamp trùng | 25s |
| 4 | [IDE] | `ListTasksQueryDto`: limit, status, owner, sort allowlist | 35s |
| 5 | [IDE] | Repository compose filter và ownership scope | 35s |
| 6 | [IDE] | Prisma 8 `orderBy([createdAt, id]).cursor().take().all()` | 40s |
| 7 | [IDE] | Lấy `limit + 1`, tạo `hasNext` và `nextCursor` | 35s |
| 8 | [TERM] | Seed hai task cùng timestamp; chèn task giữa hai request | 35s |
| 9 | [DIAGRAM] | So sánh kết quả offset bị lặp với cursor kép ổn định | 40s |
| 10 | [BROWSER] | UI load-more với filter status và sort | 30s |
| 11 | [BROWSER] | Observe trace hoặc query timing cho page đầu và page sâu | 25s |
| 12 | [B-ROLL] | Danh sách mượt; chuyển sang task được kéo vào các project | 20s |

**Tổng mục tiêu: 6 phút 20 giây.** One Dark Pro, JetBrains Mono 18–20px. Zoom đủ lớn để thấy thứ tự `createdAt` và `id`.

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

1. Pagination sai làm Task bị lặp — EP22 | Lập trình là cuộc sống
2. Cursor Pagination với Prisma 8 — EP22 | Lập trình là cuộc sống
3. Vì sao Offset chậm dần theo từng trang? — EP22 | Lập trình là cuộc sống
4. Năm nghìn Task và một Cursor ổn định — EP22 | Lập trình là cuộc sống
5. Filtering, Sorting, Pagination cho NestJS — EP22 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1. A/B test Title 2 cho intent kỹ thuật.

### 4b. SEO Description

```text
Offset nói “bỏ qua hai mươi dòng”. Cursor nói “tiếp tục sau bản ghi này”. Tập 22 xây pagination ổn định cho dữ liệu thay đổi liên tục.

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
prisma 8 pagination, cursor pagination nestjs, nestjs filtering sorting, offset vs cursor pagination, composite cursor createdAt id, prisma 8 orderBy cursor take, stable pagination postgres, api pagination best practices, list tasks nestjs, pagination ownership rbac, taskflow nestjs, học nestjs bằng ai, nestjs tập 22, prisma tiếng việt, typescript backend, lập trình là cuộc sống
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
