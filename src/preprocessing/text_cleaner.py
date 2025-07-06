import re

def clean_text(text: str) -> str:
    """
    Làm sạch văn bản đầu vào nhưng giữ lại ký tự đặc biệt quan trọng như: = & < > ' " ; ( )
    """
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    # Giữ lại các ký tự đặc biệt quan trọng
    text = re.sub(r'[^a-zA-Z0-9\s=<>\'\";()&]', '', text)
    return text.strip()
