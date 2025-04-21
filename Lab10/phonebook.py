import psycopg2
import csv

try:
    conn = psycopg2.connect(
        dbname="yel",
        user="postgres",
        password="erten2007",  
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()  
except Exception as e:
    print("Connection error:", e)
    exit()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()

def insert_from_csv(filename):
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 2:
                    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
        print("Data inserted from CSV successfully.")
    except Exception as e:
        print("Error reading CSV:", e)

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("User added.")

def update_user():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("User updated.")

def search_user():
    keyword = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyword}%', f'%{keyword}%'))
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_user():
    keyword = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (keyword, keyword))
    conn.commit()
    print("User deleted.")

def select_all():
    try:
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        if not rows:
            print("The phonebook is empty.")
        else:
            print("\nAll entries in phonebook:")
            for row in rows:
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    except Exception as e:
        print("Error while fetching data:", e)

def main():
    while True:
        print("\n1 - Insert from CSV")
        print("2 - Add manually")
        print("3 - Update record")
        print("4 - Search user")
        print("5 - Delete user")
        print("6 - Select all")
        print("0 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            filename = "W3/Lab10/contacts.csv"
            insert_from_csv(filename)
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_user()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            select_all()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

    cur.close()
    conn.close()

main()