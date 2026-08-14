#!/usr/bin/env python3
"""Sinh mẹo ghi nhớ tiếng Việt cho từng câu hỏi -> meo.json"""
import json, os, queue, threading, time, urllib.request

SP = os.path.dirname(os.path.abspath(__file__))
SRC = "/Users/duongnad/Documents/project/SWE/05_quiz/cau_hoi.json"
OUT = os.path.join(SP, "meo.json")
KEYS = [k for k in os.environ.get("GEMINI_API_KEYS", "").split(",") if k.strip()]
MODELS = ["gemini-2.5-flash", "gemini-3.1-flash-lite"]

PROMPT = """Bạn là gia sư luyện thi môn Software Engineering (SWE202c) cho sinh viên Việt Nam.

Dưới đây là một câu trắc nghiệm và đáp án đúng đã biết. Hãy viết MẸO GHI NHỚ ngắn gọn
bằng tiếng Việt, giúp sinh viên nhớ ra đáp án khi gặp lại câu này trong phòng thi.

Yêu cầu:
- "moc_nho": một móc nối 3-10 từ dạng "<từ khoá trong đề> → <từ khoá trong đáp án>".
  Đây là thứ sinh viên nhẩm lại trong đầu, phải cực ngắn và dễ đọc.
- "vi_sao": ĐÚNG MỘT câu giải thích vì sao đáp án đó đúng. Không lặp lại nguyên văn đề.
- "bay": phương án sai dễ bị chọn nhầm nhất, và một mệnh đề ngắn nói vì sao nó sai.
  Dạng "C sai vì ...". Để chuỗi rỗng nếu câu quá dễ, không có bẫy rõ ràng.

BẮT BUỘC viết tiếng Việt CÓ DẤU đầy đủ (không viết kiểu "khong dau"). Giữ nguyên thuật ngữ tiếng Anh (use case, boundary object,
cyclomatic complexity...). Không dùng markdown, không xuống dòng trong giá trị.

CÂU HỎI:
%s

CÁC PHƯƠNG ÁN:
%s

ĐÁP ÁN ĐÚNG: %s"""

SCHEMA = {"type": "object",
          "properties": {"moc_nho": {"type": "string"}, "vi_sao": {"type": "string"},
                         "bay": {"type": "string"}},
          "required": ["moc_nho", "vi_sao", "bay"]}

lock = threading.Lock()
ki = [0]


def next_key():
    with lock:
        k = KEYS[ki[0] % len(KEYS)]
        ki[0] += 1
        return k


def call(prompt, model, key):
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.7, "responseMimeType": "application/json",
                                 "responseSchema": SCHEMA, "maxOutputTokens": 2048,
                                 "thinkingConfig": {"thinkingBudget": 0}}}
    url = ("https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent?key=%s"
           % (model, key))
    req = urllib.request.Request(url, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.loads(r.read().decode())
    c = d["candidates"][0]
    if "parts" not in c.get("content", {}):
        raise RuntimeError("no parts / %s" % c.get("finishReason"))
    return json.loads(c["content"]["parts"][0]["text"])


qs = json.load(open(SRC))["cau_hoi"]
res = {}
if os.path.exists(OUT):
    res = json.load(open(OUT))          # chạy lại thì giữ phần đã có
todo = [q for q in qs if str(q["slide"]) not in res]
print("Cần sinh mẹo: %d/%d" % (len(todo), len(qs)), flush=True)

work = queue.Queue()
for q in todo:
    work.put(q)


def worker():
    while True:
        try:
            q = work.get_nowait()
        except queue.Empty:
            return
        opts = "\n".join("%s. %s" % (k, v) for k, v in sorted(q["opts"].items()))
        p = PROMPT % (q["q"], opts, ", ".join(q["ans"]))
        err = None
        for model in MODELS:
            for _try in range(4):
                try:
                    r = call(p, model, next_key())
                    with lock:
                        res[str(q["slide"])] = r
                    err = None
                    break
                except Exception as e:
                    err = "%s: %s" % (model, str(e)[:80])
                    time.sleep(6 * (_try + 1))
            if err is None:
                break
        with lock:
            n = len(res)
            if err:
                print("LỖI slide %d  %s" % (q["slide"], err), flush=True)
            elif n % 10 == 0:
                json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=2)
                print("  ...%d/%d (đã lưu)" % (n, len(qs)), flush=True)
        work.task_done()


ts = [threading.Thread(target=worker) for _ in range(3)]
for t in ts:
    t.start()
for t in ts:
    t.join()

json.dump(res, open(OUT, "w"), ensure_ascii=False, indent=2)
print("Xong: %d/%d câu có mẹo" % (len(res), len(qs)))
