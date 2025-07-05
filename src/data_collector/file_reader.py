from src.model.predict import is_malicious

def process_log_file(file_path):
    """
    Đọc log file từng dòng, kiểm tra lỗ hổng
    """
    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            text = line.strip()
            if not text:
                continue

            if is_malicious(text):
                print(f"[ALERT] Line {i}: Possible attack detected!\n -> {text}\n")
            else:
                print(f"[OK] Line {i}: No threat found.")
