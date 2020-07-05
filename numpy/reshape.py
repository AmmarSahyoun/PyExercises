import numpy as np

a = np.arange(12)
print(a, '\n')

# we can also let the numpy library figure out the correct
# number of rows or columns when reshaping an array through
# the use of value -1


print(a.reshape(-1,1))
# reshape 1D array to multi dimensional array
# if we know that we want the resulting array to have 1 column
# we can pass the integer(1 for column) and allow numpy to
# determine thw correct number of rows(-1) the array must have
print(a.shape)