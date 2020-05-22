# name = input('enter your name: ')
# age = int(input('Enter your age: '))
# if 35 > age > 18:
#     print('welcome {}, you are young'.format(name))
# if age < 18:
#     print('welcome {}, you are junior'.format(name))
# else:
#     print('welcome {}, you are Senior'.format(name))

# for i in range(0,10):
#     print(i)

# a = ('my', ' name', ' is ', 'Deres')
# b = ''.join(a).casefold()  # small letter
# c = ''.join(a).capitalize()
# print(b, '\n', c, '\n',c.upper())

# print(14%11)

# for i in range(1, 100, 7):
#     print(i)
#     if i%11 == 0:
#          break

#
from numpy import *

# a = [range(i, i+3) for i in[2, 4, 6]]
# print(a)
# b = array(a)
# print(b)
#
a = eye(5)
print(a)

b = linspace(0, 30)
print(b)

f = diag(array([5, 6, -2, 2, 5, -7, 8]))
print(f)
print('-'*30)
f = diag(array([5, 6, -2, 2, 5, -7, 8]), k=3)
print(f)
