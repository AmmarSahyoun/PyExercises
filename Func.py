# def greet(name):
#     print('ahla ' + name)
#
#
# greet('el Lubna')
# print((greet('May')))


def absolute(num):
    if num >= 0:
        return num
    else:
        return - num
print(absolute(2))
print(absolute(-4))

balance = -132
distance_fromZero = absolute(balance)
print(absolute(balance))