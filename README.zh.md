<p align="center">Dvurechensky</p>

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
  Telegram Bot Template
</h1>

<div align="center">

<strong>语言: </strong>
<span style="color: #F5F752; margin: 0 10px;">✅ CN 中文（当前）</span> |
<a href="./README.ru.md">RU Russian</a> |
<a href="./README.md">US English</a>

</div>

---

# Telegram 机器人模板

- [Telegram 机器人模板](#telegram-机器人模板)
  - [项目结构](#项目结构)
    - [优点](#优点)
    - [注意事项](#注意事项)
  - [文档](#文档)
  - [功能](#功能)
    - [前置条件](#前置条件)
    - [获取凭证](#获取凭证)
      - [Bot Token](#bot-token)
      - [API 凭证](#api-凭证)
  - [使用方法](#使用方法)
  - [日志](#日志)

---

## 项目结构

```sh
bot/
 ├─ config/
 ├─ core/
 ├─ services/
 ├─ utils/
 ├─ main.py
 └─ __init__.py
```

- **core/** — 核心层：数据库管理、服务管理、核心逻辑与基础设施
- **services/** — 功能层：commands、callbacks、keyboards、states、API 等，每个模块相互独立，易于扩展
- **utils/** — 工具函数
- **config/** — 配置（token、设置等），与逻辑分离
- **main.py** — 程序入口

---

### 优点

- 清晰的多层架构
- 易于扩展新功能（commands / services）
- 良好的模块隔离
- 适合团队开发

---

### 注意事项

- 当项目规模增大时，`services/` 目录可能变得复杂
- 可以考虑使用子模块或命名空间进行拆分

---

## 文档

- [变更记录](docs/CHANGELOG.ru.md)
- [任务列表](docs/TASKS.ru.md)
- [Linux 清理指南](docs/CLEAR_NET.ru.md)
- [远程部署](docs/INSTALL_REMOTE_HOST.ru.md)
- [代理配置](docs/PROXY_MANUAL_PUB.ru.md)
- [SMTP 检查](docs/SMTP_MANUAL.ru.md)
- [凭证说明](docs/CREDENTIALS.ru.md)
- [systemd 说明](docs/systemd/README.ru.md)

---

## 功能

- 功能 1
- 功能 2
- 功能 3
- 功能 4
- 功能 5
- 功能 6
- 功能 7
- 功能 8
- 功能 9
- 功能 10

---

### 前置条件

- Python `3.8+`
- Telegram 账号
- BotFather 提供的 bot token
- 来自 my.telegram.org 的 API 凭证

---

### 获取凭证

#### Bot Token

- 在 Telegram 中联系 `@BotFather`
- 执行 `/newbot`
- 按提示创建机器人
- 将 token 写入 `.env`

获取 `CHAT_ID`：

```
https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
```

发送 `/start` 并发送一条消息即可获取

---

#### API 凭证

- 打开 [https://my.telegram.org](https://my.telegram.org)
- 登录
- 进入 API Development tools
- 创建应用
- 获取 API_ID 和 API_HASH

---

```env
BOT_TOKEN=YOUR_BOT_TOKEN
API_ID=YOUR_API_ID
API_HASH=YOUR_API_HASH
```

---

## 使用方法

- 启动机器人: `/start`
- 查看帮助: `/help`
- 查看服务列表: `My Services`

---

## 日志

所有操作会记录在：

- `app.log`
- 控制台输出

---

> [!NOTE]
> 此模板旨在提供可扩展、结构清晰、接近生产环境的 Telegram Bot 架构。

---

<p align="center">Dvurechensky</p>
