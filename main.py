from student_manager import StudentManager


# -------------------- VALIDATION FUNCTIONS --------------------

def validate_student_id(student_id):
    if not student_id:
        return False

    if not student_id.startswith("S"):
        return False

    if not student_id[1:].isdigit():
        return False

    return True


def validate_name(name):
    if not name:
        return False

    if not all(char.isalpha() or char.isspace() for char in name):
        return False

    return True


def validate_grade(grade):
    valid_grades = ["A+", "A", "B+", "B", "C+", "C", "D", "F"]

    return grade in valid_grades


# -------------------- UTILITY FUNCTION --------------------

def pause():
    input("\nPress Enter to continue...")


# -------------------- MENU --------------------

def display_menu():
    print("\n" + "=" * 50)
    print("          STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. List All Students")
    print("5. Search Student")
    print("6. Exit")
    print("=" * 50)


# -------------------- MAIN PROGRAM --------------------

def main():

    manager = StudentManager()

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        # ==================================================
        # ADD STUDENT
        # ==================================================

        if choice == "1":

            print("\n--- ADD STUDENT ---")

            # Validate Student ID
            while True:

                student_id = input("Enter Student ID: ").strip()

                if not validate_student_id(student_id):
                    print("❌ Invalid Student ID.")
                    print(
                        "   Student ID must be in the format "
                        "S001, S002, etc."
                    )
                    continue

                if manager.search_student(student_id):
                    print("❌ Student ID already exists.")
                    print("   Please enter a different Student ID.")
                    continue

                break

            # Validate Student Name
            while True:

                name = input("Enter Student Name: ").strip()

                if not validate_name(name):
                    print("❌ Invalid name.")
                    print(
                        "   Name should contain only letters and spaces."
                    )
                    continue

                break

            # Validate Grade
            while True:

                grade = input("Enter Grade: ").strip().upper()

                if not validate_grade(grade):
                    print("❌ Invalid grade.")
                    print(
                        "   Valid grades: A+, A, B+, B, C+, C, D, F"
                    )
                    continue

                break

            # Add student
            if manager.add_student(student_id, name, grade):
                print("\n✅ Student added successfully.")
            else:
                print("\n❌ Unable to add student.")

            pause()

        # ==================================================
        # UPDATE STUDENT
        # ==================================================

        elif choice == "2":

            print("\n--- UPDATE STUDENT ---")

            # Validate Student ID
            while True:

                student_id = input("Enter Student ID: ").strip()

                if not validate_student_id(student_id):
                    print("❌ Invalid Student ID.")
                    print(
                        "   Student ID must be in the format "
                        "S001, S002, etc."
                    )
                    continue

                break

            # Check whether student exists
            student = manager.search_student(student_id)

            if not student:
                print("\n❌ Student not found.")
                pause()
                continue

            print("\nCurrent Student Details")
            print("-" * 30)
            print(f"ID    : {student.student_id}")
            print(f"Name  : {student.name}")
            print(f"Grade : {student.grade}")
            print("-" * 30)

            # Validate new name
            while True:

                name = input("Enter new name: ").strip()

                if not validate_name(name):
                    print("❌ Invalid name.")
                    print(
                        "   Name should contain only letters and spaces."
                    )
                    continue

                break

            # Validate new grade
            while True:

                grade = input("Enter new grade: ").strip().upper()

                if not validate_grade(grade):
                    print("❌ Invalid grade.")
                    print(
                        "   Valid grades: A+, A, B+, B, C+, C, D, F"
                    )
                    continue

                break

            # Update student
            if manager.update_student(student_id, name, grade):
                print("\n✅ Student updated successfully.")
            else:
                print("\n❌ Unable to update student.")

            pause()

        # ==================================================
        # DELETE STUDENT
        # ==================================================

        elif choice == "3":

            print("\n--- DELETE STUDENT ---")

            # Validate Student ID
            while True:

                student_id = input("Enter Student ID: ").strip()

                if not validate_student_id(student_id):
                    print("❌ Invalid Student ID.")
                    print(
                        "   Student ID must be in the format "
                        "S001, S002, etc."
                    )
                    continue

                break

            # Check whether student exists
            student = manager.search_student(student_id)

            if not student:
                print("\n❌ Student not found.")
                pause()
                continue

            print("\nStudent Found")
            print("-" * 30)
            print(f"ID    : {student.student_id}")
            print(f"Name  : {student.name}")
            print(f"Grade : {student.grade}")
            print("-" * 30)

            # Confirmation before deletion
            confirmation = input(
                "Are you sure you want to delete this student? (y/n): "
            ).strip().lower()

            if confirmation == "y":

                if manager.delete_student(student_id):
                    print("\n✅ Student deleted successfully.")
                else:
                    print("\n❌ Unable to delete student.")

            else:
                print("\nℹ️ Delete operation cancelled.")

            pause()

        # ==================================================
        # LIST ALL STUDENTS
        # ==================================================

        elif choice == "4":

            print("\n--- ALL STUDENTS ---")

            students = manager.list_students()

            if not students:

                print("No student records found.")

            else:

                print("-" * 50)

                print(
                    f"{'ID':<10}"
                    f"{'Name':<25}"
                    f"{'Grade':<10}"
                )

                print("-" * 50)

                for student in students:
                    student.display()

                print("-" * 50)

                print(f"Total Students: {len(students)}")

            pause()

        # ==================================================
        # SEARCH STUDENT
        # ==================================================

        elif choice == "5":

            print("\n--- SEARCH STUDENT ---")

            # Validate Student ID
            while True:

                student_id = input("Enter Student ID: ").strip()

                if not validate_student_id(student_id):
                    print("❌ Invalid Student ID.")
                    print(
                        "   Student ID must be in the format "
                        "S001, S002, etc."
                    )
                    continue

                break

            student = manager.search_student(student_id)

            if student:

                print("\nStudent Found")
                print("-" * 30)
                print(f"ID    : {student.student_id}")
                print(f"Name  : {student.name}")
                print(f"Grade : {student.grade}")
                print("-" * 30)

            else:

                print("\n❌ Student not found.")

            pause()

        # ==================================================
        # EXIT
        # ==================================================

        elif choice == "6":

            print("\nThank you for using Student Management System!")
            print("Goodbye! 👋")
            break

        # ==================================================
        # INVALID MENU OPTION
        # ==================================================

        else:

            print(
                "\n❌ Invalid choice. "
                "Please enter a number from 1 to 6."
            )

            pause()


# -------------------- PROGRAM START --------------------

if __name__ == "__main__":
    main()