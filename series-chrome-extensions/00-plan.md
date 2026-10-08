# Series Plan — "Vibe Coding Chrome Extensions" (Học lập trình bằng LLM)

- **Format:** Series ngắn hạn (Mini-series) hướng dẫn làm Chrome Extension phức tạp (MV3) bằng phương pháp Vibe Coding (Pair-programming với AI Agent). Host tự quay màn hình + tự thoại âm.
- **Thời lượng:** Mỗi video khoảng 5–7 phút.
- **Topic lane:** "Học lập trình bằng LLM" — series hướng dẫn framework/công nghệ cho Fresher, host học và build cùng LLM coding agent.
- **Giá trị cốt lõi (The "Why"):** Chứng minh rằng trong thời đại AI, Dev không mất việc mà chuyển hoá thành "Kiến trúc sư". AI viết code tốt nhất khi có một "móng nhà" (boilerplate) chuẩn và luật lệ rõ ràng.
- **Nguyên tắc:** Mỗi tập giải quyết một concept hoặc một mảng kỹ thuật cụ thể của Chrome Extension và cách dùng AI để bypass sự khó khăn đó.
- **Technical baseline:** React 18, Vite, Turborepo, TailwindCSS, TypeScript. Chrome Extension Manifest V3 (MV3).
- **AI tool:** Cursor / Windsurf / Antigravity IDE.
- **Workflow mỗi video:** (1) Yêu cầu → (2) AI lên Plan → (3) Host Review → (4) Host Approve → (5) AI Code → (6) Kiểm chứng.

---

## Danh sách tập

### EP 01 — Khám phá Boilerplate làm Chrome Extension "bá đạo" nhất
- **Beat variant:** Học bằng LLM (Concept Explainer hybrid)
- **Mục tiêu:** Giới thiệu cái "móng nhà" vững chắc (Jonghakseo/chrome-extension-boilerplate-react-vite).
- **Pain-point giải quyết:** Cấu hình rườm rà, thiếu Hot Module Replacement (HMR), tổ chức code lộn xộn khi làm Chrome Extension.
- **Nội dung chính:** Review cấu trúc thư mục (Monorepo), packages/shared, packages/ui. Demo HMR cực xịn.
- **Runtime mục tiêu:** ~6 phút (~540–660 words)
- **Script file:** `ep01-boilerplate/script.md`

### EP 02 — Vibe Coding 101: Code App AI phức tạp bằng mồm!
- **Beat variant:** Học bằng LLM
- **Mục tiêu:** Build Earpiece AI (App nghe lén phỏng vấn nhắc bài) bằng AI Agent.
- **Pain-point giải quyết:** MV3 architecture phức tạp (Service Worker + Offscreen Document).
- **Nội dung chính:** Demo "Master Prompt" để điều khiển AI tạo ra cấu trúc giao tiếp qua `IcMessage`, tự sinh code Tailwind cho Option Pages. Nhấn mạnh việc Dev đóng vai trò Kiến trúc sư (Architect).
- **Runtime mục tiêu:** ~7 phút (~630–770 words)
- **Script file:** `ep02-earpiece-ai/script.md`
