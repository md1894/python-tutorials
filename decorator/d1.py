
# this file will demonstrate decorator
# when we want to add some extra feature to the function , we define decorator for that
# so that , extra functionality will be available to all the similar functions


def give_style(fun):    #defination of decorator function

    def inner():
        print('-'*50)
        fun()
        print('-'*50)

    return inner


@give_style #now this function will have some extra functionality
def foo():
    print('hello world')


foo()

# decorator is a simple function , which takes a function as a input agrument
# and inside that decorator function one local function is defined , inner()
# that local function uses input fuunction and enhances its quality
# at the end , that local function gets returned
# when ever we define function and puts decorator over it
# pvm will call decorator function , passes that function as a input to it
# and then which ever function gets returned from that decorator function
# pvm will execute that returned function

# note that , inner local function takes same argument as the input function
# foo takes no agrument , inner also takes no agrument
# number of garuments must be same , otherwise it will give error