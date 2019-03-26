# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s , k = input().split()
for i in range(int(k)):
    perm = list(combinations(sorted(s), i+1))
    for item in perm:
        print("".join(item))
