# bot\services\telegram_client_api.py
import os
import aiohttp
import json
from typing import Optional, Dict, Any
from bot.config.settings import currentSettings as settings
from asyncio.log import logger


class TelegramClientAPI:
    """Асинхронная оболочка вокруг API Telegram Bot (getUpdates, sendMessage, editMessage и т. д.)"""

    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None

    async def start(self):
        """Запуск системы обработки API Telegram"""
        logger.info(f"[TelegramClientAPI::start] started")
        if not self.session:
            self.session = aiohttp.ClientSession()
        logger.info(f"[TelegramClientAPI::start] completed successfully")

    async def close(self):
        """Остановка системы обработки API Telegram"""
        logger.info(f"[TelegramClientAPI::close] started")
        if self.session:
            await self.session.close()
            self.session = None
        logger.info(f"[TelegramClientAPI::close] completed successfully")

    async def send_message(self, chat_id: int, text: str, reply_markup: Optional[Dict] = None) -> Dict[str, Any]:
        """Отправить сообщение через API Telegram"""
        logger.info(f"[TelegramClientAPI::send_message] started | chat_id::{chat_id} | text::{text}")
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)

        async with self.session.post(f"{settings.API_URL}/sendMessage", json=data) as resp:
            resp_json = await resp.json()
            logger.info(f"[TelegramClientAPI::send_message] completed successfully | response::{resp_json}")
            return resp_json

    async def edit_message(self, chat_id: int, message_id: int, text: str, reply_markup: Optional[Dict] = None) -> Dict[str, Any]:
        """Редактировать сообщение через API Telegram"""
        logger.info(f"[TelegramClientAPI::edit_message] started | chat_id::{chat_id} | message_id::{message_id} | text::{text}")
        data = {
            'chat_id': chat_id,
            'message_id': message_id,
            'text': text,
            'parse_mode': 'HTML'
        }
        if reply_markup:
            data['reply_markup'] = json.dumps(reply_markup)

        async with self.session.post(f"{settings.API_URL}/editMessageText", json=data) as resp:
            resp_json = resp.json()
            logger.info(f"[TelegramClientAPI::edit_message] completed successfully | response::{resp_json}")
            return await resp_json

    async def answer_callback_query(self, callback_query_id: str, text: str = "") -> Dict[str, Any]:
        """Ответ на запрос обратного вызова встроенной кнопки"""
        logger.info(f"[TelegramClientAPI::answer_callback_query] started | callback_query_id::{callback_query_id} | text::{text}")
        data = {
            'callback_query_id': callback_query_id,
            'text': text
        }
        async with self.session.post(f"{settings.API_URL}/answerCallbackQuery", json=data) as resp:
            resp_json = resp.json()
            logger.info(f"[TelegramClientAPI::answer_callback_query] completed successfully | response::{resp_json}")
            return await resp_json

    async def download_file(self, file_id: str, dest_path: str):
        """Скачать файл с серверов Telegram"""
        logger.info(f"[TelegramClientAPI::download_file] started | file_id::{file_id} | dest_path::{dest_path}")
        # Получаем путь к файлу
        async with self.session.get(f"{settings.API_URL}/getFile", params={'file_id': file_id}) as resp:
            data = await resp.json()
            if not data.get("ok"):
                logger.exception(f"[TelegramClientAPI::download_file] completed exception")
                raise Exception(f"Ошибка при получении пути файла: {data}")
            file_path = data["result"]["file_path"]

        # Скачиваем сам файл
        file_url = f"https://api.telegram.org/file/bot{settings.BOT_TOKEN}/{file_path}"
        async with self.session.get(file_url) as file_resp:
            if file_resp.status != 200:
                logger.exception(f"[TelegramClientAPI::download_file] completed exception | status::{file_resp.status}")
                raise Exception(f"Ошибка при скачивании файла: {file_resp.status}")
            content = await file_resp.read()

        # Сохраняем файл на диск
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, "wb") as f:
            f.write(content)
        
        logger.info(f"[TelegramClientAPI::download_file] completed successfully")

    async def get_updates(self, offset: int = 0, timeout: int = 30) -> list:
        """Получайте новые обновления от Telegram"""
        logger.info(f"[TelegramClientAPI::get_updates] started | offset::{offset} | timeout::{timeout}")
        params = {
            'offset': offset,
            'timeout': timeout,
            'allowed_updates': ['message', 'callback_query']
        }
        if offset:
            params['offset'] = offset
            
        async with self.session.get(f"{settings.API_URL}/getUpdates", params=params) as resp:
            data = await resp.json()
            if data.get('ok'):
                logger.info(f"[TelegramClientAPI::get_updates] completed successfully | result::{data['result']}")
                return data['result']
            logger.info(f"[TelegramClientAPI::get_updates] completed successfully | response empty")
            return []
