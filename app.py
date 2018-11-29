


"""some build in functions like print or input"""
#username = input("Enter the user's  name: ")
#print(username)

students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name,student_id = 000):
    student = {"name": name, "student_id": student_id}
    students.append(student)
"""
while(True):
    if input("Enter Yes to enter the student No for exit ") == "Yes":
        student_name = input("Enter the name ")
        student_id = input("Enter the ID ")
        add_student(student_name,student_id)
    else:
        break """
        
def save_file(student):
    try:
        f = open("students.txt","a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")

read_file()
print_student_titlecase()

student_name = input("Input students name ")
student_id = input("Input students ID ")

add_student(student_name, student_id)
save_file(student_name)

