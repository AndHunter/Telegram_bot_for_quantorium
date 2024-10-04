from aiogram.types import Message
from keyboard import keyboard_start, keyboard_help


async def first_cmd(message: Message):
    await message.answer('Здравствуйте, вас приветствует помощник по учебному заведению "Кванториум Фотоника".',
                         reply_markup=keyboard_start)


async def help_cmd(message: Message):
    await message.answer("""Наш телефон
    +7 (342) 214-42-69
    Наша почта
    KvantoriumPerm@gmail.com
    Мы здесь
    Пермь, ул.25 октября, 64/1

    Мы открыты
    пн-сб, 9:00–21:00

    Наши соцсети
    VK | YouTube | Telegram
    """, reply_markup=keyboard_help)


# Функция для обработки нажатий на кнопки
async def handler_command(message: Message):
    if message.text.lower() == "информация":
        await help_cmd(message)
    elif message.text.lower() == "назад":
        await first_cmd(message)