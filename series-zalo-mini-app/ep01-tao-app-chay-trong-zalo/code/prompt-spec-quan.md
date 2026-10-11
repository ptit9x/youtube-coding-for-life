# Prompt 1 — Spec quán "Gắp Thêm" cho Opus (EP01, scene 10–11)

Gõ verbatim vào agent panel của Antigravity (Opus), theo đúng shot list:

```
Bối cảnh: mình đang làm Zalo Mini App cho quán cơm gia đình nhỏ (tên Gắp Thêm),
quay series YouTube. Project vừa scaffold từ template e-commerce của zmp-cli
(React + TypeScript + Tailwind + ZaUI), chưa sửa gì. Backend dự kiến Supabase.

Nhiệm vụ: lên plan sản phẩm cho v1 gồm: xem menu, đặt bàn, gọi món trước
(pre-order), voucher, blog, tab admin ẩn cho chủ quán.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file. Plan phải nêu:
scope từng mảng, bảng dữ liệu cần, rủi ro, thứ tự triển khai đề xuất.
Cuối cùng gợi ý phần nào nên cắt khỏi v1 cho một quán 3 bàn.
```

Ghi chú production:
- Prompt tiếng Việt cho dễ demo — nhắc trên phim: làm thật thì prompt tiếng Anh rẻ hơn.
- Sau khi Opus trả plan: host scroll review, highlight 3 mục thanh toán/giao hàng/tích điểm, gõ yêu cầu cắt scope, rồi approve. Toàn bộ theo 6 bước: Yêu cầu → Plan → Review → Approve → Code (tập sau) → Kiểm chứng.
