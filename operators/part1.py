
# floor division operator
print(type(7//2)) # 3 (truncate floating part) if both operands are int

print(type(7.0//2)) # 3.0

# normal division operator
print(type(7/2)) # 3.5

# exponent operator
# 2 raise to 4
print(2**4)
print(2**5)


# ------------------------- RELATIONAL OPERATOR ----------------------------------------

# relational operators can be applied on str data type also
a = 'mehul'
b = 'omkar kulkarni'
c = 'mehul'

print(b > a)
print(b >= a)
print(b <= a)
print(a == c)

#chaining of relational operators is also possible

#if any of the relation in the chain is false , then whole result becomes false 
print('chaining --------')
print(10 < 20 < 30)
print(10 < 20 < 30 > 40)