#Nested Lists:
#Sometimes we can take one list inside another list. Such type of lists are called nested
#lists.

n=[10,20,[30,40]]
print(n)
print(n[0])
print(n[2])
print(n[2][0])
print(n[2][1])


# output-->
# [10, 20, [30, 40]]
# 10
# [30, 40]
# 30
# 40


# Note: We can access nested list elements by using index just like accessing multi
# dimensional array elements.

#Nested List as Matrix:
#In Python we can represent matrix by using nested lists.

n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Elements by Row wise:")
for r in n:
    print(r)
print("Elements by Matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()


# Elements by Row wise:
# [10, 20, 30]
# [40, 50, 60]
# [70, 80, 90]
# Elements by Matrix style:
# 10 20 30
# 40 50 60
# 70 80 90


# List Comprehensions:
# It is very easy and compact way of creating list objects from any iterable objects
# (Like List, Tuple, Dictionary, Range etc) based on some condition.


# Syntax: list = [expression for item in list if condition]


s = [ x*x for x in range(1,11)]
print(s)
v = [2**x for x in range(1,6)]
print(v)
m = [x for x in s if x%2==0]
print(m)


# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [2, 4, 8, 16, 32]
# [4, 16, 36, 64, 100]


# program to print the first character of words present in the list
words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[0] for w in words]
print(l)


# Output: ['B', 'N', 'V', 'C']


# common elements present in num1 and num2

num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[ i for i in num1 if i not in num2]
# printing elements that are not common
print(num3) # op->[10,20] 
#common elements present in num1 and num2
num4=[i for i in num1 if i in num2]
print(num4) #op->[30, 40]




















