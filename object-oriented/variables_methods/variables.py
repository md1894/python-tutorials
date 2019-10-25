
class student:
    SCHOOL_NAME = 'st joseph' # static variable

    def __init__(self,name,age):
        self.name = name # instance variable
        self.age = age # instance variable

    def m1(self):
        a  = 10 # local variable
        for a1 in range(a+1):
            print(a1)


st = student('mehul',18)
# you can access static variables by using class name
print(student.SCHOOL_NAME)
# you can access instance variable by using object reference
print(st.name)
print(st.age)

    