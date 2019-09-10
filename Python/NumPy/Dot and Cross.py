import numpy as np
np.set_printoptions(sign=' ') # for spacing (to pass the test)

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
a = np.array(a)

b = []
for _ in range(n):
    b.append(list(map(int, input().split())))
b = np.array(b).transpose()

ans = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(np.dot(a[i], b[j]))
    ans.append(row)

print(np.matrix(ans))
