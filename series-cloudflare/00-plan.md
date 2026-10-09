# Series Plan — "Cloudflare Combo Free: Lỗ hổng kinh tế" (Season 1: 10 tập, lane: Học lập trình bằng LLM)

- **Format:** mỗi tập một mảnh của MỘT app thật chạy 100% trên free tier Cloudflare (Workers + D1 + R2 + Workers AI). Host tự quay màn hình + tự thoại âm, 8–10 phút, ~650–800 từ thoại.
- **Đối tượng:** Fresher/dev Việt — người muốn deploy sản phẩm thật mà không trả VPS, không thẻ quốc tế.
- **Hook series:** "Combo lỗ hổng kinh tế" — Cloudflare cho free quá nhiều thứ mà hoạt động production-grade. Nói thẳng giới hạn, KHÔNG tô hồng: free tier có quota ngày, reset 00:00 UTC, vượt là lỗi thật (Error 1027).
- **Technical baseline:** Wrangler v4 (cài local trong project, không global), TypeScript, Workers mặc định ESM. Mỗi tập hiện phiên bản thật trên màn hình (`npx wrangler --version`).
- **AI tool:** **Opus trong IDE Antigravity** (agent panel), đúng AI-Driven Development Workflow 6 bước: Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng. Host tự gõ lại ít nhất 1 đoạn AI sinh mỗi tập. Prompt tiếng Việt trên màn hình, nói rõ prompt tiếng Anh rẻ hơn.
- **Spine:** build **EchoNotes** — API ghi âm: upload audio → R2, transcript bằng Whisper (Workers AI), tóm tắt bằng LLM, lưu D1, xử lý nền bằng Queues. Kết series = một sản phẩm deploy sẵn dùng + bảng quota thật trên dashboard.
- **Chain rule:** tập sau mở bằng NỖI ĐAU tập trước tạo ra. Không tập nào mở bằng "hôm nay ta học X".

## Bảng gap đối thủ (nghiên cứu 09/10/2026)

| Kênh/nội dung | Format | Điểm yếu khai thác |
| --- | --- | --- |
| Cloudflare Developers (official) | "Workers Explained" ~5 phút, EN, 599K views | Concept-only, không build app thật, không tiếng Việt |
| "Learn CF Workers 101" (03/2024) | Full course 40+ phút, EN | Cũ: wrangler v3 era, pricing/model đổi nhiều từ 2024 |
| webdecoded, freeCodeCamp-style | Tutorial rời rạc từng service | Không combo D1+R2+AI+Logs trong một spine; không AI-mentor angle |
| Nội dung tiếng Việt | Gần như trống trên chủ đề Workers/D1/R2 (tín hiệu yếu — cần search lại trước EP01) | Cửa ngôn ngữ: series này là bản VI hệ thống đầu tiên |

Ba trục định vị: (1) ngôn ngữ — VI cho chủ đề EN-heavy; (2) format — 8–10 phút/tập thay vì course 40 phút+; (3) angle — học CÙNG AI mentor (6 bước) trên một app thật, không phải tutorial cài đặt.

## Danh sách tập Season 1

### EP 01 — Deploy API lên 330+ thành phố, giá 0 đồng: Workers là gì?
- ← pain nguồn: muốn có API công khai mà VPS tốn tiền + tutorial 3 tiếng lỗi thời.
- Học: V8 isolate ≠ container (không cold start, isolate start nhanh hơn Node process ~100 lần), workers.dev domain, `wrangler init` → `wrangler deploy`, curl từ máy mình.
- Free thật: 100.000 requests/ngày (vượt → Error 1027). Nói thẳng: 10 phút xem = biết hết "lỗ hổng" là gì.
- AI sequence: AI giải thích isolate vs container bằng chính codebase vừa sinh → host chất vấn 1 câu → verify bằng response thật.
- Thành quả: URL công khai trả JSON. → **pain: mỗi lần sửa code phải deploy lên cloud mới test được — chậm và tốn mạng.**

### EP 02 — Code trên localhost như ở production: wrangler dev
- ← pain: EP01 sửa 1 dòng cũng phải deploy mới thấy kết quả.
- Học: `wrangler dev` chạy workerd — đúng runtime production trên máy, offline được, hot reload; so với deploy-để-test; khi nào cần `--remote` (binding thật).
- AI sequence: AI viết failing test case trước → host chạy local → sửa → xanh.
- Thành quả: vòng lặp sửa-chạy-debug trong vài giây, không tốn quota deploy. → **pain: API chưa có dữ liệu — restart gì cũng trống trơn.**

### EP 03 — D1: database SQLite ngay sát edge, free 5 triệu dòng đọc/ngày
- ← pain: API chỉ trả dữ liệu cứng trong code.
- Học: D1 là gì (SQLite ở edge), rows read/written là cách tính tiền khác GB hay giờ, `wrangler d1 migrations`, binding `env.DB`, CRUD notes.
- Free thật: 5 triệu rows đọc + 100.000 rows viết/ngày, 5 GB storage.
- AI sequence: AI lên plan migration + repository → host review SQL từng dòng (accept/reject như review PR).
- Thành quả: note lưu lại, restart không mất. → **pain: ghi âm là file vài MB — nhét vào DB là sai Fletcher.**

### EP 04 — R2: chứa file audio 10 GB free, egress 0 đồng
- ← pain: D1 hợp dữ liệu cấu trúc, không hợp blob.
- Học: object storage, Class A/B operations là gì, vì sao egress free là "lỗ hổng" thật (so S3), presigned upload, binding `env.BUCKET`.
- Free thật: 10 GB-month, 1 triệu Class A + 10 triệu Class B/tháng, egress free.
- AI sequence: AI đề xuất lưu audio trong D1 dạng base64 → host bắt lỗi thiết kế sai → AI sửa plan → compare.
- Thành quả: upload audio từ curl → file nằm trên R2. → **pain: có file rồi nhưng đọc nội dung audio vẫn phải… ngồi nghe tay.**

### EP 05 — Workers AI: transcribe audio bằng Whisper FREE mỗi ngày
- ← pain: audio nằm trên R2 nhưng không search được.
- Học: binding `env.AI`, Neurons là đơn vị gì, whisper-large-v3-turbo ~46,63 Neurons/phút → free 10.000 Neurons/ngày ≈ hơn 200 phút audio; một số model bắt buộc thẻ trả phí (GLM-5.x, Kimi, DeepSeek v4) — nói rõ để không tưởng "free hết".
- AI sequence: prompt AI sinh endpoint transcript → host đo thời gian thật + đọc output từng dòng.
- Thành quả: POST audio → transcript text. → **pain: transcript dài, người dùng muốn tóm tắt — nhưng gọi model trong request dễ timeout.**

### EP 06 — Queues: việc nặng để sau, không giữ user chờ
- ← pain: transcript + tóm tắt chạy trong request, response chậm, dễ vượt CPU time.
- Học: producer/consumer, consumer retry, DLQ; tóm tắt bằng LLM text model (llama-3.2) trong consumer.
- AI sequence: AI refactor flow sync → async → host verify bằng log consumer chạy sau khi response đã trả.
- Thành quả: upload trả 202 ngay, kết quả đến sau. → **pain: consumer fail giữa chừng — không biết lỗi gì vì chưa có log.**

### EP 07 — Workers Logs: debug production bằng log thật, 200K events/ngày free
- ← pain: job lỗi trên production, localhost không tái hiện được.
- Học: `wrangler tail`, Workers Logs trong dashboard, structured log (JSON field), correlation id; retention 3 ngày bản free.
- Free thật: 200.000 log events/ngày (Free), 20 triệu/tháng (Paid $5). ⚠️ 01/12/2026 Cloudflare chuyển sang pricing Observability — fact-sheet phải re-verify trước khi quay.
- AI sequence: AI chèn log field theo schema → host query log thật để bắt lỗi consumer từ EP06.
- Thành quả: bắt được lỗi thật bằng log, không đoán mò. → **pain: mỗi request đều gọi AI + D1, tốn quota oan khi trùng lặp.**

### EP 08 — Cache với KV + gọi nội bộ vài mili-giây
- ← pain: lặp request giống nhau quét D1 + AI liên tục.
- Học: KV (read 100K/ngày free, write 1K/ngày — KHÔNG phải cache write-heavy), cache-aside, TTL; các dịch vụ Cloudflare gọi nhau qua binding nội bộ — service bindings chạy cùng thread, "zero added latency" theo docs — đo `performance.now()` thật trên màn hình.
- AI sequence: AI đề xuất cache mọi thứ → host bắt sai (write limit) → thu hẹp cache đúng chỗ.
- Thành quả: request lặp trả từ cache, quota D1/AI giảm. → **pain: dùng nhiều nhà cung cấp AI, không thấy hết chi phí/lỗi ở một chỗ.**

### EP 09 — AI Gateway: một cửa cho mọi AI call
- ← pain: gọi thẳng provider — không analytics, không rate limit, không fallback.
- Học: gateway là proxy: caching response AI, rate limiting, retry/fallback model; core features free (analytics, cache, rate limit); log storage free 100K logs (tổng).
- Phân biệt rõ: model free nằm ở Workers AI (10K Neurons/ngày) — AI Gateway bản thân là proxy điều phối, không phải nguồn model free. Đây là điểm hay bị nhầm.
- AI sequence: AI chuyển endpoint sang gateway → host A/B cùng prompt qua/thẳng gateway, so số liệu dashboard.
- Thành quả: mọi AI call hiện trên một dashboard. → **pain: app xong nhưng chưa biết tổng thể đang tốn quota gì, đâu là giới hạn phải theo dõi.**

### EP 10 — Recap: bảng quota thật + khi nào đáng trả $5
- ← pain: 9 tập xong, viewer cần bản đồ toàn bộ "combo".
- Học: tổng hợp EchoNotes đã build (Workers+D1+R2+AI+Queues+KV+Gateway), dashboard quota thật trên màn hình, khi nào nâng Workers Paid $5/tháng, Containers chỉ có trên Paid (không free) — dùng khi cần task nâng cao ngoài giới hạn Workers.
- AI sequence: AI đóng vai reviewer hỏi "tại sao chọn X thay vì Y" → host trả lời bằng trade-off đã thật sự implement.
- Thành quả: viewer cầm bảng free-tier 2026 ra quyết định riêng. Teaser Season 2.

### Roadmap Season 2 (đề xuất)
- Containers (paid, task nâng cao: render, ffmpeg) — Durable Objects (state realtime) — Cron Triggers — Workflows (multi-step) — frontend trên Workers (Pages/framework) — Realtime (WebSocket) — Vectorize (RAG) — Hyperdrive (query DB có sẵn từ VN).

## Fact-sheet đã xác minh (nguồn: developers.cloudflare.com, fetch 09/10/2026 — RE-VERIFY trước mỗi tập quay)

| Dịch vụ | Free tier | Bằng chứng |
| --- | --- | --- |
| Workers | 100.000 req/ngày, reset 00:00 UTC, vượt → Error 1027 | workers/platform/limits (verified) |
| Workers Logs | 200.000 events/ngày, retention 3 ngày; ⚠️ đổi pricing Observability từ 01/12/2026 | workers/platform/pricing (verified) |
| Workers AI | 10.000 Neurons/ngày; whisper-large-v3-turbo 46,63 N/phút ≈ 214 phút audio/ngày; whisper 41,14 N/phút ≈ 243 phút | workers-ai/platform/pricing (verified) |
| Workers AI model trả phí | GLM-5.2/5.3/5.3-flash, Kimi K2.6/K2.7-code, DeepSeek v4 — bắt buộc thẻ | workers-ai/platform/pricing (verified) |
| D1 | 5 triệu rows đọc/ngày + 100.000 rows viết/ngày, 5 GB | d1/platform/pricing (verified) |
| R2 | 10 GB-month, 1 triệu Class A + 10 triệu Class B/tháng, egress 0 đồng | r2/pricing (verified) |
| KV | 100.000 đọc + 1.000 viết/ngày, 1 GB | workers/platform/pricing (verified) |
| AI Gateway | Core features free (analytics, caching, rate limiting); log 100K total (Free) | ai-gateway/reference/pricing (verified) |
| Service bindings | Cùng thread, "zero added latency" — đo lại bằng performance.now() khi quay | runtime-apis/bindings/service-bindings (verified) |
| Containers | KHÔNG có free — cần Workers Paid $5/tháng (gồm 375 vCPU-phút + 25 GiB-giờ/tháng) | containers/platform/pricing (verified) |

Số chưa có bằng chứng công khai trong phiên này: giới hạn CPU/request bản free — đo trên dashboard khi quay EP01, không nói số trước.

## Nguyên tắc không được phá

1. Không multi-account / tài khoản ảo lách quota — nói thẳng trên màn hình nếu nhắc tới.
2. Mọi con số quota hiển thị đúng class bằng chứng (verified/host-tested); số thay đổi theo tháng → fact-sheet dated + pre-flight re-verify, narration tránh số cứng khi không cần.
3. Free có giới hạn — mỗi tập nói rõ quota và hiện dashboard thật.
4. Vẫn đủ 6-step AI workflow + host tự gõ lại ≥1 đoạn mỗi tập.

## Visual identity thumbnail

- Màu chủ đạo: CLOUDFLARE ORANGE `#F6821F` + trắng + navy đậm — tách hẳn khỏi NEST RED (NestJS) và CYAN (OpenClaw) để cluster riêng trong suggestions.
- Bố cục giữ grammar của series NestJS: headline 3–5 từ bên trái, `#NN` JetBrains Mono góc trên trái (nhỏ hơn headline ~40%), host/dev bên phải ~35–40%.
- Motif riêng series: badge "FREE" hoặc "0 ĐỒNG" góc phải dưới — chỉ dùng khi tập đó thật sự free.
