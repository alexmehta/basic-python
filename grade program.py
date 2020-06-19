name = input("What is the Students name")
grade = int(input("What Score Did They Get"))
age = int(input("What is there age"))
class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

student1 = student (name, age, grade)

if student1.grade > 50:
    print(student1.name + " passed")

else:
    print(student1.name + " did not pass")