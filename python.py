from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🟢 Yahan Apna BotFather Ka API Token Dalna
TOKEN = "7733834389:AAGAI9Iifgv5KHpvVn1S9crEp4xY-hFFbpQ"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Send me a photo, and I will edit it in Ghibli style!")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
