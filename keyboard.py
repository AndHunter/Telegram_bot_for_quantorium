from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types


kb_start = [
    [
    types.KeyboardButton(text="Бесплатные курсы"),
    types.KeyboardButton(text="Платные курсы"),
    types.KeyboardButton(text="Информация"),
    types.KeyboardButton(text="Выдача сертификатов")
     ]

]
keyboard_start = types.ReplyKeyboardMarkup(
    keyboard=kb_start,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

kb_help = [
    [
    types.KeyboardButton(text="Бесплатные курсы"),
    types.KeyboardButton(text="Платные курсы"),
    types.KeyboardButton(text="Выдача сертификатов"),
    types.KeyboardButton(text="Назад")
     ]

]
keyboard_help = types.ReplyKeyboardMarkup(
    keyboard=kb_help,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

kb_free_courses = [
    [
    types.KeyboardButton(text="Все кванториумы"),
    types.KeyboardButton(text="Как попасть"),
    types.KeyboardButton(text="Назад")
     ]

]
keyboard_free_courses = types.ReplyKeyboardMarkup(
    keyboard=kb_help,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

kb_how_to_get = [
    [
    types.KeyboardButton(text="Все кванториумы"),
    types.KeyboardButton(text="Информация"),
    types.KeyboardButton(text="Назад")
     ]

]
keyboard_how_to_get = types.ReplyKeyboardMarkup(
    keyboard=kb_help,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

