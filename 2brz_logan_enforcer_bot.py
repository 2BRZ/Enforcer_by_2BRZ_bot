import logging
import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MASTER_KEY = os.getenv("MASTER_LICENSE_KEY")
AUTHORIZED_KEYS = os.getenv("AUTHORIZED_KEYS", "").split(",")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

RAID_COUNT = 0
RAID_USERS = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to 2BRZ_Enforcer.bot — Logan's on duty.
"
        "Use /startraid to launch a raid.
"
        "Use /weaponx for transformation.
"
        "This bot is LICENSE PROTECTED."
    )

async def weaponx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo=open("weaponx.png", "rb"),
        caption="🧬 Logan has entered Wolverine Mode!
💥 Claws Out. Let’s Raid.
“LFG Raiders”",
    )

async def startraid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚔️ Raid with Logan", callback_data="join_raid")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🚨 RAID MODE ACTIVATED.
Click to join the raid:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global RAID_COUNT
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if user_id not in RAID_USERS:
        RAID_USERS.add(user_id)
        RAID_COUNT += 1
        await query.edit_message_text(text=f"💥 {RAID_COUNT} Raiders joined.
Next Target Loading…")
    else:
        await query.edit_message_text(text="⚠️ You already joined the raid.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weaponx", weaponx))
    app.add_handler(CommandHandler("startraid", startraid))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
