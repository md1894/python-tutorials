
print('inner exception is handled by outer except block')
try:
    print(10+10)
    print('10'+'10')
    try:
        print(10+'10')
    except ArithmeticError:
        print('inner except block')
    finally:
        print('inner finally block')
except TypeError:
    print('outer except block')
finally:
    print('outer finally block')


print('inner exception is handled by inner except block')
try:
    print(10+10)
    print('10'+'10')
    try:
        print(10+'10')
    except TypeError:
        print('inner except block')
    finally:
        print('inner finally block')
except:
    print('outer except block')
finally:
    print('outer finally block')


print('--------------------------------------------------------------------------')
print('inner finally block will not execute')

try:
    print(10+10)
    print('outer try block ')
    print('10'+10)
    try:
        print(10+500)
    except TypeError:
        print('inner except block')
    finally:
        print('inner finally block')
except TypeError:
    print('outer except block')
finally:
    print('outer finally block')


# once we entered inside try block , its corresponding finally block will executed compulsory
# if we didnt enter try block , then its finally block will not be executed