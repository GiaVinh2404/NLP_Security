from .config_default import Config

class LocalConfig(Config):
    DEBUG = True
    CLOUD_PROVIDER = "None"  # Không kết nối Cloud khi test local
    LOG_LEVEL = "DEBUG"

    # Thay đổi các giá trị phù hợp môi trường phát triển
    DASHBOARD_PORT = 8501
    ENABLE_AUTH = False
