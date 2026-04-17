import csv
from connect import get_connection  # предполагается, что у тебя есть такая функция


# Создание таблицы
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


# Вставка из CSV
def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()


# Вставка с консоли
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


# Обновление контакта
def update_contact():
    name = input("Enter name to update: ")
    choice = input("Update (1) name or (2) phone? ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, name)
        )
    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE name = %s",
            (new_phone, name)
        )

    conn.commit()
    cur.close()
    conn.close()


# Поиск с фильтрами
def query_contacts():
    print("1 - Show all")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose option: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s",
            ('%' + name + '%',)
        )

    elif choice == "3":
        prefix = input("Enter phone prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


# Удаление
def delete_contact():
    print("1 - Delete by name")
    print("2 - Delete by phone")

    choice = input("Choose option: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()


# Меню
def main():
    create_table()

    while True:
        print("\nPhoneBook Menu:")
        print("1 - Insert from CSV")
        print("2 - Insert from console")
        print("3 - Update contact")
        print("4 - Query contacts")
        print("5 - Delete contact")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contact_data.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()