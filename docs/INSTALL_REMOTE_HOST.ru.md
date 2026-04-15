<div align="center" style="margin: 20px 0; padding: 10px; background: #1c1917; border-radius: 10px;">
  <strong>🌐 Язык: </strong>
  
  <span style="color: #F5F752; margin: 0 10px;">
    ✅ 🇷🇺 Русский (текущий)
  </span>
  | 
  <a href="./INSTALL_REMOTE_HOST.md" style="color: #0891b2; margin: 0 10px;">
    🇺🇸 English
  </a>
</div>

- [На главную](../README.ru.md)

---

- [Установка](#установка)
  - [Подготовка](#подготовка)
  - [Установка Windows](#установка-windows)
  - [Установка Ubuntu 22.04](#установка-ubuntu-2204)

# Установка

## Подготовка

- Копируем следующие папки на удалённый хост
  - папки:
    - `bot`
  - файлы
    - `.env` - [Используем этот, со своими ключами](../.env)
    - `requirements.txt`

## Установка Windows

1. Ставим python.exe с офф. сайта

2. **Создайте виртуальную среду:**

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Установите зависимости:**

```sh
pip install -r requirements.txt
```

4. **Запустить бота:**

```sh
python -m bot.main
```

- Чек ОС

```sh
cat /etc/os-release
lsb_release -a
```

- Сброс старого SSH

```sh
ssh-keygen -R 1.2.3.4
```

## Установка Ubuntu 22.04

1. **Создайте виртуальную среду:**

```sh
apt update && apt upgrade -y
sudo apt install python3.10-venv -y
python3 -m venv venv
source venv/bin/activate
```

2. **Установите зависимости:**

```sh
pip install -r requirements.txt
```

3. **Запустить бота:**

```sh
python3 -m bot.main
```
