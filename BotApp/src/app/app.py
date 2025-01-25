import os
from aiogram import Dispatcher, Bot
from .settings import API_TOKEN
from . import commands
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN = API_TOKEN


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
            commands.cmd,
        )
    print("Bot is running...")
    await dp.start_polling(bot)

