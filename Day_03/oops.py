# class Student:
#     name = "karan"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# init function(constructor)
# class Student:

#     # parameterized constructor
#     def __init__(self,name, marks):
#         self.name = name
#         self.name = marks
#         print("adding new student in the database")

# s1 = Student("Karan","87")
# print(s1.name)


# Methods
class Student:

    # parameterized constructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def Welcome(self):
        print("welcome Student!", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan","87")
s1.Welcome()
print(s1.get_marks())


    


