from command import first_cmd, help_cmd, handler_command

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import logging

BOT_TOKEN = '6853584795:AAG1X_3nVDG9SzatOwKvlxooIpAsrBhYXrE'


async def start_bot(bot: Bot):
    await bot.send_message(5867884661, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(5867884661, text='Бот остановлен')



async def start():
    logging.basicConfig(level=logging.INFO,
                         format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(first_cmd, Command(commands='start'))
    dp.message.register(help_cmd, Command(commands='info'))
    dp.message.register(handler_command)



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())