
import logging
import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "7565862724:AAFA-kZ0Q2BLY_deUkLjrmFQMHqsOjoC9fI")

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Raid counter
raid_count = 0
RAID_LIMIT = 11

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to the 2BRZ Brotherhood! Type /weaponx to activate Logan mode.")

async def weaponx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global raid_count
    if raid_count >= RAID_LIMIT:
        await update.message.reply_text("🛑 Logan's claws need to cool down... 11 raids already triggered.")
        return

    raid_count += 1
    image_path = "logan_weaponx_2brz.png"
    await update.message.reply_photo(photo=InputFile(image_path), caption="💥 Logan activated. LFG Raiders 🧠⚔️")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weaponx", weaponx))
    app.run_polling()

if __name__ == "__main__":
    main()
