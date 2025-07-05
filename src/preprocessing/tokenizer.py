from nltk.tokenize import word_tokenize
import nltk

# Tải dữ liệu NLTK lần đầu nếu cần
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def tokenize_text(text: str) -> list:
    """
    Tách từ văn bản thành danh sách token
    """
    tokens = word_tokenize(text)
    return tokens
