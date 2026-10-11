# EP08 — Share & growth loop: Mini App lan trong Zalo | Zalo Mini App #8

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7 phút
- **Word count PART 1:** 616 từ (~6.5 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** verify `openShareSheet` API hiện hành (params đổi giữa các bản SDK); test share thật vào nhóm Zalo trước khi quay.

## PART 1 — SCRIPT

App đã đủ thứ: đặt bàn, gọi món, voucher, blog. Và có đúng chừng ấy người dùng: ba người nhà mình. Sản phẩm tốt mà không ai biết, bằng không có sản phẩm.

Mùa ba mở màn bằng việc mở cửa: cho app lan trong Zalo. Và Zalo cho việc này một thứ mà App Store không có: tin nhắn. Người Việt không gửi link App Store cho nhau. Người Việt gửi tin. Bấm là mở. Không cài. Không chờ. Đó là lợi thế cấu trúc của Mini App, và hôm nay mình gắn nó vào app.

Công cụ chỉ một dòng gọi API: openShareSheet. Khách bấm, Zalo hiện danh sách bạn bè và nhóm, chọn, gửi. Vấn đề không nằm ở code. Vấn đề nằm ở chỗ nào của app xứng đáng được chia sẻ. Câu hỏi mà dân làm sản phẩm gọi là placement, mình gọi bằng tiếng quán: treo biển ở đâu cho người ta nhớ.

Mình đem câu hỏi đó đi hỏi Opus, kiểu hỏi một mentor chứ không phải đặt hàng code. Ba vị trí nó đề xuất. Một: nút share chung trên trang chủ. Chuẩn, và vô dụng. Không ai chia sẻ trang chủ của quán ăn. Hai: chia sẻ món — bấm món nào chia món đó. Hợp lý hơn, nếu món có mặt nhìn ngon. Ba: chia sẻ ngay trên màn hình voucher. Cái này mới đúng người dùng Việt: tặng ng.other cái mình vừa được tặng. Mình vừa nhận voucher tô phở một nghìn, tính năng cho mình chuyển tay nó cho bạn bè trông như một món quà, không phải một quảng cáo. Mình chọn vị trí ba. Quyết định thiết kế quan trọng hơn code.

Một vòng nhỏ trong tab admin để chủ quán tự làm vòng này: mỗi voucher có nút bật chia sẻ. Và mã QR in ra dán ở quầy: khách quét vào app, nhận voucher mở màn, app nằm luôn trong recently của Zalo. Vòng lặp trọn: tới quán, quét, nhận, dùng, chia.

Nói về tiền thì phải học người đi trước. Highlands Coffee chạy chiến dịch voucher trên Mini App: hơn hai triệu người dùng trong bốn mươi ngày, tỉ lệ chuyển đổi năm mươi sáu phần trăm, ba trăm bốn mươi bảy nghìn lượt quan tâm trang OA. Con số đó không phải vì app đẹp. Mà vì đúng công thức: quét mã tại bàn, chơi nhỏ, nhận voucher, voucher nằm trong app đợi quay lại. Công thức ấy không phải của hãng lớn. Nó scale xuống được cho quán ba bàn. Link case study mình để dưới mô tả.

Code phần này ngắn. Prompt cho Opus: share sheet ở màn voucher, kèmParams tiêu đề và đường dẫn mini app. Nó lên plan, mình duyệt, nó code. Có một chi tiết mình tự gõ: câu chữ trên nút share. Không dùng "Chia sẻ ứng dụng". Dùng: Chan thêm một tô cho bạn. Tên quán biến thành lời mời. Bốn chữ, không ai dạy, chỉ quán Việt mới đùa được.

Kiểm chứng ngay trong tập: mình share voucher vào một nhóm bạn. Trên điện thoại khác, bạn mở tin nhắn, bấm, app Chan Thêm mở ra thẳng màn voucher. Không App Store. Không tải. Ba giây từ tin nhắn tới voucher.

Nhưng chuyện kể xong thì mọi thứ trên app đã trong tay khách. Còn một cổng cuối chưa qua, và cổng này không code mà chờ: Zalo duyệt. Trước khi gửi duyệt, app phải trông như sản phẩm thật: hết placeholder, ảnh thật, nhẹ, không nút chết. Tập sau: đứng vào giày người kiểm duyệt và tổng dọn app. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen (time-lapse 3–5s); giữ nguyên: prompt tư vấn placement, cảnh share 2 điện thoại thật. Mở đầu 3–5s recap EP07 (blog đọc trong app).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | Zalo: danh sách bạn bè, một nhóm chat bất kỳ; overlay "3 NGƯỜI DÙNG — ĐỀU HỌ RICHARD" | Cold open | 20 |
| 2 | [DIAGRAM] | Mini App vs App Store: đường "gửi link → cài → chờ → mở" gạch bỏ; đường "gửi tin → bấm → mở" sáng xanh | "Mùa ba mở màn… lợi thế cấu trúc" | 30 |
| 3 | [IDE] | DÁN Prompt 1 (hỏi mentor về placement share) → Opus liệt kê 3 vị trí kèm lập luận; host scroll từng vị trí, khoanh chọn vị trí 3 (màn voucher) | "Công cụ chỉ một dòng… quan trọng hơn code" | 55 |
| 4 | [DIAGRAM] | Vòng lặp: tới quán → quét QR → nhận voucher → dùng → share → người mới; vẽ tròn, mũi tên khép | "Một vòng nhỏ… dùng, chia" | 30 |
| 5 | [BROWSER] | Case study Highlands (miniforbusiness.zalo.me): zoom số liệu 2 triệu user / 56,9% / 347K OA; caption nguồn | "Nói về tiền… scale xuống được" | 35 |
| 6 | [IDE] | Prompt 2 (code share) → plan ngắn → approved → time-lapse code; rồi host TỰ GÕ text nút share "Chan thêm một tô cho bạn" | "Code phần này ngắn… quán Việt mới đùa được" | 35 |
| 7 | [PHONE]+[PHONE] | **Cảnh chủ lực — 2 điện thoại:** máy A share voucher vào nhóm thật → máy B nhận tin → bấm → app mở thẳng màn voucher (đếm NHANH 1-2-3 giây trên màn hình) | "Kiểm chứng ngay… tới voucher" | 35 |
| 8 | [DIAGRAM] | Cổng duyệt Zalo vẽ như cửa kim loại + hàng chờ; checklist mờ phía sau | "Nhưng chuyện kể xong… chờ: Zalo duyệt" | 20 |
| 9 | [B-ROLL] | Bàn phím + điện thoại; overlay "TẬP 9: NHÌN QUA MẮT NGƯỜI DUYỆT" | Teaser + CTA | 15 |

**Tổng: 275 giây ≈ 4,6 phút hình** + thoại dày → runtime ~6,5–7 phút.

**Batch-record:** scene 3+6 một phiên IDE; scene 7 cần 2 phone + bạn bè thật trong nhóm (xin phép hoặc dùng nhóm của đội làm phim); scene 5 mở sẵn tab trước.

---

## Prompt cho Opus

### Prompt 1 — Hỏi mentor về placement (scene 3)

```
Mình không cần code ngay. Câu hỏi sản phẩm: Mini App quán phở "Chan Thêm"
đã có menu, đặt bàn, pre-order, voucher (kèm màn "Đã lưu"), blog. Giờ muốn
gắn nút chia sẻ qua openShareSheet.

Hỏi: nên đặt nút share ở đâu cho người dùng Việt thật sự bấm? Đề xuất
3 vị trí, mỗi vị trí kèm: ai bấm, lúc nào, vì sao họ bấm (hoặc không bấm).
Không code — chỉ tư vấn. Cuối cùng đoán vị trí nào conversion cao nhất
và giải thích.
```

### Prompt 2 — Code share sheet (scene 6)

```
Bối cảnh: đã chốt share ở màn hình voucher đã lưu.

Nhiệm vụ: lên plan thêm nút share gọi openShareSheet với tiêu đề
"Chan Thêm — tặng bạn voucher quán phở" và đường dẫn mini app (type zalo
mini app, path tới màn voucher). Kèm nút bật/tắt chia sẻ cho từng voucher
trong tab admin (qua admin-api).

QUY TẮC: trình PLAN trước, chờ approve, chưa sửa file.
```

Lưu verbatim tại `code/prompt-ep08.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of two phones facing each other on a dark wooden restaurant table, one showing a blue voucher being sent in a chat, the other receiving it with a glow, steam from pho bowls between them, neon blue light beams connecting the screens, shallow depth of field, 8k, photorealistic, high-end commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of a hand pressing a glowing blue share button on a phone screen with sharing ripples spreading outward like water waves made of light, dark moody room with city bokeh through window, a pho bowl in warm light at the edge of frame, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of a small pho restaurant counter at night with a glowing blue QR code stand on it, a customer's phone scanning it, warm kitchen light behind, rain on the window, intimate documentary mood, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #8: Chia sẻ trong 3 giây, không cần App Store | Lập trình là cuộc sống`
2. `Zalo Mini App #8: Treo biển share ở đâu cho người ta bấm? | Lập trình là cuộc sống`
3. `Zalo Mini App #8: Highlands 2 triệu user — công thức quán 3 bàn cũng dùng được | Lập trình là cuộc sống`
4. `Zalo Mini App #8: Voucher biến thành quà tặng, không phải quảng cáo | Lập trình là cuộc sống`
5. `Zalo Mini App #8: "Chan thêm một tô cho bạn" — nút share của quán Việt | Lập trình là cuộc sống`

### 4b. SEO Description

```
App đủ tính năng… và 3 người dùng, đều họ Richard. Tập 8 mở mùa 3: gắn vòng lan truyền trong Zalo — share 3 giây mở app, voucher thành quà tặng, và công thức Highlands 2 triệu user scale xuống cho quán 3 bàn.

✅ openShareSheet: một dòng API, cả vấn đề nằm ở placement
✅ Hỏi AI như hỏi mentor: 3 vị trí share, chọn màn voucher (tặng quà ≠ quảng cáo)
✅ Vòng lặp: tới quán → quét QR → nhận voucher → dùng → share
✅ Case study Highlands: 2 triệu user, 56,9% chuyển đổi, 347K follow OA (link dưới)
✅ Nút share tự viết: "Chan thêm một tô cho bạn"
✅ Test thật 2 máy: tin nhắn → bấm → voucher trong 3 giây

Links:
- Case study Highlands Mini App: https://miniforbusiness.zalo.me/case-study/highlands-coffee-tang-ti-le-chuyen-doi-voi-chien-dich-phat-voucher-tren-zalo-mini-app
- Zalo Mini App docs: https://mini.zalo.me/docs

Timestamps:
00:00 Ba người dùng, đều họ Richard
00:20 Lợi thế cấu trúc: tin nhắn, không cài
00:50 Hỏi AI: treo biển ở đâu?
01:45 Vòng lặp quán nhỏ
02:15 Bài học 2 triệu user
03:20 Code ngắn, câu chữ khó
03:55 Ba giây từ tin nhắn tới voucher
04:40 Cổng cuối: người duyệt (teaser)

#ZaloMiniApp #vibecoding #laptrinh #growth #sharesheet #LapTrinhLaCuocSong #voucher #caseStudy #React #aiagent #quangba #marketingquan
```

### 4c. Keywords

```
zalo mini app, sharesheet, chia se zalo, growth loop, viral mini app, opensharesheet api, placement nut share, highlands mini app, case study zalo, voucher viral, qr code quan an, marketing nha hang, vibe coding, lap trinh la cuoc song, tang voucher, app khong can cai
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#08` góc trên phải.

### Option 1 — "3 GIÂY / TỪ TIN NHẮN TỚI APP"
- Image: Prompt 1. Text: `3 GIÂY` (trắng, to) / `TỚI APP` (blue) + badge `KHÔNG CÀI` nhỏ.

### Option 2 — "VOUCHER / LÀ QUÀ, KHÔNG PHẢI QC"
- Image: Prompt 2. Text: `VOUCHER LÀ QUÀ` (trắng) / `KHÔNG PHẢI QC` (blue) + badge `#08`.

### Option 3 — "QUÉT / LÀ VÀO"
- Image: Prompt 3. Text: `QUÉT` (trắng) / `LÀ VÀO` (blue) + badge `QR` nhỏ.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
