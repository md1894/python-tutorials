# in this program we will demonstrate the use of with statement
# with is used in file handling to automatically close the file

with open('read.txt','r') as f:
    print(f.read())
    print('is file closed ',f.closed)
print('is file closed ',f.closed)