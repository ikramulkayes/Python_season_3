class Student:
    def __init__(self):
        self.name = None
        self.cgpa = 0.0
s1 = Student()
s2 = Student()

s1.name = "baby"
s2 = s1
s1.name = "mouly"
print(s1.name)
print(s2.name)
s2.name = "fahad"
print(s1.name)
print(s2.name)
