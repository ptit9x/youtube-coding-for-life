# EP09 — Polish & checklist duyệt: nhìn qua mắt người kiểm duyệt | Zalo Mini App #9

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7 phút
- **Word count PART 1:** 481 từ (~5.1 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** chạy `zmp build` thật trước khi quay, ghi lại con số dung lượng bundle; nén sẵn ảnh WebP.

## PART 1 — SCRIPT

Mọi tính năng đã xong. Giờ thì app đạt chuẩn chưa gửi duyệt được? Chưa. Vì người duyệt không phải mình, cũng không phải khách. Là một nhân viên Zalo, mở app của mình trong vòng năm phút, tìm một lý do để từ chối.

Tập hôm nay đổi vai. Mình mời Opus đóng chính vai đó: người kiểm duyệt. Nhiệm vụ của nó: duyệt app Chan Thêm như duyệt app của người lạ, thật nghiêm túc, liệt kê mọi lý do có thể từ chối. Cách dùng AI ít ai nói: không nhờ nó code, mà nhờ nó trở thành người khó tính thay mình.

Kết quả của một lượt duyệt giả: danh sách dài hơn mình tưởng. Nút menu dẫn tới trang template demo còn sót. Ảnh món chụp dọc, hiển thị méo. Hai permission khai báo mà một cái chưa từng gọi. Giấy tờ tùy thân của quán: thiếu trang chính sách quyền riêng tư. Và chữ lorem ipsum vẫn nằm trong một trang blog demo. Bốn tập polish không bằng một lượt bị bắt lỗi.

Chỗ nào sửa được là sửa thật: xóa trang sót, nén ảnh, gỡ permission thừa. Chỗ nào là văn bản thì viết thật: trang quyền riêng tư, một trang tĩnh, nói thẳng app lưu số điện thoại để làm gì — quán liên hệ xác nhận đặt bàn, không bán cho ai. Mỗi permission còn lại phải khớp đúng chỗ code gọi nó, vì người duyệt đối chiếu hai bên.

Rồi đến con số mình phải hạ: mười megabyte. Trần dung lượng của Mini App. Bundle mình đang mười hai, quá. Ba thủ phạm quen mặt: ảnh PNG mỗi tấm vài trăm kilobyte, một font nhúng nguyên bộ, và một thư viện markdown dùng cho blog. Ba obrada: ảnh qua WebP, còn một phần tư dung lượng. Font bỏ hẳn, dùng system font của Zalo, chuẩn mà nhẹ. Thư viện markdown thì giữ, nhưng import đúng component cần dùng, không kéo cả gói. Build lại: tám phẩy ba. Đậu. Màn hình lệnh build và con số đó là ánh sáng xanh của tập này.

Còn hai chi tiết sống còn dễ bỏ sót. Màn hình lỗi mạng: quán wifi yếu, khách vẫn phải thấy thông báo dễ hiểu, không phải trang trắng. Và nút back của điện thoại: Mini App chạy trong webview, back phải về trang trước trong app, không phải thoát khỏi app ngay. Hai chi tiết đó là kiểu khấc mà người duyệt sờ tới đầu tiên.

Danh sách chốt hết, tick hết. App sạch, nhẹ, và nhất quán. Giờ mới tới cổng cuối: deploy thật lên hệ thống Zalo, điền hồ sơ, bấm gửi, và bắt đầu những ngày chờ. Tập sau là tập đó, và nó là tập có ít code nhất nhưng nhiều cảm xúc nhất series. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen/build (time-lapse 3–5s); giữ nguyên: danh sách lỗi AI, cảnh sửa thật, con số build. Mở đầu 3–5s recap EP08 (share 2 máy).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [DIAGRAM] | Đồng hồ cát + cửa "REVIEW"; text "5 PHÚT — TÌM 1 LÝ DO TỪ CHỐI" | Cold open | 20 |
| 2 | [IDE] | DÁN Prompt 1 (AI đóng vai reviewer) → danh sách lỗi hiện ra từng nhóm; host scroll chậm, zoom "lorem ipsum" và "permission chưa dùng" | "Tập hôm nay đổi vai… một lượt bị bắt lỗi" | 55 |
| 3 | [IDE] | Sửa thật nhanh (cắt ghép 4–5 nhịp): xóa trang demo, thay ảnh dọc, gỡ permission, xóa lorem; tick checklist mỗi mục | "Chỗ nào sửa được… đối chiếu hai bên" | 45 |
| 4 | [BROWSER] | Trang privacy policy tĩnh viết thật: zoom dòng "lưu SĐT để liên hệ xác nhận đặt bàn, không chia sẻ" | "Chỗ nào là văn bản… không bán cho ai" | 25 |
| 5 | [TERM] | **Cảnh con số — không cắt:** `zmp build` chạy (time-lapse phần chờ) → dừng lại ở "12.1 MB"; overlay đỏ "VƯỢT 10MB" | "Rồi đến con số… quá" | 25 |
| 6 | [DIAGRAM] | 3 thủ phạm → 3 obrada: PNG→WebP (1/4), font nhúng→system font, markdown lib→import chọn lọc | "Ba thủ phạm quen mặt… cả gói" | 35 |
| 7 | [TERM] | Build lại → "8.3 MB" — giữ nguyên cảnh, zoom con số; overlay xanh ĐẠU | "Build lại: tám phẩy ba… ánh sáng xanh" | 20 |
| 8 | [PHONE] | Test 2 khấc: bật chế độ máy bay → màn lỗi mạng thân thiện; nút back đi về trang trước (không thoát app) | "Còn hai chi tiết sống còn… sờ tới đầu tiên" | 35 |
| 9 | [IDE] | Checklist tổng tick 100%; git log sạch theo từng mục; overlay "SẴN SÀNG NỘP" | "Danh sách chốt hết… nhiều cảm xúc nhất series" | 20 |
| 10 | [B-ROLL] | Bàn phím im, màn hình chờ; overlay "TẬP 10: GỬI DUYỆT — 3 NGÀY CHỜ" | Teaser + CTA | 15 |

**Tổng: 295 giây ≈ 4,9 phút hình** + thoại dày → runtime ~6,5–7 phút.

**Batch-record:** scene 2+3 một phiên IDE; scene 5+7 một phiên terminal (chạy build thật 2 lần, giữ số thật); scene 8 một phiên phone.

---

## Prompt cho Opus

### Prompt 1 — AI đóng vai reviewer Zalo (scene 2)

```
Bối cảnh: Mini App "Chan Thêm" hoàn thiện chức năng, chuẩn bị nộp duyệt
phát hành trên Zalo. Người duyệt sẽ mở app 5 phút và tìm lý do từ chối.

Nhiệm vụ: đóng vai nhân viên kiểm duyệt của Zalo, làm mặt lạnh, không nể nang.
Đọc toàn bộ cấu trúc app + quyền khai báo + nội dung hiện có; liệt kê TẤT CẢ
lý do có thể từ chối, chia nhóm: nội dung (placeholder, chữ chết, ảnh demo),
kỹ thuật (permission khai mà không dùng, màn lỗi, nút back), và hồ sơ
(chính sách quyền riêng tư, mô tả app). Xếp theo nguy cơ từ chối cao → thấp.
Không sửa gì — chỉ báo cáo kiểu biên bản duyệt.
```

Lưu verbatim tại `code/prompt-ep09.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a dark IDE screen with a long list of glowing red error items being checked off one by one turning green, a young Vietnamese developer reflected in the screen with a serious face, moody night lighting, neon red and blue accents, 8k, photorealistic, developer documentary. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of a giant glowing blue scale weighing a smartphone on one side against a "10 MB" weight block on the other, dark tech laboratory background with floating code particles, dramatic rim lighting, deep shadows, 8k, photorealistic, high-end commercial. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of a pho bowl and a phone on a dark desk, the phone screen showing a clean green checklist complete, warm steam catching blue monitor light, shallow depth of field, intimate documentary mood, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #9: Mượn AI làm nhân viên kiểm duyệt | Lập trình là cuộc sống`
2. `Zalo Mini App #9: Bundle 12MB → 8.3MB trong một buổi | Lập trình là cuộc sống`
3. `Zalo Mini App #9: Người duyệt tìm gì trong 5 phút của bạn | Lập trình là cuộc sống`
4. `Zalo Mini App #9: Lorem ipsum — ký ức tội đồ của app | Lập trình là cuộc sống`
5. `Zalo Mini App #9: Checklist 100% mới dám bấm gửi duyệt | Lập trình là cuộc sống`

### 4b. SEO Description

```
Trước khi Zalo duyệt, tự duyệt trước đã. Tập 9: mời AI đóng vai nhân viên kiểm duyệt mặt lạnh, bắt lỗi chính app của mình — rồi hạ bundle từ 12 xuống 8.3MB và tick sạch checklist.

✅ Dùng AI làm reviewer thay vì coder — cách ít ai nói
✅ Biên bản lỗi: trang demo sót, ảnh méo, permission khai mà không dùng, lorem ipsum
✅ Privacy policy viết thật: lưu SĐT để xác nhận đặt bàn, không bán cho ai
✅ Hạ bundle <10MB: PNG→WebP, bỏ font nhúng, import markdown chọn lọc
✅ Hai khấc sống còn: màn lỗi mạng + nút back trong webview
✅ zmp build: 12.1 → 8.3 MB — màn hình ánh sáng xanh

Timestamps:
00:00 Người duyệt có 5 phút
00:20 AI làm mặt lạnh
01:15 Biên bản lỗi dài hơn tưởng
02:00 Sửa thật + privacy policy
02:50 Con số phải hạ: 10MB
03:15 Ba thủ phạm, ba obrada
03:50 8.3 MB — đậu
04:10 Hai khấc dễ bỏ sót
04:45 Checklist 100% (teaser gửi duyệt)

#ZaloMiniApp #vibecoding #laptrinh #bundleSize #webp #LapTrinhLaCuocSong #appreview #checklist #zmp #React #aiagent #privacypolicy
```

### 4c. Keywords

```
zalo mini app, kiem duyet app, reviewer ai, dung ai lam reviewer, bundle size giam, toi uu ung dung, webp anh, system font, import chon loc, checklist phat hanh, privacy policy mau, permission thua, nut back webview, man hinh loi mang, zmp build, vibe coding, lap trinh la cuoc song
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#09` góc trên phải.

### Option 1 — "AI LÀM / NGƯỜI DUYỆT"
- Image: Prompt 1. Text: `AI LÀM` (trắng) / `NGƯỜI DUYỆT` (blue) + badge `MẶT LẠNH` nhỏ.

### Option 2 — "12MB / CÒN 8.3"
- Image: Prompt 2. Text: `12MB` (trắng, gạch đỏ) / `CÒN 8.3` (blue) + badge `ĐẠU <10MB`.

### Option 3 — "100% / MỚI DÁM GỬI"
- Image: Prompt 3. Text: `100%` (trắng) / `MỚI DÁM GỬI` (blue) + badge `#09`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
