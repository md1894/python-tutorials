# when we should use inner class
# if we want a scenario like-->
# without existing one type of object , if there is no chance of existing another type of object
# then such kind of flexibility we can attain with the help of inner class


# without existing outerclass object , there is no chance of existing inner class object. inner class object
# is closely associated with outer class object


class Outer:
    def __init__(self):
        print('creating Outer class object')

    class Inner:
        def __init__(self):
            print('creating Inner class object')

        def m1(self):
            print('inner class method')


if __name__ == '__main__':
    o = Outer()
    i = o.Inner() # we can create inner class object , but with the help of outer class only
    i.m1()

    i1 = Outer().Inner()
    i1.m1()