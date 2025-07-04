import logging
import os
import random
import requests
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

# Constants
SPAM_KEYWORDS = ["http", ".com", "t.me/", "joinchat", "airdrop", "free sol", "pump"]
TRIVIA_QUESTIONS = [
    "What blockchain did 2BRZ launch on?",
    "Who are the two brothers behind 2BRZ?",
    "What platform can you stake $2BRZ on?",
    "Complete the phrase: DYOR or ____?",
    "What's the name of the 2BRZ enforcer bot?"
]
MEME_TRIGGERS = {
    "rekt": "💀 Rekt harder than a degen without a ledger.",
    "rug": "🚨 Rug alert! Not on Logan's watch.",
    "moon": "🌕 Straight to the moon — no brakes, no seatbelt.",
    "hodl": "🛡️ HODL like Logan’s holding back a full-stack punch.",
    "wen lambo": "🤑 Soon™. But first, stack $2BRZ and hydrate."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⚡️ 2BRZ Logan Enforcer ready. Watching the grid.")

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            "🚨 Welcome to the brotherhood, soldier. You’ve entered the digital trenches. DYOR, stay sharp, "
            "and don’t trust links unless they come from the core. 🔒 #2BRZ"
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = update.message.text.lower()

    if any(kw in message_text for kw in SPAM_KEYWORDS):
        try:
            await update.message.delete()
            return
        except:
            pass

    for trigger, response in MEME_TRIGGERS.items():
        if trigger in message_text:
            await update.message.reply_text(response)
            return

    if "2brz trivia" in message_text or "daily question" in message_text:
        question = random.choice(TRIVIA_QUESTIONS)
        await update.message.reply_text(f"🤔 2BRZ Daily Question:
{question}")

# Inline commands
async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://price.jup.ag/v4/price?ids=3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
        data = requests.get(url).json()
        price = data["data"]["3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"]["price"]
        await update.message.reply_text(f"🟢 Current $2BRZ Price: ${price:.8f}")
    except:
        await update.message.reply_text("❌ Couldn't fetch price. Try again later.")

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📈 Market cap info coming soon...")

async def logan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "Logan: I build in silence and strike in code.",
        "Logan: Rugproof. Ruthless. Relentless.",
        "Logan: You don’t hype a brotherhood — you earn it."
    ]
    await update.message.reply_text(random.choice(quotes))

async def zeph(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quotes = [
        "Zeph: Strategic minds win long-term games.",
        "Zeph: The market whispers. I listen.",
        "Zeph: Calculated. Composed. Consistent."
    ]
    await update.message.reply_text(random.choice(quotes))

async def links(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟢 Jupiter: https://jup.ag/tokens/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump\n"
        "📊 Dexscreener: https://dexscreener.com/solana/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
    )

async def stake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 Stake here: https://app.streamflow.finance/staking/solana/mainnet/3P7YRV9M3y8wjtnJ8AHjd5jpV8y9k2tyfZu946NGxtpn\n"
        "📈 Rewards live, just like the brotherhood."
    )

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚫 No spam\n🔗 No fake links\n✅ DYOR\n🤝 Respect the brotherhood\n👊 Brotherhood > Hype"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("caps", caps))
    app.add_handler(CommandHandler("logan", logan))
    app.add_handler(CommandHandler("zeph", zeph))
    app.add_handler(CommandHandler("links", links))
    app.add_handler(CommandHandler("stake", stake))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("✅ Enforcer Bot with extras is running.")
    app.run_polling()
