import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# Cấu hình đường dẫn
DATA_PATH = os.path.join("datasets", "train_data_complex.csv")
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Đọc dữ liệu
print(f"[INFO] Đọc dữ liệu từ {DATA_PATH}")
data = pd.read_csv(DATA_PATH)
print(f"[INFO] Dataset: {data.shape[0]} dòng")

# Tách dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    data["text"], data["label"], test_size=0.2, random_state=42, stratify=data["label"]
)

# Vector hóa văn bản
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Huấn luyện mô hình Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Đánh giá mô hình
y_pred = model.predict(X_test_vec)
print("[INFO] Kết quả đánh giá:")
print(classification_report(y_test, y_pred, digits=4))

# Lưu model và vectorizer
model_path = os.path.join(MODEL_DIR, "vuln_detector.pkl")
vectorizer_path = os.path.join(MODEL_DIR, "vectorizer.pkl")

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)

print(f"[INFO] Đã lưu model tại {model_path}")
print(f"[INFO] Đã lưu vectorizer tại {vectorizer_path}")
