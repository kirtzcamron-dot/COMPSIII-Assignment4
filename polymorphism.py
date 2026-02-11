class Student:
    def __init__(self, name, major, gpa_for_semesters):
        self.name = name                 
        self.major = major               
        self.__gpa_for_semesters = gpa_for_semesters  

    def __str__(self):
        return f"{self.name} is studying {self.major}."

    def get_gpa(self):
        return self.__gpa_for_semesters

    def set_gpa(self, new_value):
        self.__gpa_for_semesters = new_value

    def calculate_average_gpa(self):
        total = sum(self.__gpa_for_semesters)
        count = len(self.__gpa_for_semesters)
        return total / count

    def is_in_good_standing(self):
        print(f"{self.name} is a student.")

class UndergraduateStudent(Student):
    # Delete this and write your code here
    pass

class GraduateStudent(Student):
    # Delete this and write your code here
    pass