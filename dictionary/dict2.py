# Important Functions of Dictionary:
# dict():
# To create a dictionary
#     d = dict()  It creates empty dictionary
#     d = dict({100:"dubey",200:"ravi"})  It creates dictionary with specified elements
#     d = dict([(100,"dubey"),(200,"shiva"),(300,"ravi")])
# It creates dictionary with the given list of tuple elements

# 2) len()
# Returns the number of items in the dictionary.

# 3) clear():
# To remove all elements from the dictionary.

# 4) get():
# To get the value associated with the key
# d.get(key)
# If the key is available then returns the corresponding value otherwise returns None.It
# wont raise any error.

# d.get(key,defaultvalue)
# If the key is available then returns the corresponding value otherwise returns default
# value.

print('-------------------------------------- get function demo ---------------------------')
d={100:"dubey",200:"ravi",300:"shiva"}

print(d[100]) # dubey
#print(d[400]) # KeyError:400
print(d.get(100)) # dubey
print(d.get(400)) # None
print(d.get(100,"Guest")) # dubey
print(d.get(400,"Guest")) # Guest

print('----------------------------------------------- pop() demo ----------------------------')
# pop():
# d.pop(key)
#  It removes the entry associated with the specified key and returns the
# corresponding value.
#  If the specified key is not available then we will get KeyError.

print(d.pop(100))
print(d)
#print(d.pop(400)) # key error

print('------------------------------- popitem() ----------------------------------')
# popitem():
# It removes an arbitrary item(key-value) from the dictionaty and returns it.
d={100:"dubey",200:"ravi",300:"shiva"}
print(d)
print(d.popitem())
print(d)


# keys():
# It returns all keys associated with dictionary.
print('----------------------------------- keys demo ----------------------------------')
d={100:"dubey",200:"ravi",300:"shiva"}
print(d.keys())
for k in d.keys():
    print(k)

# values():
# It returns all values associated with the dictionary.

print('------------------------------------ values demo ------------------------------')
print(d.values())
for v in d.values():
    print(v)

# items():
# It returns list of tuples representing key-value pairs.
# [(k,v),(k,v),(k,v)]


print('---------------------------------- items demo ---------------------------------')

for k,v in d.items():
    print(k,"--",v)