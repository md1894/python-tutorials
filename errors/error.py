# try with multiple except block
# pvm will give chance to each except block from top to bottom

try:
    i = int(input('Enter first value:'))
    j = int(input('Enter second value:'))
    print(i/j)
except ZeroDivisionError:
    print('cannot divide by zero')
except ValueError:
    print('invalid values')


# order of except block is important
print('----------------- ENTER ONLY INTEGER VALUES --------------------')
try:
    i = int(input('Enter first value:'))
    j = int(input('Enter second value:'))
    print(i/j)
except ArithmeticError:
    print('Arithmetic error parent class of ZeroDivisionError')
except ZeroDivisionError:
    print('ZeroDivisionError is a sub class of ArithmeticError , hence it will never get chance')

# single except block that can handle multiple different exception
print('-------------single except block that can handle multiple different exception-----------------')
try:
    i = int(input('Enter first value:'))
    j = int(input('Enter second value:'))
    print(i/j)
except (ArithmeticError,ValueError) as msg:
    print('multi exception block',msg.__class__.__name__)



