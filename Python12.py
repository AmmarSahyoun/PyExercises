from numpy import *

# create list contained nested lists
d = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
print(d)
t = array(d)  # cast to numpy array
print('numpy array that does not conatin comma: \n', t)
print('dimension is :', t.ndim)
print('the shape is:', t.shape)
print('the size is :', t.size)
print("===================================")
# define a numpy array
A = array([[0, 1, 1], [1, 0, 1]])
B = array([[1, 1], [1, 1], [-1, 1]])
# perform matrix mltiolication
c = dot(A, B)
print(c)
print('====================')
X = array([[1, 0], [0, 1]])
Y = array([[2, 1], [1, 2]])
Z = dot(X, Y)
print(Z)
