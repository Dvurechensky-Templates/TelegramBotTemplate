# core/database_manager.py
from asyncio.log import logger
import sqlite3


class DatabaseManager:
    """Handles all database operations"""

    def __init__(self, db_path: str = "app.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize database tables"""
        logger.info(f"[DatabaseManager::init_database] started")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS telegram_bot_users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')

            # Таблица сервисов бота
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS services (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    display_name TEXT NOT NULL,
                    description TEXT,
                    is_active BOOLEAN DEFAULT 0,
                    config_json TEXT,
                    last_started TIMESTAMP,
                    last_stopped TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')

            # Добавляем начальные сервисы если их нет
            cursor.executemany('''
                INSERT OR IGNORE INTO services (name, display_name, description, is_active)
                VALUES (?, ?, ?, ?)
            ''', [
                ('test_service', 'Тестовый сервис', 'Описание тестового сервиса', 1),
            ])

            conn.commit()

        logger.info(f"[DatabaseManager::init_database] completed successfully")

    def add_user(self, user_id: int, username: str = None, first_name: str = None, last_name: str = None):
        """Добавление пользователя в бота для управления им"""
        logger.info(f"[DatabaseManager::add_user] started | {user_id} | {username} | {first_name} | {last_name}")

        """Add or update user"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO telegram_bot_users 
                (user_id, username, first_name, last_name)
                VALUES (?, ?, ?, ?)
            ''', (user_id, username, first_name, last_name))
            conn.commit()

        logger.info(f"[DatabaseManager::add_user] completed successfully")

    def enable_service(self, service_name: str):
        """Активация сервиса"""
        logger.info(f"[DatabaseManager::enable_service] started | {service_name}")

        """Включить сервис"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE services 
                SET is_active = 1, 
                    last_started = CURRENT_TIMESTAMP,
                    updated_at = CURRENT_TIMESTAMP
                WHERE name = ?
            ''', (service_name,))
            conn.commit()

        logger.info(f"[DatabaseManager::enable_service] completed successfully")

    def disable_service(self, service_name: str):
        """Деактивация сервиса"""
        logger.info(f"[DatabaseManager::disable_service] started | {service_name}")

        """Выключить сервис"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE services 
                SET is_active = 0,
                    last_stopped = CURRENT_TIMESTAMP,
                    updated_at = CURRENT_TIMESTAMP
                WHERE name = ?
            ''', (service_name,))
            conn.commit()

        logger.info(f"[DatabaseManager::disable_service] completed successfully")

    def get_service_status(self, service_name: str) -> bool:
        """Получить статус сервиса"""
        logger.info(f"[DatabaseManager::get_service_status] started | {service_name}")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT is_active FROM services WHERE name = ?', (service_name,))
            result = cursor.fetchone()
            logger.info(f"[DatabaseManager::get_service_status] completed successfully")
            return bool(result[0]) if result else False

    def get_all_services(self):
        """Получить все сервисы"""
        logger.info(f"[DatabaseManager::get_all_services] started")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT name, display_name, is_active FROM services')
            logger.info(f"[DatabaseManager::get_all_services] completed successfully")
            return cursor.fetchall()
        
    def get_service_info(self, service_name: str):
        """Получить полную информацию о сервисе"""
        logger.info(f"[DatabaseManager::get_service_info] started | {service_name}")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT name, display_name, description, is_active, 
                    last_started, last_stopped, created_at
                FROM services 
                WHERE name = ?
            ''', (service_name,))
            logger.info(f"[DatabaseManager::get_service_info] completed successfully")
            return cursor.fetchone()
        