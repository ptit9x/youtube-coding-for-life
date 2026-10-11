# EP03 — Khách bấm đặt bàn: định danh Zalo + SĐT một chạm | Zalo Mini App #3

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7–8 phút
- **Word count PART 1:** 649 từ (~6.8 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** đối chiếu docs ZaUI form components (DatePicker/Input) và docs `getPhoneNumber` phiên bản hiện hành trước khi quay.

## PART 1 — SCRIPT

Menu đã sống trong database. Nhưng thử đặt một bàn xem. Không được. App không biết mình là ai. Mỗi người mở app là một khách lạ không tên, và khách lạ thì không đặt bàn được.

Tập này gỡ hai chốt một lúc: cho app biết khách là ai, và làm cái form đặt bàn đầu tiên.

Định danh trước. Cách tệ nhất là bắt khách tự đăng ký: tên, mật khẩu, xác nhận mật khẩu, quên mật khẩu. Khách phở sáng nay chỉ muốn ăn, không muốn lập tài khoản. Cách tốt hơn nằm ngay trong Zalo. Ai mở Mini App thì đã có Zalo, và Zalo đã biết họ là ai. Mình gọi hai API: login lấy mã, getUserInfo lấy profile. Nôm na là OAuth thu nhỏ: app không bao giờ thấy mật khẩu Zalo của khách, chỉ nhận lại một định danh, zaloId, kèm tên và avatar. Mình gửi spec này cho Opus. Nó lên plan, mình review, có một chi tiết mình phải hỏi lại: zaloId do app tự khai, nói cách khác là có thể giả danh được. Nó xác nhận: đúng, nếu cần bảo mật thật thì phải xác thực phía server, vàseason sau mình sẽ làm cái đó qua Edge Function. Cho quán ba bàn, chấp nhận được. Mình ghi debt lên bảng, duyệt plan.

Một điều kiện bắt buộc: phải xin quyền trong dashboard Zalo. Mỗi quyền phải khai báo và được duyệt, xin cái nào phải dùng cái đó. Mình xin getUserInfo và getPhoneNumber.

getPhoneNumber là quyền nhạy cảm nhất trong danh sách. Nó lấy số điện thoại của khách, một chạm, khỏi gõ. Với quán thì vàng: có số là gọi xác nhận được. Với người duyệt thì dấu hỏi: app này lấy SĐT để làm gì? Đáp án phải thật: lưu lại để quán liên hệ xác nhận đặt bàn. Câu chữ đó đi vào phần giải trình khi nộp duyệt ở tập mười, nhớ giúp mình.

Code chạy: mở app, nút đăng nhập Zalo xanh hiện ra, bấm, cho phép, và header đổi thành đúng tên với avatar Zalo của mình. Dùng lại cho nút lấy SĐT: một chạm, ô số điện thoại điền sẵn.

Giờ form đặt bàn. Yêu cầu với Opus: ngày, giờ, số người, tên, số điện thoại, ghi chú. Kèm luật cũ. Nó lên plan nhanh gọn. Mình review. Và nó bỏ sót một thứ: khách chọn được ngày hôm qua. Form không có trí nhớ, nên phải tự hỏi: nếu khách gửi ngày quá khứ thì sao? Mình bắt lỗi, bảo nó thêm rule, nó sửa plan. Mình duyệt.

Phần form mình tự gõ, từ bản plan đã duyệt. Không phải nghi lễ, là cách nhanh nhất để mọi dòng code trên màn hình đều qua tay mình một lần. Date picker của ZaUI, time slot sinh từ giờ mở cửa của quán, sáu giờ sáng đến hai giờ trưa, bậc thang ba mươi phút. Số người thì bấm cộng trừ. Tất cả converdict components: React giữ giá trị, mình kiểm soát. Submit. Hiện modal: quán sẽ xác nhận qua số điện thoại này. Done.

Kiểm chứng kiểu tus: thử ngày hôm qua, ăn cờ chặn. Bỏ trống số điện thoại, ăn cờ chặn. Điền tử tế, submit, màn hình thành công. Mình mở Supabase. Một dòng mới trong bảng bookings. Tên mình, số mình, sáng mai bảy giờ, ba người. Đơn đặt bàn đầu tiên của quán, đi từ ngón tay khách tới database, không giấy note, không điện thoại.

Nhưng khoan. Đơn nằm trong database rồi. Phía quán thì sao? Mẹ mình không biết đọc dashboard Supabase. Người bán phở cần thứ khác: đơn mới tự chạy tới, có tiếng, nhìn là hiểu. Tập sau mình làm màn hình đó, và một tiếng ting đổi cách quán nhận khách. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen code (time-lapse 3–5s); giữ nguyên: prompt, review, host tự gõ form, ca test sai. Mở đầu 3–5s recap EP02 (menu thật chạy).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | App trong Zalo: menu thật load → bấm thử nút đặt bàn → disabled/vô danh, overlay "AI LÀ AI?" | Cold open | 25 |
| 2 | [DIAGRAM] | Hai lối: (a) form đăng ký dài dằng dặc nhiều bước vs (b) Zalo → zaloId; chọn (b) | "Định danh trước… OAuth thu nhỏ" | 30 |
| 3 | [BROWSER] | Dashboard mini.zalo.me → quản lý permission: tick getUserInfo + getPhoneNumber; zoom mô tả quyền | "Một điều kiện bắt buộc… xin cái nào phải dùng cái đó" | 30 |
| 4 | [IDE] | DÁN Prompt 1 → plan Opus: flow login/getUserInfo; host scroll, dừng ở mục "spoofable"; gõ câu hỏi chất vấn; AI xác nhận + ghi debt "Edge Function (EP04)" | "Mình gửi spec này cho Opus… duyệt plan" | 55 |
| 5 | [DIAGRAM] | Bảng trắng 2 cột: "Có Edge Function" vs "Chưa có — chấp nhận rủi ro v1"; gắn sticky "DEBT: EP04" | "Nó xác nhận… ghi debt lên bảng" | 20 |
| 6 | [PHONE] | App: nút "Đăng nhập với Zalo" → overlay consent → header hiện tên + avatar thật | "Code chạy… avatar Zalo của mình" | 25 |
| 7 | [DIAGRAM] | Zoom 1 slide: getPhoneNumber = quyền nhạy cảm; 2 dòng: khách được gì / người duyệt hỏi gì; caption giải trình nộp duyệt | "getPhoneNumber là quyền nhạy cảm nhất… nhớ giúp mình" | 30 |
| 8 | [PHONE] | Nút "Lấy SĐT" → 1 chạm → ô input tự điền số | "Dùng lại cho nút lấy SĐT…" | 15 |
| 9 | [IDE] | DÁN Prompt 2 (form plan) → plan hiện; host review, khoanh "thiếu rule ngày quá khứ" → gõ yêu cầu bổ sung → AI sửa plan → approved | "Giờ form đặt bàn… nó sửa plan. Mình duyệt" | 50 |
| 10 | [IDE] | Host TỰ GÕ form (booking.tsx): DatePicker, timeslot generator, stepper số người; quay thật, tốc độ tối đa 1.2x | "Phần form mình tự gõ… qua tay mình một lần" | 60 |
| 11 | [PHONE] | Test case: chọn ngày hôm qua → toast chặn; bỏ trống SĐT → toast chặn | "Kiểm chứng kiểu tus… ăn cờ chặn" | 25 |
| 12 | [PHONE] | Điền tử tế → submit → màn hình thành công; [BROWSER] Supabase table bookings: dòng mới highlight — KHÔNG cắt, giữ nguyên nhịp | "Điền tử tế… không điện thoại" | 30 |
| 13 | [B-ROLL] | Quầy quán phở thật / tô phở bốc khói; overlay "TẬP 4: QUÁN CÓ TIẾNG TING" | Teaser + CTA | 15 |

**Tổng: 410 giây ≈ 6,8 phút hình.**

**Batch-record:** scene 3+7 một phiên browser; scene 4+9 một phiên IDE; scene 10 quay riêng trọn take; scene 1+6+8+11+12 một phiên phone sau khi code xong.

---

## Prompt cho Opus

### Prompt 1 — Định danh Zalo (scene 4)

```
Bối cảnh: Mini App "Chan Thêm" (quán phở 3 bàn), menu đã chạy Supabase (EP02).
Cần định danh người dùng để làm đặt bàn + voucher "của tôi".

Nhiệm vụ: lên plan tích hợp định danh Zalo: login() lấy mã, getUserInfo lấy
profile (zaloId, name, avatar). Trình flow gọi, nơi lưu zaloId, và rủi ro bảo
mật của việc tin zaloId phía client.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
Plan phải có mục rủi ro nói rõ zaloId client-side có thể bị giả danh;
gợi ý hướng khắc phục để mình cân nhắc cho tập sau.
```

### Prompt 2 — Form đặt bàn (scene 9)

```
Bối cảnh: đã có zaloId + getPhoneNumber (1 chạm). Bảng bookings (id, zalo_id,
name, phone, book_date, book_time, party_size, note, status, created_at) đã tồn
tại trong Supabase, RLS cho anon INSERT.

Nhiệm vụ: lên plan form đặt bàn: DatePicker, time slot sinh từ giờ mở cửa
(06:00–14:00, bước 30 phút), stepper số người (1–12), tên, SĐT (nút 1 chạm),
ghi chú. Validation client: không nhận ngày quá khứ, SĐT đủ 10 số, tên không trống.

QUY TẮC: trình PLAN trước, chờ approve, chưa sửa file.
```

Lưu verbatim tại `code/prompt-ep03.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a young Vietnamese developer holding a smartphone showing a blue login button with a Zalo-style avatar appearing at the top of a food app, dark room lit by monitor glow, steam from a bowl of pho in the foreground, dramatic Zalo blue neon accents, shallow depth of field, bokeh city lights, 8k, photorealistic, high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic close-up photograph of a hand tapping a glowing blue button on a phone screen in a dark room, a consent dialog floating holographically above the phone with Vietnamese text, neon blue rim lighting, deep navy background, high contrast, 8k, photorealistic, developer documentary style. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of a phone displaying a clean booking form with a calendar and time slots beside a real steaming bowl of pho on a wooden restaurant table at dawn, soft blue tech glow contrasting warm morning light, shallow depth of field, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #3: Khách đặt bàn bằng chính tài khoản Zalo | Lập trình là cuộc sống`
2. `Zalo Mini App #3: Lấy số điện thoại khách trong một chạm | Lập trình là cuộc sống`
3. `Zalo Mini App #3: Đơn đặt bàn đầu tiên rơi vào database | Lập trình là cuộc sống`
4. `Zalo Mini App #3: Không mật khẩu, không đăng ký — Zalo lo | Lập trình là cuộc sống`
5. `Zalo Mini App #3: AI quên chống ngày quá khứ, mình bắt | Lập trình là cuộc sống`

### 4b. SEO Description

```
App biết menu nhưng không biết khách là ai. Tập 3: định danh bằng chính tài khoản Zalo (login + getUserInfo), lấy SĐT một chạm, và ra đơn đặt bàn đầu tiên — từ ngón tay khách tới database.

✅ login() + getUserInfo: OAuth thu nhỏ, app không thấy mật khẩu Zalo
✅ zaloId: định danh ổn định; nói thẳng rủi ro spoof — debt trả ở EP04
✅ Xin permission trong dashboard: xin cái nào phải dùng cái đó
✅ getPhoneNumber: quyền nhạy cảm nhất — và câu giải trình khi nộp duyệt
✅ Form đặt bàn: AI lên plan, host bắt lỗi "chọn được ngày hôm qua"
✅ Kiểm chứng: ca sai bị chặn, đơn thật nằm trong bảng bookings

Links:
- Zalo JS APIs: https://mini.zalo.me/docs
- Supabase: https://supabase.com

Timestamps:
00:00 Khách lạ không tên
00:25 Hai lối định danh, chọn lối Zalo
00:55 Xin quyền trong dashboard
01:25 AI lên plan + sự thật về zaloId
02:45 Đăng nhập Zalo trong app
03:10 Quyền nhạy cảm nhất: SĐT một chạm
03:55 AI quên ngày quá khứ
04:45 Host tự gõ form
05:45 Test sai, test đúng
06:15 Đơn đầu tiên vào database
06:40 Quán cần tiếng ting (teaser)

#ZaloMiniApp #Zalo #vibecoding #laptrinh #React #OAuth #getUserInfo #getPhoneNumber #LapTrinhLaCuocSong #aiagent #form #datban
```

### 4c. Keywords

```
zalo mini app, dinh danh zalo, login zalo api, getuserinfo zalo, getphonenumber zalo, quyen zalo mini app, oauth don gian, zaloId, form dat ban, react form validation, controlled components, date picker, vibe coding, ai lam app, vibe coding tieng viet, dat ban nha hang, app dat mon, supabase insert, lap trinh la cuoc song, developer viet nam
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#03` góc trên phải.

### Option 1 — "KHÔNG MẬT KHẨU / VẪN BIẾT LÀ AI"
- Image: Prompt 1. Text: `KHÔNG MẬT KHẨU` (trắng, 2 dòng) / `BIẾT LÀ AI` (blue) + badge `#03`.

### Option 2 — "MỘT CHẠM / LẤY SỐ ĐIỆN THOẠI"
- Image: Prompt 2. Text: `MỘT CHẠM` (trắng) / `LẤY SĐT` (blue) + badge `1 TAP` nhỏ.

### Option 3 — "ĐƠN ĐẦU TIÊN / VÀO DATABASE"
- Image: Prompt 3. Text: `ĐƠN ĐẦU TIÊN` (trắng) / `VÀO DB` (blue) + badge `#03`.

Typography: như EP01/EP02 (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
