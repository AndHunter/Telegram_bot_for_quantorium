from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")


async def view_database():
    """Получает данные из базы данных и форматирует их для отображения."""
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM certificates;")
    rows = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    data = " | ".join(column_names) + "\n" + "-" * 40 + "\n"

    for row in rows:
        data += " | ".join(map(str, row)) + "\n"

    cursor.close()
    conn.close()

    return data
