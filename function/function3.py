# this file demonstrate variable number of arguments
# type1--> variable number of positional arguments

def sum(*n):
    sum = 0
    print('-------------------------------------------')
    print('inside sum(*n)')
    print('agruments passed -->{}'.format(n))
    print('type of argument is {}'.format(type(n)))
    for n1 in n:
        sum = sum + n1
    print('sum is {}'.format(sum))
    print('-------------------------------------------')

sum(10,20,30,40)
sum(10,20,30,40,50,60,70,80)
sum(1,2,3,4,5,6)

# note we can mix variable length argument with positional argument

def sum1(pos,*n):
    sum = 0
    print('-------------------------------------------')
    print('inside sum1(pos,*n)')
    print('agruments passed -->{} and {}'.format(pos,n))
    print('type of argument is {}'.format(type(n)))
    for n1 in n:
        sum = sum + n1
    print('sum is {}'.format(sum))
    print('-------------------------------------------')

sum1('mehul',10,20,30,40)

# note : after variable length argument if we take any other argument then it must be keyword argument

def sum2(*n,pos='mehul'):
    sum = 0
    print('-------------------------------------------')
    print('inside sum2(*n,pos)')
    print('agruments passed --> {} and {}'.format(n,pos))
    print('type of argument is {}'.format(type(n)))
    for n1 in n:
        sum = sum + n1
    print('sum is {}'.format(sum))
    print('-------------------------------------------')

sum2(10,20,30,40,50,pos='mehul')
# if called sum2(10,20,30,40,50,'mehul')  ---> error


# just observe how these functions are called