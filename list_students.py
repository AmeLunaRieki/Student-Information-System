class ListStudents:
    def __init__(self, student_db):
        self.student_db = student_db

    def execute(self):
        return self.student_db.values()
