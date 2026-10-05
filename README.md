# Student Management System

A Python-based command-line Student Management System developed using Object-Oriented Programming, file handling, input validation, and JSON data persistence.

This project was developed as part of the Syntecxhub internship project requirements.

---

## Project Overview

The Student Management System is a command-line application that allows users to manage student records efficiently.

The application provides functionality to:

- Add students
- Update student records
- Delete student records
- Display all students
- Search for students
- Store student information permanently using JSON

---

## Features

- Add new student records
- Update existing student records
- Delete student records
- Display all student records
- Search students by Student ID
- Unique Student ID validation
- Student name validation
- Grade validation
- Delete confirmation
- JSON-based data persistence
- Formatted command-line interface
- Object-Oriented Programming structure
- File handling
- CRUD operations

---

## Technologies Used

- Python 3
- JSON
- Object-Oriented Programming (OOP)
- File Handling
- Command Line Interface (CLI)
- Visual Studio Code
- Git
- GitHub

---

## Project Structure

The project contains the following files:

- main.py - Main application and menu interface
- student.py - Contains the Student class
- student_manager.py - Handles student management operations
- students.json - Stores student records
- README.md - Project documentation
- .gitignore - Specifies files ignored by Git

---

## Object-Oriented Design

The project uses two main classes.

### Student Class

The Student class represents an individual student.

Each student contains:

- Student ID
- Student Name
- Grade

The class also provides methods to:

- Convert student information into dictionary format
- Display student details

### StudentManager Class

The StudentManager class manages all student records.

It provides methods for:

- Adding students
- Updating students
- Deleting students
- Searching students
- Listing students
- Loading student data
- Saving student data

---

## How to Run the Project

### Step 1: Clone the Repository

Use the following command:

git clone YOUR_GITHUB_REPOSITORY_URL

### Step 2: Open the Project Folder

Use:

cd Syntecxhub_Student_Management_System

### Step 3: Run the Application

Use:

python main.py

---

## Application Menu

When the application starts, the following menu is displayed:

1. Add Student
2. Update Student
3. Delete Student
4. List All Students
5. Search Student
6. Exit

---

## Input Validation

The application validates student information before storing it.

### Student ID Validation

Student IDs must follow the format:

S001
S002
S003

Student IDs must:

- Start with the letter S
- Contain numbers after S
- Be unique

### Student Name Validation

Student names can contain:

- Letters
- Spaces

Numbers and special characters are not accepted.

### Grade Validation

The supported grades are:

- A+
- A
- B+
- B
- C+
- C
- D
- F

---

## Data Persistence

Student records are stored in the students.json file.

Example student records include:

- S001 - Lasya - A
- S002 - Ananya - B+
- S003 - Rahul - A+
- S004 - Priya - B
- S005 - Arjun - C+

The application automatically loads existing student records when it starts.

Whenever a student is:

- Added
- Updated
- Deleted

the changes are automatically saved to the JSON file.

This allows student data to remain available even after closing and reopening the application.

---

## CRUD Operations

The application supports all major CRUD operations.

### Create

Add a new student record.

### Read

Display and search student records.

### Update

Modify an existing student's name and grade.

### Delete

Remove an existing student record after confirmation.

---

## Internship Requirements Covered

This project demonstrates:

- Python programming
- CLI application development
- Object-Oriented Programming
- Classes and objects
- Constructors
- Methods
- File input and output
- JSON data persistence
- Input validation
- CRUD operations
- Formatted console output

---

## Future Enhancements

The project can be extended with:

- Student attendance management
- Subject-wise marks
- GPA calculation
- Search by student name
- Sorting students by grade
- CSV export
- SQLite database integration
- Graphical User Interface (GUI)
- Student login system

---

## Author

Lasya Sai Manasa

Syntecxhub Internship Project