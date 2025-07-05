from src.preprocessing import clean_text, tokenize_text

# Danh sách từ khóa nghi ngờ (có thể mở rộng)
SUSPICIOUS_KEYWORDS = [
    "select", "union", "drop", "insert", "script", "alert", "or 1=1", "--", "sleep(", "benchmark(", "<script>"
]

def is_malicious(text: str) -> bool:
    """
    Kiểm tra văn bản có khả năng chứa tấn công không.
    """
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in cleaned or keyword in tokens:
            return True
    return False
