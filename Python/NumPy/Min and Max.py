import numpy as np

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

ans = np.min(mat, axis=1)
print(np.max(ans))
