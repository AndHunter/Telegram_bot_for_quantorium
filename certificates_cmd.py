from typing import Optional, List
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from draw_certificat import create_certificate
from keyboard import keyboard_paid_courses
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import FSInputFile
from states import CertificateStates
from dotenv import load_dotenv
import asyncio
import os
import gspread

load_dotenv()


def get_relative_dates(end_date_str: str) -> List[str]:
    """
    Получает даты сертификатов относительно указанной даты.

    Аргументы:
        end_date_str (str): Дата из столбца 'end date' в формате "DD.MM.YY".

    Возвращает:
        list[str]: Список из упорядоченных дат для актуальной, прошлой и позапрошлой группы.
    """
    end_date = datetime.strptime(end_date_str, "%d.%m.%y")
    end_month_day = end_date.strftime("%d.%m")

    end_year = end_date.year

    # Если месяц 05 (май), то возвращаем список с май, декабрь и снова май
    if end_month_day == "26.05":
        return [
            f"{end_month_day}.{end_year}",  # 26.05.XX (основная дата)
            f"26.12.{end_year - 1}",  # 26.12.(прошлый год)
            f"{end_month_day}.{end_year - 1}"  # 26.05.(прошлый год)
        ]

    # Если месяц 12 (декабрь), то возвращаем список с декабрь, май и снова декабрь
    elif end_month_day == "26.12":
        return [
            f"{end_month_day}.{end_year}",  # 26.12.XX (основная дата)
            f"26.05.{end_year - 1}",  # 26.05.(прошлый год)
            f"26.12.{end_year - 1}"  # 26.12.(прошлый год)
        ]

    # В случае других дат (если они не 26.05 или 26.12), возвращаем стандартный порядок
    else:
        return [
            f"{end_month_day}.{end_year}",  # Основная дата
            f"26.12.{end_year - 1}",  # 26.12.XX (прошлый год)
            f"26.05.{end_year - 1}"  # 26.05.XX (прошлый год)
        ]


def authorize_google_sheets() -> gspread.client.Client:
    """
        Авторизует доступ к Google Sheets с использованием учетных данных из файла JSON.

        Returns:
            gspread.client.Client: Объект клиента gspread для работы с Google Sheets.
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("crenditails.json", scope)
    client = gspread.authorize(creds)
    return client


def find_data(sheet: gspread.Worksheet, search_value: str) -> Optional[dict]:
    """
       Ищет данные в листе Google Sheets по заданному значению.

       Args:
           sheet (gspread.Worksheet): Лист Google Sheets, в котором осуществляется поиск.
           search_value (str): Значение, по которому производится поиск.

       Returns:
           Optional[dict]: Словарь с данными найденной строки или None, если данные не найдены.
    """
    all_records = sheet.get_all_records()
    search_value = search_value.lower()
    for row in all_records:
        if search_value in (str(value).lower() for value in row.values()):
            return row
    return None


async def get_certificates_cmd(message: types.Message, state: FSMContext):
    """
        Отправляет пользователю сообщение с просьбой ввести ФИО для поиска сертификата.

        Args:
            message (types.Message): Сообщение, полученное от пользователя.
            state (FSMContext): Контекст состояния для работы с состояниями.

        Returns:
            None
     """
    await message.answer("Пожалуйста, введите ФИО ребёнка для поиска сертификата:")
    await state.set_state(CertificateStates.waiting_for_name)


async def process_name(message: types.Message, state: FSMContext):
    """
    Обрабатывает введенное пользователем ФИО и ищет соответствующий сертификат в Google Sheets.

    Если сертификат найден, он будет создан и отправлен пользователю.

    Args:
        message (types.Message): Сообщение, полученное от пользователя.
        state (FSMContext): Контекст состояния для работы с состояниями.

    Returns:
        None
    """
    user_name = message.text
    sheet = authorize_google_sheets().open("test").sheet1
    found_row = find_data(sheet, user_name.lower())

    if found_row and found_row.get("former group"):
        end_date_str = found_row.get("end date")

        if not end_date_str:
            await message.answer("Дата окончания не найдена. Вы можете сделать результат вручную написав в поддержку", reply_markup=keyboard_paid_courses)
            return

        dates = get_relative_dates(end_date_str)
        certificate_path = f'certificates/{user_name.replace(" ", "_")}_certificate.jpg'
        former_group = found_row['former group']

        group_number = former_group[-1] if former_group[-1].isdigit() else None

        if group_number == "3":
            for i in range(3, 0, -1):
                group = former_group[:-1] + str(i)
                create_certificate(user_name, group, dates[3 - i])
                if os.path.exists(certificate_path):
                    await message.answer_photo(
                        FSInputFile(certificate_path),
                        caption=f"Ваш сертификат за группу {group} ({dates[3 - i]}). Проверьте все данные на сертификате. Если возникла проблема обратитесь в поддержку!",
                        reply_markup=keyboard_paid_courses
                    )
        elif group_number == "2":
            for i in range(2, 0, -1):
                group = former_group[:-1] + str(i)
                create_certificate(user_name, group, dates[2 - i])
                if os.path.exists(certificate_path):
                    await message.answer_photo(
                        FSInputFile(certificate_path),
                        caption=f"Ваш сертификат за группу {group} ({dates[2 - i]}). Проверьте все данные на сертификате. Если возникла проблема обратитесь в поддержку!",
                        reply_markup=keyboard_paid_courses
                    )
        elif group_number == "1":
            create_certificate(user_name, former_group, dates[0])
            if os.path.exists(certificate_path):
                await message.answer_photo(
                    FSInputFile(certificate_path),
                    caption=f"Ваш сертификат за группу {former_group} ({dates[0]}). Проверьте все данные на сертификате. Если возникла проблема обратитесь в поддержку!",
                    reply_markup=keyboard_paid_courses
                )

        await asyncio.sleep(5)
        if os.path.exists(certificate_path):
            os.remove(certificate_path)
    else:
        await message.answer("Сертификат не найден. Пожалуйста проверьте коректность данных.", reply_markup=keyboard_paid_courses)

    await state.clear()
