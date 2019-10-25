# If we want to represent a group of unique values as a single entity then we should go
# for set.
# Duplicates are not allowed.
# Insertion order is not preserved.But we can sort the elements.
# Indexing and slicing not allowed for the set.
# Heterogeneous elements are allowed.
# Set objects are mutable i.e once we creates set object we can perform any changes in
# that object based on our requirement.
# We can represent set elements within curly braces and with comma seperation
# We can apply mathematical operations like union, intersection, difference etc on set
# objects.

print('creation of set object--------------')
s={10,20,30,40}
print(s)
print(type(s))
print('------------------------------------')

#We can create set objects by using set() Function s = set(any sequence)

l = [10,20,30,40,10,20,10]
s=set(l)
print(s) # {40, 10, 20, 30}

s=set(range(5))
print(s) #{0, 1, 2, 3, 4}

#note:
# While creating empty set we have to take special care.
# Compulsory we should use set() function.
# s = {}  It is treated as dictionary but not empty set.

s=set()
print(s)
print(type(s))


print('------------------------- important functions of set-----------------------')
# add(x):
# Adds item x to the set.
s={10,20,30}
s.add(40)
print(s) #{40, 10, 20, 30}

# update(x,y,z):
# To add multiple items to the set.
# Arguments are not individual elements and these are Iterable objects like List, Range
# etc.
# All elements present in the given Iterable objects will be added to the set.
s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)
#Output: {0, 1, 2, 3, 4, 40, 10, 50, 20, 60, 30}


# Q) What is the difference between add() and update()
# Functions in Set?
# We can use add() to add individual item to the Set,where as we can use update()
# function to add multiple items to Set.
# add() function can take only one argument where as update() function can take any
# number of arguments but all arguments should be iterable objects.

# Q) Which of the following are valid for set s?
# s.add(10)
# s.add(10,20,30)  TypeError: add() takes exactly one argument (3 given)
# s.update(10)  TypeError: 'int' object is not iterable
# s.update(range(1,10,2),range(0,10,2)


print('copy function demo ------------------------')

# copy():
# Returns copy of the set.
# It is cloned object.

s = {10,20,30}
s1 = s.copy()
print(s1)

print('pop function demo -----------------------------')

#pop():
# It removes and returns some random element from the set.

s={40,10,30,20}
print(s)
print(s.pop())
print(s)


# remove(x):
# It removes specified element from the set.
# If the specified element not present in the Set then we will get KeyError.

print('remove function demo----------------------------')

s = {40, 10, 30, 20}
s.remove(30)
print(s) #40, 10, 20

print('discard function demo')
# discard(x):
# It removes the specified element from the set.
# If the specified element not present in the set then we won't get any error.
s = {10, 20, 30}
s.discard(10)
print(s)
s.discard(50)
print(s)
# Q) What is the difference between remove() and discard() functions in Set?
# Q) Explain differences between pop(),remove() and discard() functionsin Set?