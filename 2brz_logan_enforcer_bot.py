import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
MASTER_KEY = os.getenv("MASTER_LICENSE_KEY")
RAID_LIMIT = 11

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

active_raids = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("🔥 Welcome to 2BRZ_Enforcer.bot — Logan's on duty. Type /weaponx or /startraid to get started.")

async def weaponx(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_photo(
        photo="https://path-to-your-logan-claws-image.png",
        caption="💥 Logan has entered Wolverine Mode!

🗯️ *LFG Raiders!*",
        parse_mode="Markdown"
    )

async def startraid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_chat.id
    active_raids[chat_id] = {"count": 0, "users": set()}

    keyboard = [[InlineKeyboardButton("⚔️ Raid with Logan", callback_data="raid_logan")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔥 Raid initiated! Click below to join the raid:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    user = query.from_user
    chat_id = query.message.chat.id

    if chat_id in active_raids:
        if user.id not in active_raids[chat_id]["users"]:
            active_raids[chat_id]["users"].add(user.id)
            active_raids[chat_id]["count"] += 1
            count = active_raids[chat_id]["count"]
            await query.edit_message_text(f"🔥 {user.first_name} joined the raid!
👥 Total Raiders: {count}/{RAID_LIMIT}")

            if count >= RAID_LIMIT:
                await context.bot.send_message(chat_id=chat_id, text="💀 Logan Raid Complete. 11/11 achieved.")
                del active_raids[chat_id]
        else:
            await query.edit_message_text(f"⛔ {user.first_name}, you're already in this raid.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weaponx", weaponx))
    app.add_handler(CommandHandler("startraid", startraid))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()
