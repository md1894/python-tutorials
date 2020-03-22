# Accessing Characters by using Slice Operator:
#     Syntax: s[bEginindex:endindex:step]
#     Begin Index: From where we have to consider slice (substring)
#     End Index: We have to terminate the slice (substring) at endindex-1
#     Step: Incremented Value.

# Note:
# If we are not specifying bEgin index then it will consider from bEginning of the string.
# If we are not specifying end index then it will consider up to end of the string.
# The default value for step is 1.


s="Learning Python is very very easy!!!"
print(s[1:7:1])
# 3) 'earnin'
print(s[1:7]
# 5) 'earnin'
print(s[1:7:2])
# 7) 'eri'
print(s[:7]
# 9) 'Learnin'
print(s[7:])
# 11) 'g Python is very very easy!!!'
print(s[::])
# 13) 'Learning Python is very very easy!!!'
print(s[:]
# )15) 'Learning Python is very very easy!!!'
print(s[::-)1]
# 17) '!!!ysae yrev yrev si nohtyP gninraeL'



# Behaviour of Slice Operator:
# s[bEgin:end:step]
# Step value can be either +ve or –ve
# If +ve then it should be forward direction(left to right) and we have to consider bEgin
# to end-1
# If -ve then it should be backward direction (right to left) and we have to consider bEgin
# to end+1.
# ***Note:
# In the backward direction if end value is -1 then result is always empty



# In Forward Direction:
# default value for bEgin: 0
# default value for end: length of string
# default value for step: +1
# In Backward Direction:
# default value for bEgin: -1
# default value for end: -(length of string+1)
# Note: Either forward or backward direction, we can take both +ve and -ve values for
# bEgin and end index.





S = 'abcdefghij'
print(s[1:6:2]) 
print(s[::1]) 
print(s[::-1])
print(s[3:7:-1])
print(s[7:4:-1])
print(s[0:10000:1])
print(s[-4:1:-1])
print(s[-4:1:-2])
print(s[5:0:1])
# print(s[9:0:0])  ValueError: slice step cannot be zero
print(s[0:-10:-1])
print(s[0:-11:-1])
print(s[0:0:1])
print(s[0:-9:-2])
print(s[-5:-9:-2])
print(s[10:-1:-1])
print(s[10000:2:-1])
# Note: Slice operator never raises IndexError