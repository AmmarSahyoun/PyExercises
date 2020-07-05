import numpy as np

# the numpy arange function generates a numpy array with
# values that are evenly spaced based on start and stop
# intervales and spacing in between that are specified upon declaration

numbers = np.arange(6, 32, 5)
print(numbers,'\n')
print(type(numbers),'\n')
# it created a numpy array with value ranging
# from 0 to 8 a step size of 1 in between each value

points = np.arange(4, 15, 1.5 )
print(points)

print("---------------------------------------")
# there are three type of indexing:
# 1-element access
# 2-basic slicing
# 3- advanced indexing
values = np.arange(9)
print()
print(f"we have numpy array: {values}")
print()
print(f"from right index:{values[-3:-2]}")
print(f"index from right to left{values[-3::-2]}")