
    import logging
    import os
    import random
    import requests
    from telegram import Update, ChatPermissions
    from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ChatMemberHandler

    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # Constants
    WELCOME_MESSAGE = (
        "🚨 Welcome to the brotherhood, soldier. You’ve entered the digital trenches. DYOR, stay sharp, "
        "and don’t trust links unless they come from the core. 🔒 #2BRZ"
    )

    SPAM_KEYWORDS = ["http", ".com", "t.me/", "joinchat", "airdrop", "free sol", "pump"]
    TRIVIA_QUESTIONS = [
        "What blockchain did 2BRZ launch on?",
        "Who are the two brothers behind 2BRZ?",
        "What platform can you stake $2BRZ on?",
        "Complete the phrase: DYOR or ____?"
    ]

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("⚡️2BRZ Logan Enforcer activated. Ready to defend.")

    async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
        for member in update.message.new_chat_members:
            await update.message.reply_text(WELCOME_MESSAGE)

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_text = update.message.text.lower()
        if any(kw in message_text for kw in SPAM_KEYWORDS):
            try:
                await update.message.delete()
                return
            except:
                pass

        # Simple Q&A
        if "what is 2brz" in message_text:
            await update.message.reply_text(
                "$2BRZ is blood, code, and brotherhood. Born from blockchain warzones. "
                "No VC. No rug. Just two brothers and one mission: We're just 2-bro's doing our best in a manipulated digital world. #2BRZ 💥"
            )
        elif "where can i buy" in message_text:
            await update.message.reply_text(
                "🟢 Jupiter: https://jup.ag/tokens/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump\n"
                "📊 Dexscreener: https://dexscreener.com/solana/3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
            )
        elif "how do i stake" in message_text:
            await update.message.reply_text(
                "🔗 Stake here: https://app.streamflow.finance/staking/solana/mainnet/3P7YRV9M3y8wjtnJ8AHjd5jpV8y9k2tyfZu946NGxtpn\n"
                "📈 Rewards live, just like the brotherhood."
            )
        elif "price" in message_text or "/price" in message_text:
            await get_price(update, context)
        elif "daily question" in message_text:
            question = random.choice(TRIVIA_QUESTIONS)
            await update.message.reply_text(f"🤔 2BRZ Daily Question:
{question}")

    async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            url = "https://price.jup.ag/v4/price?ids=3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"
            data = requests.get(url).json()
            price = data["data"]["3oB7hyAZXqrzzbSebt3XykCrXqAX6Vv57Qdin3bVpump"]["price"]
            await update.message.reply_text(f"🟢 Current $2BRZ Price: ${price:.8f}")
        except:
            await update.message.reply_text("❌ Couldn't fetch price. Try again later.")

    if __name__ == '__main__':
        logging.basicConfig(level=logging.INFO)
        app = ApplicationBuilder().token(BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

        print("✅ 2BRZ Logan Enforcer Bot is running.")
        app.run_polling()
