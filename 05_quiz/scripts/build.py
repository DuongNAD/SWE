#!/usr/bin/env python3
"""Sinh ngân hàng câu hỏi (Markdown) + trang luyện quiz (HTML) từ slides.json + meo.json."""
import json, os, re

import trang

SP = os.path.dirname(os.path.abspath(__file__))
DEST = trang.DEST
os.makedirs(DEST, exist_ok=True)

data = json.load(open(os.path.join(SP, "slides.json")))
MEO = {}
if os.path.exists(os.path.join(SP, "meo.json")):
    MEO = json.load(open(os.path.join(SP, "meo.json")))

quiz, noidung = [], []
for r in data:
    n = int(re.search(r"(\d+)", r["file"]).group(1))
    if r.get("loai") == "quiz" and r.get("cau_hoi"):
        opts = {k: v for k, v in (r.get("lua_chon") or {}).items() if v and v.strip()}
        ans = [a for a in (r.get("dap_an") or []) if a in opts]
        m = MEO.get(str(n), {})
        quiz.append({"slide": n, "q": r["cau_hoi"].strip(), "opts": opts, "ans": ans,
                     "hook": m.get("moc_nho", ""), "why": m.get("vi_sao", ""),
                     "trap": m.get("bay", "")})
    else:
        noidung.append({"slide": n, "text": (r.get("van_ban") or "").strip()})

quiz.sort(key=lambda x: x["slide"])
noidung.sort(key=lambda x: x["slide"])
co_meo = sum(1 for q in quiz if q["hook"])

# ---------- Markdown ----------
md = ["# Ngân hàng câu hỏi — Sever_1_SEMESTER_3-4_SWE202c", "",
      "Nguồn: Google Slides `1_MO0B88ZCLa7cV_bi8NmbwS-o9h-MiHuGnS9I2G5NwQ` (276 slide).",
      "Đáp án lấy từ khung ghi chú của từng slide. Mẹo ghi nhớ do Gemini soạn.", "",
      "| Chỉ số | Số lượng |", "|---|---|",
      "| Câu hỏi trắc nghiệm | %d |" % len(quiz),
      "| Câu nhiều đáp án | %d |" % sum(1 for q in quiz if len(q["ans"]) > 1),
      "| Câu có mẹo ghi nhớ | %d |" % co_meo,
      "| Slide nội dung (không phải câu hỏi) | %d |" % len(noidung), "", "---", ""]

for i, q in enumerate(quiz, 1):
    md.append("### Câu %d  <sub>(slide %d)</sub>" % (i, q["slide"]))
    md.append("")
    md.append(q["q"])
    md.append("")
    for k in sorted(q["opts"]):
        md.append("- **%s.** %s%s" % (k, q["opts"][k], " ✅" if k in q["ans"] else ""))
    md.append("")
    md.append("> **Đáp án: %s**" % ", ".join(q["ans"]))
    if q["hook"]:
        md.append(">")
        md.append("> 💡 **Móc nhớ:** %s" % q["hook"])
        if q["why"]:
            md.append("> · %s" % q["why"])
        if q["trap"]:
            md.append("> · ⚠️ %s" % q["trap"])
    md.append("")

if noidung:
    md += ["---", "", "## Slide nội dung (không phải câu hỏi)", ""]
    for s in noidung:
        md.append("**Slide %d** — %s" % (s["slide"], s["text"].replace("\n", " ")[:400] or "(trống)"))
        md.append("")

open(os.path.join(DEST, "NGAN_HANG_CAU_HOI.md"), "w").write("\n".join(md))

# ---------- HTML ----------
trang.viet("quiz.html", quiz, "Quiz SWE202c", "swe202c_quiz_v2",
           trang.thanh_dieu_huong(trang.chia_phan(len(quiz)), 0))

json.dump({"nguon": "Google Slides 1_MO0B88ZCLa7cV_bi8NmbwS-o9h-MiHuGnS9I2G5NwQ",
           "tong_slide": len(data), "cau_hoi": quiz, "slide_noi_dung": noidung},
          open(os.path.join(DEST, "cau_hoi.json"), "w"), ensure_ascii=False, indent=2)

print("Câu hỏi: %d | có mẹo: %d | nội dung: %d" % (len(quiz), co_meo, len(noidung)))
print("Chạy tiếp chia.py để sinh các trang phan_N.html")
