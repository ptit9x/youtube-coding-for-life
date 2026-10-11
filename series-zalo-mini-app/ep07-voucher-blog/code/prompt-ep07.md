# Prompts EP07 — verbatim cho Opus

## Prompt 1 — Review toàn bộ schema (scene 4)

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

## Prompt 2 — CRUD blog (scene 6)

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

Ghi chú production:
- Scene 4: kết quả review của Opus cần chuẩn bị trước (chạy thật ngoài camera) để biết lỗi thật nó bắt là gì; nếu không phải index, sửa thoại + diagram cho khớp sự thật — không dàn dựng lỗi giả.
- Scene 7: bài blog viết trên màn hình là bài THẬT của quán — không placeholder.
