<p align="center">✨Dvurechensky✨</p>

<p align="center">
  <a href="https://sites.google.com/view/dvurechensky" target="_blank">
    <img alt="Dvurechensky" src="https://shields.dvurechensky.pro/badge/Dvurechensky-Nikolay-blue">
  </a>
  <img src="https://shields.dvurechensky.pro/badge/Python-3.11-blue?logo=python&logoColor=FFE873">
  <img src="https://shields.dvurechensky.pro/badge/Telegram-Bot-green?logo=telegram&logoColor=white">
  <img src="https://shields.dvurechensky.pro/badge/Asyncio-gray?logo=python&logoColor=00BFFF">
  <img src="https://shields.dvurechensky.pro/badge/APIs-gray?logo=postman&logoColor=FF6C37">
</p>

<h1 align="center">
  ✨ Telegram Bot Template ✨
</h1>

<div align="center" style="margin: 20px 0; padding: 10px; background: #1c1917; border-radius: 10px;">
  <strong>🌐 Язык: </strong>
  
  <span style="color: #F5F752; margin: 0 10px;">
    ✅ 🇷🇺 Русский (текущий)
  </span>
  | 
  <a href="./README.md" style="color: #0891b2; margin: 0 10px;">
    🇺🇸 English
  </a>
</div>

---

# Шаблон бота для Telegram

- [Шаблон бота для Telegram](#шаблон-бота-для-telegram)
  - [Структура](#структура)
    - [✅ Плюсы:](#-плюсы)
    - [⚠️ Минусы/заметки:](#️-минусызаметки)
  - [Документация](#документация)
  - [Функции](#функции)
    - [Предварительные условия](#предварительные-условия)
    - [Получение учетных данных](#получение-учетных-данных)
      - [Токен бота](#токен-бота)
      - [Учетные данные API](#учетные-данные-api)
  - [Использование](#использование)
  - [Ведение журнала](#ведение-журнала)

## Структура

```sh
bot/
 ├─ config/
 ├─ core/
 ├─ services/
 ├─ utils/
 ├─ main.py
 └─ __init__.py
```

- **core/** — ядро: менеджеры БД, сервисов, тесты. Всё, что отвечает за логику и инфраструктуру.
- **services/** — отдельный слой для конкретных функциональностей: callbacks, commands, keyboards, states, api. Каждый сервис изолирован и можно легко расширять.
- **utils/** — вспомогательные функции/утилиты.
- **config/** — конфиги бота (токены, настройки). Отделено от логики.
- **main.py** — точка входа.

### ✅ Плюсы:

- Чистая `многослойная` архитектура.
- Легко `масштабировать`, `добавлять` новые `команды`/`сервисы`.
- Хорошая изоляция логики и сервиса.
- Подходит для командной работы — никто не будет ломать ядро, работая над клавиатурами или `callbacks`.

### ⚠️ Минусы/заметки:

- Если проект станет реально большим, `services/` может вырасти и станет сложно ориентироваться. Можно будет рассмотреть `submodules` или `package namespace`.

## Документация

- [Полный файл изменений](docs/CHANGELOG.ru.md)
- [Задачи](docs/TASKS.ru.md)
- [Полная чистка Linux тачки после использования](docs/CLEAR_NET.ru.md)
- [Установка](docs/INSTALL_REMOTE_HOST.ru.md)
- [Настройка прокси-сервера](docs/PROXY_MANUAL_PUB.ru.md)
- [SMTP - проверка доступности портов](docs/SMTP_MANUAL.ru.md)
- [CREDENTIALS](docs/CREDENTIALS.ru.md)
- [Информация о systemd](docs/systemd/README.ru.md)

## Функции

- ✨ Функция 1
- 👹 Функция 2
- 🔐 Функция 3
- 💀 Функция 4
- 💬 Функция 5
- ☔ Функция 6
- 🛡️ Функция 7
- 💾 Функция 8
- 📋 Функция 9
- 🌁 Функция 10

### Предварительные условия

- Python `3.8+`
- `Аккаунт` Telegram
- `Токен` бота от @BotFather
- Учётные `данные API` от my.telegram.org

### Получение учетных данных

#### Токен бота

- Написать @BotFather в Telegram
- Отправить `/newbot`
- Следуйте `инструкциям` по созданию бота
- Скопируйте `токен` в ваш файл `.env`
- Чтобы узнать `CHAT_ID` - перейдите по адресу `https://api.telegram.org/bot<YOUR_TOKEN_BOT>/getUpdates` и предварительно нажмите `/start` в боте и введите `1 сообщение` в чате куда его добавите `администратором`
- `API_HASH` - берётся из аккаунта разработчика телеграмма с `my.telegram.org`

```sh
BOT_TOKEN=YOUR_BOT_TOKEN
API_ID=YOUR_API_ID
API_HASH=YOUR_API_HASH
```

#### Учетные данные API

- Посетите `https://my.telegram.org`
- Войдите, используя свой `номер` `телефона`
- Перейти к разделу `API Development tools`
- Выберите `Create new application`
- Скопируйте API ID, BOT TOKEN и API Hash в ваш файл `.env`
- Указать допустимые идентификаторы Telegram в [ADMIN_USERNAMES](bot/config/settings.py) которые будут `пользоваться` вашим ботом и станут его `администраторами`

## Использование

- Запустить бота: `/start`
- Посмотрите справку: `/help`
- Список ваших сервисов: `🌀 My Services`

## Ведение журнала

Все действия регистрируются в:

- `app.log` (файл)
- Вывод в консоль

<p align="center">✨Dvurechensky✨</p>
