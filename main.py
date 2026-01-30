import add_student
import delete_student
import list_students
import show_student_info
import enter_grade

file_path = "students.txt"

def load_students(file_path):
    students = {}
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) >= 4:
                    student_id = int(parts[0])
                    students[student_id] = {
                        'id': student_id,
                        'name': parts[1],
                        'surname': parts[2],
                        'grade': float(parts[3]) if parts[3] != 'None' else None
                    }
    except FileNotFoundError:
        pass
    return students

def save_students(file_path, students):
    with open(file_path, "w", encoding='utf-8') as file:
        for student in students.values():
            file.write(f"{student['id']}, {student['name']}, {student['surname']}, {student['grade']} \n")

print("Student Information System")
print("--------------------------")
print("""1. Add Student
2. Delete Student
3. List All Students
4. Enter grade to a student
5. Show Student Info
6. Show All Students Average
7. Exit
""")

student_db = load_students(file_path)

while True:
    choice = input("Select an option (1-7):")
    if choice == '1':
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        surname = input("Enter Student Surname: ")
        adder = add_student.AddStudent(student_db)
        print(adder.add_student(student_id, name, surname))
    elif choice == '2':
        student_id = int(input("Enter Student ID to delete: "))
        deleter = delete_student.DeleteStudent(student_db)
        if deleter.delete_student(student_id):
            print(f"Student with ID {student_id} deleted successfully.")
    elif choice == '3':
        lister = list_students.ListStudents(student_db)
        students = lister.execute()
        if not students:
            print("No students found.")
        else:
            for student in students:
                print(
            f"ID: {student['id']}, "
            f"Name: {student['name']}, "
            f"Surname: {student['surname']}, "
            f"Grade: {student['grade']}"
            )
    elif choice == '4':
        student_id = int(input("Enter Student ID to enter grade: "))
        grade = float(input("Enter Grade: "))
        grader = enter_grade.EnterGrade(student_db)
        if 0 <= grade <= 100:
            if grader.execute(student_id, grade):
                print(f"Grade {grade} entered for student ID {student_id}.")
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")

    elif choice == '5':
        student_id = int(input("Enter Student ID to show info: "))
        shower = show_student_info.ShowStudentInfo(student_db)
        student_info = shower.execute(student_id)
        if student_info:
           print(
        f"ID: {student_info['id']}, "
        f"Name: {student_info['name']}, "
        f"Surname: {student_info['surname']}, "
        f"Grade: {student_info['grade']}"
        )
        else:
            print(f"No student found with ID {student_id}.")
    elif choice == '6':
        total = 0
        count = 0
        for student in student_db.values():
            if student['grade'] is not None:
                total += student['grade']
                count += 1
        if count > 0:
            average = total / count
            print(f"Average grade of all students: {average:.2f}")
        else:
            print("No grades available to calculate average.")
    elif choice == '7':
        save_students(file_path, student_db)
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")