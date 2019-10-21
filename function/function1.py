
# we have to use two keywords (1.def , 2.return) while defining function in python
# return keyword is optional
# when function is not returning any value , None object gets returned

def noArgNoReturn():
    print('-------------------------------------------------------------------------------------------')
    print('inside noArgNoReturn()')
    print('this is a function in which you dont have to pass any argument , also it wont return any value')

def noArgButReturnValue():
    print('--------------------------------------------------------------------------------------------')
    print('inside noArgButReturnValue()')
    # you can return any value , for demo purpose i am returning str value
    return 'this is a string that gets returned from noArgButReturnValue()'

x = noArgNoReturn()
print('value that gets returned from noArgNoReturn() is',x)

x = noArgButReturnValue()
print('value that gets returned from noArgButReturnValue() is--->>',x)