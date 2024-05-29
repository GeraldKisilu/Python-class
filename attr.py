# Class Attributes & Methods
class Student:
    COHORTS = ["SDF-FT09","SDF-FT08","SDF-FT07"]
    student_count = 0
    students = []
    def __init__(self,name,cohort):
        if self.check_cohort(cohort):
            Student.student_count +=1
            Student.update_student_count()
            self.name = name
        else:
            print("Invalid cohort")

    @classmethod
    def update_student_count(cls,number = 1):
        cls.student_count += number
    
    @classmethod
    def check_cohort(cls,cohort):
        return cohort in cls.COHORTS
    
    @classmethod
    def show_students(cls):
        print([student for student in cls.students])

stud1 = Student("Geek","SDF-FT05")
stud2 = Student("Gabby","SDF-FT08")
stud2 = Student("Fatu","SDF-FT09")

# print(stud1.cohort)
# print(stud2.name)
# print(Student.student_count)

