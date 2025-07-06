import pandas as pd
import os

output_csv = "datasets/train_data_mixed.csv"
os.makedirs("datasets", exist_ok=True)

# Payload độc hại ngụy trang là traffic thật
malicious_samples = [
    "username=admin' OR '1'='1",
    "search=laptop' UNION SELECT * FROM users --",
    "email=test@example.com' OR '1'='1",
    "id=5; DROP TABLE users; --",
    "GET /product?id=5' AND '1'='1 HTTP/1.1",
    "message=Hi there!<script>alert('XSS')</script>",
    "' OR sleep(5)#",
]

# Dữ liệu hoàn toàn lành tính
benign_samples = [
    "username=guest&password=1234",
    "GET /index.html HTTP/1.1",
    "search=smartphone&category=electronics",
    "email=abc@example.com",
    "POST /api/contact message=Hello",
    "comment=Nice product, will buy again",
    "id=42",
    "search=order status",
    "Welcome to our website",
]

# Tạo dataset
data = []

for text in malicious_samples:
    data.append({"text": text, "label": 1})

for text in benign_samples:
    data.append({"text": text, "label": 0})

# Nhân bản dữ liệu để tăng số lượng
data *= 20  # Nhân lên 20 lần cho tập lớn hơn

# Tạo DataFrame và shuffle
df = pd.DataFrame(data).sample(frac=1, random_state=42).reset_index(drop=True)

# Lưu dataset
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"[INFO] Đã sinh dataset {len(df)} dòng và lưu tại {output_csv}")
