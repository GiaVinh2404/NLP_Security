from src.preprocessing import clean_text, tokenize_text, fit_vectorizer, transform_text

sample_data = [
    "SELECT * FROM users WHERE id = 1; -- SQL Injection",
    "<script>alert('XSS')</script>",
    "Normal login request: username=admin&password=123"
]

# Bước 1: Làm sạch
cleaned = [clean_text(text) for text in sample_data]
print("Cleaned:", cleaned)

# Bước 2: Tokenize
tokens = [tokenize_text(text) for text in cleaned]
print("Tokens:", tokens)

# Bước 3: Vector hoá TF-IDF
fit_vectorizer(cleaned)
vecs = [transform_text(text) for text in cleaned]
print("Vector shape:", [v.shape for v in vecs])
