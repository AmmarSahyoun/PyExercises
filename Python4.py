print(int(True))
x = 4
x = x / 2
print(x)

# replace
a = " the table is in the kitchen"
print(a.upper())
b = a.replace("table", "chair")
print(b)

# find the start of the phrase index
q = "hello Mike"
print(q.find("Mike"))

c = "01234567"
print(c[::2])

s = str(1) + str(1)
print(s)

# Tuples
r = (1, 2, 4, 9, 5, 0)
e = "Ammar", "Elderes"
print(r + e)

# to sort a tuple, assign it to another variable
w = sorted(r)
print(w)

# lists
B = [1, 2, [3, 'a'], [4, 'b']]
print(B[3][1])
print()

d = [1]
d.append([2, 3, 4, 5])  # add one element
print(d)
d.extend([6, 7, 8])  # add many elements
print(d)

cloned = d[:]  # creatte cloned list from a list d
d[1] = "cloned"
print(d)
print(cloned)

string = "   i am learning AI these days"
print(string.split())
