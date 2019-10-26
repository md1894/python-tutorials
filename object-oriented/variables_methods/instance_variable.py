# in python number of instance variables vary from object to object , of same class
# we can declare instance variable at 3 places , that i will demonstrate below


class student:
    def __init__(self,name,age):        # place no 1 : inside constructor , using self referenece
        self.name = name
        self.age = age

    def isContestantOfOlympiad(self,score):     # place no 2 : inside instance method
        self.olympiadScore = score


s = student('mehul',26)
print(s.__dict__)
s.isContestantOfOlympiad(250)
print(s.__dict__)
s.fathers_name = 'narendra'  # place no 3 : outside the class
print(s.__dict__)


#note __dict__ is a special variable of type dictionary , which will give you information about instance variable

class demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def deleteA(self):
        del self.a  # a instance variable will be deleted from the object


# can also delete multiple instance variable in a single line del self.a,self.b,self.c
d = demo(10,20)
print(d.__dict__)
d.deleteA()
print(d.__dict__)

c = demo(300,400)
print(c.__dict__)

# value of instance variable can be updated , simply by using any object reference and assignment operator
# either self , or external object reference


# note : if we delete or update instance variable of one object then , that changes wont be refelected to
# another object of same class
# because each object maintains separate copy of instance variable