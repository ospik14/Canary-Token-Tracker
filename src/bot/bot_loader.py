import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def start_bot():
    await dp.start_polling(bot)
