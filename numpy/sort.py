import numpy as np

a = np.array([[6, 5, 4], [3, 2, 1]])
print(a, '\n')
print('--------------')
# note the values have only been sorted within each row and
# the order of the rows within the 2D arra yhas now changed
# this is because by default axis = -1
print(np.sort(a), '\n')
print(np.sort(a, axis=-1), '\n')
print('--------------')
print(' the axis = 0')
print(np.sort(a, axis=0), '\n')
print('--------------')
print(' the axis = 1')
print(np.sort(a, axis=1), '\n')
print('--------------')
print(' the axis = None')
print(np.sort(a, axis=None), '\n')
print('+++++++++++++++++++++++++++++++++++++++')
# We will define a variable and set this equal tp list that contains tuple with
# two values first name s10; this define the name of the field and corresponding
# data type *String of 10, String of 10 or integer
dtype = [('firstName', 'S10'), ('lastName', 'S12'), ('age', int)]
values = [('John', 'Smith', 57), ('Sarah', 'Ahmed', 33), ('Allison', 'Anderson', 64)]
a = np.array(values, dtype=dtype)
# this create a structures array with the values and data types defined above
print(np.sort(a, order='firstName'), '\n')
print(np.sort(a, order='age'), '\n')
print(np.sort(a, order=['lastName', 'firstName']), '\n')

#  the numpy argsort function is used to return the indiced than
#  can be used to sort an array
