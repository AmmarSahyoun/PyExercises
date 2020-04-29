from numpy import *

# create list contained nested lists
d = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
print('First step create list', type(d))
print(d)
t = array(d)  # cast to numpy array 'matrix'
print('numpy array that does not contain comma: \n', t)
print('matrix dimension is :', t.ndim)
print('the matrix shape is:', t.shape)
print('the matrix size is :', t.size)
print('=========DOT multiplication===========')
# define a numpy array
A = array([[0, 1, 1], [1, 0, 1]])
B = array([[1, 1], [1, 1], [-1, 1]])
# perform numpy array multiplication
c = dot(A, B)
print(A, '* \n', B, '=\n', c)
print('*******************************')
X = array([[1, 0], [0, 1]])
Y = array([[2, 1], [1, 2]])
Z = dot(X, Y)
print(X, '*\n', Z, '=\n', Z)
print('++++++++Create 3D list and cast to numpy array +++++++++')
f = [[['what', 'is'], ['your', 'name']], [['what', 'is'], ['your', 'age']], [['where', 'do'], ['you', 'live']]]
g = array(f)
print(g)
print(g.ndim)
print(g.size)
print(g.shape)
print('++++++Create conditional list and cast to numpy array +++++++')
p1 = [range(i, i + 4) for i in [3, 5]]
p2 = [range(i, i + 3) for i in (1, 4)]
pp1 = array(p1)
pp2 = array(p2)
print('this is list p1: ', type(p1))
print('this is array pp1 type:', type(pp1))
