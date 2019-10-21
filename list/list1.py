# If we want to represent a group of individual objects as a single entity where insertion
# order preserved and duplicates are allowed, then we should go for List.


# insertion order preserved.

# duplicate objects are allowed.

# heterogeneous objects are allowed.

# List is dynamic because based on our requirement we can increase the size and
# decrease the size.


# In List the elements will be placed within square brackets and with comma seperator.

# We can differentiate duplicate elements by using index and we can preserve insertion
# order by using index. Hence index will play very important role.

# Python supports both positive and negative indexes. +ve index means from left to
# right where as negative index means right to left.

# List objects are mutable.i.e we can change the content.
# ----------------------------------------------------------------------------------------------------------

# to create a empty list

list=[]
print(list)
print(type(list))
# output-->
#[]
#<class 'list'>


# dynamic i.e user will input list as ['abc','xyz']
list=eval(input("Enter List:"))
print(list)
print(type(list))


# with range function
# l=list(range(0,10,2))
# print(l)
# print(type(l))

# slice operator with list
print('-----------------------------------')
print('slice operator with list data type')
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100])
print('------------------------------------')


# output--->
# [3, 5, 7]
# [5, 7, 9]
# [4, 5, 6, 7]
# [9, 7, 5]
# [5, 6, 7, 8, 9, 10]

print('---------------------------------------')
# proof that list object are mutable
n=[10,20,30,40]
print(n)
n[1]=777
print(n)

#output-->
#[10, 20, 30, 40]
#[10, 777, 30, 40]

# list with while loop
print('-------------------------')
print('list with while loop')
n = [0,1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(n):
    print(n[i])
    i=i+1


# output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print('-----------------------------')
print('list with for loop')
n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    print(n1)


# output-->
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# for loop with if and list
print('-----------------------------------')
print('list with if block')
n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    if n1%2==0:
        print(n1)


# output-->
# 0
# 2
# 4
# 6
# 8
# 10



# display the list element with index wise
print('-------------------------------')
print('index wise printing of list')
l = ["A","B","C"]
x = len(l)
for i in range(x):
    print(l[i],"is available at positive index: ",i,"and at negative index: ",i-x)


# output-->
# A is available at positive index: 0 and at negative index: -3
# B is available at positive index: 1 and at negative index: -2
# C is available at positive index: 2 and at negative index: -1