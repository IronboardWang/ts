import numpy as np

# array = np.random.random((3,4))
# # print(array)
# # print(array[0, 0])
# # print(array > 0.2)
# # print(array[array > 0.2])
# print(np.round(array))
#
# first = np.array([1,2,3])
# second = np.array([1,2,3])
# print(first + second)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm  = [x * 2.54 for x in dimensions_inch]
