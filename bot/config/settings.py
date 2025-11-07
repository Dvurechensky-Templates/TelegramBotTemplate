# config/settings.py
import os
from dotenv import load_dotenv
from asyncio.log import logger

# Загружаем .env
load_dotenv()

class Settings:
    """Глобальные настройки проекта"""
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    API_ID: int = int(os.getenv("API_ID", "0"))
    API_HASH: str = os.getenv("API_HASH", "")
    API_URL: str = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN', '')}"
    ADMIN_USERNAMES = ['dvurechensky_pro']

    LOG_FILE: str = os.getenv("LOG_FILE", "app.log")

    @property
    def is_valid(self) -> bool:
        """Проверка, что все ключи заполнены"""
        logger.info(f"[Settings::is_valid] started")
        logger.info(f"[DatabaseManager::init_database] completed successfully | BOT_TOKEN::{self.BOT_TOKEN} | API_ID::{self.API_ID} | API_HASH::{self.API_HASH}")
        return all([self.BOT_TOKEN, self.API_ID, self.API_HASH])

# Создаём единый экземпляр
currentSettings = Settings()
