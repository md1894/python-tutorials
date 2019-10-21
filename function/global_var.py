# variables that are declared outside of a function are called global variable
# these variables can be accessed in all functions of that module i.e. current module

a = 10

def f1():
    loc = 100
    print(a)

def f2():
    print(a)
    #print(loc)  # --> this will produce error , because loc is a local variable declared in f1() 

def f3():
    print(a)

f1()
f2()
f3()

# global keyword in python
# used to declare global variable inside a function
# to make global variable available inside a function so that we can perform required modifications

aa = 500

def f4():
    print()
    #aa = 10  # --> this will produce an error
    global aa
    aa = 555
    print(aa)

def f5():
    print(aa)

f4()  # op: 555
f5()


# note :if global variable and local variable is having the same name then we can access 
# global variable inside a function as follows

gl = 550

def f6():
    gl = 500
    print('value of local variable gl is',gl)
    print('value of global variable gl is',globals()['gl']) 

f6()


# run this script file and observe the changes in output