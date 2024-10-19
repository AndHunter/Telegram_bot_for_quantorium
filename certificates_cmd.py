import gspread
from typing import Optional
import os
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from draw_certificat import create_certificate
from keyboard import keyboard_paid_courses
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.types import FSInputFile
import asyncio
from states import CertificateStates


def authorize_google_sheets() -> gspread.client.Client:
    """
    Функция для авторизации в Google Sheets.

    :return: Авторизованный клиент для работы с Google Sheets.
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("crenditails.json", scope)
    client = gspread.authorize(creds)
    return client


def find_data(sheet: gspread.Worksheet, search_value: str) -> Optional[dict]:
    """
    Функция для поиска данных в таблице.

    :param sheet: Лист Google Sheets.
    :param search_value: Значение для поиска в таблице.
    :return: Найденная строка в виде словаря или None, если данные не найдены.
    """
    all_records = sheet.get_all_records()
    for row in all_records:
        if search_value in row.values():
            return row
    return None


async def get_certificates_cmd(message: types.Message, state: FSMContext):
    """
    Функция для запроса ФИО у пользователя.

    :param message: Сообщение от пользователя.
    :param state: Текущее состояние FSMContext.
    """
    await message.answer("Пожалуйста, введите ваши ФИО для поиска сертификата:")
    await state.set_state(CertificateStates.waiting_for_name)


async def process_name(message: types.Message, state: FSMContext):
    """
    Поиск сертификатов по ФИО.

    :param message: Сообщение от пользователя, содержащее ФИО.
    :param state: Текущее состояние FSMContext.
    """
    user_name = message.text
    sheet = authorize_google_sheets().open("test").sheet1
    found_row = find_data(sheet, user_name)

    if found_row:
        certificate_path = f'certificates/{user_name.replace(" ", "_")}_certificate.jpg'
        if not os.path.exists(certificate_path):
            create_certificate(user_name, found_row['former group'], datetime.now().strftime("%d.%m.%Y"))

        if os.path.exists(certificate_path):
            await message.answer_photo(FSInputFile(certificate_path), caption="Ваш сертификат готов!",
                                       reply_markup=keyboard_paid_courses)
            await asyncio.sleep(5)  # Ожидаем 5 секунд перед удалением
            os.remove(certificate_path)  # Удаляем сертификат
        else:
            await message.answer("Не удалось создать сертификат.", reply_markup=keyboard_paid_courses)
    else:
        await message.answer("Сертификат не найден.", reply_markup=keyboard_paid_courses)

    await state.clear()
