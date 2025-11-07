- [Очистка](#очистка)
  - [echo \> /var/log/wtmp](#echo--varlogwtmp)
  - [echo \> /var/log/btmp](#echo--varlogbtmp)
  - [echo \> /var/log/lastlog](#echo--varloglastlog)
  - [История команд (очистка)](#история-команд-очистка)
  - [Проверка последних логинов](#проверка-последних-логинов)
  - [Блокировка от брутфорса](#блокировка-от-брутфорса)

## Очистка

### echo > /var/log/wtmp

```sh
# cat /var/log/wtmp
sudo truncate -s 0 /var/log/wtmp
```

### echo > /var/log/btmp

```sh
# cat /var/log/btmp
sudo truncate -s 0 /var/log/btmp
```

### echo > /var/log/lastlog

```sh
# cat /var/log/lastlog
sudo truncate -s 0 /var/log/lastlog
```

### История команд (очистка)

```sh
history -c
```

```sh
history -c
: > ~/.bash_history
history -w
```

### Проверка последних логинов

```sh
# Последние логины
last
lastlog

# Неудачные попытки входа
lastb
who

# Проверить, есть ли процессы в старых терминалах
ps -t pts/1
ps -t pts/2
ps -t pts/3

# Завершить неиспользуемые сессии (если они пустые)
sudo pkill -9 -t pts/1
sudo pkill -9 -t pts/2
sudo pkill -9 -t pts/3

# Или проще - перезагрузить сервер
reboot

(exit или Ctr + D завершают сессии)
```

### Блокировка от брутфорса

- Установка

```sh
sudo apt install fail2ban -y
```

- Копируем конфиг

```sh
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```

- Редактируем

```sh
sudo nano /etc/fail2ban/jail.local
```

> Содержимое

```sh
[sshd]
enabled = true
port = ssh
logpath = /var/log/auth.log
maxretry = 3
bantime = 86400
findtime = 600
```

> или если `ошибка`

```sh
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5
backend = systemd

[sshd]
enabled = true
port = ssh
maxretry = 3
bantime = 3600
backend = systemd
```

- Запуск

```sh
sudo fail2ban-client -t # отладка
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
sudo systemctl status fail2ban
```

- Остановка и удаление

```sh
sudo systemctl stop fail2ban
sudo apt remove --purge fail2ban -y
```

- Глянуть кто забанен

```sh
sudo fail2ban-client status sshd
```

- Перезапуск

```sh
sudo systemctl restart fail2ban
sudo fail2ban-client status sshd
```

- Логи

```sh
sudo tail -20 /var/log/fail2ban.log
```
