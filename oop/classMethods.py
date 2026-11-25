# Class methods = Allow operations related to the class itself.
# take (cls)(->refer to the class it's like (self)) as the first parameter, which represents the class itself.

class Student:

    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    # Instance Method
    def get_info(self):
        return f"{self.name} = {self.gpa}"

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return cls.total_gpa / cls.count

print(Student.get_count()) # It's a class method because it get the count info and count is a class instance

student1 = Student("lair", 4)

student2 = Student("luiz", 3.6)

print(Student.get_average_gpa())