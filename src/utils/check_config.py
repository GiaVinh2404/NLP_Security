from src.config import AppConfig

def show_config():
    print("=" * 30)
    print(f"PROJECT NAME : {AppConfig.PROJECT_NAME}")
    print(f"DEBUG MODE   : {AppConfig.DEBUG}")
    print(f"DATA DIR     : {AppConfig.RAW_DATA_DIR}")
    print(f"MODEL DIR    : {AppConfig.MODEL_DIR}")
    print(f"NLP MODEL    : {AppConfig.NLP_MODEL}")
    print(f"DASHBOARD    : {AppConfig.DASHBOARD_HOST}:{AppConfig.DASHBOARD_PORT}")
    print(f"CLOUD MODE   : {AppConfig.CLOUD_PROVIDER}")
    print(f"LOG LEVEL    : {AppConfig.LOG_LEVEL}")
    print("=" * 30)

if __name__ == "__main__":
    show_config()
