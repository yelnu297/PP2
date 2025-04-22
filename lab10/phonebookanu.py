# -*- coding: utf-8 -*-
import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebookanu",  # Имя базы данных
        user="postgres",          # Имя пользователя
        password="123456"         # Пароль
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(15)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # пропускаем заголовок
            for row in reader:
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Данные успешно импортированы из CSV.")
    except Exception as e:
        print("Ошибка при импорте из CSV:", str(e))
    cur.close()
    conn.close()

def insert_from_input():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Запись добавлена.")

def update_entry():
    old_name = input("Введите имя для обновления: ")
    new_name = input("Новое имя (оставьте пустым, чтобы не изменять): ")
    new_phone = input("Новый номер телефона (оставьте пустым, чтобы не изменять): ")

    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()
    print("Запись обновлена.")

def search():
    filter_type = input("Поиск по (имя/телефон): ").strip()
    value = input("Введите значение: ")
    conn = connect()
    cur = conn.cursor()
    if filter_type == "имя":
        cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (value,))
    elif filter_type == "телефон":
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (value,))
    else:
        print("Неверный тип фильтра.")
        return
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("Записи не найдены.")
    cur.close()
    conn.close()

def delete_entry():
    value = input("Введите имя или номер телефона для удаления: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE first_name = %s OR phone = %s", (value, value))
    conn.commit()
    cur.close()
    conn.close()
    print("Запись удалена.")

def menu():
    create_table()
    while True:
        print("\n=== МЕНЮ ТЕЛЕФОННОГО СПРАВОЧНИКА ===")
        print("1. Импортировать из CSV")
        print("2. Добавить вручную")
        print("3. Обновить запись")
        print("4. Поиск")
        print("5. Удалить запись")
        print("6. Выход")
        print("=============================")

        choice = input("Выберите опцию (1-6): ")

        if choice == "1":
            filename = input("Введите путь к CSV файлу: ")
            insert_from_csv(filename)
        elif choice == "2":
            insert_from_input()
        elif choice == "3":
            update_entry()
        elif choice == "4":
            search()
        elif choice == "5":
            delete_entry()
        elif choice == "6":
            print("До свидания!")
            break
        else:
            print("Неверная опция, попробуйте снова.")

if __name__ == "__main__":
    menu()
