import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"👋 Welcome to the 2BRZ Brotherhood, {user.mention_html()}!
"
        "This bot was built by Logan to help patrol the digital streets.

"
        "💡 Type /commands to see what I can do."
    )

async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "💡 Commands:
"
        "/start - Welcome message
"
        "/commands - Show available commands
"
        "/logan - Activate Logan Mode"
    )

async def logan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🛡️ Logan Mode Activated: Enforcer engaged. Watching the streets.")

def main() -> None:
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("commands", commands))
    application.add_handler(CommandHandler("logan", logan))
    application.run_polling()

if __name__ == '__main__':
    main()
