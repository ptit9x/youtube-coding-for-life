# Prompts EP08 — verbatim cho Opus

## Prompt 1 — Hỏi mentor về placement (scene 3)

```
Mình không cần code ngay. Câu hỏi sản phẩm: Mini App quán phở "Chan Thêm"
đã có menu, đặt bàn, pre-order, voucher (kèm màn "Đã lưu"), blog. Giờ muốn
gắn nút chia sẻ qua openShareSheet.

Hỏi: nên đặt nút share ở đâu cho người dùng Việt thật sự bấm? Đề xuất
3 vị trí, mỗi vị trí kèm: ai bấm, lúc nào, vì sao họ bấm (hoặc không bấm).
Không code — chỉ tư vấn. Cuối cùng đoán vị trí nào conversion cao nhất
và giải thích.
```

## Prompt 2 — Code share sheet (scene 6)

```
Bối cảnh: đã chốt share ở màn hình voucher đã lưu.

Nhiệm vụ: lên plan thêm nút share gọi openShareSheet với tiêu đề
"Chan Thêm — tặng bạn voucher quán phở" và đường dẫn mini app (type zalo
mini app, path tới màn voucher). Kèm nút bật/tắt chia sẻ cho từng voucher
trong tab admin (qua admin-api).

QUY TẮC: trình PLAN trước, chờ approve, chưa sửa file.
```

Ghi chú production:
- Scene 7 cần nhóm Zalo thật + 2 điện thoại: chuẩn bị trước, xin phép nhóm hoặc dùng nhóm nội bộ đội làm phim.
- Nút share text "Chan thêm một tô cho bạn" là đoạn host TỰ GÕ của tập — không cho AI viết câu này.
