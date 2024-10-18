from aiogram.types import Message
from datetime import datetime
from keyboard import (
    keyboard_start,
    keyboard_help,
    keyboard_free_courses,
    keyboard_how_to_get,
    quantum_keyboard,
    keyboard_record,
    keyboard_paid_courses
)
from main import ADMIN_ID
from certificates_cmd import get_certificates_cmd, process_name
from aiogram.fsm.context import FSMContext

from states import CertificateStates

# TODO вынести константы в отдельный файл .env
LINK_SITE, TEXT_SITE = 'https://kvantorium-perm.ru/', "сайте"
LINK_VK, TEXT_VK = 'https://vk.com/kvantorium.fotonika', 'VK'
LINK_YOUTUBE, TEXT_YOUTUBE = 'https://www.youtube.com/channel/UC8Q99tRVe6T-zzsjBI89RWQ/videos', 'Youtube'
LINK_TG, TEXT_TG = 'https://t.me/kvantoriumperm', 'Telegram'


async def support_cmd(message: Message):
    """Команда поддержки, отправляет сообщение о том, что вопрос будет передан администратору."""
    await message.answer(
        "Пожалуйста, напишите ваш вопрос, и администратор скоро свяжется с вами.",
        reply_markup=keyboard_start
    )


async def forward_to_admin(message: Message):
    """Пересылает сообщение от пользователя администратору."""
    if message.text.lower() != "назад":
        await message.answer("Ваш вопрос отправлен администратору.")
        await message.bot.send_message(
            ADMIN_ID,
            f"Вопрос от @{message.from_user.username} ({message.from_user.id}):\n{message.text}"
        )
    else:
        await first_cmd(message)


async def admin_reply(message: Message):
    """Отправляет ответ от администратора пользователю."""
    if message.chat.id == ADMIN_ID:
        if message.reply_to_message is not None:
            parts = message.reply_to_message.text.split('(')
            user_id = parts[-1].split(')')[0]
            await message.bot.send_message(user_id, f"Ответ от администратора:\n{message.text}")
        else:
            await message.answer("Пожалуйста, ответьте на сообщение пользователя, чтобы отправить ответ.")


async def first_cmd(message: Message):
    """Отправляет приветственное сообщение пользователю."""
    await message.answer(
        'Здравствуйте, вас приветствует помощник по учебному заведению "Кванториум Фотоника", выберите пожалуйста действие на клавиатуре.',
        reply_markup=keyboard_start
    )


async def help_cmd(message: Message):
    """Отправляет информацию о учреждении."""
    await message.answer(
        f"""
        Наш {f"<a href=\"{LINK_SITE}\">{TEXT_SITE}</a>"}

        Наш телефон: +7 (342) 214-42-69
        Наша почта: KvantoriumPerm@gmail.com
        Мы здесь: Пермь, ул.25 октября, 64/1
        Мы открыты: пн-сб, 9:00–21:00
        Наши соцсети: {f"<a href=\"{LINK_VK}\">{TEXT_VK}</a>"} | 
        {f"<a href=\"{LINK_YOUTUBE}\">{TEXT_YOUTUBE}</a>"} | 
        {f"<a href=\"{LINK_TG}\">{TEXT_TG}</a>"}
        """,
        reply_markup=keyboard_help,
        parse_mode="HTML"
    )


async def free_courses_cmd(message: Message):
    """Отправляет сообщение о бесплатных курсах."""
    await message.answer(
        """Вы выбрали бесплатные курсы,
        выберите пожалуйста действие на клавиатуре.""",
        reply_markup=keyboard_free_courses
    )


async def how_to_get_cmd(message: Message):
    """Отправляет информацию о том, как попасть на курсы."""
    await message.answer(
        f"Вам нужно пройти тесты для вступления, на нашем сайте {f"<a href=\"{LINK_SITE}\">{TEXT_SITE}</a>"}",
        parse_mode="HTML",
        reply_markup=keyboard_how_to_get
    )


async def all_quantuams_cmd(message: Message):
    """Отправляет сообщение о выборе квантумов."""
    await message.answer(
        "Выберите квантум о котором хотите узнать подробней ",
        reply_markup=quantum_keyboard
    )


async def record_cmd(message: Message):
    """Отправляет информацию о записи на курсы."""
    current_month = datetime.now().month

    if current_month in [1, 8, 9, 10]:  # Январь, Август, Сентябрь, Октябрь
        await message.answer(
            "Чтобы записаться на курс, пожалуйста, заполните форму.",  # TODO получить ссылку на форму
            reply_markup=keyboard_record
        )
    else:
        await message.answer(
            "Запись на курсы закончена, следующая начнётся в начале полугодия.",
            reply_markup=keyboard_record
        )


async def paid_courses_cmd(message: Message):
    """Отправляет сообщение о платных курсах."""
    await message.answer(
        """Вы выбрали платные курсы,
выберите пожалуйста действие на клавиатуре.""",
        reply_markup=keyboard_paid_courses
    )


async def handler_command(message: Message, state: FSMContext):
    """Обрабатывает команды и пересылает сообщения пользователям и администратору."""
    if message.reply_to_message is not None:
        if message.chat.id == ADMIN_ID:
            # Если это ответ от админа, отправляем ответ пользователю
            await admin_reply(message)
            return
        else:
            await forward_to_admin(message)
            return

    # Обработка команд от пользователей
    if message.text.lower() == "информация":
        await help_cmd(message)
    elif message.text.lower() == "назад":
        await first_cmd(message)
    elif message.text.lower() == "бесплатные курсы":
        await free_courses_cmd(message)
    elif message.text.lower() == "платные курсы":
        await paid_courses_cmd(message)
    elif message.text.lower() == "как попасть":
        await how_to_get_cmd(message)
    elif message.text.lower() == "все кванториумы":
        await all_quantuams_cmd(message)
    elif message.text.lower() == "записаться на курс":
        await record_cmd(message)
    elif message.text.lower() == "выдача сертификатов":
        await get_certificates_cmd(message, state)
    else:
        current_state = await state.get_state()  # Проверяем, находится ли пользователь в состоянии ожидания имени
        if current_state == CertificateStates.waiting_for_name.state:
            await process_name(message, state)
        else:
            await message.answer("Неизвестная команда. Пожалуйста, попробуйте снова.")
