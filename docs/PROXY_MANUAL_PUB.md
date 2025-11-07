- [Руководство по поднятию прокси](#руководство-по-поднятию-прокси)
  - [1. 3proxy (самый простой вариант)](#1-3proxy-самый-простой-вариант)
    - [**Сетевой фильтр**](#сетевой-фильтр)
    - [**Запуск:**](#запуск)
  - [2. Альтернатива: TinyProxy (ещё проще)](#2-альтернатива-tinyproxy-ещё-проще)
  - [3. Настройка для Telegram](#3-настройка-для-telegram)
  - [4. Важные моменты безопасности](#4-важные-моменты-безопасности)
  - [5. Проверка работы](#5-проверка-работы)

# Руководство по поднятию прокси

## 1. 3proxy (самый простой вариант)

**Установка на Ubuntu/Debian:**

```bash
# Обновляем пакеты
sudo apt update && sudo apt upgrade -y

# Ставим 3proxy
sudo apt install build-essential git net-tools mc -y

# Качаем исходники 3proxy
git clone https://github.com/3proxy/3proxy.git
cd 3proxy

# Компилируем
make -f Makefile.Linux
sudo make -f Makefile.Linux install
```

**Настройка конфига (/etc/3proxy/3proxy.cfg):**

- Чтобы найти точный адрес конфига `3proxy` смотрим его сервис

```sh
nano /etc/systemd/system/3proxy.service
```

> Будет примерно следующее

```sh
sudo tee /etc/systemd/system/3proxy.service > /dev/null <<'EOF'
[Unit]
Description=3proxy tiny proxy server
Documentation=man:3proxy(1)
After=network.target

[Service]
Type=forking
Environment=CONFIGFILE=/etc/3proxy/3proxy.cfg
ExecStart=/usr/local/bin/3proxy ${CONFIGFILE}
ExecReload=/bin/kill -SIGUSR1 $MAINPID
KillMode=process
Restart=on-failure
RestartSec=60s
LimitNOFILE=65536
LimitNPROC=32768
RuntimeDirectory=3proxy

[Install]
WantedBy=multi-user.target
Alias=3proxy.service
EOF
```

- Просмотр конфигурации

```bash
# cat /etc/3proxy/3proxy.cfg
sudo nano /etc/3proxy/3proxy.cfg
```

- Этот конфиг `/etc/3proxy/3proxy.cfg` может вести в `/usr/local/3proxy/conf/3proxy.cfg` что проверяется следюющей командой:

```sh
find / -name "3proxy.cfg" 2>/dev/null
# вывод
/usr/local/3proxy/conf/3proxy.cfg
/etc/3proxy/3proxy.cfg
/home/linuxuser/3proxy/scripts/3proxy.cfg
root@vultr:/home/linuxuser/3proxy#
```

- Заменим эту странную переадресацию на новый конфиг

```sh
sudo nano /etc/3proxy/3proxy.cfg
```

```sh
sudo tee  /etc/3proxy/3proxy.cfg  > /dev/null <<'EOF'
daemon
maxconn 30
nscache 65536
timeouts 1 5 30 60 180 1800 15 60

# DNS servers
nserver 8.8.8.8
nserver 8.8.4.4

# auth
auth strong
users your_login:CL:your_password
allow your_login

# socks5 only
socks -p1080

# logs (optional)
# log /logs/3proxy.log D
EOF
```

### **Сетевой фильтр**

```sh
sudo ufw allow 1080/tcp
# или
sudo iptables -A INPUT -p tcp --dport 1080 -j ACCEPT
```

### **Запуск:**

```bash
sudo pkill -9 3proxy
sleep 2
sudo systemctl daemon-reload
sudo systemctl enable 3proxy
sudo systemctl start 3proxy
sudo systemctl status 3proxy
```

```sh
# Старт ручной
sudo /bin/3proxy /etc/3proxy/3proxy.cfg
3proxy /etc/3proxy/3proxy.cfg
# Проверка
ps aux | grep 3proxy
# Ещё проверка
netstat -tlnp | grep 1080
# Тест прокси
curl --socks5 your_login:your_password@localhost:1080 http://ifconfig.me
```

- Полезные команды

```sh
# проверка запуска 3proxy
netstat -tlnp | grep 1080
# отключение 3proxy
sudo pkill -9 3proxy
# инициализация сервиса
sudo systemctl daemon-reload
sudo systemctl enable 3proxy
sudo systemctl start 3proxy
sudo systemctl status 3proxy
# тестирование подключения с внешнего компьютера
curl --socks5 your_login:your_password@localhost:1080 http://ifconfig.me
```

## 2. Альтернатива: TinyProxy (ещё проще)

**Установка:**

```bash
sudo apt install tinyproxy -y
```

**Настройка (/etc/tinyproxy/tinyproxy.conf):**

```bash
Port 8888
Allow 0.0.0.0/0  # или твой IP для безопасности
BasicAuth username password  # опционально
```

**Запуск:**

```bash
sudo systemctl enable tinyproxy
sudo systemctl start tinyproxy
```

## 3. Настройка для Telegram

**Формат прокси для Telegram:**

```
Тип: SOCKS5/HTTP
IP: твой_сервер_IP
Порт: 3128 (или тот что указал)
Логин: user (если установил)
Пароль: password (если установил)
```

## 4. Важные моменты безопасности

**Обязательно:**

- Открой порт в фаерволе:

```bash
sudo ufw allow 3128/tcp
```

**Рекомендуется:**

- Использовать сложные пароли
- Ограничить доступ по IP (`Allow твой_IP` в tinyproxy)
- Рассмотреть настройку аутентификации

## 5. Проверка работы

```bash
curl --proxy http://user:password@localhost:3128 http://ifconfig.me
```
