
import os
import logging
import requests
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Basic command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👊 Welcome to the 2BRZ Brotherhood. Type /help to get started.")

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "💡 Commands:
"
        "/start - Welcome message
"
        "/help - This help menu
"
        "/price - Get current $2BRZ price
"
        "/stake - Info on how to stake $2BRZ
"
        "/buy - Where to buy $2BRZ
"
    )
    await update.message.reply_text(help_text)

# Price command
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Live $2BRZ price:
https://dexscreener.com/solana/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump")

# Stake command
async def stake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Stake $2BRZ and earn:
https://app.streamflow.finance/staking/solana/mainnet/3P7YRV9M3y8wjtnJ8AHjd5jpV8y9k2tyfZu946NGxtpn")

# Buy command
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Buy $2BRZ here:
https://jup.ag/tokens/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump")

# Message handler
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()
    if "what is 2brz" in user_text:
        await update.message.reply_text(
            "$2BRZ is blood, code, and brotherhood. No VC. No rug. Just 2 brothers in a manipulated digital world. #2BRZ 💥"
        )
    else:
        await update.message.reply_text("⚔️ I'm Logan, the Enforcer. Type /help to see what I can do.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("stake", stake))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    app.run_polling()

if __name__ == "__main__":
    main()
