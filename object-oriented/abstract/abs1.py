# abstract class means , class whose implementation is incomplete
# abstract class contains zero or more abstract
# we cant instantiate abstract class , i.e. we cant create object of it
# we have to import @abstractmethod and ABC from abc module
# ABC stands for abstract base class

from abc import ABC,abstractmethod

class studentProto(ABC):        # way to declare class as abstract
    
    def __init__(self,name,age,nativePlace,percentageMarks):
        self.name = name
        self.age = age
        self.nativePlace = nativePlace
        self.percentageMarks = percentageMarks


    @abstractmethod     # say to declare method as abstract
    def displayInfo(self):
        pass

    def setInfo(self,name=None,age=None,nativePlace=None,percentageMarks=None):
        if name != None:
            self.name = name
        elif age != None:
            self.age = age
        elif nativePlace != None:
            self.nativePlace = nativePlace
        else:
            self.percentageMarks = percentageMarks

    
class studentConcrete(studentProto):

    def __init__(self,name,age,nativePlace,percentageMarks):
        super().__init__(name,age,nativePlace,percentageMarks)

    def displayInfo(self):
        print('name=',self.name)
        print('age=',self.age)
        print('nativePlace=',self.nativePlace)


# note that , displayInfo is an abstract method , means compulsory child class must 
# provide some implementation for it 
# if not then , we cant create object for child class
# then child class will also become abstract

s = studentConcrete('mehul',25,'mumbai',88.5)
s.displayInfo()
