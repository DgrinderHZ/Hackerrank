import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = arr[::-1]
    arr = numpy.array(arr, float)
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
