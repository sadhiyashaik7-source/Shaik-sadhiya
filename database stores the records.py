import sqlite3

def create_table():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def insert_record(name, age, course):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    conn.close()


def display_records():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student")
    records = cursor.fetchall()
    conn.close()

    if records:
        print("\nStudent Records:")
        for row in records:
            print(
                f"ID: {row[0]}, Name: {row[1]}, "
                f"Age: {row[2]}, Course: {row[3]}"
            )
    else:
        print("\nNo records found.")


def main():
    create_table()

    while True:
        print("\n1. Insert Record")
        print("2. Display Records")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")

            insert_record(name, age, course)
            print("Record inserted successfully.")

        elif choice == '2':
            display_records()

        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()