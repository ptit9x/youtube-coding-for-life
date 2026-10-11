# Prompts EP02 — verbatim cho Opus

## Prompt 1 — Thiết kế schema menu (scene 4)

```
Bối cảnh: Zalo Mini App "Chan Thêm" (quán phở gia đình 3 bàn). Đã scaffold xong,
chưa có backend. Vừa tạo Supabase project (region Singapore). Menu hiện nằm trong
mock/*.json của template.

Nhiệm vụ: lên plan schema Postgres cho menu quán phở: nhóm món và món. Kèm chính
sách RLS gợi ý (mục tiêu: public chỉ đọc được menu).

QUY TẮC: trình PLAN trước, chờ mình approve, chưa tạo file, chưa chạy SQL.
Plan nêu: bảng, cột, kiểu dữ liệu, lý do từng quyết định, rủi ro.
```

## Prompt 2 — Cắt scope (scene 5)

```
Plan của bạn đang quá to cho quán 3 bàn: bỏ i18n, bỏ audit log, bỏ rating.
Giữ tối thiểu để chạy menu thật. Trình lại plan rút gọn, giải thích ngắn
vì sao phần bỏ đi là an toàn. Chưa đụng file.
```

## Prompt 3 — Đổi service đọc menu (scene 10)

```
Bối cảnh: đã có bảng categories + dishes trong Supabase, RLS cho phép anon SELECT.
App đang đọc menu từ mock/*.json trong services/menu.ts.

Nhiệm vụ: lên plan sửa services/menu.ts sang fetch Supabase bằng anon key
(từ import.meta.env). Giữ nguyên interface trả về để page không phải sửa.

QUY TẮC: trình PLAN + diff dự kiến trước, chờ approve mới sửa file.
```

Ghi chú production:
- Prompt 3 được approve → diff hiện trong cùng cảnh (scene 10), host đọc diff từng dòng trước khi duyệt — đúng bước 3 và 6 của workflow.
