
# we can use same operator for multiple purposes
# python supports operator overloading

print(20+30)
print('20'+'30')

# here i will overload the + operator for customized objects
# book objects

class book:

    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        total_pages = self.pages + other.pages
        return total_pages

print('--------------------- OVERLOADING + OPERATOR FOR BOOK OBJECTS ____________________________')
b1 = book(200)
b2 = book(250)

print(b1+b2)


# note __add__(self,other) is known as a magic method
# b1+b2 --> b1 will pass as self , and b2 will pass as other
# when we use + operator between these two objects , automatically __add__(self,other) will be called

# list of operators and magic method

# + --> __add__         (plus operator)
# - --> __sub__         ( minus operator)               
# * --> __mul__         ( multiplication operator)
# / --> __div__         ( division operator)
# //(floor division) --> __floordiv__
# % --> __mod__
# ** --> __pow__
# += --> __iadd__       (compound addition operator)
# -= --> __isub__
# < --> __lt__          (less than)
# <= --> __le__         (less than or equal to)
# > --> __gt__          (greater than)
# >= --> __ge__         (greater than or equal to)
# == --> __eq__         (equal)
# != --> __ne__         (not equal)

