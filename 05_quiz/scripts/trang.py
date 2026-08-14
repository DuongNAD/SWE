#!/usr/bin/env python3
"""Dựng trang quiz HTML từ quiz_tpl.html — dùng chung cho build.py (bản đủ) và chia.py (bản lẻ)."""
import datetime, json, os

SP = os.path.dirname(os.path.abspath(__file__))
DEST = "/Users/duongnad/Documents/project/SWE/05_quiz"
CO = 50  # mỗi phần 50 câu, phần cuối gộp luôn phần dư cho khỏi lẻ một nhúm


def chia_phan(tong, co=CO):
    """Cắt [1..tong] thành các đoạn `co` câu; đoạn cuối nuốt luôn phần dư.

    260 câu → 50/50/50/50/60. Trả về [(dau, cuoi)] đánh số từ 1, bao gồm cả hai đầu.
    """
    n = max(1, tong // co)
    doan = [(i * co + 1, (i + 1) * co) for i in range(n - 1)]
    doan.append(((n - 1) * co + 1, tong))
    return doan


def ten_file(i):
    return "phan_%d.html" % i


def thanh_dieu_huong(doan, hien_tai):
    """hien_tai: 0 = trang đủ, 1..n = phần thứ i."""
    li = ['<a href="quiz.html"%s>Tất cả</a>' % (' class="now"' if hien_tai == 0 else "")]
    for i, (a, b) in enumerate(doan, 1):
        li.append('<a href="%s"%s>Phần %d<small> · %d–%d</small></a>'
                  % (ten_file(i), ' class="now"' if hien_tai == i else "", i, a, b))
    return '<div class="parts">%s</div>' % "".join(li)


def viet(ten, quiz, tieu_de, khoa, nav):
    tpl = open(os.path.join(SP, "quiz_tpl.html")).read()
    page = (tpl.replace("__DATA__", json.dumps(quiz, ensure_ascii=False))
               .replace("__TITLE__", tieu_de)
               .replace("__KEY__", khoa)
               .replace("__NAV__", nav)
               .replace("__N__", str(len(quiz)))
               .replace("__BUILD__", datetime.datetime.now().strftime("%H:%M %d/%m")))
    open(os.path.join(DEST, ten), "w").write(page)
    return len(page)
