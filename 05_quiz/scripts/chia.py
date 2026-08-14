#!/usr/bin/env python3
"""Chia quiz thành nhiều trang nhỏ: phan_1.html … phan_N.html (mỗi phần 50 câu, phần cuối 60).

Mỗi phần có khoá localStorage riêng nên tiến độ không đè lên nhau, và không đè lên
trang đủ 260 câu (`quiz.html`) — làm phần nào tính điểm phần đó.
Chạy sau build.py; nguồn dữ liệu là cau_hoi.json.
"""
import json, os

import trang

quiz = json.load(open(os.path.join(trang.DEST, "cau_hoi.json")))["cau_hoi"]
doan = trang.chia_phan(len(quiz))

for i, (a, b) in enumerate(doan, 1):
    phan = quiz[a - 1:b]
    trang.viet(trang.ten_file(i), phan,
               "Quiz SWE202c — Phần %d/%d" % (i, len(doan)),
               "swe202c_quiz_v2_p%d" % i,
               trang.thanh_dieu_huong(doan, i))
    print("phan_%d.html — câu %d–%d (%d câu)" % (i, a, b, len(phan)))

print("Tổng: %d câu / %d phần" % (len(quiz), len(doan)))
