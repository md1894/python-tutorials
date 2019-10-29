

# generator function to generate sequence 'A' , 'B' , 'C'

def myGen():
    yield 'A'
    yield 'B'
    yield 'C'

x = myGen()
print(type(x))
print(next(x))
print(next(x))
print(next(x))
#print(next(x))         #StopIteration
x = myGen()
print('print sequence using loop')
for x1 in x:
    print(x1)

# generator function to generate first n values

def nValues(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
print('generating first n values')
x = nValues(5)
for x1 in x:
    print(x1)