#!/usr/bin/env python3
"""
Chấm tự động các bài làm trong kiểm thử hồi quy.
    python3 scripts/94_cham_hoi_quy.py

Với mỗi đề, đọc yêu cầu THẬT từ chính file đề (số lượng requirement mỗi đề một khác),
rồi kiểm bài làm tương ứng. Chỉ kiểm những thứ đếm/kiểm được máy móc — đúng số lượng,
đúng định dạng, đúng công thức. Không chấm nội dung hay dở.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OK, BAD, WARN = "✅", "❌", "⚠️"


# Ba kiểu đánh dấu câu mà model thực sự sinh ra:
#   ### Question 3      (de2)
#   **Question 3**      (de3)
#   3.                  (de1 — số trần trên một dòng)
#   ## 1. Kanban Model  (de2 sau khi chạy lại)
RE_AS_SYSTEM = re.compile(
    r"^\s*(?:[-*\u2022]\s*)?(?:\d+(?:\.\d+)*\s+)?[Aa]s a system\b", re.M)

MARKERS = [
    re.compile(r"^\s*(?:#{1,5}\s*)?(?:\*\*)?\s*(?:Question|Câu)\s*([1-6])\b", re.M | re.I),
    re.compile(r"^\s*#{1,5}\s*([1-6])\.\s+\S", re.M),
    re.compile(r"^\s*([1-6])\.\s*$", re.M),
]


def phan_bai(txt):
    """Cắt bài làm thành từng câu 1..6. Chịu được cả 3 kiểu đánh dấu,
    và 'BẢN NỘP' nằm trước hay sau phần bài làm đều được."""
    m = re.search(r"^#{1,3}\s*BẢN NỘP", txt, re.M)
    ung_vien = [txt]
    if m:
        # ưu tiên phần sau BẢN NỘP, nhưng chỉ khi nó thật sự chứa bài làm
        ung_vien = [txt[m.end():], txt]

    for body in ung_vien:
        for pat in MARKERS:
            marks = [(int(x.group(1)), x.start()) for x in pat.finditer(body)]
            # giữ chuỗi tăng dần 1..6 xuất hiện muộn nhất
            best, cur = [], []
            for num, pos in marks:
                if cur and num != cur[-1][0] + 1:
                    # >= : khi hoà, lấy chuỗi XUẤT HIỆN SAU. Bài làm thật luôn nằm
                    # sau bảng phân loại ở đầu file, mà bảng đó cũng đánh Câu 1..6.
                    if len(cur) >= len(best):
                        best = cur
                    cur = []
                cur.append((num, pos))
            if len(cur) >= len(best):
                best = cur
            if len(best) >= 5:
                parts = {}
                for i, (num, pos) in enumerate(best):
                    end = best[i + 1][1] if i + 1 < len(best) else len(body)
                    parts[num] = body[pos:end]
                return parts
    return {}


def yeu_cau_q3(de):
    m = re.search(r"5 functional requirements,\s*(\d+)\s*(\w+) requirements,?\s*and\s*(\d+)\s*(\w+)",
                  de, re.I)
    return (5, int(m[1]), m[2].lower(), int(m[3]), m[4].lower()) if m else (5, 3, "?", 2, "?")


def dem_muc(s):
    """Đếm dòng liệt kê có đánh số hoặc gạch đầu dòng."""
    return len([l for l in s.split("\n") if re.match(r"^\s*(?:[-*•]|\d+[.)]|FR\d|NFR\d)\s+\S", l)])


rows = []
for de_path in sorted((ROOT / "page/de_batch").glob("de*.txt")):
    name = de_path.stem
    bai = ROOT / f"page/out/batch_{name}.md"
    if not bai.exists():
        rows.append((name, "—", ["chưa có bài làm"]))
        continue
    de, txt = de_path.read_text(errors="replace"), bai.read_text(errors="replace")
    q = phan_bai(txt)
    n_fr, n_a, ten_a, n_b, ten_b = yeu_cau_q3(de)
    loi = []

    # Q1 — có chốt agree/disagree và có biện luận bám đề
    s = q.get(1, "")
    if not re.search(r"\bI (?:agree|disagree)", s, re.I):
        loi.append("Q1 không nói rõ agree/disagree")
    # Biện luận có thể diễn đạt nhiều kiểu, không chỉ 'because'.
    noi = len(re.findall(r"\b(?:because|since|matches?|fits?|aligns?|suits?|suitable|"
                         r"match with project|this is why|corresponds)\b", s, re.I))
    if noi < 3:
        loi.append(f"Q1 biện luận mỏng (chỉ {noi} chỗ nối đặc trưng với đề)")

    # Q2 — phải nêu RÕ cả white-box và black-box (lỗi đã sửa ở khuôn)
    s = q.get(2, "")
    if not re.search(r"white[- ]box", s, re.I) or not re.search(r"black[- ]box", s, re.I):
        loi.append("Q2 thiếu white-box hoặc black-box")
    if not re.search(r"unit", s, re.I) or not re.search(r"integration", s, re.I) \
       or not re.search(r"system testing", s, re.I):
        loi.append("Q2 thiếu cấp độ kiểm thử")
    if not re.search(r"developer", s, re.I) or not re.search(r"tester|QA", s, re.I):
        loi.append("Q2(b) thiếu người thực hiện")

    # Q3 — đúng số lượng theo chính đề này
    s = q.get(3, "")
    tong = dem_muc(s)
    can = n_fr + n_a + n_b
    if tong != can:
        loi.append(f"Q3 có {tong} mục, đề cần {can} ({n_fr}FR+{n_a}{ten_a}+{n_b}{ten_b})")
    for ten in (ten_a, ten_b):
        if ten != "?" and not re.search(ten[:6], s, re.I):
            loi.append(f"Q3 không thấy nhóm '{ten}'")

    # Q4 — đúng 5 story, đủ công thức, không có 'As a system'
    s = q.get(4, "")
    stories = re.findall(r"[Aa]s an? [^\n]*", s)
    if len(stories) != 5:
        loi.append(f"Q4 có {len(stories)} user story, cần đúng 5")
    thieu = [st for st in stories if "so that" not in st.lower()]
    if thieu:
        loi.append(f"Q4 có {len(thieu)} story thiếu 'so that'")
    if RE_AS_SYSTEM.search(s):
        loi.append("Q4 dùng 'As a system' (phải là vai trò con người)")

    # Q5 — đúng 2 pattern
    s = q.get(5, "")
    pats = set(re.findall(r"\b(Singleton|Observer|Factory|Strategy|Facade|Adapter|MVC|Decorator|Builder)\b",
                          s, re.I))
    if len(pats) != 2:
        loi.append(f"Q5 nhận diện {len(pats)} pattern ({', '.join(sorted(pats)) or 'không rõ'}), cần đúng 2")

    # Q6 — định dạng EOS và số hiệu story khớp task
    s = q.get(6, "")
    if not re.search(r"A\.\s*Activities", s, re.I):
        loi.append("Q6 thiếu phần A")
    if not re.search(r"B\.\s*Releases", s, re.I):
        loi.append("Q6 thiếu phần B")
    if len(re.findall(r"Release\s*\d", s, re.I)) < 2:
        loi.append("Q6 có dưới 2 Release")
    if RE_AS_SYSTEM.search(s):
        loi.append("Q6 dùng 'As a system'")
    tasks = set(re.findall(r"^\s*[-*•]?\s*(\d+\.\d+)\s", s, re.M))
    stories6 = set(re.findall(r"^\s*[-*•]?\s*(\d+\.\d+)\.\d+\s", s, re.M))
    lac = stories6 - tasks
    if tasks and lac:
        loi.append(f"Q6 story không khớp task: {', '.join(sorted(lac))}")

    rows.append((name, f"{n_a}{ten_a[:4]}+{n_b}{ten_b[:4]}", loi))

print(f"\n{'ĐỀ':<6} {'Q3 YÊU CẦU':<14} KẾT QUẢ")
print("─" * 78)
tong_loi = 0
for name, yc, loi in rows:
    tong_loi += len(loi)
    if not loi:
        print(f"{name:<6} {yc:<14} {OK} đạt toàn bộ")
    else:
        print(f"{name:<6} {yc:<14} {BAD} {len(loi)} lỗi")
        for l in loi:
            print(f"{'':<21}   • {l}")
print("─" * 78)
print(f"Tổng: {sum(1 for _,_,l in rows if not l)}/{len(rows)} đề đạt, {tong_loi} lỗi\n")
