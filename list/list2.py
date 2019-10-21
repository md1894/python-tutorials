# len function , calculate length of the list
print('----------------------------------')
print('len() function demo')
n = [10, 20, 30, 40]
print(len(n))
print('-----------------------------------')
# output-->
# 4

#count():
#It returns the number of occurrences of specified item in the list
print('-------------------------------------------')
print('count() function demo')
n=[1,2,2,2,2,3,3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print('-----------------------------------')
# output-->
# 1
# 4
# 2
# 0

#index():
#Returns the index of first occurrence of the specified item.
print('---------------------------------------------')
print('index() function demo')
n = [1, 2, 2, 2, 2, 3, 3]
print(n.index(1)) # op-> 0
print(n.index(2)) # op-> 1
print(n.index(3)) # op-> 5
#print(n.index(4)) # op-> ValueError: 4 is not in list
print('----------------------------------------------')

# Note: If the specified element not present in the list then we will get ValueError.Hence
# before index() method we have to check whether item present in the list or not by using in
# operator.
# print( 4 in n) # op-> False


#append() Function:
#We can use append() function to add item at the end of the list.

print('-------------------------------')
print('append function demo')
list=[]
list.append("A")
list.append("B")
list.append("C")
print(list)
print('------------------------------------')

#Eg: To add all elements to list upto 100 which are divisible by 10
print('To add all elements to list upto 100 which are divisible by 10')
list=[]
for i in range(101):
    if i%10==0:
        list.append(i)
print(list)
print('--------------------------------------------------------------')

#insert() Function:
#To insert item at specified index position
print('------------------------------------------------')
print('insert function demo')
n=[1,2,3,4,5]
n.insert(1,888)
print(n)
print('--------------------------------------------')

n=[1,2,3,4,5]
n.insert(10,777)
n.insert(-10,999)
print(n)


#Note: If the specified index is greater than max index then element will be inserted at last
#position. If the specified index is smaller than min index then element will be inserted at
#first position.