# this file demonstrate is a relationship between the object
# we can establish is a relationship , with the help of inheritance 

# example : employee and person
# employee is a person
# i.e person will be a parent class , we will make employee as a child class 
# we will resuse code present inside person class , in employee class


class Person:

    def __init__(self,name,age,gender,dateOfBirth):
        print('Person class constructor called')
        self.name = name
        self.age = age
        self.gender = gender
        self.dateOfBirth = dateOfBirth

    def printPersonalDetail(self):
        print('----------------- PERSONAL DETAIL ----------------------')
        print('name is',self.name)
        print('age is',self.age)
        print('gender is',self.gender)
        print('date of birth is',self.dateOfBirth)


class Employee(Person):

    def __init__(self,name,age,gender,dateOfBirth,jobTitle,department,salry,jobLocation):
        super().__init__(name,age,gender,dateOfBirth)   # calling parent class constructor
        self.jobTitle = jobTitle
        self.jobLocation = jobLocation
        self.department = department
        self.salry = salry

    def displayDetails(self):
        # super().printPersonalDetail()
        self.printPersonalDetail()   # here i am not writing code to display personal details , i am reusing parent class code
        print('----------------------------- EMPLOYEE DETAILS --------------------')
        print('job title is',self.jobTitle)
        print('department is',self.department)
        print('location is ',self.jobLocation)
        print('salry is',self.salry)


e = Employee('mehul',26,'M','18th feb 1994','software engineer','IT',50000,'UK')
e.displayDetails()


# i can call parent class method by using super() function , or by using self