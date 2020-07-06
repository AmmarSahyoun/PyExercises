import numpy as np

# The numpy library has the ability to generate random
# lists of data, shuffle existing data and draw
# samples based onspecified distribution

random = np.random.rand(5, 3)
# this function return numpy array with
# random values between 0 - 1 in the specified shape
print(random, '\n')

# to change the range we can multiyply the function
# by the largest number we want tp produce
print(50 * random, '\n')
print('----------------------------', '\n')

print(f"the array before shuffle: \n {random}")
# this shuffle the first column of the random array
np.random.shuffle(random[:, 0])
print(f"the array after shuffle 1column : \n {random}")
print('----------------------------', '\n')

print(f"the array before shuffle: \n {random}")
# this shuffle the first column of the random array
np.random.shuffle(random[1, :])
print(f"the array after shuffle 2row : \n {random}")

print('----------------------------------' '\n')
# We can create array of numbers which draws samples
# from normal distribution, or more commonly called
# a bell curve, this function take 3 arguments, first is
# the mean or canter of distribution, second is the
# standard deviation or dpread of the data from the mean, the
# last argument is the shape of resulting array

print(np.random.normal(50, 15, (3, 4)))
print('+++++++++++++++++++++++++++++')
# we can creat array with negative array's value
b = np.random.randn(3,2,4)
print(b)
print(b.shape)
