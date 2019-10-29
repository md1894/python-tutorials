# generator is used to generate the sequence of values
# we can get sequence of values by using collections such as list,tuple,set,dictionary
# but , with generator memory utilization is efficient
# generator will generate value on demand
# but collections will store all values

x = [x*x for x in range(10)]
print(x)

# when we use tuple comprehension we get a generator object

x = (x*x for x in range(10))
print(type(x))
print(x)
while True:
    g = next(x)
    print(g)
    if g == 81:
        break
    
# note , if i want to generate a sequence that is huge 
# it contains lakhs of elements
# in that case we cant use list 
# it will raise memory problem
# generator in that case will be best suitable