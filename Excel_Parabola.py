def parabola(x):
    y = x ** 2
    return y


for value in range(-5, 6):
    squared = parabola(value)
    print('{} i kvadrat är {:2d}'.format(value, squared))
