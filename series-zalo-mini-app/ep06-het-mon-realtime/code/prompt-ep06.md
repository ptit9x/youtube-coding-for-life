# Prompts EP06 — verbatim cho Opus

## Prompt 1 — Hết món realtime + optimistic + race (scene 3)

```
Bối cảnh: Mini App "Chan Thêm". Đã có: dishes.available (EP02), tab admin +
admin-api Edge Function (EP04), menu realtime, giỏ hàng pre-order (EP05).

Nhiệm vụ: lên plan tính năng "hết món":
1) Tab admin: công tắc bật/tắt available cho từng món (qua admin-api).
2) Menu khách: realtime — món available=false thì mờ, badge "Hết món",
   không thêm được vào giỏ. Chỉ đổi dòng món affected, không re-render cả list.
3) Xử lý va chạm: món đang nằm trong giỏ bị tắt giữa chừng → bỏ khỏi giỏ,
   hiện thông báo nhỏ; Edge Function nhận đơn thì rà lại từng món, loại món
   đã tắt trước khi ghi vào orders.

QUY TẮC: trình PLAN trước, chờ mình approve, chưa sửa file.
Plan nêu rõ: optimistic UI cho công tắc admin (đổi ngay, lùi nếu fail),
và thứ tự xử lý race: quầy thắng, khách được báo, server là trọng tài.
```

Ghi chú production:
- Cảnh 6+7 cần 2 thiết bị + người phụ bấm (như EP04). Cảnh race (7) nên tập dượt 1 lần trước khi quay thật — timing khó.
- Kiểm tra lại data quán sau khi quay xong: bật lại available cho các món đã tắt trong demo.
