
class test:

    def __init__(self,x):
        self.__x = x

    def __m1Private(self):
        print('inside the private method')

    def m1Public(self):
        print('inside the public method')
        print('value of private variable is',self.__x)


t = test(10)
#t.__m1Private()
t.m1Public()