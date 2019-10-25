
#in python3 there are three types of method
#1.instance method
#2.class method
#3.static method

class student:

    SCHOOL_NAME = 'st joseph'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):    # instance method
        print('name is',self.name," age is",self.age)

    @classmethod
    def displaySchoolInfo(cls):   # class method
        print('school name is',cls.SCHOOL_NAME)

    @staticmethod           # static method
    def someUtil(a,b):
        return a+b


st = student('neha',17)
st.display()
student.displaySchoolInfo()
print(student.someUtil(200,58))

# in class method just similar to self there is an reference cls
# this is known as reference to class level object to student
# this class level object stores class level information
# we have to use decorators to declare class and static methods
# we can call static and class method by using classname


# class methods , ---> we can only access static variables
# static methods ---> cant access static and instance variables
# if we want to access them in static variables , then i have to pass them while calling static methods
