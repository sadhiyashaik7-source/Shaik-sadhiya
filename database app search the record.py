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


def search_record_by_id(student_id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM student WHERE id = ?",
        (student_id,)
    )

    record = cursor.fetchone()
    conn.close()
    return record


def search_record_by_name(name):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM student WHERE name LIKE ?",
        ('%' + name + '%',)
    )

    records = cursor.fetchall()
    conn.close()
    return records


def main():
    create_table()

    while True:
        print("\n1. Insert Record")
        print("2. Search by ID")
        print("3. Search by Name")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter course: ")

            insert_record(name, age, course)
            print("Record inserted successfully!")

        elif choice == '2':
            student_id = int(input("Enter student ID to search: "))
            record = search_record_by_id(student_id)

            if record:
                print(
                    f"Record found: ID: {record[0]}, "
                    f"Name: {record[1]}, Age: {record[2]}, "
                    f"Course: {record[3]}"
                )
            else:
                print("No record found with that ID.")

        elif choice == '3':
            name = input("Enter student name to search: ")
            records = search_record_by_name(name)

            if records:
                print("Records found:")
                for record in records:
                    print(
                        f"ID: {record[0]}, Name: {record[1]}, "
                        f"Age: {record[2]}, Course: {record[3]}"
                    )
            else:
                print("No record found with that name.")

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()