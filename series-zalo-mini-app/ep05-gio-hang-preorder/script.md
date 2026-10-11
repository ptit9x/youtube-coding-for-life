# EP05 — Giỏ hàng & pre-order: giá bị đóng băng lúc đặt | Zalo Mini App #5

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7 phút
- **Word count PART 1:** 573 từ (~6.0 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** đọc lại cart components của template zaui-shop trong repo thật (tên prop có thể khác docs) trước khi viết cảnh quay.

## PART 1 — SCRIPT

Quán giờ nhận bàn qua app. Nhưng khách ngồi xuống rồi thì sao? Muốn tô đặc biệt, thêm gân, ít hành. Vẫn phải gọi miệng, chị ơi một tiếng, chờ mẹ rảnh tay.

Mùa hai mở màn bằng việc nối menu với bàn: giỏ hàng và gọi món trước. Khách đặt bàn xong, lướt menu, thêm tô vào giỏ, gửi. Quán nhận kèm đơn, biết trước nấu gì.

Template e-commerce mình lấy từ tập một có sẵn giỏ hàng. Đáng lẽ code nhanh. Nhưng trước khi đụng code, có một câu hỏi thiết kế phải trả lời trước, và nó là câu hỏi khó nhất series này: quán đổi giá ngày mai, thì đơn hôm qua tính theo giá nào?

Câu hỏi nghe ngớ ngẩn. Cho đến khi bạn mở bảng orders và phải quyết định lưu gì. Cách tự nhiên nhất: lưu danh sách id món. Nhẹ, sạch, chuẩn thiết kế database. Nhưng rồi khoét ngay lỗ hổng: đơn liện hệ dish id, giá nằm ở bảng dishes. Sáng mai mẹ nâng giá tô đặc biệt từ bốn mươi lên bốn lăm. Mở lại đơn hôm qua: bốn lăm. Đơn cũ tự sửa giá. Khách cãi, quán lỗ, không ai sai cả. Database đúng, hóa đơn sai.

Giải pháp: ngược đời nhưng đúng. Lưu kèm cái giá tại thời điểm đặt, chép thẳng vào đơn, dưới dạng jsonb. Nghe như lỗi thiết kế, phải không? Lưu trùng dữ liệu là tội trong môn database. Nhưng ở đây trùng có chủ đích: đơn không phải con trỏ tới menu. Đơn là hóa đơn. Hóa đơn là bản chụp của thực tế lúc chốt. Tên món, giá, số lượng, nằm im trong đơn mãi mãi. Menu đổi là chuyện của hôm nay, không được quay sửa lịch sử.

Vậy nên hôm nay mình phải thắng AI một keo về mặt lý thuyết. Mình gửi spec cho Opus: bảng orders, liên kết booking, items. Nó lên plan chuẩn chỉnh: items là mảng dish id. Chuẩn đó, nhưng sai cho quán mình. Mình gõ lại: trường hợp quán đổi giá mai, đơn hôm qua hiện bao nhiêu? Nó phân tích rồi tự sửa: thêm snapshot giá vào jsonb. Lần này plan đúng. Duyệt.

Code phần lớn AI làm, đúng quy trình. Mình chỉ vào đọc diff, và tự gõ lại hàm tính tổng: cộng giá trong snapshot nhân số lượng, không bao giờ cộng từ bảng dishes. Mười dòng, nhưng là mười dòng bảo vệ hóa đơn.

Chạy thật. Khách đặt bàn, thêm tô đặc biệt và hai ly nước, gửi. Trên tablet admin, booking kèm đơn món hiện ra đủ tên, số lượng, tổng tiền.

Rồi test vàng của tập này: mình vào Supabase, sửa giá tô đặc biệt lên gấp đôi, lưu. Mở lại đơn vừa rồi. Tổng tiền không nhúc nhích. Giá đã bị đóng băng từ lúc khách bấm gửi. Còn menu thì đã hiện giá mới. Cùng một món, hai con số, hai sự thật, mỗi sự thật đúng chỗ của nó.

Nhưng меню ngày mai lại có vấn đề khác. Sáu giờ sáng hết bánh phở, mẹ gắn tạm nhãn "hết". Khách vẫn đặt tô, đơn vẫn về, quán vẫn phải chạy ra chào lỗi. App phải biết món nào hết trước khi khách bấm. Tập sau: một công tắc ở quầy, menu trên tay khách đổi trong vài giây. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen (time-lapse 3–5s); giữ nguyên: prompt, host thắng AI về schema, host tự gõ hàm total, test vàng. Mở đầu 3–5s recap EP04 (tablet ting + nút xác nhận).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | App: booking confirmed; khách ngồi bàn, mở menu,… không có cách nào gọi món trước — scroll vô ích; overlay "VẪN GỌI MIỆNG" | Cold open | 20 |
| 2 | [DIAGRAM] | Câu hỏi trung tâm viết to: "ĐỔI GIÁ MAI → ĐƠN HÔM QUA TÍNH SAO?" dưới là 2 nhánh: dish_id sống vs snapshot jsonb | "Quán giờ nhận bàn… câu hỏi khó nhất series này" | 30 |
| 3 | [DIAGRAM] | Timeline minh họa lỗ hổng: hôm qua 40k (đơn) → hôm nay 50k (dishes) → đơn cũ hiện 50k ❌; caption "Database đúng, hóa đơn sai" | "Cách tự nhiên nhất… hóa đơn sai" | 35 |
| 4 | [DIAGRAM] | Hóa đơn giấy scan/bičú phở: mũi tên "bản chụp thực tế lúc chốt"; gắn nhãn denormalize CÓ CHỦ ĐÍCH | "Giải pháp… không được quay sửa lịch sử" | 30 |
| 5 | [IDE] | DÁN Prompt 1 (orders schema) → plan Opus: items = dish_id[]; host khoanh vùng, gõ câu chất vấn "đổi giá mai thì sao?" (Prompt 2) → AI tự sửa plan thêm snapshot → approved | "Vậy nên hôm nay… Duyệt" | 55 |
| 6 | [IDE] | Host TỰ GÕ hàm calculateTotal (đọc từ snapshot × qty, không đụng bảng dishes) — quay thật | "Mình chỉ vào đọc diff… bảo vệ hóa đơn" | 30 |
| 7 | [PHONE] | Khách: đặt bàn → thêm món vào cart (dùng cart template) → gửi; tablet [TABLET]: booking + đơn món hiện đủ tên/số lượng/tổng | "Chạy thật… tổng tiền" | 30 |
| 8 | [BROWSER] | **Test vàng — không cắt:** Supabase sửa giá tô đặc biệt gấp đôi → lưu → mở lại đơn: tổng KHÔNG đổi → mở menu: giá MỚI hiện; split màn kết đôi | "Rồi test vàng… mỗi sự thật đúng chỗ của nó" | 40 |
| 9 | [PHONE] | Menu sáng: món "Hết"… nhưng app vẫn cho đặt (đơn rớt) — overlay "6H SÁNG HẾT BÁNH PHỞ" | "Nhưng menu ngày mai… chào lỗi" | 20 |
| 10 | [B-ROLL] | Bếp quán thật, nồi nước dùng bốc khói; overlay "TẬP 6: HẾT MÓN" | Teaser + CTA | 15 |

**Tổng: 305 giây ≈ 5,1 phút hình** + thoại dày → runtime ~6,5–7 phút.

**Batch-record:** scene 5 một phiên IDE; scene 1+7 một phiên phone; scene 8 cần chuẩn bị sẵn giá cũ/mới (đổi xong ĐỔI LẠI ngay sau take để không hỏng data thật).

---

## Prompt cho Opus

### Prompt 1 — Orders schema (scene 5)

```
Bối cảnh: Mini App "Chan Thêm". Đã có: bookings (EP03), admin realtime +
Edge Function admin-api (EP04), menu realtime từ dishes. Giỏ hàng lấy từ
cart components của template.

Nhiệm vụ: lên plan bảng orders + flow pre-order: khách đặt bàn kèm món
(hoặc mang đi). Đơn gồm items (món + số lượng), liên kết booking_id nếu có,
tổng tiền, ghi chú, trạng thái (new/accepted/served/cancelled).

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
```

### Prompt 2 — Chất vấn snapshot giá (scene 5, gõ sau khi plan hiện)

```
Câu hỏi: quán đổi giá món ngày mai, thì đơn hôm qua hiện tổng bao nhiêu?
Nếu items chỉ lưu dish_id thì chuyện gì xảy ra với đơn cũ khi bảng dishes
đổi giá? Phân tích rồi tự sửa plan nếu cần — nhớ mục tiêu: đơn là hóa đơn,
không được đổi sau khi chốt.
```

Lưu verbatim tại `code/prompt-ep05.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a hand holding a phone showing a food cart with a glowing frozen price tag on one item, steam from a pho bowl behind, dramatic blue neon lighting with frost-like light accents on the frozen price, dark moody background, shallow depth of field, 8k, photorealistic, high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic close-up photograph of an old paper restaurant invoice on a dark wooden table next to a smartphone showing a digital order, a red arrow connecting the unchanged total numbers, warm amber lamp light contrasting cool blue screen glow, high contrast, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of a developer at a dark desk with two screens, one showing a database schema diagram with a JSON block highlighted in neon blue, the other a phone food app, steam rising from pho in the foreground, shallow depth of field, bokeh, 8k, photorealistic, developer documentary. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #5: Đổi giá mai, đơn hôm qua tính bao nhiêu? | Lập trình là cuộc sống`
2. `Zalo Mini App #5: Giá bị đóng băng đúng lúc khách bấm đặt | Lập trình là cuộc sống`
3. `Zalo Mini App #5: Denormalize là xấu — trừ khi nó là hóa đơn | Lập trình là cuộc sống`
4. `Zalo Mini App #5: Gọi món trước, quán biết trước nấu gì | Lập trình là cuộc sống`
5. `Zalo Mini App #5: Lưu dish_id hay lưu giá? Câu hỏi 50k | Lập trình là cuộc sống`

### 4b. SEO Description

```
Mùa 2 mở màn: giỏ hàng + gọi món trước cho quán phở. Và câu hỏi khó nhất series: quán đổi giá ngày mai thì đơn hôm qua tính theo giá nào? Đáp án: đóng băng giá lúc đặt — denormalize có chủ đích.

✅ Tái dùng cart components của template e-commerce
✅ Lỗ hổng lưu dish_id sống: đơn cũ tự đổi giá khi menu đổi
✅ Đơn là hóa đơn = bản chụp thực tế lúc chốt (jsonb snapshot)
✅ Host thắng AI một keo về thiết kế schema
✅ Tự gõ hàm total: cộng từ snapshot, không bao giờ từ bảng dishes
✅ Test vàng: sửa giá gấp đôi — đơn cũ không nhúc nhích

Timestamps:
00:00 Vẫn gọi miệng "chị ơi"
00:20 Câu hỏi 50 nghìn
01:15 Lỗ hổng dish_id sống
01:50 Hóa đơn là bản chụp
02:20 Host vs AI: một keo schema
03:15 Mười dòng bảo vệ hóa đơn
03:45 Chạy thật: booking kèm món
04:25 Test vàng: giá gấp đôi, đơn im
05:05 Sáng mai hết bánh phở (teaser)

#ZaloMiniApp #Supabase #vibecoding #laptrinh #database #denormalization #jsonb #LapTrinhLaCuocSong #giohang #React #aiagent
```

### 4c. Keywords

```
zalo mini app, gio hang react, preorder nha hang, snapshot gia, denormalization la gi, jsonb postgres, luu don hang, thiet ke schema don hang, dish id vs snapshot, vibe coding, ai thiet ke schema, chat van phan bien ai, test gia doi, don hang khong doi gia, lap trinh la cuoc song, app goi mon, quan an cong nghe
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#05` góc trên phải.

### Option 1 — "ĐỔI GIÁ MAI / ĐƠN HÔM QUA?"
- Image: Prompt 1. Text: `ĐỔI GIÁ MAI` (trắng) / `ĐƠN HÔM QUA?` (blue) + badge `#05`.

### Option 2 — "GIÁ ĐÓNG BĂNG / LÚC ĐẶT"
- Image: Prompt 2. Text: `GIÁ ĐÓNG BĂNG` (trắng) / `LÚC ĐẶT` (blue) + badge `❄` nhỏ.

### Option 3 — "AI CHUẨN / MÌNH VẪN SỬA"
- Image: Prompt 3. Text: `AI CHUẨN` (trắng) / `MÌNH VẪN SỬA` (blue) + badge `#05`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
