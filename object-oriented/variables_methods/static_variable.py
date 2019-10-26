# in python we can declare static variable at 6 places 
# those 6 place i will demonstrate below

class Test:
    a = 10      #place no one 

    def __init__(self):
        Test.b = 20     #place no 2

    def m1(self):
        Test.c = 30     # place no 3

    @classmethod
    def m2(cls):
        cls.d = 40      # place no 3
        Test.e = 50     # place no 4

    @staticmethod
    def m3():
        Test.f = 60     # place no 5


# note : we can use <class-name>.__dict__ , it will give class level information
# like Test.__dict__

print(Test.__dict__['a'])
t = Test()
print(Test.__dict__['a'],Test.__dict__['b'])
t.m1()
print(Test.__dict__['a'],Test.__dict__['b'],Test.__dict__['c'])
Test.m2()
print(Test.__dict__['a'],Test.__dict__['b'],Test.__dict__['c'],Test.__dict__['d'],Test.__dict__['e'])
Test.m3()
print(Test.__dict__['a'],Test.__dict__['b'],Test.__dict__['c'],Test.__dict__['d'],Test.__dict__['e'],Test.__dict__['f'])
Test.g = 70     # place no 6
print(Test.__dict__['a'],Test.__dict__['b'],Test.__dict__['c'],Test.__dict__['d'],Test.__dict__['e'],Test.__dict__['f'],Test.__dict__['g'])

# note:
# we can access static variable by any thing
# i.e classname,cls,self,object-reference outside class
# which ever is available you can use accordingly

# we can modify static variable either by using classname or cls variable
# similarly we can delete static variable either by using classname or cls variable