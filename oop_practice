class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name - {self.name}, age - {self.age}"
class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    def __str__(self):
        return f"{super().__str__()}, salary - {self.salary}"

class Student(Person):
    def __init__(self, name, age, scholarship):
        super().__init__(name, age)
        self.scholarship = scholarship
    def __str__(self):
        return f"{super().__str__()}, scholarship {self.scholarship}"

teacher = [
    Teacher ("Sam", 19, 2000),
    Teacher ("Clare", 32, 1100),
    Teacher ("Max", 21, 1000)
]

def total_salary(teachers):
    total = 0
    for teacher in teachers:
        total += teacher.salary
    return total

print(total_salary(teacher))

