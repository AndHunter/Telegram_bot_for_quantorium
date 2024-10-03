from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types


kb = [
    [
    types.KeyboardButton(text="Бесплатные курсы"),
    types.KeyboardButton(text="Платные курсы"),
    types.KeyboardButton(text="Информация"),
    types.KeyboardButton(text="Выдача сертификатов")
     ]

]
keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)