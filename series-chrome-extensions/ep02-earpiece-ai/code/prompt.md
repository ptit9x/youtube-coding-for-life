Dựa trên repo boilerplate chrome-extension-boilerplate-react-vite (React 18 + Vite + Turborepo + Tailwind), hãy giúp tôi xây dựng "Earpiece AI" - một Chrome Extension (MV3) giúp transcribe audio từ online meetings (Google Meet, Zoom) và dùng AI để gợi ý câu trả lời.

Core Architecture & Data Flow (Bắt buộc tuân thủ):

Kiến trúc MV3: Giao tiếp qua IcMessage contract (đặt trong packages/shared/lib/messages.ts).
Service Worker (src/background): Quản lý orchestrate chrome.tabCapture.getMediaStreamId và gửi streamId đi.
Offscreen Document (pages/offscreen): DOM duy nhất chạy Web Speech API. Cần có cơ chế auto-restart mỗi 30s để vượt giới hạn của Chrome. Trả transcript về UI.
Side Panel (pages/side-panel): UI chính hiển thị Transcript (bên trái) và AI Suggestion (bên phải).
Hệ thống Settings & Storage (packages/storage & pages/options):
Sử dụng pattern createStorage của boilerplate để quản lý file cấu hình EarpieceConfig.
Cần một trang Options page đẹp mắt chứa các cấu hình quan trọng. Ví dụ phần "Recognition & Conversation" cần có:
userName: Tên ứng viên (giúp Speech-to-text nhận diện đúng hơn).
sttLang: Ngôn ngữ STT (Hỗ trợ en-US, vi-VN, ja-JP, ko-KR, zh-CN).
Các toggle switches (boolean): oneOnOne (Call 1-1), showVietnamese (Hiện dịch tiếng việt), debugAllRemote.
minConfidence: Lọc nhiễu âm thanh.
Design System (packages/ui):
Đừng code UI trực tiếp vào file. Hãy tách các component cơ bản như <Card>, <Field>, <Input>, <Select>, <Button> vào package packages/ui để tái sử dụng ở cả Side Panel và Options Page.
Sử dụng TailwindCSS, thiết kế giao diện tối (Dark mode) hiện đại.
i18n (Đa ngôn ngữ):
Áp dụng hệ thống đa ngôn ngữ vào packages/i18n/locales/{en,vi}/messages.json. Mọi string UI (ví dụ: "Recognition & Conversation") cần phải lấy từ hệ thống i18n để đảm bảo tính đồng bộ.
Step-by-Step Execution Plan:

Bước 1: Định nghĩa EarpieceConfig trong storage và IcMessage contract. Setup component library cơ bản trong packages/ui.
Bước 2: Xây dựng trang Options với RecognitionSection để quản lý config.
Bước 3: Tạo Offscreen document và viết logic auto-restart cho Web Speech API.
Bước 4: Cấu hình Service worker kết nối luồng capture audio.
Bước 5: Xây dựng Side Panel hiển thị real-time transcript và AI suggestion.
Bắt đầu ngay với Bước 1: Hãy liệt kê cấu trúc thư mục sẽ tạo và cho tôi xem code của EarpieceConfig cùng vài component UI cốt lõi.