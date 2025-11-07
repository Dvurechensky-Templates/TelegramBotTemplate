# bot\services\commands\help.py


async def handle(message, bot):
    """Обработчик команды /help"""
    help_text = (
        "🔐 <b>Справочная информация</b>\n\n"
        "<b>Как использовать:</b>\n"
        "<b>В разработке</b>\n\n"
    )

    await bot.sendMsg(message['chat']['id'], help_text)