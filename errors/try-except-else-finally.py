try:
    i = int(input('Enter first value:'))
    j = int(input('Enter second value:'))
    print(i/j)
except BaseException as msg:
    print('type of exception is',type(msg))
    print('type of exception is',msg.__class__)
    print('the exception class name',msg.__class__.__name__)
    print('description is',msg)
else:
    print(' no exception occured -------------- ')
    print('else will execute if no execption occured')
finally:
    print('compulsory code ---------------- , weather exception occured or not')

    # if exception is not handled , then before abnormal termination finally block will be executed

try:
    print(10/0)
except ValueError:
    print('ValueError handler')
finally:
    print('*********************************************************')
    print('even exception not handled , then also finally executed')
    print(50*'*')

