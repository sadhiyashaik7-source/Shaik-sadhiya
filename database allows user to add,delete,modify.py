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


def add_record(name, age, course):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    conn.close()
    print("Record added successfully!")


def delete_record(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM student WHERE id = ?",
        (student_id,)
    )

    if cursor.rowcount > 0:
        print("Record deleted successfully!")
    else:
        print("Record not found!")

    conn.commit()
    conn.close()


def update_record(student_id, name, age, course):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE student SET name = ?, age = ?, course = ? WHERE id = ?",
        (name, age, course, student_id)
    )

    if cursor.rowcount > 0:
        print("Record updated successfully!")
    else:
        print("Record not found!")

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
        print("No records found.")


def main():
    create_table()

    while True:
        print("\n----- Student Database Menu -----")
        print("1. Add Record")
        print("2. Display Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter course: ")
            add_record(name, age, course)

        elif choice == '2':
            display_records()

        elif choice == '3':
            student_id = int(
                input("Enter student ID to update: ")
            )
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            update_record(student_id, name, age, course)

        elif choice == '4':
            student_id = int(
                input("Enter student ID to delete: ")
            )
            delete_record(student_id)

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()