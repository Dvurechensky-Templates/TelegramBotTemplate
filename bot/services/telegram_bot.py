# bot\services\telegram_bot.py
import asyncio
from asyncio.log import logger
from typing import Dict

from bot.core import DatabaseManager
from bot.core import ServiceManager
from bot.services import TelegramClientAPI
from bot.services.callbacks import handle_services_callbacks
from bot.services.commands import help, my_services, start
from bot.services.states import TestStates


class TelegramBot:
    """Main bot class using getUpdates"""

    def __init__(self):
        self.db = DatabaseManager()
        self.service_manager: ServiceManager = ServiceManager(self.db, self)

        self.user_states: Dict[int, str] = {}
        self.offset = 0
        self.api: TelegramClientAPI = TelegramClientAPI()

        # Словарь соответствия состояний методам-обработчикам
        self.actions_states = TestStates(self)
        self.state_handlers = {
            # тестовые обработки событий ввода пользователя
            "waiting_test_input": self.actions_states.waiting_test_input
        }

        # команды бота
        self.commands = {
            '/help': help.handle,
            '/start': start.handle,
            "ℹ️ Help": help.handle,
            "🌀 My Services": my_services.handle
        }                

    async def initialize(self):
        """Инициализация сервисов бота"""
        await self.service_manager.initialize()

    async def sendMsg(self, chat_id: int, text: str, keyboard=None):
        """Универсальная отправка сообщения"""
        await self.api.send_message(chat_id, text, keyboard)

    async def editMsg(self, chat_id: int, message_id: int, text: str, keyboard=None):
        """Универсальное редактирование сообщения"""
        await self.api.edit_message(chat_id, message_id, text, keyboard)
   
    async def downloadFile(self, file_id: str, dest_path: str):
        """Универсальное скачивание файла пользователя"""
        await self.api.download_file(file_id=file_id, dest_path=dest_path)

    async def handle_text_message(self, message):
        """Обработка текстовых сообщений"""
        user_id = message['from']['id']
        text = message['text']

        # Обрабатывать только приватные чаты
        if message['chat']['type'] != 'private':
            return

        handler = self.commands.get(text)

        if handler:
            await handler(message, self)
        elif user_id in self.user_states:
            await self.handle_user_input(message)

    async def handle_user_input(self, message):
        """Обрабатывать пользовательский ввод на основе текущего состояния"""
        user_id = message['from']['id']
        full_state = self.user_states.get(user_id)  # example "waiting_test_input:param_id1:param_id2"
        
        if full_state:
            # Берем только базовую часть состояния (до первого двоеточия)
            base_state = full_state.split(':')[0]  # "waiting_test_input"
            handler = self.state_handlers.get(base_state)
            
            if handler:
                logger.info(f"[TelegramBot::handle_user_input] Handling user input with state: {full_state}")
                await handler(message)
            else:
                logger.error(f"[TelegramBot::handle_user_input] No handler for base state: {base_state}")

    async def handle_group_message(self, message):
        chat_id = message['chat']['id']
        message_id = message['message_id']
        
        # обработка постов в каналах приватных и публичных 
        from_user = message.get('from', {}).get('id')
        if not from_user and 'sender_chat' in message:
            from_user = message['sender_chat']['id']  
        
        text = message.get('text', '')
        
        # Игнорируем сообщения от самого бота (только для message, не для channel_post)
        if 'from' in message and message.get('from', {}).get('is_bot', False):
            return
        
        # ваша обработка
        # ...

    async def handle_callback_query(self, callback_query):
        """Обработка запросов обратного вызова"""
        query_id = callback_query['id']
        data = callback_query['data']
        user_id = callback_query['from']['id']
        message = callback_query['message']
        chat_id = message['chat']['id']
        message_id = message['message_id']

        logger.info(f"[TelegramBot::handle_callback_query][^] RAW CALLBACK DATA: '{data}'")

        await self.api.answer_callback_query(query_id)

        # === ВОЗВРАТ В ГЛАВНОЕ МЕНЮ ===
        if data == "back_main":
            await start.handle(message, self)

        # === УПРАВЛЕНИЕ СЕРВИСАМИ ===
        if data.startswith("service_"):
            await handle_services_callbacks(data, user_id, chat_id, message_id, self)
      
    async def process_update(self, update):
        """Обрабатывает одно конкретное обновление, пришедшее от getUpdates."""
        try:
            self.offset = update['update_id'] + 1

            if 'channel_post' in update:
                channel_post = update['channel_post']
                # Обрабатываем посты в каналах и группах
                if channel_post['chat']['type'] in ['channel', 'group', 'supergroup']:
                    await self.handle_group_message(channel_post)  # используем тот же обработчик
                        
            if 'message' in update:
                message = update['message']

                # Только приватные чаты ( можно убрать )
                if message['chat']['type'] != 'private':

                    if (message['chat']['type'] == 'group' or message['chat']['type'] == 'supergroup'):
                        await self.handle_group_message(message)
                    
                    return

                user_id = message['from']['id']

                if 'text' in message:
                    text = message['text']

                    handler = self.commands.get(text)
                    if handler:
                        await handler(message, self)
                    elif message['from']['id'] in self.user_states:
                        await self.handle_user_input(message)

                # Проверяем состояние пользователя (даже если нет 'text')
                if user_id in self.user_states:
                    await self.handle_user_input(message)
                    return

            elif 'callback_query' in update:
                await self.handle_callback_query(update['callback_query'])

        except Exception as e:
            logger.error(f"[TelegramBot::process_update] Error processing update: {e}")

    async def run(self):
        """Запустить бота"""
        await self.api.start()

        logger.info("[TelegramBot::run] Bot starting with getUpdates...")

        try:
            while True:
                updates = await self.api.get_updates(offset=self.offset)

                for update in updates:
                    update_str = str(update).encode('ascii', 'ignore').decode('ascii')
                    logger.info(f"[TelegramBot::run] Processing update: {update_str}")
                    await self.process_update(update)

                if not updates:
                    await asyncio.sleep(1)

        except KeyboardInterrupt:
            logger.info("[TelegramBot::run] Bot stopped by user")
        except Exception as e:
            logger.error(f"[TelegramBot::run] Bot crashed: {e}")
        finally:
            await self.api.close()

