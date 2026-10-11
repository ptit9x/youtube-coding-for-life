# EP06 — Hết món: tắt một nút ở quầy, menu sống lại trên tay khách | Zalo Mini App #6

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7 phút
- **Word count PART 1:** 638 từ (~6.7 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** chuẩn bị 2 thiết bị (phone khách + tablet admin) như EP04; verify hành vi Realtime cho UPDATE (không chỉ INSERT).

## PART 1 — SCRIPT

Sáu giờ sáng, nồi nước dùng vừa xong. Bánh phở hôm nay giao thiếu. Mẹ chửi nhẹ một tiếng, rồi cứ bán. Mười một giờ, khách đặt tô, bếp trả lời: hết bánh rồi em. Khách đứng dậy đi quán khác. Ba lần một tuần như thế.

App hôm nay phải học được câu "hết". Và học từ đúng người: người đứng sau nồi nước dùng.

Cấu trúc thì đã có sẵn từ tập hai: cờ available trong bảng dishes, hiện đang nằm im. Việc còn lại là nối nó vào hai đầu. Đầu quầy: một công tắc trong tab admin, bấm là tắt món. Đầu khách: menu realtime, món tắt thì mờ đi, gắn chữ hết món, và giỏ hàng từ chối thêm món đó.

Mình gửi spec này cho Opus, kèm một chi tiết mình đoán trước được: nó sẽ chọn cách an toàn nhất, tải lại menu từ đầu khi có thay đổi. Cách đó chạy được, nhưng chatté. Mình yêu cầu nó nghĩ thêm: có cách nào chỉ đổi đúng dòng món bị tắt, không render lại cả danh sách không? Nó đề xuất optimistic UI. Dịch nôm na: bấm trước, tin sau. Người dùng bấm công tắc, giao diện đổi ngay lập tức, rồi request mới đi đi. Nếu server xác nhận, ổn thỏa. Nếu fail, giao diện lùi về như cũ.

Và chính chỗ đó sinh ra một tình huống rất đời: hai chuyện xảy ra cùng lúc. Mẹ tắt món tô đặc biệt. Cùng giây đó, một khách đang có tô đặc biệt trong giỏ, chuẩn bị bấm gửi. Đơn đó tính sao? Đây là bài toán race condition, hai dòng dữ liệu đua nhau, và nó không chỉ nằm trong sách: quán nào cũng gặp, ngày nào cũng gặp.

Quy tắc xử lý phải rõ ràng, không được để code tự quyết. Mình chọn: quầy thắng. Nếu món bị tắt giữa chừng, giỏ của khách bỏ món đó ra, kèm một dòng xin lỗi nhỏ: món vừa hết, xin chọn món khác. Đắng một chút cho khách, nhưng nhẹ hơn nhiều so với đặt xong mới biết không có. Còn về data, một ràng buộc ở Edge Function khi nhận đơn: rà từng món trong giỏ, món nào đã tắt thì loại khỏi đơn trước khi ghi. Server là trọng tài cuối cùng, client chỉ là bảng tin.

Plan có đủ ba mảnh: công tắc admin, menu realtime mờ món, và xử lý va chạm giỏ hàng. Mình duyệt. AI code. Vài phút sau, buổi diễn bắt đầu.

Tablet ở quầy, điện thoại ở tay khách. Mình bấm tắt tô đặc biệt trên tablet. Không quá hai giây, màn hình điện thoại: tô đặc biệt mờ đi, gắn nhãn hết món. Không F5. Không tải lại. Khách muốn thêm cũng không được, nút cộng đã khóa.

Rồi màn race: mình để tô đặc biệt trong giỏ trên điện thoại, chạy sang tablet bấm tắt, quay lại điện thoại bấm gửi đơn. App bỏ tô đặc biệt ra, hiện dòng: món vừa hết, xin chọn món khác. Đơn gửi đi chỉ còn phần còn sống. Đúng như thiết kế: quầy thắng, khách được báo, data sạch.

Sáu giờ sáng mai, khi xe bánh phở lại giao thiếu, mẹ bấm một nút. Cả menu của quán, trên mọi chiếc điện thoại của mọi khách, tự biết điều trong hai giây. Giá trị của một nút bấm, đong bằng số lần khách không phải đứng dậy đi nữa.

Quán giờ chạy trơn từ khách tới bếp. Nhưng nhìn lại: khách ăn xong đi luôn, không có gì níu. Không có lý do mở lại app lần sau. Tập sau mình gắn hai thứ níu chân: voucher cho khách, và trang blog cho quán kể chuyện. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen (time-lapse 3–5s); giữ nguyên: prompt, 2 cảnh hai thiết bị. Mở đầu 3–5s recap EP05 (giá đóng băng). Cảnh bếp thật đầu tập cần quay ngoài giờ hoặc dùng footage quán.

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [B-ROLL] | Bếp quán sáng sớm: nồi nước dùng bốc khói, khay bánh phở trống; overlay "6:00 — HẾT BÁNH PHỞ" | Cold open | 25 |
| 2 | [DIAGRAM] | Sơ đồ 2 đầu: công tắc admin → dishes.available → menu khách mờ + giỏ chặn; liền mạch realtime | "Cấu trúc thì đã có sẵn… hai đầu" | 30 |
| 3 | [IDE] | DÁN Prompt 1 (toggle + realtime + optimistic) → plan Opus (có mục optimistic UI + xử lý race) → host scroll review → approved | "Mình gửi spec… tin sau" | 45 |
| 4 | [DIAGRAM] | Timeline race: t=0 quầy tắt món ‖ t=0 khách có món trong giỏ → va chạm → 3 luật: quầy thắng / khách được báo / server trọng tài | "Và chính chỗ đó… ngày nào cũng gặp" | 40 |
| 5 | [IDE] | Zoom phần plan xử lý giỏ: bỏ món + dòng xin lỗi + ràng buộc Edge Function rà lại trước khi ghi; host gõ 1 câu chốt "quầy thắng" → approved | "Quy tắc xử lý phải rõ ràng… bảng tin" | 30 |
| 6 | [PHONE]+[TABLET] | **Cảnh chủ lực:** bấm tắt trên tablet → điện thoại: món mờ + badge "Hết món" + nút cộng khóa (≤2 giây) | "Tablet ở quầy… nút cộng đã khóa" | 30 |
| 7 | [PHONE]+[TABLET] | **Cảnh race:** giỏ có tô đặc biệt → chạy sang tablet tắt → quay lại phone bấm gửi → app bỏ món, hiện dòng xin lỗi, đơn gửi phần còn lại | "Rồi màn race… data sạch" | 40 |
| 8 | [B-ROLL] | Quầy quán + phone menu; overlay "MỘT NÚT — MỌI MÀN HÌNH" | "Sáu giờ sáng mai… đi nữa" | 20 |
| 9 | [PHONE] | Khách ăn xong đóng app, màn hình đen; overlay "RỒI SAO? KHÔNG CÓ GÌ NÍU" | "Quán giờ chạy trơn… không có lý do mở lại" | 15 |
| 10 | [B-ROLL] | Voucher giấy + bút viết blog; overlay "TẬP 7: VOUCHER + BLOG" | Teaser + CTA | 15 |

**Tổng: 290 giây ≈ 4,8 phút hình** + thoại dày → runtime ~6,5–7 phút.

**Batch-record:** scene 3+5 một phiên IDE; scene 6+7 cần 2 thiết bị như EP04 (quay nhiều takes cho race); scene 1 quay tại quán buổi sáng.

---

## Prompt cho Opus

### Prompt 1 — Hết món realtime + optimistic + race (scene 3)

```
Bối cảnh: Mini App "Chan Thêm". Đã có: dishes.available (EP02), tab admin +
admin-api Edge Function (EP04), menu realtime, giỏ hàng pre-order (EP05).

Nhiệm vụ: lên plan tính năng "hết món":
1) Tab admin: công tắc bật/tắt available cho từng món (qua admin-api).
2) Menu khách: realtime — món available=false thì mờ, badge "Hết món",
   không thêm được vào giỏ. Chỉ đổi dòng món affected, không re-render cả list.
3) Xử lý va chạm: món đang nằm trong giỏ bị tắt giữa chừng → bỏ khỏi giỏ,
   hiện thông báo nhỏ; Edge Function nhận đơn thì rà lại từng món, loại món
   đã tắt trước khi ghi vào orders.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
Plan nêu rõ: optimistic UI cho công tắc admin (đổi ngay, lùi nếu fail),
và thứ tự xử lý race: quầy thắng, khách được báo, server là trọng tài.
```

Lưu verbatim tại `code/prompt-ep06.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a hand tapping a glowing toggle switch on a tablet at a small Vietnamese pho restaurant counter, and in the background a phone menu item visibly greyed out with a SOLD OUT badge, steam from pho bowls, dramatic blue tech glow against warm kitchen light, shallow depth of field, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic split-scene photograph: left side a steaming pho pot in a warm morning kitchen, right side a dark tech screen showing a menu list with one dimmed item, a lightning bolt of blue light connecting both worlds, high contrast, 8k, photorealistic, high-end commercial. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic close-up photograph of two phones on a dark wooden table, one showing a cart with one item crossed out and a small apology message, the other showing a toggle switch being turned off, neon blue lighting, deep shadows, moody atmosphere, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #6: Hết bánh phở — menu tự biết trong 2 giây | Lập trình là cuộc sống`
2. `Zalo Mini App #6: Quầy tắt một nút, cả quán thấy ngay | Lập trình là cuộc sống`
3. `Zalo Mini App #6: Món trong giỏ bị tắt giữa chừng thì sao? | Lập trình là cuộc sống`
4. `Zalo Mini App #6: Optimistic UI: bấm trước, tin sau | Lập trình là cuộc sống`
5. `Zalo Mini App #6: Race condition ở quán phở, không phải trong sách | Lập trình là cuộc sống`

### 4b. SEO Description

```
6h sáng hết bánh phở, 11h khách vẫn đặt — quán mất khách ngay tại bàn. Tập 6: một công tắc ở quầy, menu trên mọi điện thoại tự "biết điều" trong 2 giây — kèm bài race condition rất đời: món trong giỏ bị tắt giữa chừng thì sao?

✅ Nối cờ available vào hai đầu: công tắc admin + menu realtime
✅ Optimistic UI: bấm trước tin sau, lùi lại nếu fail
✅ Race condition đời thường: quầy tắt món đúng lúc khách gửi giỏ
✅ Luật xử lý: quầy thắng, khách được báo, server là trọng tài
✅ Edge Function rà từng món trước khi ghi đơn
✅ Test thật trên 2 thiết bị: toggle → mờ ≤2 giây, giỏ tự bỏ món

Timestamps:
00:00 6h sáng hết bánh phở
00:45 Hai đầu của một công tắc
01:15 AI lên plan + optimistic UI
02:00 Race condition ở quán phở
02:40 Quầy thắng, server trọng tài
03:10 Màn diễn 2 thiết bị
03:40 Màn race: giỏ va vào công tắc
04:20 Một nút, mọi màn hình
04:40 Không có gì níu khách (teaser voucher + blog)

#ZaloMiniApp #Supabase #Realtime #vibecoding #laptrinh #optimisticUI #racecondition #LapTrinhLaCuocSong #React #aiagent #hetmon
```

### 4c. Keywords

```
zalo mini app, het mon realtime, optimistic UI la gi, race condition vi du that, sold out badge, toggle switch admin, supabase realtime update, menu realtime, xu ly gio hang, web app quan an, vibe coding, ai code assistant, lap trinh la cuoc song, quan pho cong nghe, app nha hang viet
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#06` góc trên phải.

### Option 1 — "HẾT MÓN / 2 GIÂY BIẾT"
- Image: Prompt 1. Text: `HẾT MÓN` (trắng) / `2 GIÂY BIẾT` (blue) + badge `REALTIME` nhỏ.

### Option 2 — "QUẦY TẮT / KHÁCH THẤY"
- Image: Prompt 2. Text: `QUẦY TẮT` (trắng) / `KHÁCH THẤY` (blue) + badge `#06`.

### Option 3 — "GIỎ VA / CÔNG TẮC"
- Image: Prompt 3. Text: `GIỎ VA` (trắng) / `CÔNG TẮC` (blue) + badge `RACE!` viền đỏ.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
