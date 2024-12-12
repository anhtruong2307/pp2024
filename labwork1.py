class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    # Input functions
    def input_number_of_students(self):
        return int(input("Enter number of students in the class: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        self.students.append(Student(student_id, name, dob))

    def input_number_of_courses(self):
        return int(input("Enter number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        self.courses.append(Course(course_id, name))

    def select_course_and_input_marks(self):
        print("Available courses:")
        for idx, course in enumerate(self.courses):
            print(f"{idx + 1}. {course.name} (ID: {course.course_id})")
        
        course_index = int(input("Select a course by number: ")) - 1
        if course_index < 0 or course_index >= len(self.courses):
            print("Invalid course selection!")
            return

        selected_course = self.courses[course_index]
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.student_id}): "))
            student.marks[selected_course.course_id] = mark

    # Listing functions
    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID: {student.student_id}, Name: {student.name}, DOB: {student.dob}")

    def show_student_marks_for_course(self):
        print("Available courses:")
        for idx, course in enumerate(self.courses):
            print(f"{idx + 1}. {course.name} (ID: {course.course_id})")

        course_index = int(input("Select a course by number: ")) - 1
        if course_index < 0 or course_index >= len(self.courses):
            print("Invalid course selection!")
            return

        selected_course = self.courses[course_index]
        print(f"Marks for course: {selected_course.name}")
        for student in self.students:
            mark = student.marks.get(selected_course.course_id, "N/A")
            print(f"{student.name} (ID: {student.student_id}): {mark}")

# Main program
if __name__ == "__main__":
    school_system = SchoolSystem()

    # Input number of students and their details
    num_students = school_system.input_number_of_students()
    for _ in range(num_students):
        school_system.input_student_information()

    # Input number of courses and their details
    num_courses = school_system.input_number_of_courses()
    for _ in range(num_courses):
        school_system.input_course_information()

    while True:
        print("\nMenu:")
        print("1. List courses")
        print("2. List students")
        print("3. Input marks for a course")
        print("4. Show student marks for a course")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            school_system.list_courses()
        elif choice == 2:
            school_system.list_students()
        elif choice == 3:
            school_system.select_course_and_input_marks()
        elif choice == 4:
            school_system.show_student_marks_for_course()
        elif choice == 5:
            break
        else:
            print("Invalid choice, please try again!")
