# to take input from keyboard , use input() function
# by default values are type 'str'

name = input('enter name : ')
age = input('enter age : ')

print('name is {0} and its type is {1}'.format(name,type(name)))
# name is mehul and its type is <class 'str'>

print('age is {0} and its type is {1}'.format(age,type(age)))
# age is 26 and its type is <class 'str'>

# to type caste it we will use type casting functions


age = int(input('enter age:'))
print('type of age is {0}'.format(type(age)))
# type of age is <class 'int'>

# read multiple values from keyboard in a single line

a,b = [int(x) for x in input('enter two numbers : ').split()]
print('a X b = ',a*b)
# enter two numbers : 2 3
# a X b =  6

# type casting inside a collection

l_ = [int(x) for x in '100,25,45'.split(',')]

for x in l_:
    print('value is {0} and its type is {1}'.format(x, type(x)))

# value is 100 and its type is <class 'int'>
# value is 25 and its type is <class 'int'>
# value is 45 and its type is <class 'int'>


# eval() : to evaluate the result

x = eval(input('type any type of data : '))
print(' value is {0} and type is {1}'.format(x, type(x)))

# type any type of data : 55*5
# value is 275 and type is <class 'int'>

# type any type of data : {10,'mehul','seema'}
# value is {10, 'seema', 'mehul'} and type is <class 'set'>

# type any type of data : {10:'abc', 20:'mehul'}
# value is {10: 'abc', 20: 'mehul'} and type is <class 'dict'>

# type any type of data : 56.023
# value is 56.023 and type is <class 'float'>

