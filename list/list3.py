# extend() Function:
# To add all items of one list to another list
# l1.extend(l2)
# all items present in l2 will be added to l1

print('-------------------------------------------------')
print('extend function')
order1=["Chicken","Mutton","Fish"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)
print('------------------------------------------------')
# op -> ['Chicken', 'Mutton', 'Fish', 'RC', 'KF', 'FO']
order = ["Chicken","Mutton","Fish"]
order.extend("Mushroom")
print(order)
print('----------------------')
# op-> ['Chicken', 'Mutton', 'Fish', 'M', 'u', 's', 'h', 'r', 'o', 'o', 'm']
# this is because , we passed <str> and str is a list of characters, i.e. sequence of characters

#remove() Function:
#We can use this function to remove specified item from the list.If the item present
#multiple times then only first occurrence will be removed.

print('remove demo')
n=[10,20,10,30]
n.remove(10)
#If the specified item not present in list then we will get ValueError
print(n)
print('---------------------------')

# Note: Hence before using remove() method first we have to check specified element
# present in the list or not by using in operator.

# pop() Function:
# It removes and returns the last element of the list.
# This is only function which manipulates list and returns some element.
print('pop demo')
n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n)
print('-------------------------------------')

#If the list is empty then pop() function raises IndexError


# Note:
# 1) pop() is the only function which manipulates the list and returns some value
# 2) In general we can use append() and pop() functions to implement stack datastructure
# by using list,which follows LIFO(Last In First Out) order.
# In general we can use pop() function to remove last element of the list. But we can use to
# remove elements based on index.
# n.pop(index)  To remove and return element present at specified index.
# n.pop()  To remove and return last element of the list


n = [10,20,30,40,50,60]
print(n.pop()) # op-> 60
print(n.pop(1)) # op-> 20
print(n.pop(10)) # op-> IndexError: pop index out of range
print('--------------------------------------------------')