# bot/utils/logger.py
import logging
import sys
from bot.config.settings import currentSettings as settings 


def setup_logger(name: str = __name__):
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            # <-- добавлено encoding='utf-8' для записи в файл
            logging.FileHandler(settings.LOG_FILE, encoding='utf-8'),
            # <-- явно указываем поток stdout, чтобы брать тот, который ты, возможно, уже переназначил
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(name)
