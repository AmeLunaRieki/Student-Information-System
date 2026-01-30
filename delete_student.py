class DeleteStudent:
    def __init__(self, student_db):
        self.student_db = student_db

    def delete_student(self, student_id):
        if student_id in self.student_db:
            del self.student_db[student_id]
            return True
        else:
            print(f"Student with ID {student_id} does not exist.")
            return False
