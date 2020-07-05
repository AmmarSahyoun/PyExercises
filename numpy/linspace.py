# The numpy linspace function returns evenly spaced numbers
# based on a specified interval
import numpy as np

# the default number of samples in the result is set to 50
# however we are able to change this value by adding argument
numbers = np.linspace(0, 10)
print(type(numbers))
print(numbers, '\n')

new_numbers = np.linspace(0, 10, num=5)
print(new_numbers)

# The ability to include or exclude the ending
# value from the result is another difference between
# the linspace and arange functions, because
# the arange function does not include the ending value

print('-------------------------')
# if we want to determine the step size between each sample
# in the aray, we add argument retstep=True

last = np.linspace(0, 10, retstep=True)
print(type(last))
print(last)

# Note that the type now become tuple which contains a
# numpy array with the equally spaced samples and a
# float which is the step size between each sample