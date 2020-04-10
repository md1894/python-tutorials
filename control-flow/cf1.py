# else block in loops

i_ = int(input('enter the number which breaks the loop under 10 only'))

for x in range(10):
    if(x == i_):
        break
else:
    print('loop completed !!!')
    print('if break statement not executed then else statement will execute after the loop')
