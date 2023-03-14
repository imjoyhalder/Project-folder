class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

class ClassManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                print(f"Name: {student.name}")
                print(f"Grade: {student.grade}")
                print(f"Age: {student.age}")

    def delete_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                self.students.remove(student)
                print(f"Deleted student: {student_name}")

    def view_all_students(self):
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Grade: {student.grade}")
            print(f"Age: {student.age}")

# Example usage:
cms = ClassManagementSystem()

student1 = Student("Alice", "A", 15)
student2 = Student("Bob", "B", 16)
student3 = Student("Charlie", "C", 17)

cms.add_student(student1)
cms.add_student(student2)
cms.add_student(student3)

print("Viewing all students:")
cms.view_all_students()

print("\nViewing a single student:")
cms.view_student("Bob")

print("\nDeleting a student:")
cms.delete_student("Charlie")

print("\nViewing all students after deletion:")
cms.view_all_students()
