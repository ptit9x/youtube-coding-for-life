#!/usr/bin/env python3
"""Weekly YouTube channel report for "Lập trình là cuộc sống".

Scrapes public channel data (no API key needed), diffs against the
previous weekly snapshot, and prints a Vietnamese markdown report.
Designed to be run by a Hermes cron job every Sunday evening (Asia/Ho_Chi_Minh).

State: .channel-snapshots.json next to this file (gitignored), keeps up to
52 weekly snapshots. First run stores a baseline and says so.
Exit codes: 0 = report printed, 1 = scrape failure (message on stderr).
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timedelta, timezone

HANDLE = "laptrinhlacuocsong"
HERE = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(HERE, ".channel-snapshots.json")
TZ = timezone(timedelta(hours=7))  # Asia/Ho_Chi_Minh
UA = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
    "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8",
}


def fetch_initial_data(url: str) -> dict:
    req = urllib.request.Request(url, headers=UA)
    html = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", errors="replace")
    m = re.search(r"var ytInitialData = (.+?);\s*</script>", html) or re.search(
        r"ytInitialData\s*=\s*(.+?);\s*</script>", html
    )
    if not m:
        raise RuntimeError("ytInitialData not found — YouTube HTML may have changed")
    return json.loads(m.group(1))


def find_all(obj, key: str) -> list:
    out = []
    if isinstance(obj, dict):
        if key in obj:
            out.append(obj[key])
        for v in obj.values():
            out.extend(find_all(v, key))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(find_all(v, key))
    return out


def parse_views(txt: str):
    """'221 lượt xem' -> 221, '3,8 N lượt xem' -> 3800, '12K views' -> 12000."""
    t = txt.replace("lượt xem", "").replace("views", "").strip()
    m = re.match(r"([\d.,]+)\s*(N|Tr|K|M)?", t, re.IGNORECASE)
    if not m:
        return None
    num_s, unit = m.group(1), (m.group(2) or "").upper()
    if unit:
        num = float(num_s.replace(",", "."))
    else:
        num = float(num_s.replace(",", "").replace(".", ""))
    return int(num * {"N": 1e3, "TR": 1e6, "K": 1e3, "M": 1e6, "": 1}[unit])


def parse_count(txt: str):
    """'37 người đăng ký' -> 37, '7.556 lượt xem' -> 7556."""
    m = re.search(r"[\d.,]+", txt or "")
    if not m:
        return None
    try:
        return int(m.group().replace(".", "").replace(",", ""))
    except ValueError:
        return None


def parse_age_days(txt: str):
    """'2 tuần trước' -> 14, '3 ngày trước' -> 3."""
    m = re.search(r"(\d+)\s*(giây|phút|giờ|ngày|tuần|tháng|năm)", txt or "")
    if not m:
        return None
    n, unit = int(m.group(1)), m.group(2)
    factor = {
        "giây": 1 / 86400, "phút": 1 / 1440, "giờ": 1 / 24,
        "ngày": 1, "tuần": 7, "tháng": 30, "năm": 365,
    }[unit]
    return n * factor


def scrape_channel() -> dict:
    about = fetch_initial_data(f"https://www.youtube.com/@{HANDLE}/about")
    meta = {}
    for vm in find_all(about, "aboutChannelViewModel"):
        meta = {
            "subs_txt": vm.get("subscriberCountText", ""),
            "videos_txt": vm.get("videoCountText", ""),
            "views_txt": vm.get("viewCountText", ""),
        }
        break
    meta_num = {
        "subs": parse_count(meta.get("subs_txt", "")),
        "video_count": parse_count(meta.get("videos_txt", "")),
        "total_views": parse_count(meta.get("views_txt", "")),
    }
    if meta_num["subs"] is None:
        raise RuntimeError("could not parse subscriber count — about page layout changed?")

    vids_data = fetch_initial_data(f"https://www.youtube.com/@{HANDLE}/videos")
    videos = []
    for lockup in find_all(vids_data, "lockupViewModel"):
        try:
            md = lockup["metadata"]["lockupMetadataViewModel"]
            rows = md["metadata"]["contentMetadataViewModel"]["metadataRows"]
            parts = [p["text"]["content"] for r in rows for p in r.get("metadataParts", [])]
        except (KeyError, IndexError):
            continue
        views_txt = parts[0] if parts else ""
        pub_txt = parts[1] if len(parts) > 1 else ""
        videos.append({
            "title": md["title"].get("content", ""),
            "views": parse_views(views_txt),
            "views_txt": views_txt,
            "pub": pub_txt,
            "age_days": parse_age_days(pub_txt),
        })
    if not videos:
        raise RuntimeError("0 videos parsed from /videos tab — renderer changed?")
    return {
        "ts": datetime.now(TZ).isoformat(timespec="seconds"),
        "meta": {**meta, **meta_num},
        "videos": videos,
    }


def load_state() -> list:
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return []


def save_state(history: list) -> None:
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(history[-52:], f, ensure_ascii=False, indent=1)


def fmt_delta(now, prev, suffix=""):
    if now is None or prev is None:
        return ""
    d = now - prev
    sign = "+" if d >= 0 else ""
    return f" ({sign}{d}{suffix} so với tuần trước)"


def build_report(cur: dict, prev: dict | None) -> str:
    now = datetime.now(TZ)
    lines = []
    lines.append(f"📺 **Báo cáo tuần — Kênh Lập trình là cuộc sống** ({now:%d/%m/%Y})")
    lines.append("")

    m, pm = cur["meta"], (prev or {}).get("meta", {})
    subs_d = fmt_delta(m.get("subs"), pm.get("subs"))
    views_d = fmt_delta(m.get("total_views"), pm.get("total_views"), " views")
    lines.append("**Tổng quan**")
    lines.append(f"- Subscribers: **{m.get('subs', '?')}**{subs_d}")
    lines.append(f"- Tổng views: **{m.get('total_views', '?')}**{views_d}")
    lines.append(f"- Số video công khai: {m.get('video_count', '?')}")

    vids = cur["videos"]
    newest = min((v for v in vids if v["age_days"] is not None), key=lambda v: v["age_days"], default=None)
    if newest:
        gap = newest["age_days"]
        gap_txt = f"{gap:.0f} ngày" if gap >= 1 else "< 1 ngày"
        lines.append(f"- Video mới nhất: {gap_txt} trước — {newest['title'][:60]}")
        if gap > 10:
            lines.append(f"  ⚠️ Đã {gap:.0f} ngày chưa đăng video — cadence 1 video/tuần đang đứt!")

    if not prev:
        lines.append("")
        lines.append("ℹ️ Đây là lần chạy đầu (baseline) — từ tuần sau sẽ có so sánh tăng trưởng.")
        lines.append("")
        lines.append("**Video công khai gần nhất**")
        for v in vids[:8]:
            age = f"{v['age_days']:.0f} ngày" if v["age_days"] is not None else "?"
            lines.append(f"- {v['views_txt']} · {age} · {v['title'][:70]}")
        return "\n".join(lines)

    # --- diffs vs last week ---
    prev_by_title = {v["title"]: v for v in prev.get("videos", [])}
    cur_titles = {v["title"] for v in vids}

    new_videos = [v for v in vids if v["title"] not in prev_by_title]
    if new_videos:
        lines.append("")
        lines.append(f"**🆕 Video mới trong tuần ({len(new_videos)})**")
        for v in new_videos:
            lines.append(f"- {v['title'][:70]} — {v['views_txt']}")
    else:
        lines.append("")
        lines.append("🆕 Không có video mới trong tuần.")

    grew = []
    for v in vids:
        p = prev_by_title.get(v["title"])
        if p and v["views"] is not None and p["views"] is not None and v["views"] > p["views"]:
            grew.append((v["views"] - p["views"], v))
    grew.sort(reverse=True, key=lambda x: x[0])
    if grew:
        lines.append("")
        lines.append("**Tăng views tuần này**")
        for delta, v in grew[:6]:
            lines.append(f"- ▲{delta} → {v['views_txt']} · {v['title'][:65]}")

    subs = m.get("subs")
    if subs and subs > 0:
        fresh = [v for v in vids if v["age_days"] is not None and v["age_days"] <= 30 and v["views"]]
        if fresh:
            ratios = [v["views"] / subs for v in fresh]
            best = max(fresh, key=lambda v: v["views"])
            lines.append("")
            lines.append("**Signal phân phối**")
            lines.append(
                f"- Views/sub video <30 ngày: cao nhất {max(ratios):.1f}× "
                f"(>2× = thuật toán đang đẩy ra ngoài)"
            )
            lines.append(f"- Video hiệu quả nhất: {best['title'][:60]} ({best['views_txt']})")

    hist = load_state()
    if len(hist) >= 3:
        sub_hist = [h["meta"].get("subs") for h in hist[-5:] if h["meta"].get("subs") is not None]
        sub_hist.append(subs)
        if all(s is not None for s in sub_hist):
            lines.append("")
            lines.append(f"- Xu hướng subs 5 tuần: {' → '.join(str(s) for s in sub_hist)}")

    lines.append("")
    lines.append("Gợi ý: kiểm tra YouTube Studio (CTR + retention của video mới) để bổ sung số liệu riêng tư.")
    return "\n".join(lines)


def main() -> int:
    try:
        cur = scrape_channel()
    except Exception as e:
        print(f"LỖI scrape kênh @{HANDLE}: {e}", file=sys.stderr)
        return 1
    history = load_state()
    prev = history[-1] if history else None
    print(build_report(cur, prev))
    history.append(cur)
    save_state(history)
    return 0


if __name__ == "__main__":
    sys.exit(main())
