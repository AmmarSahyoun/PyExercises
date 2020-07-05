# numpy array is alternative to a python list
import numpy as np

miles_list = [280, 300, 360, 140]
gallons_list = [7.1, 8.2, 10.10, 6.8]

# print(miles_list/gallons_list)
# this operation can't be done with a standard list, cause the lists
# are in different type
# to perform this operation for each element, we can use numpy

# to convert to numpy array
miles = np.array(miles_list)
print(miles)
gallons = np.array(gallons_list)

mpg = miles / gallons
print(f"mpg = {mpg}")
print('++++++++++++\n')
print(mpg[2])

# we can also select data with this numpy array by passing a
# comparision operator within the square brackets:

print(mpg > 35)
# the result is a boolean value for each element
# within the numpy array indicating if the element
# is greater than 35 or not

print('++++++++++++++\n')
print(mpg[mpg > 35])
# the result will be the values in the mpg numpy array
# that are greater than 35 instead of a boolean value

# selecting portion of data from a list or array or
# sub-setting is a common operation and more practical with the
# additional functionality provided by numpy array
