# Enter your code here. Read input from STDIN. Print output to STDOUT


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s  = input()
perm = groupby(s)
for item, k in perm:
    print("(" + str(int(len(list(k)))) + ", " + item + ")" , end = ' ')
