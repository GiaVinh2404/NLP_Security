import os
import pandas as pd
import random

payload_dir = "datasets/payloads"
output_csv = "datasets/train_data_complex.csv"
os.makedirs("datasets", exist_ok=True)

# Đọc từng loại payload
def load_payloads(filename):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

sql_payloads = load_payloads(os.path.join(payload_dir, "sql_injection_payloads.txt"))
xss_payloads = load_payloads(os.path.join(payload_dir, "xss_payloads.txt"))
path_payloads = load_payloads(os.path.join(payload_dir, "path_traversal_payloads.txt"))

# Dữ liệu lành tính phong phú
benign_samples = [
    "GET /products?id=15&category=books HTTP/1.1",
    "POST /api/user/login email=abc@example.com&pass=123456",
    "search=Samsung Galaxy S21",
    "username=nguyenvana&phone=0909123456",
    "feedback=This site is awesome!",
    "GET /profile.php?user=guest",
    "page=index.html",
    "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",  # JWT giả lập
]

# Sinh dữ liệu phức tạp
data = []

# Payload ngụy trang
def obfuscate(payload):
    wrappers = [
        lambda x: f"user_input={x}&submit=Submit",
        lambda x: f"<div>{x}</div>",
        lambda x: f"q={x}&sort=asc",
        lambda x: f"comment=Nice product {x}",
        lambda x: f"email=test@example.com&msg={x}",
    ]
    return random.choice(wrappers)(payload)

# Sinh tấn công ngụy trang
for p in sql_payloads + xss_payloads + path_payloads:
    # 50% payload rõ ràng, 50% ngụy trang
    if random.random() < 0.5:
        data.append({"text": p, "label": 1})
    else:
        data.append({"text": obfuscate(p), "label": 1})

# Sinh nhiều dữ liệu lành tính lặp lại cho cân bằng
benign_samples *= (len(data) // len(benign_samples)) + 2
benign_samples = benign_samples[:len(data)]

for p in benign_samples:
    data.append({"text": p, "label": 0})

# Trộn dữ liệu
random.shuffle(data)

# Ghi ra file
df = pd.DataFrame(data)
df.to_csv(output_csv, index=False, encoding="utf-8")

print(f"[INFO] Đã sinh dataset phức tạp với {len(df)} dòng, lưu tại {output_csv}")
