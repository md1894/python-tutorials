# seek --> use to move the cursor position
# tell --> to know the cursor position


with open('read.txt','r') as f:
    print('currently the cursor is present at ',f.tell())
    print('-------------------------------------------------')
    print('read some data and then see where cursor has gone , 10 characters')
    print(f.read(10))
    print('position of cursor is ',f.tell())
    print('read 10 characters again :: ',f.read(10))
    print('cursor position is ',f.tell())
    f.seek(0)       #position is resetted
    #f.seek(-20)        # cannot take negative values
    print('read 10 characters again :: ',f.read(10))

