import numpy as np

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

ans = np.sum(mat, axis=0)
print(np.prod(ans))
