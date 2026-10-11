# EP12 — Bonus trong mạch: Web app có sẵn thành Mini App trong 30 phút | Zalo Mini App #12

- **Trạng thái:** 📝 script draft — chờ host duyệt (chún quay)
- **Runtime mục tiêu:** ~6–7 phút (tập mở rộng, nhẹ hơn)
- **Word count PART 1:** 528 từ (~5.6 phút thoại)
- **Demo app:** một web React có sẵn (gợi ý: một app nhỏ của kênh — không dùng vibe-expense vì có auth/Phó tạp; demo đơn giản thuần UI + fetch)
- **Pre-flight:** chạy `zmp init` đường "Use ZMP to deploy only" trên app demo THẬT trước khi quay — ghi lại đúng prompt và file sinh ra.

## PART 1 — SCRIPT

Mùa chính khép lại ở tập mười một. Tập hôm nay dành cho một nhóm người cụ thể: bạn đã có web app chạy rồi, giờ muốn nó lên Zalo. Không scaffold lại từ đầu. Không viết lại. Ba mươi phút.

Con đường này chính hãng, ít ai biết. zmp init có hai chế độ. Tạo mới, cái mình dùng suốt mười một tập. Và chế độ thứ hai: Use ZMP to deploy only. Dịch thô: ZMP chỉ lo phần đóng gói và phát hành, code của bạn giữ nguyên. Hỗ trợ chính thức của Zalo, có cả bài hướng dẫn "chuyển đổi web app thành Zalo Mini App trong 30 phút" trên docs.

Mình lấy một app React nhỏ có thật: một trang quản lý chi tiêu demo tự viết hồi trước, thuần React, chạy Vite, có fetch data. Làm mẫu cho số đông: đa số web app của dev Việt viết React, và React là chuẩn của Mini App luôn.

Ba điều kiện nhập môn, nói trước để bạn tự soi. Một: app phải chạy được trên mobile, vì Mini App sống trong webview màn hình dọc. Web chỉ đẹp trên desktop là hơi khó. Hai: root DOM phải là div id app. Vite mặc định sinh div id root, đổi một chữ. Ba: mọi tính năng gọi năng lực hệ thống, camera, vị trí, chia sẻ, phải đi qua ZJSBridge thay vì API trình duyệt. App thuần UI như demo này gần như không chạm tới.

Chạy thử. Vào thư mục app, gõ zmp init. Nó hỏi Mini App ID — tài khoản và app mình tạo từ tập một dùng lại được. Chọn phương thức đăng nhập, chọn chế độ deploy only, đặt tên. Xong. Git status cho thấy vài file mới: app-config.json là hộ chiếu của app trên Zalo, zmp-cli.json vài dòng config build. Code cũ: chạm đúng một chữ, root thành app.

Chạy zmp start. Trình duyệt mở localhost ba nghìn. App chi tiêu của mình, nguyên vẹn, giao diện cũ, data cũ, chạy trong khung Mini App. Quét mã QR: mở trong Zalo thật. Từ web tới Mini App, ba mươi phút đúng như docs hứa.

Nhưng nói thật phần việc còn lại, để tập này không thành quảng cáo. Ba mươi phút đó đưa app LÊN được Zalo, chưa chắc đưa app VÀO được tim người dùng. Thiết kế phải học theo ZaUI mới giống hệ sinh thống. Màn hình phải chịu được webview: fonts, scroll, nút back. Quy trình duyệt vẫn nguyên: nội dung thật, permission khớp, dưới mười megabyte. Chuyển đổi nhanh, nghiêm túc thì vẫn phải tuning.

Đoạn cuối, dọn dẹp cả series. Ai theo đủ mười một tập giờ cầm trong tay một vòng đầy: kênh đã có loạt series backend với NestJS, giờ thêm Mini App trên Zalo. Backend tự viết cộng Mini App chạy frontend chính là kiến trúc của phần lớn sản phẩm Việt Nam thật: API của mình, siêu app của người khác, khách hàng của mọi người. Hẹn gặp lại ở mùa thanh toán, Checkout SDK, và mấy cái app nữa. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ install/gen (time-lapse 3–5s); giữ nguyên: prompt CLI, cảnh git status, cảnh mở trong Zalo. Mở đầu 3–5s recap EP11 (publish + quán).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [BROWSER] | Web app demo (chi tiêu) chạy trên desktop; rồi thu nhỏ cửa sổ → méo mó trên mobile (devtools); overlay "ĐÃ CÓ WEB APP?" | Cold open | 25 |
| 2 | [BROWSER] | Docs Zalo trang chuyển đổi web → mini app; zoom dòng "30 phút" + "Use ZMP to deploy only" | "Con đường này chính hãng… trên docs" | 25 |
| 3 | [DIAGRAM] | 3 điều kiện: mobile-first / div#app / ZJSBridge; kèm ảnh minh họa từng cái | "Mình lấy một app React… không chạm tới" | 40 |
| 4 | [TERM]+[IDE] | `cd demo-app` → `zmp init` → các prompt hiện ra (zoom từng prompt: Mini App ID → login → deploy only → tên); Enter | "Chạy thử… đặt tên" | 40 |
| 5 | [TERM]+[IDE] | `git status`: vài file mới (app-config.json, zmp-cli.json…); mở app-config.json; [IDE] đổi `id="root"` → `id="app"` — ZOOM chữ đổi | "Xong. Git status… root thành app" | 35 |
| 6 | [TERM]+[PHONE] | `zmp start` → localhost:3000 app nguyên vẹn; quét QR → mở trong Zalo thật (giữ cảnh) | "Chạy zmp start… đúng như docs hứa" | 35 |
| 7 | [DIAGRAM] | "Phần việc còn lại" checklist: ZaUI look, webview quirks (font/scroll/back), duyệt + <10MB; caption "chuyển đổi nhanh, tuning thì không" | "Nhưng nói thật… vẫn phải tuning" | 35 |
| 8 | [DIAGRAM] | Bản đồ kênh: NestJS series (backend) + series này (Mini App) = kiến trúc sản phẩm Việt: API mình, siêu app người khác | "Đoạn cuối… khách hàng của mọi người" | 30 |
| 9 | [B-ROLL] | Đóng laptop, kéo ghế; overlay "MÙA THANH TOÁN — COMING SOON" | Kết + CTA | 15 |

**Tổng: 280 giây ≈ 4,7 phút hình** + thoại → runtime ~6,5 phút.

**Batch-record:** scene 2 một phiên browser; scene 4+5+6 MỘT phiên liền mạch terminal→IDE→phone (làm thật 1 lần); scene 1 dùng app demo chuẩn bị trước.

---

## Prompt cho Opus

Tập này không có AI code sequence chính — beat AI của tập là **tư vấn checklist tuning** (scene 7):

```
Bối cảnh: mình vừa chuyển một web app React (Vite, thuần UI + fetch) thành
Zalo Mini App bằng "Use ZMP to deploy only". App chạy được nhưng còn nguyên
nhìn giống web.

Nhiệm vụ: lên checklist tuning sau chuyển đổi, xếp theo ảnh hưởng trải
nghiệm: (1) khác biệt webview Zalo vs trình duyệt thường (font, scroll,
nút back, safe-area), (2) nên ZaUI- hóa những thành phần nào trước,
(3) reminded duyệt phát hành: nội dung/permission/bundle. Không code —
tư vấn ngắn, mỗi mục 1–2 câu.
```

Lưu verbatim tại `code/prompt-ep12.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a web application on a laptop screen transforming into a mobile app on a phone, morphing light particles flowing from laptop to phone, dark room with neon blue transformation glow, shallow depth of field, 8k, photorealistic, high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic close-up photograph of a terminal screen showing a file diff changing id="root" to id="app" with the changed line glowing neon blue, a mechanical keyboard in the foreground, dark moody room, 8k, photorealistic, developer documentary. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of two screens side by side: a desktop web dashboard on the left and the same app running inside a chat super-app on a phone on the right, a glowing 30-minute hourglass between them, dramatic blue lighting, deep navy background, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #12: Web app có sẵn → Mini App trong 30 phút | Lập trình là cuộc sống`
2. `Zalo Mini App #12: zmp init đườngdeploy only — code giữ nguyên | Lập trình là cuộc sống`
3. `Zalo Mini App #12: Đã có web React? Đưa lên Zalo không viết lại | Lập trình là cuộc sống`
4. `Zalo Mini App #12: 30 phút lên Zalo, nhưng tuning thì không | Lập trình là cuộc sống`
5. `Zalo Mini App #12: API mình, siêu app người khác — kiến trúc sản phẩm Việt | Lập trình là cuộc sống`

### 4b. SEO Description

```
Bạn đã có web app rồi? Không cần viết lại. Tập bonus: đường "Use ZMP to deploy only" chính hãng của zmp-cli — đưa web React lên Zalo trong 30 phút, đổi đúng 1 chữ trong code.

✅ zmp init 2 chế độ: tạo mới (mùa chính) vs deploy only (tập này)
✅ 3 điều kiện nhập môn: mobile-first, div#app, ZJSBridge
✅ File sinh ra: app-config.json + zmp-cli.json — code cũ chạm 1 chữ
✅ Demo thật: web chi tiêu React+Vite → mở trong Zalo qua QR
✅ Nói thật phần còn lại: ZaUI- hóa, webview quirks, duyệt vẫn nguyên
✅ Bản đồ kênh: NestJS backend + Mini App = kiến trúc sản phẩm Việt

Links:
- Docs chuyển đổi: https://mini.zalo.me/docs
- Series backend NestJS: playlist kênh

Timestamps:
00:00 Đã có web app?
00:25 Đường chính hãng ít ai biết
01:10 Ba điều kiện nhập môn
01:50 zmp init deploy only — chạy thật
02:30 Git status: vài file, 1 chữ đổi
03:05 App nguyên vẹn trong Zalo
03:40 30 phút lên, tuning thì không
04:15 API mình, siêu app người khác
04:45 Mùa thanh toán (teaser)

#ZaloMiniApp #vibecoding #laptrinh #React #Vite #zmp #LapTrinhLaCuocSong #webapp #deploy #indiedev
```

### 4c. Keywords

```
zalo mini app, chuyen web app thanh mini app, zmp init deploy only, use zmp to deploy only, web react len zalo, div id app, zjsbridge, webview zalo, tuning mini app, zaui components, 30 phut len zalo, kien truc san pham viet, nestjs backend, vibe coding, lap trinh la cuoc song
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#12 • BONUS` góc trên phải.

### Option 1 — "WEB CÓ SẴN / 30 PHÚT LÊN ZALO"
- Image: Prompt 1. Text: `WEB CÓ SẴN` (trắng) / `30 PHÚT LÊN ZALO` (blue, 2 dòng) + badge `KHÔNG VIẾT LẠI`.

### Option 2 — "ĐỔI 1 CHỮ / THÀNH MINI APP"
- Image: Prompt 2. Text: `ĐỔI 1 CHỮ` (trắng) / `THÀNH MINI APP` (blue) + badge `#12`.

### Option 3 — "API MÌNH / SIÊU APP NGƯỜI KHÁC"
- Image: Prompt 3. Text: `API MÌNH` (trắng) / `SIÊU APP NGƯỜI KHÁC` (blue, 2 dòng) + badge `KIẾN TRÚC VIỆT`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
