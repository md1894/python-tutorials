# importance of __str__() method
# we have to return string
# this magic method is use to provide meaningful representation to our object

class student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return " name is {} age is {} marks is {}".format(self.name,self.age,self.marks)


class test:
    pass

t = test()
print(t)        #<__main__.test object at 0x7f863178ff98>

s = student('mehul',26,99.78)
s1 = student('nakul',22,55)

print(s)
print(s1)