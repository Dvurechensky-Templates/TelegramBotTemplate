<div align="center" style="margin: 20px 0; padding: 10px; background: #1c1917; border-radius: 10px;">
  <strong>🌐 Language: </strong>
  
  <a href="./PROXY_MANUAL_PUB.ru.md" style="color: #F5F752; margin: 0 10px;">
    🇷🇺 Russian
  </a>
  | 
  <span style="color: #0891b2; margin: 0 10px;">
    ✅ 🇺🇸 English (current)
  </span>
</div>

- [Back to main](../README.md)

---

- [Proxy Setup Guide](#proxy-setup-guide)
  - [1. 3proxy (the simplest option)](#1-3proxy-the-simplest-option)
    - [**Network Filter**](#network-filter)
    - [**Start:**](#start)
  - [2. Alternative: TinyProxy (even simpler)](#2-alternative-tinyproxy-even-simpler)
  - [3. Telegram Configuration](#3-telegram-configuration)
  - [4. Important Security Notes](#4-important-security-notes)
  - [5. Verification](#5-verification)

# Proxy Setup Guide

## 1. 3proxy (the simplest option)

**Installation on Ubuntu/Debian:**

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install build-essential git net-tools mc -y

# Download 3proxy sources
git clone https://github.com/3proxy/3proxy.git
cd 3proxy

# Compile
make -f Makefile.Linux
sudo make -f Makefile.Linux install
```

**Config setup (/etc/3proxy/3proxy.cfg):**

- To find the exact config path, check the service file:

```sh
nano /etc/systemd/system/3proxy.service
```

> It will look something like this:

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

- View configuration:

```bash
# cat /etc/3proxy/3proxy.cfg
sudo nano /etc/3proxy/3proxy.cfg
```

- This config may point to another location, check with:

```sh
find / -name "3proxy.cfg" 2>/dev/null
# output example:
# /usr/local/3proxy/conf/3proxy.cfg
# /etc/3proxy/3proxy.cfg
# /home/linuxuser/3proxy/scripts/3proxy.cfg
```

- Replace it with your own clean config:

```sh
sudo nano /etc/3proxy/3proxy.cfg
```

```sh
sudo tee /etc/3proxy/3proxy.cfg > /dev/null <<'EOF'
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

### **Network Filter**

```sh
sudo ufw allow 1080/tcp
# or
sudo iptables -A INPUT -p tcp --dport 1080 -j ACCEPT
```

### **Start:**

```bash
sudo pkill -9 3proxy
sleep 2
sudo systemctl daemon-reload
sudo systemctl enable 3proxy
sudo systemctl start 3proxy
sudo systemctl status 3proxy
```

```sh
# Manual start
sudo /bin/3proxy /etc/3proxy/3proxy.cfg
3proxy /etc/3proxy/3proxy.cfg

# Check process
ps aux | grep 3proxy

# Check port
netstat -tlnp | grep 1080

# Test proxy
curl --socks5 your_login:your_password@localhost:1080 http://ifconfig.me
```

- Useful commands:

```sh
# check if 3proxy is running
netstat -tlnp | grep 1080

# stop 3proxy
sudo pkill -9 3proxy

# service management
sudo systemctl daemon-reload
sudo systemctl enable 3proxy
sudo systemctl start 3proxy
sudo systemctl status 3proxy

# test from external machine
curl --socks5 your_login:your_password@localhost:1080 http://ifconfig.me
```

---

## 2. Alternative: TinyProxy (even simpler)

**Installation:**

```bash
sudo apt install tinyproxy -y
```

**Configuration (/etc/tinyproxy/tinyproxy.conf):**

```bash
Port 8888
Allow 0.0.0.0/0  # or restrict to your IP for security
BasicAuth username password  # optional
```

**Start:**

```bash
sudo systemctl enable tinyproxy
sudo systemctl start tinyproxy
```

---

## 3. Telegram Configuration

**Proxy format for Telegram:**

```
Type: SOCKS5/HTTP
IP: your_server_IP
Port: 3128 (or the one you configured)
Login: user (if set)
Password: password (if set)
```

---

## 4. Important Security Notes

**Required:**

- Open the port in the firewall:

```bash
sudo ufw allow 3128/tcp
```

**Recommended:**

- Use strong passwords
- Restrict access by IP (`Allow your_IP` in tinyproxy)
- Enable authentication

---

## 5. Verification

```bash
curl --proxy http://user:password@localhost:3128 http://ifconfig.me
```
