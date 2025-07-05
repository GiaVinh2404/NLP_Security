import os

class Config:
    # General
    PROJECT_NAME = "Web Vulnerability Detection AI"
    VERSION = "1.0"
    DEBUG = False

    # Data paths
    RAW_DATA_DIR = os.path.join(os.getcwd(), "datasets", "raw")
    PROCESSED_DATA_DIR = os.path.join(os.getcwd(), "datasets", "processed")
    LABELED_DATA_DIR = os.path.join(os.getcwd(), "datasets", "labeled")
    MODEL_DIR = os.path.join(os.getcwd(), "models")

    # Model parameters
    MODEL_NAME = "nlp_vuln_detector"
    THRESHOLD = 0.7  # Ngưỡng cảnh báo lỗ hổng

    # Cloud parameters
    CLOUD_PROVIDER = "AWS"
    CLOUD_REGION = "ap-southeast-1"
    
    # Logging
    LOG_LEVEL = "INFO"

    # Visualization
    DASHBOARD_HOST = "0.0.0.0"
    DASHBOARD_PORT = 8501

    # Security
    ENABLE_AUTH = True
    API_KEY = os.getenv("API_KEY", "changeme")  # Nên để API_KEY trong .env

    # NLP Settings
    NLP_MODEL = "bert-base-uncased"
    REMOVE_STOPWORDS = True
    USE_LEMMATIZATION = True

