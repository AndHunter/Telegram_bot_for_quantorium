import gspread
from aiogram.fsm.context import FSMContext
from oauth2client.service_account import ServiceAccountCredentials
from aiogram import types

from keyboard import keyboard_paid_courses
from states import CertificateStates

def authorize_google_sheets():
    """Функция для авторизации в Google Sheets."""
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("test2-438807-eb153fcc37ff.json", scope)
    client = gspread.authorize(creds)
    return client

def find_data(sheet, search_value):
    """Функция для поиска данных в таблице."""
    all_records = sheet.get_all_records()
    for row in all_records:
        if search_value in row.values():
            return row
    return None
async def get_certificates_cmd(message: types.Message, state: FSMContext):
    """Функция для запроса ФИО у пользователя."""
    await message.answer("Пожалуйста, введите ваши ФИО для поиска сертификата:")
    await state.set_state(CertificateStates.waiting_for_name)


async def process_name(message: types.Message, state: FSMContext):
    """Обрабатываем введенные ФИО и ищем сертификаты."""
    user_name = message.text

    client = authorize_google_sheets()

    spreadsheet_name = "test"
    sheet = client.open(spreadsheet_name).sheet1
    found_row = find_data(sheet, user_name)

    if found_row:
        await message.answer(f"Найдена строка: {found_row}", reply_markup=keyboard_paid_courses)
    else:
        await message.answer("Сертификат не найден.", reply_markup=keyboard_paid_courses)

    await state.finish()
