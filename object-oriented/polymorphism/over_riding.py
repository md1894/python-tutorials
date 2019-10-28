
class demoParent:

    def m1(self):
        print('inside m1() demoParent class')


class demoChild(demoParent):

    def m1(self):
        print('inside m1() of demoChild class')


d = demoChild()
d.m1()