# We can use List, Tuple and Set to represent a group of individual objects as a single
# entity.
# If we want to represent a group of objects as key-value pairs then we should go for
# Dictionary.

# Eg:
# rollno ---- name
# phone number -- address
# ipaddress --- domain name

# Duplicate keys are not allowed but values can be duplicated.
# Hetrogeneous objects are allowed for both key and values.
# Insertion order is not preserved
# Dictionaries are mutable
# Dictionaries are dynamic
# indexing and slicing concepts are not applicable

# Note: In C++ and Java Dictionaries are known as "Map" where as in Perl and Ruby it is
# known as "Hash"


# How to Create Dictionary?
# d = {} OR d = dict()
# We are creating empty dictionary. We can add entries as follows

print('We are creating empty dictionary. We can add entries as follows--------')
d = {} #OR d = dict()
d[100]="dubey"
d[200]="mehul"
d[300]="nakul"
print(d) # {100: 'dubey', 200: 'mehul', 300: 'nakul'}

# we can create dictionary directly by initialization
#d = {key:value, key:value}

print('accessing data from dictionary---------------------')
print(d[100])
print(d[200])
print(d[300])


# If the specified key is not available then we will get KeyError
# print(d[400]) # KeyError: 400

if 400 in d:
    print(d[400])
else:
    print('wrong key 400')


# How to Update Dictionaries?
# d[key] = value

# If the key is not available then a new entry will be added to the dictionary with the
# specified key-value pair
print('---------------------------- update dictionary demo-------------------------')
# If the key is already available then old value will be replaced with new value.
d[100]="narendra"
d[400]="meena"
print(d)

print('--------------------------------- delete dictionary demo ---------------------')
# del d[key]
# It deletes entry associated with the specified key.
# If the key is not available then we will get KeyError.

print(d)
print('deleting record whose key is 200')
del d[200]
print(d)

# d.clear()
# To remove all entries from the dictionary.
print('------------------- clear demo ---------------------')
# creating the copy of d
d1=d.copy()
print(d1)
d1.clear()
print(d1)

# del d1
# To delete total dictionary.Now we cannot access d1.

del d1
#print(d1)  #--> error
















