class AddStudent:
    def __init__(self, student_db):
        self.student_db = student_db

    def add_student(self, student_id,  name, surname):
        if student_id in self.student_db:
            return f"Student with ID {student_id} already exists."
        
        self.student_db[student_id] = {
            'id': student_id,
            'name': name,
            'surname': surname,
            'grade': None
        }
        return f"Student {name} added successfully."