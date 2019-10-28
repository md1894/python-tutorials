import time

class test:
    def __init__(self):
        print('object creation')

    def __del__(self):
        print('destroying object')


t = test()
t = None
time.sleep(5)
t2 = test()

# when object points to None , it is eligible for garbage collection
# garbagecollector will call destructor on that object
# if program reaches end of code , then automatically every object is eligible for garbage collection

# constructor --> def __init__(self)
# destructor --> def __del__(self) 

