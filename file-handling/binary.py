
f = open('source.png','rb')
data = f.read()
print('type of data is ',type(data))

f1 = open('dest.png','wb')  # if file is not present then new file is created 
f1.write(data)
print('write successful')
f.close()
f1.close()

# usually to process binary data libraries are used
# like opencv , and other image processing libraries