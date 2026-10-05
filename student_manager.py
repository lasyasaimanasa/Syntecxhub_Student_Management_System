import json
from student import Student


class StudentManager:

    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

                self.students = [
                    Student(
                        student["id"],
                        student["name"],
                        student["grade"]
                    )
                    for student in data
                ]

        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def save_students(self):
        data = [
            student.to_dict()
            for student in self.students
        ]

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_student(self, student_id, name, grade):

        for student in self.students:
            if student.student_id == student_id:
                return False

        student = Student(student_id, name, grade)

        self.students.append(student)
        self.save_students()

        return True

    def update_student(self, student_id, name, grade):

        for student in self.students:

            if student.student_id == student_id:
                student.name = name
                student.grade = grade

                self.save_students()

                return True

        return False

    def delete_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()

                return True

        return False

    def list_students(self):
        return self.students

    def search_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                return student

        return None