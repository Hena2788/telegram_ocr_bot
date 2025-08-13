# Telegram OCR Bot 🤖📸

A Telegram bot that extracts text from images using Optical Character Recognition (OCR).

## Features ✨
- Extracts text from images sent by users
- Supports multiple languages (via Tesseract)
- Easy setup with Python and Telegram Bot API
- Environment variable configuration

## Prerequisites 🛠️
- Python 3.8+
- Tesseract OCR installed
- Telegram Bot Token from [@BotFather](https://t.me/BotFather)

## Installation 📥

### 1. Clone the repository
git clone https://github.com/yourusername/telegram-ocr-bot.git
cd telegram-ocr-bot

### 2. Set up virtual environment (recommended)
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
# or: .venv\Scripts\activate   # Windows (CMD)
# or: source .venv/bin/activate # Linux/Mac
```

### 3. Install Tesseract OCR
- **Windows**: Download from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
- **Mac**: `brew install tesseract`
- **Linux**: `sudo apt install tesseract-ocr`

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration ⚙️

1. Create `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TESSERACT_CMD=C:\Path\To\tesseract.exe  # Windows example
# TESSERACT_CMD=/usr/bin/tesseract     # Linux/Mac example
```

2. For non-English languages, install additional Tesseract language packs.

## Usage 🚀
```bash
python bot.py
```

## Bot Commands 🤖
- `/start` - Welcome message
- Send any image to extract text

## Project Structure 📂
```
telegram-ocr-bot/
├── bot.py            # Main bot script
├── requirements.txt  # Dependencies
├── .env              # Configuration (gitignored)
├── .gitignore
└── README.md
```

## Troubleshooting 🐛
- **Pillow installation issues**: Try `pip install --upgrade pip wheel setuptools`
- **Tesseract not found**: Verify path in `.env` matches your installation
- **Permission errors**: Run as administrator if needed

## License 📄
MIT License - Feel free to modify and distribute

---

**Note**: Remember to keep your bot token secret! Never commit `.env` to version control.
