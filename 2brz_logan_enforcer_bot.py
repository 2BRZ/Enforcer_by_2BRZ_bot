
import logging
import os
from dotenv import load_dotenv
from telegram import Update, ChatMember
from telegram.ext import (
    ApplicationBuilder,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

WELCOME_MESSAGE = (
    "👋 Welcome to the 2BRZ Brotherhood!

"
    "🛡️ Please don’t spam or you’ll be removed.
"
    "✅ Type /help for commands.
"
    "#2BRZ #CryptoBuiltRight"
)

HELP_TEXT = (
    "💡 Commands:
"
    "/start – Activate bot
"
    "/help – Show this help message
"
    "/about – Learn more about 2BRZ"
)

ABOUT_TEXT = (
    "📡 This bot is powered by 2BRZ.
"
    "🚨 Logan's watching. Keep it clean.
"
    "🌐 Visit: https://2brz.com"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot activated. Type /help to get started!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(ABOUT_TEXT)

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=f"👋 Welcome to the 2BRZ Brotherhood, {member.mention_html()}!

🛡️ Please don’t spam or you’ll be removed.
✅ Type /help for commands.",
            parse_mode="HTML",
        )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()
