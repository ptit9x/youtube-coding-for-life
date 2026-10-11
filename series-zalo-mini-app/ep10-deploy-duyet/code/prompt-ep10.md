# Prompts EP10 — verbatim cho Opus

## Prompt 1 — Soạn giải trình permission (scene 5)

```
Bối cảnh: Mini App "Chan Thêm" (quán phở) gửi duyệt phát hành trên Zalo.
App xin 3 quyền: getUserInfo (hiện tên/avatar trong app), getPhoneNumber
(điền SĐT khi đặt bàn), share (gửi voucher cho bạn bè).

Nhiệm vụ: soạn bản nháp phần "giải trình mục đích sử dụng quyền" cho từng
permission trong form gửi duyệt. Mỗi quyền 2–3 câu, tiếng Việt, nói đúng
thực tế app làm. Mục tiêu: người duyệt đọc xong hiểu quyền đó dùng ở màn
nào, cho ai, vì sao cần.

KHÔNG bịa công năng app không có. Nếu thiếu thông tin thì hỏi mình trước.
```

Ghi chú production:
- Tập này QUAY THẬT toàn bộ: login, deploy, điền form, bấm gửi — không diễn lại. Bấm hỏng là mất take.
- Chạy `zmp login` + `zmp deploy` thử một vòng TRƯỚC ngày quay (vào bản Testing cũ) để biết flow thật.
- Bấm gửi duyệt thật XONG CUỐI buổi quay batch; cảnh "Đã duyệt" capture khi email/notification tới — dành cho EP11.
