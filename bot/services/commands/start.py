# bot\services\commands\start.py
from bot.services.keyboards.keyboards import main_keyboard
from bot.config import currentSettings


def is_admin(username: str) -> bool:
    """Проверяет, является ли пользователь администратором"""
    if not username:
        return False
    return username.lower() in [admin.lower() for admin in currentSettings.ADMIN_USERNAMES]

async def handle(message, bot):
    """Handle /start command"""
    user = message['from']
    user_id = user['id']
    username = user.get('username')

    # Проверяем права доступа
    if not is_admin(username):
        await bot.sendMsg(
            message['chat']['id'],
            "❌ У вас нет доступа к этому боту!\n"
            "Обратитесь к администратору для получения прав 🛠️"
        )
        return
    
    bot.db.add_user(
        user_id,
        user.get('username'),
        user.get('first_name'),
        user.get('last_name')
    )

    welcome_text = (
        f"🔐 Хм, {user.get('first_name', 'User')} 😈\n"
        "Добро пожаловать шаблон бота от ⭐<b>Dvurechensky</b>⭐!\n\n"
        "\t\t\t\t\t<b>Доступные функции и команды</b>:\n\n"
        "•🔥 <b><u>My Services</u></b> - Показывает список функций и сервисов, статусы их активации в боте\n"
        "•🔥 <b><u>Help</u></b> - Справочная информация\n\n"
        "Выберите вариант из меню ниже:"
    )

    await bot.sendMsg(
        message['chat']['id'],
        welcome_text,
        main_keyboard()
    )