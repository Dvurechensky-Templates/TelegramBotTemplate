# bot/core/service_manager.py
from asyncio.log import logger
from bot.core.database_manager import DatabaseManager
from bot.core import TestService


class ServiceManager:
    """Менеджер сервисов и функций"""
    def __init__(self, db_manager: DatabaseManager, bot):
        self.db = db_manager
        self.bot = bot
        self.active_services = {}  # Для хранения активных задач сервисов
        self.test_service = TestService(self.db, self.bot)

    async def initialize(self):
        """Инициализация менеджера управления сервисами"""
        logger.info(f"[ServiceManager::initialize] started")
        await self.test_service.initialize()
        logger.info(f"[ServiceManager::initialize] completed successfully")

    async def start_service(self, service_name: str):
        """Запуск сервисов по имени"""
        logger.info(f"[ServiceManager::start_service] started | {service_name}")
        try:
            match service_name:
                case "test_service":
                    await self.test_service.start()
                case _:
                    logger.error(f"[ServiceManager::start_service] Unknown service: {service_name}")
                    return False
            
            logger.info(f"[ServiceManager::start_service] Service {service_name} started")
            return True
            
        except Exception as e:
            logger.exception(f"[ServiceManager::start_service] Error starting service {service_name}: {e}")
            return False

    async def stop_service(self, service_name: str):
        """Остановка сервисов по имени"""
        logger.info(f"[ServiceManager::stop_service] started | {service_name}")
        try:
            match service_name:
                case "test_service":
                    await self.test_service.stop()
                case _:
                    logger.error(f"[ServiceManager::stop_service] Unknown service: {service_name}")
                    return False
            
            logger.info(f"[ServiceManager::stop_service] Service {service_name} stopped")
            return True
            
        except Exception as e:
            logger.exception(f"[ServiceManager::stop_service] Error stopping service {service_name}: {e}")
            return False

    async def get_service_status(self, service_name: str) -> bool:
        """Получить статус сервиса (работает/не работает)"""
        logger.info(f"[ServiceManager::get_service_status] started | {service_name}")
        # Проверяем и в БД и в активных сервисах
        db_status = self.db.get_service_status(service_name)
        runtime_status = service_name in self.active_services
        
        logger.info(f"[ServiceManager::get_service_status] completed successfully | db_status::{db_status} | runtime_status::{runtime_status}")
        return db_status and runtime_status

    async def restart_services(self, service_name: str):
        """Перезапуск сервиса"""
        logger.info(f"[ServiceManager::restart_services] started | {service_name}")
        await self.stop_service(service_name)
        await self.start_service(service_name)
        logger.info(f"[ServiceManager::get_service_status] completed successfully")

