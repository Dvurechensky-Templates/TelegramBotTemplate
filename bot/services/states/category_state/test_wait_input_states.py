# bot\services\states\category_state\test_wait_input_states.py
from bot.services.keyboards.keyboards import main_keyboard
from asyncio.log import logger


class TestStates:
    def __init__(self, bot):
        self.bot = bot

    # Если вы внесли в user_states новое состояние то будет отрабатывать этот action
    async def waiting_test_input(self, message):
        """Обработка ввода от аккаунта"""
        user_id = message['from']['id']
        chat_id = message['chat']['id']
        text = message['text']
        logger.info(f"[test_wait_input_states::waiting_test_input] started | user_id::{user_id} | chat_id::{chat_id} | text::{text}")

        # Получаем параметры param из состояния если те были заданы через двоеточие
        full_state = self.bot.user_states.get(user_id)
        if not full_state or not full_state.startswith("waiting_test_input:"):
            logger.info(f"[test_wait_input_states::waiting_test_input] not state waiting_test_input")
            return  # некорректное состояние
        param_id = int(full_state.split(':')[1])

        # Проверка на команду "Отмена"
        if text.lower() in ["отмена", "/cancel"]:
            self.bot.user_states.pop(user_id, None)
            await self.bot.sendMsg(chat_id, "❌ Действие отменено. Возврат в главное меню.")
            # Можно показать клавиатуру главного меню
            await self.bot.sendMsg(chat_id, "🔗 Главное меню:", main_keyboard(user_id))
            logger.info(f"[test_wait_input_states::waiting_test_input] completed successfully | cancel")
            return

        # Проверяем ввод и перенаправляем пользователя дальше на сервис или сообщение о статусе обработке ввода
        # ...

        # Убираем состояние, так как действие завершено
        self.bot.user_states.pop(user_id, None)

        # Возврат в главное меню или панель управления
        await self.bot.sendMsg(chat_id, "🔗 возвращение в главное меню...", main_keyboard())
        logger.info(f"[test_wait_input_states::waiting_test_input] completed successfully")
