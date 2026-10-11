# Bonus B — Thanh toán trong Mini App: Checkout SDK | Zalo Mini App (Bonus)

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7 phút
- **Word count PART 1:** 546 từ (~5.7 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them` (nhánh v2/payment)
- **Cảnh gate:** quay TỐI THIỂU 1 cảnh thật giao sandbox (không cần giao thật); phần hộ kinh doanh nói bằng narration + diagram.
- **Pre-flight:** đối chiếu repo chính thức `Zalo-MiniApp/checkout-sdk-tutorial` + docs Checkout SDK hiện hành; xác nhận danh mục payment yêu cầu loại hình sở hữu nào trên dashboard.

## PART 1 — SCRIPT

Mùa một khép lại với một câu chưa trả: khách đặt, khách gọi, rồi khách… trả tiền tại quầy. Tiện cho quán, phiền cho app. Mùa thanh toán bắt đầu bằng đúng câu hỏi đó: sao không trả trong app luôn?

Câu trả lời ngắn: được. Zalo có Checkout SDK, khách bấm thanh toán, ví ZaloPay hoặc thẻ, xong tiền vào tài khoản quán. Câu trả lời dài hơn mới là nội dung hôm nay: được, sau khi đi qua ba cổng.

Cổng một: giấy tờ. Thanh toán là ngành nhạy cảm, Zalo chặt hơn hẳn các quyền thường. Cá nhân như mùa một thì đến đây dừng: tính năng thu tiền đòi hỏi chủ app là hộ kinh doanh hoặc doanh nghiệp, giấy phép đầy đủ. Mẹ mình chưa có hộ kinh doanh, nên mùa một đi đường cá nhân và chốt vững phần đặt món. Mùa thanh toán là mùa làm giấy. Kể ra cũng hợp đời: quán nhỏ muốn thu tiền mobil, đầu tiên là ra ủy ban phường đăng ký hộ kinh doanh, không phải mở IDE.

Cổng hai: kỹ thuật. Checkout SDK khác các API mình từng dùng ở một điểm: nó giao dịch với tiền, nên mọi bước đều có chữ ký và chữ kiểm. Khởi tạo đơn: tiền, món, mã đơn duy nhất. Gọi SDK mở màn thanh toán. Zalo xử lý với khách. Rồi callback về server mình: kết quả giao dịch, kèm chữ ký để chứng minh tin này thật sự từ Zalo, không phải kẻ xấu giả mạo. Nếu bỏ qua bước xác minh chữ ký, ai cũng có thể nhắn "đơn đã thanh toán" vào server quán và nhận phở không tiền. Kiểm chứng ở server, không bao giờ tin tin nhắn từ client.

Cổng ba: đối soát. Tiền trong ví, đơn trong database, hai bên phải khớp từng ngày. Giao dịch treo, khách bấm rồi đóng app giữa chừng, hoàn tiền một nửa — những ca đời này không nằm trong quick start, nằm trong phần "xử lý lỗi" mà không ai đọc cho tới khi cần.

Về demo, mình làm trên nhánh v2 của repo Chan Thêm: thêm nút thanh toán ở màn giỏ hàng, khới tạo đơn qua Edge Function giữ khóa, gọi Checkout SDK mở màn sandbox, nhận callback xác minh chữ ký, đơn chuyển trạng thái đã thanh toán. Sandbox cho phép chạy hết vòng mà không động tới tiền thật. Phần khai merchant và giấy tờ làm ngoài camera, vì lý do rõ.

Một quyết định thiết kế đáng nói trước khi kết: giá đổi, đơn đóng băng từ mùa một, giờ còn đúng hơn. Thanh toán xong thì đơn là hợp đồng đã ký. Snapshot giá từ tập năm chính là thứ protects quán khỏi chuyện khách giữ đơn cũ chờ giá xuống rồi thanh toán. Ngày càng thấy những quyết Judgment "nhàm" đầu series là móng của những tính năng sau.

Mùa thanh toán sẽ dài: merchant, sandbox, chữ ký, hoàn tiền, đối soát, rồi thằng nghiệt ngã nhất: quản lý đơn song song giữa tiền và món. Nếu quán nhà bạn cũng đang chuẩn bị làm giấy, làm cùng lúc với mình. Hẹn gặp lại ở tập sau của mùa hai. Làm theo cùng mình thì lưu kênh.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen (time-lapse 3–5s); giao dịch sandbox là cảnh thật tối thiểu 1 lần; phần giấy tờ KHÔNG quay (narration + diagram). Mở đầu 3–5s recap EP11/12.

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | App v1: khách đặt xong → màn "thanh toán tại quầy"; overlay "SAO KHÔNG TRẢ TRONG APP?" | Cold open | 20 |
| 2 | [DIAGRAM] | 3 cổng vẽ như 3 cánh cửa: Giấy tờ / Kỹ thuật (chữ ký) / Đối soát | "Câu trả lời ngắn… ba cổng" | 30 |
| 3 | [DIAGRAM] | Cổng 1: Cá nhân ❌ / HKD-DN ✅ cho payment; sơ đồ ủy ban phường → hộ kinh doanh → dashboard | "Cổng một: giấy tờ… không phải mở IDE" | 35 |
| 4 | [DIAGRAM] | Cổng 2: flow đơn → SDK → ZaloPay → callback + chữ ký → server xác minh → status đổi; gạch đỏ đường "tin client không xác minh" | "Cổng hai: kỹ thuật… không phải kẻ xấu giả mạo" | 45 |
| 5 | [DIAGRAM] | Cổng 3: bảng đối soát ngày (tiền ví ‖ đơn DB, khớp/treo/hoàn); caption "phần không ai đọc" | "Cổng ba: đối soát… cho tới khi cần" | 30 |
| 6 | [IDE] | DÁN Prompt 1 (tích hợp sandbox) → plan Opus: Edge Function tạo đơn + verify chữ ký; host review zoom đoạn verify | "Về demo… giữ khóa" | 45 |
| 7 | [PHONE] | **Cảnh sandbox thật:** giỏ hàng → nút Thanh toán → màn ZaloPay sandbox → xác nhận → callback → đơn "Đã thanh toán" (chạy thật 1 lần, giữ nguyên) | "Gọi Checkout SDK… không động tới tiền thật" | 40 |
| 8 | [DIAGRAM] | Vòng pull-back: EP05 snapshot giá ←highlight→ hợp đồng đã ký; caption "móng đầu series" | "Một quyết định thiết kế… tính năng sau" | 30 |
| 9 | [B-ROLL] | Giấy tờ + bàn phím cạnh nhau; overlay "MÙA 2: THANH TOÁN — LÀM GIẤY CÙNG NHAU" | Teaser + CTA | 15 |

**Tổng: 290 giây ≈ 4,8 phút hình** + thoại → runtime ~6,5–7 phút.

**Batch-record:** scene 6 một phiên IDE; scene 7 cần tài khoản sandbox chuẩn bị trước (merchant test); scene 3+4+5 dựng diagram một phiên Excalidraw.

---

## Prompt cho Opus

### Prompt 1 — Tích hợp Checkout SDK sandbox (scene 6)

```
Bối cảnh: Mini App "Chan Thêm" v1 đã live (đặt bàn, pre-order với snapshot
giá jsonb, admin-api Edge Function). Làm v2 ở nhánh riêng: thanh toán qua
Zalo Checkout SDK, môi trường SANDBOX (merchant test).

Nhiệm vụ: lên plan tích hợp:
1) Nút thanh toán ở màn giỏ hàng.
2) Edge Function payment-create: tạo đơn với mã duy nhất, số tiền từ snapshot
   giá trong DB (không tin số tiền client gửi lên), khởi tạo giao dịch.
3) Callback payment-notify: xác minh chữ ký từ Zalo, chữ ký đúng mới đổi
   trạng thái đơn sang đã thanh toán.
4) Trường hợp khách đóng app giữa chừng: đơn treo, xử lý sau.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
Nêu rõ từng bước cái nào chạy client, cái nào chạy server, vì sao.
```

Lưu verbatim tại `code/prompt-bonus-b.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a phone showing a glowing blue payment confirmation screen with a checkmark, held above a steaming bowl of pho on a dark restaurant table, dramatic blue neon light on the payment UI contrasting warm food light, shallow depth of field, 8k, photorealistic, high-end fintech commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of three glowing doors in a dark futuristic corridor, the third door open revealing blue light and a payment terminal, a developer silhouette walking toward them, dramatic rim lighting, deep navy and blue tones, high contrast, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic close-up photograph of a digital signature seal glowing neon blue being verified on a dark screen, a red forged document beside it dissolving into particles, moody tech atmosphere, deep shadows, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App Bonus: Thanh toán trong app — 3 cổng phải qua | Lập trình là cuộc sống`
2. `Zalo Mini App Bonus: Checkout SDK chạy sandbox thật | Lập trình là cuộc sống`
3. `Zalo Mini App Bonus: Không xác minh chữ ký = cho không tô phở | Lập trình là cuộc sống`
4. `Zalo Mini App Bonus: Cá nhân không thu tiền được — đi làm hộ kinh doanh | Lập trình là cuộc sống`
5. `Zalo Mini App Bonus: Snapshot giá mùa 1 cứu thanh toán mùa 2 | Lập trình là cuộc sống`

### 4b. SEO Description

```
Khách đặt xong vẫn phải trả tiền tại quầy. Tập bonus mở mùa thanh toán: Checkout SDK — được, sau khi qua 3 cổng: giấy tờ (hộ kinh doanh), chữ ký callback, đối soát. Kèm demo sandbox chạy thật.

✅ Checkout SDK: khách trả bằng ZaloPay/thẻ ngay trong app
✅ Cổng 1: thanh toán đòi chủ app là HKD/DN — mùa này đi làm giấy
✅ Cổng 2: callback + xác minh chữ ký ở server — tin client là cho không hàng
✅ Cổng 3: đối soát tiền ví ‖ đơn DB, xử lý đơn treo/hoàn tiền
✅ Demo thật trên nhánh v2: sandbox, Edge Function giữ khóa, không tiền thật
✅ Caller back: snapshot giá EP05 chính là hợp đồng đã ký khi có thanh toán

Links:
- Checkout SDK tutorial: https://github.com/Zalo-MiniApp/checkout-sdk-tutorial
- Zalo Mini App docs: https://mini.zalo.me/docs

Timestamps:
00:00 Sao không trả trong app?
00:20 Ba cổng
00:50 Cổng 1: làm giấy trước, code sau
01:25 Cổng 2: chữ ký và kẻ giả mạo
02:10 Cổng 3: đối soát — phần không ai đọc
02:40 Demo sandbox thật
03:20 Snapshot giá mùa 1 cứu mùa 2
03:50 Mùa 2 phía trước

#ZaloMiniApp #CheckoutSDK #ZaloPay #vibecoding #laptrinh #payment #LapTrinhLaCuocSong #sandbox #hokinhdoanh #EdgeFunction
```

### 4c. Keywords

```
zalo mini app, checkout sdk, thanh toan trong app, zalopay tich hop, callback xac minh chu ky, webhook signature, doi soat giao dich, don treo, hoan tien, sandbox payment, ho kinh doanh thanh toan, merchant zalo, vibe coding, lap trinh la cuoc song, edge function payment
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `BONUS • THANH TOÁN` góc trên phải.

### Option 1 — "TRẢ TIỀN / TRONG APP"
- Image: Prompt 1. Text: `TRẢ TIỀN` (trắng) / `TRONG APP` (blue) + badge `CHECKOUT SDK`.

### Option 2 — "3 CỔNG / MỚI ĐẾN TIỀN"
- Image: Prompt 2. Text: `3 CỔNG` (trắng) / `MỚI ĐẾN TIỀN` (blue) + badge `BONUS`.

### Option 3 — "CHỮ KÝ SAI / KHÔNG CÓ PHỞ"
- Image: Prompt 3. Text: `CHỮ KÝ SAI` (trắng) / `KHÔNG CÓ PHỞ` (blue) + badge `VERIFY!` viền đỏ.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
