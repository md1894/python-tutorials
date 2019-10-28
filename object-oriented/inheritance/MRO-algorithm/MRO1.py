# MRO algorithm is useful in case of hybrid inheritance
# MRO stands for Method Resolution Order
# in python every class is a subclass of object class

# in hybrid inheritance we can find MRO of any class by using mro() function
# syntax is <class-name>.mro()


# consider hybrid inheritance , a simple example
# A is super class for both B and C 
# D is child class of class B and C

#                           A
#                          / \
#                         B   C
#                          \ /
#                           D

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print('printing mro of different classes')
print(D.mro())      #DBCAO   O--> object class
# this means if there is one method whose name is m1()
# python will sequentially search for m1() method in order DBCAO
# where it will find first , it will execute , and there by stops the search
# first it will search in D class
# then in B , C , A , object class at last