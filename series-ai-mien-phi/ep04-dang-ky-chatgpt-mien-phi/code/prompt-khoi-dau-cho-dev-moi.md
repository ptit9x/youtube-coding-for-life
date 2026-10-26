# EP02 — Bộ Prompt Khởi Đầu Cho Dev Mới (dùng với ChatGPT free)

> Companion của script EP02. Đây là những prompt dùng được ngay sau khi đăng ký —
> đúng triết lý kênh: **AI giải thích, mình hiểu** — không phải AI viết hộ, mình copy.

## Quy tắc 3 nhịp (nhắc lại trong video)

1. Dán **đúng đoạn code liên quan** — đừng ném cả file 500 dòng.
2. Hỏi **ngắn**, dồn ngữ cảnh vào một câu.
3. Yêu cầu **giải thích + phản biện** — đừng nhờ viết hộ.

## 10 prompt khởi đầu

### 1. Hiểu hàm lạ (prompt đầu tiên trong video)
```
Giải thích hàm này cho mình như cho người mới học Node.js. Đi từng bước,
không bỏ bước nào:

<dán 1 hàm ngắn vào đây>
```

### 2. Đọc code cũ của chính mình
```
Đây là code mình viết 6 tháng trước, giờ mình không hiểu nữa :(
Giải thích nó làm gì, và chỉ ra 1 chỗ dễ gây bug nhất.
```

### 3. Đọc thông báo lỗi
```
Mình gặp lỗi này khi chạy Node.js. Giải thích lỗi xảy ra vì đâu,
và gợi ý mình tự fix theo hướng nào (đưa hướng dẫn, đừng đưa code hoàn chỉnh):

<dán stack trace>
```

### 4. Hỏi trước khi Google 10 tab
```
Mình là fresher Node.js. Giải thích sự khác nhau giữa
`synchronous` và `asynchronous` bằng một ví dụ đời thực ngoài lập trình.
```

### 5. Review code ngược
```
Đóng vai senior review code này. Chỉ ra đúng 3 vấn đề quan trọng nhất,
xếp theo mức độ nghiêm trọng, kèm lý do:

<dán đoạn code>
```

### 6. Học concept bằng cách bị hỏi ngược (chuẩn bị phỏng vấn)
```
Mình vừa học xong REST API. Đặt cho mình 5 câu hỏi phỏng vấn fresher
từ dễ đến khó, mỗi câu một chủ đề. Đợi mình trả lời xong rồi mới chấm.
```

### 7. Chọn 1 trong nhiều lựa chọn
```
Mình cần chọn giữa Express, Fastify và NestJS cho project học tập cá nhân.
Bối cảnh: mình biết JavaScript cơ bản, muốn đi làm backend Node.js.
Phân tích ngắn gọn và chọn HÀNG ĐẦU cho case của mình — đừng liệt kê mọi thứ.
```

### 8. Giải thích lại theo kiểu khác (khi vẫn chưa hiểu)
```
Vẫn chưa hiểu. Giải thích lại khái niệm này như thể mình là học sinh cấp 3,
dùng phép so sánh với nấu ăn.
```

### 9. Viết commit message / README (việc nhỏ, cho AI làm)
```
Viết commit message ngắn gọn cho diff này theo conventional commits:

<dán git diff>
```

### 10. Kết thúc phiên học — tự tổng kết
```
Trong phiên chat này mình đã hỏi về: <liệt kê>. Tạo cho mình 1 trang
"cheat sheet" 10 dòng chốt lại kiến thức, để mình tự đọc lại mai.
```

## Lưu ý quota (bản free)

- Mỗi câu hỏi kèm code dài = tốn quota nhanh → dán đoạn tối thiểu.
- Hết quota trong ngày → thường vẫn chat được model nhẹ hơn; việc nặng để mai.
- Đừng multi-account: mất lịch sử chat là mất "bộ nhớ học tập" giá trị nhất.
