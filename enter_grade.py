class EnterGrade:
    def __init__(self, student_db):
        self.student_db = student_db

    def execute(self, student_id, grade):
        if student_id in self.student_db:
            self.student_db[student_id]['grade'] = grade
            return True
        else:
            return False
