class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = student ("Nick", 12, 51)

if student1.grade > 50:
    print(student1.name + " passed")

else:
    print(student1.name + " did not pass")