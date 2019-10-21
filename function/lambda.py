# sometimes we define a function without a name , such functions are called 
# lambda function or anonymous function

# this is a simple function

def square(x):
    return x*x

print('the square of 4 is ',square(4))

# same task i can perform using lambda function


sq =lambda x:x*x

# syntax of lambda function is ::-->  lambda arg_list : expression

print('the square of 4 is',sq(4))

# lambda function is applied as a agrument to useful functional programming methods 
# such as map() , filter() , reduce()

# map--> this function is used to add or remove or edit something to each element of the sequence

# below program will transform sequence [1,2,3,4,5] to [10,20,30,40,50]

l = list(map(lambda x:x*10,range(1,6)))
l2 = list(range(1,6))
print('supplied list is')
print(l2)
print('transformed list is')
print(l)

# syntax of map function is <any-sequence-type>(map(<lambda-function>,<any-sequence>))
# we have to type-cast the output obtained from map function to the sequence which we required

# filter--> this function will filter the values of sequence as per the given condition

l = list(filter(lambda x:x%2==0,range(1,31)))
# only those element will be present inside the list , in which this condition holds true
# x%2==0
# only even number
l2 = list(range(1,31))
print('supplied list to filter() is ')
print(l2)
print('filtered list is',l)


# reduce--> this function will reduce the list to a single value
# example is sum of elements of a list

from functools import reduce
# reduce function is present inside functools module , it is not a built in function of python

i = reduce(lambda x,y:x+y,range(1,11))
print('sum os 1 to 10 is',i)

# every thing in python is an object

# empty function

def f1():
    print('hello inside f1()')

print(f1)
print(id(f1))

# function aliasing
f1()
f = f1
print('given alias as f')
f()

# note in the above example only one function is available i.e f1()
# but we can call that function by either f1() or by f()
# if we delete one name , then also we can access that same function by the another name

del f1

f()

#del f   #if we delete f , then calling this function will produce an error
#f()


# you can pass function as an argument to another function

def container(name,age,dept,remark):
    print('-----------------------------------------------------------')
    print('inside container function')
    print('name is {}'.format(name))
    print('age is {}'.format(age))
    print('studied in department {}'.format(dept))
    remark(name)
    print('-----------------------------------------------------------')

bad = lambda name:print('{} is a bad candidate'.format(name))
good = lambda name:print('{} is a good candidate'.format(name))

container('mehul',26,'mechanical',good)
container('nakul',22,'animation-vfx',bad)

# fuunctions which we pass inside another function are known as callback functions















