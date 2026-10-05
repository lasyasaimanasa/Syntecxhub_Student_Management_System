class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }

    def display(self):
        print(
            f"{self.student_id:<10}"
            f"{self.name:<25}"
            f"{self.grade:<10}"
        )