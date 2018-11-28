


"""some build in functions like print or input"""
#username = input("Enter the user's  name: ")
#print(username)

students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name,student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)

while(True):
    if input("Enter Yes to enter the student No for exit ") == "Yes":
        student_name = input("Enter the name ")
        student_id = input("Enter the ID ")
        add_student(student_name,student_id)
    else:
        break
        
print(len(students))
print_student_titlecase()


