import logging
import os
import random
import string
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
MASTER_LICENSE = "2BRZ-121-W3AP0NX-D3V3L0P3R-F0R3V3R-OSAIN-K3Y"
AUTHORIZED_LICENSES = [MASTER_LICENSE]
LICENSE_EXPIRY = {}

RAID_COUNTER = 0
RAIDERS = set()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def generate_license_key():
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=42))
    return random_part + "2BRZ"

def is_license_valid(license_key: str):
    if license_key == MASTER_LICENSE:
        return True
    expiry = LICENSE_EXPIRY.get(license_key)
    return expiry and expiry > datetime.utcnow()

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("🔥 Welcome to 2BRZ_Enforcer.bot — Logan's on duty.")

async def license(update: Update, context: CallbackContext):
    user_license = os.getenv("USER_LICENSE_KEY")
    if not user_license:
        await update.message.reply_text("🚫 No license key set.")
        return

    if is_license_valid(user_license):
        await update.message.reply_text("✅ License is valid and active.")
    else:
        await update.message.reply_text("❌ License expired or invalid. Please purchase a license to continue.")

async def weaponx(update: Update, context: CallbackContext):
    await update.message.reply_photo(
        photo="https://raw.githubusercontent.com/2BRZ/2BRZ_Enforcer/main/assets/weaponx.png",
        caption="🧬 Logan has entered WeaponX Mode

⚔️ LFG Raiders!",
    )

async def raid(update: Update, context: CallbackContext):
    global RAID_COUNTER
    keyboard = [[InlineKeyboardButton("🚀 Raid with Logan", callback_data="join_raid")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    RAID_COUNTER = 0
    RAIDERS.clear()
    await update.message.reply_text("🔥 Raid has started! Click below to join:", reply_markup=reply_markup)

async def button_handler(update: Update, context: CallbackContext):
    global RAID_COUNTER
    query = update.callback_query
    user_id = query.from_user.id
    if query.data == "join_raid":
        if user_id not in RAIDERS:
            RAIDERS.add(user_id)
            RAID_COUNTER += 1
            await query.answer(f"You've joined the raid! Total Raiders: {RAID_COUNTER}")
        else:
            await query.answer("You're already in, soldier!")
    await query.edit_message_reply_markup(reply_markup=None)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("license", license))
app.add_handler(CommandHandler("weaponx", weaponx))
app.add_handler(CommandHandler("startraid", raid))
app.add_handler(CallbackQueryHandler(button_handler))

if __name__ == "__main__":
    user_license = os.getenv("USER_LICENSE_KEY", "")
    if user_license and user_license != MASTER_LICENSE:
        LICENSE_EXPIRY[user_license] = datetime.utcnow() + timedelta(days=3)
        AUTHORIZED_LICENSES.append(user_license)

    print("🔥 2BRZ_Enforcer.bot is live")
    app.run_polling()
