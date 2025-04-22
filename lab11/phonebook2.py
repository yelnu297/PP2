import psycopg2
import json

# Подключение к базе
def connect():
    return psycopg2.connect(
        dbname="phonebookanu2",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

def search_by_pattern():
    pattern = input("Введите шаблон поиска (часть имени или номера): ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
            rows = cur.fetchall()
            for row in rows:
                print(row)

def insert_or_update_user():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
            conn.commit()
            print("Добавлено или обновлено.")

def insert_many_users():
    num = int(input("Сколько пользователей хотите добавить? "))
    users = []
    for _ in range(num):
        name = input("Имя: ")
        phone = input("Телефон: ")
        users.append({"name": name, "phone": phone})
    
    json_data = json.dumps(users)
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s)", (json_data,))
            conn.commit()
            print("Множественное добавление выполнено.")

def get_paginated_users():
    limit = int(input("Введите лимит: "))
    offset = int(input("Введите смещение (offset): "))
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
            rows = cur.fetchall()
            for row in rows:
                print(row)

def delete_by_name_or_phone():
    value = input("Введите имя или телефон для удаления: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_by_name_or_phone(%s)", (value,))
            conn.commit()
            print("Удалено.")

def menu():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Поиск по шаблону")
        print("2. Добавить или обновить одного пользователя")
        print("3. Добавить нескольких пользователей")
        print("4. Просмотр с пагинацией")
        print("5. Удалить по имени или телефону")
        print("6. Выход")
        
        choice = input("Выберите опцию (1-6): ")
        
        if choice == '1':
            search_by_pattern()
        elif choice == '2':
            insert_or_update_user()
        elif choice == '3':
            insert_many_users()
        elif choice == '4':
            get_paginated_users()
        elif choice == '5':
            delete_by_name_or_phone()
        elif choice == '6':
            print("Выход.")
            break
        else:
            print("Неверная опция, попробуйте снова.")

if __name__ == "__main__":
    menu()
