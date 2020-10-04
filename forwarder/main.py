from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils.executor import start_polling


TOKEN = getenv('BOT_TOKEN')
response = 'Бот переехал на новый адрес @mznaim_bot.\nThe bot has moved to new address @zmanim_bot.'

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def handle_all(msg: Message):
    await msg.reply(response)


start_polling(dp)
