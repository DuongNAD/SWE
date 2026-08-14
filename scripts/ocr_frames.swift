// OCR ảnh bằng Vision framework của macOS — chạy hoàn toàn offline, KHÔNG tốn quota AI.
// Biên dịch: swiftc -O -o scripts/bin/ocrframes scripts/ocr_frames.swift
// Dùng:      scripts/bin/ocrframes 01_raw/b5/frames/*.jpg > 01_raw/b5/ocr_frames.txt
//
// In ra dạng:
//   ### 12:30
//   <chữ đọc được trên màn hình, giữ thứ tự đọc trái->phải, trên->dưới>
//
// Timestamp suy từ tên file: frames/NNNN.jpg -> (NNNN-1)*FRAME_INTERVAL giây.
// Với ảnh scene (sNNNN.jpg) thì đọc mốc thời gian từ scenes/times.txt nếu có.
// Đổi khoảng lấy mẫu bằng biến môi trường FRAME_INTERVAL (mặc định 5 giây).

import Foundation
import Vision
import ImageIO

func loadImage(_ path: String) -> CGImage? {
    guard let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: path) as CFURL, nil)
    else { return nil }
    return CGImageSourceCreateImageAtIndex(src, 0, nil)
}

func mmss(_ sec: Double) -> String {
    let s = Int(sec.rounded())
    return String(format: "%02d:%02d", s / 60, s % 60)
}

let FRAME_INTERVAL = Int(ProcessInfo.processInfo.environment["FRAME_INTERVAL"] ?? "") ?? 5

/// Timestamp cho ảnh frames/NNNN.jpg (1 ảnh / FRAME_INTERVAL giây) hoặc scenes/sNNNN.jpg.
func timestamp(for path: String) -> String {
    let url = URL(fileURLWithPath: path)
    let stem = url.deletingPathExtension().lastPathComponent
    let dir = url.deletingLastPathComponent()

    if stem.hasPrefix("s"), let idx = Int(stem.dropFirst()) {
        let timesFile = dir.appendingPathComponent("times.txt")
        if let raw = try? String(contentsOf: timesFile, encoding: .utf8) {
            let times = raw.split(separator: "\n").compactMap { line -> Double? in
                guard let r = line.range(of: "pts_time:") else { return nil }
                return Double(line[r.upperBound...].prefix { !$0.isWhitespace })
            }
            if idx - 1 < times.count { return mmss(times[idx - 1]) }
        }
        return "??:??"
    }
    if let n = Int(stem) { return mmss(Double((n - 1) * FRAME_INTERVAL)) }
    return "??:??"
}

/// Gom các dòng nhận diện được theo hàng ngang rồi sắp trái->phải,
/// để bảng test case / class diagram không bị xáo trộn thứ tự.
func readingOrder(_ obs: [VNRecognizedTextObservation]) -> [String] {
    let items = obs.compactMap { o -> (y: Double, x: Double, h: Double, s: String)? in
        guard let t = o.topCandidates(1).first?.string, !t.isEmpty else { return nil }
        let b = o.boundingBox
        return (y: Double(b.midY), x: Double(b.minX), h: Double(b.height), s: t)
    }
    guard !items.isEmpty else { return [] }

    let tol = max(items.map(\.h).reduce(0, +) / Double(items.count) * 0.6, 0.01)
    var rows: [[(y: Double, x: Double, h: Double, s: String)]] = []
    for it in items.sorted(by: { $0.y > $1.y }) {
        if var last = rows.last, let ref = last.first, abs(ref.y - it.y) <= tol {
            last.append(it); rows[rows.count - 1] = last
        } else {
            rows.append([it])
        }
    }
    return rows.map { $0.sorted { $0.x < $1.x }.map(\.s).joined(separator: "  ") }
}

let paths = Array(CommandLine.arguments.dropFirst())
guard !paths.isEmpty else {
    FileHandle.standardError.write(Data("usage: ocrframes <anh.jpg ...>\n".utf8))
    exit(2)
}

var out = ""
var okCount = 0
for path in paths {
    guard let img = loadImage(path) else {
        FileHandle.standardError.write(Data("!! không đọc được: \(path)\n".utf8)); continue
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["vi-VN", "en-US"]
    req.usesLanguageCorrection = true
    req.minimumTextHeight = 0.008           // bắt cả chữ nhỏ trong IDE

    do {
        try VNImageRequestHandler(cgImage: img, options: [:]).perform([req])
    } catch {
        FileHandle.standardError.write(Data("!! OCR lỗi \(path): \(error)\n".utf8)); continue
    }
    let lines = readingOrder(req.results as? [VNRecognizedTextObservation] ?? [])
    guard !lines.isEmpty else { continue }   // khung hình không có chữ thì bỏ qua
    out += "### \(timestamp(for: path))\n" + lines.joined(separator: "\n") + "\n\n"
    okCount += 1
}
FileHandle.standardError.write(Data("OCR xong: \(okCount)/\(paths.count) ảnh có chữ\n".utf8))
print(out, terminator: "")
