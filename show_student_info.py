class ShowStudentInfo:
    def __init__(self, student_db):
        self.student_db = student_db

    def execute(self, student_id):
        return self.student_db.get(student_id)
