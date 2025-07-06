from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

# Load model và vectorizer
vectorizer = joblib.load(os.path.join("models", "vectorizer.pkl"))
model = joblib.load(os.path.join("models", "vuln_detector.pkl"))

# Khởi tạo Flask App
app = Flask(__name__)
CORS(app)

# Route kiểm tra hoạt động
@app.route("/api/ping", methods=["GET"])
def ping():
    return jsonify({"message": "API is running!"})

# Route nhận input text, dự đoán tấn công
@app.route("/api/scan", methods=["POST"])
def scan():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON"}), 400

    text = data["text"]
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    result = {
        "input": text,
        "malicious": bool(prediction),
        "message": "Detected as Malicious" if prediction else "Detected as Benign"
    }
    return jsonify(result)

# Route nhận file text, quét từng dòng
@app.route("/api/scan-file", methods=["POST"])
def scan_file():
    if "file" not in request.files:
        return jsonify({"error": "Missing file parameter"}), 400

    file = request.files["file"]
    results = []

    for line in file:
        text = line.decode("utf-8").strip()
        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]
        results.append({
            "text": text,
            "malicious": bool(prediction)
        })

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
