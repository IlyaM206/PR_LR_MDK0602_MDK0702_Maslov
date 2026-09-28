import mysql.connector
from mysql.connector import Error
import time

DB_HOST = '5.183.188.132'
DB_PORT = 3306
DB_USER = 'db_vgu_student'
DB_PASSWORD = 'thasrCt3pKYWAYcK'
DB_NAME = 'db_vgu_test3'


def create_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if connection.is_connected():
            print("Подключение к БД установлено")
            return connection
    except Error as e:
        print(f"Ошибка подключения: {e}")
        return None


def fetch_data(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM category_description LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Ошибка выполнения запроса: {e}")
    finally:
        if cursor:
            cursor.close()


def main():
    max_retries = 3
    retry_delay = 5
    connection = None

    for attempt in range(max_retries):
        print(f"Попытка подключения {attempt + 1} из {max_retries}...")
        connection = create_connection()
        if connection:
            break
        time.sleep(retry_delay)

    if not connection:
        print("Не удалось подключиться к БД. Завершение работы.")
        return

    fetch_data(connection)

    connection.close()
    print("Соединение закрыто")


if __name__ == "__main__":
    main()