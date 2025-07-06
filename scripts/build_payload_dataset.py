import pandas as pd
import os

payload_file = "datasets/payloads/sql_payloads.txt"
output_csv = "datasets/train_data_from_payloads.csv"

# Đọc payloads đã lưu
with open(payload_file, "r", encoding="utf-8") as f:
    payloads = [line.strip() for line in f if line.strip()]

print(f"[INFO] Số lượng payloads độc hại: {len(payloads)}")

# Sinh thêm dữ liệu lành tính (bạn có thể mở rộng sau)
benign_samples = [
    "GET /index.html HTTP/1.1",
    "POST /login HTTP/1.1",
    "username=admin&password=1234",
    "Welcome to our website",
    "This is a normal search request"
]

print(f"[INFO] Số lượng dữ liệu lành tính: {len(benign_samples)}")

# Ghép thành dataset
data = []

# Nhãn 1: Payload độc hại
for text in payloads:
    data.append({"text": text, "label": 1})

# Nhãn 0: Dữ liệu lành tính
for text in benign_samples:
    data.append({"text": text, "label": 0})

# Tạo DataFrame và lưu ra CSV
df = pd.DataFrame(data)
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"[INFO] Đã lưu dataset tại {output_csv} với {len(df)} dòng")
