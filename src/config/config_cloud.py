from .config_default import Config

class CloudConfig(Config):
    DEBUG = False
    CLOUD_PROVIDER = "AWS"  # Có thể thay "GCP" hoặc "Azure"
    LOG_LEVEL = "INFO"

    # Đường dẫn trên hệ thống cloud
    RAW_DATA_DIR = "/var/data/raw"
    PROCESSED_DATA_DIR = "/var/data/processed"
    LABELED_DATA_DIR = "/var/data/labeled"
    MODEL_DIR = "/var/models"

    ENABLE_AUTH = True  # Bắt buộc xác thực khi triển khai cloud

    # Có thể thêm thông tin kết nối Cloud hoặc Storage Bucket
    AWS_BUCKET_NAME = "my-vuln-detector-data"
