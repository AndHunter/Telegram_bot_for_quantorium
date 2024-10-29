import psycopg2


def view_database():
    # Подключение к базе данных
    conn = psycopg2.connect(
        dbname="tgbot_quantarium_db",
        user="postgres_admin",
        password="postgres",
        host="localhost"
    )
    cursor = conn.cursor()

    # Выполнить запрос для получения всех данных из таблицы certificates
    cursor.execute("SELECT * FROM certificates;")
    rows = cursor.fetchall()

    # Получение названий столбцов для более удобного отображения
    column_names = [desc[0] for desc in cursor.description]
    print(" | ".join(column_names))
    print("-" * 40)

    # Вывод данных построчно
    for row in rows:
        print(" | ".join(map(str, row)))

    # Закрытие курсора и соединения
    cursor.close()
    conn.close()


# Вызов функции
view_database()
