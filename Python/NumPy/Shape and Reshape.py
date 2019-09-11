import numpy

change_array = numpy.array(list(map(int, input().split())))
change_array.shape = (3, 3)
print(change_array)
