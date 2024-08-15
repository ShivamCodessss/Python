class Student():
    def __init__(self):
        self.name = "Random"
        self.grade = "Fail"
        self.district = "Orange County"

Student1 = Student()
print(Student1.name)
print(Student1.grade)

class Std():
    def __init__(self, name, grade, district):
        self.name = name
        self.grade = grade
        self.district = district

Std1 = Std("sam", "k", "Red County")
print(Std1.name)
print(Std1.grade)

