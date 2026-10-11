# Prompts EP03 — verbatim cho Opus

## Prompt 1 — Định danh Zalo (scene 4)

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

## Prompt 2 — Form đặt bàn (scene 9)

```
Bối cảnh: đã có zaloId + getPhoneNumber (1 chạm). Bảng bookings (id, zalo_id,
name, phone, book_date, book_time, party_size, note, status, created_at) đã tồn
tại trong Supabase, RLS cho anon INSERT.

Nhiệm vụ: lên plan form đặt bàn: DatePicker, time slot sinh từ giờ mở cửa
(06:00–14:00, bước 30 phút), stepper số người (1–12), tên, SĐT (nút 1 chạm),
ghi chú. Validation client: không nhận ngày quá khứ, SĐT đủ 10 số, tên không trống.

QUY TẮC: trình PLAN trước, chờ approve, chưa sửa file.
```

Ghi chú production:
- Scene 4: sau khi AI xác nhận rủi ro spoof, host nói debt "Edge Function — EP04" và dán sticky lên bảng trắng (scene 5) — beat trả nợ ở tập sau.
- Scene 9: bắt buộc có cảnh host khoanh lỗi "thiếu rule ngày quá khứ" TRƯỚC khi gõ prompt sửa — đây là AI-sai-có-chủ-đích của tập.
