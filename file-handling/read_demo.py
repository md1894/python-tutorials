f = open('read.txt','r')
v = f.read()
print(v)
# prints the content of file 
# this content is meant for demo
# we will demonatrate read function

f.close()
# now we will read content line by line

f = open('read.txt','r')
v = f.readlines()
for v1 in v:
    print('-----')
    print(v1)
    print('-----')