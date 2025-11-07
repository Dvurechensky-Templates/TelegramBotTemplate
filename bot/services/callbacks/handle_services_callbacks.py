# bot\services\callbacks\handle_services_callbacks.py
# Управление сервисами и функциями

from datetime import datetime
from bot.services.keyboards.keyboards import services_management_keyboard
from asyncio.log import logger


async def handle_services_callbacks(data, user_id, chat_id, message_id, bot_instance):
    """Обработка callback'ов связанных с управлением группами"""
    parts = data.split(':')
    action = parts[0]

    if action == "service_refresh":
        await services_refresh(bot_instance, chat_id, message_id, user_id)

    elif action == "service_info":
        service_name = parts[1]
        await service_info(bot_instance, chat_id, message_id, user_id, service_name)

    elif action == "service_disable":
        service_name = parts[1]
        await service_disable(bot_instance, chat_id, message_id, user_id, service_name)

    elif action == "service_enable":
        service_name = parts[1]
        await service_enable(bot_instance, chat_id, message_id, user_id, service_name)

        
async def service_info(bot_instance, chat_id, message_id, user_id, service_name):
    """Показать иформацию о сервисе"""
    logger.info(f"[handle_services_callbacks::service_info] started | chat_id::{chat_id} | message_id::{message_id} | user_id::{user_id} | service_name::{service_name}")

    service_data = bot_instance.db.get_service_info(service_name)
    
    if not service_data:
        await bot_instance.editMsg(
            chat_id=chat_id,
            message_id=message_id,
            text="❌ Сервис не найден"
        )
        logger.info(f"[handle_services_callbacks::service_info] completed successfully | Сервис не найден")
        return
    
    name, display_name, description, is_active, last_started, last_stopped, created_at = service_data
    
    # Форматируем статус
    status = "🟢 ВКЛЮЧЕН" if is_active else "🔴 ВЫКЛЮЧЕН"
    
    # Форматируем даты
    def format_date(timestamp):
        if timestamp:
            format_date_val = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M')
            logger.info(f"[handle_services_callbacks::service_info::format_date] completed successfully | {format_date_val}")
            return format_date_val
        logger.info(f"[handle_services_callbacks::service_info::format_date] completed successfully | Никогда")
        return "Никогда"
    
    # Создаем сообщение
    message_text = f"""
📊 <b>Информация о сервисе</b>

<b>Название:</b> {display_name}
<b>Статус:</b> {status}
<b>Описание:</b> {description or 'Нет описания'}

<b>📅 Создан:</b> {format_date(created_at)}
<b>▶️ Последний запуск:</b> {format_date(last_started)}
<b>⏹️ Последняя остановка:</b> {format_date(last_stopped)}
"""
    
    # Клавиатура для управления
    keyboard = []
    
    # Кнопка включения/выключения
    if is_active:
        keyboard.append([{'text': '⏹️ Выключить', 'callback_data': f'service_disable:{service_name}'}])
    else:
        keyboard.append([{'text': '▶️ Включить', 'callback_data': f'service_enable:{service_name}'}])
    
    # Кнопки назад и обновить
    keyboard.append([
        {'text': '🔙 Назад к сервисам', 'callback_data': 'service_refresh'}
    ])
    
    reply_markup = {'inline_keyboard': keyboard}
    
    await bot_instance.editMsg(
        chat_id,
        message_id,
        message_text,
        reply_markup
    )

    logger.info(f"[handle_services_callbacks::service_info] completed successfully")

    
async def service_disable(bot_instance, chat_id, message_id, user_id, service_name):
    """Выключить сервис"""
    logger.info(f"[handle_services_callbacks::service_disable] started | {chat_id} | {message_id} | {user_id} | {service_name}")
    bot_instance.db.disable_service(service_name)
    await bot_instance.service_manager.stop_service(service_name)
    await services_refresh(bot_instance, chat_id, message_id, user_id)
    logger.info(f"[handle_services_callbacks::service_disable] completed successfully")

async def service_enable(bot_instance, chat_id, message_id, user_id, service_name):
    """Включить сервис"""
    logger.info(f"[handle_services_callbacks::service_enable] started | {chat_id} | {message_id} | {user_id} | {service_name}")
    bot_instance.db.enable_service(service_name)
    await bot_instance.service_manager.start_service(service_name)
    await services_refresh(bot_instance, chat_id, message_id, user_id)
    logger.info(f"[handle_services_callbacks::service_enable] completed successfully")

async def services_refresh(bot_instance, chat_id, message_id, user_id):
    """Обновить список групп"""
    logger.info(f"[handle_services_callbacks::services_refresh] started | {chat_id} | {message_id} | {user_id}")
    await bot_instance.editMsg(
            chat_id,
            message_id,
            "🔗 <b>Управление сервисами и функциями</b>\n\n",
            services_management_keyboard(bot_instance.db, user_id)
        )
    logger.info(f"[handle_services_callbacks::services_refresh] completed successfully")
