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

<div align="center">

<strong>Language: </strong>
<a href="./README.zh.md">🇨🇳 中文</a> |
<a href="./README.ru.md">🇷🇺 Russian</a> |
<span style="color: #F5F752; margin: 0 10px;">✅ 🇺🇸 English (current)</span>

</div>

---

# Telegram Bot Template

- [Telegram Bot Template](#telegram-bot-template)
  - [Structure](#structure)
    - [✅ Pros:](#-pros)
    - [⚠️ Cons/Notes:](#️-consnotes)
  - [Documentation](#documentation)
  - [Features](#features)
    - [Prerequisites](#prerequisites)
    - [Getting Credentials](#getting-credentials)
      - [Bot Token](#bot-token)
      - [API Credentials](#api-credentials)
  - [Usage](#usage)
  - [Logging](#logging)

## Structure

```sh
bot/
 ├─ config/
 ├─ core/
 ├─ services/
 ├─ utils/
 ├─ main.py
 └─ __init__.py
```

- **core/** — core layer: DB managers, services, tests. Everything responsible for logic and infrastructure.
- **services/** — separate layer for specific functionality: callbacks, commands, keyboards, states, API. Each service is isolated and easily extendable.
- **utils/** — helper functions/utilities.
- **config/** — bot configuration (tokens, settings). Separated from logic.
- **main.py** — entry point.

### ✅ Pros:

- Clean `layered` architecture.
- Easy to `scale` and `add` new `commands`/`services`.
- Good separation of logic and services.
- Suitable for team development — no one breaks the core while working on keyboards or `callbacks`.

### ⚠️ Cons/Notes:

- If the project grows significantly, `services/` may become too large and harder to navigate. Could be improved later with `submodules` or `package namespaces`.

## Documentation

- [Full changelog](docs/CHANGELOG.md)
- [Tasks](docs/TASKS.md)
- [Full Linux machine cleanup after usage](docs/CLEAR_NET.md)
- [Installation](docs/INSTALL_REMOTE_HOST.md)
- [Proxy server setup](docs/PROXY_MANUAL_PUB.md)
- [SMTP - port availability check](docs/SMTP_MANUAL.md)
- [CREDENTIALS](docs/CREDENTIALS.md)
- [Systemd info](docs/systemd/README.md)

## Features

- ✨ Feature 1
- 👹 Feature 2
- 🔐 Feature 3
- 💀 Feature 4
- 💬 Feature 5
- ☔ Feature 6
- 🛡️ Feature 7
- 💾 Feature 8
- 📋 Feature 9
- 🌁 Feature 10

### Prerequisites

- Python `3.8+`
- Telegram `account`
- Bot `token` from @BotFather
- `API credentials` from my.telegram.org

### Getting Credentials

#### Bot Token

- Message @BotFather in Telegram
- Send `/newbot`
- Follow the `instructions` to create your bot
- Copy the `token` into your `.env` file
- To get `CHAT_ID` — go to `https://api.telegram.org/bot<YOUR_TOKEN_BOT>/getUpdates`, first send `/start` to your bot and send `1 message` in the chat where the bot is added as an `administrator`
- `API_HASH` — obtained from your Telegram developer account at `my.telegram.org`

```sh
BOT_TOKEN=YOUR_BOT_TOKEN
API_ID=YOUR_API_ID
API_HASH=YOUR_API_HASH
```

#### API Credentials

- Visit `https://my.telegram.org`
- Log in using your `phone number`
- Go to `API Development tools`
- Select `Create new application`
- Copy API ID, BOT TOKEN, and API Hash into your `.env` file
- Specify allowed Telegram usernames in [ADMIN_USERNAMES](bot/config/settings.py) who will `use` your bot and become its `administrators`

## Usage

- Start the bot: `/start`
- View help: `/help`
- List your services: `🌀 My Services`

## Logging

All actions are logged in:

- `app.log` (file)
- Console output

<p align="center">✨Dvurechensky✨</p>
