# A variable shared among all instances e.g:

class Student:
    human = True # It'll be shared among all instances with the same value. If you change it, the value will update for every instance.
    # Always acess the class variable by the class name, e.g: Student.human
    num_student = 0
    def __init__(self):
        Student.num_student += 1