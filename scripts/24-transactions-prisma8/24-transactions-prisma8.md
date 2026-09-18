# NestJS #24 — Transactions: trọn vẹn hoặc không làm

- **Series:** Học NestJS bằng AI — tập 24/45
- **Target runtime:** khoảng 6 phút 10 giây (563 từ thoại)
- **Outcome:** Create Task và attach Label chạy trong Prisma 8 callback transaction, rollback đúng khi lỗi.
- **Pain tập kế:** Dashboard join nhiều bảng đúng dữ liệu nhưng lặp lại và làm database nặng.

---

## PART 1 — SCRIPT

Task được tạo thành công. Label thứ hai bị trùng và insert thất bại.

API trả lỗi, nhưng database vẫn giữ Task cùng label đầu tiên.

User bấm thử lại và nhận thêm một Task gần giống hệt.

Mỗi câu lệnh riêng lẻ đều đúng. Cả business operation lại sai.

Mình thử cleanup trong `catch`.

Cleanup cũng có thể fail. Và code bắt đầu giống người lau nhà giữa động đất.

Bước ngoặt là database phải nhìn nhiều write như một đơn vị duy nhất.

Transaction là lời hứa: hoặc mọi bước commit, hoặc mọi bước rollback.

Nó không phải bùa chống mọi lỗi đồng thời. Nhưng nó bảo vệ tính nguyên vẹn của một operation.

Mình yêu cầu AI dựng test tái hiện lỗi attach label giữa chừng.

AI dùng `$transaction` theo Prisma 7.

Mình dừng ở bước review. Project này dùng Prisma 8.

API đúng là `db.transaction` với callback, và mọi query phải đi qua `tx.orm`.

Mình đặt transaction boundary trong application service.

Controller không quản lý transaction. Repository đơn lẻ cũng không biết toàn bộ use case.

Service biết create Task và attach các Label phải cùng thành công.

Trong callback, mình tạo Task bằng `tx.orm.public.Task.create`.

Sau đó `TaskLabel.createAll` ghi toàn bộ liên kết.

Callback trả về ID cần thiết. Khi callback kết thúc, transaction mới commit.

Nếu một label không tồn tại hoặc liên kết vi phạm ràng buộc, callback throw.

PostgreSQL rollback cả Task lẫn những junction đã tạo.

Một lỗi rất kín vẫn có thể phá transaction.

Chỉ cần một repository dùng `db.orm` thay vì `tx.orm` bên trong callback.

Query đó chạy trên connection riêng và commit ngay.

Mình truyền transaction context rõ ràng vào các repository tham gia use case.

Type và test phải làm việc dùng nhầm handle trở nên khó hơn.

Sau đó mình tạo hai request đồng thời gắn cùng một Label.

Kiểm tra trước rồi insert không đủ. Cả hai request đều có thể thấy “chưa tồn tại”.

Composite primary key ở database mới là hàng rào cuối.

Một request thành công. Request còn lại nhận conflict có thể giải thích.

Transaction vẫn cần ngắn.

Mình không gọi email, object storage hay API bên ngoài khi đang giữ connection database.

Những việc đó có thể chậm, timeout, hoặc không rollback cùng PostgreSQL.

Sau commit, hệ thống mới phát sự kiện hoặc tạo job nền.

Đây là lý do transaction không giải quyết distributed transaction hộ mình.

Mình bật test failure injection ngay sau Task create.

Callback throw. Query kiểm tra không thấy Task và không thấy TaskLabel.

Mình chạy lại đường thành công. Cả Task và hai Label xuất hiện cùng lúc.

Cuối cùng, hai request đồng thời không tạo liên kết trùng.

Transaction không làm code hết lỗi. Nó làm lỗi không để lại nửa sự thật.

Trong production, dữ liệu nửa đúng thường khó sửa hơn request thất bại rõ ràng.

TaskFlow đã nhất quán, nhưng dashboard đang query cùng một graph liên tục.

Tập sau, Redis sẽ làm nó nhanh hơn, rồi cố tình cho ta thấy cache cũ nguy hiểm thế nào.

Nếu bạn muốn biến nhiều write thành một lời hứa, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERM] | Create task lỗi giữa chừng nhưng DB vẫn còn Task và một junction | 30s |
| 2 | [IDE] | Cho thấy cleanup trong `catch` phình ra và vẫn có failure path | 20s |
| 3 | [DIAGRAM] | Hai write nằm trong một transaction: commit tất cả hoặc rollback | 25s |
| 4 | [BROWSER] | Highlight `$transaction` Prisma 7; đối chiếu Prisma 8 callback API | 25s |
| 5 | [IDE] | Application service mở `db.transaction(async tx => ...)` | 40s |
| 6 | [IDE] | Tạo Task và `TaskLabel.createAll` qua `tx.orm` | 40s |
| 7 | [IDE] | Demo bug repository dùng nhầm `db.orm`; refactor nhận transaction context | 35s |
| 8 | [DIAGRAM] | Hai request đồng thời; unique composite key chặn race | 40s |
| 9 | [DIAGRAM] | Những gì không đặt trong transaction: email, storage, external API | 25s |
| 10 | [TERM] | Failure injection và query xác nhận zero Task/TaskLabel | 35s |
| 11 | [TERM] | Happy path có Task và hai Label; concurrent test xanh | 35s |
| 12 | [B-ROLL] | Commit xanh, cut sang dashboard query lặp lại | 20s |

**Tổng mục tiêu: 6 phút 10 giây.** One Dark Pro, font 18–20px. Hiển thị riêng `db.orm` và `tx.orm` với màu highlight khác nhau.

### Code cốt lõi

```ts
return this.db.transaction(async (tx) => {
  const task = await tx.orm.public.Task.create({
    title: input.title,
    ownerId: actor.id,
    projectId: input.projectId,
  });

  await tx.orm.public.TaskLabel.createAll(
    input.labelIds.map((labelId) => ({
      taskId: task.id,
      labelId,
      attachedBy: actor.id,
    })),
  );

  return task;
});
```

```ts
// Sai: write này nằm ngoài transaction và không rollback.
await this.db.transaction(async (tx) => {
  await this.db.orm.public.Task.create(input);
  throw new Error('forced failure');
});
```

### Prompt cho AI

```text
Reproduce and then fix partial Task creation with Prisma 8 transactions.
- First add a test that fails after Task creation but before all TaskLabel rows exist.
- Use db.transaction(async tx => ...) and Prisma 8 APIs only.
- Route every participating query through tx.orm, never db.orm inside the callback.
- Keep the boundary in the application service that owns the whole use case.
- Rely on database constraints for concurrent duplicate TaskLabel inserts.
- Map the losing concurrent request to a clear conflict response.
- Keep email, object storage and external HTTP calls outside the transaction.
- Do not present isolation-level configuration unless the installed Prisma 8 release supports it.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right watching a database transaction split between a complete green state and a broken half-written red state, dark black and navy environment, NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of several glowing database writes locked inside one transparent atomic capsule, developer silhouette on the right, deep shadows, NestJS red-pink #E0234E rim light, empty dark left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a dark terminal showing a rollback erasing half-created task records, developer face on the right lit by red and white monitor light, black and navy background, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Transaction: Hoặc trọn vẹn, hoặc không làm — EP24 | Lập trình là cuộc sống
2. Một request lỗi để lại nửa dữ liệu — EP24 | Lập trình là cuộc sống
3. Prisma 8 Transaction không còn `$transaction` — EP24 | Lập trình là cuộc sống
4. Vì sao `db.orm` phá rollback? — EP24 | Lập trình là cuộc sống
5. Chặn Race Condition khi gắn Label — EP24 | Lập trình là cuộc sống

**Khuyên dùng:** Title 2. A/B test Title 1 cho chủ đề evergreen.

### 4b. SEO Description

```text
Mỗi câu lệnh có thể đúng nhưng cả business operation vẫn sai. Tập 24 dùng Prisma 8 transaction để Task và Label cùng thành công hoặc cùng rollback.

✅ Đặt transaction boundary ở application service
✅ Dùng db.transaction và tx.orm của Prisma 8
✅ Tái hiện lỗi nửa trạng thái bằng failure injection
✅ Phát hiện bug dùng db.orm bên trong callback
✅ Dùng constraint chống race condition
✅ Giữ external side effect ngoài transaction
✅ Kiểm chứng rollback bằng database thật

🔗 Prisma 8 Transactions: https://docs.prisma.io/docs/orm/fundamentals/transactions
🔗 Prisma 8 Writing Data: https://docs.prisma.io/docs/orm/v8/fundamentals/writing-data

⏱ 0:00 Một Task nửa hoàn thành
⏱ 0:35 Cleanup không đủ
⏱ 1:05 Transaction là gì
⏱ 1:40 Prisma 8 callback transaction
⏱ 2:30 tx.orm và bug db.orm
⏱ 3:25 Race condition và constraint
⏱ 4:20 Giữ transaction ngắn
⏱ 5:15 Rollback test

#NestJS #Prisma8 #Transaction #PostgreSQL #RaceCondition #DataIntegrity #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
prisma 8 transaction, db transaction tx orm, nestjs database transaction, prisma 8 rollback, transaction boundary service, partial write database, race condition postgres, composite key conflict, createAll prisma 8, prisma 7 vs prisma 8 transaction, task label transaction, failure injection test, taskflow nestjs, học nestjs bằng ai, nestjs tập 24, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `NỬA DỮ LIỆU` — WHITE `#FFFFFF`
- `LÀ DỮ LIỆU SAI` — NEST RED `#E0234E`
- Badge nhỏ: `EP 24`

### Option 2
- `TẤT CẢ` — WHITE `#FFFFFF`
- `HOẶC KHÔNG GÌ` — NEST RED `#E0234E`
- Badge nhỏ: `TRANSACTION`

### Option 3
- `ĐỪNG DÙNG` — WHITE `#FFFFFF`
- `DB.ORM Ở ĐÂY` — NEST RED `#E0234E`
- Badge nhỏ: `PRISMA 8`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
