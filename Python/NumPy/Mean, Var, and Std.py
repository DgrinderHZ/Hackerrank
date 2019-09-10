import numpy as np
np.set_printoptions(sign=' ') # for spacing (to pass the test)

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
mat = np.array(mat)

print(np.mean(mat, axis=1))
print(np.var(mat, axis=0))
print(np.std(mat, axis=None))
