import sqlite3

class StudentRecords:
    def __init__(self, db_name="Student.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()   # ✅ FIXED
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Student(
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    def insert_data(self, name, score):
        for student_id in name:
            self.cursor.execute("""
            INSERT OR REPLACE INTO Student(student_id, student_name, score)
            VALUES (?, ?, ?)
            """, (student_id, name[student_id], score[student_id]))
        self.conn.commit()

    def get_top_three(self):
        self.cursor.execute("""
        SELECT student_id, student_name, score
        FROM Student
        ORDER BY score DESC
        LIMIT 3
        """)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


def main():
    student_name = {
        101: "Saksham",
        102: "Divya",
        103: "Suman",
        104: "Dipendra",
        105: "Sushil",
        106: "Bhaskar"
    }

    student_score = {
        101: 88,
        102: 70,
        103: 80,
        104: 50,
        105: 45,
        106: 30
    }

    student1 = StudentRecords()
    student1.insert_data(student_name, student_score)
    top_three = student1.get_top_three()
    print("The top three students are:", top_three)
    student1.close()


if __name__ == "__main__":
    main()
