from numpy import *
import time
import sys
import matplotlib.pyplot as plt
# %matplotlib inline

def Plotvec1(u, z, v):
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


def Plotvec2(a, b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


u = array([1, 0])
v = array([0, 1])
z = u + v
print(u, v, z)
print(Plotvec1(u, z, v))
print("==========[1 2]=====[3 2]==========")
u = array([1, 2])
v = array([3, 2])
print('u*v = ', u * v)
print('dot represent how similar are the vectors:', dot(u, v))
l = array([-5, 2, 3, 4, -1])
print(l + 1)

# create the numpy array in radians
x = array([0, pi / 2, pi])
print('numpy array in radiand', x)
h= sin(x)
print(h)
#Makeup a numpy array within [-2, 2] and 5 elements
j = linspace(-2, 2, num=5)
print(j)
print("=========================================")
# Makeup a numpy array within [0, 2π] and 100 elements
x = linspace(0, 2*pi, num=100)
print(x)
y = sin(x)
print(y)
print(plt.plot(x,y))
