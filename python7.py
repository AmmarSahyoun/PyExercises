age = input("Enter your age:")

if int(age) > 18:
    print("you can enter the Bar")
elif age == 18:
    print("Coca-Cola")
else:
    print("welcome to drink cola")
print("out loop")

x = 5
while x != 2:
    print(x)
    x -= 1

a = 1


def do(x):
    a = 100
    return (x + a)


print(do(1))

print("=" * 10)


def add(x):
    return (x + x)


print(add(1))
print("====================")


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, 'y=', self.y)


print("====================")


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p1 = Points(1, 2)
p1.print_point()

print("====================")


class Points(object):  # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):  # function
        print('x=', self.x, ' y=', self.y)


p2 = Points(1, 2)

p2.x = 2

p2.print_point()
