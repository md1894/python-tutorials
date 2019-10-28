# gc module in python

# gc.isenabled()
# gc.disable()

# gc is bydefault enabled

import gc

print('garbage collector is enabled')
print(gc.isenabled())
print('gc disabled')
gc.disable()
print('gc enabled:?')
print(gc.isenabled())