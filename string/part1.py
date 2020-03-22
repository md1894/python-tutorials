# The most commonly used object in any project and in any programming language is String
# only. Hence we should aware complete information about String data type.
# What is String?
# Any sequence of characters within either single quotes or double quotes is considered as a
# String.
# Syntax:
s = 'mehul'
s = "mehul"
# Note: In most of other languges like C, C++, Java, a single character with in single quotes
# is treated as char data type value. But in Python we are not having char data type.Hence it
# is treated as String only.
ch = 'a'
print(type(ch))


# How to define multi-line String Literals?
# We can define multi-line String literals by using triple single or double quotes.
# Eg:
s = '''dubey
software
solutions'''

print(s)

# We can also use triple quotes to use single quotes or double quotes as symbol inside
# String literal.

# s = 'This is ' single quote symbol'  Invalid
# s = 'This is \' single quote symbol'  Valid
# s = "This is ' single quote symbol"  Valid
# s = 'This is " double quotes symbol'  Valid
# s = 'The "Python Notes" by 'dubey' is very helpful'  Invalid
# s = "The "Python Notes" by 'dubey' is very helpful"  Invalid
# s = 'The \"Python Notes\" by \'dubey\' is very helpful'  Valid
# s = '''The "Python Notes" by 'dubey' is very helpful'''  Valid



# How to Access Characters of a String?
# We can access characters of a string by using the following ways.
# 1) By using index
# 2) By using slice operator
# 1) Accessing Characters By using Index:

# Python supports both +ve and -ve Index.
# +ve Index means Left to Right (Forward Direction)
# -ve Index means Right to Left (Backward Direction)
s = 'dubey'

s='dubey'
s[0]
'd'
s[4]
'a'
s[-1]
'a'
s[10]
# IndexError: string index out of range
# Note: If we are trying to access characters of a string with out of range index then we will
# get error saying: IndexError


# Q) Write a Program to Accept some String from the Keyboard and display its
# Characters by Index wise (both Positive and Negative Index)

s=input("Enter Some String:")
i=0
for x in s:
    print("The character present at positive index {} and at nEgative index {} is {}".fo
    rmat(i,i-len(s),x))
    i=i+1
