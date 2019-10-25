# note:
# constructor is a special method in python class
# name is always __init__(self)
# whenever object is created , constructor is called
# it is optional
# if not present python provides default constructor
# per object creation constructor will be executed once

# def __init__(self):
#        pass

class test:
    def m1(self):
        print('m1()')


print('-------------------------------------------')
t = test()
t.m1()
print('--------------------------------------------')
class demo:

    def __init__(self):
        print('constructor called ...')


d = demo()
d.__init__()
d.__init__()

# we can call constructor explicitly , but then no new object gets created 
# it will be executed just like a normal method

print('-----------------------------------------------')

# we cant define two constructor with same name , but different arguments
# overloading concept not applicable in python


class test1:
    def __init__(self):
        print('zero arg constructor')

    def __init__(self,x):
        print('one-arg constructor')


#t1 = test1() --> this line if uncommented , produces error
t2 = test1(10)




# note:

# python will consider the latest constructor , i.e. one-arg constructor
# it will discard all the previous constructors
# only the last constructor will be considered , all the other constructor will be discarded
# if we are creating object by calling any previous constructor
# then it produces error
# like in above example if i call constructor like t = test()--> invalid