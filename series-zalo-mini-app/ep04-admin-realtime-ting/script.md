# EP04 — Quán nhận đơn: realtime tiếng ting + Edge Function giữ chìa khóa | Zalo Mini App #4

- **Trạng thái:** 📝 script draft — chờ host duyệt (chưa quay)
- **Runtime mục tiêu:** ~8–9 phút (tập "trả nợ" của cả season 1)
- **Word count PART 1:** 630 từ (~6.6 phút thoại)
- **Repo app:** `/home/vmo/vibe-coding/chan-them`
- **Pre-flight:** verify UI "Replication" của Supabase (bật Realtime cho bảng) tại thời điểm quay; test âm thanh ting trên thiết bị quay.

## PART 1 — SCRIPT

Đơn đặt bàn nằm gọn trong database. Sáng nay ba khách đặt, mẹ mình không biết ai cả. Vì mẹ không đọc dashboard Supabase. Không ai bán phở mà đọc dashboard.

Hôm nay chấm dứt cảnh đó. Một màn hình cho quán, đơn mới tự chạy tới, có tiếng ting, và nút bấm xác nhận. Hai thứ phải làm: realtime và quyền.

Realtime trước, vì dễ hiểu mà ít ai giải thích. Supabase Realtime, dưới nắp capô, là cơ chế cũ của Postgres: LISTEN NOTIFY. Khi một dòng được chèn vào bảng bookings, Postgres hét lên một tiếng, Supabase bắt lấy, đẩy qua websocket tới mọi client đang nghe. App mình chỉ việc subscribe kênh của bảng bookings. Không F5. Không hỏi mỗi năm giây. Chuyện tới thì nó tới.

Mình gửi spec cho Opus: màn hình admin, ẩn với khách, hiện khi zaloId trùng chủ quán; danh sách booking hôm nay; cột mới rơi vào thì kêu ting. Nó lên plan. Nó chủ động gợi ý thêm settings cho tiếng ting và rung. Gọn, mình duyệt. Code chạy nhanh, và đây là cảnh đáng xem nhất từ đầu series: điện thoại mình đặt bàn, tablet ở quầy kêu ting, đơn hiện lên không cần F5. Hai thiết bị, một dòng data, chạy xuyên qua server Singapore.

Nhưng thử bấm nút Xác nhận trên đơn. Không xong. Lỗi. Đỏ lựng.

Và đây không phải bug. Là phòng thủ của chính mình từ tập hai. RLS hiện chỉ cho hai việc: ai cũng đọc được menu, ai cũng chèn được booking. Chỉnh sửa trạng thái đơn? Không ai được phép. Khách không được, chủ quán cũng không. Cánh cửa khóa kín đúng như thiết kế.

Cách phá khóa dở nhất: mở policy update cho tất cả. Mở là khách ghé app cũng bấm được nút hủy đơn của người khác. Cách phá dở nhì, tinh vi hơn: nhét service role key vào code app. Chìa tổng, mở mọi cửa. Nhét vào client nghĩa là chìa tổng nằm trong bundle javascript, ai tải app về cũng mổ ra đọc được. Đây chính là lỗi mà Opus vừa đề xuất trong plan của nó. Nó ghi: nhanh nhất là dùng service role key phía client. Câu đó sai về security, đúng về deadline. Và mình từ chối. Không phải vì mình đạo đức hơn AI, mà vì quán có SĐT thật của khách thật trong database.

Cách đúng: đẩy việc nhạy cảm lên server. Supabase có Edge Function, một hàm nhỏ chạy trên server của họ, môi trường Deno. Chìa tổng chỉ nằm ở đó, trong biến môi trường, không xuống client bao giờ. App gọi hàm, hàm kiểm tra mã PIN admin, đúng thì dùng chìa tổng đổi trạng thái đơn. Nhắc debt từ tập ba: zaloId có thể giả danh. Giờ mọi lệnh nhạy cảm đi qua Edge Function, có PIN, có chìa tổng phía server. Trả nợ xong một món.

Mình yêu cầu Opus làm lại plan theo hướng đó. Nó làm, mình review từng dòng: hàm admin dash confirm và cancel, PIN đọc từ env, chỉ trả kết quả, không trả key. Duyệt. Deploy Edge Function. Rồi khoảnh khắc đích: đặt bàn từ điện thoại, đơn hiện trên tablet, bấm Xác nhận, trạng thái đổi từ Chờ sang Đã xác nhận, ngay trước mắt, không load lại trang.

Tóm tắt mùa một bằng một câu: quán có quy trình đóng. Khách đặt, quán duyệt, data sống một chỗ. Nhưng khách ngồi xuống rồi thì gọi món thế nào? Vẫn phải gọi miệng. Tập sau mình nối menu với bàn: giỏ hàng, gọi món trước, và câu hỏi khó nhất series này: quán đổi giá mai, thì đơn hôm qua tính theo giá nào. Làm theo cùng mình thì lưu kênh, hẹn gặp lại.

---

## PART 2 — SHOT LIST

Quy tắc series: không quay chờ gen/deploy (time-lapse 3–5s); giữ nguyên: prompt, review plan, cảnh AI-đề-xuất-sai, cảnh hai thiết bị song song. Mở đầu 3–5s recap EP03 (booking row trong Supabase).

| # | Tag | Nội dung quay | Dialogue map | Giây |
|---|-----|---------------|--------------|------|
| 1 | [PHONE]+[BROWSER] | Split: đặt bàn trên phone (nhanh) ‖ Supabase dashboard trên laptop — row mới; overlay "MẸ KHÔNG BIẾT" | Cold open | 25 |
| 2 | [DIAGRAM] | Excalidraw: client A INSERT → Postgres (LISTEN/NOTIFY) → websocket → client B tự render; gạch bỏ biểu tượng "poll mỗi 5s" | "Realtime trước… chuyện tới thì nó tới" | 40 |
| 3 | [IDE] | DÁN Prompt 1 (admin realtime) → plan Opus (kèm gợi ý sound + vibrate); host scroll review → approved | "Mình gửi spec cho Opus… mình duyệt" | 40 |
| 4 | [PHONE]+[TABLET] | **Cảnh chủ lực — quay song song 2 máy:** phone đặt bàn → tablet ở quầy kêu TING + đơn hiện; giữ nguyên nhịp, không cắt | "Code chạy nhanh… xuyên qua server Singapore" | 35 |
| 5 | [TABLET] | Bấm "Xác nhận" → lỗi đỏ (RLS chặn); zoom thông báo lỗi | "Nhưng thử bấm nút Xác nhận… Đỏ lựng" | 20 |
| 6 | [DIAGRAM] | 3 phương án trên bảng: (1) mở policy hết ❌ (2) service_role trong client ❌ (3) Edge Function ✅; mỗi cái 1 dòng lý do | "Cách phá khóa dở nhất… nằm trong bundle" | 40 |
| 7 | [IDE] | Zoom plan của Opus, dòng "dùng service role key phía client cho nhanh" highlight đỏ; host lắc đầu, gõ prompt phản biện (Prompt 2) | "Đây chính là lỗi mà Opus vừa đề xuất… khách thật trong database" | 45 |
| 8 | [DIAGRAM] | Flow Edge Function: app → gọi hàm (kèm PIN) → env giữ service_role → đổi status → trả kết quả; badge "DEBT PAID: zaloId spoof" | "Cách đúng: đẩy việc nhạy cảm… trả nợ xong một món" | 35 |
| 9 | [IDE] | Prompt 3 (làm lại plan) → plan mới: admin-api confirm/cancel; host đọc từng dòng (zoom đoạn PIN env + không trả key) → approved → deploy (time-lapse 4s) | "Mình yêu cầu Opus làm lại… không trả key" | 50 |
| 10 | [PHONE]+[TABLET] | **Cảnh đích:** phone đặt bàn → tablet ting → bấm Xác nhận → status đổi "Chờ → Đã xác nhận" realtime; KHÔNG cắt | "Rồi khoảnh khắc đích… không load lại trang" | 30 |
| 11 | [DIAGRAM] | Recap season 1 một màn hình: khách → app → Supabase → admin; các pain đã gỡ đánh dấu xanh | "Tóm tắt mùa một… data sống một chỗ" | 25 |
| 12 | [B-ROLL] | Tô phở bốc khói đặt cạnh tablet đang hiện đơn; overlay "TẬP 5: GỌI MÓN TRƯỚC" | Teaser + CTA | 15 |

**Tổng: 400 giây ≈ 6,7 phút hình** (+ thoại dày hơn chút → runtime ~8 phút).

**Batch-record:** scene 3+7+9 một phiên IDE (cùng conversation Opus); scene 4+5+10 cần 2 thiết bị + người phụ giúp bấm phone (quay trước/lấy bằng camera thứ hai hoặc phone thứ ba); scene 1 dùng footage tái sử dụng từ EP03 scene 12.

---

## Prompt cho Opus

### Prompt 1 — Màn hình admin realtime (scene 3)

```
Bối cảnh: Mini App "Chan Thêm". Đã có bảng bookings trong Supabase; app đã có
zaloId (EP03). Chủ quán = zaloId OWNER_ID (biến env).

Nhiệm vụ: lên plan tab admin ẩn trong app: chỉ hiện khi zaloId khớp OWNER_ID.
Gồm: danh sách booking theo ngày, trạng thái (pending/confirmed/done/cancelled),
và realtime: subscribe bảng bookings qua Supabase Realtime, dòng mới thì phát
tiếng ting (Web Audio) + rung nếu thiết bị hỗ trợ.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
Lưu ý: KHÔNG tự đổi policy RLS. Việc đổi trạng thái đơn sẽ làm ở bước sau
qua Edge Function — plan chỉ cần để nút disabled kèm chú thích.
```

### Prompt 2 — Phản biện đề xuất sai (scene 7)

```
Bạn vừa đề xuất nhét service_role key vào code client để sửa trạng thái booking
cho nhanh. Giải thích lại: ai đọc được bundle Mini App? Nếu key lộ, attacker
làm được gì với dữ liệu khách (SĐT thật)? Rồi đề xuất lại phương án không đưa
key xuống client. Trình plan mới, chưa đụng file.
```

### Prompt 3 — Edge Function admin-api (scene 9)

```
Bối cảnh: đã chốt phương án Edge Function (Deno) trên Supabase cho thao tác
admin. service_role key nằm trong env của hàm (SUPABASE_SERVICE_ROLE_KEY),
không xuống client.

Nhiệm vụ: lên plan hàm admin-api với 2 endpoint: booking/confirm, booking/cancel.
Input: booking id + ADMIN_PIN. Hàm kiểm tra PIN (env ADMIN_PIN), đúng thì dùng
service key đổi status, sai thì trả 401. Response không bao giờ chứa key.
Kèm: cách app gọi hàm, và nút admin nối vào đó.

QUY TẮC: trình PLAN trước, chờ approve, chưa tạo file.
```

Lưu verbatim tại `code/prompt-ep04.md`.

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic photograph of a tablet mounted on a small restaurant counter displaying a glowing blue order list with one highlighted new order, steam from pho bowls in the warm background, dramatic blue tech glow contrasting warm amber kitchen light, shallow depth of field, 8k, photorealistic, like a high-end food tech commercial. Not a screenshot, not a tutorial, not cartoon.`

2. `A cinematic photograph of two devices on a dark wooden table — a smartphone showing a booking confirmation and a tablet ringing with a notification bell icon glowing neon blue — connected by a floating beam of blue light, dark moody room, high contrast, 8k, photorealistic, developer documentary style. Not a screenshot, not a tutorial, not cartoon.`

3. `A cinematic close-up photograph of a developer's hand refusing a glowing red key icon floating above a keyboard while a green secure vault door glows in the background screen, dark room lit by monitor glow, neon blue and red accents, deep shadows, 8k, photorealistic. Not a screenshot, not a tutorial, not cartoon.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles (5)

1. `Zalo Mini App #4: Đơn về tới quầy, quán có tiếng ting | Lập trình là cuộc sống`
2. `Zalo Mini App #4: AI đề xuất để lộ key, mình nói không | Lập trình là cuộc sống`
3. `Zalo Mini App #4: Realtime không F5 — đơn tự chạy tới | Lập trình là cuộc sống`
4. `Zalo Mini App #4: Edge Function: chìa tổng không bao giờ xuống client | Lập trình là cuộc sống`
5. `Zalo Mini App #4: Nút Xác nhận bị khóa — và đó là điều đúng | Lập trình là cuộc sống`

### 4b. SEO Description

```
Đơn đặt bàn vào database rồi… nhưng mẹ chủ quán không đọc dashboard. Tập 4 (finale mùa 1): realtime tiếng ting cho quán + Edge Function giữ chìa khóa — và khoảnh khắc AI đề xuất sơ hở bảo mật, host phải bắt.

✅ Supabase Realtime = Postgres LISTEN/NOTIFY đẩy qua websocket
✅ Tab admin ẩn theo zaloId chủ quán, ting + rung khi có đơn mới
✅ Nút Xác nhận bị RLS chặn — phòng thủ đúng như thiết kế
✅ AI đề xuất nhét service_role key vào client → host phản biện, làm lại plan
✅ Edge Function (Deno): PIN + chìa tổng chỉ sống phía server
✅ Trả nợ EP03: zaloId spoofable → thao tác nhạy cảm qua server

Links:
- Supabase Realtime: https://supabase.com/docs/guides/realtime
- Supabase Edge Functions: https://supabase.com/docs/guides/functions
- Zalo Mini App docs: https://mini.zalo.me/docs

Timestamps:
00:00 Mẹ không đọc dashboard
00:40 Realtime dưới nắp capô
01:20 Tab admin + tiếng ting
02:00 Hai thiết bị, một dòng data
02:20 Nút Xác nhận… khóa đỏ
02:45 Ba cách phá khóa, hai cách dở
03:30 AI đề xuất lộ key — phản biện
04:15 Edge Function giữ chìa tổng
05:05 Chốt màn: đặt → ting → xác nhận
05:35 Recap mùa 1 + teaser giỏ hàng

#ZaloMiniApp #Supabase #Realtime #EdgeFunction #Deno #vibecoding #laptrinh #LapTrinhLaCuocSong #security #serviceRoleKey #RLS #aiagent
```

### 4c. Keywords

```
zalo mini app, supabase realtime, postgres listen notify, websocket don hang, edge function supabase, deno la gi, service role key, bao mat api key, admin panel, tab admin an, tieng thong bao, realtime khong f5, vibe coding, ai lam sai, ai bao mat, prompt phan bien, lap trinh la cuoc song, quan an cong nghe, app nha hang viet nam
```

---

## PART 5 — THUMBNAIL PACKAGE (3 options)

Visual identity: Zalo blue `#0068FF` + trắng + đen/navy. Badge `#04` góc trên phải.

### Option 1 — "ĐƠN TỰ / CHẠY TỚI"
- Image: Prompt 1. Text: `ĐƠN TỰ` (trắng) / `CHẠY TỚI` (blue) + badge `TING!` nhỏ.

### Option 2 — "AI ĐỀ XUẤT / LỘ KEY"
- Image: Prompt 3. Text: `AI ĐỀ XUẤT` (trắng) / `LỘ KEY` (blue, shock word) + badge `NÓI KHÔNG` viền đỏ.

### Option 3 — "HAI MÁY / MỘT DÒNG DATA"
- Image: Prompt 2. Text: `HAI MÁY` (trắng) / `MỘT DÒNG DATA` (blue, 2 dòng) + badge `#04`.

Typography: như các tập trước (Anton, 1280×720, dòng 110–140px, stroke đen, glow blue, check 320×180).
