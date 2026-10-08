from students import StudentManager


def main():
    manager = StudentManager()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            course = input("Enter course: ")

            manager.add_student(name, age, course)

        elif choice == "2":
            manager.view_students()

        elif choice == "3":
            name = input("Enter student name to search: ")
            manager.search_student(name)

        elif choice == "4":
            name = input("Enter student name to delete: ")
            manager.delete_student(name)

        elif choice == "5":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()