from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# TODO доделать функционал клавиатуры

# Основная клавиатура
kb_start = [
    [KeyboardButton(text="Бесплатные курсы"), KeyboardButton(text="Платные курсы")],
    [KeyboardButton(text="Информация"), KeyboardButton(text="Выдача сертификатов")],
    [KeyboardButton(text="Поддержка")]
]

keyboard_start = ReplyKeyboardMarkup(
    keyboard=kb_start,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)

# Клавиатура помощи
kb_help = [
    [KeyboardButton(text="Бесплатные курсы"), KeyboardButton(text="Платные курсы")],
    [KeyboardButton(text="Выдача сертификатов"), KeyboardButton(text="Назад")],
    [KeyboardButton(text="Поддержка")]
]

keyboard_help = ReplyKeyboardMarkup(
    keyboard=kb_help,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)

# Клавиатура бесплатных курсов
kb_free_courses = [
    [
        KeyboardButton(text="Все квантумы"),
        KeyboardButton(text="Как попасть"),
        KeyboardButton(text="Назад"),
        KeyboardButton(text="Поддержка")
    ]
]

keyboard_free_courses = ReplyKeyboardMarkup(
    keyboard=kb_free_courses,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)

# Клавиатура "Как попасть"
kb_how_to_get = [
    [KeyboardButton(text="Все квантумы"), KeyboardButton(text="Информация")],
    [KeyboardButton(text="Записаться на курс"), KeyboardButton(text="Назад")],
    [KeyboardButton(text="Поддержка")]
]

keyboard_how_to_get = ReplyKeyboardMarkup(
    keyboard=kb_how_to_get,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)

# Клавиатура записи на курс
kb_record = [
    [KeyboardButton(text="Информация"), KeyboardButton(text="Назад")],
    [KeyboardButton(text="Поддержка")]
]

keyboard_record = ReplyKeyboardMarkup(
    keyboard=kb_record,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)

# Инлайн кнопки для квантумов
button_media = InlineKeyboardButton(text="Медиаквантум", url="https://kvantorium-perm.ru/quantum/media/")
button_aero = InlineKeyboardButton(text="Аэроквантум", url="https://kvantorium-perm.ru/quantum/aero/")
button_bio = InlineKeyboardButton(text="Биоквантум", url="https://kvantorium-perm.ru/quantum/bio/")
button_cosmo = InlineKeyboardButton(text="Космоквантум", url="https://kvantorium-perm.ru/quantum/cosmo/")
button_it = InlineKeyboardButton(text="IT-квантум", url="https://kvantorium-perm.ru/quantum/it/")
button_nano = InlineKeyboardButton(text="Наноквантум", url="https://kvantorium-perm.ru/quantum/nano/")
button_hightech = InlineKeyboardButton(text="Хайтек", url="https://kvantorium-perm.ru/quantum/hightech/")
button_photonics = InlineKeyboardButton(text="Фотоника", url="https://kvantorium-perm.ru/quantum/photonics/")
button_vr_ar = InlineKeyboardButton(text="VR / AR", url="https://kvantorium-perm.ru/quantum/vr/")
button_design = InlineKeyboardButton(text="Промышленный дизайн", url="https://kvantorium-perm.ru/quantum/promodesign/")
button_robot = InlineKeyboardButton(text="Промробоквантум", url="https://kvantorium-perm.ru/quantum/robo/")

quantum_keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [button_media, button_aero],
    [button_bio, button_cosmo],
    [button_it, button_nano],
    [button_hightech, button_photonics],
    [button_vr_ar, button_design],
    [button_robot]
])

# Клавиатура платных курсов
kb_paid_courses = [
    [KeyboardButton(text="Все квантумы"), KeyboardButton(text="Записаться на курс")],
    [KeyboardButton(text="Информация"), KeyboardButton(text="Назад")],
    [KeyboardButton(text="Поддержка")]
]

keyboard_paid_courses = ReplyKeyboardMarkup(
    keyboard=kb_paid_courses,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)

# Клавиатура админ панели
kb_admin_panel = [
    [KeyboardButton(text="Вывод БД"), KeyboardButton(text="Генерация сертификата")],
    [KeyboardButton(text="Отправить юзеру"), KeyboardButton(text="Назад")]
]

keyboard_admin_panel = ReplyKeyboardMarkup(
    keyboard=kb_admin_panel,
    resize_keyboard=True,
    input_field_placeholder="Выберите действие на клавиатуре"
)
