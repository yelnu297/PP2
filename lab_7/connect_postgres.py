# -*- coding: utf-8 -*-

import psycopg2

try:
    # Подключаемся к базе
    connection = psycopg2.connect(
        host="localhost",       # адрес сервера (обычно localhost)
        port="5432",            # порт PostgreSQL (обычно 5432)
        database="имя_базы",    # замени на имя своей базы
        user="имя_пользователя",# замени на своего пользователя
        password="пароль"       # и пароль
    )

    connection.set_client_encoding('UTF8')

    print("✅ Успешное подключение к базе данных!")

    # Создаем "курсор" — он помогает выполнять SQL-запросы
    cursor = connection.cursor()

    # Пример запроса — получим версию PostgreSQL
    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    print("Версия базы данных:", result)

    # Закрываем соединение
    cursor.close()
    connection.close()

except Exception as e:
    print("❌ Ошибка:", e)
