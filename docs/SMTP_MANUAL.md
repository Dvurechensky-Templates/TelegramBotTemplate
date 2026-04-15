<div align="center" style="margin: 20px 0; padding: 10px; background: #1c1917; border-radius: 10px;">
  <strong>🌐 Language: </strong>
  
  <a href="./SMTP_MANUAL.ru.md" style="color: #F5F752; margin: 0 10px;">
    🇷🇺 Russian
  </a>
  | 
  <span style="color: #0891b2; margin: 0 10px;">
    ✅ 🇺🇸 English (current)
  </span>
</div>

- [Back to main](../README.md)

---

- [🧰 Option 1. Using `telnet` (classic)](#-option-1-using-telnet-classic)
  - [🔹 Install telnet:](#-install-telnet)
  - [🔹 Port check:](#-port-check)
- [🧰 Option 2. Using `openssl` (TLS / SMTPS check)](#-option-2-using-openssl-tls--smtps-check)
- [🧰 Option 3. Using `nc` (netcat)](#-option-3-using-nc-netcat)
- [🧰 Option 4. Using Python (if you want to integrate into a script)](#-option-4-using-python-if-you-want-to-integrate-into-a-script)
- [🧰 Option 5. Using PowerShell (on Windows)](#-option-5-using-powershell-on-windows)
- [🧱 Commonly blocked](#-commonly-blocked)

## 🧰 Option 1. Using `telnet` (classic)

### 🔹 Install telnet:

**Ubuntu / Debian:**

```bash
apt install telnet -y
```

**CentOS / RHEL:**

```bash
yum install telnet -y
```

### 🔹 Port check:

```bash
telnet smtp.gmail.com 587
```

or

```bash
telnet mail.domain.com 465
```

If you see:

```
Connected to smtp.gmail.com.
Escape character is '^]'.
220 smtp.gmail.com ESMTP ...
```

— it means the **port is open and outgoing connection is allowed**.

If you see:

```
Connection refused
```

or

```
Connection timed out
```

— it means the **port is closed or blocked by provider / firewall**.

---

## 🧰 Option 2. Using `openssl` (TLS / SMTPS check)

To check secure ports (465, 587):

```bash
openssl s_client -connect smtp.gmail.com:465 -crlf -quiet
```

or

```bash
openssl s_client -connect smtp.gmail.com:587 -starttls smtp -crlf -quiet
```

If the connection is successful — you will see the certificate and a line like `250 STARTTLS` or `220 Ready to start TLS`.

---

## 🧰 Option 3. Using `nc` (netcat)

- Quick port availability check:

```bash
nc -zv smtp.gmail.com 25 465 587
```

- Output example:

```
Connection to smtp.gmail.com 587 port [tcp/submission] succeeded!
```

---

## 🧰 Option 4. Using Python (if you want to integrate into a script)

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

## 🧰 Option 5. Using PowerShell (on Windows)

```powershell
Test-NetConnection smtp.gmail.com -Port 587
```

- Result:

```
TcpTestSucceeded : True
```

> means the port is open.

---

## 🧱 Commonly blocked

Many hosting providers and ISPs **block outgoing SMTP port 25** to prevent spam.

If it is blocked:

- Use **465 (SMTPS)** or **587 (submission)** instead.
- Or configure a relay via your mail service (Mailgun, SendGrid, Postmark, etc.).

---
