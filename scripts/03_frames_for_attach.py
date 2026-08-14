#!/usr/bin/env python3
"""
Chọn ảnh sơ đồ để đính kèm cho agent xem trực tiếp.

    python3 scripts/03_frames_for_attach.py b5
    python3 scripts/03_frames_for_attach.py ucd1 --max 60

Ra: 01_raw/<id>/attach/  — ảnh đã đổi tên thành mốc thời gian, ví dụ `12m30s.jpg`

Vì sao cần: OCR trả về CHỮ trong sơ đồ nhưng mất CẤU TRÚC — không biết class nào
nối class nào, mũi tên hướng nào, multiplicity 1..* nằm ở đầu nào. Với Q5 Class
Diagram và Use case diagram thì phần mất đó mới là phần được chấm điểm.
Cách chữa: đính kèm chính khung hình cho agent nhìn.

Chọn lọc thế nào: lấy các khung hình chuyển cảnh (màn hình đổi hẳn), ưu tiên khung
có nhiều mẩu chữ ngắn rải rác — đặc trưng của sơ đồ hộp-và-mũi-tên, khác hẳn slide
chữ chạy dài. Bỏ khung gần trùng nhau.
"""
import sys, re, shutil, argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("id")
ap.add_argument("--max", type=int, default=40, help="số ảnh tối đa (mặc định 40)")
ap.add_argument("--all", action="store_true", help="lấy hết khung chuyển cảnh, không lọc")
a = ap.parse_args()

d = ROOT / "01_raw" / a.id
scenes, times_file = d / "scenes", d / "scenes" / "times.txt"
if not scenes.is_dir():
    sys.exit(f"!! chưa có {scenes} — chạy scripts/01_prep_media.sh trước")

times = []
if times_file.exists():
    for line in times_file.read_text(errors="replace").split("\n"):
        m = re.search(r"pts_time:([\d.]+)", line)
        if m:
            times.append(float(m[1]))

# điểm "giống sơ đồ" của từng khung, đọc từ ocr_scenes.txt
score = {}
ocr = d / "ocr_scenes.txt"
if ocr.exists():
    cur = None
    for line in ocr.read_text(errors="replace").split("\n"):
        m = re.match(r"^###\s+(\d+):(\d+)", line)
        if m:
            cur = int(m[1]) * 60 + int(m[2])
            score[cur] = [0, 0]
        elif cur is not None and line.strip():
            score[cur][0] += 1                     # số dòng
            score[cur][1] += len(line.strip())     # tổng ký tự

imgs = sorted(scenes.glob("s*.jpg"))
picked = []
for i, p in enumerate(imgs):
    t = times[i] if i < len(times) else None
    if t is None:
        continue
    lines, chars = score.get(int(t), [0, 0])
    avg = chars / lines if lines else 0
    # sơ đồ: nhiều dòng, mỗi dòng ngắn. slide chữ: ít dòng, mỗi dòng dài.
    diagramish = lines >= 5 and avg <= 40
    picked.append((t, p, diagramish, lines))

if not a.all:
    only = [x for x in picked if x[2]]
    if len(only) >= 5:
        picked = only

picked.sort(key=lambda x: -x[3])          # nhiều chữ trước
picked = sorted(picked[: a.max], key=lambda x: x[0])

out = d / "attach"
if out.exists():
    shutil.rmtree(out)
out.mkdir(parents=True)
for t, p, _, _ in picked:
    shutil.copy(p, out / f"{int(t)//60:02d}m{int(t)%60:02d}s.jpg")

print(f"== {a.id}: chọn {len(picked)}/{len(imgs)} khung hình -> {out}")
print("   Kéo cả thư mục này vào ô chat của Antigravity, rồi chạy prompts/P1b_doc_so_do.md")
