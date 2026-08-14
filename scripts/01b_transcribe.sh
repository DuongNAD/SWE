#!/usr/bin/env bash
# Pha A2 — Chuyển giọng nói thành chữ, CHẠY LOCAL, không tốn quota AI.
# Chạy: bash scripts/01b_transcribe.sh          (tất cả video)
#       bash scripts/01b_transcribe.sh b5 b7    (chỉ vài video)
#
# Ra: 01_raw/<id>/transcript.srt  (có timestamp)
#
# Cần cài 1 lần (chọn 1 trong 2):
#   pip3 install mlx-whisper          # khuyến nghị cho máy Apple Silicon, nhanh nhất
#   brew install whisper-cpp          # bản C++, cần tải model .bin thủ công
# Model dùng: large-v3-turbo — đủ tốt cho tiếng Việt lẫn thuật ngữ tiếng Anh.

set -euo pipefail
cd "$(dirname "$0")/.."

# large-v3 (không phải turbo): chậm hơn ~2 lần nhưng nghe tiếng Việt lẫn thuật ngữ
# tiếng Anh chính xác hơn rõ rệt. Chạy local nên chậm không tốn gì.
MODEL="${WHISPER_MODEL:-mlx-community/whisper-large-v3-mlx}"

# Mồi từ vựng: Whisper bám theo đoạn văn này để phiên âm đúng thuật ngữ.
# Không có nó, "class diagram" hay ra thành "cờ lát đai ơ gram".
PROMPT="${WHISPER_PROMPT:-Bài giảng môn Software Engineering SWE202c. Các thuật ngữ hay gặp: \
use case diagram, use case description, actor, precondition, postcondition, main flow, \
alternative flow, exception flow, class diagram, attribute, method, association, aggregation, \
composition, inheritance, multiplicity, sequence diagram, activity diagram, state diagram, \
entity, boundary, controller, requirement, functional requirement, non-functional requirement, \
test case, test data, expected result, boundary value analysis, equivalence partitioning, \
black box testing, white box testing, unit test, SRS, UML, extend, include, generalization.}"

if command -v mlx_whisper >/dev/null 2>&1; then ENGINE=mlx
elif command -v whisper-cli >/dev/null 2>&1; then ENGINE=cpp
else
  cat <<'EOF'
!! Chưa có công cụ nhận dạng giọng nói. Cài 1 trong 2 rồi chạy lại:

   pip3 install mlx-whisper
   brew install whisper-cpp

EOF
  exit 1
fi
echo "Dùng engine: $ENGINE  |  model: $MODEL"

want=" $* "

for d in 01_raw/*/; do
  id=$(basename "$d")
  [[ $# -gt 0 && $want != *" $id "* ]] && continue
  audio="01_raw/$id/audio.m4a"
  [[ -f "$audio" ]] || { echo "!! thiếu $audio — chạy scripts/01_prep_media.sh trước"; continue; }
  srt="01_raw/$id/transcript.srt"
  [[ -f "$srt" ]] && { echo "== $id: đã có transcript, bỏ qua"; continue; }

  echo "== $id: đang nhận dạng…"
  if [[ $ENGINE == mlx ]]; then
    # --condition-on-previous-text False là BẮT BUỘC, không phải tuỳ chọn.
    # Để mặc định (True), Whisper bám vào câu vừa nhận dạng để đoán câu tiếp theo,
    # và chỉ cần lặp một câu là nó khoá vào vòng lặp vô hạn. Đo trên b1-1:
    # bật -> 1099 đoạn chỉ có 88 nội dung khác nhau, "Được chưa anh em?" lặp 982 lần
    # từ phút 3:10 tới hết. Tắt -> 46 đoạn, chuỗi lặp dài nhất là 2. Cùng file audio.
    # Nếu báo không tải được model, đổi sang: WHISPER_MODEL=mlx-community/whisper-large-v3-turbo
    mlx_whisper "$audio" --model "$MODEL" --language vi \
      --initial-prompt "$PROMPT" \
      --condition-on-previous-text False \
      --output-format srt --output-dir "01_raw/$id" --output-name transcript
  else
    wav="01_raw/$id/audio.wav"
    [[ -f "$wav" ]] || ffmpeg -nostdin -v error -y -i "$audio" -ar 16000 -ac 1 "$wav"
    : "${WHISPER_CPP_MODEL:?Đặt WHISPER_CPP_MODEL=/đường/dẫn/ggml-large-v3.bin}"
    whisper-cli -m "$WHISPER_CPP_MODEL" -f "$wav" -l vi --prompt "$PROMPT" \
      -osrt -of "01_raw/$id/transcript"
    rm -f "$wav"
  fi
  echo "   -> $srt ($(wc -l < "$srt" | tr -d ' ') dòng)"
done
