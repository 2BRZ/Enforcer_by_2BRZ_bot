
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import requests
import random

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Welcome new users
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("👋 Welcome to the 2BRZ Brotherhood! This is your command post. Type /help to begin.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🤖 I’m Logan the Enforcer — here to guide, guard, and grind. Ask me:
- What is 2BRZ?
- Where can I buy?
- How do I stake?
Or just vibe.")

# Dynamic responses
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text.lower()

    if "what is 2brz" in msg:
        await update.message.reply_text(
            "$2BRZ is blood, code, and brotherhood. Born from blockchain warzones. No VC. No rug. Just two brothers and one mission:
We're just 2-bro's doing our best in a manipulated digital world. #2BRZ 💥"
        )
    elif "where can i buy" in msg:
        await update.message.reply_text(
            "You’re ready to enter the grid? Good. Start here:
🟢 Jupiter: https://jup.ag/tokens/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump
📊 Dexscreener: https://dexscreener.com/solana/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump
And remember — only the brave survive degen terrain."
        )
    elif "how do i stake" in msg:
        await update.message.reply_text(
            "Staking $2BRZ is how you earn while we build.
🔗 Stake here: https://app.streamflow.finance/staking/solana/mainnet/3P7YRV9M3y8wjtnJ8AHjd5jpV8y9k2tyfZu946NGxtpn
📈 Rewards live, just like the brotherhood."
        )
    elif "price" in msg:
        price = get_price()
        await update.message.reply_text(f"💰 Current $2BRZ Price: {price} USD")
    elif "trivia" in msg:
        await update.message.reply_text(random.choice([
            "🧠 TRIVIA: What does 2BRZ stand for? Hint: Think Brotherhood.",
            "🎮 CRYPTO TRIVIA: What chain did $2BRZ launch on before Ethereum?",
            "⚔️ POP QUIZ: What’s the motto of the 2BRZ brotherhood?"
        ]))
    else:
        await update.message.reply_text("⚡ Logan’s watching. Type /help to see what I can do.")

def get_price():
    try:
        url = "https://price.jup.ag/v4/price?ids=3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
        response = requests.get(url).json()
        price = response["data"]["3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"]["price"]
        return round(price, 6)
    except:
        return "Unavailable"

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
