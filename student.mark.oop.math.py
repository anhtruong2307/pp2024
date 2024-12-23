import math
import numpy as np
import curses

def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def display_menu(stdscr):
    stdscr.clear()
    menu = [
        "1. Input number of students in a class",
        "2. Input student information",
        "3. Input number of courses",
        "4. Input course information",
        "5. Select a course and input marks for students",
        "6. List courses",
        "7. List students",
        "8. Show student marks for a given course",
        "9. Calculate and display average GPA",
        "10. Exit"
    ]
    stdscr.addstr("Options:\n")
    for line in menu:
        stdscr.addstr(line + "\n")
    stdscr.refresh()

# Define classes and core functions
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}  # Course ID: Marks
        self.gpa = 0.0

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

def calculate_gpa(student, courses):
    total_credits = 0
    weighted_sum = 0
    for course_id, mark in student.marks.items():
        course = next((course for course in courses if course.course_id == course_id), None)
        if course:
            total_credits += course.credits
            weighted_sum += mark * course.credits
    if total_credits > 0:
        student.gpa = round(weighted_sum / total_credits, 2)
    else:
        student.gpa = 0.0

def select_course_input_marks(students, courses):
    list_courses(courses)
    course_id = input("Select a course ID: ")
    selected_course = next((course for course in courses if course.course_id == course_id), None)
    if selected_course:
        for student in students:
            while True:
                try:
                    marks = float(input(f"Enter marks for {student.name} in {selected_course.name}: "))
                    marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
                    student.marks[course_id] = marks
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
    else:
        print("Course not found.")

# Main Program
def main(stdscr):
    students = []
    courses = []

    while True:
        display_menu(stdscr)
        stdscr.addstr("\nEnter your choice (1-10): ")
        choice = int(stdscr.getkey())
        if choice == 1:
            num_students = input_number("Enter the number of students: ")
            for _ in range(num_students):
                student = Student(
                    input("Enter student ID: "),
                    input("Enter student name: "),
                    input("Enter student D.o.B: ")
                )
                students.append(student)
        elif choice == 3:
            num_courses = input_number("Enter the number of courses: ")
            for _ in range(num_courses):
                course = Course(
                    input("Enter course ID: "),
                    input("Enter course name: "),
                    input_number("Enter course credits: ")
                )
                courses.append(course)
        elif choice == 5:
            select_course_input_marks(students, courses)
        elif choice == 9:
            for student in students:
                calculate_gpa(student, courses)
            students.sort(key=lambda x: x.gpa, reverse=True)
            print("\nStudents sorted by GPA:")
            for student in students:
                print(f"{student.name} (ID: {student.student_id}): GPA = {student.gpa}")
        elif choice == 10:
            stdscr.addstr("Exiting the program. Goodbye!\n")
            break
        else:
            stdscr.addstr("Invalid choice. Please enter a valid option.\n")
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
