# when finally block will not get executed
# if my pvm will shut down explicitly then finally block will not get executed
# to shut down pvm explicitly we have to call one method
# in os module , there is one method _exit(0)
# finally block will not get executed

import os


try:
    print('inside try')
except:
    print('inside except')
finally:
    print('inside finally')

print('-------------------------------------- NOW USING os._exit(0) -------------------------------------')

try:
    print('try')
    os._exit(0)
except:
    print('except')
finally:
    print('finally')