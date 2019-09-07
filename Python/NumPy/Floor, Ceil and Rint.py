import numpy as np

np.set_printoptions(sign=' ') # for spacing (to pass the test)

a = list(map(float, input().split()))
print(np.floor(a))
print(np.ceil(a))
print(np.rint(a) , end='')

