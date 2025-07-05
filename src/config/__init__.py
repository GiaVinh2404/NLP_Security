import os
from dotenv import load_dotenv

# Load file .env (nếu có)
dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)

# Xác định môi trường hoạt động
ENVIRONMENT = os.getenv("ENVIRONMENT", "local").lower()

if ENVIRONMENT == "cloud":
    from .config_cloud import CloudConfig as AppConfig
else:
    from .config_local import LocalConfig as AppConfig
