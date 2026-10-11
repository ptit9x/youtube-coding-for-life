# EP07 — Voucher + Blog: lý do quay lại + chỗ kể chuyện của quán | Zalo Mini App #7

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~8 phút (đầy nhất season 2 — 2 tính năng + review schema)
- **Word count PART 1:** 644 từ (~6.8 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** verify `react-markdown` tương thích bundle size (<10MB tổng); chuẩn bị bài blog đầu tiên thật của quán.

## PART 1 — SCRIPT

Ứng dụng chạy trơn từ khách tới bếp. Nhưng cứ nhìn người khách rời quán là thấy vấn đề: không có gì níu. Hết ăn là hết app. Trên mạng người ta gọi đây là retention, mình gọi bằng tiếng quán: khách quen.

Hôm nay gắn hai móc níu. Chiều: voucher cho khách. Tối: blog cho quán.

Voucher trước, vì cấu trúc nó thú vị hơn vẻ ngoài. Bảng vouchers giữ thứ quán phát: tiêu đề, loại giảm, giá trị, điều kiện đơn tối thiểu, hạn. Bảng user_vouchers giữ thứ khách giữ: ai lưu voucher nào, lúc nào, và đã dùng chưa. Tách hai bảng là tách hai quyền: quán quyết định phát gì, khách quyết định giữ gì. Môi giới là một dòng trong bảng giữa.

Và một dòng ấy dạy một bài database đáng nhớ: cùng một khách, bấm lưu một voucher hai lần, sinh ra hai dòng giống hệt nhau. Để yên thì kho voucher của người ta phình lên dữ dội. Bài học: unique constraint, ràng buộc duy nhất trên cặp zaloId và voucherId. Database tự từ chối dòng trùng, code không cần nhớ. Ràng buộc đặt đúng chỗ thì lỗi không bao giờ kịp sinh ra.

Nhưng khoan, theo dõi kỹ kiểu nghĩ của mình một chút. Đây là lượt soát tổng thể từ đầu series, và mình muốn AI làm việc đó cùng mình. Bảy tập, chục bảng, không ai rà lại hết thì sớm muộn cũng có thứ rơi. Mình nhờ Opus review toàn bộ schema: đọc từng bảng, từng quan hệ, chỉ ra chỗ yếu. Nó trả lời được phần lớn, và bắt được một lỗi thật: query voucher của tôi quét bảng user_vouchers theo zaloId, mà cột ấy chưa có index. Quán ba bàn thì chưa thấy, ba trăm đơn một ngày thì query chậm dần. Mình duyệt migration thêm index. Máy nghĩ được điều người mệt thì bỏ sót.

Giờ blog. Cái quán nào cũng có chuyện: bát phở của bà ngoại, chuyến tàu mang gia đình vào Nam, bí quyết Nin xương sáu tiếng. Mấy chuyện ấy đang đổ lên Facebook, lướt hai ngày là chìm. App có trang blog là quán giữ được chuyện của mình trong nhà. Về kỹ thuật, đơn giản bất ngờ: một bảng posts, app render markdown, y như README trên GitHub. Ai Maintains cũng được: textarea trong tab admin, viết bằng markdown, bấm đăng. Không deploy, không duyệt lại app. Nội dung là data, data đổi thoải mái.

Có một câu phân quyền phải trả lời: ai được đăng bài? Câu trả lời của cả series đến giờ: mọi thứ nhạy cảm đi qua Edge Function với PIN. Blog không ngoại lệ. Chỉ có chủ quán được publish. Mình gửi spec, Opus lên plan CRUD, mình review đúng một chỗ: route publish phải nằm sau admin-api, không có đường tắt nào từ client thẳng vào bảng posts. Duyệt.

Và một điều tiền thưởng không nằm trong plan: viết bài đầu tiên. Mình không nhờ AI viết. Bài kể chuyện mẹ mình bắt đầu bán phở từ cái xe đẩy. Máy biết cấu trúc câu, người mới biết chuyện. Đó cũng là tinh thần của cả series: AI lo phần khuôn, mình lo phần hồn.

Kiểm chứng chốt: khách lưu voucher "tô phở giá một nghìn khai trương", quầy dập dấu đã dùng, khách bấm lưu lần nữa bị database từ chối. Bài blog hiện trong app, đọc được trên điện thoại, kèm ảnh quán thật.

Giờ app đã đủ: khách tới, đặt, gọi, được tặng, đọc chuyện quán. Nhưng cả hệ thống này vẫn chỉ có một người dùng thật: gia đình mình. Không ai ngoài xóm biết Chan Thêm tồn tại trên Zalo. Tập sau: mở cửa. Nút share, vòng lan truyền, và bài học từ những chuỗi lớn. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen (time-lapse 3–5s); giữ nguyên: prompt, cảnh AI review schema, cảnh host tự viết blog. Mở đầu 3–5s recap EP06 (món mờ realtime).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE] | Khách ăn xong, trả tiền, đóng app — màn hình chính Zalo; overlay "HẾT ĂN LÀ HẾT APP" | Cold open | 20 |
| 2 | [DIAGRAM] | 2 bảng vouchers + user_vouchers và dòng trung gian; nhãn "quán phát / khách giữ" | "Voucher trước… bảng giữa" | 30 |
| 3 | [IDE] | Demo lỗi: INSERT 2 dòng trùng zaloId+voucherId → dòng 2 nổ unique violation; zoom dòng lỗi; rồi [DIAGRAM] thêm constraint | "Và một dòng ấy… kịp sinh ra" | 35 |
| 4 | [IDE] | DÁN Prompt 1 (review toàn bộ schema sau 6 tập) → Opus trả kết quả: list bảng + điểm yếu; zoom mục "user_vouchers.zalo_id thiếu index" → host gõ "approve migration" | "Nhưng khoan… người mệt thì bỏ sót" | 50 |
| 5 | [DIAGRAM] | Blog = 1 bảng posts + markdown render; so sánh nhanh bên cạnh README GitHub | "Giờ blog… data đổi thoải mái" | 30 |
| 6 | [IDE] | Prompt 2 (CRUD blog) → plan; host zoom đúng route publish → admin-api; gõ câu chốt "không đường tắt" → approved | "Có một câu phân quyền… Duyệt" | 40 |
| 7 | [IDE] | **Host tự viết bài đầu tiên** trong textarea markdown (không AI): vài câu chuyện mẹ + xe đẩy; preview render đẹp | "Và một điều tiền thưởng… phần hồn" | 40 |
| 8 | [PHONE] | Kiểm chứng: lưu voucher → quầy dập used (tablet) → bấm lưu lần 2 bị chặn; mở blog trong app đọc bài, có ảnh quán | "Kiểm chứng chốt… ảnh quán thật" | 35 |
| 9 | [PHONE] | Màn hình Zalo trống, search "Chan Thêm" không ra; overlay "0 NGƯỜI DÙNG" | "Giờ app đã đủ… tồn tại trên Zalo" | 15 |
| 10 | [B-ROLL] | Ai đó share app vào nhóm Zalo (thu sẵn); overlay "TẬP 8: MỞ CỬA" | Teaser + CTA | 15 |

**Tổng: 310 giây ≈ 5,2 phút hình** + thoại dày → runtime ~7,5–8 phút.

**Batch-record:** scene 3+4+6 một phiên IDE (conversation Opus liên tục); scene 7 quay riêng trọn take (gõ chậm, chữ thật); scene 8 cần tablet + phone như EP06.

---

## Prompt cho Opus

### Prompt 1 — Review toàn bộ schema (scene 4)

```
Bối cảnh: Mini App "Chan Thêm" đã qua 6 tập: categories, dishes (RLS read),
bookings (anon insert), orders (jsonb snapshot), user vouchers sắp tạo,
sắp thêm posts. Tab admin + Edge Function admin-api đã chạy.

Nhiệm vụ: đóng vai DBA review toàn bộ schema hiện có: đọc từng bảng, từng
quan hệ, từng policy RLS; chỉ ra (1) điểm yếu hiệu năng (index thiếu cho
query thật), (2) mâu thuẫn quyền nào giữa các policy, (3) trường nào thừa
hoặc thiếu. Sắp xếp theo mức độ quan trọng. Chưa sửa gì — chỉ báo cáo.

Kèm: đề xuất migration cho top 1 điểm yếu, chờ mình approve.
```

### Prompt 2 — CRUD blog (scene 6)

```
Bối cảnh: đã có admin-api Edge Function với ADMIN_PIN (EP04). Cần trang blog
cho quán: danh sách + đọc bài, admin viết bài bằng markdown (textarea) và
publish. Bảng posts: title, cover_url, content_md, published, published_at.

Nhiệm vụ: lên plan CRUD blog + 2 trang khách (list, detail render markdown
bằng react-markdown). Quy tắc quyền: publish/unpublish và mọi ghi đều qua
admin-api; client chỉ được SELECT bài published.

QUY TẮC: trình PLAN trước, chờ approve, chưa sửa file.
Plan phải vẽ rõ route publish đi qua Edge Function — không đường tắt nào
từ client thẳng vào bảng posts.
```

Lưu verbatim tại `code/prompt-ep07.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a hand holding a phone showing a glowing blue gift voucher card in a food app, steam from pho bowls in a warm restaurant background, dramatic blue neon glow on the voucher edges, shallow depth of field, bokeh lights, 8k, photorealistic, high-end commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of a small Vietnamese pho restaurant owner writing on a tablet at night, the screen showing a blog editor, warm lamp light on her face, the kitchen softly blurred behind with a giant stock pot, intimate documentary mood, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic split photograph of an old food cart on a Vietnamese street at dawn on the left and the same scene as a illustrated blog cover on a glowing phone screen on the right, connected by drifting steam, moody blue and amber tones, high contrast, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #7: Voucher + Blog: níu khách quay lại quán | Lập trình là cuộc sống`
2. `Zalo Mini App #7: AI rà schema 6 tập, bắt được 1 index thiếu | Lập trình là cuộc sống`
3. `Zalo Mini App #7: Lưu voucher 2 lần? Database tự nói không | Lập trình là cuộc sống`
4. `Zalo Mini App #7: Blog cho quán phở, viết xong không cần deploy | Lập trình là cuộc sống`
5. `Zalo Mini App #7: AI lo phần khuôn, mình lo phần hồn | Lập trình là cuộc sống`

### 4b. SEO Description

```
App chạy trơn rồi — nhưng hết ăn là hết app. Tập 7: hai móc níu khách (voucher + blog), một lượt AI review toàn bộ schema sau 6 tập (bắt được index thiếu), và bài blog đầu tiên không cho AI viết.

✅ vouchers + user_vouchers: tách "quán phát" khỏi "khách giữ"
✅ Unique constraint: database tự chặn lưu trùng — lỗi không kịp sinh ra
✅ AI đóng vai DBA review schema: bắt user_vouchers.zalo_id thiếu index
✅ Blog = bảng posts + react-markdown; viết bài không cần deploy/duyệt lại
✅ Quyền publish đi qua Edge Function — không đường tắt vào posts
✅ Bài mở màn: chuyện mẹ bán phở từ xe đẩy — AI lo khuôn, mình lo hồn

Timestamps:
00:00 Hết ăn là hết app
00:20 Voucher: quán phát, khách giữ
01:10 Lưu 2 lần — database nói không
01:40 AI rà toàn bộ schema 6 tập
02:30 Blog cho quán: chuyện không chìm theo Facebook
03:10 Quyền publish: không đường tắt
03:50 Viết bài đầu tiên (không AI)
04:30 Kiểm chứng chốt
05:00 0 người dùng ngoài gia đình (teaser share)

#ZaloMiniApp #Supabase #vibecoding #laptrinh #voucher #blog #markdown #reactmarkdown #LapTrinhLaCuocSong #uniqueconstraint #databaseindex #aiagent
```

### 4c. Keywords

```
zalo mini app, voucher tich hop, he thong voucher, unique constraint postgres, index database, review schema, dba ai, blog trong app, react markdown, xuat ban bai viet, khong can deploy, retention khach hang, vibe coding, lap trinh la cuoc song, quan pho, app nha hang
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#07` góc trên phải.

### Option 1 — "HẾT ĂN / KHÔNG HẾT APP"
- Image: Prompt 1. Text: `HẾT ĂN` (trắng) / `KHÔNG HẾT APP` (blue) + badge `#07`.

### Option 2 — "AI RÀ / 6 TẬP SCHEMA"
- Image: Prompt 2 (biến thể: màn hình schema). Text: `AI RÀ` (trắng) / `6 TẬP SCHEMA` (blue) + badge `BẮT 1 LỖI`.

### Option 3 — "AI LO KHUÔN / MÌNH LO HỒN"
- Image: Prompt 3. Text: `AI LO KHUÔN` (trắng) / `MÌNH LO HỒN` (blue) + badge `#07`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
