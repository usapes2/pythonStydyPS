

"""some build in functions like print or input"""
#username = input("Enter the user's  name: ")
#print(username)

students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student.title()
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name,student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)


add_student(name = "Mark", student_id = 15)

""" Number of argumets provided to the funciton """
def var_args(name,*args):
    print(name)
    print(args)

def var_args2(name,**kwargs):
    print(name)
    print(kwargs["description"], kwargs["feedback"])

#var_args("Lizzard","Loves Py",None,123)

var_args2("Lizzard",description = "Loves Py", feedback = None)





