# The numpy zeros function returns an array of a specified
# shape filled with zeros
import numpy as np

box = np.zeros(5)
print(box,'\n')
# In addition we can pass tuple as the first argument with the
# integers that present the array shape

empty = np.zeros((3, 4))
print(empty,'\n')

# To convert the values to integers, we can pass int as second argume
# Alternativly, we can pass the data type str which will return an
# empty array of string

print(np.zeros((2,2), int),'\n')
print(np.zeros((5,1), str),'\n')