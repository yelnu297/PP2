import psycopg2
import re

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="lab11",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255),
            phone VARCHAR(20)
        );
    """)
    conn.commit()


def search_pattern(pattern):
    cur.execute("""
        SELECT * FROM phonebook
        WHERE username ILIKE %s OR phone ILIKE %s;
    """, (f'%{pattern}%', f'%{pattern}%'))
    rows = cur.fetchall()
    print("Results:")
    for row in rows:
        print(row)


def insert_or_update_user(username, phone):
    cur.execute("SELECT * FROM phonebook WHERE username = %s;", (username,))
    if cur.fetchone():
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s;", (phone, username))
        print("Phone updated.")
    else:
        cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s);", (username, phone))
        print("User inserted.")
    conn.commit()


def insert_many_users(user_list):
    invalids = []
    for username, phone in user_list:
        if re.fullmatch(r'\d{10,}', phone):
            cur.execute("SELECT * FROM phonebook WHERE username = %s;", (username,))
            if cur.fetchone():
                cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s;", (phone, username))
            else:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s);", (username, phone))
        else:
            invalids.append((username, phone))
    conn.commit()
    print("Invalid entries:", invalids)


def get_page(limit, offset):
    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s;", (limit, offset))
    rows = cur.fetchall()
    print("Page results:")
    for row in rows:
        print(row)


def delete_user(username=None, phone=None):
    if username:
        cur.execute("DELETE FROM phonebook WHERE username = %s;", (username,))
    if phone:
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
    conn.commit()
    print("User deleted if found.")


def main_menu():
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Search by pattern")
        print("2. Insert or update user")
        print("3. Insert many users")
        print("4. Get paginated data")
        print("5. Delete by username or phone")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            pattern = input("Enter pattern to search: ")
            search_pattern(pattern)

        elif choice == "2":
            username = input("Enter username: ")
            phone = input("Enter phone: ")
            insert_or_update_user(username, phone)

        elif choice == "3":
            n = int(input("How many users to insert? "))
            users = []
            for _ in range(n):
                name = input("  Name: ")
                phone = input("  Phone: ")
                users.append((name, phone))
            insert_many_users(users)

        elif choice == "4":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            get_page(limit, offset)

        elif choice == "5":
            uname = input("Enter username (or leave empty): ")
            phone = input("Enter phone (or leave empty): ")
            delete_user(uname if uname else None, phone if phone else None)

        elif choice == "0":
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    try:
        main_menu()
    finally:
        cur.close()
        conn.close()