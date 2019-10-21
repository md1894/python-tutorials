# this source file will demonstrate types of agruments that we can pass in functions

# 1. positional arguments

def posDemo(a,b,c):
    print('-----------------------------------------------------------------------')
    print('inside posDemo(a,b,c) arg1={} arg2={} arg3={}'.format(a,b,c))
    print('-----------------------------------------------------------------------')

posDemo(10,20,30)
posDemo(30,10,20)

# observe the change when calling above function

# ------------------------------------------------------------------------------------------------------------------------
# keyword arguments
# you can pass agrument by assigning it to a keyword i.e parameter name 

def keywordDemo(a,b,c):
    print('------------------------------------------------------------------------')
    print('inside keywordDemo() function')
    print('arg1={} arg2={} arg3={}'.format(a,b,c))
    print('-----------------------------------------------------------------------')

keywordDemo(c = 100 , a = 500 , b = 888) # because of keyword argument we can pass argument in any order
keywordDemo(500,888,100)

# output in both function call is same

# default argument

def defaultDemo(a,b='def-val'):
    print('------------------------------------------------------------------------')
    print('inside defaultDemo() function a={} b={}'.format(a,b))
    print('------------------------------------------------------------------------')

defaultDemo(10,20)
defaultDemo(100)

# observe output in both the function call

# note:--> after default agrument you cannot pass any non-default argument
# defaultDemo(a,b="def-val",c)  ===>> you cannot keep function prototype as this
# otherwise you will get syntax error