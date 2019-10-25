#reverse():
#We can use to reverse() order of elements of list.

print('reverse demo ------------------------------------------------')
n=[10,20,30,40]
print(n,'-- original list')
n.reverse()
print(n,'-- reversed list')

#sort():
# In list by default insertion order is preserved. If want to sort the elements of list
# according to default natural sorting order then we should go for sort() method.
# For numbers  Default Natural sorting Order is Ascending Order
# For Strings  Default Natural sorting order is Alphabetical Order

#Note: To use sort() function, compulsory list should contain only homogeneous elements.
#Otherwise we will get TypeError

print('sort demo ---------------------------------------------')

n = [20,5,15,10,0]
n.sort()
print(n) # op-> [0,5,10,15,20]
s = ["Dog","Banana","Cat","Apple"]
s.sort()
print(s) # op-> ['Apple','Banana','Cat','Dog']

#To Sort in Reverse of Default Natural Sorting Order:
#We can sort according to reverse of default natural sorting order by using reverse=True
#argument.


print('sort with reverse demo -------------------------------------------')
n = [40,10,30,20]
n.sort()
print(n) # op-> [10,20,30,40]
n.sort(reverse = True)
print(n) # op-> [40,30,20,10]
n.sort(reverse = False)
print(n) # op-> [10,20,30,40]

#Aliasing and Cloning of List Objects:
#The process of giving another reference variable to the existing list is called aliasing.
print('-------------------------------alias demo---------------------------------')
x=[10,20,30,40]
y=x
print(id(x))
print(id(y))
print('x is alias for y , they both are pointing to the same object')

#The problem in this approach is by using one reference variable if we are changing
#content, then those changes will be reflected to the other reference variable.

y[1] = 777
print(x) # op-> [10,777,30,40]


#To overcome this problem we should go for cloning.
#The process of creating exactly duplicate independent object is called cloning.
#We can implement cloning by using slice operator or by using copy() function.

# by using slice operator
print('creating a distinct copy using slice operator')
x = [10,20,30,40]
y = x[:]
y[1] = 777
print(x) # op-> [10, 20, 30, 40]
print(y) # op-> [10, 777, 30, 40]

print('same program using copy function')

x = [10,20,30,40]
y = x.copy()
y[1] = 777
print(x) # op-> [10, 20, 30, 40]
print(y) # op-> [10, 777, 30, 40]

print('can use concetanation operator +')

a = [10, 20, 30]
b = [40, 50, 60]
c = a+b
print(c) # op-> [10, 20, 30, 40, 50, 60]

print('repetition operator *')
x = [10, 20, 30]
y = x*3
print(y) # op-> [10, 20, 30, 10, 20, 30, 10, 20, 30]

print('comparison of list objects')
x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG", "CAT", "RAT"]
print(x == y) #op-> True
print(x == z) #op-> False
print(x != z) #op-> True

# Note: Whenever we are using comparison operators (==, !=) for List objects then the
# following should be considered
# 1) The Number of Elements
# 2) The Order of Elements
# 3) The Content of Elements (Case Sensitive)
# Note: When ever we are using relatational Operators (<, <=, >, >=) between List Objects,
# only 1 ST Element comparison will be performed.

x = [50, 20, 30]
y = [40, 50, 60, 100, 200]
print(x>y) #op-> True
print(x>=y) #op-> True
print(x<y) #op-> False
print(x<=y) #op-> False

print('membership operator demo')
n=[10,20,30,40]
print (10 in n)
print (10 not in n)
print (50 in n)
print (50 not in n)

# Output
# True
# False
# False
# True

# clear() Function:
# We can use clear() function to remove all elements of List.