
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Set your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Example daily questions
daily_questions = [
    "What’s one thing you learned about crypto this week?",
    "If $2BRZ hit $1.00 tomorrow, what would you do first?",
    "What makes 2BRZ different from the rest of the meme world?",
]

# Command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first = update.effective_user.first_name
    await update.message.reply_text(f"👋 Welcome to 2BRZ Brotherhood, {user_first}! Type /logan or /price to get started.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🛠️ Commands:
/start
/help
/price
/logan
/wenlambo
/2brztrivia")

async def logan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🧠 LOGAN: The Enforcer of Brotherhood. No rugs. No puppets. Just raw code and real vibes. #2BRZ")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("💰 Current $2BRZ Price: Check https://jup.ag/swap/SOL-2BRZ for live pricing.")

async def wenlambo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🚗 WEN LAMBO? When brotherhood > hype and utility > speculation. Sit tight.")

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    question = random.choice(daily_questions)
    await update.message.reply_text(f"🤔 2BRZ Daily Question:
{question}")

# Main function
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("price", price))
    application.add_handler(CommandHandler("logan", logan))
    application.add_handler(CommandHandler("wenlambo", wenlambo))
    application.add_handler(CommandHandler("2brztrivia", trivia))

    application.run_polling()

if __name__ == '__main__':
    main()
