# bot\core\test_service.py
from bot.core.database_manager import DatabaseManager
from asyncio.log import logger


class TestService:
    """Тестовый сервис"""

    def __init__(
        self,
        db_manager: DatabaseManager,
        bot,
    ):
        self.db = db_manager
    
    async def initialize(self):
        """Запуск цикла обработки очереди."""
        logger.info(f"[TestService::initialize] started")
        state_start = self.db.get_service_status("test_service")
        if state_start:
           await self.start()
        logger.info(f"[TestService::initialize] completed successfully")

    async def start(self):
        """Запуск сервиса"""
        logger.info(f"[TestService::start] started")
        self.running = True
        logger.info(f"[TestService::start] completed successfully")

    async def stop(self):
        """Остановка сервиса"""
        logger.info(f"[TestService::stop] started")
        self.running = False
        logger.info(f"[TestService::stop] completed successfully")
