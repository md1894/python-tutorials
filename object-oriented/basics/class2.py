
class test:

    def __init__(self):
        pass
    
    def addr(self):
        print('the address of object pointed by self is',id(self))



print('--------------------------------------------------------------------')
t=test()
print('the address of object pointed by t is',id(t))
t.addr()


# note
# self is only used inside the class defination
# self is a reference variable pointing to the current object
# we cannot use self outside the class
# to access the member variables inside the class , we need self as a reference variable
# outside the class t is available as a reference variable , but inside there is no t
# first argument to the constructor is self , we dont need to pass it , python virtual machine will set this variable value
# first argument to the instance method is self
# self is not a keyword 
# we can give any name to it 
# see class demo , below

class demo:
    def __init__(mehul,a,b,c):
        mehul.a = a
        mehul.b = b
        mehul.c = c

    def m1(dubey):
        print('the value of instance variables are',dubey.a,dubey.b,dubey.c)


print('-------------------------------------------------------------------------------------')
d = demo('first-arg',10.556,500)
d.m1()