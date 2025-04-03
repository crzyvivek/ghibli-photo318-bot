import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

TOKEN = "7733834389:AAGAI9Iifgv5KHpvVn1S9crEp4xY-hFFbpQ"
ADMIN_USERNAME = "@crzy_vivek"
ADMIN_TELEGRAM_ID = 1528171780
WHATSAPP_LINK = "https://wa.me/qr/OKTN7MRAWI3CH1"
UPI_ID = "crzyvivek@ybl"
QR_CODE_LINK = "https://files.catbox.moe/dd0deu.jpg"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Start Command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    welcome_text = ("\U0001F44B *Welcome to AI Photo Editor Bot!*\n\n"
                    "I can edit your photos with various effects.\n"
                    "Choose an option below to get started:")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Create/Edit Photo", "Buy Plan", "My Plan", "Contact Support", "About"]
    keyboard.add(*buttons)
    await message.reply(welcome_text, parse_mode="Markdown", reply_markup=keyboard)

# Contact Support
@dp.message_handler(lambda message: message.text == "Contact Support")
async def contact_support(message: types.Message):
    support_text = (f"For any support, contact us here:\n"
                    f"📞 *WhatsApp:* [Click Here]({WHATSAPP_LINK})\n"
                    f"✈️ *Telegram:* {ADMIN_USERNAME}")
    await message.reply(support_text, parse_mode="Markdown", disable_web_page_preview=True)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
  
