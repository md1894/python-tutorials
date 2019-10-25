# 1) Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple
# object, we cannot perform any changes in that object.
# 2) Hence Tuple is Read only version of List.
# 3) If our data is fixed and never changes then we should go for Tuple.
# 4) Insertion Order is preserved
# 5) Duplicates are allowed
# 6) Heterogeneous objects are allowed.
# 7) We can preserve insertion order and we can differentiate duplicate objects by using
# index. Hence index will play very important role in Tuple also.
# 8) Tuple support both +ve and -ve index. +ve index means forward direction (from left to
# right) and -ve index means backward direction (from right to left)
# 9) We can represent Tuple elements within Parenthesis and with comma seperator.
# 10) Parenethesis are optional but recommended to use.


t=10,20,30,40
print(t)
print(type(t))

#Output
#(10, 20, 30, 40)
#<class 'tuple'>
t=()
print(type(t)) #op-> tuple

# Note: We have to take special care about single valued tuple.compulsary the value
# should ends with comma, otherwise it is not treated as tuple.

t=(10)
print(t)
print(type(t))
t=(10,)
print(t)
print(type(t))
# Output
# 10
# <class 'int'>
#Output
# (10,)
# <class 'tuple'>

# Tuple Creation:
# 1) t = ()
# Creation of Empty Tuple
# 2) t = (10,)
# t = 10,
# Creation of Single valued Tuple, Parenthesis are Optional, should ends with Comma
# 3) t = 10, 20, 30
# t = (10, 20, 30)
# Creation of multi values Tuples & Parenthesis are Optional.


# creating tuple by using tuple function , type casting
list=[10,20,30]
t=tuple(list)
print(t)
t=tuple(range(10,20,2))
print(t)


# cmp():
# It compares the elements of both tuples.
# If both tuples are equal then returns 0
# If the first tuple is less than second tuple then it returns -1
# If the first tuple is greater than second tuple then it returns +1


# t1=(10,20,30)
# t2=(40,50,60)
# t3=(10,20,30)
# print(cmp(t1,t2)) # op-> -1
# print(cmp(t1,t3)) # op-> 0
# print(cmp(t2,t3)) # op-> +1

# note : only in python 2.x , not in python3

# Tuple Packing and Unpacking:
# We can create a tuple by packing a group of variables.

a = 10
b = 20
c = 30
d = 40
t = a, b, c, d
print('tuple-packing')
print(t) #op-> (10, 20, 30, 40)


# Here a, b, c, d are packed into a Tuple t. This is nothing but Tuple packing.
# Tuple unpacking is the reverse process of Tuple packing.
# We can unpack a Tuple and assign its values to different variables.

print('tuple unpacking-------------------')

t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)


# Note: At the time of tuple unpacking the number of variables and number of values
# should be same, otherwise we will get ValueError.


# Tuple Comprehension:
# Tuple Comprehension is not supported by Python.
# t = ( x**2 for x in range(1,6))
# Here we are not getting tuple object and we are getting generator object.

print('tuple comprehension -------------------')
t= ( x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)

# <class 'generator'>
# 1
# 4
# 9
# 16
# 25



# note other things like , +,* operators we can use on tuple objects , just like list
# we can also sort elements of tuple by using simple python built in functions
# these are the important points about tuple data structure



















