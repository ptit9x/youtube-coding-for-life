# Prompts Bonus B — verbatim cho Opus

## Prompt 1 — Tích hợp Checkout SDK sandbox (scene 6)

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

Ghi chú production:
- Chuẩn bị tài khoản merchant TEST/sandbox trước ngày quay — không đăng ký merchant thật trên camera.
- Phần hộ kinh doanh: narration + diagram, KHÔNG quay giấy tờ thật.
- Nếu sandbox flow đổi theo docs mới (tên param/màn hình), chạy thử trước và cập nhật thoại — số liệu/ten màn phải là thật.
