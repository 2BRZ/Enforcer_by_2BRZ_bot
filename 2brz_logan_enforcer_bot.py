
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# LOGGING SETUP
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# YOUR BOT TOKEN
BOT_TOKEN = "7565862724:AAFA-kZ0Q2BLY_deUkLjrmFQMHqsOjoC9fI"

# COMMANDS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to the 2BRZ Brotherhood!
This is Logan, your digital enforcer.
Type /help to see what I can do.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠️ Commands:
"
        "/start - Introduction
"
        "/help - Show this help menu
"
        "/logan - Who is Logan?
"
        "/price - Current 2BRZ price
"
        "You can also say things like 'wen lambo' or '2brz trivia' for a surprise!"
    )

async def logan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 Logan Estrada: The Blockchain Brawler.
"
        "A warrior forged in code. Loyalty is his law. Action is his nature.
"
        "#2BRZ #HackTheMeme"
    )

async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 $2BRZ Current Price: Check https://jup.ag/swap/SOL-2BRZ for real-time updates!"
    )

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "wen lambo" in text:
        await update.message.reply_text("🚀 Sooner than the haters expect… 🏎️")
    elif "2brz trivia" in text:
        await update.message.reply_text("🤓 Trivia Time: What does DYOR stand for?
(Hint: It’s the #1 rule in crypto.)")
    elif "gm" in text or "good morning" in text:
        await update.message.reply_text("🌞 GM Brother. Let’s dominate the chain today.")
    elif "rekt" in text:
        await update.message.reply_text("💀 If you’re not learning, you’re losing. We don’t get REKT — we get WISER.")

# MAIN FUNCTION
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("logan", logan_command))
    app.add_handler(CommandHandler("price", price_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    app.run_polling()

if __name__ == '__main__':
    main()
