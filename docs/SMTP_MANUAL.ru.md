<div align="center" style="margin: 20px 0; padding: 10px; background: #1c1917; border-radius: 10px;">
  <strong>🌐 Язык: </strong>
  
  <span style="color: #F5F752; margin: 0 10px;">
    ✅ 🇷🇺 Русский (текущий)
  </span>
  | 
  <a href="./SMTP_MANUAL.md" style="color: #0891b2; margin: 0 10px;">
    🇺🇸 English
  </a>
</div>

- [На главную](../README.ru.md)

---

- [🧰 Вариант 1. Через `telnet` (классика)](#-вариант-1-через-telnet-классика)
  - [🔹 Установи telnet:](#-установи-telnet)
  - [🔹 Проверка порта:](#-проверка-порта)
- [🧰 Вариант 2. Через `openssl` (TLS / SMTPS проверка)](#-вариант-2-через-openssl-tls--smtps-проверка)
- [🧰 Вариант 3. Через `nc` (netcat)](#-вариант-3-через-nc-netcat)
- [🧰 Вариант 4. Проверка через Python (если хочешь встроить в скрипт)](#-вариант-4-проверка-через-python-если-хочешь-встроить-в-скрипт)
- [🧰 Вариант 5. Через PowerShell (в Windows)](#-вариант-5-через-powershell-в-windows)
- [🧱 Часто блокируются](#-часто-блокируются)

## 🧰 Вариант 1. Через `telnet` (классика)

### 🔹 Установи telnet:

**Ubuntu / Debian:**

```bash
apt install telnet -y
```

**CentOS / RHEL:**

```bash
yum install telnet -y
```

### 🔹 Проверка порта:

```bash
telnet smtp.gmail.com 587
```

или

```bash
telnet mail.domain.com 465
```

Если видишь:

```
Connected to smtp.gmail.com.
Escape character is '^]'.
220 smtp.gmail.com ESMTP ...
```

— значит **порт открыт и исходящее соединение разрешено**.
Если:

```
Connection refused
```

или

```
Connection timed out
```

— значит **порт закрыт или заблокирован провайдером / фаерволом**.

---

## 🧰 Вариант 2. Через `openssl` (TLS / SMTPS проверка)

Для проверки защищённых портов (465, 587):

```bash
openssl s_client -connect smtp.gmail.com:465 -crlf -quiet
```

> или

```bash
openssl s_client -connect smtp.gmail.com:587 -starttls smtp -crlf -quiet
```

Если подключение установлено — ты увидишь сертификат и строку `250 STARTTLS` или `220 Ready to start TLS`.

---

## 🧰 Вариант 3. Через `nc` (netcat)

- Быстрая проверка доступности порта:

```bash
nc -zv smtp.gmail.com 25 465 587
```

- Вывод покажет:

```
Connection to smtp.gmail.com 587 port [tcp/submission] succeeded!
```

---

## 🧰 Вариант 4. Проверка через Python (если хочешь встроить в скрипт)

```python
import smtplib

for port in [25, 465, 587]:
    try:
        server = smtplib.SMTP('smtp.gmail.com', port, timeout=5)
        server.quit()
        print(f"✅ Port {port} is open")
    except Exception as e:
        print(f"❌ Port {port} failed: {e}")
```

---

## 🧰 Вариант 5. Через PowerShell (в Windows)

```powershell
Test-NetConnection smtp.gmail.com -Port 587
```

- Результат:

```
TcpTestSucceeded : True
```

> означает, что порт открыт.

---

## 🧱 Часто блокируются

Многие хостинги и провайдеры **блокируют исходящий SMTP-порт 25** для защиты от спама.
Если он закрыт:

- Используй **465 (SMTPS)** или **587 (submission)**.
- Или настрой реле через свой почтовый сервис (Mailgun, SendGrid, Postmark и т.д.).

---
