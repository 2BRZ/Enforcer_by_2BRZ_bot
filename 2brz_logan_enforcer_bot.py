
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    welcome_message = (
        f"👋 Welcome to the 2BRZ Brotherhood, {user.mention_html()}!
"
        "🔥 This bot is powered by Logan's Enforcer Protocol.
"
        "Use /help to see available commands."
    )
    await update.message.reply_html(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "🛠️ Available Commands:
"
        "/start - Welcome message
"
        "/help - List of commands
"
        "More features coming soon..."
    )
    await update.message.reply_text(help_text)

def main() -> None:
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    logger.info("Logan Enforcer Bot has started.")
    app.run_polling()

if __name__ == '__main__':
    main()
