import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="yel",
    user="postgres",
    password="erten2007"
)
cur = conn.cursor()

def search_pattern():
    pattern = input("Enter part of name or phone number: ")
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    results = cur.fetchall()
    if results:
        print("Results found:")
        for row in results:
            print(row)
    else:
        print("No matches found.")

def insert_or_update_user():
    name = input("Enter username: ")
    phone = input("Enter phone number (digits only): ")
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    conn.commit()
    print(f"User '{name}' inserted or updated.")

def insert_many_users():
    n = int(input("How many users do you want to add? "))
    user_list = []
    for i in range(n):
        name = input(f"User #{i+1} name: ")
        phone = input(f"User #{i+1} phone: ")
        user_list.append([name, phone])
    cur.execute("CALL insert_many_users(%s);", (user_list,))
    conn.commit()
    print("Bulk insert completed.")

def get_paginated():
    limit = int(input("How many records to display? "))
    offset = int(input("How many records to skip? "))
    cur.execute("SELECT * FROM get_paginated_data(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No data to display.")

def delete_user():
    ident = input("Enter username or phone number to delete: ")
    cur.execute("CALL delete_user(%s);", (ident,))
    conn.commit()
    print("User deleted (if found).")

def main_menu():
    while True:
        print("\nPhoneBook Menu:")
        print("1. Search by pattern")
        print("2. Insert or update user")
        print("3. Insert many users")
        print("4. View records with pagination")
        print("5. Delete user")
        print("0. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            search_pattern()
        elif choice == '2':
            insert_or_update_user()
        elif choice == '3':
            insert_many_users()
        elif choice == '4':
            get_paginated()
        elif choice == '5':
            delete_user()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

    cur.close()
    conn.close()

main_menu()