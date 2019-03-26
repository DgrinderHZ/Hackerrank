# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s , k = input().split()
perm = list(permutations(sorted(s), int(k)))
for item in perm:
    print("".join(item))
