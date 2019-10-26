

# note for class method @classmethod decorator is necessary
# but for static method @staticmethod decorator is not mandatory
# based on how the method is called , it becomes either instance method or static method

class demo:
    
    def staticOrInstance(x):
        print(x)


d = demo()
demo.staticOrInstance(10) # acts as a static method , prints the value of 10
d.staticOrInstance()    # acts as a instance method , prints object reference , because x is acting like self


#10
#<__main__.demo object at 0x7fc8531097f0>
