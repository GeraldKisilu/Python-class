class Person:
    def __init__(self, name, age, height, color):
        self.name = name
        self.age = age
        self.height = height
        self.color = color
    def walk(self):
        print("Walking out to eat!")

    def talk(self):
        print("Codility test")

    def discuss(self):
        print("Discuss about economy")

class Student(Person):
    def __init__(self, name, age, height, color, grade):
        super().__init__(name, age, height, color)
        self.grade = grade
    def walk(self):
        print("Walking to class")
    def talk(self):
        print("Skrrrt skrrrt")
    def discuss(self):
        super().discuss()#to ensure not to repeat initializing the attribute
        print("Discussing about codility")

stud1 = Student("Gerald", 23, 188, "Chocolate", 95)
print(stud1.name)
print(stud1.grade)
stud1.walk()
stud1.talk()
stud1.discuss()