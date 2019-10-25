

class Student:
    ''' this class was developed by mehulkumar dubey
        for demo purpose '''
    
    def __init__(self):
        print('inside init method ',self)
        self.name = 'mehul'
        self.age = 26
        self.marks = 95.5

    def displayDetail(self):
        print('my name is',self.name)
        print('i am {} years old'.format(self.age))
        print('my marks are',self.marks)



class StudentCustomized:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def displayDetail(self):
        print('my name is',self.name)
        print('i am {} years old'.format(self.age))
        print('my marks are',self.marks)


print(Student.__doc__) # it prints the documentation string of class Student
#help(Student)

st1 = Student()
print('---------------------------------------------------- class with hard-coded members------------------------')
print('displaying the values of data members')
print(st1.name)
print(st1.age)
print(st1.marks)
print('call displayDetail() function present inside Student class')
st1.displayDetail()
print('--------------------------------------------------------- class with user supplied values --------------------')
st2 = StudentCustomized('nakul',22,65.78)
print('displaying the values of data members')
print(st2.name)
print(st2.age)
print(st2.marks)
print('call displayDetail() function present inside Student class')
st2.displayDetail()