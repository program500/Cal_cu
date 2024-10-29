import json

class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address
    
    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject: str, grade: str):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print(f"Student Information: Name: {self.name}, ID: {self.student_id}, Age: {self.age}, Address: {self.address}, Enrolled Courses: {', '.join(self.courses)}, Grades: {self.grades}")


class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Information: Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join([student.name for student in self.students])}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name: str, age: int, address: str, student_id: str):
        student = Student(name, age, address, student_id)
        self.students[student_id] = student 
        print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name: str, course_code: str, instructor: str):
        course = Course(course_name, course_code, instructor)
        self.courses[course_code] = course
        print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id: str, course_code: str):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Error: Student ID or Course Code does not exist.")

    def add_grade_for_student(self, student_id: str, course_code: str, grade: str):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            if course_code in student.courses:
                student.add_grade(course_code, grade)
                print(f"Grade {grade} added for {student.name} in {self.courses[course_code].course_name}.")
            else:
                print("Error: Student is not enrolled in this course.")
        else:
            print("Error: Student ID or Course Code does not exist.")

    def display_student_details(self, student_id: str):
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print("Error: Student ID does not exist.")

    def display_course_details(self, course_code: str):
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print("Error: Course Code does not exist.")

    def save_data(self, filename: str):
        data = {
            'students': {student_id: {
                'name': student.name,
                'age': student.age,
                'address': student.address,
                'grades': student.grades,
                'courses': student.courses
            } for student_id, student in self.students.items()},
            'courses': {course_code: {
                'course_name': course.course_name,
                'instructor': course.instructor,
                'students': [student.student_id for student in course.students]
            } for course_code, course in self.courses.items()}
        }
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for student_id, student_data in data['students'].items():
                student = Student(student_data['name'], student_data['age'], student_data['address'], student_id)
                student.grades = student_data['grades']
                student.courses = student_data['courses']
                self.students[student_id] = student
            
            for course_code, course_data in data['courses'].items():
                course = Course(course_data['course_name'], course_code, course_data['instructor'])
                self.courses[course_code] = course
                for student_id in course_data['students']:
                    if student_id in self.students:
                        course.add_student(self.students[student_id])
                        self.students[student_id].enroll_course(course.course_name)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Error: File not found.")


def main():
    system = StudentManagementSystem()
    while True:
        print("\n====Student Management System====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        option = input("Select Option: ")

        if option == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            system.add_student(name, age, address, student_id)

        elif option == '2':
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            system.add_course(course_name, course_code, instructor)

        elif option == '3':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            system.enroll_student_in_course(student_id, course_code)

        elif option == '4':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            system.add_grade_for_student(student_id, course_code, grade)

        elif option == '5':
            student_id = input("Enter Student ID: ")
            system.display_student_details(student_id)

        elif option == '6':
            course_code = input("Enter Course Code: ")
            system.display_course_details(course_code)

        elif option == '7':
            filename = input("Enter filename to save data: ")
            system.save_data(filename)

        elif option == '8':
            filename = input("Enter filename to load data: ")
            system.load_data(filename)

        elif option == '0':
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
