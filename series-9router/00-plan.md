# Series: 9Router — AI Gateway Cho Dev Thông Minh

## Tổng quan series

**Chủ đề:** 9Router — open-source local AI routing gateway giúp dev quản lý
nhiều AI coding tool (Claude Code, Cursor, Cline, Copilot...) qua 1 endpoint
duy nhất, tự động fallback khi hết quota, tiết kiệm token 20–40%.

**Đối tượng:** Junior/Fresher dev đang dùng hoặc muốn dùng AI coding tools
nhưng gặp vấn đề: tốn tiền subscription, bị rate limit, quản lý nhiều API key
phức tạp.

**Topic lane:** "Học lập trình bằng LLM" — series hướng dẫn tool cho dev,
storytelling-driven, không phải tutorial khô khan.

**Số tập:** 2 tập (có thể mở rộng thêm nếu cộng đồng quan tâm)

**Phiên bản 9Router:** v0.5.40–v0.5.50 (footage đã quay)

---

## Footage đã quay

| File | Thời lượng | EP | Nội dung |
|------|-----------|-----|---------|
| `001-install.mov` | 3:29 | EP01 | GitHub repo, npm install, providers, combo |
| `002-9router_cach_dung_co_ban.mov` | 6:54 | EP01 | Endpoint, API Key, Combo chi tiết, Usage, Settings |
| `002-9router_multi_task.mov` | 0:12 | EP01+02 | Heavy usage: 255 requests, $18.76 |
| `003_connect_claude01.mov` | 1:51 | EP02 | 9Router CLI Tools → Claude Cowork config |
| `003_use_with_claude_app.mov` | 6:52 | EP02 | Cowork: code review, plan |
| `003_use_with_claude_app002.mov` | 9:03 | EP02 | Cowork: fix bugs, commit, push |
| `003_use_with_claude_code.mov` | 9:48 | EP02 | Claude Code CLI: /init, CLAUDE.md, coding |
| `003_use_with_claude_code_install_plugin.mov` | 1:19 | EP02 | 9Router CLI interface + plugin install |
| `chatgpt_free_new_email.mov` | 0:33 | Bonus | ChatGPT Plus free trial trick |

---

## Danh sách tập

### EP01 — Cài đặt 9Router trên Mac và cách dùng cơ bản
- **Thời lượng mục tiêu:** 6–7 phút
- **Nội dung chính:**
  - Nỗi đau: bị rate limit, tốn tiền subscription
  - 9Router là gì — local AI routing gateway, open source, MIT
  - Cài đặt: `node -v`, `npm install -g 9router`
  - CLI interface: Web UI / Terminal UI / Hide to Tray
  - Dashboard (tiếng Việt): Điểm cuối → tạo API Key
  - Nhà cung cấp: OAuth (Claude Code, Codex, Copilot...), Free (iFlow, Kiro...), API Key (OpenRouter, GLM...)
  - Kết hợp (Combo): 4 chiến lược — Fallback, Vòng tròn, Fusion, Capacity auto-switch
  - Vision Adapter — auto-switch model khi cần vision
  - Thống kê: usage analytics, provider graph, recent requests
  - Token Saver, Cài đặt (ngôn ngữ, bảo mật)
- **Variant:** Học bằng LLM

### EP02 — 9Router + Claude Code & Claude Cowork
- **Thời lượng mục tiêu:** 7–8 phút
- **Nội dung chính:**
  - Claude Cowork config trong 9Router (tab Công cụ → endpoint, API key, models, MCP, Tools)
  - Demo Cowork: code review → plan → fix 9 issues → commit
  - Claude Code config: env vars hoặc 9Router CLI Tools
  - Lưu ý ANTHROPIC_AUTH_TOKEN conflict
  - Demo Claude Code: /init → CLAUDE.md → /model → coding
  - Claude Code plugins (context7)
  - Usage analytics: 255 requests, 12.5M tokens, mostly free
- **Variant:** Học bằng LLM

---

## Branding & Visual

- **IDE theme:** Monokai / Dracula / One Dark Pro
- **Font:** JetBrains Mono ≥18px
- **Terminal:** iTerm2, dark background, clean prompt
- **Dashboard:** 9Router dashboard tại localhost:20128 (tiếng Việt)
- **Color accent:** Neon green #00FF41, cyan #00D4FF, purple #BD93F9
