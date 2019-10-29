
def verify(fun):
    def inner(n):
        li = ['CM','PM','MLA']
        if n in li:
            print('*'*35)
            print('Hello {} you are important to us'.format(n))
            print('*'*35)
        else:
            fun(n)
    return inner

@verify
def wish(n):
    print('simple ordinary person {}'.format(n))




print(type(wish))
wish('PM')
wish('MLA')
wish('mehul')