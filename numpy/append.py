# the numpy append function aööows us to add
# new values to the end of an existing numoy array

# this function returns a copy of the existing array
# with the values appended to the specified axis
import numpy as np

numbers = np.arange(9)
print(numbers, '\n')
print(np.append(numbers, 9.1), '\n')
# it does not modify the oriuginal aray
print(numbers, '\n')

# to add more than one value to the number array we have
# a few options: we can pass a tuple with the value
# of 9 and 10 seperated by s comms to the second argument

print(np.append(numbers, (9.1, 5)), '\n')

# the second option is to pass the same values within a list

print(np.append(numbers, [111, 9.1, 5]), '\n')

# we need 2D array to append values to it
numbers_2d = numbers.reshape(3, 3)
# the shape automatic change when we add single number or tuple
print(np.append(numbers_2d, 5), '\n')

print(np.append(numbers_2d, (5, 22)), '\n')

# But if we add 2d array it would be added as a 4th row/column
print(np.append(numbers_2d, [[9, 10, 11]], axis=0),'\n')
print(numbers_2d)

