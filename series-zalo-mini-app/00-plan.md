# Series Plan — "Vibe Zalo Mini App" (15 tập chính + 2 bonus, lane: Học lập trình bằng LLM)

- **Format:** 15 tập build MỘT Mini App thật cho quán ăn nhỏ — đặt bàn, gọi món trước, voucher, blog, tab admin — từ tạo app trên mini.zalo.me đến Publish và vận hành. Host tự quay màn hình + tự thoại âm.
- **Thời lượng:** mỗi tập 8–10 phút, ~650–800 từ thoại. Tập premiere (EP01) được phép dài hơn với approval. Chỉ dài hơn khi outcome không tách hợp lý.
- **Nguyên tắc tách tập:** mỗi tập một outcome chính và một pain nối sang tập sau. Hai outcome độc lập mà cần quá 18 phút → tách đôi.
- **Technical baseline:** Zalo Mini App CLI (docs 26/1/2026: `npx create-zalo-mini-app <tên>` hoặc `npm i -g zmp-cli` + `zmp init`), template e-commerce kiểu zaui-shop (React + TypeScript + Tailwind + ZaUI), Supabase free tier (Postgres + RLS + Realtime + Edge Functions). **Pin exact version mọi tool trên màn hình khi quay; re-verify trước khi viết từng script** — chính sách Zalo (KYB, duyệt) và template đổi liên tục.
- **AI tool:** **Opus trong IDE Antigravity 1.0** (agent panel bên phải). Pattern: hỏi – đọc – chất vấn – verify.
- **Spine:** build **một app duy nhất cho một quán ăn** (tên đã chốt: **"Gắp Thêm"** — động từ văn hoá mâm cơm Việt, lời mời "gắp thêm đi", icon đôi đũa): khách xem menu, đặt bàn, gọi món trước, lưu voucher, đọc blog; chủ quán quản lý qua tab admin ẩn. Không thanh toán trong app (v1), trả tiền tại quầy. Series này **đồng thời là app thật** cho quán — mọi tập quay trên repo thật `/home/vmo/vibe-coding/gap-them/` (tạo ở EP02).
- **Chain rule:** tập sau mở bằng NỖI ĐAU tập trước tạo ra. Mỗi EP dưới đây ghi "← pain" kế thừa và "→ pain mới" chuyển tiếp.
- **Differentiator:** mỗi tập đúng MỘT AI sequence liền mạch theo **AI-Driven Development Workflow 6 bước: Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng**. Không bao giờ copy-blind. Host tự gõ lại ít nhất một đoạn code AI sinh mỗi tập.

## Gap research (tại 10/2026)

| Nguồn hiện có | Hình thức | Lỗ hổng |
|---|---|---|
| miniapp.vn, wifim.vn, cnv.vn | Trang marketing agency | Bán dịch vụ, không có code, không dạy |
| GitHub zaui-shop, mini-zalo-demo, checkout-sdk-tutorial | Template code + README setup | Có code không có dạy học; đa số fork 2023–2025, lỗi thời |
| Docs chính thức + Coffee Shop Tutorial (mini.zalo.me) | Text hướng dẫn từng bước | Không phải video; không có AI-assisted workflow; không quay được cảnh duyệt/publish thật |
| YouTube tiếng Việt | — | **Không tìm thấy series nào** vibe-code Zalo Mini App từ đầu đến live bằng AI agent (re-verify lại lúc viết script EP01) |

Khoảng trống khai thác: **tiếng Việt + mới 2026** (KYB bắt buộc từ 15/10/2025, CLI `create-zalo-mini-app` mới) + **hành trình đầy đủ giấy tờ → code → duyệt → live** + thương hiệu kênh **AI là mentor không phải người làm hộ**.

## Facts đã verify (nguồn, 10/2026)

- Tạo app: cá nhân tự đăng ký tại mini.zalo.me, không cần công ty để bắt đầu. Nền tảng miễn phí đăng ký + phát hành; Zalo host bundle qua CDN. Bundle < 10MB.
- **KYB = xác thực chủ sở hữu** (bắt buộc từ 15/10/2025 trước khi gửi duyệt phiên bản đầu; sau 31/12/2025 áp cho toàn bộ app đang sống). Theo docs chính thức (mini.zalo.me + miniapp.zaloplatforms.com, 10/2026), chia theo loại hình:
  - **Cá nhân:** tài khoản Zalo đã định danh eKYC là đủ — hệ thống tự liên kết, không nộp giấy tờ, không chờ.
  - **Doanh nghiệp/Hộ kinh doanh:** xác thực qua OA doanh nghiệp, hoặc nộp GCN đăng ký DN/HKD + CCCD người đại diện — xét duyệt 3–5 ngày làm việc.
  - Riêng ngành nghề có điều kiện (y tế, thuốc, tài chính...) phải nộp thêm giấy phép ngành; app đặt bàn + blog không thuộc nhóm này, nhưng chọn danh mục trên dashboard là thấy yêu cầu thật.
- Duyệt phiên bản: 3–5 ngày làm việc (sạch thì 1–2). Lý do reject hiện trong dashboard.
- Mini App = web app chạy trong webview Zalo, giao tiếp nền tảng qua ZJSBridge; mọi permission phải khai báo và được duyệt trước khi dùng.
- Case study số liệu growth (Highlands: 2 triệu người dùng, chuyển đổi 56,9%, 347K follow OA trong 40 ngày) — chỉ dùng kèm link miniforbusiness.zalo.me.

## Quy ước đóng gói (tăng click, giữ retention)

- Tiêu đề đánh số: `Zalo Mini App #NN: <kết quả cụ thể> | Lập trình là cuộc sống`.
- 30 giây đầu chiếu đúng bằng chứng đã hứa trong tiêu đề: app mở trong Zalo thật, đơn chạy về, màn hình duyệt.
- Nhịp nội dung: lỗi thật / tình huống thật → AI đề xuất → host bắt lỗi hoặc chất vấn → sửa → kiểm chứng bằng request/diff/app chạy.
- Thumbnail: 2–4 từ lớn, bổ sung cho tiêu đề, không lặp tiêu đề.

## Visual identity thumbnail của series

- Bố cục cố định như series NestJS: headline lớn bên trái (3–5 từ), developer 35–40% bên phải, màn hình code làm nền phụ.
- Màu chủ đạo: **Zalo blue `#0068FF`** + trắng `#FFFFFF` + đen/navy đậm. Không dùng neon green/cyan cho headline.
- Font Anton (hoặc Helvetica Neue Condensed Black), stroke đen, shadow gọn. Số `#NN` góc cố định mỗi tập.
- Thumbnail đầu tiên (EP01) là ảnh tham chiếu chuẩn cho cả series; kiểm tra dấu tiếng Việt ở full-size và bản thu nhỏ 320×180.

## Phiên âm thêm cho series này

| Từ | Đọc là |
|---|---|
| ZaUI | Za-U-I |
| zmp / zmp-cli | zét-em-pi / zét-em-pi-cli |
| KYB | kê-ai-bi |
| Supabase | su-pa-bết |
| ZJSBridge | zét-giét-ét bờ-rích |
| Vite | vít |
| Deno | đi-nô |
| webview | ouét-viu |

## Cổng kiểm tra trước khi viết/quay từng script

1. **CLI probe:** chạy thật `npx create-zalo-mini-app` / `zmp init` trong thư mục scratch (TMPDIR, stdin đóng hoặc `script -qec`) — ghi lại đúng prompt hiện tại và output; không script prompt mà CLI đã bỏ. Pin version.
2. **Policy re-verify:** mở lại trang KYB + quy trình duyệt (docs.zaloplatforms.com, miniapp.zaloplatforms.com) tại thời điểm viết EP01 và EP14 — ngày chính sách dịch, không quote từ memory.
3. **Supabase UI flow:** verify lại đường tạo project / SQL editor / bật Realtime khi viết EP03, EP06.
4. **ZaUI API:** đối chiếu docs component hiện hành khi viết EP05, EP13 — props đổi giữa các bản zmp-ui.
5. Số liệu người dùng/case study: chỉ kèm URL nguồn chính thức.

## SEASON 1 — GIẤY TỜ & NỀN TẢNG (EP 01–05)

### EP 01 — premiere: App chạy trong Zalo, không cần App Store | Zalo Mini App #1
- **Mở màn theo đúng format premiere:** chào kênh → gap (tutorial VN không có, docs tiếng Anh, KYB vừa đổi) → tinh thần series (AI là mentor, host review từng dòng).
- Học: Mini App là gì — web app < 10MB chạy trong webview Zalo; vì sao super app (tiền lệ WeChat, 75 triệu user Zalo, không cần cài đặt, Zalo host CDN); cái giá của nền tảng: kiểm duyệt + permission + **KYB** (xác thực chủ sở hữu, bắt buộc từ 15/10/2025).
- Trace: điều gì xảy ra khi người dùng bấm mở một Mini App (tải bundle từ CDN → webview → ZJSBridge).
- Thao tác thật (đã chốt đường đi): tạo app trên mini.zalo.me loại **Cá nhân** — Zalo đã eKYC là xác thực xong ngay, không có cảnh nộp giấy tờ. Đường DN/Hộ kinh doanh (nộp GCN + CCCD, chờ 3–5 ngày; khi nào nên gắn HKD: danh mục F&B đúng hơn, bắt buộc nếu làm thanh toán) giải thích bằng narration + bảng so sánh 1 màn hình, không làm thật trên camera.
- AI sequence: host đưa spec quán (đặt bàn/gọi món/voucher/blog) → AI lên plan toàn bộ product → host review, **cắt scope v1** (bỏ thanh toán, giao hàng, tích điểm) → approve plan. Kể hành động (plan → review → approve) nhưng KHÔNG liệt kê tên 6 bước — chưa giới thiệu.
- Thành quả: app tồn tại trên dashboard, xác thực chủ sở hữu xong ngay (Cá nhân/eKYC), có Mini App ID. → **pain mới: đã có "giấy khai sinh" nhưng chưa có dòng code nào — máy còn trống.**
- File: `ep01-app-trong-zalo/script.md`

### EP 02 — Scaffold: zmp-cli sinh project thế nào và mỗi file để làm gì
- ← pain: EP01 xong tay vẫn trắng — chưa có gì để code.
- Học (deep): vì sao scaffold sinh ra từng thứ — `app-config.json` (title, config toàn app), root `<div id="app">`, **ZMPRouter** thay react-router (ràng buộc history của webview), pages phải đăng ký trong router, ZaUI là design system chuẩn Zalo, `mock/*.json` là data giả của template.
- Thao tác thật: cài CLI, tạo project (template e-commerce), `zmp start`, mở localhost:3000, **quét QR preview trong Zalo điện thoại thật**.
- Host tự gõ: đổi tên app trong `app-config.json`, sửa một page.
- AI sequence: nhờ AI giải thích từng file scaffold sinh ra + map vai trò → host quality-check bằng cách hỏi lại "xóa được file nào?" → AI nhận file thừa của template → host duyệt danh sách xóa.
- **Cuối tập: giới thiệu 6-bước AI-Driven Development Workflow LẦN ĐẦU** (app đã cài và chạy xong — đúng vị trí theo quy tắc kênh).
- Thành quả: app "của mình" mở được trong Zalo. → **pain mới: đó vẫn là quán cafe demo — menu hardcode trong `mock/`, không phải quán mình.**
- File: `ep02-scaffold-zmp-cli/script.md`

### EP 03 — Supabase: dọn nhà cho data (có service đứng trước khi connect)
- ← pain: menu nằm trong file json — sửa một giá phải deploy lại.
- Học: schema categories/dishes (normalize vì sao — không nhét một blob json); **RLS là gì** (metaphor duy nhất: bảo vệ kiểm soát ở tầng dữ liệu, như bảo vệ từng bàn thay vì chỉ cửa); anon key vs service_role key — service_role tuyệt đối không xuống client.
- Thao tác thật (đúng quy tắc "standing service trước"): tạo Supabase project → SQL editor tạo bảng → bật RLS read-only → `.env` gitignore → app fetch menu thay `mock/`.
- Trace: bấm mở app → request tới Supabase → row → render màn hình menu.
- AI sequence: yêu cầu AI thiết kế schema menu → AI đề xuất thêm nhiều bảng thừa (i18n, audit) → host cắt bằng YAGNI → approve migration SQL → chạy → verify bằng select thật.
- Thành quả: đổi giá trong DB, app cập nhật không cần build. → **pain mới: app không biết khách là ai — ai mở cũng là khách lạ.**
- File: `ep03-supabase-data/script.md`

### EP 04 — Định danh người dùng Zalo, không cần mật khẩu
- ← pain: không có người dùng thì không có đặt bàn, không có voucher "của tôi".
- Học (deep): `login()` và `getUserInfo` — flow OAuth thu nhỏ; zaloId là định danh ổn định; vì sao platform khóa data người dùng sau permission + duyệt; trade-off thẳng thắn: không dùng Supabase Auth thì zaloId là định danh app-level, có thể spoof — chấp nhận cho v1 vì stakes thấp, nâng cấp ở EP07.
- Thao tác thật: khai báo permission trong dashboard, thêm nút đăng nhập, header hiện avatar + tên từ Zalo.
- AI sequence: hỏi AI "vì sao không tự làm đăng nhập mật khẩu?" → AI trình bày trade-off → host quyết định dùng identity của platform.
- Thành quả: mở app thấy đúng tên và avatar Zalo của mình. → **pain mới: biết khách là ai rồi — nhưng khách vẫn phải gọi điện đặt bàn.**
- File: `ep04-dinh-danh-zalo/script.md`

### EP 05 — Form đặt bàn & số điện thoại một chạm
- ← pain: khách vẫn đặt bàn qua điện thoại, quán vẫn ghi sổ.
- Học: controlled components; time slot sinh từ `app_settings` (giờ mở cửa); `getPhoneNumber` là permission nhạy cảm — giải trình mục đích khi xin duyệt; validation client khác validation server (v1 chưa có server validator — nói thật hạn chế, EP07 xử lý).
- Thao tác thật: form ngày/giờ/số người/tên/SĐT, nút lấy SĐT một chạm, insert vào `bookings`, màn hình thành công.
- Host tự gõ: toàn bộ form bằng tay (đây là đoạn "AI viết, mình hiểu" của tập — host tự gõ từ plan AI đưa).
- AI sequence: AI lên plan form + validation → host review (bắt AI quên chống chọn ngày quá khứ) → approve → AI code → host test bằng ca sai (ngày quá khứ, thiếu SĐT).
- Thành quả: một đơn đặt bàn nằm trong DB. → **pain mới: quán phải ngồi F5 dashboard Supabase mới biết có đơn.**
- File: `ep05-form-dat-ban/script.md`

## SEASON 2 — CHẠY THẬT (EP 06–10)

### EP 06 — Realtime: đơn tự chạy về, quán có tiếng ting
- ← pain: đơn đến mà không ai biết — F5 cả ngày.
- Học (deep): Supabase Realtime — dưới hood là Postgres LISTEN/NOTIFY đẩy qua websocket; subscribe channel; tab admin ẩn hiện theo zaloId của chủ quán; tiếng ting + rung khi có INSERT mới.
- Trace: INSERT từ điện thoại này → Postgres event → websocket → màn hình admin tự thêm dòng.
- AI sequence: nhờ AI làm notification → AI đề xuất poll mỗi 5 giây → host chất vấn chi phí + độ trễ → đổi sang realtime subscribe → verify hai thiết bị song song trên màn hình.
- Thành quả: hai thiết bị cùng mở, đơn hiện ra ngay. → **pain mới: thấy đơn nhưng không bấm được "Xác nhận" — RLS đang chặn đúng như thiết kế.**
- File: `ep06-realtime-don-moi/script.md`

### EP 07 — Edge Function: chìa khóa của chủ quán
- ← pain: khách thì được thêm đơn, quán thì không được sửa đơn — ai cũng bị chặn như nhau.
- Học (deep): Edge Function chạy Deno trên server của Supabase; service_role chỉ sống ở server; PIN admin trong env; vì sao không bao giờ nhét service_role vào client. Đây là chỗ trả nợ EP04/EP05: mọi ghi của admin đi qua hàm này, có thể validate + authorize thật.
- AI moment (tập này AI làm sai có chủ đích): AI đề xuất đặt service_role trong code client "cho nhanh" → host bắt lỗi, giải thích ai cũng đọc được bundle → thiết kế lại qua Edge Function.
- Thao tác thật: viết `admin-api` (confirm/cancel booking), gọi từ tab admin, thấy status đổi realtime.
- Thành quả: chủ quán bấm Xác nhận/Huỷ ngay trên app. → **pain mới: đặt bàn xong rồi — nhưng khách muốn gọi món trước luôn.**
- File: `ep07-edge-function-admin/script.md`

### EP 08 — Giỏ hàng & pre-order: giá bị đóng băng lúc đặt
- ← pain: khách đặt bàn nhưng menu chỉ để xem.
- Học: tái dùng cart components của template; `orders.items` là jsonb **snapshot giá tại thời điểm đặt** — denormalization có chủ đích (sau này đổi giá, đơn cũ không bị sửa theo); tính total ở đâu.
- Trace: thêm món → cart state → submit → booking + order liên kết nhau.
- AI sequence: yêu cầu AI thiết kế orders schema → AI tham chiếu `dish_id` sống → host chất vấn "quán đổi giá mai, đơn hôm qua hiện bao nhiêu?" → chốt snapshot giá trong jsonb.
- Thành quả: đơn pre-order đầy đủ món + tổng tiền đúng. → **pain mới: hết cơm rang mà app vẫn cho đặt.**
- File: `ep08-gio-hang-preorder/script.md`

### EP 09 — Hết món: tắt một nút ở quầy, menu sống lại trên tay khách
- ← pain: bếp hết món, app không biết → đơn rớt, khách giận.
- Học: toggle `available` qua admin-api; menu nhận realtime; badge "Hết món" chặn thêm vào giỏ; optimistic UI là gì và rủi ro rollback.
- AI sequence: AI code toggle + realtime → host test race: tắt món đúng lúc đang có nó trong giỏ → quyết định xử lý (bỏ món + báo khách) → verify.
- Thành quả: tắt món ở quầy, điện thoại khác thấy mờ ngay. → **pain mới: app xịn rồi — nhưng chưa có lý do nào để khách quay lại.**
- File: `ep09-het-mon-realtime/script.md`

### EP 10 — Voucher + recap nửa chặng
- ← pain: khách ăn xong đi luôn, không có gì kéo về.
- Học: bảng `vouchers` + `user_vouchers`; unique constraint một user lưu một lần; `used_at` đánh dấu ở quầy; hạn chế thật của RLS với zaloId spoofable (nói thẳng, stakes thấp nên chấp nhận — nâng cấp nếu cần).
- Recap EP01–09: từ dashboard trống → app có menu, định danh, đặt bàn, realtime, admin, pre-order. Bản đồ kiến trúc 1 màn hình.
- AI sequence: nhờ AI review toàn bộ schema sau 7 tập → AI phát hiện thiếu index cho query voucher của user → host duyệt migration.
- Thành quả: khách lưu voucher, quầy dập dấu đã dùng. → **pain mới: có voucher mà chưa ai biết app tồn tại.**
- File: `ep10-voucher-recap/script.md`

## SEASON 3 — TĂNG TRƯỞNG & PHÁT HÀNH (EP 11–15)

### EP 11 — Share & growth loop:Mini App lan trong Zalo
- ← pain: 0 người dùng ngoài gia đình host.
- Học: `openShareSheet` (bạn bè/nhóm/feed), widget follow OA, QR in dán tại bàn; học từ case study thật có nguồn (Highlands — 2 triệu user, 56,9% chuyển đổi, link miniforbusiness.zalo.me); vòng tăng trưởng mini app: quét QR tại quán → dùng → share → người mới.
- AI sequence: hỏi AI thiết kế "khoảnh khắc share" tự nhiên nhất (màn hình nào, lời mời gì) → AI đề xuất 3 chỗ → host chọn màn hình voucher → code → verify trên Zalo thật.
- Thành quả: share app vào một nhóm Zalo, bạn bè mở được ngay. → **pain mới: quán muốn tự viết bài giữ chân khách — chưa có chỗ.**
- File: `ep11-share-growth/script.md`

### EP 12 — Blog chăm sóc khách ngay trong app
- ← pain: bài viết quán đang đăng Facebook — app không có chỗ kể chuyện.
- Học: bảng `posts`, render markdown (`react-markdown`), ảnh cover; admin viết bài bằng textarea markdown — nội dung đổi không cần deploy/duyệt lại.
- AI sequence: AI lên CRUD bài viết → host review quyền (chỉ admin-api được publish) → code → host tự viết bài đầu tiên thật của quán.
- Thành quả: danh sách + trang đọc bài chạy trong app. → **pain mới: chuẩn bị gửi duyệt — app phải trông như sản phẩm, không像 demo.**
- File: `ep12-blog-trong-app/script.md`

### EP 13 — Polish & checklist duyệt: nhìn qua mắt người kiểm duyệt
- ← pain: chức năng đủ nhưng còn chữ placeholder, ảnh nặng, nút chết.
- Học: checklist duyệt của Zalo — nội dung thật, không placeholder, permission khai báo phải dùng thật, privacy policy (ghi rõ lưu SĐT để xác nhận đặt bàn); tối ưu bundle < 10MB (ảnh WebP, system font, kiểm tra `zmp build` output).
- AI sequence: nhờ AI đóng vai reviewer Zalo duyệt app → AI liệt kê lỗi (placeholder, nút chết, permission thừa) → host sửa từng mục → verify lại.
- Thành quả: app sạch, bundle nhẹ, sẵn sàng deploy. → **pain mới: mọi thứ chỉ chạy trên máy host — chưa ai khác mở được.**
- File: `ep13-polish-checklist/script.md`

### EP 14 — Deploy & gửi duyệt: 3–5 ngày chờ
- ← pain: app chỉ mình host mở được (QR dev).
- Học: `zmp login` + `zmp deploy`; quản lý phiên bản trên dashboard; gửi duyệt từ trạng thái Testing; **KYB từ EP01 giờ trả nợ** — đủ điều kiện gửi; các lý do reject phổ biến và cách đọc feedback trong dashboard.
- Thao tác thật: deploy thật, điền hồ sơ duyệt, bấm gửi. Kể thẳng thắn: chờ 3–5 ngày làm việc là một phần của đời mini app dev.
- AI sequence: nhờ AI soạn mô tả phiên bản + giải trình permission (bản thân bài học: viết cho người duyệt đọc) → host biên tập cho đúng sự thật → nộp.
- Thành quả: trạng thái "Chờ xét duyệt". → **pain mới: chờ duyệt xong — publish và vận hành ra sao.**
- File: `ep14-deploy-duyet/script.md`

### EP 15 — Go live, vận hành & tổng kết: quán có app riêng, tổng chi 0 đồng platform
- ← pain: được duyệt (hoặc xử lý xong feedback reject nếu có thật — quay thật) — còn bước cuối.
- Học: bấm Publish; QR dán tại bàn/cửa; tablet ở quầy chạy tab admin làm "màn hình bếp"; chi phí tổng: 0đ platform + Supabase free tier + thời gian; roadmap v2: Checkout SDK thanh toán, dine-in QR gọi món tại bàn, ZNS thông báo, Supabase Auth chuẩn hóa.
- Recap toàn series: kiến trúc cuối cùng 1 màn hình; 5 câu phỏng vấn mapping (webview vs native, super app distribution, RLS, denormalization, vì sao Edge Function giữ secret).
- AI moment kết: AI đóng vai interviewer hỏi "nếu 1000 đơn/ngày thì hệ thống này vỡ ở đâu?" → host trả lời bằng điểm yếu thật đã biết.
- Thành quả: người lạ tìm thấy app trong Zalo, đặt được bàn thật. Kết series bằng teaser đường đến bonus/v2.
- File: `ep15-go-live-tong-ket/script.md`

## BONUS

### Bonus A — Web app có sẵn thành Mini App trong 30 phút
- Dùng đường `zmp init` → "Use ZMP to deploy only" cho project web sẵn (docs chính thức có hướng dẫn chuyển đổi). Demo trên một web React có thật.
- File: `bonus-a-web-thanh-mini-app/script.md`

### Bonus B — Thanh toán trong Mini App: Checkout SDK
- v2 của app: tích Zalo Checkout SDK (repo chính thức checkout-sdk-tutorial làm mẫu); cần hộ kinh doanh cho KYB nhóm thanh toán; quy trình duyệt chặt hơn.
- File: `bonus-b-checkout-sdk/script.md`

## Nguyên tắc xuyên suốt series

1. Mỗi ep mở bằng NỖI ĐAU của ep trước (chain rule) — không bao giờ mở bằng "hôm nay ta học X".
2. Mỗi ep đúng MỘT AI sequence liền mạch — vài lượt hỏi–đáp phục vụ một outcome, không biến thành trình diễn tính năng AI.
3. **AI-Driven Development Workflow 6 bước** (giới thiệu lần đầu ở cuối EP02, sau milestone app chạy): Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng. AI không bao giờ tự ý sửa.
4. Host tự gõ lại ít nhất một đoạn code AI sinh mỗi tập — "AI viết, mình hiểu".
5. Kết mỗi ep một câu teaser cho ep sau.
6. Tool AI: Opus trong IDE Antigravity 1.0; host prompt tiếng Việt cho dễ demo, nhắc viewers prompt tiếng Anh rẻ hơn.
7. Mọi lệnh CLI và prompt trong script phải được **probe thật trước khi quay** (cổng kiểm tra ở trên) — không script prompt mà CLI phiên bản hiện tại đã bỏ.
8. Title đánh số: `Zalo Mini App #NN: <hook> | Lập trình là cuộc sống`; thumbnail `#NN` góc cố định.

## Câu hỏi mở cần chốt trước khi viết EP01

- ~~Q1 — Tên quán/app~~ **ĐÃ CHỐT: "Gắp Thêm"** (repo `gap-them`). Lưu ý: trước khi tạo app thật ở EP01, host tự Google/Facebook search "Gắp Thêm" quán ăn 30 giây + để Zalo dashboard chặn trùng tên nếu có.
- ~~Q2 — Xác thực chủ sở hữu~~ **ĐÃ CHỐT: Cá nhân** (Zalo eKYC). Chuyện hộ kinh doanh giải thích bằng narration trong EP01 (khi nào cần HKD), không làm thật trên camera.
- **Q3 — Nhịp đăng:** xen kẽ với series NestJS đang chạy (1 NestJS : 1 Mini App/tuần) hay chạy riêng mùa mới? Ảnh hưởng đến việc EP14 có khớp lịch chờ duyệt 3–5 ngày thật hay không (nên quay trước, chèn cảnh chờ duyệt thật).
