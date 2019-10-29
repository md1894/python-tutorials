
def decor1(fun):
    def inner():
        print('inside decorator 1')

    return inner

def decor2(fun):
    def inner():
        print('inside decorator 2')

    return inner


@decor1
@decor2
def fun():
    print('hello fun()')

fun()


# decor2 is the nearest decorator
# decor1 is the farthest decorator
# so decor1 will return a function , that will get executed
# decor1 will take a function as a input , which is returned by decor2


