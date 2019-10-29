f = open('demo1.txt','w')
f.write('mehul')
f.write('dubey')
f.write('python')
f.close()
print('write successfully completed')

# mehuldubeypython
# this content will be written in the file , demo1.txt

f = open('demo1.txt','w')
f.write('mehul\n')
f.write('dubey\n')
f.write('python\n')
f.close()
print('write successfully completed')

# this content will be written in the file demo1.txt
# mehul
# dubey
# python

f = open('demo1.txt','a')
f.write('mehul\n')
f.write('dubey\n')
f.write('python\n')
f.close()

# this data will be written in demo1.txt
# mehul
# dubey
# python
# mehul
# dubey
# python


# demo2.txt

f = open('demo2.txt','w')
lines = ['my name is mehul\n','i am 25 years old\n','i am a mechanical engineer\n','i am working as a software engineer\n']
f.writelines(lines)
f.close()
print('written lines')

# instead of list , we can pass tuple , set , dictionary
# if dictionary , only keys will be added
# keys must be of string type only

# if you want values , then f.writelines(d.values())

