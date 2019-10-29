try:
    i = int(input('Enter first value:'))
    j = int(input('Enter second value:'))
    print(i/j)
except ZeroDivisionError:
    print('cannot divide by zero')
except:         # default except block
    print('invalid values')

# default except block must be the last block
