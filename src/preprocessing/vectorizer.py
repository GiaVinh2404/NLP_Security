from sklearn.feature_extraction.text import TfidfVectorizer

# Khởi tạo TF-IDF toàn cục (dùng chung)
tfidf_vectorizer = TfidfVectorizer(max_features=500)

def fit_vectorizer(texts: list):
    """
    Huấn luyện vectorizer với tập dữ liệu ban đầu
    """
    tfidf_vectorizer.fit(texts)

def transform_text(text: str):
    """
    Chuyển văn bản sang vector đặc trưng
    """
    return tfidf_vectorizer.transform([text]).toarray()
