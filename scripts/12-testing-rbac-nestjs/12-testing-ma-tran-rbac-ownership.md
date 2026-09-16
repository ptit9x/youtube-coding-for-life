# NestJS #12 — Testing phân quyền bằng Jest và Supertest

- **Series:** Học NestJS bằng AI — tập 12/45
- **Target runtime:** ~14 phút
- **Outcome:** Unit test, integration test và e2e bảo vệ auth, RBAC, ownership.
- **Pain mở EP13:** Test làm duplication lộ rõ và tạo cám dỗ refactor quá tay.

---

## PART 1 — SCRIPT

Terminal báo coverage 100%. Mình đảo PermissionGuard để người thiếu quyền được đi qua, nhưng toàn bộ test vẫn xanh.

Con số đẹp vừa bỏ lọt một bug bảo mật.

EP11 kết thúc với ba request màu xanh và đỏ đúng như mong đợi.

Không ai nhớ thử lại mọi role, permission và owner sau mỗi lần sửa code.

Security không được kiểm tra bằng niềm tin. Nó cần một ma trận có thể chạy lại.

Mình chưa mở Jest ngay. Trước hết, mình liệt kê các nhánh quan trọng.

Không token phải trả 401. Thiếu permission trả 403. Đúng owner thành công, còn sai owner bị chặn.

Permission trùng qua hai role chỉ có một hiệu lực. Revoke phải mất quyền, còn direct DENY phải thắng role.

Ma trận là specification nhỏ. Nó cho AI biết hành vi cần bảo vệ.

Nếu dự án không dùng direct override, bỏ hai ca ALLOW và DENY.

Test không nên bảo vệ feature chưa tồn tại.

Không phải mọi test đều cần khởi động toàn bộ ứng dụng.

Unit test kiểm tra một class với dependency giả.

Integration test kiểm tra repository với database test thật.

E2E test đi từ HTTP tới database và quay về response.

PermissionGuard phù hợp với unit test. Prisma repository cần integration test.

Luồng login rồi sửa task phù hợp với e2e.

Kim tự tháp này giúp bộ test vừa nhanh, vừa đủ niềm tin.

Mình đưa ma trận cho AI và yêu cầu sinh unit test đầu tiên.

AI tạo một test như sau.

Nó chỉ kiểm tra `response.status` có tồn tại.

Test chạy xanh. Nhưng 200, 403 hay 500 đều làm nó xanh.

Mình thử mutation nhỏ trong guard.

Mình đảo nhánh thiếu quyền thành `return true`.

Đây là bug nghiêm trọng. Bộ test vẫn xanh toàn bộ.

Coverage có thể cao, nhưng assertion không chứng minh đúng hành vi.

Mình sửa test để nó nói đúng điều cần bảo vệ.

User A patch task của User B phải nhận 403.

Sau đó, mình đọc lại task từ database.

Đọc lại database phải thấy title vẫn là `Original`.

Status đúng chưa đủ. Side effect cũng phải đúng.

Với create, hãy kiểm tra owner lấy từ token chứ không từ payload.

Với revoke, hãy dùng lại access token cũ để xác nhận quyền biến mất.

E2E dùng database riêng, không dùng database development.

Mỗi test tự tạo dữ liệu cần thiết. Test không phụ thuộc thứ tự chạy.

`DATABASE_URL` của test phải trỏ tới database `taskflow_test` độc lập.

Trước suite, chạy migration. Trước mỗi test, dọn các bảng theo thứ tự quan hệ.

Không dùng production secret. Không copy dữ liệu thật vào test.

Repository integration test xác nhận unique constraint và transaction.

Mock Prisma không thể chứng minh database thật xử lý đúng những điều đó.

Mình trả guard về code đúng. Test đỏ chuyển thành xanh.

Sau đó, mình thử phá ownership rule. Ca sai owner lập tức đỏ.

Giờ mỗi thay đổi authorization đều có lưới an toàn.

Coverage giúp tìm vùng chưa chạy. Nó không đo chất lượng assertion.

Một test tốt phải thất bại khi behavior quan trọng bị phá.

Trong lúc viết test, ba service lộ ra nhiều method giống tên nhau.

AI đề nghị gom chúng vào `BaseCrudService` để giảm code.

Nghe rất DRY, nhưng đó có thể là một chiếc bẫy.

Tập sau, ta refactor bằng bằng chứng thay vì cảm giác. Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [BROWSER] | Chuỗi request thủ công khó lặp lại | 35s |
| 2 | [DIAGRAM] | Ma trận auth, permission và ownership | 75s |
| 3 | [DIAGRAM] | Unit, integration và e2e theo ranh giới | 60s |
| 4 | [AI] | AI sinh assertion `toBeDefined` | 60s |
| 5 | [IDE] | Mutation guard nhưng test vẫn xanh | 80s |
| 6 | [IDE] | Host viết assertion status và side effect | 100s |
| 7 | [IDE] | Test revoke bằng access token cũ | 75s |
| 8 | [TERMINAL] | Chạy database test độc lập | 80s |
| 9 | [IDE] | Phá ownership rule và nhìn test đỏ | 70s |
| 10 | [DIAGRAM] | Coverage khác chất lượng assertion | 45s |
| 11 | [B-ROLL] | BaseCrudService xuất hiện như chiếc bẫy | 30s |

**Tổng: 710 giây ≈ 11:50.** Dành thêm hai phút giải thích output Jest; font tối thiểu 18px.

### Code cốt lõi

```ts
it('forbids updating another user task', async () => {
  await request(app.getHttpServer())
    .patch(`/tasks/${otherTask.id}`)
    .set('Authorization', `Bearer ${userAToken}`)
    .send({ title: 'Hacked' })
    .expect(403);

  const saved = await prisma.task.findUniqueOrThrow({
    where: { id: otherTask.id },
  });
  expect(saved.title).toBe('Original');
});
```

```ts
it('applies a revoked permission immediately', async () => {
  await revokePermissionFromRole(memberRole.id, 'tasks.update');
  await request(app.getHttpServer())
    .patch(`/tasks/${ownTask.id}`)
    .set('Authorization', `Bearer ${existingAccessToken}`)
    .send({ title: 'Blocked' })
    .expect(403);
});
```

### Prompt cho AI

```text
Create a test plan from this authorization matrix before writing code.
Separate unit, repository integration and HTTP e2e tests.
Every test must assert exact status, response shape and important side effects.
Include missing role, duplicate permission, revoke, wrong owner and direct DENY.
Use an isolated test database.
Do not mock behavior that belongs to PostgreSQL.
Show how one deliberate mutation proves each security test is meaningful.
```

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic red security test matrix turning green row by row on a dark monitor, developer watching closely, neon code reflections, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic broken permission guard caught by a glowing Jest safety net, dark server room, red alert and neon green tests, cinematic lighting, 16:9, photorealistic, no text.`
3. `A cinematic close-up of a developer pressing one key as dozens of authorization paths light up, dark IDE, green and red nodes, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. Testing phân quyền NestJS bằng Jest và Supertest — EP12 | Lập trình là cuộc sống
2. Viết E2E Test cho RBAC và Ownership — EP12 | Lập trình là cuộc sống
3. Test PermissionGuard trong NestJS — EP12 | Lập trình là cuộc sống
4. Unit Test, Integration Test và E2E khác nhau thế nào? — EP12 | Lập trình là cuộc sống
5. Vì sao coverage cao vẫn chưa đủ? — EP12 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test thêm Title 2 cho outcome và Title 5 cho curiosity dễ hiểu.

### 4b. SEO Description

```text
Coverage 100% vẫn có thể bỏ lọt bug authorization. Tập này biến auth, RBAC và ownership thành ma trận test chạy lại được.

✅ Vẽ authorization test matrix
✅ Chia unit, integration và e2e test
✅ Dùng Jest và Supertest
✅ Assert status lẫn database side effect
✅ Test revoke với access token cũ
✅ Cô lập PostgreSQL dành cho test
✅ Dùng mutation để kiểm tra chất lượng test

⏱ 0:00 Postman không phải bằng chứng
⏱ 1:10 Vẽ ma trận quyền
⏱ 3:00 Chọn đúng loại test
⏱ 4:30 Test xanh nhưng vô dụng
⏱ 6:20 Assertion có giá trị
⏱ 8:45 Database test độc lập
⏱ 10:40 Mutation và payoff

#NestJS #Jest #Supertest #Testing #RBAC #Authorization #Prisma #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
nestjs testing, jest nestjs, supertest nestjs, rbac testing, authorization test matrix, permission guard test, ownership testing, prisma integration test, e2e nestjs, test coverage, mutation testing, nestjs tiếng việt, nestjs tập 12, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `COVERAGE 100%` — WHITE
- `VẪN LỌT BUG` — RED `#FF3B30`
### Option 2
- `ĐỪNG TIN` — WHITE
- `POSTMAN` — NEON GREEN `#00FF41`
### Option 3
- `TEST MA TRẬN` — NEON GREEN `#00FF41`
- `KHÓA LỖI QUYỀN` — WHITE

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
