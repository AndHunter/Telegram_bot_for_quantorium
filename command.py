from aiogram.types import Message, FSInputFile
from datetime import datetime
from draw_certificat import create_certificate
from keyboard import (
    keyboard_start, keyboard_help, keyboard_free_courses,
    keyboard_how_to_get, quantum_keyboard, keyboard_record,
    keyboard_paid_courses, keyboard_admin_panel
)
from certificates_cmd import get_certificates_cmd, process_name
from aiogram.fsm.context import FSMContext
from scripts.db_output import view_database
from states import CertificateStates, ManualCertificateStates
from dotenv import load_dotenv
from logger import log
import os

load_dotenv()

LINK_SITE = os.getenv("LINK_SITE")
TEXT_SITE = os.getenv("TEXT_SITE")
LINK_VK = os.getenv("LINK_VK")
TEXT_VK = os.getenv("TEXT_VK")
LINK_YOUTUBE = os.getenv("LINK_YOUTUBE")
TEXT_YOUTUBE = os.getenv("TEXT_YOUTUBE")
LINK_TG = os.getenv("LINK_TG")
TEXT_TG = os.getenv("TEXT_TG")
ADMIN_ID = os.getenv("ADMIN_ID")


async def support_cmd(message: Message) -> None:
    """Команда поддержки, отправляет сообщение о том, что вопрос будет передан администратору."""
    await message.answer("Пожалуйста, напишите ваш вопрос, и администратор скоро свяжется с вами.",
                         reply_markup=keyboard_start)
    log(message)


async def forward_to_admin(message: Message) -> None:
    """Пересылает сообщение от пользователя администратору."""
    if message.text.lower() != "назад":
        await message.answer("Ваш вопрос отправлен администратору.")
        await message.bot.send_message(
            ADMIN_ID,
            f"Вопрос от @{message.from_user.username} ({message.from_user.id}):\n{message.text}"
        )
    else:
        await first_cmd(message)
    log(message)


async def admin_reply(message: Message) -> None:
    """Отправляет ответ от администратора пользователю."""
    if message.chat.id == ADMIN_ID:
        if message.reply_to_message is not None:
            parts = message.reply_to_message.text.split('(')
            user_id = parts[-1].split(')')[0]
            await message.bot.send_message(user_id, f"Ответ от администратора:\n{message.text}")
    else:
        await message.answer("Пожалуйста, ответьте на сообщение пользователя, чтобы отправить ответ.")
    log(message)


async def admin_panel(message: Message) -> None:
    """Админ панель. Отправляет БД полностью или ручная генерация сертификата"""
    if message.chat.id == int(ADMIN_ID):
        await message.answer(
            f"Здравствуйте, {message.from_user.first_name}. Вы вошли в админ панель. Выберите действие на клавиатуре.",
            reply_markup=keyboard_admin_panel
        )
    log(message)


async def first_cmd(message: Message) -> None:
    """Отправляет приветственное сообщение пользователю."""
    await message.answer(
        'Здравствуйте, вас приветствует помощник по учебному заведению "Кванториум Фотоника", выберите пожалуйста действие на клавиатуре.',
        reply_markup=keyboard_start
    )
    log(message)


async def help_cmd(message: Message) -> None:
    """Отправляет информацию о учреждении."""
    await message.answer(
        f"""Наш {f"<a href=\"{LINK_SITE}\">{TEXT_SITE}</a>"}
        Наш телефон: +7 (342) 214-42-69
        Наша почта: KvantoriumPerm@gmail.com
        Мы здесь: Пермь, ул.25 октября, 64/1
        Мы открыты: пн-сб, 9:00–21:00
        Наши соцсети: {f"<a href=\"{LINK_VK}\">{TEXT_VK}</a>"} |
        {f"<a href=\"{LINK_YOUTUBE}\">{TEXT_YOUTUBE}</a>"} |
        {f"<a href=\"{LINK_TG}\">{TEXT_TG}</a>"}
        """, reply_markup=keyboard_help,
        parse_mode="HTML"
    )
    log(message)


async def free_courses_cmd(message: Message) -> None:
    """Отправляет сообщение о бесплатных курсах."""
    await message.answer(
        "Вы выбрали бесплатные курсы, выберите пожалуйста действие на клавиатуре.",
        reply_markup=keyboard_free_courses
    )
    log(message)


async def how_to_get_cmd(message: Message) -> None:
    """Отправляет информацию о том, как попасть на курсы."""
    await message.answer(
        f"Вам нужно пройти тесты для вступления, на нашем сайте ",
        parse_mode="HTML", reply_markup=keyboard_how_to_get
    )
    log(message)


async def all_quantuams_cmd(message: Message) -> None:
    """Отправляет сообщение о выборе квантумов."""
    await message.answer(
        "Выберите квантум, о котором хотите узнать подробнее.",
        reply_markup=quantum_keyboard
    )
    log(message)


async def record_cmd(message: Message) -> None:
    """Отправляет информацию о записи на курсы."""
    current_month = datetime.now().month
    if current_month in [1, 8, 9, 10]:
        await message.answer(
            "Чтобы записаться на курс, пожалуйста, заполните форму.",  # TODO получить ссылку на форму
            reply_markup=keyboard_record
        )
    else:
        await message.answer(
            "Запись на курсы закончена, следующая начнётся в начале полугодия.", reply_markup=keyboard_record
        )
    log(message)


async def paid_courses_cmd(message: Message) -> None:
    """Отправляет сообщение о платных курсах."""
    await message.answer(
        "Вы выбрали платные курсы, выберите пожалуйста действие на клавиатуре.",
        reply_markup=keyboard_paid_courses
    )
    log(message)


async def manual_certificate_cmd(message: Message, state: FSMContext) -> None:
    """Начало создания сертификата. Спрашиваем имя."""
    await message.answer("Введите ФИО участника:")
    await state.set_state(ManualCertificateStates.waiting_for_name)
    log(message)


async def process_name_for_certificate(message: Message, state: FSMContext) -> None:
    """Обрабатывает введенное имя, запрашивает группу."""
    await state.update_data(name=message.text)
    await message.answer("Введите группу участника:")
    await state.set_state(ManualCertificateStates.waiting_for_group)
    log(message)


async def process_group_for_certificate(message: Message, state: FSMContext) -> None:
    """Обрабатывает введенную группу, запрашивает дату окончания."""
    await state.update_data(group=message.text)
    await message.answer("Введите дату окончания (например, 01.01.2025):")
    await state.set_state(ManualCertificateStates.waiting_for_date)
    log(message)


async def process_date_for_certificate(message: Message, state: FSMContext) -> None:
    """Обрабатывает введенную дату окончания, создает сертификат."""
    await state.update_data(date=message.text)
    data = await state.get_data()
    name, group, date = data["name"], data["group"], data["date"]

    certificate_path = create_certificate(name, group, date)
    if certificate_path:
        await message.answer("Сертификат успешно создан.")
        await message.answer_document(FSInputFile(certificate_path))
    else:
        await message.answer("Произошла ошибка при создании сертификата.")

    await state.clear()
    log(message)


async def handler_command(message: Message, state: FSMContext) -> None:
    """Обрабатывает команды, пересылает сообщения и управляет генерацией сертификатов."""

    # Проверяем, является ли сообщение ответом (для пересылки админу или ответа админу)
    if message.reply_to_message is not None:
        if message.chat.id == int(ADMIN_ID):
            await admin_reply(message)
            return
        else:
            await forward_to_admin(message)
            return

    current_state = await state.get_state()

    if current_state == ManualCertificateStates.waiting_for_name.state:
        await process_name_for_certificate(message, state)
        return

    elif current_state == ManualCertificateStates.waiting_for_group.state:
        await process_group_for_certificate(message, state)
        return

    elif current_state == ManualCertificateStates.waiting_for_date.state:
        await process_date_for_certificate(message, state)
        return

    if message.text.lower() == "генерация сертификата" and message.chat.id == int(ADMIN_ID):
        await manual_certificate_cmd(message, state)

    elif current_state == CertificateStates.waiting_for_name.state:
        await process_name(message, state)

    elif message.text.lower() == "информация":
        await help_cmd(message)
    elif message.text.lower() == "назад":
        await first_cmd(message)
    elif message.text.lower() == "админ панель" and message.chat.id == int(ADMIN_ID):
        await admin_panel(message)
    elif message.text.lower() == "вывод бд" and message.chat.id == int(ADMIN_ID):
        db_data = await view_database()

        if db_data:
            await message.answer(f"Данные из базы:\n{db_data}")
        else:
            await message.answer("Нет данных для отображения.")
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
        current_state = await state.get_state()
        if current_state == CertificateStates.waiting_for_name.state:
            await process_name(message, state)
        else:
            await message.answer("Неизвестная команда. Пожалуйста, попробуйте снова.")
    log(message)
