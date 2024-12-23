def input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    print("\nOptions:")
    print("1. Input number of students in a class")
    print("2. Input student information")
    print("3. Input number of courses")
    print("4. Input course information")
    print("5. Select a course and input marks for students")
    print("6. List courses")
    print("7. List students")
    print("8. Show student marks for a given course")
    print("9. Exit")

class System:
    def __init__(self):
        self.students_list = []
        self.courses_list = []

def input_students(students_list):
    while True:
        try:
            num_students = input_number("Enter the number of students: ")
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break

    for _ in range(num_students):
        student_info = input_student_info()
        students_list.append(student_info)

class Student:
    def __init__(self, num_students, student_id, name, dob):
        self.num_students = num_students
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student D.o.B: ")
    return {"ID": student_id, "Name": name, "D.O.B": dob, "Marks": {}}

class Course:
    def __init__(self, num_courses, course_id, name):
        self.num_courses = num_courses
        self.course_id = course_id
        self.name = name

def input_courses(courses_list):
    while True:
        try:
            num_courses = input_number("Enter the number of courses: ")
        except ValueError:
            print("Please enter a valid number.")
            continue
        else:
            break
    for _ in range(num_courses):
        course_info = input_course_info()
        courses_list.append(course_info)

def input_course_info():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return {"ID": course_id, "Name": name}

def select_course_input_marks(students_list, courses_list):
    list_courses(courses_list)
    course_id = input("Select a course ID: ")
    
    selected_course = next((course for course in courses_list if course['ID'] == course_id), None)
    
    if selected_course:
        for student in students_list:
            select_course_input_marks_for_student(student, selected_course)
    else:
        print("Course not found.")

def select_course_input_marks_for_student(student, course):
    marks = float(input(f"Enter marks for {student['Name']} in {course['Name']}: "))
    student['Marks'][course['ID']] = marks

def list_courses(courses_list):
    print("\nList of Courses:")
    for course in courses_list:
        print(f"Course ID: {course['ID']}, Course Name: {course['Name']}")

def list_students(students_list):
    print("\nList of Students:")
    for student in students_list:
        print(f"Student ID: {student['ID']}, Name: {student['Name']}")

def show_student_marks_for_course(students_list, courses_list):
    list_students(students_list)
    student_id = input("Select a student ID: ")
    
    selected_student = next((student for student in students_list if student['ID'] == student_id), None)
    
    if selected_student:
        list_courses(courses_list)
        course_id = input("Select a course ID: ")
        
        if course_id in selected_student['Marks']:
            print(f"\nMarks for {selected_student['Name']} in Course {course_id}: {selected_student['Marks'][course_id]}")
        else:
            print(f"\nNo marks available for {selected_student['Name']} in Course {course_id}")
    else:
        print("Student not found.")

#Main
students_list = []
courses_list = []

while True:
    display_menu()
    choice = input_number("Enter your choice (1-9): ")

    if choice == 1:
        input_students(students_list)
    elif choice == 2:
        students_list.append(input_student_info())
    elif choice == 3:
        input_courses(courses_list)
    elif choice == 4:
        courses_list.append(input_course_info())
    elif choice == 5:
        select_course_input_marks(students_list, courses_list)
    elif choice == 6:
        list_courses(courses_list)
    elif choice == 7:
        list_students(students_list)
    elif choice == 8:
        show_student_marks_for_course(students_list, courses_list)
    elif choice == 9:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    sms = System()
    sms.run()