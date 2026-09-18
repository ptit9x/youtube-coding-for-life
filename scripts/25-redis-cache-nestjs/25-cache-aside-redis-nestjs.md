# NestJS #25 — Caching với Redis: học cách quên

- **Series:** Học NestJS bằng AI — tập 25/45
- **Target runtime:** khoảng 6 phút 25 giây (619 từ thoại)
- **Outcome:** Dashboard dùng cache-aside qua Redis, key theo scope và invalidation đúng khi dữ liệu hoặc quyền đổi.
- **Pain tập kế:** Gửi email nhắc deadline trong HTTP request làm user phải chờ mail server.

---

## PART 1 — SCRIPT

Dashboard TaskFlow đúng dữ liệu, nhưng mỗi lần refresh lại join Project, Task và Label.

Query mất gần một giây. Mười tab mở cùng lúc biến database thành máy sưởi.

Mình thêm Redis. Request sau còn vài chục mili giây.

Rồi mình thu hồi quyền của một user.

Dashboard cũ vẫn hiện dữ liệu admin thêm năm phút nữa.

Cache vừa làm hệ thống nhanh hơn, và sai nhanh hơn.

Bước ngoặt là hiểu cache không chỉ cần biết cách nhớ. Nó phải biết lúc nào quên.

Cache-aside là flow đơn giản.

Service hỏi cache trước. Nếu miss, nó đọc database rồi ghi kết quả vào cache.

Database vẫn là nguồn sự thật. Redis chỉ giữ bản sao có thời hạn.

Mình yêu cầu AI đề xuất cache cho mọi GET endpoint.

Plan nghe rất năng suất và rất nguy hiểm.

Không phải dữ liệu nào cũng đáng cache. Dữ liệu theo quyền càng không thể dùng chung một key.

Mình giới hạn scope vào dashboard query nặng và lặp lại.

Key đầu tiên AI tạo là `dashboard`.

Nghĩa là user đầu tiên có thể đổ dữ liệu của mình vào cache cho tất cả người sau.

Mình đổi key thành namespace có version, user ID và access version.

Access version tăng mỗi khi role hoặc permission hiệu lực thay đổi.

Guard đọc version hiện hành cùng permission từ database.

Mình không lấy access version cũ trong JWT để tạo cache key.

Key cũ vẫn tồn tại tới TTL, nhưng không request mới nào chạm vào nó.

Đó là invalidation bằng versioned key.

Với thay đổi task, project hoặc label, service xóa key dashboard liên quan sau khi database commit.

Xóa trước commit có thể tạo race: request khác đọc database cũ rồi cache lại.

TTL vẫn cần thiết như lưới an toàn.

Nhưng TTL không thay thế invalidation khi dữ liệu liên quan đến quyền.

“Chờ năm phút rồi tự đúng” không phải security policy.

Mình cấu hình CacheModule với Redis qua Keyv và URL từ env đã validate.

TTL dùng mili giây. Một nhầm lẫn đơn vị có thể biến một phút thành nhiều giờ.

Trong service, cache miss và cache hit đều được đo.

Hit rate cao chưa chắc tốt nếu key giữ dữ liệu sai hoặc tốn quá nhiều memory.

Sau đó mình cố tình tái hiện bug.

User admin mở dashboard. Redis giữ response có dữ liệu toàn hệ thống.

Mình revoke role nhưng không tăng access version.

Request tiếp theo vẫn hit cache cũ. Test security báo đỏ.

Mình đưa invalidation vào cùng use case thay đổi quyền.

Role bị revoke, access version tăng, request kế tiếp miss cache và query lại scope member.

Dữ liệu admin biến mất ngay.

Mình sửa một task. Dashboard cache bị xóa sau commit và response mới hiện title đã đổi.

Cuối cùng, mình tắt Redis.

Nếu cache lỗi, dashboard có thể chậm hơn nhưng vẫn đọc được database theo policy đã chọn.

Cache là tối ưu, không nên trở thành nguồn sống duy nhất của read path.

Kết quả: latency giảm rõ rệt, database bớt query lặp, revoke vẫn có hiệu lực ngay.

Cache tốt không phải cache giữ được nhiều. Nó là cache quên đúng lúc.

Dashboard đã nhanh. Email nhắc deadline vẫn giữ request chờ một mail server thất thường.

Tập sau, BullMQ sẽ đưa việc nặng ra nền và buộc mình đối mặt với retry cùng duplicate.

Nếu bạn muốn tối ưu mà không bán rẻ tính đúng đắn, hãy đồng hành cùng series này.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Lời thoại / nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Dashboard load chậm; Observe cho thấy query lặp | 25s |
| 2 | [TERM] | Redis cache hit làm latency giảm, rồi revoke quyền nhưng dữ liệu cũ còn | 30s |
| 3 | [DIAGRAM] | Cache-aside: get → miss → DB → set → response | 25s |
| 4 | [BROWSER] | Review đề xuất cache mọi GET và key `dashboard` | 25s |
| 5 | [DIAGRAM] | Key `taskflow:v1:dashboard:userId:accessVersion` | 35s |
| 6 | [IDE] | CacheModule với `createKeyv(REDIS_URL)` và TTL mili giây | 30s |
| 7 | [IDE] | Dashboard service get/miss/set; DB là source of truth | 40s |
| 8 | [DIAGRAM] | Invalidate sau commit; race khi delete trước commit | 30s |
| 9 | [TERM] | Test bug revoke không bump version; thấy cache hit sai | 35s |
| 10 | [IDE] | Sửa access version và invalidation; security test xanh | 40s |
| 11 | [TERM] | Tắt Redis; minh họa fallback về database theo policy | 25s |
| 12 | [BROWSER] | So sánh latency và query count trước/sau | 30s |
| 13 | [B-ROLL] | Redis key biến mất; cut sang request chờ gửi email | 15s |

**Tổng mục tiêu: 6 phút 25 giây.** One Dark Pro, JetBrains Mono 18–20px. Không quay Redis URL hoặc credential; dùng dữ liệu test khi demo quyền.

### Code cốt lõi

```ts
CacheModule.registerAsync({
  imports: [ConfigModule],
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    stores: [createKeyv(config.getOrThrow('REDIS_URL'))],
  }),
});
```

```ts
const key = `taskflow:v1:dashboard:${user.id}:${authz.accessVersion}`;
const cached = await this.cache.get<DashboardView>(key);
if (cached) return cached;

const fresh = await this.dashboardRepository.readFor(user);
await this.cache.set(key, fresh, 60_000);
return fresh;
```

### Prompt cho AI

```text
Plan a narrow cache-aside optimization for the TaskFlow dashboard.
- Use Nest CacheModule with the current Keyv Redis adapter and validated REDIS_URL.
- Keep PostgreSQL as the source of truth.
- Cache only the expensive dashboard read, not every GET route.
- Include user scope and accessVersion in the key namespace.
- Read the current accessVersion from the authorization context, not a stale JWT claim.
- Invalidate task/project/label views after the database commit.
- Increment accessVersion whenever effective roles or permissions change.
- Treat TTL as a safety net, never as authorization invalidation.
- Add hit/miss metrics, a revoke-permission regression test and a Redis-outage test.
- Wait for approval before implementation.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a Vietnamese male developer on the right watching a blazing fast Redis cache return an old forbidden admin dashboard, dark monitor with one red warning, deep black and navy background, NestJS red-pink #E0234E accents, empty left space for headline text, 16:9, photorealistic, no text.`
2. `A cinematic photograph of a glowing Redis memory cube on the right erasing one stale permission key at the exact moment access is revoked, dramatic dark code environment, NestJS red-pink #E0234E rim light, empty left side, 16:9, photorealistic, no text.`
3. `A cinematic photograph of a developer balancing a fast cache path against a truthful PostgreSQL database on a dark monitor, subject right, black and navy scene with NestJS red-pink #E0234E highlights, empty left space, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Cache nhanh nhưng vẫn có thể sai — EP25 | Lập trình là cuộc sống
2. Caching với Redis: Học cách quên — EP25 | Lập trình là cuộc sống
3. Bug Permission cũ còn sống trong Cache — EP25 | Lập trình là cuộc sống
4. Cache-Aside cho NestJS đúng cách — EP25 | Lập trình là cuộc sống
5. TTL không phải Security Policy — EP25 | Lập trình là cuộc sống

**Khuyên dùng:** Title 1. A/B test Title 2 cho search intent.

### 4b. SEO Description

```text
Cache vừa làm hệ thống nhanh hơn, và sai nhanh hơn. Tập 25 dùng Redis theo cache-aside mà vẫn revoke permission có hiệu lực ngay.

✅ Chọn đúng query đáng cache
✅ Dùng CacheModule với Keyv Redis
✅ Thiết kế key theo user và access version
✅ Invalidate sau database commit
✅ Phân biệt TTL với security invalidation
✅ Tái hiện bug quyền cũ còn trong cache
✅ Đo hit rate, latency và fallback khi Redis lỗi

🔗 NestJS Caching: https://docs.nestjs.com/techniques/caching
🔗 Keyv Redis: https://github.com/jaredwray/keyv/tree/main/packages/redis

⏱ 0:00 Dashboard chậm
⏱ 0:35 Cache nhanh nhưng sai
⏱ 1:10 Cache-aside
⏱ 1:45 Key theo permission scope
⏱ 2:30 Redis và TTL
⏱ 3:20 Invalidate sau commit
⏱ 4:15 Bug revoke permission
⏱ 5:20 Redis outage và kết quả

#NestJS #Redis #Caching #CacheAside #Authorization #Performance #TypeScript #Backend #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs redis cache, cache aside nestjs, keyv redis nestjs, cache invalidation permissions, redis stale data bug, nestjs cache manager, versioned cache key, access version rbac, ttl milliseconds cache, redis outage fallback, dashboard cache nestjs, postgres source of truth, taskflow nestjs, học nestjs bằng ai, nestjs tập 25, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `CACHE NHANH` — WHITE `#FFFFFF`
- `NHƯNG SAI` — NEST RED `#E0234E`
- Badge nhỏ: `EP 25`

### Option 2
- `QUYỀN ĐÃ THU HỒI` — WHITE `#FFFFFF`
- `CACHE VẪN NHỚ` — NEST RED `#E0234E`
- Badge nhỏ: `REDIS`

### Option 3
- `HỌC CÁCH` — WHITE `#FFFFFF`
- `QUÊN` — NEST RED `#E0234E`
- Badge nhỏ: `CACHE`

**Typography chung:** Canvas 1280×720. Anton cho headline, JetBrains Mono cho badge. Chữ trái chiếm khoảng một phần ba khung, mỗi dòng cao 110–130px, line spacing 0.85, stroke đen 8px, shadow gọn 8px. Chỉ dùng trắng và NestJS red-pink `#E0234E`; không đặt chữ lên mặt. Tạo chữ trong Canva, giữ ảnh sạch không chữ và kiểm tra preview 320×180.
