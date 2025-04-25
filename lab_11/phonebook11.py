import psycopg2


def connect():
    return psycopg2.connect(
        database="phonebook_11",
        user="postgres",
        password="Ggg123ddd",
        host="localhost",
        port="5432"
    )


def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    results = cur.fetchall()
    if results:
        print("\nНайдено:")
        for row in results:
            print(f"Имя: {row[0]}, Телефон: {row[1]}")
    else:
        print("Совпадений не найдено.")
    cur.close()
    conn.close()


def insert_or_update_user(first_name, phone_number):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)",
                (first_name, phone_number))
    conn.commit()
    cur.close()
    conn.close()


def insert_many_users(names, phones):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT insert_many_users(%s::text[], %s::text[])",
                (names, phones))
    incorrect = cur.fetchone()[0]

    if incorrect:
        print("Неверные данные:")
        for entry in incorrect:
            print(" -", entry)
    else:
        print("Все пользователи успешно добавлены.")

    conn.commit()
    cur.close()
    conn.close()


def get_paginated_users(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    cur.close()
    conn.close()


def delete_by_name_or_phone(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_by_name_or_phone(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Удаление выполнено.")


def show_full_phonebook():
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, first_name, phone_number FROM phonebook_11 ORDER BY id")
    rows = cur.fetchall()
    if rows:
        print("\n=== Полная таблица PhoneBook ===")
        for row in rows:
            print(f"ID: {row[0]}, Имя: {row[1]}, Телефон: {row[2]}")
    else:
        print("Таблица пуста.")
    cur.close()
    conn.close()


def main_menu():
    while True:
        print("\n==== МЕНЮ ====")
        print("1. Поиск по шаблону")
        print("2. Добавить/обновить пользователя")
        print("3. Массовая вставка")
        print("4. Показать пользователей с лимитом")
        print("5. Удалить по имени или телефону")
        print("6. Показать всю таблицу")
        print("0. Выйти")

        choice = input("Выбери действие: ")

        if choice == "1":
            pattern = input("Введите шаблон для поиска: ")
            search_by_pattern(pattern)

        elif choice == "2":
            first = input("Enter first name: ")
            phone = input("Enter phone number: ")
            insert_or_update_user(first, last, phone)

        elif choice == "3":
            count = int(input("Сколько пользователей вставить? "))
            names = []
            phones = []
            for i in range(count):
                print(f"Пользователь #{i+1}")
                names.append(input("  Имя: "))
                phones.append(input("  Телефон: "))
            insert_many_users(names, phones)

        elif choice == "4":
            limit = int(input("Сколько показать: "))
            offset = int(input("С какого смещения начать: "))
            get_paginated_users(limit, offset)

        elif choice == "5":
            name = input("Имя для удаления (или пусто): ")
            phone = input("Телефон для удаления (или пусто): ")
            delete_by_name_or_phone(name or None, phone or None)

        elif choice == "0":
            print("Выход...")
            break
        elif choice == "6":
            show_full_phonebook()
        else:
            print("Неверный выбор. Попробуй снова.")


if __name__ == "__main__":
    main_menu()
