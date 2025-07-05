import re

def clean_text(text: str) -> str:
    """
    Làm sạch văn bản đầu vào: loại bỏ ký tự đặc biệt, khoảng trắng thừa, chuyển thường.
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # Loại bỏ khoảng trắng thừa
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Giữ lại chữ cái, số, khoảng trắng
    return text.strip()
