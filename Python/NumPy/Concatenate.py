import numpy as np

n, m, p = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

b = []
for _ in range(m):
    b.append(list(map(int, input().split())))

print(np.concatenate((a,b), axis=0))
