import os
import pandas as pd
import random

payload_dir = "datasets/payloads"
output_csv = "datasets/train_data_large.csv"
os.makedirs("datasets", exist_ok=True)

# Đọc từng loại payload
def load_payloads(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

sql_payloads = load_payloads(os.path.join(payload_dir, "sql_injection_payloads.txt"))
xss_payloads = load_payloads(os.path.join(payload_dir, "xss_payloads.txt"))
path_payloads = load_payloads(os.path.join(payload_dir, "path_traversal_payloads.txt"))

# Dữ liệu lành tính mẫu (có thể bổ sung thêm sau)
benign_samples = [
    "GET /home HTTP/1.1",
    "username=guest&password=123",
    "search=iphone&category=electronics",
    "email=abc@example.com",
    "message=Hello, great product!",
    "order_id=42",
    "contact=hello@example.com",
]

# Sinh dữ liệu
data = []

for p in sql_payloads:
    data.append({"text": p, "label": 1})

for p in xss_payloads:
    data.append({"text": p, "label": 1})

for p in path_payloads:
    data.append({"text": p, "label": 1})

# Nhân bản dữ liệu lành tính cho cân bằng
benign_samples *= (len(data) // len(benign_samples)) + 1
benign_samples = benign_samples[:len(data)]  # Cắt cho bằng số lượng dữ liệu tấn công

for p in benign_samples:
    data.append({"text": p, "label": 0})

# Shuffle dữ liệu
random.shuffle(data)

# Ghi ra file
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"[INFO] Đã sinh dataset với {len(df)} dòng, lưu tại {output_csv}")
