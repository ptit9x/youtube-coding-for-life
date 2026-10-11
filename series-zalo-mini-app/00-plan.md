# Series Plan — "Vibe Zalo Mini App" (12 tập chính + 2 bonus, lane: Học lập trình bằng LLM)

- **Format:** 12 tập build MỘT Mini App thật cho quán ăn nhỏ — đặt bàn, gọi món trước, voucher, blog, tab admin — từ tạo app trên mini.zalo.me đến Publish và vận hành. Host tự quay màn hình + tự thoại âm.
- **Thời lượng:** mỗi tập 6–10 phút, ~500–800 từ thoại (user-corrected 10/2026: vibe coding ra app nhanh; tập gọn, mở màn là app đang chạy). Tập premiere (EP01) được phép dài hơn với approval. Chỉ dài hơn khi outcome không tách hợp lý.
- **Nguyên tắc tách tập:** mỗi tập một outcome chính và một pain nối sang tập sau. Hai outcome độc lập mà cần quá 18 phút → tách đôi. Không viết tập "setup thuần" — mọi tập mở màn bằng kết quả chạy được của tập trước.
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
2. **Policy re-verify:** mở lại trang KYB + quy trình duyệt (docs.zaloplatforms.com, miniapp.zaloplatforms.com) tại thời điểm viết EP01 và EP10 — ngày chính sách dịch, không quote từ memory.
3. **Supabase UI flow:** verify lại đường tạo project / SQL editor / bật Realtime khi viết EP02, EP04.
4. **ZaUI API:** đối chiếu docs component hiện hành khi viết EP03 (form đặt bàn), EP09 (polish) — props đổi giữa các bản zmp-ui.
5. Số liệu người dùng/case study: chỉ kèm URL nguồn chính thức.
6. **Quy tắc cắt ghép (user-corrected 10/2026):** thời gian AI sinh code / install / build KHÔNG quay trực tiếp — cắt thành time-lapse 3–5 giây hoặc chèn narration giải thích quyết định trong lúc chờ; giữ nguyên thời lượng thật của: prompt gõ, plan review, git diff, và moment app chạy. Đây là cách series ngắn lại mà vẫn giữ thương hiệu "host review từng dòng".

## SEASON 1 — TỪ SỐ 0 ĐẾN QUÁN NHẬN ĐƠN (EP 01–04)

### EP 01 — premiere: Một chiều ra app chạy trong Zalo | Zalo Mini App #1
- **Mở màn bằng KẾT QUẢ:** 30 giây đầu chiếu app "Gắp Thêm" mở trong Zalo thật, đặt một bàn — rồi mới chào kênh → gap (tutorial VN không có, docs tiếng Anh, chính sách vừa đổi) → tinh thần series (AI là mentor, host review từng dòng).
- Học (gọn cho premiere): Mini App là gì — web app < 10MB chạy trong webview Zalo; vì sao super app (không cần cài, Zalo host CDN); cái giá: kiểm duyệt + permission + xác thực chủ sở hữu (Cá nhân = Zalo eKYC xong ngay; khi nào cần HKD — narration + bảng so sánh 1 màn hình, không làm thật trên camera).
- Thao tác thật (nhanh, cắt ghép): tạo app trên mini.zalo.me loại **Cá nhân** (tên, danh mục Ẩm thực, icon) → có **Mini App ID**; cài CLI, tạo project `gap-them` (template e-commerce), `zmp start`, **quét QR mở trong Zalo điện thoại thật**. Không đi từng prompt CLI trên màn hình — tóm tắt + chèn kết quả.
- AI sequence: host đưa spec quán (đặt bàn/gọi món/voucher/blog) → AI lên plan toàn bộ product → host review, **cắt scope v1** (bỏ thanh toán, giao hàng, tích điểm) → approve. AI giải thích nhanh scaffold sinh gì (`app-config.json`, ZMPRouter, ZaUI) — chỉ file chạm tới hôm nay.
- **Cuối tập: giới thiệu 6-bước AI-Driven Development Workflow LẦN ĐẦU** (app đã cài và chạy xong — đúng vị trí theo quy tắc kênh).
- Thành quả: app "Gắp Thêm" (đang là quán demo) mở được trong Zalo + plan v1 đã duyệt. → **pain mới: menu là json hardcode của template — không phải món của quán mình.**
- File: `ep01-tao-app-chay-trong-zalo/script.md`

### EP 02 — Supabase: menu thật, đổi giá không cần deploy
- ← pain: menu nằm trong `mock/*.json` — sửa một giá phải build lại app.
- Học: schema categories/dishes (normalize vì sao); **RLS là gì** (metaphor duy nhất: bảo vệ từng bàn thay vì chỉ cánh cửa); anon key vs service_role key — service_role tuyệt đối không xuống client.
- Thao tác thật: tạo Supabase project → SQL editor tạo bảng → bật RLS read-only → `.env` gitignore → app fetch menu thay `mock/`. Trace 1 dòng: bấm mở app → request → row → render.
- AI sequence: yêu cầu AI thiết kế schema menu → AI đề xuất thêm bảng thừa (i18n, audit) → host cắt bằng YAGNI → approve migration SQL → chạy → verify bằng select thật.
- Thành quả: đổi giá trong DB, menu trên Zalo cập nhật không cần build. → **pain mới: app không biết khách là ai — ai mở cũng là khách lạ.**
- File: `ep02-supabase-menu-that/script.md`

### EP 03 — Khách bấm đặt bàn: định danh Zalo + SĐT một chạm
- ← pain: không có người dùng thì không có đặt bàn, không có voucher "của tôi".
- Học (deep): `login()` + `getUserInfo` — OAuth thu nhỏ; zaloId là định danh ổn định; `getPhoneNumber` là permission nhạy cảm — giải trình mục đích khi xin duyệt; trade-off thẳng thắn: zaloId app-level có thể spoof — chấp nhận v1 vì stakes thấp, nói rõ hạn chế validation client (EP04 trả nợ).
- Thao tác thật: khai báo permission trong dashboard; form ngày/giờ/số người/tên/SĐT sinh time slot từ giờ mở cửa; nút lấy SĐT một chạm; insert vào `bookings`; màn hình thành công.
- Host tự gõ: toàn bộ form bằng tay (đoạn "AI viết, mình hiểu" của tập — gõ từ plan AI đưa).
- AI sequence: AI lên plan form + validation → host review, bắt AI quên chống chọn ngày quá khứ → approve → AI code → host test ca sai (ngày quá khứ, thiếu SĐT).
- Thành quả: một đơn đặt bàn nằm trong DB. → **pain mới: quán phải ngồi F5 dashboard Supabase mới biết có đơn.**
- File: `ep03-dinh-danh-dat-ban/script.md`

### EP 04 — Quán nhận đơn: realtime tiếng ting + Edge Function giữ chìa khóa
- ← pain: đơn đến mà không ai biết — chủ quán F5 cả ngày.
- Học (deep): Supabase Realtime = Postgres LISTEN/NOTIFY đẩy qua websocket; tab admin ẩn hiện theo zaloId chủ quán; Edge Function chạy Deno — service_role chỉ sống ở server; đây là chỗ trả nợ EP03: mọi ghi của admin đi qua hàm này, validate + authorize thật.
- AI moment (AI làm sai có chủ đích): AI đề xuất poll 5 giây + đặt service_role trong client "cho nhanh" → host bắt lỗi (ai cũng đọc được bundle) → đổi sang realtime subscribe + Edge Function `admin-api` (confirm/cancel booking).
- Trace: INSERT từ điện thoại này → Postgres event → websocket → màn hình admin tự thêm dòng + tiếng ting.
- Thành quả: hai thiết bị song song — khách đặt, quán bấm Xác nhận/Huỷ ngay trên app. → **pain mới: đặt bàn xong — nhưng khách muốn gọi món trước luôn.**
- File: `ep04-admin-realtime-ting/script.md`

## SEASON 2 — CHẠY THẬT (EP 05–08)

### EP 05 — Giỏ hàng & pre-order: giá bị đóng băng lúc đặt
- ← pain: khách đặt bàn nhưng menu chỉ để xem.
- Học: tái dùng cart components của template; `orders.items` là jsonb **snapshot giá tại thời điểm đặt** — denormalization có chủ đích (sau này đổi giá, đơn cũ không bị sửa theo); tính total ở đâu.
- Trace: thêm món → cart state → submit → booking + order liên kết nhau.
- AI sequence: yêu cầu AI thiết kế orders schema → AI tham chiếu `dish_id` sống → host chất vấn "quán đổi giá mai, đơn hôm qua hiện bao nhiêu?" → chốt snapshot giá trong jsonb.
- Thành quả: đơn pre-order đầy đủ món + tổng tiền đúng. → **pain mới: hết cơm rang mà app vẫn cho đặt.**
- File: `ep05-gio-hang-preorder/script.md`

### EP 06 — Hết món: tắt một nút ở quầy, menu sống lại trên tay khách
- ← pain: bếp hết món, app không biết → đơn rớt, khách giận.
- Học: toggle `available` qua admin-api; menu nhận realtime; badge "Hết món" chặn thêm vào giỏ; optimistic UI là gì và rủi ro rollback.
- AI sequence: AI code toggle + realtime → host test race: tắt món đúng lúc đang có nó trong giỏ → quyết định xử lý (bỏ món + báo khách) → verify.
- Thành quả: tắt món ở quầy, điện thoại khác thấy mờ ngay. → **pain mới: app xịn rồi — nhưng chưa có lý do nào để khách quay lại.**
- File: `ep06-het-mon-realtime/script.md`

### EP 07 — Voucher + Blog: lý do quay lại + chỗ kể chuyện của quán
- ← pain: khách ăn xong đi luôn; bài viết quán đang đổ lên Facebook, app không có chỗ giữ chân.
- Học: bảng `vouchers` + `user_vouchers` (unique constraint một user lưu một lần; `used_at` dập ở quầy); bảng `posts` + render markdown (`react-markdown`), admin viết bài bằng textarea — nội dung đổi không cần deploy/duyệt lại; hạn chế thật của RLS với zaloId spoofable (nói thẳng, stakes thấp nên chấp nhận).
- AI sequence: nhờ AI review toàn bộ schema sau 6 tập (AI phát hiện thiếu index cho query voucher của user → host duyệt migration) → rồi plan CRUD blog (host review quyền: chỉ admin-api được publish) → host tự viết bài đầu tiên thật của quán.
- Thành quả: khách lưu voucher, quầy dập dấu đã dùng; danh sách + trang đọc bài chạy trong app. → **pain mới: có voucher, có bài hay — mà chưa ai biết app tồn tại.**
- File: `ep07-voucher-blog/script.md`

### EP 08 — Share & growth loop: Mini App lan trong Zalo
- ← pain: 0 người dùng ngoài gia đình host.
- Học: `openShareSheet` (bạn bè/nhóm/feed), widget follow OA, QR in dán tại bàn; học từ case study thật có nguồn (Highlands — 2 triệu user, 56,9% chuyển đổi, link miniforbusiness.zalo.me); vòng tăng trưởng mini app: quét QR tại quán → dùng → share → người mới. CTA series: "Gắp thêm một đứa bạn vào".
- AI sequence: hỏi AI thiết kế "khoảnh khắc share" tự nhiên nhất → AI đề xuất 3 chỗ → host chọn màn hình voucher → code → verify trên Zalo thật.
- Thành quả: share app vào một nhóm Zalo, bạn bè mở được ngay. → **pain mới: chuẩn bị gửi duyệt — app phải trông như sản phẩm, không phải demo.**
- File: `ep08-share-growth/script.md`

## SEASON 3 — PHÁT HÀNH & TỔNG KẾT (EP 09–12)

### EP 09 — Polish & checklist duyệt: nhìn qua mắt người kiểm duyệt
- ← pain: chức năng đủ nhưng còn chữ placeholder, ảnh nặng, nút chết.
- Học: checklist duyệt của Zalo — nội dung thật, không placeholder, permission khai báo phải dùng thật, privacy policy (ghi rõ lưu SĐT để xác nhận đặt bàn); tối ưu bundle < 10MB (ảnh WebP, system font, kiểm tra `zmp build` output).
- AI sequence: nhờ AI đóng vai reviewer Zalo duyệt app → AI liệt kê lỗi (placeholder, nút chết, permission thừa) → host sửa từng mục → verify lại.
- Thành quả: app sạch, bundle nhẹ, sẵn sàng deploy. → **pain mới: mọi thứ chỉ chạy trên máy host — chưa ai khác mở được.**
- File: `ep09-polish-checklist/script.md`

### EP 10 — Deploy & gửi duyệt: 3–5 ngày chờ
- ← pain: app chỉ mình host mở được (QR dev).
- Học: `zmp login` + `zmp deploy`; quản lý phiên bản trên dashboard; gửi duyệt từ trạng thái Testing; **xác thực chủ sở hữu từ EP01 giờ trả nợ** — đủ điều kiện gửi; các lý do reject phổ biến và cách đọc feedback trong dashboard.
- Thao tác thật: deploy thật, điền hồ sơ duyệt, bấm gửi. Kể thẳng thắn: chờ 3–5 ngày làm việc là một phần của đời mini app dev.
- AI sequence: nhờ AI soạn mô tả phiên bản + giải trình permission (bản thân bài học: viết cho người duyệt đọc) → host biên tập cho đúng sự thật → nộp.
- Thành quả: trạng thái "Chờ xét duyệt". → **pain mới: chờ duyệt xong — publish và vận hành ra sao.**
- File: `ep10-deploy-duyet/script.md`

### EP 11 — Go live, vận hành & tổng kết: quán có app riêng, tổng chi 0 đồng platform
- ← pain: được duyệt (hoặc xử lý xong feedback reject nếu có thật — quay thật) — còn bước cuối.
- Học: bấm Publish; QR dán tại bàn/cửa; tablet ở quầy chạy tab admin làm "màn hình bếp"; chi phí tổng: 0đ platform + Supabase free tier + thời gian; roadmap v2: Checkout SDK thanh toán, dine-in QR gọi món tại bàn, ZNS thông báo, Supabase Auth chuẩn hóa.
- Recap toàn series: kiến trúc cuối cùng 1 màn hình; 5 câu phỏng vấn mapping (webview vs native, super app distribution, RLS, denormalization, vì sao Edge Function giữ secret).
- AI moment kết: AI đóng vai interviewer hỏi "nếu 1000 đơn/ngày thì hệ thống này vỡ ở đâu?" → host trả lời bằng điểm yếu thật đã biết.
- Thành quả: người lạ tìm thấy app trong Zalo, đặt được bàn thật. Kết series bằng teaser đường đến bonus/v2.
- File: `ep11-go-live-tong-ket/script.md`

### EP 12 — Bonus trong mạch: Web app có sẵn thành Mini App trong 30 phút
- Tách khỏi phần bonus: đây là tập "mở rộng" có số riêng cho người xem có sẵn web app (kiểu vibe-expense). Dùng đường `zmp init` → "Use ZMP to deploy only" (docs chính thức có hướng dẫn). Demo trên một web React có thật. Recap cuối: kênh đã có cả backend (NestJS series) lẫn Mini App — cộng cả hai là full cycle sản phẩm Việt.
- File: `ep12-web-thanh-mini-app/script.md`

## BONUS

### Bonus B — Thanh toán trong Mini App: Checkout SDK
- v2 của app: tích Zalo Checkout SDK (repo chính thức checkout-sdk-tutorial làm mẫu); cần hộ kinh doanh cho KYB nhóm thanh toán; quy trình duyệt chặt hơn.
- File: `bonus-b-checkout-sdk/script.md`

## Nguyên tắc xuyên suốt series

1. Mỗi ep mở bằng NỖI ĐAU của ep trước (chain rule) — không bao giờ mở bằng "hôm nay ta học X".
2. Mỗi ep đúng MỘT AI sequence liền mạch — vài lượt hỏi–đáp phục vụ một outcome, không biến thành trình diễn tính năng AI.
3. **AI-Driven Development Workflow 6 bước** (giới thiệu lần đầu ở cuối EP01, sau milestone app chạy): Yêu cầu → Plan → Review → Approve → Thực hiện → Kiểm chứng. AI không bao giờ tự ý sửa.
4. Host tự gõ lại ít nhất một đoạn code AI sinh mỗi tập — "AI viết, mình hiểu".
5. Kết mỗi ep một câu teaser cho ep sau.
6. Tool AI: Opus trong IDE Antigravity 1.0; host prompt tiếng Việt cho dễ demo, nhắc viewers prompt tiếng Anh rẻ hơn.
7. Mọi lệnh CLI và prompt trong script phải được **probe thật trước khi quay** (cổng kiểm tra ở trên) — không script prompt mà CLI phiên bản hiện tại đã bỏ.
8. Title đánh số: `Zalo Mini App #NN: <hook> | Lập trình là cuộc sống`; thumbnail `#NN` góc cố định.

## Câu hỏi mở cần chốt trước khi viết EP01

- ~~Q1 — Tên quán/app~~ **ĐÃ CHỐT: "Gắp Thêm"** (repo `gap-them`). Lưu ý: trước khi tạo app thật ở EP01, host tự Google/Facebook search "Gắp Thêm" quán ăn 30 giây + để Zalo dashboard chặn trùng tên nếu có.
- ~~Q2 — Xác thực chủ sở hữu~~ **ĐÃ CHỐT: Cá nhân** (Zalo eKYC). Chuyện hộ kinh doanh giải thích bằng narration trong EP01 (khi nào cần HKD), không làm thật trên camera.
- **Q3 — Nhịp đăng:** xen kẽ với series NestJS đang chạy (1 NestJS : 1 Mini App/tuần) hay chạy riêng mùa mới? Ảnh hưởng đến việc EP10 có khớp lịch chờ duyệt 3–5 ngày thật hay không (nên quay trước, chèn cảnh chờ duyệt thật).
