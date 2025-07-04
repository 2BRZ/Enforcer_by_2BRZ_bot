import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_message = (
        f"👋 Welcome to the 2BRZ Brotherhood, {user.mention_html()}!
"
        "You're now part of the resistance — Logan is watching. 🔒"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=welcome_message,
                                   parse_mode="HTML")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
