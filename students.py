class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, name, age, course):
        student = {
            "name": name,
            "age": age,
            "course": course
        }

        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n===== STUDENTS =====")

        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student['name']} | Age: {student['age']} | Course: {student['course']}")

    def search_student(self, name):
        for student in self.students:
            if student["name"].lower() == name.lower():
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                return

        print("Student not found.")

    def delete_student(self, name):
        for student in self.students:
            if student["name"].lower() == name.lower():
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")