
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# BOT TOKEN
BOT_TOKEN = "BOT_TOKEN = BOT_TOKEN = "7565862724:AAFA-kZ0Q2BLY_deUkLjrmFQMHqsOjoC9fI"


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Welcome Message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Welcome to the 2BRZ Brotherhood!\n\n"
        "Type /help to see what I can do. This bot keeps things clean, answers questions, and brings Logan’s ⚔️ fire to Telegram. Stay sharp."
    )

# Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🛠️ Commands:\n"
        "/start – Welcome message\n"
        "/help – Show this help\n"
        "/logan – Get Logan’s wisdom\n"
        "/price – Check $2BRZ price\n"
        "You can also type things like 'wen lambo' or '2brz trivia' for fun."
    )

# Fun Replies
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()

    if "wen lambo" in text:
        await update.message.reply_text("🚗 Soon. But only if you HODL like a real bro.")
    elif "rekt" in text:
        await update.message.reply_text("💀 Get rekt or get stacked. Choose wisely.")
    elif "2brz trivia" in text:
        question = random.choice([
            "What year did 2BRZ launch?",
            "Who's the brawler of 2BRZ?",
            "What does DYOR stand for?",
            "What’s the 2BRZ motto?",
            "Where was 2BRZ born — ETH or SOL?"
        ])
        await update.message.reply_text(f"🤔 2BRZ Daily Question:\n{question}")
    elif "/logan" in text:
        await update.message.reply_text(
            "⚔️ Logan says: 'If you’re waiting for permission, you’ve already lost. Move fast. Build faster. Honor always.'"
        )

# Main function
def main() -> None:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("logan", echo))
    application.add_handler(CommandHandler("price", echo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == "__main__":
    main()
