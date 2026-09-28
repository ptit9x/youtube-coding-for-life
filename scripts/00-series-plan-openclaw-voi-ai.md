# Series Plan — "OpenClaw: trợ lý AI tự host" (5 tập, lane: Học lập trình bằng LLM)

- **Format:** 5 tập 8–12 phút (tập concept ~9, tập thực hành ~11). Host tự quay màn hình + tự thoại âm. Toàn bộ demo chạy trên gateway OpenClaw thật của host (systemd `openclaw-gateway.service`, port 18789, OpenClaw 2026.9.6, cron jobs + Telegram delivery đang sống).
- **Nguyên tắc tách tập:** mỗi tập một outcome và một pain nối sang tập sau. Gộp được thì gộp — không kéo dài để chạm mốc thời lượng.
- **Baseline kỹ thuật:** Ubuntu + Node 24 (nvm), OpenClaw 2026.9.6 stable, Telegram làm channel chính (bot token qua @BotFather), model qua provider config (đang dùng zai/glm-5.3). Khi setup, luôn hiện phiên bản thật trên màn hình (`openclaw --version`).
- **AI canon của series:** giữ pattern hỏi–đọc–chất vấn–verify của kênh, nhưng "AI moment" mang tính meta: dùng chính agent OpenClaw để sinh nội dung (viết skill, phân tích run lỗi) rồi host kiểm chứng bằng transcript/config — agent là đối tượng lẫn công cụ của series.
- **Spine:** build MỘT trợ lý dev thật từ con số 0 — từ gateway trống đến trợ lý nhớ ngữ cảnh, tự gửi digest, chạy đúng workflow, khóa an toàn, đa kênh. Người xem theo dõi được từng thay đổi trong `~/.openclaw/`.
- **Chain rule:** tập sau mở bằng NỖI ĐAU tập trước tạo ra. Không tập nào mở bằng "hôm nay ta học X".
- **Differentiator:** mỗi tập đúng MỘT sequence liền mạch; mọi claim về config/lỗi đều có bằng chứng trên màn hình (transcript, `cron runs`, `git diff` cho skill). Không có cảnh "đọc docs hộ người xem".

## Competitor gap table (research 2026-09-28)

| Kênh | Format | Điểm yếu khai thác |
|---|---|---|
| Hostinger / Metics Media (EN, ~952K views) | 1 video dài "ultimate guide": deploy VPS 1-click, không viết code | Không đụng terminal thật, không debug, bán VPS; không có cron/skill sâu |
| Mì AI (VI) | Install A–Z trên VPS + tour tính năng | Dừng ở cài đặt; không có workflow dev, không có forensics lỗi |
| Hostinger VN (VI) | "Từ số 0 đến trợ lý trong 15 phút" | Setup một chiều; không nói bảo mật chiều sâu, không nói chi phí token |
| Blog/skill sites (openclawskills.dev, useclaw.pro) | Text guide cron/security | Không phải video; tài liệu third-party, cần verify lại từng claim |

**Định vị 3 trục:** ngôn ngữ (VI cho chủ đề EN-dominant) · format (mini-series mỗi tập 1 outcome vs 1 video dài) · góc (trợ lý của dev chạy trên máy dev — không phải VPS no-code; hiểu mechanism chứ không click-through).

## Tập 0 (đã có) — BONUS 17.5: Chatbot biết nói, Gateway biết làm

- File: `bonus-17-5-openclaw-ai-gateway/bonus-17-5-openclaw-ai-gateway.md` (script xong, quay được ngay).
- Vai trò trong series: tập mở màn — giới thiệu kiến trúc 3 lớp và chứng minh gateway thật. → **pain sang OC#01: muốn có bản tin 6:00 như vậy thì bắt đầu từ đâu?**

## OC#01 — Từ số 0 đến trợ lý trong Telegram: onboard, pairing và systemd

- ← pain: Bonus 17.5 cho thấy đích đến; người xem chưa có gì trong `~/.openclaw/`.
- Học: `openclaw onboard` (tự cài systemd user service), tạo bot @BotFather, `openclaw channels add --channel telegram --token`, pairing (`pairing list` → `approve`), cấu trúc thư mục `~/.openclaw/` (config, state, skills, media), `systemctl --user status`, journalctl.
- AI moment: hỏi agent "giải thích cấu trúc ~/.openclaw của mình như cho fresher" — host đối chiếu bằng `ls` thật.
- Thành quả: nhắn Telegram từ điện thoại, agent trả lời trên máy đang chạy gateway. → **pain: trợ lý chỉ trả lời khi mình nhắn — sáng nào cũng phải tự hỏi "có gì mới".**

## OC#02 — Cron jobs và digest mỗi sáng: robot làm ca đêm

- ← pain: agent phản hồi thụ động; muốn nó tự dậy 6:00 đọc tin và gửi digest.
- Học: `openclaw automations create` (cron expr, `--channel telegram --to <chatId>`), main vs isolated session (isolated = phiên riêng `cron:<jobId>`, không spam lịch sử chính), `cron run` test tay, `cron runs --id` xem status, timeoutSeconds cho job dài, chi phí token thật.
- AI moment: job lỗi thật (`error (4x)`) — mở transcript, phát hiện model khai "tool không tồn tại" dù có tool; fix một dòng config; chạy lại thành xanh. Log thắng lời kể của AI.
- Thành quả: digest 6:00 tự tới Telegram, job lỗi được chữa bằng bằng chứng. → **pain: mỗi lần giao việc theo workflow là phải dán lại cả đoạn hướng dẫn dài.**

## OC#03 — Skills và memory: dạy agent một lần, nhớ mãi

- ← pain: lặp prompt dài mỗi ngày; agent quên ngữ cảnh giữa các phiên.
- Học: viết `~/.openclaw/skills/dev-workflow/SKILL.md` (frontmatter + các bước workflow 6 bước của series NestJS), `openclaw skills list` ✓ ready, agent tự nạp skill khi việc khớp; session scope per-sender, `/new` reset, trí nhớ qua phiên.
- AI moment: giao việc có và không có skill — so sánh hai transcript; host review từng dòng skill như review PR (git diff khi thêm skill).
- Thành quả: agent theo đúng workflow 6 bước không cần nhắc; cùng model, hành vi khác. → **pain: agent chạy shell trên máy mình và nghe tin nhắn từ ngoài — ai cũng mở cửa được thì sao?**

## OC#04 — Bảo mật và đa kênh: khóa cửa, rồi mở thêm cửa

- ← pain: tiện quá nhưng đáng sợ — process chạy shell, nghe mọi tin nhắn.
- Học: pairing/allowlist là mặc định an toàn; `requireMention` cho nhóm; sandbox `non-main` (Docker) cho session lạ; bảo vệ secret (đừng để agent đọc `.env`, `~/.ssh`); cân nhắc khi cài skill từ ClawHub (kiểm tra nguồn — sẽ verify lại số liệu vụ skill độc khi viết script, không trích số third-party chưa kiểm chứng); thêm kênh thứ hai (WhatsApp QR hoặc WebChat) — cùng một trợ lý, nhiều cánh cửa.
- AI moment: mô phỏng người lạ nhắn bot → bị chặn ở pairing; host demo `configWrites: false` chặn agent tự sửa config từ chat.
- Thành quả: trợ lý đa kênh vẫn an toàn — người lạ không vào được, session lạ bị sandbox. → **pain (hướng đi tiếp, không thành tập): model là plugin — đổi model, fallback, chi phí.**

## Nguyên tắc xuyên suốt

1. Mỗi tập mở bằng NỖI ĐAU tập trước (chain rule).
2. Mỗi tập đúng MỘT AI sequence liền mạch, phục vụ một outcome.
3. Mọi claim cấu hình/lỗi phải có bằng chứng trên màn hình (transcript, `cron runs`, `ls`, `git diff`) — không có cảnh "tin mình đi".
4. Nói thẳng chi phí: token đốt như tiền điện; bắt đầu bằng một job.
5. Title đánh số series: `OpenClaw #NN: <hook> | Lập trình là cuộc sống`; thumbnail anchor `#NN` góc trái, màu nhận diện series là CYAN `#00D4FF` trên nền tối (khác NEST RED của series NestJS).
6. Bonus 17.5 giữ nguyên số hiệu (không đổi thành #01) để không phá anchor đã đăng; series mới đánh số từ #01 với prefix `OpenClaw`.
