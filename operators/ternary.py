a = 10
b = 20

# simple ternary operator
min = a if a < b else b
print(min)

a , b, c = 15 , 17 , 9

# nesting of ternary operator
max = a if a > b and a > c else b if b > c else c
print(max)