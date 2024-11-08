import psycopg2


async def view_database():
    """Получает данные из базы данных и форматирует их для отображения."""
    conn = psycopg2.connect(
        dbname="tgbot_quantarium_db",
        user="postgres_admin",
        password="postgres",
        host="localhost"
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
