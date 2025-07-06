import requests
import os

RAW_DIR = "datasets/payloads"
os.makedirs(RAW_DIR, exist_ok=True)

# Đường dẫn raw file trên GitHub
URL = "https://raw.githubusercontent.com/payloadbox/sql-injection-payload-list/master/README.md"

resp = requests.get(URL)
resp.raise_for_status()

lines = [l.strip() for l in resp.text.splitlines() if l.strip() and not l.startswith("#")]

out_file = os.path.join(RAW_DIR, "sql_payloads.txt")
with open(out_file, "w", encoding="utf-8") as f:
    for l in lines:
        f.write(l + "\n")

print(f"[INFO] Đã lưu {len(lines)} payloads vào {out_file}")
