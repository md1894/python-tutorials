# this file demonstrate variable number of keyword arguments

# for this we have to use **
# def f1(**n)
# we can call this function by passing any number of keyword arguments , internally these keyword arguments will
# gets stored inside a dictionary

def varKeyWord(**n):
    print('------------------------------------------------------')
    print('inside varKeyWord()')
    print('data received {}'.format(n))
    print('type of data received is {}'.format(type(n)))
    for k,v in n.items():
        # key = value , key-value pair
        print(k,"=",v)
    print('--------------------------------------------------------')

varKeyWord(mehul='python',omkar='c',sayli='c#',sunil='javascript',anup='java',anand='android')

# just for the reference


# def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)



# 1) f(3,2) o/p: 3 2 4 8

# 2) f(10,20,30,40) o/p: 10 20 30 40

# 3) f(25,50,arg4=100) o/p: 25 50 4 100

# 4) f(arg4=2,arg1=3,arg2=4) o/p: 3 4 4 2

# 5) f() o/p: Invalid
#  TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'


# 6) f(arg3=10, arg4=20, 30, 40) o/p: Invalid
#  SyntaxError: positional argument follows keyword argument
#  [After keyword arguments we should not take positional arguments]


# 7) f(4, 5, arg2 = 6)  Invalid
#  TypeError: f() got multiple values for argument 'arg2'


# 8) f(4, 5, arg3 = 5, arg5 = 6)  Invalid
#  TypeError: f() got an unexpected keyword argument 'arg5' 