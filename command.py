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
from states import CertificateStates, ManualCertificateStates, SendCertificateStates
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
LINK_SIT = os.getenv("LINK_SIT")
TEXT_SIT = os.getenv("TEXT_SIT")
LINK_FORM = os.getenv("LINK_FORM")
TEXT_FORM = os.getenv("TEXT_FORM")


async def support_cmd(message: Message) -> None:
    """Команда поддержки, отправляет сообщение о том, что вопрос будет передан администратору."""
    await message.answer(
        "📝 Напишите ваш вопрос и отправьте его в ответ на это сообщение. Мы скоро свяжемся с вами!  ",
        reply_markup=keyboard_start)
    log(message)


async def forward_to_admin(message: Message) -> None:
    """Пересылает сообщение от пользователя администратору."""
    if message.text.lower() != "назад":
        await message.answer("✅ Ваш вопрос успешно отправлен администратору.")
        await message.bot.send_message(
            ADMIN_ID,
            f"📝 Вопрос от @{message.from_user.username} ({message.from_user.id}):\n{message.text}"
        )
    else:
        await first_cmd(message)
    log(message)


async def admin_reply(message: Message) -> None:
    """Отправляет ответ от администратора пользователю, поддерживая текст, фото и файлы."""
    if message.chat.id == int(ADMIN_ID):
        if message.reply_to_message is not None:
            # Получаем ID пользователя из исходного сообщения
            parts = message.reply_to_message.text.split('(')
            user_id = parts[-1].split(')')[0]

            if message.text:
                await message.bot.send_message(
                    user_id,
                    f"📩 Ответ от администратора:  \n{message.text}\n"
                    "Если у вас есть дополнительные вопросы, просто отправьте их ответом на это сообщение. Мы скоро с вами свяжемся!"
                )
            elif message.photo:
                await message.bot.send_photo(
                    user_id,
                    photo=message.photo[-1].file_id,
                    caption=message.caption or "Если возникли ещё какие-то вопросы, отправьте ответом на это сообщение. Администратор скоро свяжется с вами."
                )
            elif message.document:
                await message.bot.send_document(
                    user_id,
                    document=message.document.file_id,
                    caption=message.caption or "Если возникли ещё какие-то вопросы, отправьте ответом на это сообщение. Администратор скоро свяжется с вами."
                )
            elif message.video:
                await message.bot.send_video(
                    user_id,
                    video=message.video.file_id,
                    caption=message.caption or "Если возникли ещё какие-то вопросы, отправьте ответом на это сообщение. Администратор скоро свяжется с вами."
                )
            elif message.audio:
                await message.bot.send_audio(
                    user_id,
                    audio=message.audio.file_id,
                    caption=message.caption or "Если возникли ещё какие-то вопросы, отправьте ответом на это сообщение. Администратор скоро свяжется с вами."
                )
            elif message.voice:
                await message.bot.send_voice(
                    user_id,
                    voice=message.voice.file_id,
                    caption="Если возникли ещё какие-то вопросы, отправьте ответом на это сообщение. Администратор скоро свяжется с вами."
                )
            else:
                await message.bot.send_message(
                    user_id,
                    "Администратор отправил сообщение в неподдерживаемом формате."
                )
        else:
            await message.answer("Пожалуйста, ответьте на сообщение пользователя, чтобы отправить ответ.")
    else:
        await message.answer("Вы не являетесь администратором.")
    log(message)


async def admin_panel(message: Message) -> None:
    """Админ панель. Отправляет БД полностью или ручная генерация сертификата"""
    if message.chat.id == int(ADMIN_ID):
        await message.answer(
            f"👋 Привет, {message.from_user.first_name}!  Добро пожаловать в админ-панель. Выберите, чем мы можем помочь, используя клавиатуру ⬇️.",
            reply_markup=keyboard_admin_panel
        )
    log(message)


async def first_cmd(message: Message) -> None:
    """Отправляет приветственное сообщение пользователю."""
    await message.answer(
        """
👋 Добро пожаловать в Кванториум!
Выберите, чем мы можем помочь ⬇️.
""",
        reply_markup=keyboard_start
    )
    log(message)


async def help_cmd(message: Message) -> None:
    """Отправляет информацию о учреждении."""
    await message.answer(
        f"""
    📌 Полезная информация:  
🔗 Наш {f"<a href=\"{LINK_SIT}\">{TEXT_SIT}</a>"}  
📞 Телефон: +7 (342) 214-42-69  
📧 Почта: KvantoriumPerm@gmail.com  
📍 Адрес: Пермь, ул. 25 октября, 64/1  
🕘 Время работы: пн-сб, 9:00–21:00  
🌐 Наши соцсети: {f"<a href=\"{LINK_VK}\">{TEXT_VK}</a>"} | {f"<a href=\"{LINK_YOUTUBE}\">{TEXT_YOUTUBE}</a>"} | {f"<a href=\"{LINK_TG}\">{TEXT_TG}</a>"}  
🤖 Разработчики: РКП 2024  
        """, reply_markup=keyboard_help,
        parse_mode="HTML"
    )
    log(message)


async def free_courses_cmd(message: Message) -> None:
    """Отправляет сообщение о бесплатных курсах."""
    await message.answer(
        "🎓 Вы выбрали бесплатные курсы. Выберите действие на клавиатуре ⬇️.  ",
        reply_markup=keyboard_free_courses
    )
    log(message)


async def how_to_get_cmd(message: Message) -> None:
    """Отправляет информацию о том, как попасть на курсы."""
    await message.answer(
        f"📝 Для вступления на курс нужно пройти тесты. Сделать это можно на нашем {f"<a href=\"{LINK_SITE}\">{TEXT_SITE}</a>"}.  ",
        parse_mode="HTML", reply_markup=keyboard_how_to_get
    )
    log(message)


async def all_quantuams_cmd(message: Message) -> None:
    """Отправляет сообщение о выборе квантумов."""
    await message.answer(
        f"📋 Чтобы записаться на курс, пожалуйста, заполните {f"<a href=\"{LINK_FORM}\">{TEXT_FORM}</a>"}.",
        reply_markup=quantum_keyboard
    )
    log(message)


async def record_cmd(message: Message) -> None:
    """Отправляет информацию о записи на курсы."""
    current_month = datetime.now().month
    if current_month in [1, 8, 9, 12]:
        await message.answer(
            f"📋 Чтобы записаться на курс, пожалуйста, заполните {f"<a href=\"{LINK_FORM}\">{TEXT_FORM}</a>"}.",
            reply_markup=keyboard_record, parse_mode="HTML"
        )
    else:
        await message.answer(
            "📅 Запись на курсы завершена, следующая начнется в начале полугодия. Подождите немного! 😊",
            reply_markup=keyboard_record
        )
    log(message)


async def paid_courses_cmd(message: Message) -> None:
    """Отправляет сообщение о платных курсах."""
    await message.answer(
        "💳 Вы выбрали платные курсы. Выберите действие на клавиатуре ⬇️. ",
        reply_markup=keyboard_paid_courses
    )
    log(message)


async def manual_certificate_cmd(message: Message, state: FSMContext) -> None:
    """Начало создания сертификата. Спрашиваем имя."""
    await message.answer("📜 Введите ФИО участника для создания сертификата:")
    await state.set_state(ManualCertificateStates.waiting_for_name)
    log(message)


async def process_name_for_certificate(message: Message, state: FSMContext) -> None:
    """Обрабатывает введенное имя, запрашивает группу."""
    await state.update_data(name=message.text)
    await message.answer("📚 Введите группу участника:")
    await state.set_state(ManualCertificateStates.waiting_for_group)
    log(message)


async def process_group_for_certificate(message: Message, state: FSMContext) -> None:
    """Обрабатывает введенную группу, запрашивает дату окончания."""
    await state.update_data(group=message.text)
    await message.answer("📅 Введите дату окончания курса (например, 26.05.2024):")
    await state.set_state(ManualCertificateStates.waiting_for_date)
    log(message)


async def process_date_for_certificate(message: Message, state: FSMContext) -> None:
    """Обрабатывает введенную дату окончания, создает сертификат."""
    await state.update_data(date=message.text)
    data = await state.get_data()
    name, group, date = data["name"], data["group"], data["date"]

    certificate_path = create_certificate(name, group, date)
    if certificate_path:
        await message.answer("🎉 Сертификат успешно создан! Вот ваш сертификат: 🎓")
        await message.answer_document(FSInputFile(certificate_path))
    else:
        await message.answer("❌ Произошла ошибка при создании сертификата. Пожалуйста, попробуйте снова.")

    await state.clear()
    log(message)


async def start_send_certificate(message: Message, state: FSMContext) -> None:
    """Начало процесса отправки сертификата."""
    await message.answer("Введите ID пользователя, которому нужно отправить сертификат:")
    await state.set_state(SendCertificateStates.waiting_for_user_id)
    log(message)


async def process_user_id(message: Message, state: FSMContext) -> None:
    """Обработка ID пользователя."""
    user_id = message.text.strip()
    if not user_id.isdigit():
        await message.answer("ID пользователя должен быть числом. Попробуйте снова.")
        return

    await state.update_data(user_id=int(user_id))
    await message.answer("Теперь отправьте файл (сертификат) или фото.")
    await state.set_state(SendCertificateStates.waiting_for_file)
    log(message)


async def process_file_or_photo(message: Message, state: FSMContext) -> None:
    """Обрабатывает загрузку файла или фото от администратора и отправляет его обратно пользователю."""
    state_data = await state.get_data()
    user_id = state_data.get("user_id")

    if not user_id:
        await message.answer("ID пользователя не найден. Начните процесс заново.")
        await state.clear()
        return

    if message.document:
        document = message.document
        file_path = f"./{document.file_name}"

        await message.bot.download(document, destination=file_path)

        file = FSInputFile(file_path)
        try:
            await message.bot.send_document(chat_id=user_id, document=file)
            await message.answer(f"Файл успешно отправлен пользователю с ID {user_id}!")
        except Exception as e:
            await message.answer(f"Ошибка при отправке файла: {e}")

    elif message.photo:
        folder_path = './user_certificates'
        os.makedirs(folder_path, exist_ok=True)

        photo = message.photo[-1]
        file_path = f"{folder_path}/{photo.file_id}.jpg"

        await message.bot.download(photo, destination=file_path)

        file = FSInputFile(file_path)
        try:
            await message.bot.send_photo(chat_id=user_id, photo=file)
            await message.answer(f"Фото успешно отправлено пользователю с ID {user_id}!")
        except Exception as e:
            await message.answer(f"Ошибка при отправке фото: {e}")

    else:
        await message.answer("Пожалуйста, отправьте файл или фото.")
        return

    log(message)
    await state.clear()


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

    if current_state == ManualCertificateStates.waiting_for_name.state and message.chat.id == int(ADMIN_ID):
        await process_name_for_certificate(message, state)
        return

    elif current_state == ManualCertificateStates.waiting_for_group.state and message.chat.id == int(ADMIN_ID):
        await process_group_for_certificate(message, state)
        return

    elif current_state == ManualCertificateStates.waiting_for_date.state and message.chat.id == int(ADMIN_ID):
        await process_date_for_certificate(message, state)
        return

    elif current_state == SendCertificateStates.waiting_for_user_id.state and message.chat.id == int(ADMIN_ID):
        await process_user_id(message, state)
        return


    elif current_state == SendCertificateStates.waiting_for_file.state and message.chat.id == int(ADMIN_ID):
        await process_file_or_photo(message, state)
        return

    if message.text.lower() == "отправить юзеру" and message.chat.id == int(ADMIN_ID):
        await start_send_certificate(message, state)
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
    elif message.text.lower() == "все квантумы":
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
