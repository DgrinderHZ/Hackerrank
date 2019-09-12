# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

n, m = map(int, input().split())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

b = [list(map(int, input().split())) for _ in range(n)]

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.array(a)//np.array(b)) # print(np.divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))
