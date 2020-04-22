from numpy import *


a = sin(30 * pi / 180)
b = cos(30 * pi / 180)
c = tan(30 * pi / 180)
# convert fromradius To Degree  pi/180
print(a)
print(b)
print(c)
print('======================')
r = round(3.6546548)
print(r)
t = round(3.45679999)
print(t)
y = round(3, 5444444)
print(y)
print('======================')

q = floor(3.68525)  # up round
w = ceil(3.68525)  # down round
print(q)
print(w)
print('======================')

p = power(2, 3)
m = mod(20, 7)  # same as % rest of division
print(p, '\n', m)
# to check if 135 accept division by 5 we write
# (135 % 5) = 0
print('======================')

a = ["0", 1, "two", "3", 4]
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print('======================')

# Create a numpy array
a = array([0, 1, 2, 3, -2])
print('numpy array has no comma between elements', a)
print("a[0]:", a[0])
a[1] = 100
print('change second element', a)
print("a[-1]:", a[-1])
print('type is:', a.dtype)
print('size is:', a.size)
print('dimension is:', a.ndim)
print('the biggest value:', a.max())
print('the smalest value:', a.min())

