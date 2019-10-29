# now we will add some extra functionality to add function


def addition(fun):
    def inner(a,b):     #argument is same for add and inner , it is compulsory
        print('*'*100)
        print('THE ADDITION OF TWO NUMBERS IS {}'.format(fun(a,b)))
        print('*'*100)
    return inner

@addition
def add(a,b):
    return a+b

add(10,30)