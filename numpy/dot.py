import numpy as np

# a 2D numpyarray is defined from a list of python lists
# just like a single dimension numpy array, all elements in array
# must be asingle type

list_one = [1, 2, 3]
list_two = [4, 5, 6.1]
np_array = np.array([list_one, list_two])
print(np_array)
print(f"numbers that more than 3: {np_array[np_array > 3]}")

# if a Numpy array declared with a lists of multiple types,
# type corection will occure and the values will be all
# converted to a single type
print('++++++++++++++++')
miles_list = [240, 280, 300, 360]
gallons_list = [6.8, 7.1, 8.2, 10.1]
# will place this two lists in a 2d numpy array
trip_info = np.array([miles_list, gallons_list])
print(trip_info.shape)
# to select a value
print(trip_info[0, 1:3])

# we will declare a new variable and calculate the miles per
# gallon for each section of our trip by sub-setting the
# data from the trip_info 2D array
# will devide the first raw by the second raw of the 2d Array
mpg = trip_info[0] / trip_info[1]

print(mpg)
# if we want to add mpg array to the 2D array :
# we use np.append then we select trip_info and we
# add mpg within square brackets to match the number of
# dimentions of 2d array, choose axis= 0 to apply operation on rows not columns

trip_info = np.append(trip_info, [mpg], axis=0)
print(trip_info, '\n')

print('------------------------------------------------')
# Multiplying matrices and vectors using numpy using dot function

a = np.arange(12).reshape(4, 3)
b = np.arange(12).reshape(3, 4)
print(a, '\n')
print(b, '\n')
# when a dot function called on two arrays that are both 1 D,the
# result is a scalar represinting the inner product of the two vectors
# in 2d arrays rows multiply with the second array's column the sum the result
print(np.dot(a, b), '\n')
# we can use @ instead of np.dot command
print(a @ b, '\n')
