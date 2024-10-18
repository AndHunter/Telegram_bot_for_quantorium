from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
import logging

ADMIN_ID = 5867884661
BOT_TOKEN = '6853584795:AAG1X_3nVDG9SzatOwKvlxooIpAsrBhYXrE'


async def start_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text='Бот запущен')


async def stop_bot(bot: Bot):
    await bot.send_message(ADMIN_ID, text='Бот остановлен')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    from command import first_cmd, help_cmd, support_cmd, handler_command, forward_to_admin, admin_reply

    # Регистрация команд
    dp.message.register(first_cmd, Command(commands='start'))
    dp.message.register(help_cmd, Command(commands='info'))
    dp.message.register(support_cmd, lambda message: message.text == "Поддержка")
    dp.message.register(handler_command)
    # Регистрация обработчиков для пересылки вопросов админу
    dp.message.register(forward_to_admin, lambda message: message.chat.id != ADMIN_ID)
    dp.message.register(admin_reply, lambda message: message.chat.id == ADMIN_ID)

    # Общий обработчик сообщений

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
