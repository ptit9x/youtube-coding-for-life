# EP02 — Supabase: menu thật, đổi giá không cần deploy | Zalo Mini App #2

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~7–8 phút
- **Word count PART 1:** 674 từ (~7.1 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them` (từ EP01)
- **Pre-flight:** verify lại UI Supabase (tạo project / SQL editor / Policy editor) trước khi quay — UI đổi theo tháng.

## PART 1 — SCRIPT

Sáng nay mẹ đổi giá tô đặc biệt. Mình phải mở code, sửa một con số, build lại app, chờ ba phút. Cả nhưng tai họa đó chỉ để đổi giá một tô phở.

Đó là hậu quả của tập trước. Menu đang nằm trong file json của template, cứng ngắc. Hôm nay mình dọn nó vào một căn nhà đàng hoàng: database thật.

Mình chọn Supabase. Một nền tảng backend mã nguồn mở, tặng kèm Postgres, API sinh sẵn, và phân quyền. Tầng miễn phí đủ dư cho quán ba cái bàn.

Tạo project mất hai phút. Vùng server chọn Singapore, gần Việt Nam nhất. Xong. Giờ đến phần quan trọng nhất tập này: thiết kế bảng.

Và mình không thiết kế một mình. Mở Antigravity, gọi Opus, luật cũ: trình plan trước, chưa đụng file. Nhiệm vụ: schema cho menu quán phở. Nó trả lại một bản plan rất chuyên nghiệp. Bảng categories cho nhóm món, bảng dishes cho món. Rồi nó thêm nữa. Bảng i18n cho đa ngôn ngữ. Bảng audit log ghi ai sửa gì. Cả bảng rating năm sao cho khách chấm điểm.

Đẹp đấy. Cho một chuỗi nhà hàng một trăm chi nhánh. Quán mình có ba bàn. Khách của mẹ toàn người quen trong xóm. i18n bỏ. Audit log bỏ. Rating, nữa mới cần. Mình gõ lại yêu cầu, cắt từng mục, và bảo AI giải thích lại vì sao cắt được. Nó rút gọn còn hai bảng. Mình duyệt.

Phần SQL migration mình tự gõ, từng dòng. Không phải vì AI gõ dở. Vì tự gõ là cách mình chắc chắn hiểu từng dòng mình sắp chạy. Categories giữ nhóm món: phở, nước, thêm. Dishes giữ tên món, mô tả, giá, ảnh, và một cờ available đánh dấu hết món. Một chi tiết nhỏ: giá là số nguyên. Nghìn đồng làm đơn vị. Tiền mà lưu số thập phân là mời gọi rắc rối.

Chạy migration. Hai bảng hiện ra, trống trơn. Mình nhập mười món thật của quán, giá thật, ảnh chụp điện thoại buổi sáng.

Rồi khóa cửa. Supabase mặc định mở hoàn toàn sau khi tạo bảng. Ai có link cũng đọc được, sửa được. Không được. Mình bật RLS, Row Level Security. Ý tưởng: kiểm soát nằm ngay tại từng dòng dữ liệu. Như quán có ba bàn thì canh từng bàn, chứ không đứng canh một cánh cổng duy nhất. Chính sách đầu tiên: mọi người chỉ đọc được menu. Không ai sửa được từ phía app.

Supabase đưa hai loại chìa khóa. Anon key là chìa khách, công khai được, chỉ làm đúng những gì chính sách cho phép. Service role key là chìa tổng, mở mọi cánh cửa. Chìa tổng nằm trong file env của server, đi vào gitignore, và không bao giờ, dưới bất kỳ hình thức nào, xuống phía client.

Giờ nối app vào nhà mới. Nhờ Opus sửa service đọc menu: từ đọc file json chuyển sang fetch Supabase. Kèm plan, như mọi khi. Nó sửa một file, diff mười mấy dòng. Mình đọc từng dòng, duyệt, chạy.

Mở app trong Zalo. Menu demo biến mất. Menu thật của quán hiện lên, mười món, từ database. Một vòng trace ngắn: app gửi request, Supabase select từ bảng dishes, app render. Hết. Không ma thuật nào cả.

Kiểm chứng cuối cùng, cũng là khoảnh khắc đáng tiền nhất tập này. Mình mở bảng dishes ngay trên điện thoại, sửa giá tô đặc biệt, lưu. Quay lại app, F5. Giá mới hiện ngay. Không build. Không deploy. Mẹ muốn đổi giá, mẹ nhắn mình một tin, xong trong mười giây.

Nhưng có một chuyện dto rồi. Một ngàn người mở app Chan Thêm, với app họ là một ngàn khách lạ không tên. Không đặt bàn được, không giữ voucher được, vì app không biết ai là ai. Tập sau: dùng chính tài khoản Zalo của khách làm định danh, và làm cái form đặt bàn đầu tiên. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay thời gian chờ (install, gen code) — time-lapse 3–5s. Giữ nguyên: prompt gõ, plan review, SQL host tự gõ, git diff, moment app chạy. Dark IDE, font ≥18px. Mở đầu bằng 3–5s recappain EP01 (file json cứng).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [IDE] | Freeze frame `mock/products.json` + mũi tên đỏ vào con số giá; overlay "SÁNG NAY…" | Cold open (3 câu) | 25 |
| 2 | [DIAGRAM] | Excalidraw: hộp "file json cứng" → mũi tên → "Supabase Postgres" + nhãn "đổi giá không build" | "Đó là hậu quả… database thật" | 20 |
| 3 | [BROWSER] | supabase.com → New project → chọn region Singapore → tạo (time-lapse nhẹ phần chờ provisioning 60–90s) | "Mình chọn Supabase… hai phút" | 30 |
| 4 | [IDE] | Antigravity: DÁN Prompt 1 (schema menu) → gửi; plan của Opus hiện ra, scroll tới mục i18n/audit/rating, host highlight từng mục | "Và mình không thiết kế một mình… rất chuyên nghiệp" | 55 |
| 5 | [IDE] | Host gõ yêu cầu cắt scope (Prompt 2) → AI rút gọn plan còn 2 bảng → status "approved" | "Đẹp đấy… mình duyệt" | 45 |
| 6 | [IDE] | SQL editor Supabase: host TỰ GÕ migration (categories + dishes) — quay thật toàn bộ, tốc độ 1.2x tối đa; zoom cột `price int` và `available boolean` | "Phần SQL migration mình tự gõ… mời gọi rắc rối" | 70 |
| 7 | [BROWSER] | Table editor: nhập 10 món thật (time-lapse 5s sau 2 món đầu); bảng dishes có data | "Chạy migration… buổi sáng" | 20 |
| 8 | [DIAGRAM] | Sơ đồ RLS: 3 bàn + lock icon từng bàn vs 1 cổng + guard; policy "SELECT only" | "Rồi khóa cửa… từ phía app" | 40 |
| 9 | [IDE] | File `.env`: dán anon key (service_role quay NHANH qua, blur nếu lộ); `git status` thấy .env ignored | "Supabase đưa hai loại chìa… phía client" | 30 |
| 10 | [IDE] | Prompt 3 (fetch menu) → plan → diff của Opus: `services/menu.ts` json → supabase query; host đọc diff từng dòng | "Giờ nối app vào nhà mới… duyệt, chạy" | 45 |
| 11 | [PHONE] | App trong Zalo thật: menu thật 10 món hiện lên (so sánh split nhanh với menu demo cũ) | "Mở app trong Zalo… không ma thuật nào cả" | 25 |
| 12 | [PHONE] | Supabase table editor trên điện thoại: sửa giá tô đặc biệt → lưu → F5 app → GIÁ MỚI (cảnh tiền thưởng — giữ nguyên không cắt) | "Kiểm chứng cuối cùng… mười giây" | 35 |
| 13 | [BROWSER] | Supabase: bảng bookings/vouchers chưa tồn tại — hover chỗ trống; overlay "AI LÀ AI?" | "Nhưng có một chuyện… khách lạ không tên" | 20 |
| 14 | [B-ROLL] | Điện thoại + tô phở + laptop; overlay "TẬP 3: ĐẶT BÀN" | Teaser + CTA | 15 |

**Tổng: 475 giây ≈ 7,9 phút hình.**

**Batch-record:** scene 3 một phiên browser; scene 4+5+10 một phiên IDE; scene 6 quay riêng (trọn takes); scene 11+12 một phiên phone sau khi code xong thật.

---

## Prompt cho Opus

### Prompt 1 — Thiết kế schema menu (scene 4)

```
Bối cảnh: Zalo Mini App "Chan Thêm" (quán phở gia đình 3 bàn). Đã scaffold xong,
chưa có backend. Vừa tạo Supabase project (region Singapore). Menu hiện nằm trong
mock/*.json của template.

Nhiệm vụ: lên plan schema Postgres cho menu quán phở: nhóm món và món. Kèm chính
sách RLS gợi ý (mục tiêu: public chỉ đọc được menu).

QUY TẮC: trình PLAN trước, chờ mình approve, chưa tạo file, chưa chạy SQL.
Plan nêu: bảng, cột, kiểu dữ liệu, lý do từng quyết định, rủi ro.
```

### Prompt 2 — Cắt scope (scene 5)

```
Plan của bạn đang quá to cho quán 3 bàn: bỏ i18n, bỏ audit log, bỏ rating.
Giữ tối thiểu để chạy menu thật. Trình lại plan rút gọn, giải thích ngắn
vì sao phần bỏ đi là an toàn. Chưa đụng file.
```

### Prompt 3 — Đổi service đọc menu (scene 10)

```
Bối cảnh: đã có bảng categories + dishes trong Supabase, RLS cho phép anon SELECT.
App đang đọc menu từ mock/*.json trong services/menu.ts.

Nhiệm vụ: lên plan sửa services/menu.ts sang fetch Supabase bằng anon key
(từ import.meta.env). Giữ nguyên interface trả về để page không phải sửa.

QUY TẮC: trình PLAN + diff dự kiến trước, chờ approve mới sửa file.
```

Lưu bản verbatim tại `code/prompt-ep02.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a young Vietnamese developer at a dark desk at night looking at two screens, one showing a glowing blue database table UI and the other a phone food menu, dramatic Zalo blue neon lighting, steam rising from a bowl of pho beside the keyboard, shallow depth of field, bokeh city lights through window, 8k, photorealistic, like a high-end tech commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic close-up photograph of a hand editing a glowing blue database table row on a laptop in a dark room, the row showing a food price number highlighted in neon blue, a bowl of pho and chopsticks in the blurred background lit by monitor glow, high contrast, deep shadows, 8k, photorealistic, developer documentary style. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic photograph of a smartphone on a wooden restaurant table displaying a noodle soup menu app, floating blue data sync arrows connecting the phone to a distant glowing server rack silhouette in the dark background, moody lighting, shallow depth of field, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #2: Đổi giá trên điện thoại, menu tự cập nhật | Lập trình là cuộc sống`
2. `Zalo Mini App #2: Menu thật trong Supabase, hết cảnh build lại app | Lập trình là cuộc sống`
3. `Zalo Mini App #2: RLS là gì và vì sao khóa từng dòng dữ liệu | Lập trình là cuộc sống`
4. `Zalo Mini App #2: AI thiết kế schema, host cắt 3 bảng thừa | Lập trình là cuộc sống`
5. `Zalo Mini App #2: Database cho quán 3 bàn, đúng vừa đủ | Lập trình là cuộc sống`

### 4b. SEO Description

```
Mẹ đổi giá tô phở → phải build lại app?! Tập 2: dọn menu từ file json cứng vào Supabase thật — đổi giá trên điện thoại, menu tự cập nhật, không build, không deploy.

✅ Supabase là gì: Postgres + API + phân quyền trong một nền tảng
✅ AI lên schema menu → host review, cắt i18n/audit/rating bằng YAGNI
✅ Tự gõ SQL migration từng dòng: categories + dishes, giá là số nguyên
✅ RLS (Row Level Security): khóa ở từng dòng dữ liệu, public chỉ đọc
✅ anon key vs service_role key: chìa khách và chìa tổng
✅ Kiểm chứng: sửa giá trong DB → F5 app → giá mới

Links:
- Supabase: https://supabase.com
- Zalo Mini App docs: https://mini.zalo.me/docs

Timestamps:
00:00 Đổi giá một tô phở, tai họa ba phút
00:45 Supabase: nhà mới cho data
01:15 AI lên schema… quá to cho quán 3 bàn
02:45 Host tự gõ SQL migration
04:15 RLS: canh từng bàn, không canh cổng
05:15 Hai loại chìa khóa
05:45 Menu thật chạy trong Zalo
06:40 Sửa giá DB → app đổi ngay
07:20 Khoan — app chưa biết ai là ai

#ZaloMiniApp #Supabase #Postgres #RLS #vibecoding #laptrinh #React #TypeScript #LapTrinhLaCuocSong #database #aiagent
```

### 4c. Keywords

```
zalo mini app, supabase tieng viet, hoc supabase, supabase la gi, row level security, rls supabase, postgresql cho nguoi moi, schema database, thiet ke database menu, vibe coding, ai lam app, vibe coding tieng viet, zmp-cli, menu nha hang, app quan an, doi gia khong deploy, supabase free tier, anon key, service role key, gitignore env, lap trinh la cuoc song, developer viet nam
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#02` góc trên phải.

### Option 1 — "ĐỔI GIÁ / KHÔNG BUILD"
- Image: Prompt 2. Text: `ĐỔI GIÁ` (trắng) / `KHÔNG BUILD` (blue, "KHÔNG" shock word) + badge `#02`.

### Option 2 — "MENU / TỰ ĐỔI"
- Image: Prompt 3. Text: `MENU` (trắng) / `TỰ ĐỔI` (blue) + badge `DB THẬT` nhỏ.

### Option 3 — "AI VIẾT / MÌNH CẮT"
- Image: Prompt 1. Text: `AI VIẾT` (trắng) / `MÌNH CẮT` (blue) + badge `#02`.

Typography: như EP01 (Anton, 1280×720, dòng 110–140px, stroke đen 6–10px, glow blue 8–12px 60–70%, không đè mặt người, check 320×180).
