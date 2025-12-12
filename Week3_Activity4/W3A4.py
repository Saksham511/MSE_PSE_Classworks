# database project
# Author: Saksham Shrestha
# OOP project to create a college database (student, teacher, course)
# and show:
# 1) number of students in MSE800
# 2) list teachers teaching MSE801

import sqlite3

class Yoobee:
    def __init__(self, database_name):
        # Connect to SQLite database using connection and cursor directing as a pointer to database
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    # Create all required tables
    def _create_tables(self):
        # Create Course table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Course(
                CourseCode TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                credits INTEGER NOT NULL
            )
        """)

        # Create Student table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL
            )
        """)

        # Create Teacher table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Teacher(
                TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        # StudentCourse – many-to-many relation
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS StudentCourse(
                StudentID INTEGER,
                CourseCode TEXT,
                FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
                FOREIGN KEY(CourseCode) REFERENCES Course(CourseCode)
            )
        """)

        # TeacherCourse – many-to-many
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS TeacherCourse(
                TeacherID INTEGER,
                CourseCode TEXT,
                FOREIGN KEY(TeacherID) REFERENCES Teacher(TeacherID),
                FOREIGN KEY(CourseCode) REFERENCES Course(CourseCode)
            )
        """)

        self.connection.commit()

    def show_table(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        for row in self.cursor:
            print(row)

    def show_table(self):
        print("Student Table:")
        self.cursor.execute("SELECT * FROM Student")
        for row in self.cursor:
            print(row)

        self.cursor.execute("SELECT * FROM Teacher")
        print("Teacher Table:")
        for row in self.cursor:
            print(row)

        self.cursor.execute("SELECT * FROM Course")
        print("Course Table:")
        for row in self.cursor:
            print(row)

    # Add student into database
    def add_student(self, name, email, address):
        self.cursor.execute("INSERT INTO Student(name, email, address) VALUES (?, ?, ?)",
                            (name, email, address))
        self.connection.commit()

    # Add teacher into database
    def add_teacher(self, name, email):
        self.cursor.execute("INSERT INTO Teacher(name, email) VALUES (?, ?)",
                            (name, email))
        self.connection.commit()

    # Add course into database
    def add_course(self, CourseCode, title, description, credits):
        self.cursor.execute("INSERT INTO Course(CourseCode, title, description, credits)VALUES (?, ?, ?, ?)",
                            (CourseCode, title, description, credits))
        self.connection.commit()

    # Assign student to a course
    def assign_student_to_course(self, student_id, course_code):
        self.cursor.execute("""
            INSERT INTO StudentCourse(StudentID, CourseCode)
            VALUES (?, ?)
        """, (student_id, course_code))

        self.connection.commit()

    # Assign teacher to a course
    def assign_teacher_to_course(self, teacher_id, course_code):
        self.cursor.execute("""
            INSERT INTO TeacherCourse(TeacherID, CourseCode)
            VALUES (?, ?)
        """, (teacher_id, course_code))

        self.connection.commit()

    # Count students in a specific course
    def count_students_in_course(self, course_code):
        self.cursor.execute("""
            SELECT COUNT(*) 
            FROM StudentCourse 
            WHERE CourseCode = ?
        """, (course_code,))
        result = self.cursor.fetchone()[0]
        return result

    # List teachers teaching a course
    def get_teachers_for_course(self, course_code):
        self.cursor.execute("""
            SELECT Teacher.name
            FROM Teacher
            JOIN TeacherCourse ON Teacher.TeacherID = TeacherCourse.TeacherID
            WHERE TeacherCourse.CourseCode = ?
        """, (course_code,))

        return [row[0] for row in self.cursor.fetchall()]


def main():
    MSE_db = Yoobee('Details_of_MSE.db')
    MSE_db.show_table()
    print("Choose the operation you want to perform: ")
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Course")
    print("4. Show number of students studying MSE800")
    print("5. Show teacher names teaching MSE801")
    print("6. Assign Student to Course")
    print("7. Assign Teacher to Course")

    c = int(input("Enter your choice: "))

    match c:
        case 1:
            name = input("Enter student's name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            MSE_db.add_student(name, email, address)

        case 2:
            name = input("Enter teacher's name: ")
            email = input("Enter email: ")
            MSE_db.add_teacher(name, email)

        case 3:
            code = input("Enter Course Code: ")
            title = input("Enter title: ")
            desc = input("Enter description: ")
            credits = int(input("Enter credits: "))
            MSE_db.add_course(code, title, desc, credits)

        case 4:
            count = MSE_db.count_students_in_course("MSE800")
            print("Number of students in MSE800 =", count)

        case 5:
            teachers = MSE_db.get_teachers_for_course("MSE801")
            print("Teachers teaching MSE801:")
            for t in teachers:
                print(t)

        case 6:
            student_id = int(input("Enter Student ID to assign: "))
            course_code = input("Enter Course Code: ")
            MSE_db.assign_student_to_course(student_id, course_code)

        case 7:
            teacher_id = int(input("Enter Teacher ID to assign: "))
            course_code = input("Enter Course Code: ")
            MSE_db.assign_teacher_to_course(teacher_id, course_code)


if __name__ == '__main__':
    while True:
        main()
        input("Press any key to continue...")