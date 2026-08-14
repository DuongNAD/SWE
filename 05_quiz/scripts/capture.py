#!/usr/bin/env python3
"""Quét toàn bộ slide trong Google Slides editor: chụp vùng canvas + khung ghi chú."""
import subprocess, hashlib, os, sys, time
from PIL import Image

SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SP, "slides")
os.makedirs(OUT, exist_ok=True)

WIN = "0,121,1470,835"          # bounds cửa sổ Chrome (points)
CROP = (470, 230, 2900, 1655)   # cắt bỏ filmstrip + thanh công cụ (pixels retina)
MAX_SLIDES = 300


def osa(script):
    return subprocess.run(["osascript", "-e", script], capture_output=True, text=True).stdout.strip()


def key(code, times=1, delay=0.45):
    osa('tell application "System Events"\nrepeat %d times\nkey code %d\ndelay %.2f\nend repeat\nend tell'
        % (times, code, delay))


def shot(path):
    raw = os.path.join(SP, "_raw.png")
    subprocess.run(["screencapture", "-x", "-R" + WIN, raw], check=True)
    im = Image.open(raw).convert("RGB").crop(CROP)
    im.thumbnail((1500, 1500))
    im.save(path)
    return hashlib.md5(im.tobytes()).hexdigest()


osa('tell application "Google Chrome" to activate')
time.sleep(1.0)
key(53)          # Esc: đóng hộp thoại đồng bộ nếu có
time.sleep(0.5)
key(126, 25, 0.18)   # Up x25: về slide đầu
time.sleep(1.5)

prev, same = None, 0
n = 0
for i in range(1, MAX_SLIDES + 1):
    p = os.path.join(OUT, "slide_%03d.png" % i)
    h = shot(p)
    if h == prev:
        same += 1
        os.remove(p)
        if same >= 2:
            print("Hết deck ở slide %d" % n, flush=True)
            break
    else:
        same = 0
        n = i
        print("slide %d -> %s" % (i, os.path.basename(p)), flush=True)
    prev = h
    key(125)     # Down: slide kế tiếp
    time.sleep(0.75)

print("TỔNG: %d slide" % n)
