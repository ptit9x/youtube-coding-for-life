# BONUS 17.5 — OpenClaw: Chatbot biết nói, Gateway biết làm

- **Series:** Học NestJS bằng AI — Bonus sau tập 17, rẽ lane "Học lập trình bằng LLM" sang hạ tầng trợ lý AI tự host. Không thay đổi stack TaskFlow.
- **Target runtime:** ~10 phút
- **Vai trò:** Video đứng riêng, quay được ngay trên gateway OpenClaw đang chạy thật của host (systemd service, port 18789, 7 cron jobs, Telegram delivery).
- **Outcome:** Người xem hiểu kiến trúc channel – gateway – agent; tự chạy gateway 24/7 bằng systemd; tạo cron job trả digest về Telegram; khóa an toàn bằng pairing; điều tra job lỗi bằng transcript thật.

---

## PART 1 — SCRIPT

6 giờ sáng, tin nhắn Telegram đầu tiên đã nằm chờ.

Lịch hôm nay, vài tin công nghệ đáng đọc, và một job đang lỗi.

Mình chưa hỏi gì.

Người viết bản tin này không phải người. Nó là một process.

Trợ lý AI thì ai cũng có rồi.

ChatGPT trong tab, Gemini trong điện thoại.

Nhưng bạn chỉ trò chuyện được khi mở đúng app.

Hỏi xong, tự copy kết quả đi làm tiếp.

Nó biết nói. Nó không biết làm.

Bạn muốn nó đọc file trên máy, chạy terminal, sáng nào cũng tự gửi digest.

Thì lại mở app, dán context, xin code, tự chạy.

Xin script, tự đặt cron, tự đặt biệt lệnh hẹn giờ.

Ba việc tự làm đó có tên chung: bạn đang làm thay tool.

Trí nhớ nằm trên server người khác. Đổi messenger là mất trợ lý.

Rồi mình nhận ra vấn đề nằm ở một chữ.

Trợ lý đi cùng bạn phải nằm trên máy của bạn.

Giải pháp không phải một chatbot thông minh hơn.

Là một gateway.

OpenClaw, một process Node.js chạy trên chính máy dev của mình.

Nó không thông minh hơn ChatGPT. Nó chỉ có tay.

Có tay nghĩa là chạy được shell, đọc ghi file, mở browser, gọi API.

Cùng model đó, chat trong app thì chỉ nhận lời khuyên.

Qua gateway thì nó tự mở terminal chạy giúp bạn.

Hãy bóc kiến trúc này từng lớp.

Lớp ngoài cùng là channel: Telegram, WhatsApp, Discord.

Đó là nơi bạn gõ tin nhắn, mọi lúc, mọi nơi.

Lớp giữa là gateway, người lễ tân chạy trên máy bạn, lắng nghe cổng một-tám-bảy-tám-chín.

Tin nhắn đi Telegram qua long polling tới gateway.

Gateway gán nó vào đúng phiên của đúng người.

Phiên giống một cuốn sổ theo từng cuộc chat. Ngủ dậy vẫn còn.

Lớp trong cùng là agent cùng model bạn chọn.

Model là plugin. Sáng dùng model này cho việc tiếng Việt, trưa đổi model khác để soi code.

Một dòng config, không cài lại gì.

Chatbot thường là app người ta xây sẵn rồi mời bạn vào.

OpenClaw đảo ngược: bạn chạy server, messenger chỉ còn là cánh cửa.

Điều thú vị nhất xảy ra lúc 6 giờ sáng.

Gateway có scheduler riêng, đúng nghĩa cron của Linux.

Mình tạo job bằng một dòng lệnh: lịch trình, yêu cầu, đích trả về Telegram.

Đúng giờ, scheduler đánh thức agent trong một phiên riêng.

Agent chạy tool thật, đọc tin, chọn lọc, soạn digest.

Xong, nó gửi kết quả về đúng cuộc chat đã định.

Không ai thức. Không ai bấm nút.

Bạn muốn trợ lý 24/7 thì không được ngủ cùng máy tính.

Tức là gateway phải chạy như một service.

Systemd user service, không cần root.

Process crash thì systemd tự kéo nó dậy.

Mở lại máy, service tự sống lại, log nằm trong journalctl.

Cron job của gateway sống trong SQLite. Reboot không mất việc.

Nói thật: tự host không miễn phí.

Cron job đốt token như đốt tiền điện.

Model càng khoẻ, mỗi bản tin sáng càng đắt.

Hãy bắt đầu bằng đúng một job, xem nó đáng tiền hay không.

Bảo mật là phần phải nói thẳng.

Một process chạy shell trên máy bạn, nghe tin nhắn từ bên ngoài.

Ai nhắn cũng được chạy lệnh thì thảm họa.

OpenClaw khóa cửa bằng pairing, cơ chế ghép đôi.

Người lạ nhắn tới chỉ nhận một mã ghép đôi.

Bạn gõ lệnh approve trên máy, họ mới vào allowlist.

Số điện thoại sai một chữ số cũng không vào được.

Nhóm chat thì mặc định agent phải được mention mới trả lời.

Muốn chặt hơn, cho session lạ chạy trong sandbox Docker.

Đây là mặc định an toàn, không phải tùy chọn trả phí.

Cảnh đáng tiền nhất hôm nay đến từ chính máy mình.

Một cron job báo lỗi bốn lần liền.

Tin nhắn báo lỗi nói rằng tool không tồn tại.

Đáng lẽ mình tin, xóa job, dựng lại.

Thay vào đó, mình mở transcript, bản ghi từng bước của run đó.

Thực ra agent có tool. Model trả lời theo kiểu đoán.

Sửa một dòng config, chạy lại, job xanh.

Bài học cũ của ngành: log luôn thắng lời kể. Kể cả lời kể của AI.

Nếu bạn xem series NestJS, bạn thấy mình lặp một công thức.

Yêu cầu, AI lên plan, mình duyệt, AI làm, mình kiểm chứng.

Mỗi lần dạy AI workflow đó, lại mất một đoạn prompt dài.

Mình gom công thức đó thành một skill, một file markdown đặt vào thư mục skills của gateway.

Agent tự nạp skill khi việc khớp, và theo đúng workflow.

Từ đó không cần ai nhắc lại mỗi ngày.

Công thức tốt không nên nằm trong prompt. Nó nên nằm trong file chạy được.

Cổng một-tám-bảy-tám-chín đã sáng từ đầu video.

Bảy cron jobs, digest tự tới, trả lời từ mọi messenger mình cắm vào.

Chatbot biết nói. Gateway biết làm.

Trợ lý tốt nhất không phải model hay nhất.

Là model có tay, có trí nhớ, và nằm trên máy của bạn.

Mình là Richard. Lập trình là cuộc sống.

---

## PART 2 — SHOT LIST / SCREEN RECORDING GUIDE

| # | Type | Nội dung quay | Thời lượng |
|---|---|---|---:|
| 1 | [TERMINAL] | Màn hình Telegram: digest 6:00 thật + tin báo lỗi job `error (4x)` | 35s |
| 2 | [BROWSER] | ChatGPT/Gemini trả lời hay nhưng dừng ở chữ — không chạm được máy | 30s |
| 3 | [DIAGRAM] | Hai sơ đồ: chatbot khoá trong app vs gateway trên máy bạn | 45s |
| 4 | [DIAGRAM] | Kiến trúc 3 lớp: channels → gateway (port 18789, sessions, memory) → agent + model plugin | 70s |
| 5 | [TERMINAL] | Gateway thật: `systemctl --user status openclaw-gateway`, `ss -ltn \| grep 18789`, `openclaw --version` | 45s |
| 6 | [TERMINAL] | Tạo cron job digest 6:00 bằng `openclaw automations create` rồi `openclaw cron list` | 70s |
| 7 | [TERMINAL] | `openclaw cron run <id>` → điện thoại nhận tin → `cron runs --id <id> --limit 1` status ok | 35s |
| 8 | [DIAGRAM] | Systemd user service: crash → tự restart, mở máy → service sống lại | 35s |
| 9 | [TERMINAL] | Pairing: `openclaw pairing list telegram` + `approve` + block config `dmPolicy: "pairing"`, `requireMention: true` | 55s |
| 10 | [TERMINAL] | Điều tra job lỗi: `openclaw cron list` thấy `error (4x)` → đọc transcript → `config set ... codeMode false` → `cron run` → ok | 85s |
| 11 | [IDE] | `~/.openclaw/skills/dev-workflow/SKILL.md` theo workflow 6 bước; hỏi agent "theo đúng workflow trong skill" | 60s |
| 12 | [MONTAGE] | Tổng kết nhanh: Telegram + terminal + diagram, nhịp "chatbot biết nói, gateway biết làm" | 30s |
| 13 | [B-ROLL] | Outro bàn phím, đèn màn hình tắt dần | 15s |

**Tổng: 610 giây ≈ 10:10.** Che bot token, gateway token và chat ID khi quay; font terminal tối thiểu 18px, prompt tối giản.

### Code cốt lõi

```bash
# Cảnh 5 — gateway đang sống
systemctl --user status openclaw-gateway
ss -ltn | grep 18789
openclaw --version        # OpenClaw 2026.9.6 (eb377ac)
openclaw status
```

```bash
# Cảnh 6 — cron job digest 6 giờ sáng
openclaw automations create "0 6 * * *" \
  "Đọc tin công nghệ nổi bật trong 24 giờ qua, chọn 5 mục đáng đọc nhất cho developer Việt, mỗi mục 1 câu + link, gửi digest." \
  --name "Morning brief" \
  --channel telegram \
  --to "<TELEGRAM_CHAT_ID>"

openclaw cron list
openclaw cron run <jobId>
openclaw cron runs --id <jobId> --limit 1
```

```bash
# Cảnh 9 — khóa cửa
openclaw pairing list telegram
openclaw pairing approve telegram <CODE>
```

```json5
// ~/.openclaw/openclaw.json — mặc định an toàn của Telegram
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing",
      groups: { "*": { requireMention: true } },
    },
  },
}
```

```bash
# Cảnh 10 — điều tra job lỗi 4 lần
openclaw cron list                                   # Github Trending: error (4x)
openclaw sessions tail --session-key <jobSessionKey> --tail 40
openclaw config set 'agents.defaults.models["zai/glm-5.3"].codeMode' false
openclaw cron run <jobId>
openclaw cron runs --id <jobId> --limit 1            # → status ok
```

```markdown
<!-- ~/.openclaw/skills/dev-workflow/SKILL.md — cảnh 11 -->
---
name: dev-workflow
description: Follow the 6-step AI-driven development workflow for all coding tasks.
---
1. Clarify the goal and context.
2. Produce a plan.
3. Wait for human review.
4. Act only after approval.
5. Verify with git diff and tests.
6. Report evidence, not claims.
```

### Bước 0 — chuẩn bị trước khi quay

1. Máy quay phải có gateway đang chạy: `systemctl --user status openclaw-gateway` = active và `ss -ltn | grep 18789` = LISTEN. Máy mới thì `npm install -g openclaw@latest && openclaw onboard` (onboard cài sẵn systemd user service).
2. Bot Telegram tạo bằng @BotFather; nạp token bằng `openclaw channels add --channel telegram --token <bot-token>`.
3. Job lỗi để demo cảnh 10: dùng job thật đang `error (4x)` nếu còn; nếu đã fix, dựng lại bằng cách trỏ một job test sang model chưa nằm trong allowlist — quay xong trả config về như cũ.
4. Cách đọc: OpenClaw = "Ô-pần-Cờ-lao", systemd = "sít-têm-đi", 18789 = "một-tám-bảy-tám-chín", digest giữ nguyên.
5. File thật để quay: `~/.openclaw/openclaw.json` (config), `~/.openclaw/skills/` (skills), `~/.openclaw/state/openclaw.sqlite` (cron jobs + transcript).

---

## PART 3 — THUMBNAIL IMAGE PROMPTS

1. `A cinematic glowing gateway hub on a developer desk routing neon message streams from a phone and a laptop into one machine, dark room, cyan and green light trails, subject right, empty left space, 16:9, photorealistic, no text, no logos.`
2. `A dramatic 6 AM scene: a phone lighting up with an automated morning digest while the developer sleeps, city bokeh window, warm amber and neon green accents, 16:9, photorealistic, no text.`
3. `A cinematic split contrast: a floating chat bubble made of pure light versus a small server box with robotic hands typing on a mechanical keyboard, dark server room, purple rim lighting, 16:9, photorealistic, no text.`

---

## PART 4 — TITLES, SEO DESCRIPTION & KEYWORDS

### 4a. Titles

1. OpenClaw: Trợ lý AI chạy trên chính máy bạn — Bonus 17.5 | Lập trình là cuộc sống
2. AI Gateway là gì? Chatbot biết nói, Gateway biết làm — Bonus 17.5 | Lập trình là cuộc sống
3. Tự host trợ lý AI 24/7 nhắn Telegram — Bonus 17.5 | Lập trình là cuộc sống
4. AI tự chạy terminal, tự gửi digest mỗi sáng — Bonus 17.5 | Lập trình là cuộc sống
5. Từ ChatGPT sang AI Gateway: khác một chữ, khác cả hệ thống — Bonus 17.5 | Lập trình là cuộc sống

**Khuyên dùng:** Đăng Title 1. A/B test Title 2 cho người tò mò khái niệm gateway, Title 4 cho người muốn tự động hóa.

### 4b. SEO Description

```text
Trợ lý AI trong app chỉ biết nói. OpenClaw là gateway tự host: chạy shell, đọc file, nhớ ngữ cảnh và tự dậy lúc 6 giờ sáng gửi digest lên Telegram.

✅ Hiểu kiến trúc 3 lớp: channel – gateway – agent
✅ Chạy gateway như systemd service 24/7
✅ Tạo cron job trả kết quả về Telegram
✅ Khóa an toàn bằng pairing và allowlist
✅ Điều tra cron job lỗi bằng transcript thật
✅ Đóng gói workflow 6 bước thành skill cho agent

🔗 OpenClaw docs: https://docs.openclaw.ai
🔗 OpenClaw GitHub: https://github.com/openclaw/openclaw
🔗 Gateway architecture: https://docs.openclaw.ai/concepts/architecture.md

⏱ 0:00 Digest 6 giờ sáng
⏱ 0:35 Trợ lý biết nói nhưng không biết làm
⏱ 1:50 Bước ngoặt: gateway nằm trên máy bạn
⏱ 3:00 Bóc 3 lớp kiến trúc
⏱ 3:45 Gateway thật đang chạy
⏱ 4:55 Cron job đầu tiên
⏱ 5:30 Job chạy: điện thoại rung
⏱ 6:05 Chạy 24/7 bằng systemd
⏱ 7:00 Khóa cửa: pairing và allowlist
⏱ 8:25 Điều tra một job lỗi
⏱ 9:25 Đóng gói workflow thành skill
⏱ 9:55 Chatbot biết nói, gateway biết làm

#OpenClaw #AIAgent #AIGateway #Telegram #Automation #SelfHosting #NodeJS #LapTrinhLaCuocSong
```

### 4c. Keywords / Tags

```text
openclaw, ai gateway là gì, trợ lý ai tự host, ai agent telegram, openclaw cron job, ai tự chạy terminal, tự động hóa bằng ai, self hosted ai assistant, openclaw tiếng việt, chatbot vs agent, cron job telegram, lập trình là cuộc sống
```

---

## PART 5 — THUMBNAIL PACKAGE

### Option 1 — khuyên dùng
- `CHATBOT BIẾT NÓI` — WHITE
- `GATEWAY BIẾT LÀM` — NEON GREEN `#00FF41`
### Option 2
- `TRỢ LÝ AI` — WHITE
- `TRÊN MÁY BẠN` — NEON GREEN `#00FF41`
### Option 3
- `6 GIỜ SÁNG` — WHITE
- `TỰ THỨC DẬY` — RED `#FF3B30`

**Typography chung:** Canvas 1280×720, Anton và JetBrains Mono, chữ trái, hình phải, stroke 8px, glow 10px.
