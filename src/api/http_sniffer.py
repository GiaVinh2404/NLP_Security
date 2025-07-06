from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from src.preprocessing import clean_text
from src.model.predict import predict_ai

# Load model và vectorizer (dự phòng nếu chưa có thì fallback trong predict_ai)
vectorizer_path = os.path.join("models", "vectorizer.pkl")
model_path = os.path.join("models", "vuln_detector.pkl")

vectorizer = joblib.load(vectorizer_path) if os.path.exists(vectorizer_path) else None
model = joblib.load(model_path) if os.path.exists(model_path) else None

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
    cleaned = clean_text(text)

    if vectorizer and model:
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
    else:
        prediction = predict_ai(text)  # fallback sang heuristic nếu chưa có model

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
        if not text:
            continue  # Bỏ dòng trống

        cleaned = clean_text(text)

        if vectorizer and model:
            X = vectorizer.transform([cleaned])
            prediction = model.predict(X)[0]
        else:
            prediction = predict_ai(text)

        results.append({
            "text": text,
            "malicious": bool(prediction)
        })

    return jsonify({"results": results})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
