# clear():
# To remove all elements from the Set.

print('clear function demo ---------------------')
s={10,20,30}
print(s)
s.clear()
print(s)


print('-------------- mathematical functions on set-------------------------')
# Mathematical Operations on the Set:
# union():
#x.union(y) # We can use this function to return all elements present in both sets
#x.union(y) #OR x|y.
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.union(y)) # {10, 20, 30, 40, 50, 60}
print (x|y) # {10, 20, 30, 40, 50, 60}


# intersection():
# x.intersection(y) OR x&y.
# Returns common elements present in both x and y.

x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.intersection(y)) # {40, 30}
print(x&y) # {40, 30}


# difference():
# x.difference(y) OR x-y.
# Returns the elements present in x but not in y.


x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.difference(y)) # 10, 20
print (x-y) # {10, 20}
print (y-x) # {50, 60}


# symmetric_difference():
# x.symmetric_difference(y) OR x^y.
# Returns elements present in either x OR y but not in both.

x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print (x.symmetric_difference(y)) # {10, 50, 20, 60}
print(x^y) # {10, 50, 20, 60}


# we can use membership operator like , in and not in
s=set("dubey")
print(s)
print('d' in s)
print('z' in s)

print('set comprehension ----------------------')
s = {x*x for x in range(5)}
print (s) # {0, 1, 4, 9, 16}

s = {2**x for x in range(2,10,2)}
print (s) # {16, 256, 64, 4}


# Set Objects won't support indexing and slicing:
# 1) s = {10,20,30,40}
# 2) print(s[0]) # TypeError: 'set' object does not support indexing
# 3) print(s[1:3]) # TypeError: 'set' object is not subscriptable