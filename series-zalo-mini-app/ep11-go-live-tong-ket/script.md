# EP11 — Go live, vận hành & tổng kết: quán có app riêng, 0 đồng platform | Zalo Mini App #11

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~9–10 phút (finale — recap + phỏng vấn + go-live thật)
- **Word count PART 1:** 630 từ (~6.6 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** cảnh "Đã duyệt" phải là capture THẬT (notification/email) theo plan mùa riêng; ngày Publish và ngày quay cần cách nhau để có footage khách thật.

## PART 1 — SCRIPT

Tin nhắn tới lúc chín giờ tối. Không hồi hộp như cứ tưởng— hồi hộp lắm. Mở dashboard. Trạng thái: Đã duyệt. Mười tập, một chuỗi tin nhắn với AI, bao nhiêu cốc cà phê. Quán phở nhà mình vừa được Zalo gật đầu.

Hôm nay nốt hai việc: bấm nút Publish cuối cùng, và ngồi lại tổng kết cả hành trình.

Nút trước, vì nó ngắn. Dashboard, quản lý phiên bản, phiên bản đã duyệt, Publish. Bấm. Không có countdown, không âm thanh. Chỉ là trạng thái đổi từ màu xám sang xanh: ứng dụng đang hoạt động. Nhưng chính nút đó vừa thay đổi một thứ lớn: từ giờ, bất kỳ ai ở Việt Nam mở Zalo, tìm chữ Chan Thêm, đều thấy app của mẹ mình. Giữa bảy mươi lăm triệu người dùng, quán ba cái bàn có một ô cửa.

Cảnh quay này không dàn dựng được: ngày hôm sau, khách quen đầu tiên quét mã QR dán ở quầy. Cô khách quen chỗ mẹ, cầm điện thoại lên quét, app mở, cô nhìn tên mình hiện trên đầu app rồi cười. Không có khoảnh khắc nào trong chín tập trước đắt bằng khoảnh khắc đó.

Rồi vận hành thật. Mấy thứ này không code thêm mà quyết định app sống hay chết. Tablet ở quầy, mở tab admin, cả ngày sáng màn hình: đó là màn hình bếp. Mẹ học đúng hai thao tác: bấm xác nhận khi có đơn, gạt công tắc khi hết món. Hướng dẫn ba dòng, dán cạnh tablet. QR in ra hai loại: mã to dán tường cho khách quét vào app, mã nhỏ trên từng bàn cho voucher mở màn. Chi phí vận hành: không đồng nền tảng, không đồng hosting trong giai đoạn free tier của Supabase. Chỉ tốn thời gian của một thằng con.

Giờ ngồi lại. Nhìn lại toàn bộ kiến trúc mình và AI đã dựng trong mười tập. Vẽ ra một màn hình duy nhất: điện thoại khách bên trái, Supabase ở giữa với các bảng và Edge Function, tablet quán bên phải, Zalo bao quanh tất cả. Mười tập gom lại thành một hình. Bạn pause chụp lại, nó đáng hơn một khóa học.Structure này nằm ngang qua những câu hỏi phỏng vấn thật: webview khác native chỗ nào, vì sao RLS, vì sao đơn lưu snapshot giá, vì sao key không xuống client. Ai đi phỏng vấn mà đã từng build một lần, trả lời những câu đó bằng kinh nghiệm chứ không phải bằng thuộc lòng.

Và thử thách cuối của series: mình mời Opus đóng vai interviewer khó tính. Câu hỏi của nó: nếu mai này quán nổi, một nghìn đơn một ngày, hệ thống này vỡ ở đâu? Mình trả lời bằng những điểm yếu mình biết sẵn: zaloId chưa xác thực chặt, cạnh tranh ghi đơn, Realtime một kênh nghe hết mọi bảng, PIN đơn giản. Điểm yếu nói ra được là điểm yếu đã bắt đầu được sửa. Không trả lời được mới đáng sợ.

Vậy là xong một mùa. Tổng chi phí nền tảng: không đồng. Tổng thư viện tự viết: gần như zero, AI viết phần lớn, mình đọc lại từng dòng. Điều quý nhất mua được không phải app. Là mẹ biết con làm gì cho một buổi, và con biết mẹ bán vất vả thế nào bao nhiêu năm.

Mùa sau còn nguyên đồ chơi: thanh toán trong app qua Checkout SDK, gọi món tại bàn bằng QR cho từng bàn, ZNS gửi tin xác nhận tự động. Quán lớn dần thì tech lớn theo. Còn bây giờ: quán mở cửa, nồi nước dùng đã ninh từ bốn giờ sáng. Mời bạn một tô, Chan Thêm nhé. Hẹn gặp lại ở mùa sau.

---

## PART 2 — SHOT LIST

Quy tắc series: cảnh duyệt/publish/khách là FOOTAGE THẬT không dàn dựng; recap + phỏng vấn AI là màn hình dựng. Mở đầu 3–5s recap EP10 (trạng thái Chờ xét duyệt).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | **Capture thật:** notification/email "Đã duyệt" tới (quay màn hình đúng lúc); host mở dashboard → trạng thái xanh | Cold open (4 câu) | 30 |
| 2 | [BROWSER] | **Publish thật:** Quản lý phiên bản → nút Publish → bấm → trạng thái "Đang hoạt động"; giữ im 3 giây | "Nút trước… một ô cửa" | 30 |
| 3 | [B-ROLL] | **Footage thật ngày sau:** khách quen quét QR tại quầy; app mở; (xin phép/camera ẩn) khoảnh khắc cười khi thấy tên mình; tô phở đặt lên bàn | "Cảnh quay này không dàn dựng… đắt bằng khoảnh khắc đó" | 45 |
| 4 | [B-ROLL]+[TABLET] | Vận hành: tablet quầy chạy tab admin (đơn sáng); giấy hướng dẫn 3 dòng dán cạnh; QR to trên tường + QR nhỏ trên bàn | "Rồi vận hành thật… một thằng con" | 40 |
| 5 | [DIAGRAM] | **Recap 1 màn hình:** phone khách ← → Supabase (bảng + Edge Function + Realtime) ← → tablet admin, Zalo bao ngoài; 10 mốc series nhỏ ở rìa | "Giờ ngồi lại… bằng thuộc lòng" | 50 |
| 6 | [IDE] | **Phỏng vấn AI:** Opus đóng interviewer; câu hỏi hiện lên "1000 đơn/ngày — vỡ ở đâu?"; host trả lời, mỗi điểm yếu hiện 1 dòng trên màn (zaloId / race / 1 kênh Realtime / PIN) | "Và thử thách cuối… mới đáng sợ" | 60 |
| 7 | [DIAGRAM] | Bảng tổng kết: chi phí 0đ platform, 11 tập, 2 thiết bị, kiến trúc 1 màn hình; 5 câu phỏng vấn mapping | "Vậy là xong một mùa… bao nhiêu năm" | 35 |
| 8 | [DIAGRAM] | Roadmap v2: Checkout SDK / QR từng bàn / ZNS; icon mờ "mùa sau" | "Mùa sau còn nguyên đồ chơi… tech lớn theo" | 25 |
| 9 | [B-ROLL] | Quán sáng sớm thật: nồi nước dùng, khói, mẹ bưng tô; overlay "CHAN THÊM — ĐANG HOẠT ĐỘNG TRÊN ZALO" | Kết + CTA | 25 |

**Tổng: 340 giây ≈ 5,7 phút hình** + thoại dày nhất series (~850 từ) → runtime ~9–10 phút (finale được phép).

**Batch-record:** scene 1+2 CẦN THIẾT BỊ SẴN SÀNG khi tin duyệt tới (đây là lý do bấm gửi thật ở cuối EP10); scene 3 quay ngày hôm sau tại quán; scene 5+6+7 dựng sau khi có footage.

---

## Prompt cho Opus

### Prompt 1 — Đóng vai interviewer (scene 6)

```
Bối cảnh: series 11 tập vừa build xong Mini App "Chan Thêm" cho quán phở 3 bàn:
Supabase (RLS, Realtime, Edge Function admin-api với ADMIN_PIN), zaloId làm
định danh client-side chưa xác thực server, pre-order lưu snapshot giá jsonb.

Nhiệm vụ: đóng vai technical interviewer khó tính, phỏng vấn mình về chính
hệ thống này. Hỏi 5 câu, đi từ sản phẩm xuống kỹ thuật, câu cuối phải là:
"Nếu quán nổi, 1000 đơn/ngày, hệ thống này vỡ ở đâu trước?" — hỏi xoáy
từng lớp: client, network, database, security. Một câu một lượt, chờ mình
trả lời xong mới hỏi tiếp. Không gợi ý đáp án.
```

Lưu verbatim tại `code/prompt-ep11.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of an elderly Vietnamese woman in her small pho restaurant at dawn, smiling while holding a smartphone showing a food app with her shop name, warm morning light through steam from the stock pot, blue tech glow from the phone contrasting warm amber kitchen, emotional documentary mood, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of a hand pressing a large glowing green PUBLISH button on a dark screen, confetti of light particles frozen mid-air, dramatic blue and green lighting, deep navy background, high contrast, 8k, photorealistic, high-end commercial. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic wide photograph of a small Vietnamese pho restaurant at night seen from outside, warm light inside, a glowing blue QR code sticker on the glass door, rain reflections on the street, intimate documentary mood, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #11: ĐÃ DUYỆT — quán mẹ mình có app trên Zalo | Lập trình là cuộc sống`
2. `Zalo Mini App #11: Khách đầu tiên quét mã, mẹ cười | Lập trình là cuộc sống`
3. `Zalo Mini App #11: 11 tập, 0 đồng, một app thật đang chạy | Lập trình là cuộc sống`
4. `Zalo Mini App #11: AI phỏng vấn ngược: 1000 đơn/ngày vỡ ở đâu? | Lập trình là cuộc sống`
5. `Zalo Mini App #11: Tổng kết mùa — mời bạn một tô, Chan Thêm nhé | Lập trình là cuộc sống`

### 4b. SEO Description

```
9 giờ tối, tin nhắn tới: Đã duyệt. Tập cuối mùa 1: bấm Publish thật, ngày đầu khách lạ quét mã đặt bàn thật, tổng kết kiến trúc 11 tập — và AI đóng vai interviewer hỏi câu khó nhất: 1000 đơn/ngày thì vỡ ở đâu?

✅ Publish thật: từ trạng thái xám sang xanh — 75 triệu người dùng thấy được
✅ Khách đầu tiên quét QR tại quầy (footage thật, không dàn dựng)
✅ Vận hành: tablet làm màn hình bếp, mẹ học 2 thao tác, chi phí 0đ
✅ Recap kiến trúc 1 màn hình: client → Supabase → admin, Zalo bao quanh
✅ 5 câu phỏng vấn thật: webview vs native, RLS, snapshot giá, key, realtime
✅ AI phỏng vấn ngược: host tự chỉ 4 điểm yếu của chính hệ thống

Timestamps:
00:00 Tin nhắn 9 giờ tối
00:30 Bấm Publish
01:00 Khách đầu tiên quét mã
01:45 Vận hành: tablet + QR + 3 dòng hướng dẫn
02:25 Recap 11 tập trong 1 màn hình
03:15 5 câu phỏng vấn mapping
04:05 AI phỏng vấn: 1000 đơn/ngày
05:05 Điều quý nhất mua được
05:40 Mùa sau: thanh toán, QR bàn, ZNS
06:00 Mời bạn một tô

#ZaloMiniApp #vibecoding #laptrinh #indiedev #LapTrinhLaCuocSong #goLive #Supabase #React #aiagent #quanAn #me #tongKet
```

### 4c. Keywords

```
zalo mini app, go live app, publish mini app, van hanh quan an, tablet man hinh bep, qr code ban, tong ket series, ai interviewer, phong van ky su, 1000 don ngay, kien truc he thong, recap 11 tap, chi phi 0 dong, vibe coding, lap trinh la cuoc song, app that cho me
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#11 • FINALE` góc trên phải.

### Option 1 — "QUÁN MẸ / LÊN ZALO"
- Image: Prompt 1. Text: `QUÁN MẸ MÌNH` (trắng) / `LÊN ZALO` (blue) + badge `ĐÃ DUYỆT` xanh lá.

### Option 2 — "PUBLISH / 75 TRIỆU NGƯỜI THẤY"
- Image: Prompt 2. Text: `PUBLISH` (trắng) / `75 TRIỆU THẤY` (blue) + badge `#11`.

### Option 3 — "11 TẬP / 0 ĐỒNG"
- Image: Prompt 3. Text: `11 TẬP` (trắng) / `0 ĐỒNG` (blue) + badge `APP THẬT`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
