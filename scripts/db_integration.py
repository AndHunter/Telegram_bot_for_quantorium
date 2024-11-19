from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
import os
import gspread
import psycopg2

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


def authorize_google_sheets():
    """
        Авторизует доступ к Google Sheets с использованием учетных данных из файла JSON.

        Returns:
            gspread.client.Client: Объект клиента gspread для работы с Google Sheets.
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("../crenditails.json", scope)
    client = gspread.authorize(creds)
    return client


def update_database():
    """
        Обновляет базу данных, извлекая данные из Google Sheets и вставляя их в таблицу 'certificates'.

        Этот метод создает подключение к базе данных PostgreSQL, извлекает все записи из
        указанного листа Google Sheets и добавляет их в таблицу. Если номер уже существует,
        запись не добавляется.

        Returns:
            None
    """
    sheet = authorize_google_sheets().open("test").sheet1
    all_records = sheet.get_all_records()

    if not all_records:
        print("Нет записей в Google Sheets.")
        return

    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        cursor = conn.cursor()
        print("Успешное подключение к базе данных.")

        for row in all_records:
            fio_parent = row.get("fio parent")
            number = row.get("number")
            email = row.get("email")
            selected_course = row.get("selected course")
            choosing_a_pair = row.get("choosing a pair")
            fio_child = row.get("fio child")
            date_of_birth = row.get("date of birth")
            address = row.get("address")
            school = row.get("school")
            class_name = row.get("class")
            shift_at_school = row.get("shift at school")
            former_group = row.get("former group")
            end_date = row.get("end date")  # Новый столбец

            print(
                f"Добавление: {fio_parent}, {number}, {email}, {selected_course}, {choosing_a_pair}, {fio_child}, {date_of_birth}, {address}, {school}, {class_name}, {shift_at_school}, {former_group}, {end_date}"
            )

            cursor.execute("""
                INSERT INTO certificates (fio_parent, number, email, selected_course, choosing_a_pair, fio_child, date_of_birth, address, school, class, shift_at_school, former_group, end_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (number) DO NOTHING;
            """, (
                fio_parent, number, email, selected_course, choosing_a_pair, fio_child, date_of_birth, address, school,
                class_name, shift_at_school, former_group, end_date))

        conn.commit()
        print("Все записи успешно добавлены в базу данных.")
    except psycopg2.Error as e:
        print(f"Ошибка при работе с базой данных: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
            print("Подключение к базе данных закрыто.")


update_database()
