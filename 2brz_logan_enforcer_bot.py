
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# BOT TOKEN: Replace with your real token
BOT_TOKEN = "7565862724:AAFA-kZ0Q2BLY_deUkLjrmFQMHqsOjoC9fI"

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👋 Welcome to the 2BRZ Brotherhood! Type /help to see available commands.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = (
        "🛠️ Commands:
"
        "/start - Welcome message
"
        "/help - Show this help message
"
        "/logan - Who is Logan?
"
        "/price - Get latest 2BRZ token price
"
        "2brz trivia - Get a random trivia
"
        "wen lambo - LFG 🚀"
    )
    await update.message.reply_text(commands)

# /logan command
async def logan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("💪 Logan is the Blockchain Brawler of 2BRZ. All action. No brakes.")

# /price command
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("📈 $2BRZ price: Check it live here: https://jup.ag/swap/SOL-2BRZ")

# text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if "wen lambo" in text:
        await update.message.reply_text("🚗💨 Sooner than the haters expect. Buckle up.")
    elif "2brz trivia" in text:
        await update.message.reply_text("🤔 2BRZ Daily Question:
What does DYOR stand for?")
    else:
        await update.message.reply_text("⚡ I see you. Stay based.")

# Main function
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("logan", logan))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
