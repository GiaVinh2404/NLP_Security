import os
import pandas as pd
import random

# Thư mục chứa payload
payload_dir = "datasets/payloads"
output_csv = "datasets/train_data_complex.csv"
os.makedirs("datasets", exist_ok=True)

# Hàm đọc payload từ file
def load_payloads(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# Nạp dữ liệu từ file
sql_payloads = load_payloads(os.path.join(payload_dir, "sql_injection_payloads.txt"))
xss_payloads = load_payloads(os.path.join(payload_dir, "xss_payloads.txt"))
path_payloads = load_payloads(os.path.join(payload_dir, "path_traversal_payloads.txt"))

# Dữ liệu lành tính đa dạng
benign_samples = [
    "GET /products?id=15&category=books HTTP/1.1",
    "POST /api/user/login email=abc@example.com&pass=123456",
    "search=Samsung Galaxy S21",
    "username=nguyenvana&phone=0909123456",
    "feedback=This site is awesome!",
    "GET /profile.php?user=guest",
    "page=index.html",
    "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
    "Welcome to our platform",
    "Sign up to create your account",
    "Reset your password easily",
    "Profile updated successfully",
    "Contact support at support@example.com",
    "Thank you for using our service",
    "GET /api/status HTTP/1.1",
    "POST /register username=test&email=test@example.com",
    "<html><body>Safe content</body></html>",
]

# Hàm biến thể hóa payload để đánh lừa AI
wrappers = [
    lambda x: f"user_input={x}&submit=Submit",
    lambda x: f"<div>{x}</div>",
    lambda x: f"q={x}&sort=asc",
    lambda x: f"comment=Nice product {x}",
    lambda x: f"email=test@example.com&msg={x}",
    lambda x: f"<script>{x}</script>",
    lambda x: f"GET /api/search?keyword={x}",
]

def obfuscate(payload):
    return random.choice(wrappers)(payload)

# Tổng hợp dataset
data = []

# Thêm Payload độc hại rõ ràng và ngụy trang
for p in sql_payloads + xss_payloads + path_payloads:
    data.append({"text": p, "label": 1})  # Rõ ràng
    data.append({"text": obfuscate(p), "label": 1})  # Ngụy trang

# Cân bằng dữ liệu lành tính
benign_samples *= (len(data) // len(benign_samples)) + 2
benign_samples = benign_samples[:len(data)]

for p in benign_samples:
    data.append({"text": p, "label": 0})

# Trộn ngẫu nhiên
random.shuffle(data)

# Lưu ra file
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding="utf-8")

# Thống kê nhanh
print(f"[INFO] Đã sinh dataset với {len(df)} dòng, lưu tại {output_csv}")
print(df["label"].value_counts())

# Tuỳ chọn: Tách riêng để debug nếu cần
# df[df["label"] == 1].to_csv("datasets/malicious_samples.csv", index=False)
# df[df["label"] == 0].to_csv("datasets/benign_samples.csv", index=False)
