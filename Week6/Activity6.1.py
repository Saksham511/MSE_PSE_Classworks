class StudentRecords:
    def __init__(self,name,score):
        self.students=name
        self.scores=score
        
    def get_passed_students(self):
        passed_students={}
        for student_id in self.students:
            if self.scores[student_id]>=50:
                passed_students[student_id]={"name":self.students[student_id],
                                             "score":self.scores[student_id]}
        return passed_students

def main():
    student_name={101: "Saksham",
                  102: "Divya",
                  103: "Suman",
                  104: "Dipendra",
                  105: "Sushil",
                  106: "Bhaskar"}
    student_score={101: 88,
                   102: 70,
                   103: 80,
                   104: 50,
                   105: 45,
                   106: 30}
    student1=StudentRecords(student_name,student_score)
    passed= student1.get_passed_students()
    print("The passed students who scored above 50 are",passed)

if __name__ == "__main__":
    main()