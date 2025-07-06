import requests
import os

PAYLOAD_SOURCES = {
    "sql_injection": "https://raw.githubusercontent.com/payloadbox/sql-injection-payload-list/master/README.md",
    "xss": "https://raw.githubusercontent.com/payloadbox/xss-payload-list/refs/heads/master/README.md",
    "path_traversal": "https://raw.githubusercontent.com/nemesida-waf/waf-bypass/master/README.md",
}
OUTPUT_DIR = "datasets/payloads"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for name, url in PAYLOAD_SOURCES.items():
    print(f"[INFO] Fetching {name} payloads from {url}...")
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        payloads = [line.strip() for line in resp.text.splitlines() if line.strip()]
        print(f"[INFO] Fetched {len(payloads)} payloads for {name}")

        # Lưu ra file
        out_path = os.path.join(OUTPUT_DIR, f"{name}_payloads.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            for p in payloads:
                f.write(p + "\n")

        print(f"[INFO] Saved to {out_path}\n")
    except Exception as e:
        print(f"[ERROR] Failed to fetch {name}: {e}")

print("[INFO] Hoàn tất quá trình crawl payload.")
