# EP10 — Deploy & gửi duyệt: 3–5 ngày chờ | Zalo Mini App #10

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7 phút
- **Word count PART 1:** 540 từ (~5.7 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** `zmp login` + `zmp deploy` chạy thật trước 1 lần để biết flow; xác thực chủ sở hữu (Cá nhân/eKYC) đã xong từ EP01 — kiểm tra lại trạng thái trước camera.

## PART 1 — SCRIPT

Chín tập code. Hôm nay gần như không code gì hết. Chỉ có một lệnh deploy, một tờ hồ sơ, một nút bấm. Và một kiểu lo mà dev nào cũng biết: lo bị từ chối.

Bắt đầu. zmp login: trình duyệt mở ra, đăng nhập đúng tài khoản Zalo đã tạo app ở tập một. Rồi zmp deploy. Bundle tám phẩy ba megabyte đẩy lên máy chủ Zalo. Vài chục giây, xong. Không fanfare, không confetti. Trên dashboard mini.zalo.me, phiên bản vừa đẩy nằm ở trạng thái Testing. Nghĩa là: chỉ mình và danh sách tester xem được. Khách chưa.

Đoạn giờ là phần giấy tờ, và giấy tờ ở đây chính là sản phẩm. Phiên bản Testing có nút gửi xét duyệt. Bấm vào, Zalo hỏi mấy thứ. Mô tả phiên bản: viết gì, đổi gì so với bản trước. Với mình là bản đầu: khai trừng. Tài khoản test cho người duyệt. Và phần dễ bị đánh rớt nhất: giải trình từng permission.

Giấy phép lấy số điện thoại, họ sẽ hỏi lấy làm gì. Câu trả lời phải trùng với những gì app thật sự làm: lưu số điện thoại để quán liên hệ xác nhận đặt bàn. Viết khác đi một chút cho hay, người duyệt mở app ra đối chiếu, thấy lệch, từ chối. Nên mình nhờ Opus soạn giúp bản nháp giải trình, rồi mình ngồi sửa từng câu cho đúng sự thật đến từng chữ. AI viết nhanh, nhưng người ký tên là mình.

Bấm gửi. Trạng thái đổi: Chờ xét duyệt. Và rồi thì hết việc. Thật sự hết việc. Đây là chuỗi ngày lạ nhất của series: không có gì để làm. Ba đến năm ngày làm việc. App nằm trong hàng chờ của một nơi mình không nhìn thấy, người ta duyệt theo thứ tự và tiêu chuẩn mình không kiểm soát.

Cảm giác đó quen thuộc mà khó tả. Giống merge PR vào repo của người khác: mình làm xong phần mình, giờ quyền nằm ở chỗ khác. Dev gọi nó theo nhiều tên, nhưng bản chất là một thứ: chờ phán quyết về thứ mình đã chăm sóc.

Nên mình kể chuyện việc gì xảy ra lúc chờ, để tập này không chỉ là bài hướng dẫn nộp hồ sơ. Vụ từ chối nổi tiếng nhất mà ai làm Mini App cũng nên biết: bản bị trả lại không phải bản xấu. Lý do từ chối hiện ngay trong dashboard, cụ thể đến từng màn. Tụi mình được sửa và gửi lại không giới hạn, mỗi vòng giáo dục app của mình trưởng thành một bậc. Từ chối là review miễn phí, chỉ khác là review chậm.

Và để series không dừng ở chỗ chờ: trong lúc chờ duyệt, mình quay trước tập mười một, phần vận hành. Chuẩn bị QR in dán quầy, tablet cho mẹ, hướng dẫn ba dòng. Khi tin Đã duyệt tới, mọi thứ chỉ còn một nút: Publish.

Nếu bạn xem tới đây cùng mình: app của quán nhà mình, chín tập rưỡi công sức, đang nằm trong hàng chờ của Zalo. Tập sau: nút Publish, ngày đầu tiên khách lạ đặt bàn thật, và bài tổng kết cả series. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: deploy thật, hồ sơ thật, nút bấm thật — tập này không dàn dựng được gì, mọi cảnh là capture thật. Chờ duyệt là cảnh "đời" (notification/email) — quay thật khi xảy ra, chèn ở EP11 nếu cần. Mở đầu 3–5s recap EP09 (checklist 100%).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [TERM] | Terminal trống + host gõ chậm `zmp login` → browser mở → đăng nhập → quay lại terminal "logged in" | "Bắt đầu. zmp login…" | 30 |
| 2 | [TERM]+[BROWSER] | `zmp deploy` → progress đẩy bundle (giữ cảnh push %, cắt phần chờ) → xong; dashboard mini.zalo.me hiện phiên bản Testing | "Rồi zmp deploy… Khách chưa" | 35 |
| 3 | [DIAGRAM] | Ba trạng thái vòng đời: Testing → Chờ xét duyệt → Đã duyệt/Publish; minh họa ai thấy được ở mỗi trạng thái | "Đoạn giờ là phần giấy tờ… bản đầu: khai trừng" | 30 |
| 4 | [BROWSER] | Dashboard: form gửi duyệt — điền mô tả phiên bản (host gõ thật, quaytay chậm), tài khoản tester, upload ảnh chụp màn hình | "Bấm vào, Zalo hỏi mấy thứ… dễ bị đánh rớt nhất" | 45 |
| 5 | [IDE] | DÁN Prompt 1 (soạn giải trình permission) → bản nháp Opus; host sửa TỪNG CÂU bên cạnh, đọc to vài chỗ sửa | "Giấy phép lấy số điện thoại… người ký tên là mình" | 50 |
| 6 | [BROWSER] | **Nút bấm — không cắt:** dán giải trình vào form → check lại lần cuối → bấm "Gửi xét duyệt" → trạng thái đổi "Chờ xét duyệt"; giữ im 3 giây | "Bấm gửi. Trạng thái đổi… hết việc" | 30 |
| 7 | [B-ROLL] | Cà phê nguống, màn hình dashboard im lìm, đồng hồ; overlay "3–5 NGÀY LÀM VIỆC" | "Và rồi thì hết việc… tiêu chuẩn mình không kiểm soát" | 30 |
| 8 | [DIAGRAM] | Dashboard feedback reject mẫu: danh sách lý do cụ thể từng màn; mũi tên "sửa → gửi lại → duyệt lại"; caption "review miễn phí, review chậm" | "Vụ từ chối nổi tiếng… trưởng thành một bậc" | 40 |
| 9 | [B-ROLL] | Chuẩn bị vận hành: QR in thử, tablet mở tab admin, mẹ cầm máy; overlay "REHEARSAL NGÀY ĐẦU" | "Và để series không dừng… một nút: Publish" | 25 |
| 10 | [B-ROLL] | Đóng máy, ghế trống, đèn tắt dần; overlay "TẬP 11: PUBLISH" | Teaser + CTA | 15 |

**Tổng: 330 giây ≈ 5,5 phút hình** + thoại dày → runtime ~7 phút.

**Batch-record:** scene 1+2+4+6 là MỘT phiên dashboard/terminal liền mạch — bấm thật 1 lần, không diễn lại; scene 5 một phiên IDE; scene 7+9+10 b-roll quay thời gian thật.

**Lưu ý sản xuất:** theo plan mùa riêng — bấm gửi duyệt THẬT ở cuối buổi quay batch, rồi quay tiếp các tập khác; cảnh "Đã duyệt" (email/notification) capture thật khi tới, chèn vào EP11.

---

## Prompt cho Opus

### Prompt 1 — Soạn giải trình permission (scene 5)

```
Bối cảnh: Mini App "Chan Thêm" (quán phở) gửi duyệt phát hành trên Zalo.
App xin 3 quyền: getUserInfo (hiện tên/avatar trong app), getPhoneNumber
(điền SĐT khi đặt bàn), share (gửi voucher cho bạn bè).

Nhiệm vụ: soạn bản nháp phần "giải trình mục đích sử dụng quyền" cho từng
permission trong form gửi duyệt. Mỗi quyền 2–3 câu, tiếng Việt, nói đúng
thực tế app làm. Mục tiêu: người duyệt đọc xong hiểu quyền đó dùng ở màn
nào, cho ai, vì sao cần.

KHÔNG bịa công năng app không có. Nếu thiếu thông tin thì hỏi mình trước.
```

Lưu verbatim tại `code/prompt-ep10.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a developer's hand hovering over a mouse, the screen showing a glowing blue submit button that reads like a final decision, dark room, dramatic side lighting, a pho bowl steaming at the edge of the desk, tense cinematic mood, shallow depth of field, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of an empty office chair at 2 AM, monitors still glowing with a dashboard status bar that says waiting, blue light spilling on the desk with cold coffee, city bokeh through the window, melancholic documentary mood, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic close-up photograph of a phone notification glowing in the dark with a blue check mark, held by tense hands, screen light illuminating the face of a young Vietnamese developer at night, shallow depth of field, 8k, photorealistic, documentary style. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #10: Bấm gửi duyệt rồi — giờ chỉ còn chờ | Lập trình là cuộc sống`
2. `Zalo Mini App #10: Giải trình permission: AI viết nháp, mình ký tên | Lập trình là cuộc sống`
3. `Zalo Mini App #10: Từ chối là review miễn phí, chỉ là review chậm | Lập trình là cuộc sống`
4. `Zalo Mini App #10: Deploy thật — bundle bay lên máy chủ Zalo | Lập trình là cuộc sống`
5. `Zalo Mini App #10: 3–5 ngày dài nhất của series | Lập trình là cuộc sống`

### 4b. SEO Description

```
Chín tập code, hôm nay gần như không code: một lệnh deploy, một tờ hồ sơ, một nút bấm — và 3–5 ngày chờ phán quyết. Tập 10: deploy thật, điền hồ sơ thật, bấm gửi thật.

✅ zmp login + zmp deploy: bundle lên máy chủ Zalo, trạng thái Testing
✅ Vòng đời phiên bản: Testing → Chờ xét duyệt → Đã duyệt → Publish
✅ Phần dễ rớt nhất: giải trình từng permission — viết đúng thật app làm
✅ AI soạn nháp, host sửa từng câu: người ký tên là mình
✅ Bị từ chối = review miễn phí: lý do cụ thể trong dashboard, sửa gửi lại
✅ Trong lúc chờ: rehearsal vận hành (QR, tablet, mẹ)

Timestamps:
00:00 Tập ít code nhất, lo nhất
00:30 zmp login + deploy thật
01:35 Ba trạng thái phiên bản
02:05 Điền hồ sơ gửi duyệt
03:00 AI viết nháp, mình ký tên
03:50 Bấm gửi — hết việc thật sự
04:20 Cảm giác chờ phán quyết
05:00 Từ chối là review miễn phí
05:40 Rehearsal ngày đầu (teaser)

#ZaloMiniApp #vibecoding #laptrinh #deploy #zmp #appreview #LapTrinhLaCuocSong #permission #aiagent #indiedev #publish
```

### 4c. Keywords

```
zalo mini app, zmp deploy, zmp login, gui duyet zalo, xet duyet mini app, trang thai testing, giai trinh quyen, permission giai trinh, bi tu choi duyet, review mien phi, cho duyet 3 ngay, deploy that, publish mini app, vibe coding, lap trinh la cuoc song, indie developer viet
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#10` góc trên phải.

### Option 1 — "BẤM GỬI / RỒI CHỜ"
- Image: Prompt 1. Text: `BẤM GỬI` (trắng) / `RỒI CHỜ` (blue) + badge `3–5 NGÀY`.

### Option 2 — "3–5 NGÀY / DÀI NHẤT SERIES"
- Image: Prompt 2. Text: `3–5 NGÀY` (trắng) / `DÀI NHẤT` (blue) + badge `#10`.

### Option 3 — "TỪ CHỐI = / REVIEW MIỄN PHÍ"
- Image: Prompt 3 (biến thể icon ✗). Text: `TỪ CHỐI` (trắng) / `REVIEW MIỄN PHÍ` (blue) + badge `SỬA GỬI LẠI`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
