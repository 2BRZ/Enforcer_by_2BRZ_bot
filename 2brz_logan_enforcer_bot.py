import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """🔥 Welcome to 2BRZ_Enforcer.bot — Logan's on duty.

Use /weaponx to activate claws. Use /startraid to launch a raid."""
    )

async def weaponx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://raw.githubusercontent.com/2BRZ/2BRZ_Enforcer/main/assets/logan_claws_out.png",
        caption="Logan has entered Weapon X mode. LFG Raiders. 🧨"
    )

async def startraid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🚀 Join the Raid", callback_data="join_raid")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🔥 Raid initiated. Tap below to join the shill attack squad!", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="⚔️ Raid joined. Logan salutes you, degen.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weaponx", weaponx))
    app.add_handler(CommandHandler("startraid", startraid))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()
