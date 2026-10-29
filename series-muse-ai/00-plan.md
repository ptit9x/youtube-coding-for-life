# SERIES MUSE AI — AI LÀM, NGƯỜI GIỮ QUYỀN QUYẾT ĐỊNH

## Định vị series

Series hướng dẫn dùng Muse như một AI agent có kiểm soát. Mỗi tập giải quyết một workflow thật, có dữ liệu thật và bước kiểm chứng cuối cùng.

Điểm khác biệt của series không phải “AI bấm được bao nhiêu nút”. Điểm khác biệt là host luôn giữ context, quyền duyệt và trách nhiệm.

## Workflow bắt buộc trong mọi tập

1. **Yêu cầu:** Nêu mục tiêu, context và giới hạn quyền.
2. **Plan:** Muse trình bày cách làm trước khi hành động.
3. **Review:** Host đọc plan, kiểm tra nguồn, file, quyền và tác động.
4. **Approve:** Host xác nhận hành động cụ thể.
5. **Thực hiện:** Muse thao tác; đoạn chờ được tua nhanh và có narration.
6. **Kiểm chứng:** Mở nền tảng thật, xem diff hoặc chạy test. Không dùng lời xác nhận của AI làm bằng chứng.

## Roadmap

| Tập | Trạng thái | Chủ đề | Outcome chính | Cầu nối |
|---|---|---|---|---|
| EP01 | Sẵn sàng dựng | Quản lý Facebook Page và YouTube với Muse | Đọc số liệu, tạo draft, upload Short và comment; người giữ quyền publish | Muse làm được việc trên nhiều nền tảng. Nhưng có cần ngồi trước máy không? |
| EP02 | Kịch bản mới | Điều khiển Muse từ điện thoại | Giao việc trên điện thoại, tiếp tục trên Mac/WhatsApp, theo dõi task chạy nền và kiểm chứng | Khi workflow không còn phụ thuộc thiết bị, Muse có thể đồng hành với một project code không? |
| EP03 | Kịch bản mới | Vibe coding với Muse Spark | Build một status dashboard nhỏ theo workflow plan → review → implement → test | Muse Spark làm được project nhỏ. Tập sau đánh giá toàn bộ hệ sinh thái sau thời gian sử dụng. |
| EP04 | Tạm hoãn theo yêu cầu host | Tổng hợp những gì đang làm với Muse app | Code review, schedule, TTS, media và API | Chỉ sửa sau khi host hoàn tất footage và chốt scope. |
| EP05 | Dự kiến | Muse Code cho developer | Cài CLI, làm việc với repo thật, review diff và test | Từ app consumer sang coding agent chuyên dụng. |
| EP06 | Dự kiến | Meta Model API | Gọi Muse Spark bằng SDK/Postman, phân biệt API chính thức và workaround | Khép series bằng workflow có thể tái sử dụng trong sản phẩm. |

## Quy tắc continuity

- EP01 gọi đúng EP02 ở outro; EP02 gọi EP03; EP03 gọi EP04.
- Không nhắc “series AI Miễn Phí” trong title card hoặc narration mới.
- Một tập chỉ có một outcome trung tâm; tính năng phụ chỉ tồn tại để chứng minh outcome đó.
- Prompt đặt inline ngay sau đoạn thoại mô tả hành động.
- Muse phải dừng trước hành động công khai, gửi tin, publish, mua hàng hoặc sửa code.
- Mọi claim về giá, token, model, vùng hỗ trợ và API phải kiểm tra lại trong ngày quay.

## Chuẩn hình ảnh

- Muse và browser dùng dark mode nếu giao diện hỗ trợ.
- IDE dùng **One Dark Pro**, font **JetBrains Mono 18px**.
- Terminal prompt sạch, không hiện hostname hoặc secret.
- Footage chờ tua 4–10x; narration giải thích concept trong lúc tua.
- Crop đủ lớn để đọc trên điện thoại; che email, token, cookie và tài khoản cá nhân.

## Chuẩn thư mục

```text
series-muse-ai/
├── 00-plan.md
├── epNN-ten-tap/
│   ├── script.md
│   ├── assets/
│   └── code/
```

Không tạo `code/prompts.md`. Prompt luôn nằm trong `script.md`.

## Kiểm tra trước khi xuất bản

- Số tập trong folder, H1, description và thumbnail phải trùng nhau.
- Tổng shot list phải bằng runtime công bố.
- Không giữ màn hình chờ ở tốc độ thật quá ba giây.
- Không gọi publishable/anon key của Supabase là secret.
- Không trình bày công cụ reverse proxy dùng cookie như API chính thức.
- Link, referral code và giới hạn token phải được test lại.
- Outro phải gọi đúng tập tiếp theo.
