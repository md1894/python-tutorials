
class test:

    def __init__(self,x):
        self.x = x

    def m1(self):
        print('inside the public instance method')


t = test(10)
print(t.x)
t.m1()