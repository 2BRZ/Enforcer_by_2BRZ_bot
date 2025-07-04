
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

BOT_TOKEN = "7565862724:AAFA-kZ0Q2BLY_deUkLjrmFQMHqsOjoC9fI"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

WELCOME_MESSAGE = (
    "👋 Welcome to the 2BRZ Brotherhood!
"
    "You're now protected by the Logan Enforcer Bot.
"
    "No rugs. No bots. Just code and honor.

"
    "🛠️ Commands:
"
    "/price - Get current $2BRZ stats
"
    "/help - Learn what I can do
"
    "Say hi to trigger Logan's reply.
"
)

HELP_MESSAGE = (
    "🧠 I'm the ENFORCER — Logan’s digital twin.
"
    "Here’s what I can do:

"
    "/price - Show current 2BRZ token info
"
    "/logan - Hear Logan’s daily quote
"
    "/start - Reintroduce the bot

"
    "Or just say:
"
    "‘wen lambo’ or ‘2brz trivia’ for a surprise. 🚀"
)

TRIVIA_QUESTIONS = [
    "What year did Logan launch the $2BRZ token?",
    "What does DYOR stand for in crypto?",
    "What’s the 2BRZ motto about hype vs. brotherhood?",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_MESSAGE)

async def logan_quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔒 Logan says: 'Build in silence. Deploy in chaos.'")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "wen lambo" in text:
        await update.message.reply_text("🕶️ Logan says: ‘Lambo comes after discipline, not dreams.’")
    elif "2brz trivia" in text:
        question = random.choice(TRIVIA_QUESTIONS)
        await update.message.reply_text(f"🤔 2BRZ Daily Question:
{question}")
    elif "hi" in text or "hello" in text:
        await update.message.reply_text("👊 Logan nods silently. Welcome, brother.")
    else:
        await update.message.reply_text("💬 Logan is watching. Proceed wisely.")

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("logan", logan_quote))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
