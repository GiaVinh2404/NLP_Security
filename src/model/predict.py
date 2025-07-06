from src.preprocessing import clean_text, tokenize_text
import joblib
import os

# Đường dẫn model
MODEL_PATH = "models/vuln_detector.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

# Load model và vectorizer (nếu tồn tại)
model = None
vectorizer = None

if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    print("[WARN] Model hoặc vectorizer chưa được huấn luyện!")

# Danh sách từ khóa nghi ngờ (có thể mở rộng theo thực tế)
SUSPICIOUS_KEYWORDS = [
    "select", "union", "drop", "insert", "script", "alert", 
    "or 1=1", "--", "sleep(", "benchmark(", "<script>", 
    "' or '1'='1", "\" or \"1\"=\"1"
]

def is_malicious_heuristic(text: str) -> bool:
    """
    Kiểm tra nhanh dựa trên từ khóa nghi ngờ (rule-based).
    """
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in cleaned.lower() or keyword.lower() in tokens:
            return True
    return False


def predict_ai(text: str) -> bool:
    """
    Dự đoán sử dụng mô hình AI nếu có, fallback sang heuristic.
    """
    if model and vectorizer:
        cleaned = clean_text(text)
        X = vectorizer.transform([cleaned])
        prediction = model.predict(X)[0]
        return bool(prediction)
    else:
        print("[INFO] Đang fallback sang kiểm tra từ khóa.")
        return is_malicious_heuristic(text)
