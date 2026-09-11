# Series Plan — "Học NestJS bằng AI" (30 tập, lane: Học lập trình bằng LLM)

- **Format:** 30 video × 8–10 phút. Host tự quay màn hình + tự thoại âm.
- **AI tool:** **Opus trong IDE Antigravity** (agent panel đọc codebase thật). Pattern: hỏi – đọc – chất vấn – verify.
- **Spine:** build MỘT project thật từ đầu đến cuối — **TaskFlow**, task manager API — từ folder rỗng đến hệ thống production có realtime, queue, CI/CD. Hết series = 1 project "điệu nghệ" + Fresher hiểu từng dòng.
- **Chain rule:** tập sau mở bằng NỖI ĐAU tập trước tạo ra (không phải "hôm nay ta học X"). Dưới đây mỗi tập ghi rõ "← pain" kế thừa.
- **Differentiator:** mỗi tập đúng MỘT "Khoảnh khắc AI" — theo **AI-Driven Development Workflow 6 bước: Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng**. Không bao giờ copy-blind.

## SEASON 1 — NỀN TẢNG (EP 01–10): từ số 0 đến API công khai

### EP 01 — Học NestJS từ số 0 cùng AI ✅ (kịch bản đã có)
- ← pain: repo công ty lạ hoắc, tutorial 3h lỗi thời.
- Học: Nest CLI, cấu trúc src, Module/Controller/Service (metaphor bữa tiệc), `nest g resource`, DTO, DI cơ bản, Postman 201.
- AI moment: prompt "giải thích project THẬT của tao cho fresher" + hỏi ngược "bỏ DTO thì sao?"
- Thành quả: CRUD /tasks với mảng in-memory. → **pain mới: restart là mất sạch.**
- File: `01-hoc-nestjs-voi-ai/01-nestjs-tu-0-cung-ai.md`

### EP 02 — Validation: đơn đặt món không cho khách viết bậy
- ← pain: EP01 nhận payload gì cũng ok — gửi title là số 5 vẫn thành task.
- Học: class-validator, ValidationPipe toàn cục (whitelist, transform), custom message tiếng Việt.
- AI moment: AI sinh rule validation → host fuzz test bằng payload bậy AI generate → thấy chặn được cái nào, lọt cái nào.
- Thành quả: POST bậy → 400 rõ ràng. → **pain: dù sao data vẫn nằm trong RAM.**

### EP 03 — Prisma + PostgreSQL: bộ nhớ thật
- ← pain: EP02 xong, restart server, dữ liệu bốc hơi.
- Học: schema.prisma, migration (metaphor bản vẽ thi công), PrismaService, thay in-memory bằng DB, quan hệ User–Task.
- AI moment: AI sinh schema → host chất vấn "một task thuộc về bao nhiêu user?" TRƯỚC khi migrate.
- Thành quả: restart, data còn nguyên. → **pain: trùng email → crash 500 xấu xí.**

### EP 04 — Error handling: API phải biết nói "tôi sai"
- ← pain: EP03 unique constraint vi phạm → 500 stacktrace bắn ra client.
- Học: HttpException, NotFoundException/BadRequestException/ConflictException, 404 vs 400 vs 409, custom ExceptionFilter.
- AI moment: bảo AI liệt kê MỌI chỗ service có thể fail → học tư duy defensive.
- Thành quả: mọi lỗi trả JSON sạch, đúng status. → **pain: API ai gọi cũng được, không có cửa.**

### EP 05 — JWT Auth: cánh cửa kiểm soát ai được vào
- ← pain: EP04 xong nhưng bất kỳ ai cũng GET được task của người khác.
- Học: register/login, bcrypt hash (tại sao không plaintext), JwtModule, AuthGuard, @CurrentUser, protect /tasks.
- AI moment: tranh luận với AI "tại sao không lưu JWT trong localStorage?" — security thinking.
- Thành quả: không token → 401; có token → chỉ thấy task mình. → **pain: token 15 phút là bị đá ra giữa chừng.**

### EP 06 — Refresh token & Roles: chìa khóa có hạn sử dụng
- ← pain: EP05 đang làm dở thì token hết hạn, logout mất phiên.
- Học: access/refresh flow, tự động gia hạn, @Roles + RolesGuard, user/admin.
- AI moment: host REVIEW code AI viết, bắt được lỗ hổng có thật (AI cố ý để) — "đừng tin AI mù quáng".
- Thành quả: hết hạn tự refresh; admin xóa được task người khác. → **pain: sửa code security mà run sợ — không có gì đảm bảo không vỡ.**

### EP 07 — Testing: viết test như dev đi làm thật
- ← pain: EP06 đổi guard, không biết vỡ chỗ nào ngoài việc... thử tay từng route.
- Học: Jest unit test service với mock, e2e supertest, đỏ→xanh, coverage là gì và KHÔNG phải là gì.
- AI moment: AI sinh test → host phát hiện test "vô nghĩa" (assert gì cũng pass) → tự viết lại test có giá trị.
- Thành quả: `test` + `test:e2e` xanh, refactor hết sợ. → **pain: mỗi máy chạy một kết quả, DB config cá nhân khác nhau.**

### EP 08 — Config & môi trường: code một chỗ chạy đâu cũng được
- ← pain: EP07 e2e cần DB test, mọi người trong team cấu hình mỗi kiểu; SQL password nằm trong code.
- Học: .env, ConfigModule, env validation schema, dev/prod, gitignore secrets — vì sao lộ key là tai họa.
- AI moment: nhờ AI AUDIT repo như senior review PR — scan secret, review config.
- Thành quả: đổi PORT/DATABASE_URL không sửa code; repo sạch key. → **pain: không hiểu request chảy qua những lớp nào để debug.**

### EP 09 — Vòng đời request: Middleware, Guard, Interceptor, Pipe
- ← pain: EP08 thêm auth + pipe + guard, một request lỗi — không biết lớp nào chặn.
- Học: thứ tự middleware → guard → interceptor → pipe → handler, logging interceptor, transform response.
- AI moment: AI vẽ sequence diagram lifecycle → host đối chiếu TỪNG bước với code thật đang chạy.
- Thành quả: mọi request có log rõ lớp đi qua. → **pain: "máy tôi chạy được" — giờ cần cả thế giới gọi được.**

### EP 10 — Docker + Deploy: đưa TaskFlow ra thế giới
- ← pain: cả 9 tập chạy localhost — bạn bè không test được, máy thiếu Node cũng chết.
- Học: Dockerfile multi-stage, docker-compose kèm Postgres, env production, deploy Render/Railway.
- AI moment: AI review Dockerfile từng layer — host giải thích lại được tại sao layer nào tồn tại. Recap Season 1.
- Thành quả: public URL. → **pain: API công khai mà không có tài liệu — ai mà biết gọi thế nào.**

## SEASON 2 — CỨNG CÁP (EP 11–20): production thật sự

### EP 11 — Swagger docs: API tự viết hồ sơ
- ← pain: EP10 public xong, bạn bè (và bot) cứ hỏi "endpoint này nhận gì trả gì".
- Học: @nestjs/swagger, @ApiTags/@ApiOperation, tự sinh trang /docs từ decorator, annotate DTO.
- AI moment: nhờ AI annotate toàn bộ controller bằng swagger decorator — rồi host rà xem annotation nào nói LẠC với code.
- Thành quả: /docs đẹp, thử API ngay trên trình duyệt. → **pain: docs công khai = bản đồ cho bot spam.**

### EP 12 — Rate limiting & Helmet: dạy API tự vệ
- ← pain: EP11 xong, log thấy một IP gọi 500 lần/phút theo đúng… tài liệu.
- Học: @nestjs/throttler, giới hạn theo IP/user, helmet security headers, vì sao cần cả hai lớp.
- AI moment: AI viết script spam chính API mình — host quan sát throttler chặn, rồi hỏi AI cách vượt qua để hiểu giới hạn của nó.
- Thành quả: spam → 429, headers an toàn bật đủ. → **pain: bị spam nhưng log rời rạc — không truy nổi một request cụ thể.**

### EP 13 — Structured logging + Correlation ID
- ← pain: EP12 xảy ra lỗi lúc 2h sáng — hàng nghìn dòng log không biết dòng nào của request nào.
- Học: pino structured logging, correlation ID đi suốt request (middleware), log level, log gì và không log gì (không log password!).
- AI moment: cho AI đọc 200 dòng log rối và tóm tắt "chuyện gì đã xảy ra" — học đọc log như senior đọc.
- Thành quả: 1 request → 1 ID truy vết đầu cuối. → **pain: log nằm trong server — không ai đọc, lỗi im lặng.**

### EP 14 — Monitoring: lỗi tự bay về tìm mình (Sentry)
- ← pain: EP13 log đẹp nhưng user mới báo — mình biết sau cùng.
- Học: Sentry (hoặc GlitchTip), catch toàn cục, lỗi production tự gửi alert kèm stack + user context, release tracking.
- AI moment: host cố tình deploy 1 bug → xem AI (assistant) phân tích alert và đoán nguyên nhân — so với chẩn đoán thật.
- Thành quả: lỗi production → notification trong vài giây. → **pain: report lỗi thì có — mà cầu thủ cần gắn ảnh mô tả.**

### EP 15 — File upload: avatar và attachment cho task
- ← pain: EP14 xong, user than "task của em cần hình chụp lỗi cơ mà".
- Học: Multer, @UploadedFile, validate loại/dung lượng, lưu ở đâu (local vs S3/Cloudinary), serve file tĩnh.
- AI moment: hỏi AI "nếu người dùng upload file giả danh .jpg thì sao?" → học magic bytes, không tin extension.
- Thành quả: gắn ảnh vào task, hiển thị được. → **pain: có ảnh, data phình — GET /tasks trả cả nghìn dòng một phát.**

### EP 16 — Pagination, filtering, sorting
- ← pain: EP15 xong, task 5 nghìn dòng — response cỡ MB, client treo.
- Học: pagination offset vs cursor, query param filter, sort, metadata page, Prisma skip/take/orderBy.
- AI moment: chất vấn AI "offset pagination hỏng ở đâu khi dữ liệu chèn liên tục?" → hiểu vì sao cursor.
- Thành quả: GET /tasks?page=2 nhanh nhẹn. → **pain: task dâng cao không nhóm theo dự án được.**

### EP 17 — Quan hệ dữ liệu: Project, Label và many-to-many
- ← pain: EP16 xong nhưng task là 1 danh sách phẳng — không biết cái nào thuộc dự án nào.
- Học: quan hệ 1-n, n-n trong Prisma, migration an toàn khi đã có data, include vs select, NestJS module cho Project.
- AI moment: AI thiết kế schema — host chất vấn "xóa project thì task thuộc về ai?" (cascade vs restrict) trước khi migrate.
- Thành quả: task thuộc project, gắn nhiều label. → **pain: tạo task + label + counter — hỏng giữa chừng, data lệch.**

### EP 18 — Transactions: làm trọn vẹn hoặc không làm
- ← pain: EP17 xong, tạo task kèm label: task tạo xong, label fail — bụi luôn nửa chừng.
- Học: Prisma $transaction, rollback, khi nào cần transaction (và khi nào KHÔNG), idempotency cơ bản.
- AI moment: nhờ AI dựng kịch bản race condition thật (2 request cùng lúc) — host chạy demo thấy data lệch bằng mắt.
- Thành quả: hoặc tất cả thành công, hoặc quay về như chưa có gì. → **pain: dashboard đếm task join 5 bảng — mỗi lần load là một lần nặng.**

### EP 19 — Caching với Redis: học cách quên
- ← pain: EP18 chuẩn chỉnh nhưng dashboard query nặng, gọi liên tục, DB đổ mồ hôi.
- Học: Redis là gì (metaphor tủ ghi nhớ cạnh bàn làm việc), cache-aside, invalidate khi data đổi, TTL.
- AI moment: hỏi AI "khi nào cache là kẻ thù?" — học stale data, bug khó nhất của caching là dữ liệu CŨ.
- Thành quả: dashboard nhanh gấp nhiều lần, DB nhẹ topo. → **pain: gửi mail nhắc deadline trong request — user chờ, mail server trễ.**

### EP 20 — Background jobs với BullMQ: việc nặng để sau
- ← pain: EP19 xong, tính năng "mail nhắc việc" làm response /tasks chậm đi rõ rệt.
- Học: queue là gì (metaphor quầy nhận đơn — khoá xe xong về trước), BullMQ + Redis, retry, dead letter, job failed.
- AI moment: host tắt mail server giữa chừng — xem job retry như thế nào, rồi hỏi AI "khi nào nên bỏ cuộc?".
- Thành quả: response về ngay, mail xếp hàng gửi ngầm. Recap Season 2. → **pain: queue có mail nhắc — nhưng ai tạo job hằng đêm?**

## SEASON 3 — CHUYÊN SÂU (EP 21–30): hệ thống thực thụ

### EP 21 — Cron job: robot làm ca đêm
- ← pain: EP20 queue chỉ gửi khi có người làm gì đó — nhắc deadline cần quét mỗi sáng 6h.
- Học: @nestjs/schedule, @Cron, @Interval, job định kỳ quét task sắp due, chống chạy trùng nhiều instance.
- AI moment: hỏi AI "nếu có 3 server cùng chạy cron này thì sao?" → học distributed lock ở mức khái niệm.
- Thành quả: 6h sáng, mail nhắc việc tự bay. → **pain: bạn cùng team thêm task — phải F5 mới thấy.**

### EP 22 — Realtime WebSocket: dữ liệu tự đi đến
- ← pain: EP21 xong — mọi thứ "sống" phía server rồi nhưng trình duyệt vẫn phải refresh.
- Học: Socket.IO gateway, @WebSocketServer, emit sự kiện "task:create", client subscribe, khác biệt HTTP vs WebSocket (metaphor gọi điện vs nhắn tin).
- AI moment: AI sinh gateway — host chất vấn "emit xong client mất mạng thì sao?" → học ACK và reconnect cơ bản.
- Thành quả: task mới hiện tức thì trên tab khác. → **pain: socket ai cũng kết nối được — notify bay nhầm người.**

### EP 23 — Socket auth & rooms: phòng riêng cho mỗi người
- ← pain: EP22 mọi client nhận mọi sự kiện — riêng tư đâu mất rồi.
- Học: auth handshake cho WebSocket bằng JWT, room per user, join/leave, emit có chủ đích.
- AI moment: host cố kết nối bằng token hết hạn — xem chặn ở đâu; AI review flow và chỉ ra 1 chỗ sót.
- Thành quả: mỗi người chỉ nhận thông báo của mình. → **pain: user lỡ tay xóa task — mất trắng, không ai biết ai xóa.**

### EP 24 — Soft delete & Audit log: không có gì xóa vĩnh viễn
- ← pain: EP23 an toàn rồi nhưng một lần xóa nhầm là kẹt — không khôi phục, không truy được thủ phạm.
- Học: soft delete (deletedAt), filter mặc định ẩn bản đã xóa, restore, audit log ai-làm-gì-lúc-nào, request context ghi người thao tác.
- AI moment: nhờ AI đề xuất "audit nên log những trường nào?" — rồi cắt bớt theo tư duy privacy (không log thừa thông tin).
- Thành quả: xóa nhầm → khôi phục được; mọi thay đổi có dấu vết. → **pain: thêm field mới làm client cũ vỡ nát.**

### EP 25 — API versioning & backward compatibility
- ← pain: EP24 đổi response shape (thêm deletedAt) — app cũ parse lỗi.
- Học: URI versioning (/v1, /v2), deprecation chiến lược, không phá contract cũ, changelog cho API.
- AI moment: AI đề xuất v2 endpoint — host phê duyệt từng breaking change như review PR thật.
- Thành quả: v1 và v2 sống chung hòa bình. → **pain: data lớn dần, chỗ cũ chậm không phải chỗ mới — đo ở đâu?**

### EP 26 — Performance: N+1, index và nghệ thuật đo trước khi sửa
- ← pain: EP25 xong, vài endpoint chậm dần — sửa kiểu mò, ai cũng có ý kiến.
- Học: đo trước (timing, Prisma query log), N+1 là gì và bắt nó như nào, DB index (metaphor mục lục sách), EXPLAIN cơ bản.
- AI moment: AI nhìn query log đoán N+1 — host verify bằng số liệu thật, không tin bằng miệng.
- Thành quả: endpoint chậm nhất nhanh lên rõ rệt, có số before/after. → **pain: mọi thứ tự động trừ... deploy — vẫn tay.**

### EP 27 — CI/CD GitHub Actions: robot nhận việc deploy
- ← pain: EP26 xong nhưng mỗi lần push là RÍT rung người: test tay, build tay, deploy tay.
- Học: workflow YAML, matrix test, build image, auto deploy khi merge main, branch protection, PR check.
- AI moment: nhờ AI viết workflow — host đọc từng bước và XÓA bớt (learn: CI thừa bước cũng là lỗi).
- Thành quả: git push → test → deploy tự động. → **pain: deploy lúc 18h đang giờ cao điểm — request đang chạy bị đứt ngang.**

### EP 28 — Health check & graceful shutdown: thay lốp xe đang chạy
- ← pain: EP27 deploy tự động nhưng mỗi lần rollout là vài giây 502.
- Học: /health endpoint (liveness/readiness), SIGTERM, graceful shutdown (xong việc đang làm rồi mới nghỉ), connection draining, zero-downtime deploy.
- AI moment: hỏi AI "vài giây 502 đó chuyện gì xảy ra bên trong?" — host vẽ lại timeline shutdown bằng lời AI kể.
- Thành quả: deploy không rơi request. → **pain: thêm tính năng là sửa TaskService — file to dần, đụng gì cũng động vào nó.**

### EP 29 — Event-driven: module nói chuyện qua sự kiện
- ← pain: cả series mọi logic dồn về service — muốn thêm 1 tính năng là sờ vào file nóng.
- Học: decouple bằng event emitter trong monolith (OnEvent), domain event TaskCompleted, listener gửi mail/notify — không cần sửa TaskService, nguyên tắc open-closed bằng ngôn ngữ đời thường.
- AI moment: AI đề xuất thêm "điểm thưởng khi hoàn thành task" — host implement KHÔNG sửa một dòng TaskService — demo open-closed thật.
- Thành quả: tính năng mới = listener mới. Đây là cửa ngõ microservices sau này. → **pain: 30 tập — ôm được mớ kiến thức nào ra phỏng vấn?**

### EP 30 — Recap: từ folder rỗng đến hệ thống thật — và câu hỏi phỏng vấn
- ← pain: cuối hành trình — lo "học xong không nhớ gì, phỏng vấn hỏi gì cũng lúng túng".
- Học: map 29 tập trước thành kiến trúc TaskFlow hoàn chỉnh (1 diagram lớn), 15 câu phỏng vấn backend hay gặp rút từ project, cách kể project trong CV/phỏng vấn (STAR), roadmap tiếp theo (microservices, GraphQL, k8s).
- AI moment: AI đóng vai interviewer difficulty cao — host trả lời thật, không đoán trước — closer của series: "AI hỏi — mình hiểu".
- Thành quả: sơ đồ kiến thức + bộ câu chuyện phỏng vấn. Teaser series tiếp theo.

## Nguyên tắc xuyên suốt series

1. Mỗi ep mở bằng NỖI ĐAU của ep trước (chain rule) — không bao giờ mở bằng "hôm nay ta học X".
2. Mỗi ep có đúng MỘT khoảnh khắc AI nổi bật — không lạm dụng, đó là brand của series.
3. **AI-Driven Development Workflow (quy trình chuẩn 6 bước, xuyên suốt mọi ep):** (1) Yêu cầu — mô tả mục tiêu + context → (2) AI lên Plan → (3) host Review bằng mắt → (4) host Approve → (5) AI Thực hiện code → (6) Kiểm chứng (git diff / test / chạy app). AI không bao giờ tự ý sửa.
4. Host luôn TỰ GÕ lại ít nhất một đoạn code AI sinh trong mỗi ep — điều kiện để gọi là "mình hiểu".
5. Kết mỗi ep teaser 1 câu cho ep sau (retention loop + minh bạch chain).
6. Tool AI: **Opus trong IDE Antigravity**. Đổi tool thì giữ nguyên pattern hỏi–đọc–chất vấn.
7. Mỗi season kết bằng recap nhẹ (EP 10, 20) giúp người xem muộn bám kịp — EP 30 là tổng kết lớn.
8. Title mọi tập đánh số series: `NestJS #NN: <hook> | Lập trình là cuộc sống`.
