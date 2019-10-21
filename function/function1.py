
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

def argButNoReturn(x):
    print('-----------------------------------------------------------')
    print('inside argButNoReturn() in which agrument is passed whose value is',x)


x = noArgNoReturn()
print('value that gets returned from noArgNoReturn() is',x)

x = noArgButReturnValue()
print('value that gets returned from noArgButReturnValue() is--->>',x)

argButNoReturn(100)

# in python one function can return multiple values,below is demo for that

def multiVal():
    print('----------------------------------------------------------------------------')
    print('inside multiVal()')
    print('-----------------------------------------------------------------------------')
    return 100,'mehul',True,['abc',100.5,'nakul']

a = multiVal()
print('value returned by multival() function are',a)
print('type of value returned by multival() function is',type(a))

# as the values returned by the function must remain unchanged , that is why the type of returned value is tuple

# note , you can pass any number of arguments into a function and function also can return any number of values