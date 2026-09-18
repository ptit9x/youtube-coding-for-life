# NestJS #26 — BullMQ: việc nặng để sau

- **Series:** Học NestJS bằng AI — tập 26/45, kết Season 2
- **Target runtime:** khoảng 7 phút (680 từ thoại)
- **Outcome:** HTTP enqueue email nhanh, worker retry/backoff, final failure vào dead-letter flow và job idempotent cơ bản.
- **Pain mở Season 3:** Queue có worker nhưng chưa ai tự tạo job nhắc deadline mỗi sáng.

---

## PART 1 — SCRIPT

User tạo task trong hai trăm mili giây, rồi phải chờ mail server thêm bốn giây.

Nếu mail timeout, cả request trả lỗi dù Task đã được lưu.

User bấm lại. Task trùng, mail có thể gửi hai lần.

Mình vừa buộc một việc quan trọng chờ một việc chậm và thất thường.

Thêm timeout chỉ giúp thất bại sớm hơn.

Retry ngay trong request lại bắt user ngồi xem backend kiên trì.

Bước ngoặt là tách “Task đã được tạo” khỏi “email sẽ được gửi”.

Queue là hàng chờ bền vững. Producer thêm job, worker xử lý khi có khả năng.

BullMQ dùng Redis để giữ job và trạng thái của nó.

HTTP request trở thành producer. Mail processor trở thành worker.

Mình yêu cầu AI lập plan gửi reminder bằng `setTimeout` trong process.

Plan chạy được cho tới khi container restart.

Timer trong memory biến mất, và nhiều instance có thể tạo nhiều timer giống nhau.

Mình đổi plan sang `@nestjs/bullmq`, retry có backoff và worker tách trách nhiệm.

Backoff là khoảng chờ tăng dần giữa các lần thử, để dependency có thời gian hồi phục.

`BullModule` kết nối Redis bằng config đã validate và đăng ký queue `notifications`.

Sau khi Task commit, service thêm job `task.reminder` với payload nhỏ.

Database commit và `queue.add` vẫn chưa phải một transaction.

Process chết giữa hai bước có thể làm reminder bị mất.

Mình ghi rõ khoảng trống này và thêm reconciliation. Hệ thống chặt hơn cần transactional outbox.

Payload chỉ có notification ID, task ID và recipient ID.

Không nhét access token, password hay toàn bộ user record vào Redis.

Producer đặt bốn attempts và exponential backoff.

Worker kế thừa `WorkerHost` và route theo `job.name`.

BullMQ không dùng `@Process('name')` như Bull cũ.

Đây là một khác biệt nhỏ đủ khiến snippet cũ nằm im mà chẳng xử lý gì.

Mình tắt mail server ngay trước lần chạy đầu.

Job fail, chờ một giây, rồi thử lại với khoảng chờ dài hơn.

HTTP response ban đầu vẫn đã trả hai-không-một. Task không bị tạo lại.

Sau bốn lần thất bại, job không nên biến mất.

Listener ghi failed reason, attempts, job ID và correlation context.

Final failure được đưa vào dead-letter queue để điều tra hoặc replay có kiểm soát.

Dead-letter không phải thùng rác. Nó là phòng chờ cho lỗi cần con người quyết định.

Retry tạo ra câu hỏi khó hơn.

Email có thể đã gửi, nhưng worker chết trước khi đánh dấu complete.

Job sẽ chạy lại. Nếu handler không idempotent, user nhận hai email.

Idempotent nghĩa là chạy lại vẫn cho cùng một kết quả cuối.

Mình tạo notification ID ổn định và truyền nó làm idempotency key cho mail provider.

Database giữ trạng thái delivery với unique key.

Custom job ID giúp chặn hai job đang tồn tại cùng đại diện cho một notification.

Nó hỗ trợ dedupe, nhưng không tự tạo bảo đảm exactly-once.

Production thực tế thường là at-least-once. Handler phải chịu được việc chạy lại.

Mình bật mail server trước lần retry thứ ba.

Job hoàn tất. Delivery chỉ có một record sent và user nhận một email.

Sau đó mình replay một job dead-letter bằng notification ID cũ.

Provider nhận cùng idempotency key và không gửi trùng.

Observe hiển thị trace của worker riêng với thời gian, log và lỗi mail.

Mình đặt cảnh báo khi failed count tăng hoặc queue lag kéo dài.

Kết Season 2, TaskFlow có docs, security header, rate limit, log, trace và upload an toàn.

Nó có pagination, quan hệ, transaction, cache và background job.

Production không phải nơi code hoàn hảo. Nó là nơi failure được dự đoán và giới hạn.

Queue đã có worker, nhưng chưa ai tự tạo reminder mỗi sáng.

Season 3 sẽ bắt đầu bằng cron job, rồi đi tiếp tới realtime và nhiều server.

Nếu bạn đã đi tới đây, hãy thử tắt dependency trong chính project của mình.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | POST task chờ bốn giây rồi timeout do mail server | 30s |
| 2 | [DIAGRAM] | Tách synchronous request thành producer → Redis → worker → mail | 30s |
| 3 | [BROWSER] | Review plan `setTimeout`; mô phỏng container restart và nhiều instance | 25s |
| 4 | [IDE] | `BullModule.forRootAsync` và register queue `notifications` | 35s |
| 5 | [IDE] | Producer thêm job payload nhỏ, attempts và exponential backoff | 35s |
| 6 | [IDE] | `@Processor` + `WorkerHost`; switch theo `job.name` | 35s |
| 7 | [TERM] | Tắt mail server; HTTP vẫn 201; job retry với backoff | 40s |
| 8 | [IDE] | Final failure listener và dead-letter flow | 30s |
| 9 | [DIAGRAM] | Worker chết sau khi mail gửi; giải thích at-least-once và duplicate | 30s |
| 10 | [IDE] | Notification ID, unique delivery record, provider idempotency key | 30s |
| 11 | [TERM] | Bật mail ở retry ba; job complete, chỉ một email | 30s |
| 12 | [BROWSER] | Observe job trace, failed count và queue lag | 30s |
| 13 | [B-ROLL] | Recap EP17–26, mỗi tập 2–3 giây | 25s |
| 14 | [B-ROLL] | Worker chờ job; calendar sáng lên mở Season 3 | 15s |

**Tổng mục tiêu: 7 phút.** One Dark Pro, JetBrains Mono 18–20px. Che Redis URL, email thật và provider credential; dùng mail sandbox.

### Code cốt lõi

```ts
await this.notificationsQueue.add(
  'task.reminder',
  { notificationId, taskId, recipientId },
  {
    jobId: `task-reminder-${notificationId}`,
    attempts: 4,
    backoff: { type: 'exponential', delay: 1_000 },
    removeOnComplete: 1_000,
    removeOnFail: false,
  },
);
```

```ts
@Processor('notifications')
export class NotificationsProcessor extends WorkerHost {
  async process(job: Job<ReminderJob>) {
    switch (job.name) {
      case 'task.reminder':
        return this.mailer.sendReminder(job.data, {
          idempotencyKey: job.data.notificationId,
        });
      default:
        throw new Error(`Unsupported job: ${job.name}`);
    }
  }
}
```

### Prompt cho AI

```text
Plan resilient Task reminder delivery with @nestjs/bullmq.
- Keep Task creation synchronous and enqueue only after its database transaction commits.
- Document the commit-to-enqueue failure gap; add reconciliation or a transactional outbox when delivery must be guaranteed.
- Use a small payload with stable notificationId, taskId and recipientId; no secrets or full records.
- Configure attempts and exponential backoff, then define final-failure handling.
- Implement a WorkerHost processor and switch on job.name; do not use Bull's old @Process decorator.
- Add a dead-letter flow with explicit replay rules and audit logs.
- Make the external email side effect idempotent with a stable provider idempotency key and unique delivery record.
- Explain that custom jobId is deduplication, not exactly-once delivery.
- Test mail outage, retry recovery, worker restart, duplicate enqueue and final failure.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right watching a fast API response split from a long glowing background job queue, dark black and navy environment, NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of an email job failing, retrying along an exponential staircase, then turning green on a dark monitor, developer face on the right, NestJS red-pink #E0234E rim light, empty dark left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a resilient worker pulling glowing jobs from Redis while one failed job moves into a sealed dead-letter chamber, subject on the right, deep shadows and NestJS red-pink #E0234E highlights, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. BullMQ: Việc nặng để sau — EP26 | Lập trình là cuộc sống
2. Mail server chết, API vẫn phải sống — EP26 | Lập trình là cuộc sống
3. Retry có thể gửi Email hai lần — EP26 | Lập trình là cuộc sống
4. Background Jobs trong NestJS đúng cách — EP26 | Lập trình là cuộc sống
5. Queue, Backoff và Dead Letter với BullMQ — EP26 | Lập trình là cuộc sống

**Khuyên dùng:** Title 2. A/B test Title 1 cho search intent và nhận diện BullMQ.

### 4b. SEO Description

```text
Task đã lưu nhưng mail timeout khiến cả request thất bại. Tập 26 đưa việc chậm ra BullMQ và thiết kế worker chịu được retry.

✅ Tách producer và worker bằng Redis queue
✅ Dùng @nestjs/bullmq và WorkerHost
✅ Retry với exponential backoff
✅ Theo dõi final failure bằng dead-letter flow
✅ Thiết kế job payload không chứa secret
✅ Hiểu at-least-once và duplicate side effect
✅ Dùng idempotency key để không gửi mail hai lần
✅ Recap toàn bộ Season 2 production

🔗 NestJS Queues: https://docs.nestjs.com/techniques/queues
🔗 BullMQ Idempotent Jobs: https://docs.bullmq.io/patterns/idempotent-jobs

⏱ 0:00 Request chờ mail server
⏱ 0:35 Queue tách hai trách nhiệm
⏱ 1:15 Vì sao setTimeout không đủ
⏱ 1:50 BullMQ producer và worker
⏱ 2:55 Retry và backoff
⏱ 3:45 Dead-letter flow
⏱ 4:30 Idempotency và duplicate
⏱ 5:35 Failure test
⏱ 6:20 Recap Season 2

#NestJS #BullMQ #BackgroundJobs #Redis #Queue #Retry #Idempotency #TypeScript #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs bullmq, background jobs nestjs, bullmq retry backoff, nestjs queue redis, workerhost nestjs, bullmq idempotent job, duplicate email prevention, dead letter queue bullmq, at least once delivery, job id bullmq deduplication, mail retry nestjs, queue observability, taskflow nestjs, học nestjs bằng ai, nestjs tập 26, typescript backend, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `MAIL CHẾT` — WHITE `#FFFFFF`
- `API VẪN SỐNG` — NEST RED `#E0234E`
- Badge nhỏ: `EP 26`

### Option 2
- `VIỆC NẶNG` — WHITE `#FFFFFF`
- `ĐỂ SAU` — NEST RED `#E0234E`
- Badge nhỏ: `BULLMQ`

### Option 3
- `RETRY =` — WHITE `#FFFFFF`
- `GỬI 2 LẦN?` — NEST RED `#E0234E`
- Badge nhỏ: `QUEUE`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
