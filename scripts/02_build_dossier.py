#!/usr/bin/env python3
"""
Pha A4 — Ghép transcript + OCR thành MỘT file text duy nhất cho mỗi video.

    python3 scripts/02_build_dossier.py            # tất cả
    python3 scripts/02_build_dossier.py b5 b7

Ra: 01_raw/<id>/dossier.md

Đây là file mà agent trong Antigravity sẽ đọc. Nó thay thế hoàn toàn việc
đưa video vào AI: lời giảng lấy từ transcript, chữ trên màn hình lấy từ OCR,
cả hai đều đã có timestamp nên vẫn truy được nguồn về video gốc.

Khử trùng lặp: slide đứng yên nhiều phút thì chỉ in màn hình 1 lần, các block
sau ghi "(màn hình không đổi)" — giảm mạnh số token mà không mất thông tin.
"""
import sys, re, difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = 30           # gộp thoại thành block 30 giây
SAME = 0.97          # >= mức này coi như màn hình không đổi (đặt cao = giữ nhiều chi tiết)
MAX_SHOTS = 2        # tối đa mấy trạng thái màn hình khác nhau in ra trong 1 block


def parse_srt(p: Path):
    """-> [(giây bắt đầu, text)]"""
    if not p.exists():
        return []
    out, blocks = [], re.split(r"\n\s*\n", p.read_text(encoding="utf-8", errors="replace"))
    for b in blocks:
        m = re.search(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->", b)
        if not m:
            continue
        sec = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
        text = " ".join(l.strip() for l in b.split("\n")[m.string[:m.start()].count("\n") + 1:]).strip()
        if text:
            out.append((sec, text))
    return out


def parse_ocr(p: Path):
    """-> [(giây, text)] từ file có các mốc '### mm:ss'"""
    if not p.exists():
        return []
    out, cur, buf = [], None, []
    for line in p.read_text(encoding="utf-8", errors="replace").split("\n"):
        m = re.match(r"^###\s+(\d+):(\d+)\s*$", line)
        if m:
            if cur is not None and buf:
                out.append((cur, "\n".join(buf).strip()))
            cur, buf = int(m[1]) * 60 + int(m[2]), []
        elif cur is not None:
            buf.append(line)
    if cur is not None and buf:
        out.append((cur, "\n".join(buf).strip()))
    return [(s, t) for s, t in out if t]


def mmss(s):
    return f"{int(s)//60:02d}:{int(s)%60:02d}"


def build(vid: str) -> bool:
    d = ROOT / "01_raw" / vid
    info = dict(
        l.split("=", 1) for l in (d / "info.txt").read_text().strip().split("\n") if "=" in l
    ) if (d / "info.txt").exists() else {}

    cues = parse_srt(d / "transcript.srt")
    shots = sorted(parse_ocr(d / "ocr_frames.txt") + parse_ocr(d / "ocr_scenes.txt"))
    if not cues and not shots:
        print(f"!! {vid}: chưa có transcript lẫn OCR — bỏ qua")
        return False

    dur = float(info.get("duration_sec", 0)) or (
        max([c[0] for c in cues] + [s[0] for s in shots], default=0) + BLOCK
    )

    L = [
        f"# DOSSIER — {vid}",
        "",
        f"- file gốc: `{info.get('file','?')}`",
        f"- thời lượng: {dur/60:.1f} phút",
        f"- nguồn: transcript tự động (Whisper) + OCR màn hình (Apple Vision), đều chạy offline",
        "",
        "> **Độ tin cậy — đọc trước khi dùng:**",
        "> `Nói:` là giọng giảng viên do máy nhận dạng, có thể sai thuật ngữ tiếng Anh.",
        "> `Màn hình:` là chữ OCR từ khung hình, có thể sai vài ký tự nhưng bố cục đúng.",
        "> Khi hai nguồn lệch nhau: **tin `Màn hình` cho tên class / thuộc tính / bảng / code**,",
        "> **tin `Nói` cho lời giải thích và quy trình**. Timestamp là của video gốc.",
        "",
        "---",
        "",
    ]

    ci = si = 0
    last_shot = ""
    for start in range(0, int(dur) + 1, BLOCK):
        end = start + BLOCK
        said = []
        while ci < len(cues) and cues[ci][0] < end:
            # Lưới an toàn: Whisper thỉnh thoảng vẫn lặp một câu vài lần liên tiếp.
            # Gộp lại thành một, tránh dossier phình ra vì rác.
            if not said or said[-1] != cues[ci][1]:
                said.append(cues[ci][1])
            ci += 1
        seen = []
        while si < len(shots) and shots[si][0] < end:
            seen.append(shots[si][1]); si += 1
        if not said and not seen:
            continue

        L.append(f"## [{mmss(start)}]")
        if said:
            L.append(f"**Nói:** {' '.join(said)}")
        if seen:
            fresh = []
            for t in seen:
                if difflib.SequenceMatcher(None, t, last_shot).ratio() >= SAME:
                    continue
                if any(difflib.SequenceMatcher(None, t, s).ratio() >= SAME for s in fresh):
                    continue
                fresh.append(t)
                last_shot = t
            # Nhiều trạng thái quá thì giữ đầu và cuối: đầu = lúc mới hiện,
            # cuối = lúc hoàn chỉnh nhất (sơ đồ vẽ xong, bảng điền xong).
            if len(fresh) > MAX_SHOTS:
                fresh = [fresh[0], fresh[-1]]
            if not fresh:
                L.append("**Màn hình:** (không đổi)")
            else:
                for t in fresh:
                    L += ["**Màn hình:**", "```", t, "```"]
        L.append("")

    out = d / "dossier.md"
    out.write_text("\n".join(L), encoding="utf-8")
    n = len(out.read_text(encoding="utf-8"))
    print(f"== {vid}: dossier.md — {n:,} ký tự (~{n//3.5:,.0f} token), "
          f"{len(cues)} câu thoại, {len(shots)} khung hình có chữ")
    return True


ids = sys.argv[1:] or sorted(p.name for p in (ROOT / "01_raw").iterdir() if p.is_dir())
ok = sum(build(v) for v in ids)
print(f"\nXong {ok}/{len(ids)} video.")
