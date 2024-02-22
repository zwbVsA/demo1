class Student:
    default_age=20

    def __init__(self):
        self.default_age = 16

s = Student()

print(s.default_age,Student.default_age)

print(dir(s))

print(s.__dict__)
print(s.__class__)