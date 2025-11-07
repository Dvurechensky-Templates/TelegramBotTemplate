# bot\services\keyboards\keyboards.py
from bot.core.database_manager import DatabaseManager
from asyncio.log import logger


def main_keyboard():
    """Главное меню - Inline клавиатура"""
    logger.info(f"[keyboards::main_keyboard] process")
    return {
        'keyboard': [
            [
                {'text': '🌀 My Services'},
            ],
            [
                {'text': 'ℹ️ Help'},
            ]
        ]
    }

def services_management_keyboard(db: DatabaseManager, user_id: int):
    """
    Возвращает список сервисов с кнопками управления.
    """
    logger.info(f"[keyboards::services_management_keyboard] started | user_id::{user_id}")
    keyboard = []
    
    # Получаем все сервисы из БД
    services = db.get_all_services()
    
    # Добавляем каждый сервис с кнопкой включения/выключения
    for service_name, display_name, is_active in services:
        status_icon = "🟢" if is_active else "🔴"
        status_text = "Выключить" if is_active else "Включить"
        callback_data = f"service_disable:{service_name}" if is_active else f"service_enable:{service_name}"
        
        keyboard.append([
            {'text': f'{status_icon} {display_name}', 'callback_data': f'service_info:{service_name}'},
            {'text': f'{status_text}', 'callback_data': callback_data}
        ])
    
    # Кнопки обновления и назад
    keyboard.append([{'text': '🔄 Обновить', 'callback_data': 'service_refresh'}])
    keyboard.append([{'text': '🔙 На главную', 'callback_data': 'back_main'}])

    logger.info(f"[keyboards::services_management_keyboard] completed successfully")
    return {'inline_keyboard': keyboard}
