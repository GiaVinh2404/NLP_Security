from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from src.model.predict import is_malicious
from src.preprocessing import clean_text
from src.data_collector.file_reader import process_log_file

app = Flask(__name__)
CORS(app)  # Cho phép gọi từ frontend khác domain

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/api/scan", methods=["POST"])
def scan_text():
    """
    API kiểm tra lỗ hổng trên payload đơn lẻ
    """
    data = request.get_json()
    payload = data.get("payload", "")

    cleaned = clean_text(payload)
    malicious = is_malicious(payload)

    return jsonify({
        "original": payload,
        "cleaned": cleaned,
        "malicious": malicious
    }), 200


@app.route("/api/scan-file", methods=["POST"])
def scan_file():
    """
    API upload file log, quét từng dòng phát hiện lỗ hổng
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    save_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(save_path)

    results = []
    with open(save_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            text = line.strip()
            if not text:
                continue
            result = {
                "line": i,
                "content": text,
                "malicious": is_malicious(text)
            }
            results.append(result)

    return jsonify({"total_lines": len(results), "results": results}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
