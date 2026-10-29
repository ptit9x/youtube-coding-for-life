# Hướng dẫn sử dụng Diagram Assets — EP06

## Cách dùng

1. Mở file `.html` trong **Chrome**
2. Nhấn **F11** (fullscreen) hoặc **Cmd+Shift+F** (Mac)
3. Diagram **tự co/giãn fit màn hình** — hoạt động trên mọi kích thước (14" MacBook, external monitor...)
4. Đợi animation chạy xong (~3 giây)
5. **Screen record** bằng OBS hoặc QuickTime → dùng trực tiếp trong video
6. Hoặc **screenshot** (Cmd+Shift+4) → dùng làm overlay tĩnh
7. Output luôn giữ **tỉ lệ 16:9** bất kể kích thước cửa sổ

## Kỹ thuật auto-scale

Canvas cố định 1920×1080 (Full HD) nhưng tự scale bằng JS `transform: scale()`.
- Trên MacBook 14": scale ~0.55x → vừa viewport
- Trên external 27" 4K: scale ~1.0x → gần như 1:1
- Khi screen record fullscreen: output đúng 16:9, sắc nét

## Lưu ý

- Kích thước: **1920×1080** (Full HD) — khớp với video output
- Font: **JetBrains Mono** — cần cài trên máy để hiển thị đúng
  - Download: https://www.jetbrains.com/lp/mono/
  - Nếu chưa cài, browser sẽ fallback sang monospace mặc định
- Mỗi file có **CSS animation** — các element xuất hiện tuần tự
- Muốn chạy lại animation: **Cmd+Shift+R** (hard reload)

## Danh sách files

| File | Scene | Nội dung |
|---|---|---|
| `scene-03-three-layers.html` | 3 | Ba tầng context: AGENTS.md → Skill → MCP |
| `scene-06b-context-window.html` | 6b | Repo lớn vs context window, conditional reading |
| `scene-14b-convention-drift.html` | 14b | Convention drift: 10 conv không/có AGENTS.md |
| `scene-14c-prompt-repetition-tax.html` | 14c | 50 conversations × cùng instruction vs 1 file |
| `scene-16-mcp-usbc.html` | 16 | MCP = USB-C: Agent ↔ MCP ↔ servers |
| `scene-21b-three-takeaways.html` | 21b | Ba điều đáng nhớ: ≠README, Lost in Middle, Stale=Bug |

## Color scheme (khớp channel brand)

- Background: `#0a0a1a`
- Neon Green: `#00FF41`
- Cyan: `#00D4FF`
- Purple: `#BD93F9`
- Error Red: `#FF4444`
- Warning Yellow: `#FFCC00`

