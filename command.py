from aiogram.types import Message

from keyboard import keyboard


async def first_cmd(message: Message):
    await message.answer('''Здравствуйте, вас приветствует, помощник по учебному заведению "Кванториум Фотоника"."''', reply_markup= keyboard)


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

Мы здесь
Пермь, ул.25 октября, 64/1

Мы открыты
пн-сб, 9:00–21:00

Наши соцсети
VK | YouTube | Telegram""")