#!/usr/bin/env python3
"""OCR từng ảnh slide bằng Gemini, xoay vòng API key, ghi ra slides.json."""
import base64, json, os, queue, threading, time, urllib.request, urllib.error

SP = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(SP, "slides")
OUT = os.path.join(SP, "slides.json")
MODEL = "gemini-3.5-flash-lite"

KEYS = [k for k in os.environ.get("GEMINI_API_KEYS", "").split(",") if k.strip()]

PROMPT = """Đây là ảnh chụp một slide trong Google Slides.
- Phần lớn phía trên là NỘI DUNG SLIDE.
- Dải chữ nhỏ ở sát ĐÁY ảnh (nền xám nhạt, tách biệt) là GHI CHÚ của người trình bày.
  Với slide câu hỏi trắc nghiệm, ghi chú này chính là ĐÁP ÁN, thường viết liền như "ABC", "B", "ABD".

Chép lại CHÍNH XÁC, không tóm tắt, không dịch, giữ nguyên ngôn ngữ gốc.
Bỏ qua watermark ("FORU", "Hoàng Hoàng Buôn Source", logo).

Trả về JSON đúng schema:
{
  "loai": "quiz" | "noi_dung",
  "cau_hoi": "đề bài, chuỗi rỗng nếu không phải quiz",
  "lua_chon": {"A": "...", "B": "...", "C": "...", "D": "...", "E": "..."},
  "dap_an": ["A","B"],
  "ghi_chu": "nguyên văn chữ trong khung ghi chú ở đáy ảnh, rỗng nếu trống",
  "van_ban": "toàn bộ text trên slide nếu không phải quiz, rỗng nếu là quiz"
}
Chỉ đưa vào "lua_chon" các phương án thực sự xuất hiện. "dap_an" lấy từ ghi chú; nếu ghi chú trống thì để []."""

SCHEMA = {
    "type": "object",
    "properties": {
        "loai": {"type": "string", "enum": ["quiz", "noi_dung"]},
        "cau_hoi": {"type": "string"},
        "lua_chon": {"type": "object", "properties": {k: {"type": "string"} for k in "ABCDEFGH"}},
        "dap_an": {"type": "array", "items": {"type": "string"}},
        "ghi_chu": {"type": "string"},
        "van_ban": {"type": "string"},
    },
    "required": ["loai", "cau_hoi", "lua_chon", "dap_an", "ghi_chu", "van_ban"],
}

lock = threading.Lock()
key_idx = [0]


def next_key():
    with lock:
        k = KEYS[key_idx[0] % len(KEYS)]
        key_idx[0] += 1
        return k


def call_gemini(img_b64, tries=6):
    body = {
        "contents": [{"parts": [
            {"text": PROMPT},
            {"inline_data": {"mime_type": "image/png", "data": img_b64}},
        ]}],
        "generationConfig": {
            "temperature": 0,
            "responseMimeType": "application/json",
            "responseSchema": SCHEMA,
        },
    }
    last = None
    for attempt in range(tries):
        key = next_key()
        url = ("https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent?key=%s"
               % (MODEL, key))
        req = urllib.request.Request(
            url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.loads(r.read().decode())
            txt = d["candidates"][0]["content"]["parts"][0]["text"]
            return json.loads(txt)
        except urllib.error.HTTPError as e:
            last = "HTTP %s %s" % (e.code, e.read().decode()[:200])
            time.sleep(1.5 * (attempt + 1))
        except Exception as e:
            last = str(e)[:200]
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(last)


files = sorted(f for f in os.listdir(IMG_DIR) if f.endswith(".png"))
results = {}
q = queue.Queue()
for f in files:
    q.put(f)


def worker():
    while True:
        try:
            f = q.get_nowait()
        except queue.Empty:
            return
        path = os.path.join(IMG_DIR, f)
        b64 = base64.b64encode(open(path, "rb").read()).decode()
        try:
            r = call_gemini(b64)
            r["file"] = f
            with lock:
                results[f] = r
                print("OK  %s  %s" % (f, (r.get("cau_hoi") or r.get("van_ban", ""))[:60]), flush=True)
        except Exception as e:
            with lock:
                results[f] = {"file": f, "loi": str(e)}
                print("LỖI %s  %s" % (f, e), flush=True)
        finally:
            q.task_done()


threads = [threading.Thread(target=worker) for _ in range(6)]
for t in threads:
    t.start()
for t in threads:
    t.join()

ordered = [results[f] for f in files]
json.dump(ordered, open(OUT, "w"), ensure_ascii=False, indent=2)
ok = sum(1 for r in ordered if "loi" not in r)
print("\nXong: %d/%d slide -> %s" % (ok, len(ordered), OUT))
