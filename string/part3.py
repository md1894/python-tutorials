# Mathematical Operators for String:
# We can apply the following mathematical operators for Strings.
# + operator for concatenation
# * operator for repetition
print("mehul"+"soft") 
print("mehul"*2) 



# Note:
# 1) To use + operator for Strings, compulsory both arguments should be str type.
# 2) To use * operator for Strings, compulsory one argument should be str and other
# argument should be int.

# len() in-built Function:
# We can use len() function to find the number of characters present in the string.
# Eg:
s = 'mehul'
print(len(s))
# Q) Write a Program to access each Character of String in
# Forward and Backward Direction by using while Loop?
s = "Learning Python is very easy !!!"
n = len(s)
i = 0
print("Forward direction")
while i<n:
    print(s[i],end=' ')
    i +=1

print("Backward direction")
i = -1
while i >= -n:
    print(s[i],end=' ')
    i = i-1