# Prompts EP05 — verbatim cho Opus

## Prompt 1 — Orders schema (scene 5)

```
Bối cảnh: Mini App "Chan Thêm". Đã có: bookings (EP03), admin realtime +
Edge Function admin-api (EP04), menu realtime từ dishes. Giỏ hàng lấy từ
cart components của template.

Nhiệm vụ: lên plan bảng orders + flow pre-order: khách đặt bàn kèm món
(hoặc mang đi). Đơn gồm items (món + số lượng), liên kết booking_id nếu có,
tổng tiền, ghi chú, trạng thái (new/accepted/served/cancelled).

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
```

## Prompt 2 — Chất vấn snapshot giá (gõ ngay sau khi plan hiện, cùng scene 5)

```
Câu hỏi: quán đổi giá món ngày mai, thì đơn hôm qua hiện tổng bao nhiêu?
Nếu items chỉ lưu dish_id thì chuyện gì xảy ra với đơn cũ khi bảng dishes
đổi giá? Phân tích rồi tự sửa plan nếu cần — nhớ mục tiêu: đơn là hóa đơn,
không được đổi sau khi chốt.
```

Ghi chú production:
- Thứ tự bắt buộc trên màn hình: Prompt 1 → plan hiện (items = dish_id[]) → Prompt 2 → AI tự sửa → approved. Đó là toàn bộ beat "host thắng AI một keo".
- Sau scene 8 (test vàng): ĐỔI LẠI giá gốc trong Supabase ngay để data quán thật không hỏng — quên là tai nạn.
