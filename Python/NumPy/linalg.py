# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

numpy.set_printoptions(legacy='1.13') #important

n = int(input())
mat = numpy.array([list(map(float, input().split())) for _ in range(n)], float)
print(numpy.linalg.det(mat))
