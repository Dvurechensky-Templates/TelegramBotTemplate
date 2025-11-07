# bot\services\commands\my_services.py
from bot.services.keyboards.keyboards import services_management_keyboard


async def handle(message, bot):
    user = message['from']
    user_id = user['id']
    chat_id = message['chat']['id']
    
    await bot.sendMsg(
            chat_id,
            "🔗 <b>Управление сервисами</b>\n\nСуществующие фоновые сервисы:",
            services_management_keyboard(bot.db, user_id)
        )
