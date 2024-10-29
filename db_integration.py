import gspread
from oauth2client.service_account import ServiceAccountCredentials
import psycopg2


def authorize_google_sheets():
    """
        Авторизует доступ к Google Sheets с использованием учетных данных из файла JSON.

        Returns:
            gspread.client.Client: Объект клиента gspread для работы с Google Sheets.
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("crenditails.json", scope)
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

    conn = psycopg2.connect(
        dbname="tgbot_quantarium_db",
        user="postgres_admin",
        password="postgres",
        host="localhost"
    )
    cursor = conn.cursor()

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

        print(
            f"Добавление: {fio_parent}, {number}, {email}, {selected_course}, {choosing_a_pair}, {fio_child}, {date_of_birth}, {address}, {school}, {class_name}, {shift_at_school}, {former_group}")

        cursor.execute("""
            INSERT INTO certificates (fio_parent, number, email, selected_course, choosing_a_pair, fio_child, date_of_birth, address, school, class, shift_at_school, former_group)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (number) DO NOTHING;
        """, (fio_parent, number, email, selected_course, choosing_a_pair, fio_child, date_of_birth, address, school,
              class_name, shift_at_school, former_group))

    conn.commit()
    cursor.close()
    conn.close()


update_database()
