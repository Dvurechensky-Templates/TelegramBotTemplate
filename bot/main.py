#!/usr/bin/env python3
"""
Telegram Bot Template
Использует метод getUpdates для получения сообщений — по умолчанию только для приватных чатов.

Author: Dvurechensky
GitHub: https://github.com/Dvurechensky
Email: nikolay@dvurechensky.pro
Telegram: @dvurechensky_pro
"""

import asyncio
import io
import os
import sys
from bot import setup_logger
from bot import currentSettings as settings
from bot import TelegramBot

# --- Корректная установка кодировки UTF-8 ---
if sys.platform == "win32":
    # Сначала меняем кодировку консоли
    os.system("chcp 65001 >nul")

    # Переназначаем стандартные потоки (stdout и stderr)
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding="utf-8", errors="replace")

# Setup logging
logger = setup_logger(__name__)

async def main():
    """Main function"""
    if not settings.is_valid:
        logger.error("Missing API credentials")
        exit(1)

    # Start bot
    bot = TelegramBot()
    await bot.initialize()
    await bot.run()

if __name__ == "__main__":
    asyncio.run(main())
