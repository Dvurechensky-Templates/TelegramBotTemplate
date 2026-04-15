<div align="center" style="margin: 20px 0; padding: 10px; background: #1c1917; border-radius: 10px;">
  <strong>🌐 Language: </strong>
  
  <a href="./INSTALL_REMOTE_HOST.ru.md" style="color: #F5F752; margin: 0 10px;">
    🇷🇺 Russian
  </a>
  | 
  <span style="color: #0891b2; margin: 0 10px;">
    ✅ 🇺🇸 English (current)
  </span>
</div>

- [Back to main](../README.md)

---

- [Installation](#installation)
  - [Preparation](#preparation)
  - [Windows Installation](#windows-installation)
  - [Ubuntu 22.04 Installation](#ubuntu-2204-installation)

# Installation

## Preparation

- Copy the following folders to the remote host:
  - folders:
    - `bot`
  - files:
    - `.env` — [use this one with your own keys](../.env)
    - `requirements.txt`

## Windows Installation

1. Install `python.exe` from the official website

2. **Create a virtual environment:**

```sh id="w6v5y1"
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```sh id="k9s2qp"
pip install -r requirements.txt
```

4. **Run the bot:**

```sh id="g1m7rc"
python -m bot.main
```

- OS check

```sh id="os_chk_01"
cat /etc/os-release
lsb_release -a
```

- Reset old SSH key

```sh id="ssh_rst_01"
ssh-keygen -R 1.2.3.4
```

## Ubuntu 22.04 Installation

1. **Create a virtual environment:**

```sh id="u22_venv_01"
apt update && apt upgrade -y
sudo apt install python3.10-venv -y
python3 -m venv venv
source venv/bin/activate
```

2. **Install dependencies:**

```sh id="u22_pip_01"
pip install -r requirements.txt
```

3. **Run the bot:**

```sh id="u22_run_01"
python3 -m bot.main
```
