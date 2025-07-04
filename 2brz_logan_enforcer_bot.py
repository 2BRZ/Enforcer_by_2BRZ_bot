
import logging
import os
import random
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_price():
    try:
        url = "https://price.jup.ag/v4/price?ids=3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
        data = requests.get(url).json()
        return f"🪙 $2BRZ Current Price: ${data['data']['3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump']['price']:.8f}"
    except:
        return "⚠️ Price feed unavailable. Try again soon."

welcome_messages = [
    "👋 Welcome to the 2BRZ Brotherhood!
This isn’t just a chat. It’s a mission. DYOR. Stay sharp. 💥 #2BRZ",
    "🟢 Another degen just entered the grid. Welcome to the $2BRZ fam. Let's build or get REKT.",
    "🎮 You’ve jacked into the system. Type /help to learn what $2BRZ is all about. Brotherhood > Hype."
]

daily_questions = [
    "🧠 Daily Question: If $2BRZ were a video game, what genre would it be and why?",
    "🔥 Degen Prompt: What's your wildest crypto gain (or loss)?",
    "⚔️ 2BRZ Trivia: What does DYOR stand for?",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(welcome_messages))

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(get_price())

async def stake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Stake your $2BRZ here:
https://app.streamflow.finance/staking/solana/mainnet/3P7YRV9M3y8wjtnJ8AHjd5jpV8y9k2tyfZu946NGxtpn"
    )

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(daily_questions))

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Buy $2BRZ:
Jupiter: https://jup.ag/tokens/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump
"
        "Dexscreener: https://dexscreener.com/solana/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()
    if "what is 2brz" in msg:
        await update.message.reply_text(
            "$2BRZ is blood, code, and brotherhood. Born from blockchain warzones. "
            "No VC. No rug. Just two brothers and one mission:
We're just 2-bro's doing our best in a manipulated digital world. #2BRZ 💥"
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("stake", stake))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("trivia", trivia))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot is live...")
    app.run_polling()

if __name__ == "__main__":
    main()
