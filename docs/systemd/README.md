```sh
sudo tee /etc/systemd/system/bot.service > /dev/null <<'EOF'
[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/home/tg_bot
Environment=PATH=/home/tg_bot/venv/bin
ExecStart=/home/tg_bot/venv/bin/python3 -m bot.main
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF
```

- Проверка путей
-

# Проверьте что существует main.py в папке bot

````sh
ls -la /home/tg_bot/bot/main.py
```

# Проверьте виртуальную среду
```sh
ls -la /home/tg_bot/venv/bin/python3
```

# Перезагружаем systemd

```sh
sudo systemctl daemon-reload
````

# Включаем автозапуск при загрузке

```sh
sudo systemctl enable bot.service
```

# Запускаем сервис

```sh
sudo systemctl start bot.service
```

# Проверяем статус

```sh
sudo systemctl status bot.service
```

- Полезное

# Посмотреть логи в реальном времени

```sh
sudo journalctl -u bot.service -f
```

# Посмотреть последние логи

```sh
sudo journalctl -u bot.service -n 50
```

# Перезапустить сервис

```sh
sudo systemctl restart bot.service
```

# Остановить сервис

```sh
sudo systemctl stop bot.service
```
