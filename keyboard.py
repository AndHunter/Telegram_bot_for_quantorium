from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
    keyboard=kb_free_courses,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

kb_how_to_get = [
    [
    types.KeyboardButton(text="Все кванториумы"),
    types.KeyboardButton(text="Информация"),
    types.KeyboardButton(text="Записаться на курс"),
    types.KeyboardButton(text="Назад")
     ]

]
keyboard_how_to_get = types.ReplyKeyboardMarkup(
    keyboard=kb_how_to_get,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

kb_record = [
    [
    types.KeyboardButton(text="Информация"),
    types.KeyboardButton(text="Назад")
     ]

]
keyboard_record = types.ReplyKeyboardMarkup(
    keyboard=kb_record,
    resize_keyboard=True,
    input_field_placeholder=f"Просто нажми на кнопку"
)

button_media = InlineKeyboardButton(text="Медиаквантум", url="https://kvantorium-perm.ru/quantum/media/")
button_aero = InlineKeyboardButton(text="Аэроквантум", url="https://kvantorium-perm.ru/quantum/aero/")
button_bio = InlineKeyboardButton(text="Биоквантум", url="https://kvantorium-perm.ru/quantum/bio/")
button_cosmo = InlineKeyboardButton(text="Космоквантум", url="https://kvantorium-perm.ru/quantum/cosmo/")
button_it = InlineKeyboardButton(text="IT-квантум", url="https://kvantorium-perm.ru/quantum/it/")
button_nano = InlineKeyboardButton(text="Наноквантум", url="https://kvantorium-perm.ru/quantum/nano/")
button_hightech = InlineKeyboardButton(text="Хайтек", url="https://kvantorium-perm.ru/quantum/hightech/")
button_photonics = InlineKeyboardButton(text="Фотоника", url="https://kvantorium-perm.ru/quantum/photonics/")
button_vr_ar = InlineKeyboardButton(text="VR / AR", url="https://kvantorium-perm.ru/quantum/vr/")
button_design = InlineKeyboardButton(text="Промышленный дизайн", url="https://kvantorium-perm.ru/quantum/promodesign/   ")
button_robot = InlineKeyboardButton(text="Промробоквантум", url="https://kvantorium-perm.ru/quantum/robo/")

quantum_keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [button_media, button_aero],
    [button_bio, button_cosmo],
    [button_it, button_nano],
    [button_hightech, button_photonics],
    [button_vr_ar, button_design],
    [button_robot]
])