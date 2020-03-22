# two types
# 1. identity operator --> is, is not
# 2. membership operator

a = 'mehul'
b = 'mehul'

print(a is b) # true
print(id(a), id(b)) # same address

class demo:

    def __init__(self, a, b):
        self.a = a;
        self.b = b;

d = demo(10,202)
d1 = demo(10,202)

print(d is d1) # false
print(id(d), id(d1)) # different address

d2 = d1

print(d2 is d1) # true
print(id(d2), id(d1)) # same address

# ----------------- 'is not' operator ------------------------

a = 'mehul'
b = 'mehul'

print(a is not b) # False
print(id(a), id(b)) # same address

class demo1:

    def __init__(self, a, b):
        self.a = a;
        self.b = b;

d = demo1(10,202)
d1 = demo1(10,202)

print(d is not d1) # True
print(id(d), id(d1)) # different address

d2 = d1

print(d2 is not d1) # False
print(id(d2), id(d1)) # same address