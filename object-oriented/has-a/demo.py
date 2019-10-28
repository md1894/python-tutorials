# in this script i will demonstrate has a relationship between objects
# example , each person has some residential address associated with it 
# i am mehul , my address is 
# prideworld city , kingsbury E1-302 , Near DY Patil lohegaon , Pune 412105
# so person is a object , address is an object which is declared inside person class

class Address:

    def __init__(self,society_name,building_name,flat_number,city,pincode,land_mark=''):
        self.society_name = society_name
        self.building_name = building_name
        self.flat_number = flat_number
        self.land_mark = land_mark
        self.city = city
        self.pincode = pincode

    def getFullAddress(self):
        return """
            {} {} {} {} {} {}
        """.format(self.society_name,self.building_name,self.flat_number,self.land_mark,self.city,self.pincode)


class person:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def printCompleteDetails(self):
        print("""
        name is {} , age is {}
        address is
        """.format(self.name,self.age),self.address.getFullAddress())


a = Address('pride world city','kingsbury','E1-302','Pune','412105','Dy Patil College Lohegaon')
p = person('mehul',26,a)
p.printCompleteDetails()

# note that address object is itself inside person object
# we call such type of relationship as has a relationship in object oriented world