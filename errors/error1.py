try:
    print(10/0)
except ZeroDivisionError as msg:
    print('type of exception is',type(msg))
    print('type of exception is',msg.__class__)
    print('the exception class name',msg.__class__.__name__)
    print('description is',msg)