# if a class contains all abstract methods
# then in that case we can call that class as a interface

from abc import ABC,abstractmethod

class specifications(ABC):

    @abstractmethod
    def spec1(self):
        pass


    @abstractmethod
    def spec2(self):
        pass


    @abstractmethod
    def spec3(self):
        pass


    @abstractmethod
    def spec4(self):
        pass


class demo(ABC):
    pass

# compulsory child class must implement all these methods
# abstract class or interface is used to put some restrictions on the child class

# if the class is declared as abstract , but it contains no abstract methods
# happily we can create object of that class

d = demo()
