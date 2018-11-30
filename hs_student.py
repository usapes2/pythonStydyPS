
from student import *

""" Inheritance from Student class """

class HighSchoolStudent(Student):
    school_name = "Springfield High School"
    """ Overwrite parent's method """
    def get_school_name(self):
        return "This is high school student"
    """ Use super() to refer the parent method """
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value +"-High SCHOOL "
