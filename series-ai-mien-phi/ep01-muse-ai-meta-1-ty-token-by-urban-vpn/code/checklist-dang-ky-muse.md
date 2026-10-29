# EP01 — Checklist Đăng Ký Muse (Meta) & Fact-Sheet Xác Minh

> Companion của script EP01. **Verify lại mọi con số trong bảng này ngay trước
> khi quay** (trong app/web Muse + trang dev chính thức của Meta). Số liệu AI
> thay đổi từng tháng — ngày xác minh gần nhất: **7/10/2026**.

## A. Checklist quay video (theo thứ tự narration)

### Phần 1 — Hook mở bài (2 câu, vào walkthrough NGAY)
- [ ] Flash headline "1 tỷ token" + 2 badge đỏ: "VN CHƯA MỜ?" / "Ô MÃ BÍ ẨN?"
- [ ] Diagram referral (đặt SAU walkthrough): ô nhập "MÃ LỜI MỜI" + 2 avatar
      (+1 tỷ mỗi bên) + đồng hồ cát 48h

### Phần 2 — Đăng ký Muse (consumer app) — CẦN VPN
> Muse **chưa hỗ trợ Việt Nam**: phải qua UrbanVPN server Mỹ mới tạo được
> tài khoản (đã test 7/10/2026).

- [ ] Cài **UrbanVPN** (extension Chrome hoặc app iOS/Android) — miễn phí
- [ ] Bật server **Mỹ** → kiểm tra IP đã sang Mỹ (vào `ipinfo.io`)
- [ ] Vào `muse.ai` trên **trình duyệt** — đường dễ nhất khi dùng VPN
      (app store VN có thể chưa hiện app Muse)
- [ ] Đăng nhập bằng tài khoản Meta (Facebook hoặc Instagram) — dùng
      **account demo THẬT** (không dùng acc ảo / acc mua)
- [ ] Xác nhận đủ 18 tuổi, tài khoản hoạt động tốt
- [ ] Nếu gặp bước **xác minh thẻ Visa** (trừ 1 USD, hoàn sau ~5–7 ngày):
      quay cảnh này nhưng **blur toàn bộ số thẻ**
- [ ] Chụp màn hình **hạn mức token hiển thị trong phần tài khoản** — đối chiếu
      với bảng B bên dưới trước khi đọc narration
- [ ] Quay xong cảnh đăng ký → **tắt VPN**; mờ IP + tên server khi xuất bản

### Phần 3 — Nhận 1 tỷ token (mã lời mời) — ĐÃ XÁC NHẬN
- [ ] Icon 2 gạch ngang góc dưới → **Cài đặt** → tài khoản mới đang ở
      **gói miễn phí**
- [ ] Bấm **Quy đổi mã lời mời** → nhập mã (blur nửa mã khi xuất bản) → chụp
      **hạn mức nhảy lên 1 tỷ**
- [ ] **Mã hết hạn 48h** → làm mới mã ở description/pin comment TRƯỚC khi
      xuất bản + định kỳ sau đó (mã trong video có thể đã chết)
- [ ] Muốn có mã riêng: cài **app Muse trên điện thoại** — mục **Invite**
      chỉ hiện ở bản mobile, web không có
- [ ] App **chưa có trên App Store VN** → phải **chuyển vùng App Store sang Mỹ**
      (để link hướng dẫn ở description:
      `https://cellphones.com.vn/sforum/chuyen-vung-appstore-sang-my`);
      Android: verify lại tương tự trên Google Play trước khi nói trong video

### Phần 4 — Muse Code (dev)
- [ ] Tra docs chính thức Meta cho lệnh cài Muse Code beta mới nhất
      (lệnh có thể đã đổi so với thời gian xác minh)
- [ ] Quay: agent chia task → subagents chạy song song trong git worktree
- [ ] Quay: `muse resume` khôi phục session sau Ctrl+C
- [ ] Chụp trang pricing Meta Model API: 2 tier + bảng giá (đối chiếu bảng B)

## B. Fact-sheet đã xác minh (7/10/2026)

### Muse — app consumer
| Mục | Giá trị | Ghi chú |
|---|---|---|
| Ra mắt | 8/9/2026 (Connect 2026) | Lùi từ tháng 4 vì lý do an toàn |
| Nền tảng | iOS, Android, web `muse.ai`, WhatsApp | Tích hợp Instagram/Messenger đang mở rộng |
| Region mở | Mỹ trước | **VN chưa hỗ trợ** — đăng ký web qua UrbanVPN server Mỹ (đã test 7/10/2026) |
| Độ tuổi | 18+ | Đăng nhập bằng tài khoản Meta (FB/IG) |
| Xác minh thẻ | Có thể yêu cầu thẻ Visa khi đăng ký — giữ 1 USD, hoàn sau ~5–7 ngày | Mức xác minh, không phải phí — verify lại trước khi quay |
| Miễn phí | ~100 triệu token/tuần | Mọi tính năng; chỉ giới hạn lượng dùng |
| 1 tỷ token | Qua **mã lời mời**: cả người mời lẫn người được mời được +1 tỷ | Mã hết hạn 48h — xác nhận 7/10/2026 |
| Mã riêng (Invite) | Chỉ hiện trong **app Mobile** | Web không có mục này |
| Power | 20 USD/tháng → ~500 triệu token/tuần | |
| Maximum | 100 USD/tháng → ~3 tỷ token/tuần | |
| Model kiếm tiền | Phí nhỏ trên giao dịch Muse làm hộ (L word của Zuck) | "Free for a huge number of tokens" |
| Muse for Mac | Ra 17/9/2026, Mỹ | |
| Muse Spark 1.3 | 2/9/2026, tiết kiệm ~25% token so 1.2 | Số Meta tự công bố |

### Cảm nhận host sau khi dùng thật (7/10/2026)
- Giao diện đơn giản; response **chậm** hơn các AI khác (ChatGPT, Gemini...)
- Muse **tự reaction** tin nhắn của người dùng — điểm khác lạ so với LLM khác

### Muse Code — dev CLI (beta)
| Mục | Giá trị |
|---|---|
| Model | Muse Spark 1.2, context 1 triệu token |
| Tier free | `muse-spark-1.2-contributor` — free, rate limit theo cửa sổ 5 giờ cuộn; Meta dùng dữ liệu để cải thiện sản phẩm |
| Tier chuẩn | $0.15/M cached input · $1.25/M input · $4.25/M output (~1/4 OpenAI/Anthropic) |
| Tính năng | Subagent song song trong git worktree riêng · JSONL event log · `muse resume` · skills `/plan`, `/taste`, `/grilling`, `/grill-with-docs` |
| Phân phối | Muse Code + Meta Model API (public preview toàn cầu) + OpenRouter |
| Riêng tư | Zero-data-retention theo yêu cầu |

### Prompt tham gia Early Access Program (verify còn hiệu lực)
Gõ trực tiếp cho Muse trong app:
```
Sign me up for early access to new Muse features.
```
→ Muse hỏi thêm vài câu (mục đích sử dụng, thiết bị) → vào waitlist.

## C. Cảnh báo an toàn (nói trong video — nguyên tắc series)

1. **VPN OK — acc ảo KHÔNG**: dùng UrbanVPN (server Mỹ) để đi qua region, nhưng
   luôn đăng nhập bằng tài khoản Meta THẬT. Acc ảo bị chặn = mất ưu đãi + dữ liệu.
2. **Contributor tier = đổi dữ liệu lấy miễn phí**: nếu code nhạy cảm (dự án
   công ty) → dùng tier chuẩn hoặc yêu cầu zero-data-retention.
3. **Kết nối Gmail/Calendar/tài khoản ngân hàng vào agent**: chỉ kết nối tối
   thiểu những gì cần; kiểm tra Sentinel log định kỳ trong app.
4. **Hạn mức tính theo tuần** nhưng vẫn hữu hạn: agent đọc nhiều — đừng giao
   việc "quét cả inbox" khi chưa quen.
5. **VPN miễn phí = IP dùng chung, traffic qua bên thứ ba**: chỉ bật khi dùng
   Muse; **tắt VPN** khi login ngân hàng, email công ty, GitHub.

## D. Nguồn xác minh (7/10/2026)

- pulse2.com — "Meta Launches Muse Spark 1.2 And Muse Code Coding Agent..."
- quantrimang.com/meta-muse-ai-la-gi-217293 — tổng quan Muse, giá, region
- androguider.com — "Meta Launches Early Access Program for New Muse Features"
- techcrunch / engadget / CNBC — Muse Code launch coverage
- Google News + Bing News RSS — tra cứu headline "1 tỷ token" báo VI
