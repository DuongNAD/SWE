// OCR ảnh câu hỏi trắc nghiệm bằng Vision framework của macOS — offline, không tốn quota AI.
// Khác bản scripts/ocr_frames.swift ở hai chỗ: tiêu đề là TÊN FILE (không phải mốc thời gian
// video), và chỉ nhận tiếng Anh (đề thi SWE201c viết bằng tiếng Anh — bật thêm vi-VN làm
// language correction bẻ cong thuật ngữ, ví dụ "boundary" thành "bounday").
//
// Biên dịch: swiftc -O -o 06_swe201c_fe/scripts/bin/ocrde 06_swe201c_fe/scripts/ocr_de.swift
// Dùng:      ocrde anh/<de>/*.jpg > out/<de>.txt
//
// In ra dạng:
//   ### q1
//   <chữ đọc được, giữ thứ tự đọc trái->phải, trên->dưới>

import Foundation
import Vision
import ImageIO

func loadImage(_ path: String) -> CGImage? {
    guard let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: path) as CFURL, nil)
    else { return nil }
    return CGImageSourceCreateImageAtIndex(src, 0, nil)
}

/// Gom các dòng nhận diện được theo hàng ngang rồi sắp trái->phải, để phương án
/// A/B/C/D nằm cạnh nhau trên một dòng không bị xáo trộn thứ tự.
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
    FileHandle.standardError.write(Data("usage: ocrde <anh.jpg ...>\n".utf8))
    exit(2)
}

var out = ""
var okCount = 0
for path in paths {
    let stem = URL(fileURLWithPath: path).deletingPathExtension().lastPathComponent
    guard let img = loadImage(path) else {
        FileHandle.standardError.write(Data("!! không đọc được: \(path)\n".utf8)); continue
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["en-US"]
    req.usesLanguageCorrection = true
    req.minimumTextHeight = 0.006

    do {
        try VNImageRequestHandler(cgImage: img, options: [:]).perform([req])
    } catch {
        FileHandle.standardError.write(Data("!! OCR lỗi \(path): \(error)\n".utf8)); continue
    }
    let lines = readingOrder(req.results as? [VNRecognizedTextObservation] ?? [])
    // Ảnh không có chữ vẫn phải in tiêu đề, nếu không sẽ lệch số câu khi ghép lại.
    out += "### \(stem)\n" + lines.joined(separator: "\n") + "\n\n"
    if !lines.isEmpty { okCount += 1 }
}
FileHandle.standardError.write(Data("OCR xong: \(okCount)/\(paths.count) ảnh có chữ\n".utf8))
print(out, terminator: "")
