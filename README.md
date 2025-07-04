# 🤖 Enforcer_by_2BRZ_bot

**2BRZ Telegram Enforcer Bot**  
Built to automatically greet and moderate new members of the 2BRZ brotherhood on Telegram.  
Runs on [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and designed for Render deployment.

---

## 🔧 Features

- 👋 Sends custom welcome messages to new users
- 🛡️ Auto-enforces group rules or logs actions (optional extensions)
- 🔒 Token securely managed via `.env` file

---

## 📂 File Structure

```
Enforcer_by_2BRZ_bot/
├── .env
├── 2brz_logan_enforcer_bot.py
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Deploy on Render

1. Clone or fork this repo
2. Upload to GitHub
3. Add your bot token to `.env` like this:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

4. Connect your GitHub repo to [Render.com](https://render.com/)
5. Set start command as:
```
python 2brz_logan_enforcer_bot.py
```
6. Deploy & you're live!

---

## 📦 Dependencies

- `python-telegram-bot==20.7`
- `requests`
- `python-dotenv`

These are listed in `requirements.txt` and will auto-install on Render.

---

## 🧠 Authors

- 👊 Logan (The Blockchain Brawler)
- 🧠 Zeph (The Rational Crypto Maestro)

Part of the [2BRZ](https://www.2brz.com) Universe

---

## 🔐 Security

Bot token is stored securely using environment variables via `.env`.

---

## 📜 License

MIT License (Free to modify and use)
