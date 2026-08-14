#!/usr/bin/env bash
# Pha A3 — OCR chữ trên màn hình bằng Vision framework của macOS.
# Chạy local, KHÔNG tốn quota AI. Đây là chỗ lấy được class diagram,
# bảng test case, code trong IDE — những thứ nghe audio không có.
#
# Chạy: bash scripts/01c_ocr.sh          (tất cả)
#       bash scripts/01c_ocr.sh b5 b7
# Ra:   01_raw/<id>/ocr_frames.txt , 01_raw/<id>/ocr_scenes.txt

set -euo pipefail
cd "$(dirname "$0")/.."

BIN=scripts/bin/ocrframes
if [[ ! -x $BIN || scripts/ocr_frames.swift -nt $BIN ]]; then
  echo "Biên dịch $BIN…"
  mkdir -p scripts/bin
  swiftc -O -o "$BIN" scripts/ocr_frames.swift 2>/dev/null
fi

want=" $* "

for d in 01_raw/*/; do
  id=$(basename "$d")
  [[ $# -gt 0 && $want != *" $id "* ]] && continue

  # OCR phải dùng cùng FRAME_INTERVAL lúc cắt ảnh, nếu không timestamp sẽ lệch.
  fi_val=5
  [[ -f "$d/info.txt" ]] && fi_val=$(sed -n 's/^frame_interval=//p' "$d/info.txt" | head -1)
  [[ -z $fi_val ]] && fi_val=5
  export FRAME_INTERVAL="$fi_val"

  echo "== $id (FRAME_INTERVAL=${FRAME_INTERVAL}s)"
  for kind in frames scenes; do
    if compgen -G "$d$kind/*.jpg" >/dev/null; then
      "$BIN" "$d$kind"/*.jpg > "$d/ocr_$kind.txt"
      echo "   ocr_$kind.txt  $(wc -c < "$d/ocr_$kind.txt" | tr -d ' ') ký tự"
    fi
  done
done
