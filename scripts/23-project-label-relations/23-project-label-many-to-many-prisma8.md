# NestJS #23 — Project, Label và quan hệ dữ liệu với Prisma 8

- **Series:** Học NestJS bằng AI — tập 23/45
- **Target runtime:** khoảng 6 phút 35 giây (618 từ thoại)
- **Outcome:** Task thuộc Project, gắn nhiều Label qua explicit junction và dữ liệu cũ được migrate an toàn.
- **Pain tập kế:** Tạo task thành công nhưng attach label thất bại để lại nửa trạng thái.

---

## PART 1 — SCRIPT

TaskFlow phân trang được năm nghìn task, nhưng tất cả vẫn nằm trong một danh sách phẳng.

Không có Project. Không có Label. Chỉ có title và hy vọng.

Mình thêm `projectId` bắt buộc vào Task rồi chạy migration.

PostgreSQL từ chối. Những task cũ không biết mình thuộc project nào.

Schema mới hợp lý cho ngày mai, nhưng dữ liệu hôm qua vẫn đang tồn tại.

Xóa sạch database sẽ làm demo xanh rất nhanh.

Production thật không cho mình nút quay lại tuổi thơ như vậy.

Bước ngoặt là xem migration như một quá trình chuyển trạng thái, không phải một lệnh đổi schema.

Project và Task là quan hệ một-nhiều.

Một Project có nhiều Task. Mỗi Task giữ khóa ngoại `projectId`.

Task và Label là nhiều-nhiều.

Mỗi bên có thể kết nối với nhiều bản ghi bên kia, nên cần một bảng nối.

Mình yêu cầu AI thiết kế contract và migration plan trước.

AI đề xuất implicit many-to-many như Prisma cũ.

Mình kiểm tra tài liệu Prisma 8. Kiểu quan hệ đó chưa được hỗ trợ.

Và TaskLabel còn cần `attachedAt` cùng `attachedBy`.

Explicit junction không phải code thừa. Nó là nơi mối quan hệ có lịch sử riêng.

Mình tạo model `Project`, `Label` và `TaskLabel` với composite primary key.

Khóa kép `taskId + labelId` ngăn cùng một label bị gắn hai lần.

Label thuộc một Project và tên chỉ duy nhất bên trong Project đó.

Service từ chối nối Task với Label của Project khác.

Sau đó tới quyết định khó hơn: xóa dữ liệu cha sẽ làm gì.

Xóa Label có thể cascade qua TaskLabel vì liên kết đó không còn ý nghĩa.

Xóa Project thì mình chọn restrict nếu vẫn còn Task.

Một cú delete project không nên âm thầm kéo theo hàng nghìn task.

AI không thể tự chọn policy này. Đây là business rule.

Migration cho `projectId` đi theo hai bước.

Đầu tiên, mình thêm cột nullable và tạo một Project tên Inbox cho từng owner.

Một script backfill gán task cũ vào đúng Inbox.

Mình kiểm tra không còn dòng null, rồi migration sau mới đặt `projectId` thành bắt buộc.

Đó là expand, backfill, contract.

Tạm mở rộng để code cũ và mới cùng sống. Di chuyển dữ liệu. Cuối cùng siết ràng buộc.

Với Prisma 8, mình emit contract rồi chạy `migration plan`.

Plan là bản nháp cần review, không phải lời tiên tri.

Mình đọc từng operation, đặc biệt foreign key, unique index và delete action.

Nếu plan đòi drop cột ngoài ý muốn, quy trình dừng ở đây.

Sau khi approve, migration được apply và `db verify` xác nhận database khớp contract.

Query detail dùng `include` chỉ khi màn hình cần Project và Label.

Query list dùng `select` tối thiểu để không kéo cả graph dữ liệu.

Mình tránh vòng lặp query từng label. Một include đúng chỗ tốt hơn N cộng một query.

Cuối cùng, task cũ đều nằm trong Inbox.

Task mới chọn được Project và gắn hai Label.

Xóa Label dọn đúng junction. Xóa Project còn Task bị từ chối rõ ràng.

Quan hệ dữ liệu không chỉ nối các bảng. Nó quyết định điều gì được phép biến mất cùng nhau.

Nhưng create Task và attach Label hiện vẫn là nhiều write riêng.

Nếu write cuối fail, hệ thống sẽ còn một nửa câu chuyện.

Tập sau, transaction sẽ biến nhiều write thành một lời hứa duy nhất.

Nếu bạn muốn thiết kế dữ liệu mà không xóa lịch sử, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Danh sách task phẳng; filter nhưng không có project/label | 25s |
| 2 | [TERM] | Migration thêm `projectId NOT NULL` thất bại trên dữ liệu cũ | 25s |
| 3 | [DIAGRAM] | Vẽ Project 1–N Task và Task N–N Label qua TaskLabel | 35s |
| 4 | [BROWSER] | Highlight đề xuất implicit N–N; đối chiếu docs Prisma 8 | 25s |
| 5 | [IDE] | Viết `Project`, `Label`, `TaskLabel`, composite key và metadata | 40s |
| 6 | [DIAGRAM] | So sánh cascade TaskLabel với restrict Project còn Task | 30s |
| 7 | [DIAGRAM] | Expand → backfill Inbox theo owner → contract NOT NULL | 45s |
| 8 | [TERM] | `contract emit`, `migration plan`; review operation và DDL | 40s |
| 9 | [TERM] | Apply migration, query null count, chạy `db verify` | 30s |
| 10 | [IDE] | So sánh `include` detail và `select` list; tránh N+1 | 35s |
| 11 | [BROWSER] | Task cũ trong Inbox; task mới có hai label | 25s |
| 12 | [TERM] | Test delete Label cascade junction và Project restrict | 25s |
| 13 | [B-ROLL] | Project board hoàn chỉnh; mô phỏng attach label fail | 15s |

**Tổng mục tiêu: 6 phút 35 giây.** One Dark Pro, JetBrains Mono 18–20px. Khi quay migration, zoom foreign key và delete action thay vì cuộn toàn file.

### Code cốt lõi

```prisma
model Project {
  id      String @id @default(cuid(2))
  name    String
  ownerId String
  tasks   Task[]
  labels  Label[]
}

model Label {
  id        String      @id @default(cuid(2))
  name      String
  projectId String
  project   Project     @relation(fields: [projectId], references: [id], onDelete: Restrict)
  tasks     TaskLabel[]

  @@unique([projectId, name])
}

model TaskLabel {
  taskId     String
  labelId    String
  attachedAt DateTime @default(now())
  attachedBy String
  task        Task  @relation(fields: [taskId], references: [id], onDelete: Cascade)
  label       Label @relation(fields: [labelId], references: [id], onDelete: Cascade)

  @@id([taskId, labelId])
}
```

```bash
npx prisma contract emit
npx prisma migration plan --name add-projects-and-labels
npx prisma db migrate --advance-ref db
npx prisma db verify
```

### Prompt cho AI

```text
Plan Project and Label relations for the populated Prisma 8 TaskFlow database.
- Model Project 1:N Task and Task N:N Label with an explicit TaskLabel junction.
- Scope labels to one project and reject cross-project TaskLabel links.
- Store attachedAt and attachedBy on the junction with a composite primary key.
- Ask for the business meaning of cascade versus restrict before choosing delete actions.
- Use expand, backfill and contract for the new required task.projectId.
- Create one Inbox project per owner and prove every existing task is assigned before NOT NULL.
- Emit the contract, plan migrations and show every destructive or locking operation for review.
- Use Prisma 8 include/select APIs and avoid N+1 queries.
- Add relation and deletion-policy tests.
- Wait for approval before each migration apply step.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right facing a chaotic flat wall of task cards that reorganizes into projects and colored labels, dark navy and black background, NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of glowing database nodes Project, Task and Label connected through one precise junction on a dark monitor, developer face reflected on the right, NestJS red-pink #E0234E rim light, empty dark left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer stopping a dangerous database migration before it drops old task data, dramatic red warning on a dark terminal, subject right, black and navy environment, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Thêm quan hệ mà không xóa dữ liệu cũ — EP23 | Lập trình là cuộc sống
2. Project, Label và Many-to-Many với Prisma 8 — EP23 | Lập trình là cuộc sống
3. Một migration suýt xóa lịch sử TaskFlow — EP23 | Lập trình là cuộc sống
4. Cascade hay Restrict: AI không thể chọn hộ — EP23 | Lập trình là cuộc sống
5. Expand, Backfill, Contract trong PostgreSQL — EP23 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1. A/B test Title 2 cho search intent.

### 4b. SEO Description

```text
Schema mới có thể đúng cho ngày mai nhưng phá dữ liệu hôm qua. Tập 23 thêm Project, Label và quan hệ nhiều-nhiều mà không reset database.

✅ Phân biệt quan hệ 1-N và N-N
✅ Dùng explicit junction trong Prisma 8
✅ Lưu metadata trên TaskLabel
✅ Chọn cascade và restrict theo business rule
✅ Migrate cột bắt buộc bằng expand-backfill-contract
✅ Review migration package trước khi apply
✅ Dùng include/select đúng nhu cầu và tránh N+1

🔗 Prisma 8 Relations: https://docs.prisma.io/docs/orm/v8/fundamentals/relations-and-joins
🔗 Prisma 8 Relational Modeling: https://docs.prisma.io/docs/orm/v8/data-modeling/relational-databases

⏱ 0:00 Danh sách task phẳng
⏱ 0:35 Migration thất bại
⏱ 1:05 Quan hệ 1-N và N-N
⏱ 1:45 Explicit junction
⏱ 2:35 Cascade hay restrict
⏱ 3:20 Expand, backfill, contract
⏱ 4:30 Review migration Prisma 8
⏱ 5:35 Query và kiểm chứng

#NestJS #Prisma8 #PostgreSQL #DatabaseMigration #ManyToMany #DataModeling #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
prisma 8 relations, prisma 8 many to many, explicit junction prisma 8, nestjs project label task, postgres safe migration, expand backfill contract, cascade vs restrict database, prisma migration plan, prisma db verify, composite key task label, avoid n+1 prisma, populated database migration, taskflow nestjs, học nestjs bằng ai, nestjs tập 23, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `ĐỪNG RESET` — WHITE `#FFFFFF`
- `DATABASE` — NEST RED `#E0234E`
- Badge nhỏ: `EP 23`

### Option 2
- `TASK + LABEL` — WHITE `#FFFFFF`
- `NHIỀU - NHIỀU` — NEST RED `#E0234E`
- Badge nhỏ: `PRISMA 8`

### Option 3
- `MIGRATION` — WHITE `#FFFFFF`
- `KHÔNG MẤT DATA` — NEST RED `#E0234E`
- Badge nhỏ: `SAFE`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
