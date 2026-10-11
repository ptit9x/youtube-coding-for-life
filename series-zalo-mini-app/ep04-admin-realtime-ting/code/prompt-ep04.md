# Prompts EP04 — verbatim cho Opus

## Prompt 1 — Màn hình admin realtime (scene 3)

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

## Prompt 2 — Phản biện đề xuất sai (scene 7)

```
Bạn vừa đề xuất nhét service_role key vào code client để sửa trạng thái booking
cho nhanh. Giải thích lại: ai đọc được bundle Mini App? Nếu key lộ, attacker
làm được gì với dữ liệu khách (SĐT thật)? Rồi đề xuất lại phương án không đưa
key xuống client. Trình plan mới, chưa đụng file.
```

## Prompt 3 — Edge Function admin-api (scene 9)

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

Ghi chú production:
- Prompt 2 là "AI làm sai có chủ đích" của tập — bắt buộc có cảnh highlight dòng đề xuất lỗi trong plan TRƯỚC (đã có ở scene 7), rồi mới gõ prompt phản biện.
- Scene 4 + 10 cần 2 thiết bị: chuẩn bị phone (khách) + tablet (admin) và một người phụ bấm hoặc camera thứ ba; đấy là cảnh đáng tiền nhất mùa 1, quay nhiều takes.
