#!/usr/bin/env python3
"""Máy thu ảnh chạy ở localhost.

Trang fuoverflow (đã đăng nhập trong khung Browser) fetch ảnh đính kèm rồi POST
base64 sang đây; server ghi thẳng ra đĩa. Làm vậy vì cookie phiên của XenForo là
HttpOnly — không bốc ra ngoài để curl được, mà đẩy cả nghìn ảnh qua kết quả tool
thì vỡ context.

Chạy: python3 scripts/recv.py [PORT]   (mặc định 8787)
"""
import base64, json, os, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "anh")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787


class H(BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        # /ping để trang kiểm tra server sống; /list?de=xxx để biết ảnh nào đã có
        if self.path.startswith("/list"):
            de = self.path.split("de=")[-1] if "de=" in self.path else ""
            d = os.path.join(ROOT, de)
            names = sorted(os.listdir(d)) if os.path.isdir(d) else []
            body = json.dumps(names).encode()
        else:
            body = b'"pong"'
        self.send_response(200)
        self._cors()
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        n = int(self.headers.get("content-length", 0))
        try:
            p = json.loads(self.rfile.read(n))
            de = os.path.basename(p["de"])
            ten = os.path.basename(p["ten"])
            d = os.path.join(ROOT, de)
            os.makedirs(d, exist_ok=True)
            raw = base64.b64decode(p["b64"])
            with open(os.path.join(d, ten), "wb") as f:
                f.write(raw)
            out = {"ok": True, "bytes": len(raw)}
        except Exception as e:  # trả lỗi về trang để vòng lặp JS biết mà thử lại
            out = {"ok": False, "loi": str(e)}
        body = json.dumps(out).encode()
        self.send_response(200)
        self._cors()
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    os.makedirs(ROOT, exist_ok=True)
    print(f"nhan anh vao {ROOT}, cong {PORT}", flush=True)
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
