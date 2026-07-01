# Arch Linux Simulator

A terminal-based Arch Linux installation and environment simulator. Boots into a fake GRUB menu, prompts for login credentials, and provides a mock shell for practicing Arch-like commands.

## Getting Started

```bash
python3 src/core/main.py
```

No external dependencies — pure Python 3 standard library.

### Boot Sequence

1. **GRUB Bootloader** — Select `1: Arch Linux` to boot
2. **Login** — Authenticate with the mock credentials

### Login Credentials

| Field | Value |
|---|---|
| Username | `admin` |
| Password | `iusearchbtw` |

## Commands

| Command | Description |
|---|---|
| `exit` | Exit the simulator |
| `clear` | Clear the terminal |
| `whoami` | Display the current user |
| `sudo pacman -Syu` | Simulate an Arch system update |
| `run-app` | Launch an external application via the system shell |

## Project Structure

```
src/
└── core/
    ├── main.py                  # Entry point and REPL loop
    ├── application_run.py       # External app launcher
    ├── bootloader/grub/grub.py  # GRUB boot simulation
    ├── login/login.py           # Login prompt simulation
    └── files/username.txt       # Username data file
```

## License

MIT — Copyright (c) 2026 Li Productions.
